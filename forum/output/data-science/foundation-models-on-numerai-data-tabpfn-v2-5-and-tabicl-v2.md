---
title: "Foundation Models on Numerai Data: TabPFN v2.5 and TabICL v2"
category: Data Science
url: https://forum.numer.ai/t/foundation-models-on-numerai-data-tabpfn-v2-5-and-tabicl-v2/8269
created_at: 2026-03-30T15:07:57.340000+00:00
last_posted_at: 2026-03-30T15:07:57.416000+00:00
posts_count: 1
views: 97
tags: []
---

# Foundation Models on Numerai Data: TabPFN v2.5 and TabICL v2

---

### Post #1 — **degerhan** | 2026-03-30 15:07 UTC

In the quest for mmc, I wanted to experiment with TabPFN v2.5 and TabICL v2, foundation models for tabular data and about as different from gradient-boosted trees as you can get.

Neither works at Numerai scale, so the idea was to use them as _teachers_ to generate pseudo-labels, then train lightweight tree _students_ to replicate the predictions for inference.

TL;DR : it didn’t work. But the experiment was clean enough to be worth sharing.

_Case for optimism:_ TabPFN and TabICL process the entire training context through attention. Even if raw accuracy is mediocre, the _shape_ of the prediction function should be different.

_Case for skepticism:_ Numerai correlations are ~0.03. With a training window of ~100 eras subsampled to 20k - 40k rows, the teacher sees extremely weak signal relative to noise. These foundation models were validated on datasets where features actually predict the target. Numerai is not that.

## What I (we?) Built

### Phase 1: Teacher Predictions (Colab A100)

The pipeline runs as a Colab notebook, rolling one era at a time from ~400 to ~1200:

  1. Gather training rows from the previous 100 eras (with a 4-era embargo)
  2. Subsample 20k rows for TabPFN, 40k for TabICL (it handles more)
  3. Split 2,748 features into 10 disjoint groups of ~275 each (hash-based)
  4. For each group: predict the current era of ~6-7k rows
  5. Save a parquet per (era, group)



100 recent eras gives the teacher a rolling two-year window without exceeding row limits. Disjoint groups of ~275 features sit in TabPFN’s comfort zone. Same row sample across all groups for a given era, so signal diversity comes from the feature subsets, not the row sample.

Both models ran on identical data. TabICL is about 10x faster.

### Phase 2: Distillation

The plan was to train CatBoost and LightGBM students on the pseudo-labels. Seeing the teacher scores, I aborted.

## Results

Scored against `target_ender_20` on eras 679 to 1175 (same window as my other walk-forward experiments).

**TabICL v2** (mean across 10 feature groups):

| NC | CC | Payout  
---|---|---|---  
Mean | 0.0039 | 0.0012 | 0.0057  
Best group (g7) | 0.0050 | 0.0013 | 0.0066  
Worst group (g5) | 0.0030 | 0.0005 | 0.0033  
  
**TabPFN v2.5** (mean across 10 feature groups):

| NC | CC | Payout  
---|---|---|---  
Mean | 0.0010 | -0.0002 | 0.0004  
Best group (g7) | 0.0015 | 0.0003 | 0.0018  
Worst group (g6) | 0.0000 | -0.0013 | -0.0029  
  
TabICL has directionally positive signal across all groups. TabPFN did worse, possibly because it only had half the rows.

A tree model trained directly on `target_ender_20` with my usual pipeline gets NC ~0.0170 and CC ~0.0070. Almost an order of magnitude stronger.

With predictions this weak, I figured distilled students would inherit noise, not signal. The whole premise was that the teacher’s different inductive bias would produce orthogonal predictions worth ensembling. If the teacher can barely find signal, there’s nothing to distill.

Could there be a bug? Sure. Is the windowing or subsampling suboptimal? Most definitely. Do these models just not work at Numerai’s signal-to-noise ratio? That’s my best guess.

## Things to think about

  * **More rows might help.** The models can supposedly handle 100k to 500k rows, but I stayed conservative given my Colab memory and duration constraints.
  * **Other targets.** I only tried `target_ender_20`. Others may work better.
  * **Licensing.** I scratched a technical curiosity itch and did not get to the point of thinking about whether these models allow teacher-student pipelines, or whether Numerai competition counts as commercial use if you are staking.



## Claude can just do things now

Opus-46 and GPT-52 designed the whole pipeline from a description of the idea and an existing model repo: architecture, Colab notebook (no GPU at home), distillation script, feature grouping, all of it. I reviewed the docs, schlepped data between Colab and my dev machine (only because I didn’t realize an official Colab MCP was out), and looked at the results.

This is still the most interesting part. The experiment didn’t pan out, but going from “I wonder if this would work” to results across two SOTA models, in a few hours of my time (plus ~10 days of wall time for Colab babysitting), is still wild. Enjoying it while the novelty holds.
