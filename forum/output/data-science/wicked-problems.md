---
title: "Wicked problems"
category: Data Science
url: https://forum.numer.ai/t/wicked-problems/5289
created_at: 2022-04-20T03:15:29.620000+00:00
last_posted_at: 2022-06-18T11:21:42.184000+00:00
posts_count: 11
views: 1995
tags: []
---

# Wicked problems

---

### Post #1 — **gammarat** | 2022-04-20 03:15 UTC

Out of curiosity, has anyone here looked at formulating the TC problem in the Tournament, or the IC one in Signals, in terms of their being “wicked problems” rather than (say) optimization ones? I don’t want to spend time reinventing the wheel ![:laughing:](http://forum.numer.ai/images/emoji/twitter/laughing.png?v=10). But in conversing with someone elsewhere today about such problems, it struck me that perhaps approaching these as wicked problems might prove useful, particularly using Conklin’s generalization (see the attached Wikipedia article, under “Characteristics”).

[en.wikipedia.org](<https://en.wikipedia.org/wiki/Wicked_problem>)

### [Wicked problem](<https://en.wikipedia.org/wiki/Wicked_problem>)

In planning and policy, a wicked problem is a problem that is difficult or impossible to solve because of incomplete, contradictory, and changing requirements that are often difficult to recognize. It refers to an idea or problem that cannot be fixed, where there is no single solution to the problem; and "wicked" denotes resistance to resolution, rather than evil. Another definition is "a problem whose social complexity means that it has no determinable stopping point". Moreover, because of The p...

Of course I could be completely out to lunch. It wouldn’t be the first time ![:crazy_face:](http://forum.numer.ai/images/emoji/twitter/crazy_face.png?v=10)

---

### Post #2 — **wigglemuse** | 2022-04-20 04:27 UTC

Our problems here have some of those characteristics, but clearly not all of them. But what does “formulate the TC problem” as being wicked even mean? And how would it help?

---

### Post #3 — **gammarat** | 2022-04-20 07:49 UTC _(reply to #2)_

If I knew the answers to those questions, I wouldn’t be asking mine ![:laughing:](http://forum.numer.ai/images/emoji/twitter/laughing.png?v=10) .

I guess basically it’s just a hunch I had that TC/IC and working in a wicked problem framework—rather than (say) an optimizing one—might be productive. I think the root of that hunch lies in my target analysis background—there one can measure better or worse in terms of how quickly an algorithm picks up a target, how long you can track it in noise, how quickly you can identify it as a threat or not, that sort of thing. Everything is, in theory moderately knowable. Systems that work in the lab tend to work in practice, etc.

TC otoh doesn’t really seem to be the same. A big problem of course is that the target itself is unknown (except in a vague sort of way), and as of this moment I don’t have any sense whether an approach that’s good for this round will be at all valid the next. And of course there’s the feedback nature of the competition, which from a fairly simple Darwinian perspective might imply that good solutions will cluster, lessening the value of each. I really don’t know, these are just things to ponder.

All that said, I do like having a framework in which to approach complex problems. For example, right now (rounds 310 & 311) the Tournament I’ve just started running 50 models that might be more wicked problem type solutions; they’re built on a genetic algorithm that leans more towards survivability than achieving peak performance. Some of them are doing quite well, and the rest not so well ![:sob:](http://forum.numer.ai/images/emoji/twitter/sob.png?v=10) What’s interesting is that they correlate to each other quite consistently, one group of 25 at about 0.1 among themselves, the other at about 0.7.I’m curious as to how they will sort themselves out over a number of runs.

Over in Signals, I have been running another 50 models that were (algorithmically) very tied together. They did ok on corr an MMC, an absolutely appallingly on IC. Except for two.and those two were the least tied to the rest.

So putting those experiences together leads me to think that trying to optimize for a best solution isn’t the right way to go. It may be better to evolve a set of solutions each of which performs moderately, but generally avoids getting murdered. Does that make sense?

In any case, I do ![:heart:](http://forum.numer.ai/images/emoji/twitter/heart.png?v=10) things like this that spark my curiosity!

---

### Post #4 — **wigglemuse** | 2022-04-20 15:03 UTC

I don’t think TC has the “one shot” character where trial-and-error is useless, etc. But I do think there will be a stochastic element to it, i.e. even with the best approach you are going to win some and lose some. That’s always been true with any measure (this is the live stock market, after all), but the ups-and-downs might be greater and more seemingly random (general trends for TC that apply to most people will be less apparent than corr, for instance).

So I recommend everybody have several to many uncorrelated different approaches to gaining TC so you can have a more even-keeled portfolio of results so when one model is getting hammered another will hopefully be doing very well. Unless you really like the rough seas.

I have always approached Numerai models as more of a logic puzzle or bit of code-breaking than an optimization or stats problem. Basically, I assume that others following consensus best-practice (or at least very common) methods are quickly going to converge upon a set of (fairly correlated) models that are going to pick all the low-hanging (and probably medium-hanging) fruit, generalize decently, etc. And I’m not going to try to compete to be the best & most comprehensive low-to-medium fruit picker (beyond the extent that I am forced to be because of the scoring metrics and payout system used) as I’m just not going to win that battle…and it’s boring. So I am making the (mostly unfounded) assumptions that the results are more deterministic than they may seem and also that most people are going to be led astray by simplicity bias in some areas. (i.e. so I’m probably overfitting)

---

### Post #5 — **rigrog** | 2022-04-20 16:40 UTC

I believe that optimizing for CORR (edit: and FNC, FNCv3) is the only NON wicked problem we have.

CORR we can calculate, and tune our model for… at least for a hold-out from the (now much expanded) validation data. EDIT: one can also calculate feature-neutral correlations.

But MMC (which is gone now) and TC are utterly black boxes for us, since they’re defined using the meta-model, which we don’t have. All we can do is observe our results, and stake accordingly (CORR only, 1 X TC, or 2 X TC).

---

### Post #6 — **gammarat** | 2022-04-20 18:30 UTC _(reply to #4)_

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/numerai.discourse.group/wigglemuse/48/3094_2.png) wigglemuse:

> So I recommend everybody have several to many uncorrelated different approaches to gaining TC so you can have a more even-keeled portfolio of results so when one model is getting hammered another will hopefully be doing very well. Unless you really like the rough seas.

Well, I do like rough seas. Or at least I’m entertained by them (time for a story about outrunning a hurricane on a 230 ft ship with only emergency steering, ![:scream:](https://emoji.discourse-cdn.com/twitter/scream.png?v=13)). Anyway, using uncorrelated models is one of the things I’m interested in. For example, these are the Spearman correlations among the predictions I submitted for Tournament round 312 (very similar to 311, which are doing ok):

[![Correlations_312](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/1/15a0d9797fa40856ef53f9c417be64bad16cfb6c_2_617x500.jpeg)Correlations_3121145×927 89 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/1/15a0d9797fa40856ef53f9c417be64bad16cfb6c.jpeg> "Correlations_312")

Each group of 25 has roughly the same Corr scores within the group when run on simulated or randomized Validation data; the 1-25 group runs at about half that of the 26-50 group. In real life, the scores seem fairly evenly distributed against other Tournament submissions, but that’s going only by eyeball for now. Other tests (like against neutralization) I haven’t gotten around to writing yet.

---

### Post #7 — **gammarat** | 2022-05-23 16:56 UTC

Just carrying on with this a bit, here’s some results from eras 311 to 316. This is all very preliminary (obviously). I start at 311 because the parameters of the models have been fixed since that round.

One of the first things I wanted to look at was the relationship between Corr and TC; there seems to be a loose but positive relationship:

[![316Separate](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/5/5b126835ac7500af1133b41bbe1cc4017fe7464c_2_656x499.jpeg)316Separate813×619 46.9 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/5/5b126835ac7500af1133b41bbe1cc4017fe7464c.jpeg> "316Separate")

TC is on the vertical axis, Corr on the horizontal; the numbers above each plot are the round number, the slope, and the vertical intercept.

Putting those together gives a more general estimate of the relationship:  


[![316All](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/9/962a1a42ac29e33875e801d71d8991be08f58693_2_517x371.jpeg)316All876×629 37.4 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/9/962a1a42ac29e33875e801d71d8991be08f58693.jpeg> "316All")

What isn’t shown (as I’m to lazy to organize the data) is that the slope varies significantly from day-to-day, although I haven’t seen one yet that is negative. That may well change, round 316 is pretty flat.

Then there is also the issue of staking. How to approach that? For me, using something like the Sharpe Ratio seems reasonable for now:  


[![316Sharpe](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/6/6be15916acfe2538393aa6edbdc60d05830114db_2_690x377.jpeg)316Sharpe1130×619 37 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/6/6be15916acfe2538393aa6edbdc60d05830114db.jpeg> "316Sharpe")

The vertical axis is Sharpe, the horizontal is model number. Each model has 4 bars: TC only, Corr only, Corr+0.5*TC, and Corr+TC. How representative these are of long run effects is anybody’s guess, although a few are definitely worth killing off immediately.

But what’s interesting for me that in terms of Sharpe ratios, pure TC (blue) doesn’t dominate anything; Corr (red) is generally the best, though in a few Corr+.5*TC, or Corr+TC, are the best options.

---

### Post #8 — **greyone** | 2022-06-01 20:50 UTC

thanks [@Aventurine](</u/aventurine>) for your COE letter - wouldn’t have found this fascinating discussion.  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/5/55025d21e1a01d64c1ce3bd65941ccae6c05a99e.png)image916×649 10.2 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/5/55025d21e1a01d64c1ce3bd65941ccae6c05a99e.png> "image")

  
Re: Approach to staking, since TC is so much more uncorrelated, it has stronger diversification/risk reduction benefits than Corr from both combining with other models as well as combining across rounds. Here is a chart showing the actual volatility of the 31 models Echelon has used in our portfolio versus the vol of the total portfolio. A 65% reduction in risk versus the average model’s risk as well as having lower vol than the lowest model’s risk. We think that finding ways to combine models performance across modelers will be a helpful way to address TC’s high vol and capture some of it’s persistence.

---

### Post #9 — **jefferythewind** | 2022-06-04 10:49 UTC _(reply to #5)_

just brings up some ideas. I agree prehaps CORR and MMC etc aren’t the perfect metrics to optimize. We can think like a stock picker. Most important is precision. We don’t need to take an action, but when we do, we don’t want to be wrong. If we’re wrong we don’t want to be too wrong. To me it seems these are some basic priniciples.

---

### Post #10 — **autratec** | 2022-06-18 06:15 UTC

[![Screenshot_20220618-131323_Chrome](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/7/7579e1232f86a6368eb2ff410d885b4a48423292_2_633x500.jpeg)Screenshot_20220618-131323_Chrome1080×852 96.1 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/7/7579e1232f86a6368eb2ff410d885b4a48423292.jpeg> "Screenshot_20220618-131323_Chrome")

My corr keep positive and tc bing me -10% return. What’s the value to have 2*TC here ?

---

### Post #11 — **gammarat** | 2022-06-18 11:21 UTC _(reply to #10)_

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/a/6bbea6/48.png) autratec:

> What’s the value to have 2*TC here ?

Definitely negative. How does that model usually perform, especially on a round to round basis (rather than a daily basis)?
