---
title: "Incorporating Val2 in Training"
category: Data Science
url: https://forum.numer.ai/t/incorporating-val2-in-training/326
created_at: 2020-05-05T03:17:30.523000+00:00
last_posted_at: 2020-05-05T19:48:04.489000+00:00
posts_count: 6
views: 1748
tags: []
---

# Incorporating Val2 in Training

---

### Post #1 — **joakim** | 2020-05-05 03:17 UTC

This started as a question in the data science channel in RocketChat. Basically I would like to incorporate some of the Val2 data in my Train set, while still having both a Validation set as well as a final Test set.

My thoughts were to do the following:

  1. Combine Train set and Validation set (1&2).
  2. Divide up combined set into odd/even eras.
  3. Use odd eras as train set.
  4. Use first half of even eras as validation set.
  5. Use second half of even eras as test set.



Someone suggested that there might be data leakage from era to era, or potentially look-ahead bias (my interpretation), which if true, that would indeed be very bad (and I’m assuming the model would fail on the Test set).

I’d very much appreciate people’s thoughts on this, or other ideas on how to incorporate Val2 in Training while still having separate Val and Test sets.

---

### Post #2 — **joakim** | 2020-05-05 05:30 UTC

Just to add, my goal is to be able to develop models that generalize well on unseen data (sorry if I’m stating the obvious here).

In order to do that, I’d like to have a Validation (and Test) set that is representative of the Training set. My concern is that that may not be currently be the case with the existing Validation set. So if I optimize my model on it, the model may not be able to generalize as well on future data?

---

### Post #3 — **richai** | 2020-05-05 05:38 UTC

The danger is when people cross validate on rows instead of eras. But I think any split of the eras makes sense including this one.

However, as has been discussed, eras near each other may have similar properties as they come from the same regime to some extent. So you might want to have a large time separation in your validation as well (eras with lower numbers come from earlier times). This is why validation2 is especially useful because it is a very far away section of time from the training data.

---

### Post #4 — **ssh** | 2020-05-05 11:56 UTC

Hi!  
I would rather do not touch new VAL2 eras (197-206) at all! They are too precious for final model inference. Withing validation set 1 (121-132) we had a few some differences in eras as some eras are slightly different from others. Most of VAL2 eras are quit different from each other (different regimes or other reasons). I’m not sure if it would help to generalize on live data but it could be really useful to see how your model behaves at different regimes.  
Here, I’m attaching correlation matrix between VAL1 & VAL2 eras performance of some of my round210 META models. I’ve build different META models and for each model estimated correlation within each validation era. I estimated cross era correlation matrix and here it is. This could be more about my models’ behavior than about the relationship between eras, but maybe you also find it useful to understand about differences between VAL1 & VAL2.

In the low panel are values of cross-eras-correlation. In the upper part of the panel for all pairs of eras in VAL1&VAL2 x-y scatterplots. On a plot, each dot represents one METAmodel (all models from round210). X-Y coordinates on each plot are correlation of given METAmodel with a given pair of eras.  


[![META.models210.cor.val2](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/4065eb5d52df59aeef23171bc026d58b3a6de7f1_2_690x458.png)META.models210.cor.val21291×858 144 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/4065eb5d52df59aeef23171bc026d58b3a6de7f1.png> "META.models210.cor.val2")

  
Most of eras within VAL1 are similar (era121 and era126 slightly different)  
Within VAL2 a lot of differences. Again (NB), these could be my models not able to generalize well withing VAL2 but also part of it could reflect different regims of eras from VAL2.  
Only a few eras from VAL2 looks a little bit similar. Probably just cross-eras leakages, as in case of eras like 197 & 198 that demostrate “normal” 0.8 correlation - (normal to what I could see among live data and correlations from my model from different rounds). Probably era205 looks a little bit like eras from VAL1 regime.

---

### Post #5 — **objectscience** | 2020-05-05 13:46 UTC

## Adding “Bor’s” comment from Rocket Chat so it doesn’t get lost to time.

**bor**  
I found that most of my models have a 25% lower sharpe on val2 than on val1 (but both val1 and val2 are fairly small, so stochasticity, and I train on three eras in val1 as well, so that is maybe to be expected).

The leakage from era to era is the same you see in the live scores, where weeks following each other up have similar final scores. But training data is per month.

You could look at the model scores of other models with a 1-month difference (like week196, week 200, week 204), and see how much autocorrelation there between these.

That should give you an idea how much leakage there is between odd and even eras.

---

### Post #6 — **objectscience** | 2020-05-05 19:48 UTC _(reply to #5)_

## Continuing the conversation

**quantben**  
I also see lower correlation on val2, but at the same time, I rely more on the experience and on how much I trust my model/methodology.

It is unclear re leakage from era to era, there s a few ways there could be leakage. 4 weekly targets and weekly eras are definitely one way there is leakage. Also if some features are some kind of weighted historical average (ema or others), then there is also leakage here. I mostly assume no leakage myself, despite knowing there is some. If there is a lot of it, then I am kind of screwed, but it’s hard to fully comprehend

**daenris**  
eras are ordered, so you’re definitely training on data that happens after your validation and test data. But who knows how bad that is since they’re not giving us the necessary information to actually treat things as a timeseries.

**joakim**  
12:02 PM  
So validating a model that was trained on data from the future? Is that an issue though? If I’m training on data from the future I can see how that’s a problem. I don’t think that’s happening here though. Maybe I’m wrong?

**objectscience**  
MikeP what about synthetic data to remove the danger of training on future data, but increase the ability to validate? Do you think that’s possible here with such low s/n?

**MikeP**  
my feeling has always been that if you know enough about the underlying structure that you could generate useful synthetic data, then you know enough to just make a good model directly. Would be weird to generate synthetic data with this known underlying structure and then hope that your model can learn that underlying structure (which you already clearly know since you made the synthetic data). I know MLDP likes this area though so I must be missing something myself ![:face_with_tongue:](https://emoji.discourse-cdn.com/twitter/face_with_tongue.png?v=15)
