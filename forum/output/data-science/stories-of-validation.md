---
title: "Stories of Validation"
category: Data Science
url: https://forum.numer.ai/t/stories-of-validation/70
created_at: 2020-03-25T09:11:19.093000+00:00
last_posted_at: 2020-03-28T16:49:47.391000+00:00
posts_count: 6
views: 2628
tags: []
---

# Stories of Validation

---

### Post #1 — **bor1** | 2020-03-25 09:11 UTC

Maybe we can share some experiences on how to do a good validation, that is - how to get your validation holdout eras be a reliable indicator of how well your model will perform on live data.

It has been a mixed bag for me. One of my long-running stable models (18 weeks) offered a good opportunity to see if the 51 eras that I held out for validation were showing the same distribution of scores as my live scores. Those 51 eras weren’t selected at random, but spread out over an axis based on a second model - one that is trained on a small subset of eras and performs very well during times of no burn, and very poorly during burns (called **goodtimes**). So the 51 eras I used as validation sort of cover the range of eras that numer.ai provides in a more equal way than if you would just select 51 eras at random.

Basically what you expect if validation eras and live eras are similar [and as far as I can tell, that is still true - live is a subset on the y-axis scale here that overlaps with the validation eras], is that the two point-clouds are hard to distinguish.

Sadly, for model **Thirteen** , that wasn’t the case. About half the live eras performed considerable worse than anything I had seen in the validation dataset (top half). Weirdly enough, I have another model - **badtimes**. For that one, validation and live are spot-on (bottom half). _(The figure uses the performance of the**goodtimes** model for every era to spread out the points on the Y-axis. If you only have the validation and live scores of your model to look at how the two match up, you can make two density plots and see if they overlap. But I find it convenient to have this second axis to visualize the data with)_  


[![thirteen](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/1d5c68fad226fb1887e1fe6ebc8d535e334c6131_2_326x500.png)thirteen1032×1580 58.7 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/1d5c68fad226fb1887e1fe6ebc8d535e334c6131.png> "thirteen")

It is how well live and validation matches for my **badtimes** model that gives me confidence that the data that numer.ai is providing is not too old to be useful. The live scores that badtimes gets, based on training on 18 eras (18 different eras than goodtimes is trained on) matches the validation scores I have for badtimes as well, and the part to the bottom right where the live scores extend into territory not covered by the validation eras, is where the training eras of badtimes are.

Lessons learned. **Thirteen** was an attempt at getting a model that does well during bad (burn) times and good times. It was a bit more complicated than shown here - After I had a model that I liked, and validation didn’t look too bad, I ran the model two more times, with different sets of holdouts picked at random, and then averaged all three models together. The other two model runs performed worse than the first model run, in terms of validation performance. But together, things looked even better for validation (almost all eras positive). In retrospect, I should have discarded the first model (where validation didn’t look too bad) - as by iterating on models until I had one where validation didn’t look bad, I for sure overfitted.

I have no clue why my extreme models (both **goodtimes** and **badtimes**) have such a good correspondance between live and validation, but one lesson learned is that spending time on understanding the relationship between your validation scores and your live scores is time well spend. So keep one or two models around for a long time to check if your validation scores match up to the live scores!

---

### Post #2 — **master_key** | 2020-03-25 19:31 UTC

Great write up! Thanks for being the first to post.

Any chance that we could get a clue where bor3 fits in here?  


[![Screen Shot 2020-03-25 at 12.30.13 PM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/83b22ed8e63caac6561e991126c7e42b96167ca3_2_689x352.png)Screen Shot 2020-03-25 at 12.30.13 PM2296×1174 204 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/83b22ed8e63caac6561e991126c7e42b96167ca3.png> "Screen Shot 2020-03-25 at 12.30.13 PM")

It has been doing extraordinarily well during tough burn times, while still managing respectable scores during good times. I would love to hear if you expected this type of behavior or not from it, if it is a goodtime or badtime model, if it’s one of the blends, etc.

---

### Post #3 — **bor1** | 2020-03-26 12:57 UTC

Looked into my logs _(protip - keep a log of what you do. Over long periods, you need something to remember what you did!)_. This is the history of BOR3. Basically, in round 196 (january 25th) I switched to the BADTIMES model, cause of the virus, and in round 197 and 200 I switched the BADTIMES model to my BOR1 account (but found it hard to have the confidence to keep it there - when these models are wrong, they are really wrong, which burns).
    
    
    BOR3 has been 
    172-195:GOODTIMES,
    196:BADTIMES,
    197:DEFUNCT-LESSEXTREMEBADTIMES,
    198:BADTIMES,
    199:BADTIMES,
    200:DEFUNCT-MIDDLETIMES,
    201:BADTIMES,
    202:BADTIMES,
    203:BADTIMES,
    204:BADTIMES.
    

Here are **goodtimes** and **badtimes** live scores minus the switching account switching:  


[![goodtimes-badtimes](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/2f6fb8e56cd06896bcfea16d10064106b183be5f_2_690x314.png)goodtimes-badtimes1638×747 79.2 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/2f6fb8e56cd06896bcfea16d10064106b183be5f.png> "goodtimes-badtimes")

  
Both of them are trained on a different set of 18 eras, but they pretty well look like a p/1-p model. I wonder if it is related to the _class 0 vs rest_ & _class 1 vs rest_ models from the [python notebook](<https://github.com/numerai/example-scripts/blob/master/analysis_and_tips.ipynb>)…

---

### Post #4 — **mdo** | 2020-03-27 00:10 UTC

[@bor1](</u/bor1>) I’m not clear why you think your goodtimes and badtimes models have good correspondance between live and validation. If the two models are nearly p/1-p all their scores for live and validation would _have to_ lie nearly along a line as they do on your plot. I don’t think that scatter plot tells you anything other that they are nearly p/1-p

---

### Post #5 — **bor1** | 2020-03-27 07:47 UTC _(reply to #4)_

hmm. I think you are right there for the goodtimes and badtimes model, as they are also the coordinate system on which I plot where in space live vs validation fall. Riddle solved. For models that aren’t part of the coordinate system, the spatial plotting might still work.

So what other tools do you think we have to check for the consistency in scores between live and validation? Density distribution of scores is a bit problematic in that it takes a long time to gather enough datapoints, and as Richard says, we are now in a not so good time for quant hedgefunds, versus the time period that is our training/validation dataset, so the density distributions of scores might tell us not that much.

Arbitrage talks about hitting a correlation of 4% with validation eras. That might be one thing to look at.

> What you want to see in terms of model performance is around 4% correlation with the validation eras. Anything much above 4% is likely too overfit to be very performant, and anything 3% or below (generally speaking) likely won’t be very competitive.

---

### Post #6 — **mdo** | 2020-03-28 16:49 UTC

Yeah it’s not an easy problem. I think Arbitrage’s rule of thumb is as good a simple heuristic as you’re going to find. The “correct” thing to do would be to wait to get enough live data points so you can actually compare the distributions, but as they say, the waiting is the hardest part…
