---
title: "When to Retrain a Model — A Casuistic Analysis"
category: Tournament
url: https://forum.numer.ai/t/when-to-retrain-a-model-a-casuistic-analysis/8253
created_at: 2026-02-17T22:33:00.103000+00:00
last_posted_at: 2026-02-17T22:33:00.167000+00:00
posts_count: 1
views: 229
tags: []
---

# When to Retrain a Model — A Casuistic Analysis

---

### Post #1 — **svendaj** | 2026-02-17 22:33 UTC

Over the last year I was running simple experiment which should give me intuition of frequency of model retraining. As some of you could mention on discord and Forum I am running weekly retraining of all of my models, but I was not sure if it would not “overwrite” really good models trained in history. Now I have some insights/interpretations/hypotheses and I would like to share them with you, before I will repurpose experimental model slots for another research.

## Experimental setup

Model **[JOS_XB_LAZY](<https://numer.ai/jos_xb_lazy>)** is currently #2 on model leaderboard both at MMC20 and CORR20 rank and is retrained weekly on every Saturday when new data are available.

At round 924 (opened on Jan 20, 2025 and resolved on Feb 20, 2025) I have uploaded retrained model JOS_XB_LAZY both to its slot and to newly created slot **[JOS_XB_LAZY_W1](<https://numer.ai/jos_xb_lazy_w1>)** , which remained unchanged and was not retrained since.

Every following week (rounds 929, 934, 939, …) I retrained base model and created slot for weekly version ( [JOS_XB_LAZY_W2](<https://numer.ai/jos_xb_lazy_w2>), [JOS_XB_LAZY_W3](<https://numer.ai/jos_xb_lazy_w3>), [JOS_XB_LAZY_W4](<https://numer.ai/jos_xb_lazy_w4>), …) until round 979 (resolved on May 8, 2025) when I uploaded last experimental model JOS_XB_LAZY_W12 (now repurposed as [JOS_XB_LAZY_SH](<https://numer.ai/jos_xb_lazy_sh>)).

After that I continued to weekly retrain base model and left weekly versions without any change.

## Observations

Here are results plots of experimental models compared to base model:  


[![Cumulative score of all discussed models](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/6/6f492842541552573df3c9dd7222bf0b36a88079_2_690x271.png)Cumulative score of all discussed models1656×651 117 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/6/6f492842541552573df3c9dd7222bf0b36a88079.png> "Cumulative score of all discussed models")

  * All experimental weekly models are highly correlated.
  * Base model diverges around round 1024 about 5 months after experiment start, when experimental models fail to pick new positive signal in the data
  * Around round 1059 base model is losing positive signal in the data caught by experimental models until round 1079, when they stop deliver positive returns
  * Final decline of experimental models after round 1154 is probably result of introduction of V5.2 dataset - all experimental models used V5.0 dataset and base model was retrained on V5.2 since round 1164
  * Repurposed model W12 diverges immediately after its change and return to the weekly retraining



Here are MMC and CORR results of models selected for better clarity of plots:  


[![Cummulative MMC](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/e/ea7f14601e1d7a4bf3130f7ec6a2da8d5d350c11_2_690x272.png)Cummulative MMC1657×655 85.5 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/e/ea7f14601e1d7a4bf3130f7ec6a2da8d5d350c11.png> "Cummulative MMC")

  


[![Cummulative CORR](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/4/4401ab52447cf43d262173563043eddea17ab3c4_2_690x276.png)Cummulative CORR1652×661 84.8 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/4/4401ab52447cf43d262173563043eddea17ab3c4.png> "Cummulative CORR")

  * Decline in performance is mainly due to poor MMC



## Conclusions

  * Having good model is not enough because signal in out-of-sample data is changing.
  * Good model without retraining may deteriorate over time.
  * Frequent retraining delivers better results.
  * Weekly retraining is probably unnecessary, but monthly retraining seems to be minimum.
  * Retraining on new data is essential.
  * Retraining can overwrite better model, but superiority of unretrained model is temporal and can cease to exist after some time. Moreover, it is impossible to predict when unretrained model will perform better.



Any other observations or conclusions?
