---
layout: post
title: Deciphering non-canonical bases in nanopore sequencing data with AI
description: We developed a fast and accurate method for sequencing non-canonical bases, enabling applications in data storage, nucleic acid therapeutics, and synthetic biology.
image: '/images/posts/2024-12-02-sequencing-non-canonical-bases.markdown/XNA_Basecaller_Overview.png'
image_caption: DNA containing non-canonical bases can be directly sequenced using nanopore devices and AI
date: 2024-12-02
tags: [Metagenomic Tech]
paper: https://doi.org/10.1038/s41467-025-62347-z
publication: Nature Communications
code: https://github.com/CSB5/XNA_Basecaller/
author: [mauricio-lisboa-perez, chayaporn-suphavilai, rafael-peres-da-silva, niranjan-nagarajan]
---

&emsp;We are excited to share our latest work published in [Nature Communications](https://www.nature.com/articles/s41467-025-62347-z). In this work, we show how to achieve high-throughput sequencing of DNA containing non-canonical bases (NCBs) using nanopore sequencing and de novo basecalling enabled by splicing-based data-augmentation.

&emsp;The inability to read non-canonical bases in a direct manner has been a significant limitation for applications in data storage, nucleic acid therapeutics, and synthetic biology. Here we demonstrate that such bases can be directly analyzed using a MinION sequencer to generate unique signals that can be deconvoluted by a specialized basecaller model. 

![Overview of workflow](/images/posts/2024-12-02-sequencing-non-canonical-bases.markdown/1-paper_overview.png)
*Figure: Overview of workflow, showing the synthesis of XNA templates containing non-canonical basepairs, nanopore sequencing, signal-level analysis and direct deconvolution of canonical and non-canonical bases.*

&emsp;We validated that nanopore sequencing throughput is not impacted by NCBs and that there is notable distinguishability of their measured signals versus DNA controls and canonical bases.

&emsp;To obtain a machine learning model that can deconvolve these signals and basecall NCBs along with natural bases, we developed an enzymatic framework to synthesize DNA with high NCB purity (>90%), and generate a library of 1,024 NCB-containing oligonucleotides representing them in diverse sequence contexts.

&emsp;We leveraged our library by employing a data-augmentation technique based on splicing nanopore signals to generate reads containing NCBs in even more diverse contexts. Using these reads, we trained a generalizable model capable of sequencing NCBs with high accuracy (>80%) and specificity (99%).

&emsp;Read all about this novel solution and results in our [scientific paper](https://www.nature.com/articles/s41467-025-62347-z) and check our reproducible code on [GitHub](https://github.com/CSB5/XNA_Basecaller/)!
