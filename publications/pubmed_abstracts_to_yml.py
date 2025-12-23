#!/usr/bin/env python3
"""
Convert a PubMed-style text export into YAML grouped by year.
Parsing is paragraph-based: fields are split by empty lines.
"""

from __future__ import annotations
import argparse
import json
import re
from typing import Dict, List, Optional

try:
    import yaml
    HAVE_YAML = True
except Exception:
    yaml = None
    HAVE_YAML = False


MONTHS = {
    "Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04",
    "May": "05", "Jun": "06", "Jul": "07", "Aug": "08",
    "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12",
}

ENTRY_START_RE = re.compile(r"^\s*(\d+)\.\s", re.MULTILINE)


# ---------- helpers ----------

def split_entries(text: str) -> List[str]:
    starts = [m.start() for m in ENTRY_START_RE.finditer(text)]
    blocks = []
    for i, s in enumerate(starts):
        e = starts[i + 1] if i + 1 < len(starts) else len(text)
        blocks.append(text[s:e].strip())
    return blocks


def normalize_field(s: str) -> str:
    """Remove internal newlines and normalize whitespace."""
    return re.sub(r"\s+", " ", s.replace("\n", " ")).strip()


def parse_journal_date_doi(field: str):
    doi = None
    m = re.search(r"\bdoi:\s*([0-9]+\.[^\s;]+)", field, re.I)
    if m:
        doi = m.group(1).rstrip(".")

    # journal = everything before year
    journal = None
    m = re.search(r"\b(19|20)\d{2}\b", field)
    if m:
        journal = field[:m.start()].strip()

    # date
    pubdate = None
    m = re.search(r"\b((19|20)\d{2})\s+([A-Z][a-z]{2})(?:\s+(\d{1,2}))?", field)
    if m:
        y = m.group(1)
        mon = MONTHS.get(m.group(3))
        d = m.group(4)
        if mon and d:
            pubdate = f"{y}-{mon}-{int(d):02d}"
        elif mon:
            pubdate = f"{y}-{mon}"
        else:
            pubdate = y
    else:
        m = re.search(r"\b((19|20)\d{2})\b", field)
        if m:
            pubdate = m.group(1)

    return journal, pubdate, doi


def clean_authors(field: str) -> List[str]:
    parts = [p.strip() for p in field.split(",") if p.strip()]
    authors = []
    for p in parts:
        p = re.sub(r"\([^)]*\)", "", p)  # remove affiliations/markers
        p = re.sub(r"\s+", " ", p).strip().rstrip(".")
        if p:
            authors.append(p)
    return authors


def extract_abstract(fields: List[str]) -> str:
    """
    Abstract is typically the first long paragraph after affiliations.
    We heuristically take the longest paragraph that doesn't start with
    boilerplate labels.
    """
    candidates = []
    for f in fields:
        if any(f.startswith(x) for x in (
            "Author information", "DOI:", "PMID:", "PMCID:",
            "Conflict of interest"
        )):
            continue
        if len(f) > 200:
            candidates.append(f)

    return max(candidates, key=len) if candidates else ""


def assign_keywords(abstract: str, kwmap: Dict[str, List[str]]) -> List[str]:
    text = abstract.lower()
    hits = []
    for k, triggers in kwmap.items():
        for t in triggers:
            if t.lower() in text:
                hits.append(k)
                break
    return sorted(set(hits))


# ---------- main parser ----------

def parse_entry(block: str, kwmap: Dict[str, List[str]]):
    block = re.sub(r"^\s*\d+\.\s*", "", block)
    raw_fields = re.split(r"\n\s*\n", block)
    fields = [normalize_field(f) for f in raw_fields if f.strip()]

    journal, pubdate, doi = parse_journal_date_doi(fields[0])
    title = fields[1] if len(fields) > 1 else ""
    authors = clean_authors(fields[2]) if len(fields) > 2 else []

    # DOI may appear later
    for f in fields:
        m = re.search(r"\bdoi:\s*([0-9]+\.[^\s;]+)", f, re.I)
        if m:
            doi = m.group(1).rstrip(".")

    abstract = extract_abstract(fields)
    keywords = assign_keywords(abstract, kwmap)

    year = int(pubdate[:4]) if pubdate else None

    return year, {
        "title": title,
        "authors": authors,
        "doi": doi,
        "journal": journal,
        "date": pubdate,
        "keywords": keywords,
    }


def main() -> None:
    """
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True, help="Input PubMed-style .txt file")
    ap.add_argument("--output", required=True, help="Output .yml/.yaml file")
    
    ap.add_argument(
        "--keywords-json",
        default="{}",
        help='JSON dict like {"environmental microbiomes":["hospital","plant"],"gut microbiome":["gut","stool"]}',
    )
    args = ap.parse_args()

    kwmap = json.loads(args.keywords_json)
    if not isinstance(kwmap, dict):
        raise ValueError("--keywords-json must decode to a dict[str, list[str]]")
    """

    kwmap = {
        "environmental microbiomes": ["hospital", "plant", "soil", "water", "environmental"],
        "gut microbiome": ["gut", "stool", "fecal", "intestin", "colon", "gastric"],
        "skin microbiome": ["skin", "dermat", "cutaneous"],
        "cancer genomics": ["cancer", "tumor", "oncology", "carcinoma", "malignancy"],
        "metagenomics": ["metagenomic", "metagenome"],
        "genome assembly": ["assembly", "assembl", "scaffold"],
        "microbiome analysis": ["microbiome", "microbiota", "microbial community"]
    }

    with open("./publications/abstract-NiranjanNa-set.txt", "r", encoding="utf-8", errors="replace") as f:
        text = f.read()

    entries = split_entries(text)
    grouped = {}

    for e in entries:
        year, pub = parse_entry(e, kwmap)
        if year is None:
            continue
        grouped.setdefault(year, []).append(pub)

    yml = [
        {"year": y, "publications": grouped[y]}
        for y in sorted(grouped, reverse=True)
    ]

    with open("./publications/abstract-NiranjanNa-set.yml", "w", encoding="utf-8") as f:
        if HAVE_YAML:
            yaml.safe_dump(yml, f, sort_keys=False, allow_unicode=True)
        else:
            json.dump(yml, f, indent=2, ensure_ascii=False)

    #print(f"Wrote {args.output} ({sum(len(v) for v in grouped.values())} publications)")


if __name__ == "__main__":
    main()