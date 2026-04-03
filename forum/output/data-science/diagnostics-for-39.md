---
title: "Diagnostics for #39"
category: Data Science
url: https://forum.numer.ai/t/diagnostics-for-39/4155
created_at: 2021-09-19T08:40:17.841000+00:00
last_posted_at: 2022-01-31T00:35:20.514000+00:00
posts_count: 65
views: 4881
tags: []
---

# Diagnostics for #39

---

### Post #1 — **nyuton** | 2021-09-19 08:40 UTC

Diagnostics are built to help us, but they can be very misleading.

My most successfull model, which stands at #39 at the time of writing (nyuton_test8) has so bad diagnostics, that I almost threw it out at the beginning and I haven’t started staking on it until recently.

Trust you CV!  
I’m writing this post partly for myself as a reminder, when I see similar results with the new dataset.  
To be frank, this model uses an ensemble of models from CV folds. Data also includes validation set. This is the diagnostic of the only part that doesn’t include validation data at all. Probably a good approximation of the other models as well.

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/3/3ef94956fb0d1ba91c6dd97a39c2e61a04b9f2ff.png)image247×517 15 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/3/3ef94956fb0d1ba91c6dd97a39c2e61a04b9f2ff.png> "image")

An other model (nyuton_test15) looks ever worse than that. And it got 14 medals in its first 9 completed rounds…

---

### Post #2 — **restrading** | 2021-09-19 09:42 UTC

Defintely a great reminder, trust your CV indeed. Although I’d still keep an eye on risk because getting metals+high rank may also be a result of high variance models, which tend to do worse when regime changes

---

### Post #3 — **sunkay** | 2021-09-19 11:16 UTC

Great reminder! But what is #39?

---

### Post #4 — **qeintelligence** | 2021-09-19 11:53 UTC

The other way around is also definitely the case, I had a NN with ‘reasonable’ diagnostics (everything green) which also performed well for 5-6 rounds, after that it got burned 4 rounds, only to recover now again. And no, I didnt use val for training ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=9) (but i suspect there is a leakage because of determining the amount of epochs with the use of val)

---

### Post #5 — **nyuton** | 2021-09-19 12:36 UTC _(reply to #3)_

Ranks 39 on the leaderboard.

---

### Post #6 — **neosbrother** | 2021-09-19 13:45 UTC

So your CV results looked very good but it did poorly on the full diagnostics?

---

### Post #7 — **nyuton** | 2021-09-19 17:27 UTC _(reply to #6)_

Yes, CV was great! Validation score was not so great!

---

### Post #8 — **yxbot** | 2021-09-20 21:46 UTC _(reply to #7)_

my most profitable model - running for 4 months with top 100 3M return - also have a rubbish diagnostics score - I was able to pick it out for staking because it seems to have by far the most stable daily score, additionally, after I settled on my validation scheme it was shown to be 4th among my models on non-corr related metrics i.e. ratios based metrics

So yes, people should try to create validation methods that are at least not entirely dependent on the provided validation data.

---

### Post #9 — **profricecake** | 2021-09-22 02:21 UTC

Out of curiosity, what kind of mean correlation numbers do you see in your CV runs?

Thanks

---

### Post #10 — **nyuton** | 2021-09-22 06:20 UTC _(reply to #9)_

0.043 when trained on train+validation

---

### Post #11 — **profricecake** | 2021-09-22 14:32 UTC _(reply to #10)_

Thank you! Very helpful. I’ve been leaning on validation metrics for so long I didn’t know what to expect from a CV score!

---

### Post #12 — **profricecake** | 2021-09-22 21:34 UTC _(reply to #10)_

One other question: When you find a good set of hyperparameters using CV on some number of folds of the combined train+validation data, do you then train your final model (the one you use for tournament prediction) by using those HPs and all the available data (instead of folds)? I’m assuming not because then you wouldn’t have a sane measure of when to stop the training. But if not, then do you just stick with training on, say, 4 of 5 folds and validating on the 5th?

Thanks again.

---

### Post #13 — **nyuton** | 2021-09-23 06:59 UTC _(reply to #12)_

Oh man, this is a dead simple random forest!  
That’s the funny part of it. Apparently you can get this close to the top with an RF.  
NNs might give you a boost in MMC. But in raw accuracy (CORR) RF is hard to beat it.

---

### Post #14 — **kenfus** | 2021-09-23 09:37 UTC

Yea, I was also wondering why the diagnostics is pretty much useless when comparing models. It’s a good sanity check, but not much more. Could it be that some people have leakage to the validation-set, and thus they skew the ranks in the diagnostics to the top?  
At the beginning, I did use in CV the validation-set and even though the model never trained on the validation-set, this still lead to a massive overfit; All my metrics were light-green (99+), but the live tests were absolutely terrible ([Numerai](<https://numer.ai/kenfus>) before round 274).

---

### Post #15 — **themicon** | 2021-09-23 10:08 UTC _(reply to #14)_

Everybody had bad rounds before R274: <https://dashboard.numeraipayouts.com/> The median score was pretty much negative. You need to judge the relative performance of you model on live data, not the performance in isolation.

---

### Post #16 — **kenfus** | 2021-09-23 10:29 UTC _(reply to #15)_

I agree, and this is what I’m doing currently. However, over 4 rounds my model was  
much, much worse than other models. Maybe I should have generated more data but being in 2 of 4 rounds below a 20 percentile is enough for me to say that it is “not optimal, probably”.

---

### Post #17 — **nyuton** | 2021-09-23 10:59 UTC _(reply to #16)_

That doesn’t say much at all, you need to test longer. The above mentioned model has also has more than 2 round in the lower 20 percentile…

---

### Post #18 — **factorsparsity** | 2021-09-25 20:20 UTC _(reply to #10)_

This is for the old data format (310 features) or the new one?

BTW: I can corroborate your initial statement on the diagnostics. They don’t always indicate whether a model is good or not.

---

### Post #19 — **johnnywhippet** | 2021-09-27 15:49 UTC

The diagnostics for this model are appalling but… its a decent model. peaked at 4 for MMC and 750 or so for correlation. A consistent performer, more green than red. 19 medals in all.

[![m3_diag](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/2/2aaa19b5c710a0bafa091c1eda9b92ff1304cbfd.png)m3_diag303×518 15.2 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/2/2aaa19b5c710a0bafa091c1eda9b92ff1304cbfd.png> "m3_diag")

---

### Post #20 — **johnnywhippet** | 2021-09-29 18:39 UTC _(reply to #19)_

Those appalling diagnostics have garnered two more silver medals. I don’t get it.  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/4/4456d6ff8033707b3a543f0151632ad26cef34b9.jpeg)image438×250 28.1 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/4/4456d6ff8033707b3a543f0151632ad26cef34b9.jpeg> "image")

---

### Post #21 — **maxchu** | 2021-10-07 11:09 UTC _(reply to #19)_

Your validation diagnostics is really horrible… I think it is a dangerous sign as it is evident that your model at least performs very poorly in the validation period (which may happen in future). We cannot trust the validation result 100% but it does not mean we need to ignore it.

---

### Post #22 — **maxchu** | 2021-10-07 11:22 UTC

I agree that CV done properly is better than a fixed validation set as effectively your model has been tested on multiple validation periods which is a better evidence for the performance/generalizability of your model. But when you use your nyuton_test8 4 months live performance ranking as evidence of good model but ignore 2 years period performance of validation set… that seems a bit odd.  
So, IMO the evidence ranking is CV (if “effective validation period” longer than length of validation period) > Validation > Live (if less than the length of validation period)

---

### Post #23 — **johnnywhippet** | 2021-10-07 12:44 UTC _(reply to #21)_

Totally agree. I wouldn’t stake my life’s savings on it but… it performs [mostly] quite well. This round has since garnered two gold medals , since March it has dipped into the red on only 4 occasions. I appreciate the comment and some of that will find it’s way into my write up though Tbh it doesn’t matter if it succeeds or not as I’m doing this for an A level EPQ (UK) and I choose AI ![:smiling_face:](https://emoji.discourse-cdn.com/twitter/smiling_face.png?v=13)  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/0/0663a09b0363bc1d085fec59d896184a0528586e_2_653x499.jpeg)image750×574 69.9 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/0/0663a09b0363bc1d085fec59d896184a0528586e.jpeg> "image")

---

### Post #24 — **yxbot** | 2021-10-07 16:10 UTC

This is Grinning_cat’s old and new diagnosis:  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/1/14948a100ff9499d310754dc6d41c8b10a22438e_2_690x362.png)image955×502 79.3 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/1/14948a100ff9499d310754dc6d41c8b10a22438e.png> "image")

For a model that ranked 15th in 3 months return at time of writing, corr2mmc sharpe usually between (rank 10-60), and have not had a burn round since creation at round 263, it isn’t too bad ![:slight_smile:](https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=13)

---

### Post #25 — **yxbot** | 2021-10-07 16:13 UTC _(reply to #23)_

how does this model perform on the “old data new val” validation set? if you don’t mind sharing ![:grinning:](//forum.numer.ai/images/emoji/twitter/grinning.png?v=9)

---

### Post #26 — **johnnywhippet** | 2021-10-07 17:13 UTC _(reply to #25)_

I haven’t done that but I will when I get a mo and I’ll post the results ![:+1:](//forum.numer.ai/images/emoji/twitter/+1.png?v=9)

---

### Post #27 — **eleven_sigma** | 2021-10-17 10:54 UTC _(reply to #24)_

The problem here is that validation data aren’t representative, they are very bad eras in average. So when you train using only train set and validate the performance against validations, results are bad, but it isn’t a serious problem: as validation isn’t representative, when you put the model in real markets it works pretty well.  
You can use validation as ‘the worst scenario’ and using them in training (with careful), adjust a very robust model, that works worse in normal periods but lose less in ‘similar to validation’ periods.  
For use a better validation framework we would need the targets for the period between train and validation. Having them (not only the hell of the validation dataset) we could fit a more realistic model for an average market condition.

---

### Post #29 — **johnnywhippet** | 2021-11-19 18:40 UTC _(reply to #23)_

And… it’s finally breached the top 100 for correlation. Been in the mmc hot 100 for a while now.

---

### Post #30 — **jefferythewind** | 2021-11-20 12:12 UTC

Great thread here [@nyuton](</u/nyuton>). I seem to be on the other side of the problem. In fact I choose some best params based on cross validation and then train using those params on the whole train data, check the validation metrics (corr and MMC both 100th percentile), so CV AND validation metrics good, but live performance seems mediocre at best, although too few rounds to know for sure.

---

### Post #31 — **johnnywhippet** | 2021-12-03 18:04 UTC _(reply to #29)_

Now 32 for corr, 24 for mmc.

---

### Post #32 — **mindyoself** | 2021-12-05 13:17 UTC

I have experienced this also and thought, this is a rubbish model I have built but end up getting a very good score in production. I still think the scoring guideline is still very useful. Perhaps for conservative modelling and newbies may be best to trust the diagnostics until you rich @nyuton-level mastery and then probably you don’t need to look at the score. It is afterall an art as well. However, the riskier models may do very well, but perhaps over a shorter time frame. [@nyuton](</u/nyuton>) How long have you been running #39 for in production?

---

### Post #33 — **autratec** | 2021-12-06 00:22 UTC

A general question. What’s the value of cross validation, if we already confirm the prediction model, say XGB. Should hyper parameter, neutralisation and feature filtering be more important than CV ?

---

### Post #34 — **nyuton** | 2021-12-06 16:12 UTC _(reply to #32)_

It’s 30+ rounds by now. Still in very good position.

---

### Post #35 — **arnokha** | 2021-12-18 02:41 UTC

Just a heads up: the three different validation diagnostics you can get with legacy data may differ significantly. For example, here are three different diagnostics outputs from the same model.

Old target:  


[![val_1](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/8/8fb7e0c410fb34d109fe9b942da24bccec231ca4_2_285x500.png)val_1293×513 22.2 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/8/8fb7e0c410fb34d109fe9b942da24bccec231ca4.png> "val_1")

New target, old validation set:  


[![val_2](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/c/ca843a31b9cedefd19b5275c570fc09a701bf1d7_2_633x500.png)val_2699×552 45 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/c/ca843a31b9cedefd19b5275c570fc09a701bf1d7.png> "val_2")

New target, new validation set:  


[![val_3](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/6/6adf2013bd54fef5e120156fb420b6b1b012c2c1_2_629x499.png)val_3698×554 44.7 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/6/6adf2013bd54fef5e120156fb420b6b1b012c2c1.png> "val_3")

-0.01 from old diagnostics to new. I don’t have too much live data right now, so we’ll see how it actually translates into live performance.

---

### Post #36 — **johnnywhippet** | 2022-01-12 20:05 UTC _(reply to #31)_

15th for corr, 8th for mmc

---

### Post #37 — **johnnywhippet** | 2022-01-22 22:09 UTC _(reply to #36)_

5th for corr, 5th for mmc

---

### Post #38 — **maxchu** | 2022-01-23 00:01 UTC _(reply to #37)_

It is really good! Since your validation score is so bad, I am curious what your CV score is.

---

### Post #39 — **johnnywhippet** | 2022-01-23 10:02 UTC _(reply to #38)_

It’s a miracle… What cv score would you like to see?

---

### Post #40 — **maxchu** | 2022-01-23 10:21 UTC _(reply to #39)_

I am guessing your CV score should be very high, at least 0.045+ corr?

---

### Post #41 — **johnnywhippet** | 2022-01-23 11:48 UTC _(reply to #40)_

i’ll re-run everything this afternoon for this week’s round and post 'em. TBH i can’t remember as i’m working on some other models and this model runs on auto-pilot.

---

### Post #42 — **johnnywhippet** | 2022-01-24 00:29 UTC _(reply to #40)_

0.047577065889401226

---

### Post #43 — **maxchu** | 2022-01-24 00:43 UTC _(reply to #42)_

That is a really high cv score, is it a tree-only models or it mixed with NN too?

---

### Post #44 — **maxchu** | 2022-01-24 00:44 UTC _(reply to #42)_

It is really interesting that your validation is that low, so i guess it is a very NN-heavy ensemble? I bet the sharp ratio will not be that great. After they switched to TC, i think you need to change the ensemble selection rule.

---

### Post #45 — **johnnywhippet** | 2022-01-24 00:48 UTC _(reply to #43)_

its a boosted NN.

(this text takes the post beyond 20 chars…)

---

### Post #46 — **johnnywhippet** | 2022-01-24 00:51 UTC _(reply to #44)_

sharpe is very low.

(to get the char count past 20…)

---

### Post #47 — **maxchu** | 2022-01-24 02:39 UTC _(reply to #46)_

Thanks for the infos, would you mine also provide me with your sharpe?

---

### Post #48 — **johnnywhippet** | 2022-01-26 20:18 UTC _(reply to #37)_

1st for corr, 3rd for mmc

---

### Post #49 — **johnnywhippet** | 2022-01-26 20:21 UTC _(reply to #47)_

0.0469 From a scrap of paper. Can re-run when I’ve finished my HW.

---

### Post #50 — **maxchu** | 2022-01-27 21:32 UTC _(reply to #49)_

You mean 0.0469 for sharpe?!

---

### Post #51 — **johnnywhippet** | 2022-01-27 23:39 UTC _(reply to #50)_

Yeah… i think so… i scribbled it on a sheet of paper but i think that’s correct. i’ll re-post on sunday when i’ve got the next round’s data.

---

### Post #52 — **maxchu** | 2022-01-27 23:41 UTC _(reply to #51)_

Are you sure? 0.0469 for Sharpe is extremely low…

---

### Post #53 — **johnnywhippet** | 2022-01-27 23:47 UTC _(reply to #52)_

i’m certain its correct. will re-post sunday’s calculations. i get that its extremely low which is another reason i’m puzzled at the models performance. i’m doing a write up, trying to explain why i ran with it when on paper it looks to be a lame duck.

---

### Post #54 — **maxchu** | 2022-01-27 23:50 UTC _(reply to #53)_

Cant wait to see it, it is very interesting!

---

### Post #55 — **sunkay** | 2022-01-29 00:28 UTC _(reply to #49)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/johnnywhippet/48/2803_2.png) johnnywhippet:

> 0.0469

0.0469 is your validation sharp right? I am curious about what you cv sharp is.

---

### Post #56 — **kowalot** | 2022-01-29 16:38 UTC _(reply to #27)_

imo…training dataset is enough informative to deliver kind of solid results in diagnostics tool and validation data (without data leakage)

[![Max_drawdown_zero](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/c/c59418d77ba97d3de59b8db2f97fb56972a40a92.png)Max_drawdown_zero755×526 40.3 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/c/c59418d77ba97d3de59b8db2f97fb56972a40a92.png> "Max_drawdown_zero")

Another story is to prove it on the live data which I can’t yet, as being a new participant in the tournament.  
And I agree more data would make us more confident about our work.

---

### Post #57 — **wigglemuse** | 2022-01-29 17:14 UTC _(reply to #56)_

[@kowalot](</u/kowalot>) I’d double-check on that whole “without data leakage” thing (also check you aren’t including any of the targets as features in your training). The probability of the above results being genuine from an uncorrupted model are extremely small.

---

### Post #58 — **kowalot** | 2022-01-29 18:36 UTC _(reply to #57)_

[@wigglemuse](</u/wigglemuse>) , Ok, I will double check.

My quick checks:

  * model is trained on training data(no CV with validation data)
  * validation data are only used for early stopping (different structure)
  * target is in separated structure
  * additional targets are kept in different structure and not used in this specific configuration
  * only selected features are available by the training loop (“feature_”)
  * assertion of dataset indices between training and validation sets
  * the same code works on predicting tournament data (where certain data are unavailable)



If you see another common pattern of data leakage which I am not aware, please advise me.

I believe that the most controversial is max_drawdown. Am I right?  
This is what i tried to optimize during last week (several negative hard validation eras 864,921,922, 945).  
Normally max_drawdown is somewhere between -0.01 and -0.06.

---

### Post #59 — **wigglemuse** | 2022-01-29 18:57 UTC _(reply to #58)_

Well, yeah, you’ve got no negative eras and that’s just not gonna happen if it were truly blind to that data. However, you are now saying you were optimizing for the hard validation eras which is leakage by another name so there you go.

---

### Post #60 — **kowalot** | 2022-01-29 19:13 UTC _(reply to #59)_

My previous models have several negative val eras I changed the architecture to get rid of them. Validation data are used ONLY to stop/select certain snapshot of model (and it’s not max_drawdown). Do you suggest I should do stop of the training process based on another spare/untouched part of training (in our case pretty similar to the rest of training data as it’s one countinous block of eras)? How do you do early stopping?

---

### Post #61 — **wigglemuse** | 2022-01-29 19:29 UTC _(reply to #60)_

No, I mean it SOUNDS fine, maybe. With enough parameters you can get anything to fit anything. Your validation results are very suspicious, though. But they are not SO outrageous that I’d say that it is just absolutely positively totally impossible (even though I kinda think so). We’ve seen some where we know there was leakage or target training that are twice as good as even that. Because we don’t actually know the upper limit of what’s legitimately possible there is always the very tiny chance that you’ve done something brilliant and magical, but really they look way too good to be true and I wouldn’t trust them. Needs to be seen on live data. But hey, even if there is some “cheating” going on and these results are exaggerated that doesn’t necessarily mean the model is crap, just that it isn’t this good.

---

### Post #62 — **luee** | 2022-01-29 19:44 UTC _(reply to #58)_

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/forum.numer.ai/kowalot/48/3444_2.png) kowalot:

>   * validation data are only used for early stopping (different structure)
> 


This part is in fact data leakage and could lead to such much overestimated performance. In live you will not be able to perform early stopping on the live data, but that is essentially what you are doing here

---

### Post #63 — **kowalot** | 2022-01-29 19:56 UTC _(reply to #61)_

Anyway as [@wigglemuse](</u/wigglemuse>) , as active member of the forum/chat (which I read probably the whole ![:wink:](http://forum.numer.ai/images/emoji/twitter/wink.png?v=10) ) are skeptical I will look into it. I could make a mistake, which is quite possible, but at this moment I don’t see where. I used/tried a lot of tricks mentioned here by the community but also couple own techniques as well. For sure I want to be far from “cheating”.

---

### Post #64 — **kowalot** | 2022-01-29 21:13 UTC _(reply to #62)_

let me add results with doing early stoping on “unused”/untouched training data. I cut some portion of continous eras.
    
    
                           mean    std    sharpe      max_drawdown      apy    
    max_drawdown         0.046483  0.023462  1.981191     -0.007393  815.262085  
    

As expected this part has even better results in term of corr. Of course model lost some of the signals from cut part.

Validation without any connection to the training process.

[![Max_drawdown_eraly_stoping_on_train](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/f/f0e7cbf628c641b068532b936f721ccc9cfa1a04.png)Max_drawdown_eraly_stoping_on_train762×530 38.9 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/f/f0e7cbf628c641b068532b936f721ccc9cfa1a04.png> "Max_drawdown_eraly_stoping_on_train")

Feature exposure still quite good but lack of data suffered it a bit.

---

### Post #65 — **luee** | 2022-01-29 21:47 UTC _(reply to #60)_

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/forum.numer.ai/kowalot/48/3444_2.png) kowalot:

> My previous models have several negative val eras I changed the architecture to get rid of them.

That would be the other form of data leakage that I see, it seems like you have tweaked your model specifically for your out-of-sample performance. While the model never explicitly sees that data, it is built with performance on that very specific sample in mind. I would go through the same exercise of building my model to fit the last 100 eras of training set the best, then use that model once on the validation set. This will probably be a closer estimate of your live performance and give you an idea of the impact of data-mining bias in your current process.

---

### Post #66 — **maxchu** | 2022-01-31 00:35 UTC _(reply to #53)_

I am also curious if you have done any feature naturalization as you have very skewed corr on different eras.
