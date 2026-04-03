---
title: "What is test data used for?"
category: Data Science
url: https://forum.numer.ai/t/what-is-test-data-used-for/4138
created_at: 2021-09-17T12:46:43.683000+00:00
last_posted_at: 2021-09-27T08:57:07.955000+00:00
posts_count: 10
views: 1009
tags: []
---

# What is test data used for?

---

### Post #1 — **nyuton** | 2021-09-17 12:46 UTC

What can we do with tournament/test data?  
I normally set all to 0.5, because it takes much time to predict all data.  
Is that a bad practice?

Does anyone use it?

---

### Post #2 — **gammarat** | 2021-09-17 14:31 UTC

If your forward algorithms are accurate, then they should work in reverse. I.e. if you can predict the test data targets, then you should be able to use those results to predict the training data. The error between predicting the training/validation data gives an estimate of how accurate your algorithms are. That’s my theory at least, though it loses something in practice, ![:laughing:](http://forum.numer.ai/images/emoji/twitter/laughing.png?v=9)

I did find using the variances among the various feature groups in the old data set useful for understanding problems in developing algorithms, but I haven’t applied a similar analysis yet to the new data.

---

### Post #3 — **rigrog** | 2021-09-17 16:43 UTC

For training, I use all the feature data (train, val, test, & live), and NONE of the target data (not even in RAM). I believe the ML hipsters would call that “unsupervised learning”.

That’s what _I_ do with it; what does Numerai do with it? Not much, these days.

In the past, before staking was a thing, Numerai used a model’s test performance to decide how much weight it would have in the metamodel. Now they only use it for “back testing”, and soon (in about 3 months, according to one R. Craib) they’ll be publishing target values for all but the live rows.

---

### Post #4 — **factorsparsity** | 2021-09-25 20:38 UTC _(reply to #3)_

I’m confused. How can you train without using the targets?

As for the test data - I read somewhere that it is good practice to provide it and that it is used by Numerai for additional evaluation of the data. I just provide it - prediction is cheap, training is expensive (at least in my case).

---

### Post #5 — **rigrog** | 2021-09-25 20:58 UTC _(reply to #4)_

“Train” means “prepare to perform”, and for me that preparation involves only the features.

After rather lengthy preparation, comes the much briefer performance phase, which does use the given target values to predict the ungiven ones. But that’s not training, it’s performing.

Wikipedia’s “unsupervised learning” article covers a lot of techniques, for training on only features.

---

### Post #6 — **maxchu** | 2021-09-26 05:42 UTC

I am actually quite curious how they use the stake value to weigh their models. The absolute stake value should not be directly used IMO as they are heavily affected by the financial situation of the model maker. Also, you can easily find models with high stake value perform poorly.

The principle of using stake value as ensemble weights is also consistent with using test/valid results as I am assuming ppl deciding the stake value of their models based on the test/valid performance. In that case, using the test results for their inhouse ensemble should also include this principle, and much better they can consider the relative performance of models which stake value alone cannot achieve that.

---

### Post #7 — **wigglemuse** | 2021-09-26 12:58 UTC _(reply to #6)_

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/m/dec6dc/48.png) maxchu:

> The absolute stake value should not be directly used IMO as they are heavily affected by the financial situation of the model maker. Also, you can easily find models with high stake value perform poorly.

They’ve always said that they do use absolute stake value, and try as they might to be more clever, nothing seems to beat it. That could change of course. I also don’t think the large (or at least the large and experienced) stakers put too much weight on validation diagnostics.

---

### Post #8 — **maxchu** | 2021-09-26 23:19 UTC _(reply to #7)_

Yes, i agree that they don’t put too much weight on “the validation” set. What I mean by the validation set is not limited to the official one, the most common thing to do is cross-validation and they are still validation set. In the end, we need to have some measure on unseen samples to be sure we are doing ok, whether it is the official one or self-constructed validation is in principle the same. Also, what i mean by the test set is actually the live performance.

Finally, I think the most important thing I observed is that you can find models perform poorly with very high stakes. You can search “crowdcent” in the main tournament.

---

### Post #9 — **themicon** | 2021-09-27 08:30 UTC _(reply to #8)_

What is the timescale you are looking at to determine if a model is doing “poorly” as you state? 3 months, 6 months, 1 year, 3 years? There are lots of models that are now doing “poorly”, but were the top models 6 months ago. Is this a “poor” model: [Numerai](<https://numer.ai/mercuryai>) or did the markets change? Nobody is going to be at the top of the leaderboard for very long, so looking at snapshots is not useful.

Maybe we should look at average rank over the lifetime of a model instead?

---

### Post #10 — **maxchu** | 2021-09-27 08:57 UTC _(reply to #9)_

I guess we can ask the same question about how long numerai would determine if the stake value meta-model is doing good. I don’t think we have a magic number here, but what we can be sure of is that it is more the better. I didn’t do much detailed research/measure on how absolute stake value correlates with live performance. Maybe you are right, the absolute stake does correlate with the live performance.

I just find it very surprising that absolute stake correlates with live/future performance.
