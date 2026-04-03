---
title: "Why are my TC scores worse after V4 data? Is volatility with a high TC score good for participants?"
category: Tournament
url: https://forum.numer.ai/t/why-are-my-tc-scores-worse-after-v4-data-is-volatility-with-a-high-tc-score-good-for-participants/5362
created_at: 2022-05-08T01:22:21.042000+00:00
last_posted_at: 2022-05-10T14:35:03.592000+00:00
posts_count: 10
views: 1013
tags: []
---

# Why are my TC scores worse after V4 data? Is volatility with a high TC score good for participants?

---

### Post #1 — **taiyaki** | 2022-05-08 01:22 UTC

Hi everyone! I would like to discuss the TC score in the numerai tournament with the community.

I started the numerai tournament from this January. This tournament was exciting to test my machine learning skills. It’s been very successful in the last four months and I’ve been able to win some medals. However, after the introduction of v4 data, the TC score has deteriorated significantly.

Specifically, the percentile of TC scores from rounds 303 to 308 was 72 to 92, which was very good. However, from rounds 309 to 314, it has deteriorated significantly from 0.6 to 26.  
Source: [Numerai](<https://numer.ai/taiyaki/submissions>)

[![payout](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/f/fada7c0cfd0911e89331f4d7974fd8b0d7dbb77d_2_662x500.png)payout974×735 104 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/f/fada7c0cfd0911e89331f4d7974fd8b0d7dbb77d.png> "payout")

During this period, the model has been trained on v3 data and has not changed. However, why is the tc score so fluctuating so far?

(1) Is it a problem with the versatility of the model which I trained?  
(2) Is it due to this recent market downturn?  
(3) Is it because I am using a model trained with v3 data? Need a model trained with v4 data?

I’ve doubled the TC in score multipliers because I’ve had good the TC scores so far (rounds 303 to 308). Of course, I think it’s my responsibility that I haven’t managed my risk, but is it good for tournament participants to face such a fluctuating TC score?

Even if you think alone, there are limits, so could you please let us know what you think? Thank you.

---

### Post #2 — **wigglemuse** | 2022-05-08 03:37 UTC

It has nothing to do with the v4 data if you haven’t changed your models. (The v4 data is too new for the reason to be “everybody else got better suddenly” by using it – that’s not it.) It has everything to do with the market and the market conditions – inflation, interest rate hikes, wars – all sorts of stuff going on just in the last few months that is quite novel. But even without that, it is quite ordinary – I stress VERY ORDINARY – that performance on any measure isn’t going to be the same all the time in some narrow range. For instance we’ve seen OVER AND OVER somebody dominate the leaderboard for months, staying in the top #3 on corr (when it was ranked on corr), and then one day abruptly drop and never to be seen again (at the top of the leaderboard anyway). And TC is probably our most volatile measure yet (although I haven’t actually looked at the data on that, but some others have indicated that).

So why have your TC scores dropped? Because that’s what happens – your assumption that they will stay the same is the problem. (But remember, only the last day of a round counts – things might look bleak for all the live rounds right now but only one resolves each week and a lot can change in a week.) Welcome to Numerai – keep on fighting.

---

### Post #3 — **taiyaki** | 2022-05-08 06:46 UTC _(reply to #2)_

Thank you for reply! First of all I want to thank you for your words. I am still a newbie when it comes to numerai and didn’t know that many people have been at the top of this tournament and suddenly drop.

I’m relieved to hear that others face the same problems like this. Additionally, I knew we needed a long-term stable model, not a short-term one. I think that is one of the secrets to getting through this tournament. First of all, I will make further improvements with that as my goal. After that, I hope that the results of the upcoming rounds will improve. Thanks.

---

### Post #4 — **jrb** | 2022-05-08 11:56 UTC

Post hoc ergo propter hoc

---

### Post #5 — **oraculum** | 2022-05-10 11:29 UTC

You say you didn’t change your model but I would double check it because your Corr with MetaModel metric did change significantly between round 308 and 309 (from 0.59 to 0.46) which indicates model change. Maybe some packages got updated on your machine and producing different results. If you keep old prediction files than check it if you can reproduce them exactly with your model, or if it can reproduce the validation metric it had when you trained it.  
But yeah, even without errors TC is wild sometimes.

---

### Post #6 — **wigglemuse** | 2022-05-10 13:29 UTC

[@oraculum](</u/oraculum>) is right – something did change at 308. Are you actually using v4 data on your v3 model somehow? (What is your data pipeline?)

---

### Post #7 — **taiyaki** | 2022-05-10 13:51 UTC _(reply to #5)_

Thank you for your advice and feedback! I will check my code. Please give me some confirmation time.

---

### Post #8 — **taiyaki** | 2022-05-10 13:52 UTC _(reply to #6)_

Thank you for your advice! I will check my code. Please give me some confirmation time. Thanks.

---

### Post #9 — **taori** | 2022-05-10 14:26 UTC

> your Corr with MetaModel metric did change significantly between round 308 and 309 (from 0.59 to 0.46)

Isn’t this suppose to happen with v4 data if a user retrain its model every week? Since new target values are added every week the model stats should change weekly.

---

### Post #10 — **wigglemuse** | 2022-05-10 14:35 UTC _(reply to #9)_

He said he was using v3 data and hadn’t changed his model – he was just noticing a change in performance around the time of the v4 release – there should be no reason for a significant change between 309 & 308\. And even in the case of weekly model updating with v4, unless you are only using the most recent data that’s still a big change from week to week – something must have changed in his code or pipeline that is screwing it up. Which is actually good news – maybe he can fix it and go back to getting some high TC.
