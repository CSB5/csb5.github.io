---
layout: post
title: Constructing Consensus Sequences, Fast
description: We designed a new algorithm for finding consensus of multiple DNA sequences, which operates in linear time with respect to the length of the consensus.
image: https://www.biorxiv.org/content/biorxiv/early/2025/04/21/2025.04.16.644694/F2.large.jpg?width=800&height=600&carousel=1
date: 2025-02-13
tags: [Algorithms, Metagenomic Technologies]
preprint: https://www.biorxiv.org/content/10.1101/2025.04.16.644694v1
code: https://github.com/GZHoffie/bbs
author: zhenhao
---


Finding consensus of multiple DNA sequences has been an important and well-studied problem. Fast and accurate algorithms are critical in the workflow of (metagenomic) genome assembly, variant calling, and most recently, *trace reconstruction* in DNA data storage systems.

![](/images/posts/2025-02-13-finding-consensus-sequences/dna-storage-workflow.png)
*Typical workflow of a DNA data storage system.*

Current reconstruction algorithms typically rely on pairwise or multiple sequence alignment, whose results depend heavily on the chosen alignment scoring metrics.

![](https://www.biorxiv.org/content/biorxiv/early/2025/04/21/2025.04.16.644694/F1.large.jpg?width=800&height=600&carousel=1)
*Different scoring metrics may yield different MSA.*

However, it is well known that the sequencing error rate may vary within each read and across different datasets [[1]](#1). Finding the optimal scoring scheme that accomodates all these variations is not easy.

We therefore propose a new problem definition. Instead of assuming the error rates and finding the optimal alignment, we imagine that the sequences are observations of an unknown generative model, and try to **predict the most probable next observation of the model**. Under certain assumptions, we can show that the consensus is indeed the most probable next observation.

![](/images/posts/2025-02-13-finding-consensus-sequences/problem_definition.png)

In this work, we assume the model to be a *k*-th order Markov chain, whose parameters can be easily learned via *k*-mer counting. The parameters essentially encodes the **position-specific error rates**, making the alignment highly accurate. A novel algorithm, *Bidirectional Beam Search* (BBS), is used to infer the most probable output.

![](https://www.biorxiv.org/content/biorxiv/early/2025/04/21/2025.04.16.644694/F2.large.jpg?width=800&height=600&carousel=1)


Our algorithm takes linear time with respect to the length of the consensus, making it asymptotically faster than the other algorithms, while achieving top-tier accuracy.

![](/images/posts/2025-02-13-finding-consensus-sequences/time-usage.png)

![](/images/posts/2025-02-13-finding-consensus-sequences/real-datasets.png)

Finally, the *k*-th order Markov chain also outputs a joint probability of observing the consensus sequence, which can be used to calculate a confidence score to judge whether the output consensus sequence is reliable or not, aiding in building a fast and reliable consensus finding workflow.

![](https://www.biorxiv.org/content/biorxiv/early/2025/04/21/2025.04.16.644694/F7.large.jpg?width=800&height=600&carousel=1)


# References

<a id="1">[1] </a> Antkowiak, Philipp L., et al. "Low cost DNA data storage using photolithographic synthesis and advanced information reconstruction and error correction." <i>Nature communications</i> 11.1 (2020): 5345.