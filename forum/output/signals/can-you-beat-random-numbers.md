---
title: "Can You Beat Random Numbers?"
category: Signals
url: https://forum.numer.ai/t/can-you-beat-random-numbers/4022
created_at: 2021-09-01T09:55:15.874000+00:00
last_posted_at: 2022-04-01T16:01:54.692000+00:00
posts_count: 17
views: 3333
tags: []
---

# Can You Beat Random Numbers?

---

### Post #1 — **robo_boi** | 2021-09-01 09:55 UTC

As an experiment, I’ve been submitting random numbers between 0 and 1 for all the available tickers. The model is called ‘[Jersey Devil](<https://signals.numer.ai/jersey_devil>)’ and is currently ranked 71 for corr 20 as of round 278 with one more day to go.

I’m not staking on this model (just the minimum .01 to see returns). I use it solely as a baseline for my other models. If they can’t beat random numbers, they die. Yes it hurts when you put a lot of time and effort into a model and it doesn’t do better than random numbers ![:laughing:](https://emoji.discourse-cdn.com/twitter/laughing.png?v=13).

I was pretty surprised this has positive corr at all but we’ll have to see if that continues in the future. [Here](<https://colab.research.google.com/drive/1T36WcUhq6v-NGsU_Cme96ieY6NDkGk86?usp=sharing>) is a colab notebook with the exact code.

_Jersey Devil vs My Current Best Model_  


[![jd_ogo](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/9/9d324614851ce0c53c77ee62fc3ab2889d185e63_2_690x261.jpeg)jd_ogo1273×483 44.8 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/9/9d324614851ce0c53c77ee62fc3ab2889d185e63.jpeg> "jd_ogo")

[![jd_ogo_cumm](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/e/e8f5eacb439d0f1f9b4a3bd83a8c1788e98c3f81_2_690x259.jpeg)jd_ogo_cumm1274×479 41.1 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/e/e8f5eacb439d0f1f9b4a3bd83a8c1788e98c3f81.jpeg> "jd_ogo_cumm")

---

### Post #2 — **of_s** | 2021-09-01 13:55 UTC

This would be a perfect demonstration case of the effects of neutralization. Reporting pre- and post neutralized scores would be highly informative.

---

### Post #3 — **objectscience** | 2021-09-01 16:57 UTC

My ego could never survive this. ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=9)

---

### Post #4 — **rapidautumn** | 2021-09-06 06:43 UTC

An interesting experiment, thanks for sharing! This is not surprising on second thoughts. A randomly selected portfolio of stocks often performs quite well, especially in long bull runs. From memory there are some studies showing that it handily beats most fund managers. Whether a random portfolio could also beat a hedge fund with great data… I suspect no self-respecting hedge fund would submit to that test.

---

### Post #5 — **robo_boi** | 2021-11-26 10:21 UTC

Update. Currently around 30% avg. 3 month returns  


[![update](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/3/3476ab10fbe307375783044d5030317432d2b7b8_2_690x302.jpeg)update1304×571 106 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/3/3476ab10fbe307375783044d5030317432d2b7b8.jpeg> "update")

---

### Post #6 — **wigglemuse** | 2021-11-26 17:40 UTC

But are random numbers still even random after neutralization?

---

### Post #7 — **autratec** | 2021-11-28 04:48 UTC _(reply to #5)_

If the random number, beats majority of submission, what does it mean ?

---

### Post #8 — **wigglemuse** | 2021-11-28 16:54 UTC

Doesn’t mean anything really unless it consistently beats everything for a long time. It would be quite expected to have both good and bad runs but be close to zero when averaged over many rounds (but many more than you might intuitively think is necessary).

---

### Post #9 — **taori** | 2021-11-29 11:21 UTC _(reply to #8)_

I agree [@wigglemuse](</u/wigglemuse>). Nevertheless, it is a very interesting test and I am glad [@robo_boi](</u/robo_boi>) is sharing that with us.

---

### Post #10 — **wigglemuse** | 2021-11-29 21:00 UTC

Yes. Although, as I joked above, neutralization of random numbers would actually add a tiny bit of structure to the randomness (because that which it is neutralized against is not random). Probably not enough to notice scorewise, and if it did turn random numbers into a consistently positively (or negatively) scoring model, then that would probably indicate a bug somewhere.

---

### Post #11 — **autratec** | 2021-11-30 00:11 UTC _(reply to #8)_

if the random number is able to beat the submission, it probably means the market is moving towards certain direction at the end. and it could be driven, not by the individual company performance, but the the overall trend or human race behavior, like inflation, innovation, corporatization, etc

---

### Post #12 — **testorganisation** | 2021-12-02 01:49 UTC

Is anyone able to explain why its corr and mmc track each other so closely? (Of course better corr usually equals better mmc but my models do not display this behaviour)  
Could it be that if it randomly does well one round, it is likely to get high mmc as other models are unlikely to have submittted predictions similar to randomness?

---

### Post #13 — **wigglemuse** | 2021-12-02 02:35 UTC

[@testorganisation](</u/testorganisation>) Because a random submission will have near-zero correlation with the metamodel and so not much if any of the prediction signal is residualized away in the MMC process. (Generally, correlation with metamodel sends MMC towards zero.) So basically the reason they track the same is because they are pretty much the same.

You’ll see this behavior for everybody’s models if the metamodel itself is at zero – when the metamodel essentially is giving no (actually predictive) signal, then each component signal will have an mmc near equal to its main predictions.

---

### Post #14 — **bor1** | 2021-12-02 10:16 UTC

I haven’t thought about random for signals - but my thoughts on random in classic is that as we are predicting very-close-to-random anyway (correlation strengths of 0.03), it is pretty easy for random to perform well.

You could have 10 different random submissions, and see how well they cluster around 0, or that they indeed swing collectively above/below zero as well.

In different tournaments, random might never perform well - say, if the tournament is “Landing rovers on Mars”, a random rocket construction and route-plotting program is never going to get close to performing well :-).

---

### Post #15 — **wigglemuse** | 2021-12-02 15:34 UTC

Yes, these tournaments are symmetrically designed so that random is at zero in the center. It is exactly as difficult to score -0.1 as it is to score +0.1. But yeah, since even good score magnitudes are so low most of the time it is natural that randomness can be competitively positive for any given round. But it should over time be negative about as much. (But we also know from random walks that once it is on one side of the line, it can manage to stay there for quite a while as far as cumulative performance.)

---

### Post #16 — **kenfus** | 2021-12-15 13:12 UTC

Maybe I am crazy, but how is 0.011 35% return, when we start with 0.01? Should it not be 0.013? I think the return calculation is just wrong? When we only look at NMR, we can see that it is random because it’s still at around 0.01.

Or wait, today minus 3 months equals to 15.09, when the model went down to 0.08 NMR. The difference to 0.011 NMR it is around a 35% increase, haha. So I guess we are not losing (yet) against a random model.

---

### Post #17 — **of_s** | 2022-04-01 16:01 UTC

The real question is: **Can you beat all 0.99’s**?

I was running this experiment from the observations in these two prior posts I shared:

  * [Possible p / (1-p) vulnerability in Signals](<http://forum.numer.ai/t/possible-p-1-p-vulnerability-in-signals/4314>)
  * [Is TB200 neutralizing the Moore-Penrose Inversion neutralization step in Signals](<http://forum.numer.ai/t/is-tb200-neutralizing-the-moore-penrose-inversion-neutralization-step-in-signals/4308>)



All 0.99 submissions: <https://signals.numer.ai/of_s_3>  
All 0.01 submissions: <https://signals.numer.ai/of_s_4>
