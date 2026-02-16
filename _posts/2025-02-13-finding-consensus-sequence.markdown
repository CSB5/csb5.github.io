---
layout: post
title: Fast reconstruction of consensus sequences
description: We designed a new algorithm for finding consensus of multiple DNA sequences, which operates in linear time with respect to the length of the consensus.
image: /images/posts/2025-02-13-finding-consensus-sequences/logo.png
image_caption: Beam Search lights up the way.
date: 2025-02-13
tags: [Metagenomic Tech]
paper: https://www.cell.com/iscience/fulltext/S2589-0042(25)02052-8
publication: iScience
code: https://github.com/GZHoffie/bbs
author: [gu-zhenhao, niranjan-nagarajan]
---


Finding consensus of multiple DNA sequences has been an important and well-studied problem. Fast and accurate algorithms are critical in the workflow of (metagenomic) genome assembly, variant calling, and most recently, *trace reconstruction* in DNA data storage systems.

![](/images/posts/2025-02-13-finding-consensus-sequences/dna-storage-workflow.png)
*Typical workflow of a DNA data storage system.*

Current reconstruction algorithms typically rely on pairwise or multiple sequence alignment, whose results depend heavily on the chosen alignment scoring metrics.

![](/images/posts/2025-02-13-finding-consensus-sequences/alignment_example.jpg)
*Different scoring metrics may yield different MSA.*

However, it is well known that the sequencing error rate may vary within each read and across different datasets [[1]](#1). Finding the optimal scoring scheme that accommodates all these variations is not easy.

We therefore propose a new problem definition. Instead of assuming the error rates and finding the optimal alignment, we assume that the sequences are observations of an unknown generative model, and try to **predict the most probable next observation of the model**.

![](/images/posts/2025-02-13-finding-consensus-sequences/problem_definition.png)
*The most probable next observation is regarded as the consensus.*

In this work, we assume the model to be a *k*-th order Markov chain, whose parameters can be easily learned via *k*-mer counting. The parameters essentially encodes the **position-specific error rates**, making the alignment highly accurate. A novel algorithm, *Bidirectional Beam Search* (BBS), is used to infer the most probable output.

![](/images/posts/2025-02-13-finding-consensus-sequences/workflow.jpg)


Our algorithm takes linear time with respect to the length of the consensus, making it asymptotically faster than the other algorithms, while achieving top-tier accuracy.

![](/images/posts/2025-02-13-finding-consensus-sequences/time-usage.png)

![](/images/posts/2025-02-13-finding-consensus-sequences/real-datasets.png)

Finally, the *k*-th order Markov chain also outputs a joint probability of observing the consensus sequence, which can be used to calculate a confidence score to judge the correctness of output consensus sequences, aiding in building a fast and reliable consensus finding workflow.

![](https://www.biorxiv.org/content/biorxiv/early/2025/04/21/2025.04.16.644694/F7.large.jpg?width=800&height=600&carousel=1)


# References

<a id="1">[1] </a> Antkowiak, Philipp L., et al. "Low cost DNA data storage using photolithographic synthesis and advanced information reconstruction and error correction." <i>Nature communications</i> 11.1 (2020): 5345.
