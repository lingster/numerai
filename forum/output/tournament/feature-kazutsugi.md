---
title: "Feature kazutsugi"
category: Tournament
url: https://forum.numer.ai/t/feature-kazutsugi/2048
created_at: 2021-02-28T01:16:41.770000+00:00
last_posted_at: 2021-03-18T04:07:14.851000+00:00
posts_count: 7
views: 1557
tags: []
---

# Feature kazutsugi

---

### Post #1 — **a5zima** | 2021-02-28 01:16 UTC

Hi, everybody. I am a very newbie, trying to understand what are you doing here. I can’t find any information about feature kazutsugi, does it named in honor of Nami Kazutsugi and his “Enten” quasi-currency scheme?

Also, I can’t understand all these features they are fictional and created artificially, is this all a game?

---

### Post #2 — **dliden** | 2021-02-28 01:48 UTC

Hello! I was new a couple of weeks ago and had some of the same questions. For the data:

> At the core of the Numerai Tournament is the free dataset. It is made of high quality financial data that has been cleaned and regularized and obfuscated. Each `id` corresponds to a stock at a specific time `era`. The `features` describe the various quantitative attributes of the stock at the time. The `target` represents an abstract measure of performance ~4 weeks into the future.

![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/9/90e8adeb4f6f03ac5b052087372c6555fb93d298_2_500x500.png) [docs.numer.ai](<https://docs.numer.ai/tournament/learn#data>)

![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/3/32b3e8aa5391fe8f83bc813ffa7c27cdf492f134.png)

### [Overview | Numerai Docs](<https://docs.numer.ai/tournament/learn#data>)

Everything you need to know to get started in under 5 minutes!

The data are heavily obfuscated but they are not imaginary. The problem, as I understand it, is less about applying any subject-matter knowledge to the features themselves and more about the general problem of low-signal-high-noise tabular data.

---

### Post #3 — **wigglemuse** | 2021-02-28 01:55 UTC

Kazutsugi is not one of the “features”, but the target (the thing being predicted). Except it isn’t anymore, and has since been replaced (a few months ago) with a new target we call Nomi. And the names of the targets have traditionally been tongue-in-cheek references to certain notorious people, yes. (There are at least 5 other retired targets from an older version of the tournament – couple years back now.)

---

### Post #4 — **robbo_the_fossil** | 2021-03-01 17:42 UTC _(reply to #3)_

Who is Nomi then? Asking for SWIM

---

### Post #5 — **themicon** | 2021-03-01 19:46 UTC _(reply to #4)_

Chef Nomi - Sushiswap

---

### Post #6 — **ccc513** | 2021-03-18 02:51 UTC

[@wigglemuse](</u/wigglemuse>) I’m guessing that the different target names are to designate the various unknown methods Numerai has used internally over time to generate the target, and when the name is changed that’s just a notice to participants so they are aware their modeling approach might be more/less effective than before? If that is an accurate explanation, is there an official revision history somewhere that shows how often they’ve changed the target?

---

### Post #7 — **wigglemuse** | 2021-03-18 04:07 UTC _(reply to #6)_

The current form of the tournament has only had the two targets – nomi replaced kaz. Before that the format of everything was quite different, the scoring was different, the data was different – we had 5 binary targets at once we were getting scored on (5 separate tournaments, essentially) which was an expansion from an earlier version with a single binary target. And before that I don’t even know. Nomi replacing kaz without the data changing or other huge transformations was a unique event, and it really just changed the distribution of the same target if you will. The old versions of the tournaments never quite “worked” – for them or for us (well, a few people got rich, so I guess it worked for them). But what we have now is way way better than it used to be.
