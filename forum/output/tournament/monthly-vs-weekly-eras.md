---
title: "Monthly vs weekly eras"
category: Tournament
url: https://forum.numer.ai/t/monthly-vs-weekly-eras/3799
created_at: 2021-07-20T11:03:13.276000+00:00
last_posted_at: 2021-07-21T09:50:01.793000+00:00
posts_count: 4
views: 1101
tags: []
---

# Monthly vs weekly eras

---

### Post #1 — **eleven_sigma** | 2021-07-20 11:03 UTC

What does exactly means monthly and weekly here?

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/forum.numer.ai/master_key/48/3343_2.png)

[Validation 2 Announcement](<http://forum.numer.ai/t/validation-2-announcement/166>) [Announcements](</c/announcements/8>)

> Validation 2 [New Tournament Data File](<https://drive.google.com/file/d/1Wkp8hidVNn2nF0Xe-RaFShi_PgjdIQVd/view?usp=sharing>) [Compressed Download](<https://drive.google.com/file/d/1vApYt6rqFg4gGRhMYWtdLHW6M-NfsACz/view?usp=sharing>) [Example Predictions](<https://drive.google.com/file/d/1ZHy_FkA27vm51Kt6Rz9uFHNOTyrVehMm/view?usp=sharing>) This is a file that shows what the tournament file would look like for the most recent round (207). Feel free to download and double-check that it doesn’t affect your pipeline. Summary We will be giving out 10 additional eras of validation data (features + targets). [[image]](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/0ce37d35c2282775af4e99ed6ef6f626eec09a0a.png>) Objective The current validation data is known to be “easy”. Models trained on the training data tend to perform very well on the validatio… 

Monthly means that between the beginning of two consecutive eras there is one month (or four weeks)?  
Or monthly means that the length of period included in the era is a month?  
Or monthly means that the performance is measured one month ahead?

And weekly means that between the beginning of two consecutive eras there is one week?  
Or weekly means that the length of period included in the era is a week?  
Or weekly means that the performance is measured one week ahead?

---

### Post #2 — **andy_shaps** | 2021-07-20 14:31 UTC

Someone correct me if I’m wrong but I believe that weekly or monthly refers to what length each era is. So for example in the proposed val 1, the eras refer to months whereas the test1 era will refer to weeks. this is why each era in a “weekly” section is much higher than an era from a “monthly” section.

Hope this makes sense and helps

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/9/90f110f2b4dbdc36e647b9645ac26632021b7386.png)image1386×990 19.8 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/9/90f110f2b4dbdc36e647b9645ac26632021b7386.png> "image")

---

### Post #3 — **eleven_sigma** | 2021-07-20 17:36 UTC _(reply to #2)_

The only thing that could makes sense for me is that monthly means that the beginning between eras are spaced by four weeks and the weekly means that the beginning are spaced only by one week.  
That is, in one year of training there are 13 eras (13 x 4 = 52 weeks) and in a year if test there are 52 eras.  
This is very importat because if this is true, in training eras don’t overlap, but in test do.

---

### Post #4 — **andy_shaps** | 2021-07-21 09:50 UTC _(reply to #3)_

Sorry if I’m not being clear, there are 120 eras in the training cohort, given that we have been told this is 10 years of data, it is reasonable to assume that each monthly era is equivalent to one month (out of 12, rather than 4 weeks out of 52). If this is the case (which i think it is), then the weekly eras will overlap the monthly eras in the test data (only by a bit).

so era 120 of training data is month 120. era 121 in val1 is month 121, through to era 212 in val2 which is month 212. test eras (which are in between val eras) are weekly so era 575 of test1 is actually a monthly era of 132 and then 576 is a monthly era of 132.5, 577 is monthly 132.8. and so on.

this is given the basis that there are 52.1429 weeks in a year, which when divided by 12 months = 4.34524. so divide each “weekly” era by this number to get the monthly era.

At least, this is the basis i have been working off and would love someone to comment if they believe it to also be true or different?

Edit: they said they will change this format soon so that we have pretty much all the data in training, mostly as weekly eras, thus meaning this could change relatively soon
