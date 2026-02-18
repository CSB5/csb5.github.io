---
layout: post
title: Estimating sequencing error rates, without alignment
description: We developed a new tool that aims to perform quality control of a set of reads, without relying on mapping results or quality scores.
image: '/images/posts/2026-02-14-estimating-sequencing-error/thumbnail.png'
date: 2026-01-20
tags: [Metagenomic Tech]
preprint: https://www.biorxiv.org/content/10.64898/2026.02.12.705514v1
code: https://github.com/GZHoffie/skiver
author: [gu-zhenhao, niranjan-nagarajan]
---

Given a set of sequenced reads, how can we determine if the sequencing run is good or not? Finding the quality of the reads, which includes estimating sequencing error rates and bias, has been an important first step in numerous Bioinformatics pipelines.

Previous ways of estimating sequencing error rates include **mapping the reads** to reference genomes and inferring error rates from **Phred quality scores**. Reference genomes may however be missing or different from the genomes that are actually sequenced, especially in metagenomic samples. On the other hand, Phred quality scores can produce biased estimates if they are uncalibrated.

We therefore propose a new framework for estimating sequencing error and bias, called *skiver*, which works without the need for reference genome or relying on Phred scores. 

![](/images/posts/2026-02-14-estimating-sequencing-error/workflow.png)
*Workflow of skiver.*

The key ideas in *skiver* is to use (*k*, *v*)-mer sketches to represent the large amount of sequencing reads. A (*k*, *v*)-mer is a segment of length *k*+*v*, where the first *k* bases are the *key* and the last *v* bases are the *value*. By grouping the (*k*, *v*)-mers with the same key together, we can identify the consensus value, as well as estimate the frequency of sequencing errors.

Experiments on various real datasets show that skiver is able to accurately estimate the sequencing error rate and infer the percentage of *k*-mers in the read set that are free of sequencing errors. In addition, skiver can estimate the substitution, insertion, and deletion rates, revealing the biases of various sequencing platforms.

![](/images/posts/2026-02-14-estimating-sequencing-error/results.png)
*Skiver's estimation of error rates and error spectra on various metagenomic samples.*

Finally, skiver is computationally lightweight, making it a handy tool for quality control in modern Bioinformatic pipelines.

![](/images/posts/2026-02-14-estimating-sequencing-error/computational_resources.png)
*Computational resources needed by skiver and other baselines.*
