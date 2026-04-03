---
title: "Noob question regarding Data"
category: Tournament
url: https://forum.numer.ai/t/noob-question-regarding-data/1700
created_at: 2021-02-10T21:34:57.885000+00:00
last_posted_at: 2021-02-16T14:06:11.817000+00:00
posts_count: 11
views: 2078
tags: []
---

# Noob question regarding Data

---

### Post #1 — **flipperpie** | 2021-02-10 21:34 UTC

I just finished downloading the data and I have quick question.

I noticed that the id is unique for every record.

As per the description of the data. "Each `id` corresponds to a stock at a specific time `era`"

When I first read that description I figured I could view a given id across all eras but that it not the case.

Does this mean I can’t do any sort of historical analysis on a given id?

---

### Post #2 — **wigglemuse** | 2021-02-10 22:40 UTC

A _very_ common question. And yes, that’s exactly what it means – you cannot track a specific stock from era to era – the ids are essentially just random one-time-use identifiers. (If you are dying to do time-series analysis, take a look at the Signals side of things, but you have to bring your own data in that case.)

---

### Post #3 — **robbo_the_fossil** | 2021-02-11 04:24 UTC _(reply to #2)_

This seems to be done to deliberately prevent historical or time-series analysis. I think most noobs (like me!) come into this with the impression that that is what is to be done - time series analysis. But I have come to understand that that is not the case! You have some features and an outcome (target). Use features at era X to guess target at era X. Or perhaps more accurately, use features at era X to guess target at era X+δX. Your model will be used on features Y to determine how the hedge fund will invest at Y+δY. This is the strategy of the hedge fund I assume… we have some data right now - can it tell us what will happen in the near future with a stock price. They are not trying to build a ‘case’ over time, with more time data improving the prediction.

---

### Post #4 — **wigglemuse** | 2021-02-11 04:32 UTC

Yes, it is best just to forget all about the stock market when you are first making models. It is a black box problem with unknown features. Trying to apply financial domain knowledge will just frustrate you because you can’t.

---

### Post #5 — **madlib** | 2021-02-12 06:26 UTC

Complete noob here too & had the same question! But the answers lead to this question for me:

![](http://forum.numer.ai/user_avatar/forum.numer.ai/robbo_the_fossil/48/851_2.png) robbo_the_fossil:

> use features at era X to guess target at era X+δX

If there’s no relationship betweens the different era’s what is the use case for the multiple ere’s in the data?

---

### Post #6 — **objectscience** | 2021-02-12 15:18 UTC _(reply to #5)_

Eras are in chronological order allowing you to use a walk forward approach to validation. You may not be able to break them down into individual tickers but you can still apply time series thinking to your development.

Additionally, these groupings give you insight to when your model does well and when it doesn’t. Building a separate model(s) on difficult eras and adding it to your ensemble may help you generalize better in the future.

Finally, if you want to dig deeper, modeling the eras individually can reveal differences in feature influence. You may find Eras grouped by FI perform better/worse with different levels of neutralization. Weaving into the above ensemble, models with varying FN, could have impacts on generalization as well as MMC.

---

### Post #7 — **wigglemuse** | 2021-02-12 16:01 UTC

Also we are scored on ranking on a era-by-era basis.

---

### Post #8 — **robbo_the_fossil** | 2021-02-12 16:55 UTC _(reply to #5)_

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/m/85e7bf/48.png) madlib:

> If there’s no relationship betweens the different era’s what is the use case for the multiple ere’s in the data?

Admittedly I am new and learning, but the way I see it is this… each era can be considered an independent sample of data with many features that result in a target.

Say I want to predict what kind of vehicle is coming down my road next. It is far away so I can only determine some coarse grain properties. I can see its color, I can see how fast it is going, I can see if its exhaust is clear or sooty. Yellow, slow, sooty features suggest the next vehicle will be a school bus (in North America anyway). If those features were red, fast and clear exhaust that would suggest a Ferrari. Now there is no way this data will tell me what the vehicle after the Ferrari is, so no point in trying to model yellow->red and slow->fast and soot->clean.

So, there is probably no pattern in the sequence of vehicles as they come down my road (maybe there is - you can always look for one) - but since Tournament is arranged the way it is my guess is the underlying assumption is stock prices are best predicted by current features, not long term feature patterns. The hedge fund people _probably_ know what they are doing. But then again Signals is now a thing, and something I know nothing about yet, so this is a whole different box I’m not ready to open yet.

---

### Post #9 — **wigglemuse** | 2021-02-12 17:06 UTC _(reply to #8)_

You are assuming though that such time-based things are not already baked into the features, and they may well be. At least some of them. Also sometime soon the # of features is going to explode (x10) with various versions of the same features and maybe some truly novel ones.

---

### Post #10 — **robbo_the_fossil** | 2021-02-12 17:26 UTC _(reply to #9)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/wigglemuse/48/3094_2.png) wigglemuse:

> You are assuming though that such time-based things are not already baked into the features, and they may well be.

You’re right. I am, and without justification. That hadn’t crossed my mind. It’s an interesting idea and you are probably right.

---

### Post #11 — **flipperpie** | 2021-02-16 14:06 UTC _(reply to #10)_

btw one other observation, the D&D stats are not in the correct order.

correct order  
strength  
dexterity  
constitution  
intelligence  
wisdom  
charisma

the current order is actually driving me a bit crazy. who puts intelligence first?  
![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=9)
