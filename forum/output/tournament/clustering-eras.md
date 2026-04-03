---
title: "Clustering Eras"
category: Tournament
url: https://forum.numer.ai/t/clustering-eras/4863
created_at: 2022-01-28T03:56:20.049000+00:00
last_posted_at: 2022-02-02T21:58:41.770000+00:00
posts_count: 16
views: 2325
tags: []
---

# Clustering Eras

---

### Post #1 — **dzheng1887** | 2022-01-28 03:56 UTC

I’ve been trying to do some work to cluster Eras. However, my algorithm relies on the actual return of the period within era as well which we do not get with live data. I tried without the return of the period, but the clusters are not so good. Has anyone else made progress on this?

This is just some rough algorithm. I am just experimenting with things until I find something more promising to use some Bayes

[![xgboost_validation1](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/5/5562893de540c18bf2203602c84b736b291e9a2b_2_690x459.png)xgboost_validation11200×800 27.6 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/5/5562893de540c18bf2203602c84b736b291e9a2b.png> "xgboost_validation1")

  


[![xgboost_validation2](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/0/060008f7a5f467235fe8056aee637bfe3593bfd6_2_690x459.png)xgboost_validation21200×800 34.9 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/0/060008f7a5f467235fe8056aee637bfe3593bfd6.png> "xgboost_validation2")

---

### Post #2 — **gammarat** | 2022-01-28 05:07 UTC

I am working on clustering eras, but I’m using Signals rather than the Tournament. (Signals is great for this sort of experimentation). But the underlying process is the same, and if I get it working there I’ll move the ideas into the Tournament models.

As for the clustering, and in a very simplified form, what I’m aiming at is clustering eras by which eras can be used to invert, or solve, others, and how to identify the likelihood of a new era belonging to this or that cluster.

That decision rests on finding some sort of fingerprint, or signature, from the features themselves that can be used to identify how a new era most likely relates to known clusters.

---

### Post #3 — **dzheng1887** | 2022-01-28 15:59 UTC _(reply to #2)_

I am surprised with how many people participate in signals. I figured it would be way more difficult to put together all your own data. Then you don’t even know how much your data is already in the tournament dataset? It seems like a lot more work no?

Yes, what you describe is my approach as well for the upcoming unknown era. But I find some function of return data of the period is most important. Otherwise, I do not get the orange lines are down like the picture above. Perhaps I didn’t cluster well enough though.

---

### Post #4 — **quantverse** | 2022-01-29 10:18 UTC

It could be an interesting idea to base the clustering on some macro indicators (VIX, inflation rate, interest rates) - at least for Signals, where you can use any data you wish.

Interesting blog post from Two Sigma on this topic: [A Machine Learning Approach to Regime Modeling - Two Sigma](<https://www.twosigma.com/articles/a-machine-learning-approach-to-regime-modeling/>)

---

### Post #5 — **gammarat** | 2022-01-29 11:19 UTC _(reply to #4)_

I use Gaussian mixtures extensively in the Tournament; they’re great. In Signals, I’ve just recently started using them to separate regimes, based on signatures taken from weekly eras. Finding a practical set of numbers from features only to define a signature took some experimentation, but this week it finally seems to be working—for example, without referencing target returns, it separated out the regions immediately after market crashes (when the Fed tends to really loosen the purse strings).

---

### Post #6 — **dzheng1887** | 2022-01-29 15:47 UTC

Thanks for the resource! I have tried GMMs as well, but probably placed too many features in them. Probabilities were 0/1 when predicting eras

![:sweat_smile:](http://forum.numer.ai/images/emoji/twitter/sweat_smile.png?v=10)

---

### Post #7 — **sneaky** | 2022-01-30 19:08 UTC

Hi, I cluster eras by analyzing how well you can predict an era by overfit another era.  
The idea is: If you have an overfitted model to an era A and it is good at predicting an era B, then A and B should be similar.

How I do it:

  1. Create one model per era and train it only on its era.
  2. With every model predict every era.
  3. Measure the correlations between the predictions and targets.
  4. Create a matrix where each row is made of model correlations.



The matrix of correlations between eras sorted by era number:  


[![usefullness_of_eras1](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/8/8a0e0f2ca308266a760a328d46226e882058d1c3.png)usefullness_of_eras1480×480 159 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/8/8a0e0f2ca308266a760a328d46226e882058d1c3.png> "usefullness_of_eras1")

After a little bit of preprocessing and dimensionality reduction I cluster them.  
I played with different number of clusters and came up with 5,3, and lastly 4 being the best.

The next picture has same values as the first one, but now its sorted by cluster and number of an era within a cluster. That’s why you can see square patterns (clusters), and the waves across the squares (eras tend to be similar to eras that are timewise close to them)  


[![usefullness_of_eras2](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/f/f09436174ff51299fec0f27db2d68d8479dc9ade.png)usefullness_of_eras2480×480 160 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/f/f09436174ff51299fec0f27db2d68d8479dc9ade.png> "usefullness_of_eras2")

I am currently working on a model that would harvest this knowledge, so far it was better to use era boosting method. The era boosting method does a similar thing, but it better targets the weaknesses of a little-meta model. With the new data I have more success but the computations take a lot of time, I hope it will be worth it at the end :).

I trained 3 models on 3 clusters (now I use 4) separately to see how they would do over time, and it seems that they nicely complement each other; therefore, if I am able to guess when to use which…

[![Screenshot from 2022-01-30 19-58-03](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/6/618f848a3726af514574e6bd8b070f7787018101_2_690x231.png)Screenshot from 2022-01-30 19-58-031124×377 48.3 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/6/618f848a3726af514574e6bd8b070f7787018101.png> "Screenshot from 2022-01-30 19-58-03")

Now I am working on meta model that would predict which era is which, thus would not need a target to classify tournament eras.

---

### Post #8 — **sneaky** | 2022-01-30 19:14 UTC _(reply to #7)_

Also, I thought of using the correlation matrix as an era selection technique. It could be theoretically possible to identify “weak eras”. By weak I mean that the model don’t learn anything from them and or they are easy to predict. But my learning PC Abacus is non-stop working on other trials.

---

### Post #9 — **dzheng1887** | 2022-01-31 02:35 UTC

That is very interesting work, thank you for sharing. The models are definitely a more complicated version of the correlations between features and target cluster I performed. I realized something though.

Because I used the return in the correlations in the clustering algorithm, if I then used the same returns during validation or tournament prediction (not possible because we don’t know), then I think I am essentially causing some data leakage into the model. That is because the cluster information tells me something about the return in that period already. I am not sure if you are using the same thing when training on each individual era.

Instead, you will want to use the prior return period perhaps, or just throw returns out all together would be the safest probably.

---

### Post #10 — **sneaky** | 2022-01-31 09:29 UTC _(reply to #9)_

Yes, you cannot use the era models to classify the validation/live data. I am trying to create meta model that would learn on aggregated features of eras, with clusters being the target. For simple example:
    
    
    X = df[features+['era']].groupby('era').var()
    y = era_clusters
    

but of course var is not enough. The best part is, you can add training data for this meta model from each epoch, because aggregated features cannot be obfuscated. You just have to determine the cluster of an epoch. Or you can add data from the outside of the tournament like S&P500 index, but it will take some time to collect them.

---

### Post #11 — **sneaky** | 2022-01-31 09:36 UTC

Disclaimer: I don’t know if it is gonna work yet. I planned to write an article about it if it works.

---

### Post #12 — **profricecake** | 2022-02-01 16:40 UTC _(reply to #6)_

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/s/4bbf92/48.png) sneaky:

>   * Create one model per era and train it only on its era.
> 


How did you determine when to stop training? Did you hold out some portion of an era as validation? Did you use CV? Or did you deliberately let these models overfit given that you only wanted to use them to measure era similarity?

thx

---

### Post #13 — **sneaky** | 2022-02-01 21:07 UTC _(reply to #12)_

To select hyperparameters I used CV. Then I trained for each era a model with the same parameters without any validation. The idea is to overfit the era, but not overfit the data points. If it makes sence.

---

### Post #14 — **profricecake** | 2022-02-01 21:36 UTC _(reply to #13)_

Good to know. Thanks. I assume you found different hyperparameters for every era?

---

### Post #15 — **sneaky** | 2022-02-02 21:41 UTC _(reply to #14)_

No, I used same hyper parameters for every era. It would be time consuming to fine tune for every era, and I don’t think it is needed.

This is just my intuition, but I think that you don’t need to fine tune the hp for every era, because the number of rows and columns are the same. Yes, there should be a difference in the number of useful features, but in the worst case scenario the era model learns fewer of the less useful features, because it should prioritize the more important features. And that is something that won’t affect the clustering much.

---

### Post #16 — **profricecake** | 2022-02-02 21:58 UTC _(reply to #15)_

Thanks for the response. I share your instinct about not needing new HPs for every era. But for the sake of accuracy, the number of columns are the same across eras but the number of rows varies with each era.
