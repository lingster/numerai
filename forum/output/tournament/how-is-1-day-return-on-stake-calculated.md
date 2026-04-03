---
title: "How is 1 day return on stake calculated?"
category: Tournament
url: https://forum.numer.ai/t/how-is-1-day-return-on-stake-calculated/2422
created_at: 2021-03-17T20:49:14.059000+00:00
last_posted_at: 2021-03-18T18:51:59.829000+00:00
posts_count: 4
views: 1288
tags: []
---

# How is 1 day return on stake calculated?

---

### Post #1 — **ml_is_lyf** | 2021-03-17 20:49 UTC

Hi,

I was just wondering how 1-day return on stake is calculated for the leaderboard?

For example, consider integration_test_7 which has a 2.5% return on stake today (17th March). The live rounds are:

<https://numer.ai/integration_test_7/submissions/251>  
<https://numer.ai/integration_test_7/submissions/252>  
<https://numer.ai/integration_test_7/submissions/253>  
<https://numer.ai/integration_test_7/submissions/254>

The model is only staked on correlation. So the 1-day-return must be calculated from its correlation on those rounds today, or some calculation of its projected payout today compared to yesterday. But I can’t figure out the exact equation. Can anyone explain how it’s calculated?

Thanks in advance.

---

### Post #2 — **wigglemuse** | 2021-03-17 21:19 UTC

I think they are using the actual staked amounts for each round (along with mmc if it is turned on), so you’d probably have to look at an account with a more significant stake to make sense of it (or pull that data from api). But then I think you just look a what their projected payouts were today relative to yesterday, or maybe it is just the single day return? (That would make more sense probably.) Now I’m gonna have to go do the math…

---

### Post #3 — **profricecake** | 2021-03-17 23:14 UTC

To my eyes it looks like they are computing the difference between today’s daily corr estimate (aka “score”) and yesterday’s daily corr estimate and summing those deltas over all four rounds. Since this model is staked on corr it appears they’re not bothering including any mmc deltas.

For each of the rounds you linked I calculated the following corr deltas between 3/16 and 3/17:
    
    
    251:  0.0001 
    252: -0.0013
    253:  0.0118
    254:  0.0142
    
    sum = 0.0248

---

### Post #4 — **ml_is_lyf** | 2021-03-18 18:51 UTC

Thanks for the help guys.

Good eye [@profricecake](</u/profricecake>), I tried this today and it worked there too. So seems likely this is the calculation.

Coincidentally today is the start of a new round (18th March). So now we’re using 255 to calculate the score instead of 251.

<https://numer.ai/integration_test_7/submissions/255>

I naively assumed that given this is the first day of the round, you take the previous days value as 0, which seems to give the right number.
    
    
    252: 0.0055
    253: -0.0045
    254: -0.0009
    255: 0.0103
    
    sum = 0.0104
    

This is quite interesting, as it probably explains why on the 11th there was a huge spike in 1-day returns as the new round started. Worth bearing in mind for the future that 1-day returns on Thursday’s are probably going to be more volatile.
