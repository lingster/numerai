---
title: "Liz Experiment Review Q1 2021 : Generating Features and Applying Feature Neutralization"
category: Tournament
url: https://forum.numer.ai/t/liz-experiment-review-q1-2021-generating-features-and-applying-feature-neutralization/3011
created_at: 2021-04-22T04:58:47.958000+00:00
last_posted_at: 2021-05-11T21:13:21.802000+00:00
posts_count: 25
views: 5338
tags: []
---

# Liz Experiment Review Q1 2021 : Generating Features and Applying Feature Neutralization

---

### Post #1 — **liz** | 2021-04-22 04:58 UTC

**Introduction**

Greetings, all!

This post marks the end of my first experiment period on numer.ai. As the title suggests, I’m aiming to do something like this approximately quarterly. This time was more exploration than experiment. I’ve talked on [Daily Scores and Chill](<https://www.twitch.tv/prof_jtaylor>) about my approach to modeling and thought that might be helpful to put in writing, given I have had some success with MMC. Following that, I will discuss the experiment itself. Spoiler alert : I made some mistakes, interpret at your own peril! Feel free to reach out to me on rocketchat, where my username is ‘aelizzybeth’

**Generating features**

I believe that taking creative approaches to modeling will help generate that sweet, sweet MMC. That certainly isn’t all that is required, but I think there is a lot of MMC opportunity there.

When I started competing on numerai about 8 months ago, after surveying some posts and [rocketchat](<https://community.numer.ai/home>), I felt not much attention was being paid to feature engineering by modelers in the classic tournament. Of course, many standard models do some feature engineering on their own. Still, I felt there is ample room to find signal here, so I tapped into my [generative art roots](<https://www.instagram.com/flowyrose/?hl=en>) and designed a generative approach. I tested random forest, gbm, different kinds of transformations, as well as including or excluding the original variables. Unfortunately I didn’t take good notes at the time. The resulting process is summarized below (I implemented this in R, fwiw).

  1. set a seed for reproducing portions of process involving randomization
  2. transform the features of the dataset so there are no zeroes. (didn’t bother with the target)
  3. generate 1000 unique pairs of indices 1->310 (to correspond to features)
  4. for each generated pair, (A,B), derive a new column = Logarithm base B of A
  5. train a gbm on the new dataset (original features + 1000 engineered features)



Then, when predicting, transform new data, predict, that’s it.

[liz](<https://numer.ai/liz>) up to and including round 243 shows early iterations of this development, into the final version in the last few rounds. [urza](<https://numer.ai/urza>) shows results from round 244 til now (R256 just finished today).

**Feature Neutralization Experiment**

From R244 - R256 I carried out a 13-round experiment. I wanted to see what various degrees of feature neutralization applied to the model described above would result in, performance-wise. I used a method adapted from [a post by wigglemuse](<http://forum.numer.ai/t/model-diagnostics-feature-exposure/899/11>).

(text about misapplying FN deleted. Upon another code review, realized I did it right, sorry for the confusion). For reference, I stake Corr + 2x MMC on all models.

[Urza](<https://numer.ai/urza>) : 0 Feature Neutralization  
[Liz](<https://numer.ai/liz>) : 25% Feature Neutralization  
[Yawgmoth](<https://numer.ai/yawgmoth>) : 50% Feature Neutralization  
[Emrakul](<https://numer.ai/emrakul>) : 75% Feature Neutralization  
[Ulamog](<https://numer.ai/ulamog>) : 100% Feature Neutralization

See some box-and-whisker plots of Corr, MMC, and FNC.

Please note, the y-axis differs for each plot.

[![corr](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/30cd98d82e666f188c7a0408c63ea2dd9fb6f28b.png)corr476×356 40.8 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/30cd98d82e666f188c7a0408c63ea2dd9fb6f28b.png> "corr")

[![mmc](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/11425b87a869d9ac85c16eacca6cb41b541bdf60.png)mmc482×361 24 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/11425b87a869d9ac85c16eacca6cb41b541bdf60.png> "mmc")

[![FNC](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/d2a2ffdcd4ab665db6c053dce9cbfd3617873d20.png)FNC482×358 25.3 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/d2a2ffdcd4ab665db6c053dce9cbfd3617873d20.png> "FNC")

corr and mmc suffered the more FN, generally, during this 13-round period. I found the FNC results most interesting. Though I don’t present them here, it was interesting to see the rounds were Urza wasn’t the top performer, the order of corr performance tended to be flipped. I’ll paste the data into a comment if anyone is interested (though this can be found on the links provided as well). I would have uploaded the excel spreadsheet I used to write this but now I am tired and not sure how. I’m glad to take questions other than “what are your model parameters?”.

**Thoughts for next experiment period**  
I might get this going right away, might take a few weeks, but I want to try a few things.

  1. less overfitting
  2. xgboost (gonna skip this on next experiment cycle, slots are mapped out already)
  3. more generated features
  4. different sets of generated features
  5. automated feature selection (forgot to add at first)
  6. FN relative to original data only (forgot to add at first) [EDIT : I actually did it right the first time, but I am now interested so will experiment with full-FN vs original-FN as part of my next suite of experimental models]

---

### Post #2 — **liz** | 2021-04-22 05:01 UTC

here is the data I promised

Corr |  |  |  |  |   
---|---|---|---|---|---  
|  |  |  |  |   
ROUND | Urza | Liz | Yawgmoth | Emrakul | Ulamog  
|  |  |  |  |   
256 | 0.0831 | 0.0796 | 0.0715 | 0.054 | 0.0243  
255 | 0.0928 | 0.0882 | 0.078 | 0.0554 | 0.0153  
254 | 0.1211 | 0.1138 | 0.0991 | 0.0662 | 0.0101  
253 | 0.0475 | 0.0471 | 0.0447 | 0.0361 | 0.0172  
252 | 0.0372 | 0.0339 | 0.0281 | 0.0167 | -0.0029  
251 | 0.0448 | 0.0411 | 0.0352 | 0.025 | 0.007  
250 | 0.027 | 0.0245 | 0.0198 | 0.0102 | -0.0083  
249 | 0.0086 | 0.0092 | 0.0091 | 0.0059 | -0.0006  
248 | 0.01 | 0.0113 | 0.0138 | 0.016 | 0.0124  
247 | 0.0447 | 0.0452 | 0.0449 | 0.0398 | 0.023  
246 | 0.0495 | 0.0466 | 0.0415 | 0.0316 | 0.0139  
245 | 0.0543 | 0.049 | 0.0407 | 0.0255 | 0.0016  
244 | 0.057 | 0.0515 | 0.0425 | 0.0262 | -0.0015  
  
MMC |  |  |  |  |   
---|---|---|---|---|---  
|  |  |  |  |   
ROUND | Urza | Liz | Yawgmoth | Emrakul | Ulamog  
|  |  |  |  |   
256 | 0.0098 | 0.0083 | 0.0056 | 0.0011 | -0.0047  
255 | 0.0115 | 0.0092 | 0.0051 | -0.0026 | -0.015  
254 | 0.0314 | 0.0268 | 0.0189 | 0.0031 | -0.0212  
253 | 0.0112 | 0.0114 | 0.011 | 0.0084 | 0.0019  
252 | 0.0184 | 0.0159 | 0.012 | 0.0047 | -0.0072  
251 | 0.021 | 0.0183 | 0.0144 | 0.0086 | -0.001  
250 | 0.0153 | 0.0134 | 0.01 | 0.0035 | -0.0091  
249 | -0.0019 | -0.0013 | -0.001 | -0.0022 | -0.0046  
248 | -0.0055 | -0.0043 | -0.0018 | 0.0018 | 0.003  
247 | 0.0168 | 0.0172 | 0.0176 | 0.016 | 0.0081  
246 | 0.0194 | 0.0171 | 0.0136 | 0.008 | -0.0004  
245 | 0.0285 | 0.0241 | 0.0179 | 0.0073 | -0.0076  
244 | 0.0257 | 0.0213 | 0.0147 | 0.004 | -0.0124  
  
FNC |  |  |  |  |   
---|---|---|---|---|---  
|  |  |  |  |   
ROUND | Urza | Liz | Yawgmoth | Emrakul | Ulamog  
|  |  |  |  |   
256 | 0.0184 | 0.0195 | 0.0208 | 0.0208 | 0.0187  
255 | 0.0199 | 0.0205 | 0.0203 | 0.0169 | 0.0104  
254 | 0.0136 | 0.0155 | 0.0171 | 0.0141 | 0.0066  
253 | 0.0118 | 0.0131 | 0.014 | 0.013 | 0.0116  
252 | -0.0085 | -0.007 | -0.0047 | -0.0047 | -0.0065  
251 | 0.0065 | 0.0056 | 0.0052 | 0.0048 | 0.0055  
250 | -0.0091 | -0.0088 | -0.008 | -0.0072 | -0.0079  
249 | -0.0022 | -0.0027 | -0.0025 | -0.0017 | -0.0012  
248 | 0.0029 | 0.0048 | 0.0078 | 0.0109 | 0.0115  
247 | 0.0201 | 0.0227 | 0.0246 | 0.0241 | 0.0216  
246 | 0.0108 | 0.011 | 0.011 | 0.0106 | 0.0114  
245 | -0.0024 | -0.0005 | 0.0008 | 0.0002 | 0.0009  
244 | -0.0069 | -0.0049 | -0.0026 | -0.0021 | -0.0028

---

### Post #3 — **jimmy_woodford** | 2021-04-22 07:16 UTC

Thanks for sharing, [@liz](</u/liz>)! I have two questions about your process:

Regarding step 3, how did you select these feature pairs? Just at random or based on some selection process?

And is the logarithmic approach in step 4 based on theory or some common method?

---

### Post #4 — **liz** | 2021-04-22 11:20 UTC _(reply to #3)_

I select the pairs at random, and the logarithmic approach is just something I came up with that I thought might randomly expose more signal. I think that’s loosely based on principles of feature engineering but I’ve never read about it being done this way.

---

### Post #5 — **gbrecht** | 2021-04-22 17:13 UTC

Perhaps is an idea to pay attention to the feature groups. Either combine inside the groups, or outside the groups?

---

### Post #6 — **liz** | 2021-04-24 22:51 UTC _(reply to #5)_

could be! currently, developing a selection scheme for candidate features to transform is on my mental list of things I want to do, but won’t be doing right away

---

### Post #7 — **liz** | 2021-04-24 23:33 UTC

Edited title from “Liz Experiment Review Q1 2021 : Generating Features and Misapplying Feature Neutralization” to “Liz Experiment Review Q1 2021 : Generating Features and _**Applying**_ Feature Neutralization” and some text in the post because I realized I didn’t make an error in the first place.

In any case, I’ll be testing full-FN vs. original-FN as part of my ongoing tests. Sorry for the confusion!

---

### Post #8 — **paulito** | 2021-04-26 10:14 UTC

I guess a lot of success comes from the expantion of feature space alone (~1300 features). What"s your compute environment? I am already struggling with ~600 Features (I use ~25 GB ram), especially when it comes to inference on tournament data. I am looking for ways to get around it, but haven’t found good solutions yet.

---

### Post #9 — **senadorancap** | 2021-04-26 12:03 UTC _(reply to #8)_

I’m running a 16GB ram environment and I’m kinda using something similar to Liz approach. My solution to incorparate more features was “sample and ensemble”. Basically you run several models with sampled features and after you ensemble all of them.

---

### Post #10 — **paulito** | 2021-04-26 12:19 UTC _(reply to #9)_

Yes. I was also expeirmenting with something like that. If you don’t mind asking, what kind of model do you use for ensembling and how many models do you ensemble? In my experience ensembling just very few models with a very strikt ensemble model (eg. linear regression) does not help improving scores very much. But iI guess this is the way to go if feature space is getting too big.

---

### Post #11 — **liz** | 2021-04-26 15:44 UTC _(reply to #8)_

i’m using an r5.8xlarge ec2 instance on aws which i think is 256 gb ram and 32 cpu cores, i also have 300 gb ssd and instruct the program to use ssd when it runs out of ram. i previously ran these train jobs on a 16gb machine at home and they would take 24 hours and fail 25% of the time. on the r5.8xlarge it takes about 10 hours maybe. costs me ~25 USD. i don’t train the models every week, much faster when just predicting

---

### Post #12 — **backe** | 2021-04-26 15:57 UTC

Sus FE technique. Interesting FN experiment though!

---

### Post #13 — **liz** | 2021-04-26 16:01 UTC _(reply to #12)_

re: sus… care to expand?

---

### Post #14 — **backe** | 2021-04-26 16:24 UTC _(reply to #13)_

Suspicious… [post must be at least 20 characters]

---

### Post #15 — **liz** | 2021-04-26 16:27 UTC _(reply to #14)_

yes obviously sus = suscpicious. I was trying to invite you to contribute anything constructive ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=9)

---

### Post #16 — **backe** | 2021-04-26 16:45 UTC _(reply to #15)_

Ohh haha ![:blush:](http://forum.numer.ai/images/emoji/twitter/blush.png?v=9)  
Well, I just don’t see how your log-features could bring something new (uncorrelated) to the table. Generaly I think it’s very hard to do FE on these kinds of datasets; maybe some features on era level could work!

---

### Post #17 — **wigglemuse** | 2021-04-26 16:53 UTC

Feature expansion just by itself can sometimes work wonders. This is after all the entire basis of algorithms like SVMs that use the so-called “kernel trick” to find easier ways to separate the data in higher-dimensional space than is possible using only the original features. Downside is that it doesn’t scale well…

---

### Post #18 — **liz** | 2021-04-26 16:58 UTC _(reply to #17)_

yeah, so far it’s working nicely for me, more time will strengthen or weaken my faith in this approach. I’d most like to see how ‘urza’ performs through a regime-shift.

---

### Post #19 — **backe** | 2021-04-26 17:10 UTC _(reply to #17)_

But these features can easily be learned by a model. My questions is why would you force your model to learn from a specific set of randomly generated features. Why not e.g. arctan2(A, B) ? I think one should let their model decide - especially when you don’t know what features represent.  
Or see it this way, there are ~50k unique feature pair combinations. You randomly select 1k of them. What about the rest? This is a clear path to overfitting imho.

---

### Post #20 — **liz** | 2021-04-26 17:19 UTC _(reply to #19)_

the decision to use log base B of A was somewhat arbitrary. There are many other mappings possible. exponentially more if you get into 3-dimensional and higher!

what about the rest is indeed a question on my mind. There are too many to explore them all, when you also consider all non-trivial mappings. Phase 2 of my experiment, as I described in the post, includes testing similar models with different generated features. As noted, all these models contain the original 310 features as well. I am trying to build toward a more sensible exploration and selection of transformed features in this problem space, and chose this as my starting place. This is an ongoing, iterative experiment, and certainly not representative of a full exploration of the space I’ve described. Of course, all of that is apparent in my original post.

re : overfitting, literally everyone who competes in this tournament on a repeated basis is overfitting in some way. I’d like to avoid it somewhat but avoiding it entirely is not possible.

---

### Post #21 — **paulito** | 2021-04-27 12:23 UTC _(reply to #8)_

I am experiemnting with iterative prediction. The idea is to execute the whole preprocessing era-wise and iterate through the tournament data. This saves tons of memory ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=9). I will now try to also switch to era-wise training, which is very easy with xgboost. This will allow even broader feature space.

---

### Post #22 — **paulito** | 2021-04-27 12:25 UTC _(reply to #20)_

It’s all about that sweet spot between overfitting and maximising variance, which is arguably very very small in a tournament like this.

---

### Post #23 — **rpica** | 2021-04-29 09:32 UTC _(reply to #19)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/backe/48/1074_2.png) backe:

> But these features can easily be learned by a model.

You mean by … neural networks? As far as I know, NN are the ones that can find relations between features (do feature engineering), given that you have enough data and model capacity.

But even so, all the information you can provide as priors is going to boost where the model arrives… as an example, you could get CNN performance on images with vanilla NN (again provided enough data and capacity), but the effort to get there would be inmense, as compared as to giving spatial information and reusing parts of the network (CNNs).

I can imagine CART ensembles finding weird sequences of decisions making sort-of FE, maybe…

---

### Post #25 — **paulito** | 2021-05-11 08:59 UTC

Ok so considering the plots, feature neutralization seems to be detrimental overall. If I understand some other posts here reasoning about the usefulness of neutralization correctly, the main idea is to rebalance feature importance, which in turn would avoid overfitting and stabilize models in live environment. But if maximizing payout is your objective, then “Urza”, the model without feature neutralization, shows the best live performance. So why bother about feature neutralization after all?

One hypothesis could be that due to frequent retraining (asuming weekly model retraining), model drift is not a big problem and overfitting more benefitial than rebalancing feature importantance. Another take could be that also models with high FN do suffer from volatiliy in live data, so FN may be not as effective in terms of stabilizing CORR and MMC.

What are your takes on this and how would you improve FN so that CORR and MMC suffer less?

---

### Post #26 — **liz** | 2021-05-11 21:13 UTC _(reply to #25)_

weekly retraining isn’t particularly helpful given the training data doesn’t change weekly. I’ll write some more thoughts about FN soon.
