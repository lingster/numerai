---
title: "Numerbay: which model to choose?"
category: Tournament
url: https://forum.numer.ai/t/numerbay-which-model-to-choose/7444
created_at: 2024-05-03T15:19:07.278000+00:00
last_posted_at: 2024-05-05T09:34:17.965000+00:00
posts_count: 7
views: 795
tags: []
---

# Numerbay: which model to choose?

---

### Post #1 — **nmrdragon** | 2024-05-03 15:19 UTC

Hi, I tried to compare Numerbay models.

Why? Unlike buying art, from Numerbay models we usually want the same thing: to perform well. The Numerbay marketplace is not very friendly in this regard, as it basically shows hundreds of models, which can lead to a choice paralysis. But all we want is the one best model, right?

So I built a script that fetched some data for the best models on Numerbay (based on their 1 year average score).

My metrics are:  
annualized score (2 _mmc+0.5_ corr, full year average, i. e. not filled with zeros)  
score for 1 NMR (how much score is expected for every 1 NMR paid for the model’s predictions)  
trust score (how the model owner trusts the model, as shown by their stake in this model / total stake; some models are pretty good, but their owners have tens of Numerbay models, each one with small stakes, probably hoping for at least one model’s luck, I would not select one model randomly performing well)  
days in last year (how time-tested the model is, maximum is 365 days)  
required stake (how much you need to stake to break even; considers annualized score and price)

The models are sorted by their dragon score:  
(ln of “days in last year” * “annualized score” * “trust score”) / price

Of course these are not the only right metrics, there are so many things to look and not to look for. Feel free to develop your own metrics and scores! For example one that weighs more recent rounds would be interesting.

So here it is:  


[![Snímek obrazovky 2024-05-03 164959](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/3/3fd0f0b59fb6fd1607dc5fa2dc27516e137c7fac.png)Snímek obrazovky 2024-05-03 164959847×641 24.1 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/3/3fd0f0b59fb6fd1607dc5fa2dc27516e137c7fac.png> "Snímek obrazovky 2024-05-03 164959")

  
I highlighted 6 models, which I consider to be the most interesting, worth watching and maybe subscribing to (disclaimer: 50NN_300 is mine).

What I learned from doing this:

  * Many prediction buyers are probably losing money, because the required stakes are pretty high. Especially those of models whose owners don’t stake themselves.
  * Many models, including some popular ones, with very low scores.
  * A common strategy of listing many models with almost no stakes. As I already said, I do not consider this an honest strategy.



Thanks for reading this post and maybe thinking about Numerbay model evaluation for a while. I think it’s an interesting topic and feel free to discuss my ideas or post your own.

---

### Post #2 — **shatteredx** | 2024-05-03 17:22 UTC

Can you please state the units of “required stake” and perhaps explain a little more how you calculated it?

My “shatt048” model has a 1 year return of 256.9%. It would only require a stake of about 20 NMR to break even, as the total subscription cost for the year would be 52 NMR. What am I missing here?

---

### Post #3 — **nmrdragon** | 2024-05-03 17:47 UTC _(reply to #2)_

You seem not to count the profit added to stake as a stake increase.  
I calculated it for a single round (score * 0.14 as pf * 60 = 0.2 NMR price).  
Maybe my calculation is better, as compounding isn’t for granted, one decides each round whether to continue with you or do whatever different with the money. So I would consider the increased stake as the round’s stake, be it increased by your model or in any other way.

Thanks for your reply and of course I might be wrong.

---

### Post #4 — **shatteredx** | 2024-05-04 17:19 UTC _(reply to #3)_

Thank you. I was confused because I forgot that the decimal comma is used in Europe, and I thought the break even for my model was 60 thousand NMR ![:joy:](http://forum.numer.ai/images/emoji/twitter/joy.png?v=12)

---

### Post #5 — **nmrdragon** | 2024-05-04 17:43 UTC _(reply to #4)_

oh, that’s true, I have Google Sheets set to a local version, which uses the comma, I am sorry about any confusion and thanks for your comment  
btw shatt081 is amazing, 0.035 annualized score and price only 0.2 nmr, keep it up ![:blush:](http://forum.numer.ai/images/emoji/twitter/blush.png?v=12)

---

### Post #6 — **deepnum** | 2024-05-05 08:43 UTC

Thanks, this is great! Quick question, score annualized, is it an arithmetic mean of 2mmc+0.5corr or a geometric mean?

---

### Post #7 — **nmrdragon** | 2024-05-05 09:34 UTC _(reply to #6)_

hi, thanks!  
It’s arithmetic, I believe the official “reputation” scores are also arithmetic averages, just fill with zeros for missing days, right? But there is a small difference between my calculations and the official ones so there must be some difference in the method.
