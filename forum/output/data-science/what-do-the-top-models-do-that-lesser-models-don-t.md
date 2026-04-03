---
title: "What do the top models do that lesser models don’t?"
category: Data Science
url: https://forum.numer.ai/t/what-do-the-top-models-do-that-lesser-models-don-t/4753
created_at: 2022-01-08T22:22:48.787000+00:00
last_posted_at: 2022-02-17T05:36:27.454000+00:00
posts_count: 27
views: 4622
tags: []
---

# What do the top models do that lesser models don’t?

---

### Post #1 — **johnnywhippet** | 2022-01-08 22:22 UTC

Serious question, don’t require detail. Doing a write up and I have to compare my model - idling along in the top 30 to those above and around me. It’s obvious in terms of correlation the top models are miles ahead. What’s the secret? Without actually giving the secret away…

---

### Post #2 — **restrading** | 2022-01-09 00:30 UTC

What’s the secret for getting to around top 30? Without giving the secret? ![:upside_down_face:](http://forum.numer.ai/images/emoji/twitter/upside_down_face.png?v=10) Serious questions though, I’m still in the hundreds.

---

### Post #3 — **jacob_stahl** | 2022-01-09 01:13 UTC _(reply to #2)_

What’s the secret for getting to the hundreds? Without giving the secret? ![:upside_down_face:](http://forum.numer.ai/images/emoji/twitter/upside_down_face.png?v=10) Serious questions though, I’m still in the thousands.

---

### Post #4 — **qeintelligence** | 2022-01-09 09:53 UTC

What’s the secret for **staying** in the top 100? ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=10) I managed that before but not very long lol…

---

### Post #5 — **johnnywhippet** | 2022-01-09 12:04 UTC _(reply to #2)_

Luck… and crossing fingers that other models to perform less well than mine… ![:smiley:](http://forum.numer.ai/images/emoji/twitter/smiley.png?v=10)

---

### Post #6 — **mvanbur** | 2022-01-15 15:04 UTC

I suspect the top models have found unique ways to incorporate eras/time into their models. The stock market is a non stationary system, any model that doesn’t find a way to include time as a factor is likely not going to generalize well. It’s hard to do with numerai data because of the encryption, but I’ve found a few innovative ways to use eras. Those have been my best performing models.

---

### Post #7 — **johnnywhippet** | 2022-01-26 21:35 UTC _(reply to #6)_

Care to share? Without giving too  
Much away…

---

### Post #8 — **johnnywhippet** | 2022-01-26 21:35 UTC

Now 1st for corr, 3rd for mmc

---

### Post #9 — **profricecake** | 2022-01-26 22:31 UTC _(reply to #8)_

I’m curious why you continue to post how amazing your model is doing, both in this thread and [this one too](<http://forum.numer.ai/t/diagnostics-for-39/4155/49>).

There’s a leaderboard for that information; we don’t need it replicated in the forum multiple times. It muddies interesting discussions about the value of diagnostics and what approaches the best models are using. I keep coming back to these threads when new posts appear, hoping there might be some content. Alas, it’s mostly just you flexing.

![](http://forum.numer.ai/user_avatar/forum.numer.ai/johnnywhippet/48/2803_2.png) johnnywhippet:

> Serious question, don’t require detail. Doing a write up and I have to compare my model - idling along in the top 30 to those above and around me. It’s obvious in terms of correlation the top models are miles ahead. What’s the secret? Without actually giving the secret away…

Now that you’ve hit the very top of the leaderboard, care to answer your own question?

---

### Post #10 — **johnnywhippet** | 2022-01-26 23:16 UTC _(reply to #9)_

Sure. I’ll have a crack at that. The model diagnostics were crap, as I’ve posted previously. My model is not particularly sophisticated and I’m puzzled as to how it got where it did. The posts chart my puzzlement. Will that do you? Actually , given your tone I don’t care if it does you or not.

As for flexing, well, it’s not that, though I am pleased. this is one of several models I’d knocked up for an A level project. My theory is it’s not a good model, it’s just doesn’t perform as badly as some others.

Own question answered.

---

### Post #11 — **dzheng1887** | 2022-01-26 23:36 UTC _(reply to #10)_

haha, is this yours?

<https://numer.ai/model3_tres_optimism/submissions>

Congrats, If only you actually staked it with something, that would be pretty sweet the last few weeks

---

### Post #12 — **johnnywhippet** | 2022-01-26 23:39 UTC _(reply to #11)_

Yeah, Penniless student so not likely… though I have someone else staking it.

---

### Post #13 — **dzheng1887** | 2022-01-26 23:41 UTC _(reply to #12)_

You can borrow no? Your return is much better than a credit card even

---

### Post #14 — **dzheng1887** | 2022-01-26 23:42 UTC _(reply to #12)_

I’m sure you’ll make a ton of money soon after your school if you are messing around with boosted NNs here

Boosting all features or sets of features, or boosting one/two feature at a time like a GAM?

---

### Post #15 — **johnnywhippet** | 2022-01-26 23:43 UTC _(reply to #13)_

Not at my age sadly. Paying for uni is the dream that ain’t gonna happen.

---

### Post #16 — **johnnywhippet** | 2022-01-26 23:44 UTC _(reply to #14)_

Feature sets by era.

---

### Post #17 — **johnnywhippet** | 2022-01-26 23:47 UTC _(reply to #16)_

Sometimes it work sometimes it doesn’t. At the mo i think the conditions are spot on for the model.

---

### Post #18 — **dzheng1887** | 2022-01-27 00:09 UTC _(reply to #17)_

Hope the good results continue! If not, then there is improvements to find ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=10)

---

### Post #19 — **johnnywhippet** | 2022-01-27 00:13 UTC _(reply to #18)_

Thanks ![:blush:](http://forum.numer.ai/images/emoji/twitter/blush.png?v=10) I’m gonna be giving this up in the near future. Exams coming up… ugh… and I got to write this whole thing up. It’s proving to be harder than I thought.

---

### Post #20 — **mvanbur** | 2022-02-01 01:29 UTC _(reply to #7)_

Sure, I think everyone here already knows that you can’t convert numerai’s dataset to a stationary data due to the encryption. However, that doesn’t mean you should ignore the fact that all stock market data is time series data.

I’ve found a few ways to use sample weights to find the features most applicable to eras “similar” to the live era. Obviously, since it’s time series data usually the eras with the highest weight end up being the most recent eras. But I have found some interesting results where past eras end up with higher weights than the most recent eras.

I’m not saying to just blindly assign weights to eras, but it can an effective way to identify the most useful features/targets (since the new data is multi-target).

---

### Post #21 — **johnnywhippet** | 2022-02-01 09:45 UTC _(reply to #20)_

Mint. I’d tried to estimate the performance of sets of features over time but hadn’t thought of weighting them per se. I’m going to give it a try.

---

### Post #22 — **nyuton** | 2022-02-03 11:07 UTC

Top models are simply lucky! Most of them…  
Model’s rise, when the current era is favourable and then drop from top100.  
You can’t show me one, that sticked in the top100 for half a year long.

That’s not a problem, but you have to be aware of this fact.  
If you stay continously in the top 1000, you will get good annual profits. And that’s what really counts.  
But it’s not possible to be continously be at the top of all chars.

---

### Post #23 — **jefferythewind** | 2022-02-10 12:38 UTC

Yeah now that you say it we can see the Guitargeek has dropped out of the top 100. Wild. However we see the nopaix models continue the great performance for quite a while now.

---

### Post #24 — **wigglemuse** | 2022-02-10 16:12 UTC

We’ve seen that over and over. Someone gets to the top and is dominating for a while and they seem unstoppable and then they drop and we haven’t yet seen of any them return to their throne once deposed. Not that I’d mind doing that myself. I’m sure guitargeek’s model will probably still do pretty good even if it isn’t #1.

---

### Post #25 — **johnnywhippet** | 2022-02-10 20:46 UTC _(reply to #23)_

Nopaixx finished with a flourish today alright. Impressive stuff.

---

### Post #26 — **orbitalteapot** | 2022-02-15 20:19 UTC _(reply to #22)_

100%

High variance, luck.

---

### Post #27 — **autratec** | 2022-02-17 05:36 UTC

If the model doesn’t make too much difference, then the key contribution factor will be remaining as feature and training data filtering (ERA).
