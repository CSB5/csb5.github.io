---
layout: post
title: High-throughput deconvolution of non-canonical bases
description: We developed a fast and accurate DNA sequencing method that reads canonical and non-canonical bases using AI and nanopore technology. Enabling an expanded genetic alphabet for use in data storage, nucleic acid therapeutic, and synthetic biology.
image: '/images/posts/2024-12-02-sequencing-non-canonical-bases.markdown/XNA_Basecaller_Overview.png'
image_caption: DNA containing non-canonical bases can be directly sequenced using nanopore devices and AI
date: 2024-12-02
tags: [Metagenomic Tech]
paper: https://doi.org/10.1038/s41467-025-62347-z
publication: Nature Communications
code: https://github.com/CSB5/XNA_Basecaller/
author: [mauricio, nok, rafael, niranjan]
---

&emsp;We are excited to share our latest work published in Nature Communications. In this paper, we show how to achieve high-throughput sequencing of DNA containing non-canonical bases (NCB) using nanopore sequencing and de novo basecalling enabled by spliced-based data-augmentation.

&emsp;The inability to read XNAs in a direct manner was a significant limitation for xenobiology. Here we demonstrate that XNA-containing templates can be directly sensed using a MinION sequencer to generate unique signals that can be deconvoluted by a specialized basecaller model.

![Overview of workflow](/images/posts/2024-12-02-sequencing-non-canonical-bases.markdown/1-paper_overview.png)
*Figure: Overview of workflow, showing the synthesis of XNA templates containing non-canonical basepairs, nanopore sequencing, signal-level analysis and direct deconvolution of canonical and non-canonical bases.*

&emsp;We validated that the Nanopore sequencer is capable of processing XNAs containing the Px-Ds unnatural base (UB) pair and assessed the distinguishability of their measured signals versus DNA control and the canonical bases.

<div align="center">
  <img height="260" alt="Comparing average signal level" src="/images/posts/2024-12-02-sequencing-non-canonical-bases.markdown/2-lineplot_level_comparison.png"/>
  <img height="260" alt="Average signal fold-change" src="/images/posts/2024-12-02-sequencing-non-canonical-bases.markdown/3-signal_fold_changes-nat_bases-mean-boxplot-per_target_agg_kmer-XNA20-pub_ver.png"/>
</div>

&emsp;To obtain a machine learning model that can deconvolve these signals and basecall UBs along with natural bases, we developed an enzymatic framework to synthesize with high XNA purity (>90%) a library of 1,024 UB-containing oligonucleotides representing all 6,144 single-UB 6-mer contexts.

<div align="center">
  <img height="260" alt="XNA synthesis process" src="/images/posts/2024-12-02-sequencing-non-canonical-bases.markdown/4-synthesis_framework.png"/>
  <img height="260" alt="Ds insertion efficiency" src="/images/posts/2024-12-02-sequencing-non-canonical-bases.markdown/5-insertion_efficiency_per_pool.png"/>
</div>

*Figure: Schematic overview of XNA synthesis process, via enzymatic single-nucleotide insertion of Ds. Two alternative strategies were explored, a 31-mer (Pa) and a 20-mer (mini-hairpin) template.*

&emsp;We leveraged our library by employing our data-augmentation technique based on splicing XNA/DNA signals to generate reads containing UBs in all contexts. Using these reads, we trained a generalizable model capable of sequencing UBs with high accuracy (>80%) and specificity (99%).

<div align="center">
  <img height="350" alt="Performance of the final model" src="/images/posts/2024-12-02-sequencing-non-canonical-bases.markdown/6-per_per_ctx-POC_with_CPLX-iter_samp-train_only.png"/>
  <img height="350" alt="Basecalling confusion matrix" src="/images/posts/2024-12-02-sequencing-non-canonical-bases.markdown/7-confusion_matrix-XNA20_v2-split_model-full_read.png"/>
  <br>
  <em> Figure: (Left) Performance of the final model, based on the complex and proof-of-concept libraries for testing with diverse templates and held-out reads. (Right) Basecalling confusion matrix for NCBs and canonical bases. The last column represents deletion errors.</em>
  <br><br>
</div>



