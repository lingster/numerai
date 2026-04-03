---
title: "How does training data and validation data relate in 'time'?"
category: Tournament
url: https://forum.numer.ai/t/how-does-training-data-and-validation-data-relate-in-time/3161
created_at: 2021-05-01T20:39:30.614000+00:00
last_posted_at: 2021-05-06T19:44:11.889000+00:00
posts_count: 9
views: 1888
tags: []
---

# How does training data and validation data relate in "time"?

---

### Post #1 — **slowmoe** | 2021-05-01 20:39 UTC

Complete n00b here.

I’ve been playing with the idea of engineering features that tell you something about the era of a point. After some toying, it seems to me that whatever function describes the different regimes of different eras is somewhat continuous on large enough scales. So me thinks nice, lets think more. When I look at the regimes in the validation set (naughty, I know), they seem to connect seamlessly to the last eras of the training set. Almost as if they are directly connected in time. Does anybody know if that might be true?

To qualify what I mean with regimes of eras: when you compute the covariance matrix of all features per era, you get a bunch of rather beautiful 310x310 pixel art. If you use matrix norm as metric, those pictures vary pretty continuously over the training and validation set.

Curious to hear what you think.

---

### Post #2 — **wigglemuse** | 2021-05-01 21:03 UTC

Yep. Training data eras 1-120 represent 10 years (1 era = 1 month). So val eras 121-132 are simply the following year. Then a large gap to other validation eras 197-212 which are from fairly recent times.

---

### Post #3 — **slowmoe** | 2021-05-02 09:11 UTC _(reply to #2)_

I see, that makes a lot of sense. Thanks! Is this documented somewhere that I missed?

---

### Post #4 — **ml_is_lyf** | 2021-05-02 09:50 UTC _(reply to #3)_

Unfortunately most stuff like this isn’t documented. You can pick this kinda stuff up though from Arbitrage’s office hours. I just watched every video on the Numerai YouTube channel, takes some time but I would recommend it, just watch them while your models are training ![:slight_smile:](https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=13)

![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/2/2ce6ea2412f2d1fa7dab59c1a3f756aff246b2ed.png) [YouTube](<https://www.youtube.com/c/Numerai/videos>) ![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/080e9cd2a5cca45023fa98526e730e058604dd65_2_500x500.jpeg)

### [Numerai](<https://www.youtube.com/c/Numerai/videos>)

An artificial intelligence hedge fund built by a community of anonymous data scientists

---

### Post #5 — **jimmy_woodford** | 2021-05-02 11:24 UTC

Here’s what I’ve found (take with a grain of salt):

If we assume that era1 is January 2003, then the monthly data that we get is Jan 03 - Dec 12 in train and Jan 13 - Dec 13 & Jun 19 - Sep 20 in val. When I used this month variable in my models, it consistently improved performance by 5-10%.  
But what about weeks? If numbering is consistent, for weeks we should know exactly when they start and when they end, since live eras become test eras after completion. If this is true, era575 is week 2 2014 (starting January 9, ending February 5), and so on.  
Unfortunately, I think I never managed to bring these findings together, and my models including month as a variable performed poorly on live. I may have made a mistake. Numerai’s numbering might be inconsistent. Or since weeks often overlap months, the performance boost on monthly data may not carry over to weekly data.

In any way, I think Numerai should provide more information to let us try to find some temporal relations. And give us weekly data to train and validate.

---

### Post #6 — **gammarat** | 2021-05-02 14:04 UTC

I quite agree, at least in some ways.FWIW, I really like your idea of turning the covariance matrices into pixel art. Maybe Numerai should produce NFTs from the covariance matrices for each live era - a big one for the over all round winner, smaller ones from the matrices of combinations of feature groups - and award them to the high scorers? I digress.

Anyway, I’m personally intrigued by how each era relates to the others; so I’ve been exploring that over in the the [Analyzing Training Data](<http://forum.numer.ai/t/analyzing-training-data/3143/3>) thread. If you look at the evolution of the averaged STD for the feature groups Charisma and Strength from the first training set through to the live round there’s an interesting trend.

---

### Post #7 — **slowmoe** | 2021-05-02 21:04 UTC

yes, I should definitely listen to the podcast more. Again, I am new and there is so much left for me to explore.  
I think numbering months and weeks is somewhat problematic since the era length is not constant at all. There might be ways to mitigate that though.

here is a pic of the “average covariance” of the training data I came up with btw.  


[![featurecorrs_baseline](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/e19e3245e7c56721b6674821cbc515b4fbdfa7de_2_690x460.png)featurecorrs_baseline1500×1000 196 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/e19e3245e7c56721b6674821cbc515b4fbdfa7de.png> "featurecorrs_baseline")

---

### Post #8 — **nrichers** | 2021-05-06 19:01 UTC

![](http://forum.numer.ai/user_avatar/forum.numer.ai/jimmy_woodford/48/2479_2.png) jimmy_woodford:

> But what about weeks? If numbering is consistent, for weeks we should know exactly when they start and when they end, since live eras become test eras after completion

4-4-5 calendar may be useful to align week/month columns

[en.wikipedia.org](<https://en.wikipedia.org/wiki/4%E2%80%934%E2%80%935_calendar>)

### [4–4–5 calendar](<https://en.wikipedia.org/wiki/4%E2%80%934%E2%80%935_calendar>)

The 4–4–5 calendar is a method of managing accounting periods, and is a common calendar structure for some industries such as retail and manufacturing. It divides a year into four quarters of 13 weeks, each grouped into two 4-week "months" and one 5-week "month". The longer "month" may be set as the first (5–4–4), second (4–5–4), or third (4–4–5) unit. Its major advantage over a regular calendar is that each period is the same length and ends on the same day of the week, which is useful for plan...

---

### Post #9 — **jimmy_woodford** | 2021-05-06 19:44 UTC _(reply to #8)_

Interresting, thanks ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=9) . I’d really like to get a way to add a time variable to the mix since it so clearly works in the training/val data.
