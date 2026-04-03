---
title: "Numerai rounds to era"
category: Tournament
url: https://forum.numer.ai/t/numerai-rounds-to-era/5891
created_at: 2022-11-27T04:25:24.279000+00:00
last_posted_at: 2024-01-28T19:27:21.632000+00:00
posts_count: 9
views: 1658
tags: []
---

# Numerai rounds to era

---

### Post #1 — **dzheng1887** | 2022-11-27 04:25 UTC

Hi, is there a mapping from the numerai rounds, like 339 resolved last week, to training/validation data eras? Round 1033 seems to be the latest era with main target not NaN. So I assume that round corresponds to 339? Rounds 1034 to 1038 inclusive all have NaN for the main target, so I presume they correspond to Numerai Rounds 344, 349, 354, 359, 364?

Thanks.

---

### Post #2 — **profricecake** | 2022-11-29 04:01 UTC

My vote is for Numerai to simply include a “round” column that has the integer round number where appropriate and N/A everywhere else. So many of us are trying to work with this mapping, we might as well get it straight from the source.

---

### Post #3 — **kayeffnumeraitor** | 2022-11-29 21:11 UTC

I think it is like this, but please confirm for yourself
    
    
    def era_to_saturday_round(era):
        saturday_round = era - 695
        if saturday_round > 339:
            saturday_round = 339 + 5*(saturday_round - 339)
        return saturday_round
    
    def saturday_round_to_era(saturday_round):
        if saturday_round > 339:
            return 339 + 695 + int((saturday_round - 339)/5)
        else:
            return saturday_round + 695

---

### Post #4 — **dzheng1887** | 2022-11-29 23:06 UTC

Thank you! This helps knowing others think similarly.

---

### Post #5 — **eleven_sigma** | 2023-02-28 19:13 UTC

Latest dataset has the responses of era 1046, that using the conversion formula correspond to round 399.  
The last round resolved is at this time 404.  
So we have a delay of ‘one’ additional (now it is five as rounds are daily) weekly round.  
Why this delay? if data are known on Thursday they could be in the dataset on Saturday…

If era transformation is correct, then we need to predict round 429 using rounds up to 399, without the targets of 404, 409, 414, 419 and 424.

Could someone that have analyzed the data availability confirm this, please?

---

### Post #6 — **kayeffnumeraitor** | 2023-03-01 10:06 UTC _(reply to #5)_

So I am doing a model that always includes the latest available new data, and I asked this question in rocket chat as well but did not receive an answer.

But yes I also found that there are always five eras with missing targets instead of four between live and latest era with targets.

---

### Post #7 — **wigglemuse** | 2023-03-01 15:05 UTC

The conversion math is correct, yes (I have verified this) – the data just isn’t included as fast as hypothetically possible. (And sometimes weeks are delayed and then two added the next week, so you even can’t count on there being new data with targets every week.) There has never been an intention for the data to be available absolutely as fast as possible, and only fairly recently that newer data (with targets) would be available at all. (Signals is always there for those that want to use very recent data, but you gotta go get it yourself.)

---

### Post #8 — **klaes_ashford** | 2024-01-28 15:03 UTC

![](http://forum.numer.ai/user_avatar/forum.numer.ai/kayeffnumeraitor/48/991_2.png) kayeffnumeraitor:

> 
>     def era_to_saturday_round(era):
>         saturday_round = era - 695
>         if saturday_round > 339:
>             saturday_round = 339 + 5*(saturday_round - 339)
>         return saturday_round
>     
>     def saturday_round_to_era(saturday_round):
>         if saturday_round > 339:
>             return 339 + 695 + int((saturday_round - 339)/5)
>         else:
>             return saturday_round + 695
>     

Just jumping into this and wanted to double check that this is still correct?

---

### Post #9 — **wigglemuse** | 2024-01-28 19:27 UTC _(reply to #8)_

Yes, that is correct.
