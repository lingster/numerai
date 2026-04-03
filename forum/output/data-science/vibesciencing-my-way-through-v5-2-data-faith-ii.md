---
title: "Vibesciencing my way through v5.2 data (Faith II)"
category: Data Science
url: https://forum.numer.ai/t/vibesciencing-my-way-through-v5-2-data-faith-ii/8214
created_at: 2025-12-28T19:18:02.533000+00:00
last_posted_at: 2026-02-04T14:31:09.129000+00:00
posts_count: 2
views: 681
tags: []
---

# Vibesciencing my way through v5.2 data (Faith II)

---

### Post #1 — **degerhan** | 2025-12-28 19:18 UTC

Four things collided during the long Christmas weekend:

  * My building anxiety over not _sciencing the numerai data_ for a year
  * Faith II v5.2 changes everything (yet again)
  * Codex CLI with gpt-52-xhigh is a beast. It will not let go until it gets stuff done. Biggest improvement to my AI workflows in (checks watch) about four weeks.
  * The Kaggle Grandmasters Playbook (ht [@ia_ai](</u/ia_ai>)) has been begging for attention like a lonely golden retriever.



So I figured, let’s have some fun.

## The Skill

I asked Claude Opus to build a skill based on the [Kaggle Grandmasters Playbook](<https://developer.nvidia.com/blog/the-kaggle-grandmasters-playbook-7-battle-tested-modeling-techniques-for-tabular-data/>).

Here is the [unedited conversation](<https://gist.github.com/degerhan/a26506c7dc8459dc5894c319091dcff1>), including my silly-ass questions and Claude’s thinking traces. I am the “Human” (say it with a Ferengi accent for additional fun).

Claude decided to specialize the [tabular-ml-modeling skill](<https://github.com/degerhan/tabular-ml-modeling/blob/main/tabular-ml-modeling/SKILL.md>) for numerai instead of describing the numerai bits in the prompt. It’s his show, so I went along. Feeling the AGI.

## The Machine

Started with the Kaggle machine (ht [@svendaj](</u/svendaj>), your examples and data rock).

Codex couldn’t find its groove in 30GB of RAM though. So I said what the heck, it’s Christmas, and splurged on a month of Colab Pro+. This got me enough units for roughly 80 hours of a 160GB RAM / A100-80GB instance.

Installed Codex on Colab. Told it to use the skill to solve the numerai problem, and [keep iterating until extraordinary](<https://github.com/degerhan/tabular-ml-modeling/blob/main/numerai_prompt.md>).

## What Happened So Far

Codex got to work. No questions, no hesitation, total confidence. Used the skill, built and ran a bunch of throwaway scripts to explore data, built a pipeline for ensembling XGBoost, CatBoost, LightGBM, and just started cranking.

I got a few hours of sleep (not getting much of that since they doubled the Claude and Codex limits until New Year).

Woke up to see numerai correlation > 0.20 and tmbc > 0.17 in the interim models. After allowing myself to bask in the glory of my prompting skills for a full minute, I copied the Codex training code into a ChatGPT conversation to find the data leak.

Well, not a leak from val to train exactly, but let’s say GroupKFold is not the right way to cut temporal data. Quick search on Discord, update the skill with code from the grandmaster (ht [@shatteredx](</u/shatteredx>)) [TimeSeriesSplitEras](<https://github.com/shatteredx/TimeSeriesSplitEras>).

Oh well, still got plenty of Colab credits. Restart runtime, gave Codex the new skill, it rebuilds its complete pipeline, and starts running.

## That Brings Us to This Morning

Codex finished building the deep XGBoost models on six targets: out-of-fold validation numerai_corr ~0.0330, correlation contribution ~0.0030 (against v52_lgbm_ender20).

It has now moved onto CatBoost, which is taking a long time on a single CPU before each GPU burst. I may need to get in there and adjust some n-threads parameter manually, but I’m letting Codex work through things itself for now.

During the first (failed GroupKFold) run I used a second terminal to work on a different task on Colab. Codex saw it on the process list and freaked out, so I’m giving it its space and not touching anything.

I read Colab Pro+ instances shut down after 24 hours. I’m taking snapshots of the ~/.codex folder every minute, so I’ll restart and resume the conversation if that happens. We’ll see.

It still needs to build the CatBoost and LightGBM models, stack and ensemble them, and if it follows the skill, go back and rebuild models with 100% of the data.

I don’t think my Colab hours will be enough at the rate training is going, but there are enough logs and indicators that it doesn’t need to finish for me to get some value out of this exercise.

I’m not expecting a eureka moment out of this and will post back with whatever happens. Or not, if they happen to be post-human good!

## Are we having fun

I gotta tell you, from not having anything remotely resembling AI agency 10 months ago to watching Codex do its thing is just mindblowing.

**Keep iterating until extraordinary** was the last sentence in Claude’s prompt to Codex. I suppose that’s the dream?

---

### Post #2 — **degerhan** | 2026-02-04 14:31 UTC

**Update**

So Codex finished its run. I took some detours in the interim and deployed models on crowdcent, ncrypto, and nsignals, so this took considerably more wall time than planned.

Its basic finding: ‘you win correlation contribution by producing correct predictions, without building another boosted-tree regressor that converges to the same exposures’. This is perhaps obvious. But it’s nice to also have some action pointers.

**The pattern that worked best:**

  1. Small-feature CatBoost regressions (corr anchors)
  2. Benchmark-residual models (mmc engines)
  3. MLP ranking model (diverse orthogonal signal)
  4. Greedy sparse weights plus mild feature neutralization



**Work left on the table**

I ran out of compute. The obvious to-do list:

  * Expand the small-feature CatBoost runs
  * The ensemble needs corr anchors that aren’t all the same exposure
  * Train more residual benchmark models (more seeds, more subsets)
  * Build an “mmc library” of residual models, let greedy selection pick from it



**Validation**

Walk-forward, no leakage (hyperparams and ensemble weights fitted on train subsets), 480 training plus 160 validation eras, across 3 steps:

  * numerai corr: 0.0171
  * correlation contribution versus ender_20 benchmark: 0.0073



I think these numbers are fine? My guess is they’ll land somewhere in the ballpark of “not embarrassing” when running live. We’ll see.

**Production**

Starting round 1191, I deployed five different ensembles. The best-testing one lives at [degerhan_r19_01](<https://numer.ai/degerhan_r19_01>).

First scores came out yesterday. I was fully prepared to claim victory if they looked good. They did not. So I am now playing the “interim scores don’t matter” card ![:slight_smile:](https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=15)
