---
title: "How to solve the Numerai Tournament / lecture by Marcos Lopez de Prado"
category: Data Science
url: https://forum.numer.ai/t/how-to-solve-the-numerai-tournament-lecture-by-marcos-lopez-de-prado/3982
created_at: 2021-08-23T09:26:55.503000+00:00
last_posted_at: 2023-11-07T22:35:25.691000+00:00
posts_count: 13
views: 4419
tags: []
---

# How to solve the Numerai Tournament / lecture by Marcos Lopez de Prado

---

### Post #1 — **nyuton** | 2021-08-23 09:26 UTC

Hi,

Since I started selling my predictions, people ask, what do I do. [@ageonsen](</u/ageonsen>) posted a great lecture from Marcos Lopez de Prado a few months ago on how to solve the Numerai tournament with fairly detailed steps. I follow those steps!  
Seeing the current burning rate, I guess it didn’t get the attention neccessary.

Ageonsen is now #1 and I keep winning medals every week since I started following those instructions.  
I might have been simply lucky in the recent eras, but this lecture is certainly valuable. For the beginner and for the expert as well.

You can read it here:

[papers.ssrn.com](<https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3478927>) ![](https://cdn.ssrn.com/ssrn-global-header/11589acb53bc518aa22929bf19add113.svg)

### [Advances in Financial Machine Learning: Numerai's Tournament (seminar slides)](<https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3478927>)

Have fun!

---

### Post #2 — **profricecake** | 2021-08-27 15:31 UTC

Hi [@nyuton](</u/nyuton>) \- thanks for sharing.

The slides are a great starting point and outline a very sensible approach. But of course they leave implementation completely up to the reader. I’m curious what other references you found useful for getting into the specifics of topics like, say, feature engineering. Is the textbook one of them? Are there others of note?

Thanks again!

---

### Post #3 — **nyuton** | 2021-08-27 17:15 UTC _(reply to #2)_

Sure the textbook is great!  
Eye opening about the value of random forests. My best performing models are random forests. I stopped experimenting with NNs afterwards.

---

### Post #4 — **platemort** | 2021-08-31 12:59 UTC

Each week the era of the numerai_tournament_data.csv “test” column increases by one. How then can an era be a one month period?

---

### Post #5 — **liz** | 2021-08-31 21:03 UTC

great point, thanks!

---

### Post #6 — **nyuton** | 2021-09-01 06:37 UTC _(reply to #4)_

We start one era every week. There are 4 overlapping open eras.

---

### Post #7 — **platemort** | 2021-09-01 15:02 UTC _(reply to #6)_

I agree with that, but his paper repeatedly refers to the eras as monthly, like here “Train set: 120 months (eras)” on page 6. Shouldn’t that be 120 weeks?

---

### Post #8 — **nyuton** | 2021-09-01 15:59 UTC _(reply to #7)_

Oh, true. In the training set the eras are not overlapping. Yet…  
From 8. September we get the full dataset with overlapping eras.

---

### Post #9 — **javiermoral** | 2023-01-25 18:41 UTC

Hi nyuton, thanks for sharing. I am wondering if and how you apply stationarity tests. It makes no sense to apply test directly on the variables since each era reflects the same time period for all assets. Aggregating by eras and calculating the mean and then applying tests (e.g. Augmented Dickey-Fuller) seems too simple.

---

### Post #10 — **andralienware** | 2023-01-26 03:34 UTC _(reply to #9)_

I think that’s actually exactly what he means, but not necessarily to the variables, but to the variables’ correlation with the target.

---

### Post #11 — **javiermoral** | 2023-01-26 12:32 UTC _(reply to #10)_

I’ve aggregated by eras, computed the spearman corr of each era, created a series for each feature (v.4.1) on its correlation and then applied Augmented Dickey-Fuller) on each series. Result, not a single null hypothesis rejected. All features are stationary following this apporach.

---

### Post #12 — **andralienware** | 2023-01-26 14:58 UTC _(reply to #11)_

It may also be more important if you are competing in the signals competition.

---

### Post #14 — **f58c** | 2023-11-07 22:35 UTC

![](http://forum.numer.ai/user_avatar/forum.numer.ai/nyuton/48/687_2.png) nyuton:

> Ageonsen

thanks for the paper!
