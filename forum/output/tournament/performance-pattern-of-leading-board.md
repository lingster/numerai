---
title: "Performance Pattern of leading board"
category: Tournament
url: https://forum.numer.ai/t/performance-pattern-of-leading-board/3809
created_at: 2021-07-21T09:21:21.505000+00:00
last_posted_at: 2021-07-29T14:28:38.690000+00:00
posts_count: 13
views: 1407
tags: []
---

# Performance Pattern of leading board

---

### Post #1 — **autratec** | 2021-07-21 09:21 UTC

I looked performance pattern of top 5 on leading board. They r almost same with some minor differences:

[![Screenshot_20210721-171552_Chrome](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/6/6590115df97e2e7801724ebe7d3ad1aaa4835559_2_645x500.jpeg)Screenshot_20210721-171552_Chrome1080×837 122 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/6/6590115df97e2e7801724ebe7d3ad1aaa4835559.jpeg> "Screenshot_20210721-171552_Chrome")

  


[![Screenshot_20210721-171103_Chrome](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/7/73276f0f368ad1579b81fe05b8bf778fe61c76d1_2_651x499.jpeg)Screenshot_20210721-171103_Chrome1080×829 121 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/7/73276f0f368ad1579b81fe05b8bf778fe61c76d1.jpeg> "Screenshot_20210721-171103_Chrome")

  


[![Screenshot_20210721-171039_Chrome](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/2/277155a862e41f805bf65932d4f47d10b93cbeac_2_657x500.jpeg)Screenshot_20210721-171039_Chrome1079×820 122 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/2/277155a862e41f805bf65932d4f47d10b93cbeac.jpeg> "Screenshot_20210721-171039_Chrome")

  


[![Screenshot_20210721-171008_Chrome](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/5/54566e1e030392efdbe82c2e1ccf8b7045e34a78_2_646x499.jpeg)Screenshot_20210721-171008_Chrome1079×835 123 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/5/54566e1e030392efdbe82c2e1ccf8b7045e34a78.jpeg> "Screenshot_20210721-171008_Chrome")

  


[![Screenshot_20210721-170946_Chrome](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/7/75ebcbd5a53e1cb88d2a8776742708767d5d6f0e_2_673x500.jpeg)Screenshot_20210721-170946_Chrome1079×801 119 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/7/75ebcbd5a53e1cb88d2a8776742708767d5d6f0e.jpeg> "Screenshot_20210721-170946_Chrome")

Assume investor can stake on different model to reduce the risks. But not feasible here.

What does it mean ?

Everyone using the same model - decision tree, or there is one successful model on the long run ?

---

### Post #2 — **gammarat** | 2021-07-21 13:21 UTC

I think that it probably reflects more the orderliness of the underlying markets with respect to training data that is years out of date.

---

### Post #3 — **taori** | 2021-07-21 15:28 UTC

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/a/6bbea6/48.png) autratec:

> What does it mean ?

  * Same user(s) who submitted slight variations of the same model?

  * The model is an obvious one, so multiple users thought at the same idea that works well at this specific point in time?

  * It’s the results of using the same training data set?

---

### Post #4 — **sirmobius** | 2021-07-22 06:53 UTC

Models trained with only one or two features?

---

### Post #5 — **autratec** | 2021-07-22 07:14 UTC

based on the inputs, it could due to two main factors:

  1. same validation and training data was used - this part of rule of tournament and provided by numerai.
  2. similar ML model was used - XGB Tree

---

### Post #6 — **ssh** | 2021-07-22 16:09 UTC

take a closer look at the first 100 models and most of them will demonstrate the same pattern. I believe that the nature of this pattern is the period shocks so-called “good” or “bad” eras - that are easy or difficult to predict on the current dataset.

---

### Post #7 — **gammarat** | 2021-07-22 18:21 UTC _(reply to #5)_

I’d go with your #1 but not #2 as I don’t use any ML techniques, it’s all old-school analysis and stats _pour moi_ , and I have a similar overall pattern.  
I think what would really help would be if Numerai simply started providing the target values for the test data once the test data was a year or so old.

---

### Post #8 — **autratec** | 2021-07-22 23:15 UTC _(reply to #7)_

Surprised to learn that you r not using ML. What kind of old school analysis tool u r using ? Linear regression ?

---

### Post #9 — **gammarat** | 2021-07-22 23:54 UTC _(reply to #8)_

I actually first started working with various transform methods + simple inversion, and moved on from there. I guess my workhorse routines now are principal components analysis, kernel density estimation, and Gaussian mixtures. I think it’s more a question of _habitude_ than anything else; I’ve been using tools like those for decades, and I’m comfortable with them (I’m old enough to be one of the early adopters of [_Numerical Recipes_](<https://en.wikipedia.org/wiki/Numerical_Recipes>), back when 386s and math coprocessors were the hottest things on the block ![:laughing:](http://forum.numer.ai/images/emoji/twitter/laughing.png?v=9) ).

---

### Post #10 — **jrb** | 2021-07-23 09:55 UTC _(reply to #9)_

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/forum.numer.ai/gammarat/48/3281_2.png) gammarat:

> back when 386s and math coprocessors were the hottest things on the block

Thanks for the trip down the memory lane! My first PC was a 486DX4-100, but my school had a couple of 386s before that, and I’d even managed to get a copy of the Intel 386 Programmer’s Reference Manual, with some difficulty. I’d spent a lot of time with those 386s after school, learning to write DOS TSRs with TC and TASM. ![:slight_smile:](https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=14)

---

### Post #11 — **fireball** | 2021-07-27 22:19 UTC

![](https://avatars.discourse-cdn.com/v4/letter/a/6bbea6/48.png) autratec:

> What does it mean ?

[![Survivorship-bias.svg](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/c/c69d9dc2c1558edcd17caf238983792b75fe2e45_2_670x500.png)Survivorship-bias.svg2560×1908 297 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/c/c69d9dc2c1558edcd17caf238983792b75fe2e45.png> "Survivorship-bias.svg")

---

### Post #12 — **mattiasl** | 2021-07-29 11:21 UTC _(reply to #11)_

That’s an old classic! Modeling enough patterns that survive, one can see those patterns that did not survive…

In this instance, they mapped during world war 2 all the bullet holes that were on the airplanes that came back. They used this bullet hole map to decide to re-enforce the airplanes in the areas which did not have red dots - presumably airplanes that were hit in those areas went down and did not make it back!

---

### Post #13 — **jrb** | 2021-07-29 14:28 UTC _(reply to #12)_

[en.wikipedia.org](<https://en.wikipedia.org/wiki/Abraham_Wald>)

![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/7/77d5bd0224155759aed2a086e8204e817ad1c1e4.jpeg)

### [Abraham Wald](<https://en.wikipedia.org/wiki/Abraham_Wald>)

Abraham Wald (/wɔːld/; Hungarian: Wald Ábrahám, Yiddish: אברהם וואַלד; (1902-10-31)31 October 1902 – (1950-12-13)13 December 1950) was a Jewish Hungarian mathematician who contributed to decision theory, geometry and econometrics, and founded the field of sequential analysis. One of his well-known statistical works was written during World War II on how to minimize the damage to bomber aircraft and took into account the survivorship bias in his calculations. He spent his research career Wald was...
