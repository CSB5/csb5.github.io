#!/usr/bin/env python3
"""
Download a Google Scholar profile and summarize publications to YAML.

Outputs one YAML item per publication with:
- title
- authors (list)
- keywords (list, from Crossref 'subject' when available)
- doi (normalized https://doi.org/... link if found)

Usage:
  python scholar_to_yaml.py --user <SCHOLAR_USER_ID> -o profile.yml
  python scholar_to_yaml.py --url  "https://scholar.google.com/citations?user=XXXX" -o profile.yml

Notes:
- Be gentle and respect Google Scholar's ToS. This uses 'scholarly', which includes delays,
  but you should still avoid hammering. Consider running behind a stable IP and at low volume.
- Crossref lookups are best-effort fuzzy matches on title (+year when available).
"""

import argparse
import re
import sys
import time
from typing import Any, Dict, List, Optional, Tuple

import requests
import yaml
from rapidfuzz import fuzz, process  # fast, dependency-light fuzzy matching
from scholarly import scholarly  # pip install scholarly

CROSSREF_URL = "https://api.crossref.org/works"
USER_AGENT = "scholar-to-yaml/1.0 (mailto:youremail@example.com)"  # <-- change to your contact
MAX_ROWS = 5  # how many Crossref candidates to fetch per title
SLEEP_BETWEEN_CROSSREF = 0.4  # seconds
SLEEP_BETWEEN_SCHOLAR = 0.2  # seconds
TITLE_MATCH_THRESHOLD = 90  # fuzzy title score threshold to accept a candidate


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Export Google Scholar profile to YAML.")
    src = p.add_mutually_exclusive_group(required=True)
    src.add_argument("--user", help="Google Scholar user id (e.g., 'XXXXYYYYZZZ').")
    src.add_argument("--url", help="Full Google Scholar profile URL containing '?user=...'.")
    p.add_argument("-o", "--output", default="profile.yml", help="Output YAML file.")
    p.add_argument("--max-pubs", type=int, default=None, help="Limit number of publications (debug/testing).")
    return p.parse_args()


def extract_user_id_from_url(url: str) -> Optional[str]:
    m = re.search(r"[?&]user=([^&]+)", url)
    return m.group(1) if m else None


def fetch_author(user_id: str) -> Dict[str, Any]:
    # scholarly.search_author_id is the most direct
    author = scholarly.search_author_id(user_id)
    author = scholarly.fill(author, sections=["basics", "indices", "publications"])
    return author


def fill_publication(pub: Dict[str, Any]) -> Dict[str, Any]:
    # Fetch full details for each publication (title, authors, year, etc.)
    try:
        pub_filled = scholarly.fill(pub)
    except Exception:
        # Sometimes a pub may fail to fill; return minimal info
        pub_filled = pub
    return pub_filled


def norm_title(t: str) -> str:
    return re.sub(r"\s+", " ", t or "").strip().lower()


def crossref_lookup(title: str, year: Optional[int]) -> Tuple[Optional[str], List[str]]:
    """
    Returns (doi_url_or_none, keywords_list)
    """
    if not title:
        return None, []

    params = {
        "query.title": title,
        "rows": MAX_ROWS,
        "select": "DOI,title,author,subject,issued,container-title",
        # Crossref will consider many fields; we focus on titles and subjects
    }
    headers = {"User-Agent": USER_AGENT}
    try:
        r = requests.get(CROSSREF_URL, params=params, headers=headers, timeout=20)
        r.raise_for_status()
        data = r.json()
    except Exception:
        return None, []

    items = data.get("message", {}).get("items", [])
    if not items:
        return None, []

    # Prepare candidates with a fuzzy match on title (first title string in list)
    query_title = norm_title(title)
    scored: List[Tuple[int, Dict[str, Any]]] = []
    for it in items:
        cand_titles = it.get("title") or []
        cand_title = cand_titles[0] if cand_titles else ""
        score = fuzz.token_set_ratio(query_title, norm_title(cand_title))
        # Prefer matches close in year if provided
        if year:
            try:
                cand_year = it.get("issued", {}).get("date-parts", [[None]])[0][0]
            except Exception:
                cand_year = None
            if cand_year and abs(int(cand_year) - int(year)) <= 1:
                score += 5  # small bonus for year proximity
        scored.append((score, it))

    scored.sort(key=lambda x: x[0], reverse=True)
    best_score, best_item = scored[0]

    if best_score < TITLE_MATCH_THRESHOLD:
        return None, []

    doi = best_item.get("DOI")
    doi_url = f"https://doi.org/{doi}" if doi else None
    keywords = best_item.get("subject") or []
    # Normalize keywords: strip + deduplicate while preserving order
    seen = set()
    kw_norm: List[str] = []
    for k in keywords:
        ks = re.sub(r"\s+", " ", str(k)).strip()
        if ks and ks.lower() not in seen:
            kw_norm.append(ks)
            seen.add(ks.lower())

    return doi_url, kw_norm


def main():
    args = parse_args()
    user_id = args.user
    if args.url:
        user_id_from_url = extract_user_id_from_url(args.url)
        if not user_id_from_url:
            print("Could not extract ?user=... from the provided URL.", file=sys.stderr)
            sys.exit(1)
        user_id = user_id_from_url

    if not user_id:
        print("A Google Scholar user id is required.", file=sys.stderr)
        sys.exit(1)

    # Fetch author + base pubs
    author = fetch_author(user_id)
    author_name = author.get("name", f"user:{user_id}")
    pubs = author.get("publications", []) or []

    if args.max_pubs is not None:
        pubs = pubs[: args.max_pubs]

    results_yaml: List[Dict[str, Any]] = []

    for i, p in enumerate(pubs, 1):
        time.sleep(SLEEP_BETWEEN_SCHOLAR)
        pub_full = fill_publication(p)

        title = pub_full.get("bib", {}).get("title") or pub_full.get("bib", {}).get("citation")
        # Some entries are citations without a clear title; skip if no title
        if not title:
            continue

        # Authors from Scholar are often a string like "A Author, B B. Author, ..."
        authors_field = pub_full.get("bib", {}).get("author") or ""
        if isinstance(authors_field, str):
            # Split by " and " or commas heuristically; Scholar is inconsistent
            # Better: split on comma and strip, then post-process
            raw_authors = [a.strip() for a in re.split(r",| and ", authors_field) if a.strip()]
        elif isinstance(authors_field, list):
            raw_authors = [str(a).strip() for a in authors_field if str(a).strip()]
        else:
            raw_authors = []

        year = None
        y = pub_full.get("bib", {}).get("pub_year") or pub_full.get("bib", {}).get("year")
        try:
            year = int(str(y)) if y else None
        except Exception:
            year = None

        # Crossref best-effort DOI + keywords
        doi_url, keywords = crossref_lookup(title, year)
        time.sleep(SLEEP_BETWEEN_CROSSREF)

        item = {
            "title": title,
            "authors": raw_authors,
            "keywords": keywords or [],
            "doi": doi_url,  # can be None
        }
        results_yaml.append(item)
        print(f"[{i}/{len(pubs)}] {title[:70]}{'...' if len(title)>70 else ''} -> DOI: {doi_url or 'N/A'}")

    # Write YAML
    # Structure: a list of publications under a top-level author key (optional).
    out_doc = {
        "scholar_user": user_id,
        "author_name": author_name,
        "publications": results_yaml,
    }
    with open(args.output, "w", encoding="utf-8") as f:
        yaml.safe_dump(out_doc, f, allow_unicode=True, sort_keys=False)

    print(f"\nWrote {len(results_yaml)} items to {args.output}")


if __name__ == "__main__":
    main()