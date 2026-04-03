---
title: "Signals Churn Threshold"
category: Announcements
url: https://forum.numer.ai/t/signals-churn-threshold/7648
created_at: 2024-08-16T21:53:51.113000+00:00
last_posted_at: 2024-09-24T06:10:04.683000+00:00
posts_count: 10
views: 1071
tags: []
---

# Signals Churn Threshold

---

### Post #1 — **ark** | 2024-08-16 21:53 UTC

On September 20, 2024, we will be implementing a 15% churn threshold for all Signals submissions. Any submission that breaches this threshold will not be paid. This does not apply to Numerai or Crypto.

Churn is a statistic describing how the alpha scores of a signal changes over time. We recently open-sourced the code we use to calculate churn in Signals Diagnostics. You can find it [here](<https://github.com/numerai/numerai-tools/commit/f58990854c81eb870cf9a252f1d72aace1a34857#diff-8ff14dc2bf7de3c1800d64eec9d066618b1ab49243bfc99f1bd8c7f3fe307d56R12-R43>).

If a Signals submission has high churn, then Numerai can’t trade the signal easily. Many models built on Numerai data have low churn organically, but Signals Churn is very high. Most Signals models have > 20% week-over-week churn:

**

[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/f/fd2f4b5037418174f62f9035165ed7e52b87e0bd_2_584x303.jpeg)1600×831 90.4 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/f/fd2f4b5037418174f62f9035165ed7e52b87e0bd.jpeg>)

**

We know that this negatively impacts the churn of the Signals Meta Model because the average individual churn of Signals models is nearly 70% correlated with the Signals Meta Model Churn:

[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/7/7190614cc1dd271bb5894014c357e6496d626a9c_2_436x75.png)946×162 9.6 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/7/7190614cc1dd271bb5894014c357e6496d626a9c.png>)

[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/6/626fa6a03bbfc4514b3ba7db6514203a51df3d87_2_607x311.jpeg)1600×819 106 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/6/626fa6a03bbfc4514b3ba7db6514203a51df3d87.jpeg>)

Signals Meta Model churn too high to be useful to Numerai:

[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/6/6cb772191887ad246911a4ff1d18ff81e73bfc73_2_582x411.png)1600×1130 166 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/6/6cb772191887ad246911a4ff1d18ff81e73bfc73.png>)

To lower the churn of the Signals Meta Model, we must lower the churn of all Signals - so we are implementing a strict churn threshold that operates as follows:

  * Any model that has not submitted in the previous week will have it’s stake set to 0 
    * Any model that does not submit weekly will naturally cause high churn in the Meta Model
  * When you upload a new submission we: 
    * Calculate churn with respect to each of this model’s submissions from the previous week
    * Check if this submission has >= 15% churn with respect to any of this model’s accepted submission in the previous week. If this submission breaches the churn threshold, it’s stake is set to 0.



* * *

## FAQs

**Is 15% too low?**  
No. Our v43.cyrus_plus_teager model has never breached 15% churn, so we know this is an achievable level of churn that will guarantee a sufficient reduction in overall Signals Meta Model churn.

**How do I know what my churn is?**

We have [open-sourced](<https://github.com/numerai/numerai-tools/commit/f58990854c81eb870cf9a252f1d72aace1a34857#diff-8ff14dc2bf7de3c1800d64eec9d066618b1ab49243bfc99f1bd8c7f3fe307d56R12-R43>) the churn calculation we use in diagnostics so that you can calculate it yourself. Soon, we will use this code to display the churn on the Signals website. Any submissions that breaches the threshold will be highlighted as “high churn” in the website. Once the threshold is implemented, we will begin setting the stake to 0 for these submissions.

**When will this churn threshold take effect?**

On September 20, 2024 the threshold will be 15%.

**What about Numerai models?**

This does not affect Numerai models as they cannot control their churn level due to the obfuscation of the dataset. Instead, we have crafted a dataset that naturally results in lower-churn models. Signals, on the other hand, can easily reduce their churn because Signals models can easily calculate it. Signals models can be trained to minimize churn just the way we did with our v43.cyrus_plus_teager model.

**What if everyone breaches the threshold?**

The payout factor will heavily incentivize users to submit reliably low-churn models so they are not dropped out of the staking pool. Over time, the likelihood of everyone simultaneously breaching the threshold will drastically diminish.

---

### Post #2 — **numerologist** | 2024-08-16 23:36 UTC

Kudos to the team for open-sourcing stuff. More transparency, fewer bugs. ![:+1:](http://forum.numer.ai/images/emoji/twitter/+1.png?v=12)

> The payout factor will heavily incentivize users to submit reliably low-churn models so they are not dropped out of the staking pool.

I have a theoretical concern re this: what if there are only a few models left (at least in the beginning) - and the payouts are still primarily in MMC?  
Does this mean that half of the few remaining good low-churn models will be heavily **dis** incentivized by heavy burns? ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=12)

---

### Post #3 — **robprofit** | 2024-08-17 10:30 UTC

Is it possible that churn can be too low ? For example, a simple buy and hold strategy would have a churn of 0% which would be too low for a hedge fund. If my question shows that I don’t really understand churn, then is there a document you can point me too that explains it in more detail.

---

### Post #4 — **wigglemuse** | 2024-08-17 20:14 UTC _(reply to #3)_

It wouldn’t be too low if that was the way to make the most money. I mean obviously you want to take profit sometimes and short positions probably have a built-in deadline, but there is no inherent reason why if in some idealized world the exact same set of positions kept returning the best returns, you wouldn’t just keep holding them (or repeating them). But in the real-world that’s just not going to happen. (But for long positions, some stocks might remain the best bets for extended periods.) But still, I don’t think you need to create churn for churn’s sake. (Is there some strategic reason to do so? Make “lateral” moves just because?)

---

### Post #5 — **wrcx** | 2024-09-07 17:46 UTC

Is Sep 20 refering to round close or resolve date?

---

### Post #6 — **numerologist** | 2024-09-09 18:02 UTC

Following my post on [Numerai-induced ticker churn](<http://forum.numer.ai/t/better-lgbm-params-signals-v2-data-and-reducing-signals-churn/7638/14>), I’ve decided to look into what’s the churn for Numerai targets in the v1 data. After all, that’s what our models try to aim for.

Here are the results: in a perfect world, Numerai would want us to have **40.7%** churn on average (or **28.3%** at the very least). Code and stats:  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/d/d6efb735b1efbbde1ee49f46bf68e82eeb58ec3d_2_376x500.png)image1018×1353 117 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/d/d6efb735b1efbbde1ee49f46bf68e82eeb58ec3d.png> "image")

Disclaimer: yes, having big ticker gaps across eras (outlined in the post above as _ticker churn_) would make the _target churn_ worse since it could compare to an era that was over a week ago, but this shouldn’t distort results much realistically since you cannot trade a ticker if it regularly falls in and out from the universe. (so at the end of the day, ticker churn is basically additive)

**To the team:** I remember you mentioned that targets in the main tournament are adjusted for churn. Assuming you want us to have **both** high corr with the target **and** low churn, would it be possible to adjust targets for churn in the V2 signals data too?  
Thanks.

---

### Post #7 — **develuse** | 2024-09-22 17:54 UTC

I am trying to do my first submission, but I’m getting “churn_calculation_error: Could not calculate churn, please contact support” using the notebook from [Google Colab](<https://colab.research.google.com/github/numerai/signals-example-scripts/blob/master/example_model.ipynb>) with version 2 data for Signals competition

How do I correct my submission? looks like this is a bug of the new release

---

### Post #8 — **develuse** | 2024-09-23 19:57 UTC _(reply to #7)_

Why do I not get a reply? How could my submission correlation with previous rounds if I don’t have submissions recently.

---

### Post #9 — **ark** | 2024-09-23 22:25 UTC _(reply to #8)_

Hi develuse, apologies for the inconvenience. Could you retry your upload please?

---

### Post #10 — **develuse** | 2024-09-24 06:10 UTC

Thanks it seems fixed, any bug reward ;-)? at least the developer should be rewarded
