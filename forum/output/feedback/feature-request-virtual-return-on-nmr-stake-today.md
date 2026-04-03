---
title: "Feature request: (virtual) return on NMR stake today"
category: Feedback
url: https://forum.numer.ai/t/feature-request-virtual-return-on-nmr-stake-today/3298
created_at: 2021-05-14T14:10:49.115000+00:00
last_posted_at: 2021-05-16T13:24:48.774000+00:00
posts_count: 10
views: 1240
tags: []
---

# Feature request: (virtual) return on NMR stake today

---

### Post #1 — **qeintelligence** | 2021-05-14 14:10 UTC

Hi guys, i am one of the newbies on the tournament so it could be the following question may already have asked before but will try it anyway ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=9)

I noticed that since a couple of weeks the minimum NMR for staking is set to 3 which is currently around 180 dollars give or take. As for a lot of the newcomers this is quite a high price to pay to start staking but i understand the reasoning behind it with the gas prices at the moment.

I am wondering though if it would be possible to at least have like a (virtual) return on NMR stake today visible for your models. This would be the return you would have if you would have actually staked something on this model. The reasoning behind it is that i think it will keep a lot of the newcomers on the tournament and not be already discouraged from the start. Also you can build up more confidence on your model instead of only looking at the diagnostics results.

I think technically this should be possible for the non-staked models, though i think the team should tell us that. What do you think?

Gr. QE

---

### Post #2 — **bensch** | 2021-05-14 16:59 UTC

Would be nice especially for signals where I have no staking credits

---

### Post #3 — **ml_is_lyf** | 2021-05-14 18:41 UTC

When I started the tournament I was also really interested in 1-day returns and thought they gave a good idea of how well I was doing. But I’d recommend having a read of this post:

![](http://forum.numer.ai/user_avatar/forum.numer.ai/wigglemuse/48/3094_2.png) [Relationship of daily round correlations to final round correlations](<http://forum.numer.ai/t/relationship-of-daily-round-correlations-to-final-round-correlations/1176/2>) [Tournament](</c/tournament/7>)

> The first part of your question is unclear to me, but it sounds like you may have a misunderstanding of what the scores mean. In any case, can you re-phrase or give an example so we are sure what you are talking about? And as far as the API, again not sure what you are referring to? (I pull the scores from the API every day no problem. We are talking about the Numerai tournament, not signals, right?) 

TLDR is that your 1-day returns don’t actually really mean anything useful. As your predicting 4 weeks into the future, so your correlations intra-round don’t really mean anything, and hence neither do your 1-day returns.

You should be getting a round summary email at the end of each resolved round, which tells you the percentage return you would have got that round if you had been staking. That’s really the incentive your describing. Trying to incentivise with intra-round performance would be a bit misleading.

We just need to have new users to have patience ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=12) Having said it would be good if we could tell them somewhere to have patience for this first email, as this isn’t explained in the documentation, you only find out after 4 weeks when you get your first email

---

### Post #4 — **qeintelligence** | 2021-05-14 19:14 UTC _(reply to #3)_

Hi [@ml_is_lyf](</u/ml_is_lyf>) , thanks for the reading tip and i absolutely agree that 1-day returns by itself don’t mean anything, and a 4-week summary will give a better more realistic idea about your model. Probably you would have to wait longer up until 20 weeks to a year if you want play it really safe ![:slight_smile:](https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=13) i don’t know if i can wait that long lol.

That said, i am around for over 7 weeks now, so i did get that email and it doesn’t tell me what i would have made in terms of percentage, it only tells the CORR and MMC, Payout stays at 0 (ofcourse).  
See my round 256 example below, this one is unstaked:

[![roundsummary](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/ef12dd6c172085af9be29009484b5fa26fe65f74.png)roundsummary419×466 20.9 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/ef12dd6c172085af9be29009484b5fa26fe65f74.png> "roundsummary")

I am not sure yet if you can calculate a precise return based on only CORR and MMC from the round summary. So maybe it would be interesting to add the return in the round summary, even if you didnt stake anything?.

---

### Post #5 — **qeintelligence** | 2021-05-14 19:14 UTC _(reply to #4)_

Also for some reason the layout of the email looks weird, the numbers are not correctly spaced but for now i guess the problem is on my side.

---

### Post #6 — **ml_is_lyf** | 2021-05-14 19:28 UTC _(reply to #4)_

Ah sorry, you’re right, I misremembered. They really should have that then! Not sure if they still do, but they used to give you some free NMR (think it was 0.01) for your first model. Check the stake management panel to see if you have any credits. They might have stopped that with the sky-high gas prices though.

So you can actually calculate it if you put your round CORR in an excel spreadsheet. Your return at week n is your stake at week n-4, multiplied by CORR at week n. Then your stake at week n is your stake at week n-1 plus your returns at week n. If your staking on MMC too, you just add that to your CORR in the calculation

---

### Post #7 — **qeintelligence** | 2021-05-14 19:39 UTC _(reply to #6)_

No they still have that 0.01 NMR indeed, it is not automatically used with your first model (i used it later with another model). I guess it would be a nice feature if they did a preliminary calculation in the round summary. I was planning do make a nice BI overview with all the data you can get from the backend api, i will just add that calculation also in it. thanks for the answer!

---

### Post #8 — **aventurine** | 2021-05-14 22:49 UTC

Staking paper trading. I like!

---

### Post #9 — **ml_is_lyf** | 2021-05-16 10:45 UTC _(reply to #7)_

No worries. I’ve also now written a notebook that calculates all this for you. It also examines your model performance for live rounds so should help new users better understand how they’re doing. I would still encourage only looking at resolved rounds though as discussed above.

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/m/e56c9b/48.png) [Notebook to visualize historic model performance and see effect of different MMC multipliers and payout factors](<http://forum.numer.ai/t/notebook-to-visualize-historic-model-performance-and-see-effect-of-different-mmc-multipliers-and-payout-factors/3316>) [Tournament](</c/tournament/7>)

> The compare model graphs on our user pages are really helpful for getting an idea of how our models are performing. But they only show cumulative scores, so we don’t see the compounding effect. Also, we don’t see the combined performance of our stake on CORR and MMC, as there is no option to plot CORR+MMC. To bridge this gap I made a notebook to do all of the above. You can tabualise how your model is performing like so: pc.tabualise_performance(model_name="ml_is_lyf", start_round=251, inclu…

---

### Post #10 — **qeintelligence** | 2021-05-16 13:24 UTC _(reply to #9)_

thanks! i am going to check it out this week
