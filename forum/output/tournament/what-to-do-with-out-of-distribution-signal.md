---
title: "What to do with 'Out of Distribution' signal?"
category: Tournament
url: https://forum.numer.ai/t/what-to-do-with-out-of-distribution-signal/3219
created_at: 2021-05-05T05:57:04.675000+00:00
last_posted_at: 2021-11-02T11:04:18.832000+00:00
posts_count: 14
views: 1525
tags: []
---

# What to do with "Out of Distribution" signal?

---

### Post #1 — **sugarscoot** | 2021-05-05 05:57 UTC

# Background

Define “out of distribution” as a mismatch between the statistics used for training and production (i.e. non-stationary data). Define “OOD detection” as a task for measuring the similarity or dissimilarity between the training data and novel data.

# Problem Statement

Suppose I had a signal for how “out of distribution” the current era was. How can it be utilized to improve my current submission?

# Recommendation

Allow users to score each of their predictions according to a confidence score (0, 1). When calculating COR values, weight each prediction according to it’s confidence.

# Examples

  1. The current era has statistics which closely **matches** the training set. Competitor submits with overall **high confidence** to reap expected benefits of high correlation.
  2. The current era has statistics that **doesn’t match** anything they have seen before in the training set. Competitor submits with overall **low confidence** to indicate that their model’s performance is undetermined and therefore **risky**.



# Conclusion

Sometimes the right answer is “I don’t know”, and it would be a valuable signal to have when creating the meta-model. Additionally, as a Competitor, I feel it would be valuable to have a mechanism to automatically adjust stake down according to volatile era statistics.

---

### Post #2 — **gammarat** | 2021-05-05 15:19 UTC

I think that’s an excellent idea, and well stated.

Now so far I don’t stake (I’m just here for the math), but it strikes me that an approximate solution until Numerai gets it’s staking sorted out would be to stake your 15 model slots from low certainty to high certainty, rank your submissions by your measure of certainty, and submit them to the appropriate model slot on that basis. Maybe something like that would work.

FWIW, OoD was really important in the work I did (ASW) prior to retiring. It could be very useful here.

---

### Post #3 — **mic** | 2021-05-05 22:01 UTC _(reply to #2)_

Isn’t it the purpose of staking? If your confidence is low, decrease your stake?

---

### Post #4 — **sugarscoot** | 2021-05-06 01:34 UTC

I’m advocating for the ability to adjust stake per prediction, as opposed to adjusting stake per submission or per round.

---

### Post #5 — **mic** | 2021-05-06 02:35 UTC _(reply to #4)_

Ah OK I misunderstood.

---

### Post #6 — **profricecake** | 2021-05-06 03:17 UTC

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/s/898d66/48.png) sugarscoot:

> Suppose I had a signal for how “out of distribution” the current era was. How can it be utilized to improve my current submission?

Do you have such a signal? Any ideas/suggestions how you might come up with one?

Thanks!

---

### Post #7 — **sugarscoot** | 2021-05-06 04:15 UTC

# Why is this important now?

Something to consider is that there are many models on the top-X leaderboard which are burning heavily right now. You would expect that independent models would result in independent errors, but instead we see that these models are correlated with each other, because they are all using the same training set. If the training set does not cover statistics relevant to the current era, then there is not much a competitor can do about it. From a competitor’s perspective the correct action to take is to make less confident predictions. However, there is no way to rescale the prediction values to indicate confidence, due to how the values are normalized as percentile values in Spearman’s rank correlation.

# What would a submission with confidence values look like?

Perhaps an optional row can be added to `predictions.csv` for `confidence` that can be assumed to be 1 if not included.
    
    
    id,prediction_kazutsugi,confidence
    n36c2,0.2,0.7
    n903f,0.5,0.5
    nc4a6,0.7,0.2

---

### Post #8 — **gammarat** | 2021-05-06 04:25 UTC _(reply to #6)_

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/numerai.discourse.group/profricecake/48/2528_2.png) profricecake:

> Any ideas/suggestions how you might come up with one?

I don’t know about others’, and I don’t know if this will help, but I’m looking (when I get the chance) at the underlying distributions of variance in the feature groups. For example there’s this - plots of the standard deviations for the leading PCA vector for each feature group over the Train, Test, and Validate eras. Clearly there’s some sharp changes, but how those correlate to model effectiveness I don’t know yet.

[![LPCAbyFGroupandFile](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/da7460912b15f763fe887a5df4a5a7d7907bb156_2_690x219.jpeg)LPCAbyFGroupandFile1322×420 52.8 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/da7460912b15f763fe887a5df4a5a7d7907bb156.jpeg> "LPCAbyFGroupandFile")

The Train is to the left, the Validate is between the dashed lines, and Test/live eras are to the right. What was really interesting (to me at least) was to project the six dimensional vectors formed from those at each era back onto the Train eras That essentially forms a cosine of the angle between a current era and each of the 120 Training eras, you get some sense of how these are evolving. As here:

[![CosSurface1](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/648e231ec92ff7a15ea02f24a9e6d5614f509381_2_690x346.jpeg)CosSurface11920×963 281 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/648e231ec92ff7a15ea02f24a9e6d5614f509381.jpeg> "CosSurface1")

The right axis refer to the Training eras, the left axis to the Tournament eras. The Validate eras are the ripple towards the front. If you rotate that by about 180 degrees, the effect of regime changes are visible for the last 30 or so rounds:

[![CosSurface2](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/1a20e6c00e7dd52dcde2539a8d5a88b4edd6decb_2_690x346.jpeg)CosSurface21920×963 324 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/1a20e6c00e7dd52dcde2539a8d5a88b4edd6decb.jpeg> "CosSurface2")

It’s a lot faster to compute than the subspace angles I was looking at before.

But fwiw, I’m moving on this week to comparing Gaussian mixtures, which looks more promising.

---

### Post #9 — **sugarscoot** | 2021-05-06 05:21 UTC

Thank you Gammarat! Beautiful post. To answer profricecake’s question in very general terms… first step is to come up with summary statistics (e.g. scalar, vector, matrix), and then use some discrepancy measure to compare given eras. Gammarat chose cosine similarity between the principal component feature vectors, as detailed in his post. I imagine a competitor is free to choose from a wide selection of both. For example, I might choose Euclidean distance between the per-era feature auto-correlation matrices, and the results might be different, or not.

---

### Post #10 — **profricecake** | 2021-05-06 16:08 UTC _(reply to #8)_

Thanks for your responses, [@gammarat](</u/gammarat>) and [@sugarscoot](</u/sugarscoot>)!

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/forum.numer.ai/gammarat/48/3281_2.png) gammarat:

> For example there’s this - plots of the standard deviations for the leading PCA vector for each feature group over the Train, Test, and Validate eras.

Can you walk me through this a little more slowly? Are you computing PCA per feature group, per era, in order to identify the leading PCA vector for that group and era? Or are you computing PCA per feature group using all train, test, and validation eras and then comparing the individual era PCA vectors to this overall? Or something different entirely? Just not sure where the standard deviation measure comes from that you’re plotting for each era, but I’d very much like to know!

Thanks again.

---

### Post #11 — **gammarat** | 2021-05-06 17:30 UTC _(reply to #10)_

Pretty much option 1!

I take in a single era at a time, PCA each feature group separately, and then extract the leading column of the transformed feature group. Then I take the std of that column and save it. (I’m actually set up to do all the columns by feature group and era, but the extra columns add very little information). That gives me vectors of six numbers per era.

Being curious, lazy, and numerically gluttonous, I do all the data: Train, Validation, Test, and Live. I can then compare the Training data against all the others on the basis of the vectors mentioned above.

Cheers!

---

### Post #12 — **profricecake** | 2021-05-06 19:39 UTC _(reply to #11)_

Gotcha. So just to be clear: you pick an era, pick a feature group, and PCA that block of values. Then you take the PC vector that explains the highest variance in the data (aka the first one) and find the std of the newly-transformed PCA feature values for that vector. Then you toss the rest because, as you wrote, they don’t add much information. Do this for each feature group and it gives you 6 values per era that essentially measure the data’s variance, per group, in the most-varied PCA direction.

If I’ve got it right, then what your first plot shows is that feature groups for the most part have their “variance lanes” that they occupy fairly consistently across eras.

I’m curious how feature count impacts this.

I just ran a control simulation where I created 4000 rows of 114 gaussian random numbers. Clearly with these conditions the variance in each dimension will be almost equal so using PCA is kinda weird. But still, I did PCA on subsets of that 114 columns (equal to the size of the existing feature groups). And indeed std goes up consistently with greater dimensionality:
    
    
    num features included in PCA:  12 // STD of first column: 0.2617
    num features included in PCA:  14 // STD of first column: 0.2621
    num features included in PCA:  38 // STD of first column: 0.2731
    num features included in PCA:  46 // STD of first column: 0.2747
    num features included in PCA:  86 // STD of first column: 0.2832
    num features included in PCA: 114 // STD of first column: 0.2899
    

(btw, the std of the gaussian random numbers I used was 0.25)

There’s probably some relationship related to the sqrt of the dimensionality here that someone smarter than me has already figured out. It may not be a big deal, but I’m just curious if you’ve tried to correct for that contribution of extra dimensions (in other words, so that int being always lower than str isn’t itself necessarily a signal, since int has 12 features and str has 38).

Even without correction there are two oddballs: wisdom with 46 features competes in variance with con and cha (114 and 86, respectively). And dex with 14 competes with str (38) in the variance game too.

---

### Post #13 — **gammarat** | 2021-05-06 19:54 UTC _(reply to #12)_

Good question, [@profricecake](</u/profricecake>). What I did to avoid that sort of problem is only compare std’s from the same feature groups, just in different eras. (Except at the end, where I take the inner products on the Training era groups)

The reason for doing it that way was because I noticed that the std in two particular feature groups (data columns 13 to 136j varied much more than that of the rest, particularly from era to era. There’s a bit more detail in [this post.](<http://forum.numer.ai/t/analyzing-training-data/3143/3>)

There are probably better ways to go about this, but this was easy to set up.

---

### Post #14 — **eleven_sigma** | 2021-11-02 11:04 UTC _(reply to #13)_

Interesting post [@sugarscoot](</u/sugarscoot>) and excellent contribution [@gammarat](</u/gammarat>). The main problem I see is that we ‘only’ have 679 (with new dataset) points to estimate how the era performance will be using a dataset with a few selected features that can predict it.  
The normalization used in features (binned in 20% quantiles) doesn’t help too much, as we lose the variance of its distribution.  
By the way, did you find the ‘problem’ feasible?
