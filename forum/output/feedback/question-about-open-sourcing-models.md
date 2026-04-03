---
title: "Question about open-sourcing models"
category: Feedback
url: https://forum.numer.ai/t/question-about-open-sourcing-models/1430
created_at: 2021-01-08T07:17:13.934000+00:00
last_posted_at: 2021-01-10T06:17:02.816000+00:00
posts_count: 10
views: 1444
tags: []
---

# Question about open-sourcing models

---

### Post #1 — **qb1** | 2021-01-08 07:17 UTC

Is there a reason there is no bounty/payout for open-sourcing valuable models? If a good model is made open-source, other users will be able to use it to improve their own model. As such, the improvement to the meta-model would probably be larger than if the model was kept private and staked on.

Besides, if this payout is sufficiently large, then the payoff from open-sourcing the model would likely exceed the payoff that a user would expect from staking on his or her model. As such, he or she would have an incentive to open-source the model instead of staking on it. This would be particularly applicable to users who do not have much capital, and therefore, cannot stake significant amounts.

In other words, assuming that the value that Numerai places on a good open-sourced model exceeds a user’s private valuation of his or her own model, why doesn’t Numerai incentivize users to open-source their models?

---

### Post #2 — **themicon** | 2021-01-08 08:54 UTC

The question then becomes; “What is a good model?” Is it one that performs well over 20 weeks, 52 weeks, 2 years? And will the exact same model stay good for that long? I’ve been at this long enough to know that a good model this quarter will sink to rank ~600 in 6 months and then make it’s way back to the top in the next 6 months without it being touched. So the question is; How does Numerai know the model is good and are they willing to pay a large amount of NMR on something that might not work 6 months from now? It’s not as trivial as looking at the leaderboard and “paying a bounty” for the top models.

---

### Post #3 — **athene** | 2021-01-08 13:04 UTC _(reply to #2)_

One system could be, that Numerai announces a one time tournament with a bounty of XX Numerai for lets say a neural net that has a validation correlation of higher than 0.26.  
The bounty hunter have to submit the code or a notebook to the team. The team decides which participant(s) gets the bounty. The code of the winners gets open sourced. The most divers architectures have the most value for the meta model and should win.

That one-time tournament can be repeated each x-months for different algorithms and/or architectures.

---

### Post #4 — **wigglemuse** | 2021-01-08 15:52 UTC _(reply to #3)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/athene/48/912_2.png) athene:

> One system could be, that Numerai announces a one time tournament with a bounty of XX Numerai for lets say a neural net that has a validation correlation of higher than 0.26.  
>  The bounty hunter have to submit the code or a n

You can’t base any contest on being good on a known validation set. If you think you have a valuable model, you could open-source it and simply ask for donations from appreciative users. (Even if they don’t use the exact model, a well-documented method with code is something to learn from.) You could get more than you might think. OR…sell your model, but not to just one person, i.e. give the code to anybody that will send you 5 NMR or something. Again, you may get more than you might think, but with this method the model needs to be proved for a long time first, whereas just opening it up at the start could bring appreciation later as it is proved by users. But really, any scheme involving trying to extract a _large_ amount of money out of model that doesn’t involve simply staking on it yourself I think is a big long shot…

---

### Post #5 — **athene** | 2021-01-08 17:36 UTC _(reply to #4)_

> You can’t base any contest on being good on a known validation set

You can, if the code is submitted. The team can evaluate if the model is legit or if the creator cheated by training on the validation set.

Selling a model is an option to make money as an individual. But the benefits for the meta model would be pretty small. Having a tournament in which a couple of models get released will not only benefit the meta model but also each Numer.ai user, cause they get new ideas and approaches for their own code.

Right now we have to hope that people or generous enough to publish their secret sauces. Michael did that a couple of days ago in [Feature reversing input noise](<http://forum.numer.ai/t/feature-reversing-input-noise/1416>). But a tournament with some NMR involved would kickstart that process and offer new user more baseline models (besides integration_test) to build on.

---

### Post #6 — **wigglemuse** | 2021-01-08 17:54 UTC _(reply to #5)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/athene/48/912_2.png) athene:

> You can, if the code is submitted. The team can evaluate if the model is legit or if the creator cheated by training on the validation set.

It’ll never work if the scoring set is out there. Has to be a totally blind new dataset. Way to easy to fool “legitness” – you can easily optimize for val without explicitly training on val.

---

### Post #7 — **athene** | 2021-01-08 18:05 UTC _(reply to #6)_

I think they would see through that kind of optimizations. But even if that’s not the case, they have still a dataset that is not out there on which they can measure the performance of the models, the test dataset.

---

### Post #8 — **jrb** | 2021-01-09 11:15 UTC _(reply to #6)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/wigglemuse/48/3094_2.png) wigglemuse:

> Has to be a totally blind new dataset.

They’ve got the test set, which we submit predictions on, every week.

---

### Post #9 — **wigglemuse** | 2021-01-09 15:15 UTC _(reply to #8)_

Yes, of course there is the test set. But that wasn’t the suggestion – it was to use an open set and then just make sure the code wasn’t training on it. That wouldn’t work.

---

### Post #10 — **qb1** | 2021-01-10 06:17 UTC _(reply to #2)_

Pricing a model is not obvious, but users invest time building models and risk capital by staking on them. They must have some idea of how their model will perform, and some notion of whether their model is “good”. Otherwise, why would they be willing to stake on them?

Besides, through staking, Numerai effectively relies on what users think is a good model to determine what they view as a good model. As described [here](<https://medium.com/numerai/numeraire-the-cryptocurrency-powering-the-world-hedge-fund-5674b7dd73fe>), staking is a mechanism that allows Numerai to get a reliable signal on users’ private information.

Now, suppose that Numerai directly accesses users’ private information without going through staking. Why would they systematically reach different conclusions than users about the quality of their model?

Of course, for users to be willing to share their private information, they would need an incentive-compatible mechanism. I agree that finding such a mechanism is not trivial.

One idea would be: Numerai could commit to not using any of the information provided by users unless they acquire the user’s model.

In any case, I think that such a mechanism would significantly improve efficiency by (i) providing incentives for users that cannot afford to participate through staking, and (ii) by enabling collaboration across users through open-source.
