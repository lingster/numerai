---
title: "How to ensemble models"
category: Data Science
url: https://forum.numer.ai/t/how-to-ensemble-models/4034
created_at: 2021-09-05T07:50:40.376000+00:00
last_posted_at: 2021-09-07T14:40:52.779000+00:00
posts_count: 15
views: 3763
tags: []
---

# How to ensemble models

---

### Post #1 — **nyuton** | 2021-09-05 07:50 UTC

Hi,

I’m staking on an ensemble of my best models, because building my own meta model has its advantages.

I’ve been calculating my ensemble as  
ensemble = (prediction1 + prediction2) / 2

Which is simple, easy and wrong ![:smiley:](http://forum.numer.ai/images/emoji/twitter/smiley.png?v=9)  
I recognized it, because the result of the ensemble was always stronger influenced by one model then the other…

I learnt the hard way that different models output their predictions with different mean and standard deviation. The ensemble is then stronger influenced by the model, which has higher mean and/or standard deviation.

I believe the correct way of building an ensemble is  
ensemble = MinMaxScaler.fit_transform( prediction1.rank() + prediction2.rank() )

This method should give models equal weight in the ensemble.  
If you have a different or better method, please don’t hold it back!

Have fun!

---

### Post #2 — **jrb** | 2021-09-05 14:24 UTC _(reply to #1)_

Just don’t forget to rank your predictions on a per-era basis.

---

### Post #3 — **yxbot** | 2021-09-05 17:23 UTC _(reply to #2)_

instead of weighted average, I prefer using gmean  
also, one of my better model is a result of stacking (i.e. using out-of -fold predictions from sub models) from 5 first-level models

---

### Post #4 — **aventurine** | 2021-09-06 06:15 UTC

Was actually going to bring up stacking too like [@yxbot](</u/yxbot>) was stating. Not sure what libraries you are using or what not but scikit has a pretty good example of using the make_pipline to preprocess data and then using the stackingregressor ending with a final estimator to stack everything together. For me I really like the speed of the experimental HGB regressor and I think, gives xgboost a pretty good run for its money. Stacking like a random forest onto an HGB after doing all the feature selection, neutralization preprocessing etc could give you a little edge over just xgboost or just using the (p1+p2)/2 or the minmaxscaler on two separate models(im just throwing out some random regression/random forest stuff, im not sure what your two models are using that you are putting together) I guess in the end its all preference on how to add stuff together im sure it gets pretty much close to same results. I also think you can use that minmaxscaler to perform the weights in the stack. Here is link to fairly simple example that maybe you can cut up to help out or play around with: [Combine predictors using stacking — scikit-learn 0.24.2 documentation](<https://scikit-learn.org/stable/auto_examples/ensemble/plot_stack_predictors.html#sphx-glr-auto-examples-ensemble-plot-stack-predictors-py>)

---

### Post #5 — **andy_shaps** | 2021-09-06 10:08 UTC _(reply to #2)_

Can you elaborate on this please? do you mean to give each row within each era a rank, then use that rank as a feature for the meta model? also, why rank, has that shown some evidence to improve scores?

Thanks in advance

---

### Post #6 — **jrb** | 2021-09-06 13:53 UTC _(reply to #5)_

> Can you elaborate on this please?

Your predictions are long-short ranks for a set of stocks within each era. You might have noticed that the number of rows in each era varies, this is because the number of stocks that you’re asked to rank on changes for every era (this is more transparent of signals where you know what stocks each era is comprised of).

Given this, ranking all your predictions without grouping them by era will lead to spurious results.

> also, why rank, has that shown some evidence to improve scores?

Ranking will make your predictions equidistant from each other. What [@nyuton](</u/nyuton>) is suggesting is that averaging your predictions after ranking them will lead to “fairer” ensembles (for some arbitary definition of fair). I’d recommend plotting histograms of predictions from your model(s) for some eras and seeing things for yourself.

---

### Post #7 — **jrb** | 2021-09-06 14:18 UTC _(reply to #3)_

> instead of weighted average, I prefer using gmean

`gmean` is great when you have large outliers, which isn’t the case here.

---

### Post #8 — **yxbot** | 2021-09-06 14:58 UTC _(reply to #7)_

> `gmean` is great when you have large outliers, which isn’t the case here.

any data source to back this point up?

I use gmean mainly based on previous competition experience that it tends to work better when the final result (i.e. resolved result in each round in Numerai) could show large deviation from validation result.

personally I also avoid using weighted averaging because it explicitly requires us as a modeller to state our confidence on submodel in the form of weigh - this is something I would rather not do.

Would love to see some side-by-side comparison. couple weeks ago [@inversion](</u/inversion>) mentioned he would be doing some, so perhaps he has some nice insight to share

---

### Post #9 — **jrb** | 2021-09-06 17:25 UTC _(reply to #8)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/yxbot/48/2906_2.png) yxbot:

> any data source to back this point up?

\Bigg(\prod_{i=1}^{n} x_{i}\Bigg)^{\frac{1}{n}} = exp\Bigg(\frac{1}{n}\sum_{i=1}^{n}log(x_i)\Bigg)

---

### Post #10 — **yxbot** | 2021-09-06 17:29 UTC _(reply to #9)_

ok, my humble mind doesn’t process the ability to translate the formula to your previous point. ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=9)

Will make a note on this though, so that I can do some experiment in the future - probably with the larger validation set for the new data.

Thanks

---

### Post #11 — **jrb** | 2021-09-06 17:48 UTC _(reply to #10)_

My point is that the log transform makes geometric mean less sensitive to large values (and conversely, more sensitive to small values (< 1, which results in negative values after the log transform)). The opposite is true for arithmetic mean. And since our predictions are in [0, 1], the latter is more appealing.

---

### Post #12 — **yxbot** | 2021-09-06 18:21 UTC _(reply to #11)_

thanks for following up, it is just that it had worked very well for me in classification problems before in which case probabilities are also bound by [0,1].

Anyway, it is a point of curiosity for me now, I shall at least re-run my gmean enabled model with arithmetic mean and do some comparisons ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=9)

---

### Post #13 — **xiafanaina** | 2021-09-06 22:23 UTC _(reply to #3)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/yxbot/48/2906_2.png) yxbot:

> 5 first-level models

Might I ask what is meant by “first-level”? Stack from your best 5 models?

---

### Post #14 — **yxbot** | 2021-09-07 05:36 UTC _(reply to #13)_

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/x/7ba0ec/48.png) xiafanaina:

> Might I ask what is meant by “first-level”?

When I used the term “first-level models”, I meant the models one use as components to generate additional models. so in OP’s words - “ensemble = (prediction1 + prediction2) / 2” - in this context the “first-level” models would be the models behind prediction1 and prediction2.

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/x/7ba0ec/48.png) xiafanaina:

> Stack from your best 5 models

usually a combination of your best “single models” and models that bring in a degree of diversity.

In typically “accuracy driven” competitions like Kaggle comps, stacking is a popular technique especially for tabular dataset to squeeze additional 0.0001 point from your models bundle. This works quite well when the underlying problem and the provided dataset allow for more reliable validation

Here on Numerai, it is a bit more difficult to validate modelling results, so my original motivation was just to ensure that my model can remain stable.

---

### Post #15 — **andy_shaps** | 2021-09-07 14:40 UTC _(reply to #6)_

Thanks for the reply. I’m not sure I understand? When you talk of ranking, does this only apply to ensembling or would you do this for single model approaches? My ensemble models rely on stacking and so if this is the case, it does not apply to me (i don’t think?).

Is there something I have missed that eludes to using ranking as i keep seeing it mentioned? if so, I would greatly appreciate a link or any further information that could help my understanding of the process/method.
