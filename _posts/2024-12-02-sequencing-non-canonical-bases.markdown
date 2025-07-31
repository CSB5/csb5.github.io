---
layout: post
title: High-throughput Deconvolution of Non-canonical Bases
description: We developed a fast and accurate DNA sequencing method that reads canonical and non-canonical bases using AI and nanopore technology. Enabling an expanded genetic alphabet for use in data storage, nucleic acid therapeutic, and synthetic biology.
image: '/images/posts/2024-12-02-sequencing-non-canonical-bases.markdown/XNA_Basecaller_Overview.png'
image_caption: DNA containing non-canonical bases can be directly sequenced using nanopore devices and AI
date: 2024-12-02
tags: [Metagenomic Technologies, AI & ML, Synthetic Biology, Nanopore]
paper: https://doi.org/10.1038/s41467-025-62347-z
publication: Nature Communications
code: https://github.com/CSB5/XNA_Basecaller/
author: [mauricio, nok, rafael, niranjan]
---

Excited to share our latest work, where we show how to achieve high-throughput sequencing of DNA containing non-canonical bases using nanopore sequencing and de novo basecalling enabled by spliced-based data-augmentation. 


The inability to read XNAs in a direct manner was a significant limitation for xenobiology. Here we demonstrate that XNA-containing templates can be directly sensed using a MinION sequencer to generate unique signals that can be deconvoluted by a specialized basecaller model.

![](https://pbs.twimg.com/media/GeBP7QRa0AMtMR8?format=jpg&name=medium)

We validated that the Nanopore sequencer is capable of processing XNAs containing the Px-Ds unnatural base pair and assessed the distinguishability of their measured signals versus DNA control and the canonical bases.

![](https://pbs.twimg.com/media/GeBQkZ2a0AMBbcs?format=jpg&name=4096x4096)

![](https://pbs.twimg.com/media/GeBQkZ2a0AIRfM-?format=png&name=900x900)

To obtain a ML model that can deconvolve these signals and basecall UBs along with natural bases, we developed an enzymatic framework to synthesize with high XNA purity (>90%) a library of 1,024 UB-containing oligonucleotides representing all 6,144 single-UB 6-mer contexts.

![](https://pbs.twimg.com/media/GeBROD9a0AEQYZH?format=jpg&name=4096x4096)

![](https://pbs.twimg.com/media/GeBRPhna0AE2qpn?format=jpg&name=medium)

We leveraged our library by employing our data-augmentation technique based on splicing XNA/DNA signals to generate reads containing UBs in all contexts. Using these reads we trained a generalizable model capable of sequencing UBs with high accuracy (>80%) and specificity (99%).

![](https://pbs.twimg.com/media/GeBR0RyaEAAHjPI?format=jpg&name=medium)

![](https://pbs.twimg.com/media/GeBR0OCa0AUTnG2?format=jpg&name=medium)