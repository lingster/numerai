---
title: "Numerai Self-Supervised Learning & Data Augmentation Projects"
category: Data Science
url: https://forum.numer.ai/t/numerai-self-supervised-learning-data-augmentation-projects/5003
created_at: 2022-03-02T00:08:24.159000+00:00
last_posted_at: 2023-03-22T14:27:47.357000+00:00
posts_count: 115
views: 11073
tags: []
---

# Numerai Self-Supervised Learning & Data Augmentation Projects

---

### Post #1 — **richai** | 2022-03-02 00:08 UTC

[original Tweet thread on this topic](<https://twitter.com/richardcraib/status/1498167957263839233>)

[![Screen Shot 2022-03-01 at 3.32.34 PM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/c/c584729acc0ee9fbcd2357860b4788196daca12d_2_689x136.png)Screen Shot 2022-03-01 at 3.32.34 PM1196×236 50.1 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/c/c584729acc0ee9fbcd2357860b4788196daca12d.png> "Screen Shot 2022-03-01 at 3.32.34 PM")

  
Project 1

[![Screen Shot 2022-03-01 at 3.36.01 PM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/5/5615d4f77661b1d7844ffdfd75f9825ac55e09a7_2_690x135.png)Screen Shot 2022-03-01 at 3.36.01 PM1178×232 50.6 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/5/5615d4f77661b1d7844ffdfd75f9825ac55e09a7.png> "Screen Shot 2022-03-01 at 3.36.01 PM")

  
Project 2

**Discussion on Methods**

From our first Twitter Spaces discussion today, [@jrb](</u/jrb>) recommended Contrastive Self-Supervised Learning worked well for him for this project or creating new features.

Principal Components Analysis would also be a very basic way to generate unsupervised features like this. The goal is to make these new features maximally helpful for some later model to train on and I don’t think PCA works especially well but haven’t checked in a while on the current data.

Another method discussed was Diffusion Models. These models would take in a very noisey version of an era matrix and output another matrix which looks more like a real era. This models have had excellent results generating realistic images from noise.  
[Diffusion Models Paper](<https://arxiv.org/pdf/1503.03585.pdf>)

We also discussed how [the solution to the Jane Street Competition on Kaggle involved using an auto encoder to create new features](<https://www.kaggle.com/c/jane-street-market-prediction/discussion/224348>). See also the excellent thread on this with [@jrai](</u/jrai>) [on Numerai’s forum](<http://forum.numer.ai/t/autoencoder-and-multitask-mlp-on-new-dataset-from-kaggle-jane-street/4338>).

**Discussion where this fits with Numerai**  
If Numerai could create excellent new features or eras from these methods we could potentially make them available to everyone as features in our Data API. We could also potentially learn the new synthetic features or eras on our raw data which could be even more useful. Ultimately, giving out more features and more data to Numerai users using these methods could improve everyone’s models significantly.

**Projects**  
If you want to work on these projects, then describe how you plan to solve them in a reply to this blog post. Code snippets will be useful. If have gotten to the point of demonstrating the success of your method, I would be happy to get on a call 1-1 with you to take a look. But first try to convince me here on the forum that it’s good and ready for me to criticize. We do want to share this research publicly so anyone can use. It might even make it into an example script some day. We use PyTorch a lot, I think it would be best if you could use that if you know it but we’re not super strict.

**Prizes**  
I am hoping to make rapid progress on this this month in March. If you have something good, Numerai will get you flights and hotel to come present it to everyone at NumerCon on April 1 in SF and will also give large retro-active bounty if its especially good and our chief scientist Michael Oliver would also want to interview you for a full time job in research at Numerai.

---

### Post #2 — **nyuton** | 2022-03-02 08:10 UTC

Hi Richard,

[Umap](<https://umap-learn.readthedocs.io/en/latest/>) generates useful features from the dataset, while reducing dimensionality. Unlike PCA, Umap works with the Numerai dataset.  
I got the idea, from [Marcos Lopez de Prado’s lecture](<http://forum.numer.ai/t/how-to-solve-the-numerai-tournament-lecture-by-marcos-lopez-de-prado/3982>):

I’ve been using it for a while.

See here:  
[Numerai](<https://numer.ai/nyuton_test12>) (a newer but apparently improved version)  
[Numerai](<https://numer.ai/nyuton_test10>) (since round 275)

It won’t hit the #1 spot on the leaderboard based on CORR, but the created model has ~10% correlation with the metamodel and MMC/CORR ratio is good. It will be interesting to see it’s TC score.

Best part of it is, that it’s very simple:  
fit = umap.UMAP(n_components=100, min_dist=0)  
transformed_data = fit.fit_transform(data)

Because it’s learns embedding without the labels, I can use test AND live for the umap model as well.  
Once the dataset is transformed you can train any model on it.

---

### Post #3 — **eleven_sigma** | 2022-03-02 18:02 UTC

Hi Richard, Interesting initiative.  
I see three problems here:

  * If we have a potentially new good idea in mind, to develop and test it with new rounds is not possible before 1st April.
  * If the idea really work I can’t imagine a ‘large retro-active bounty’ that can compensate a team have several thousands of NMR at stacking.
  * You are asking for write the ideas in open forum so if we write one and you decide it is not interesting, we will loose all the advantage of this idea respect the rest of community.

---

### Post #4 — **nyuton** | 2022-03-03 09:08 UTC _(reply to #2)_

To back up my claims in my previous reply I created a sample script for applying umap to the dataset.

You can find it here with all related validation data: [numerai/Umap_eval at main · nemethpeti/numerai · GitHub](<https://github.com/nemethpeti/numerai/tree/main/Umap_eval>)

Note: this is meant to be fast and simple.  
It uses only the “medium” featureset and there are tons of ways to optimalize the code and improve the results.

Results are the following:

  * XGB baseline  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/9/9c96c783ddf66da4a1cc602cbbd4ccaba1fd3f08_2_690x484.png)image957×672 50.8 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/9/9c96c783ddf66da4a1cc602cbbd4ccaba1fd3f08.png> "image")

  * XGB model that uses the features from the dataset as well as the newly generated umap feature  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/5/566e349513ac9952b555c494abc90df9523f6bd2_2_690x483.png)image957×671 52.1 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/5/566e349513ac9952b555c494abc90df9523f6bd2.png> "image")

  * XGB model for the umap features only  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/2/2db2edfa0e2f7491c19f13d63669145c71eb095c_2_690x488.png)image955×676 52.3 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/2/2db2edfa0e2f7491c19f13d63669145c71eb095c.png> "image")




Extending the dataset with the umap features improves basically all validation metrics. And it’s worth noting again, that these improvement can be further magnified by better model and hyperparameter selection. Still it’s performance is highly correlated with the baseline model.

I included the last diagnositics to show that while it’s corr is low it has the highest MMC mean and I bet it will have the highest TC as well.

It’s not alien performance, but it’s a very simple transformation that can be used by anyone.

---

### Post #5 — **katsu1110** | 2022-03-03 11:34 UTC

[@richai](</u/richai>)  
Hi Rechard, thanks for interesting projects (and of course creating Numerai)!

I have been interested in both self-supervised learning and data augmentation approaches, but haven’t really worked on them. So this is a good time to push myself a bit:)

I started with the Project 2: data augmentation.

My approach is very simple: **cutout** , where randomly selected columns per era are set to be 0.5. Those ‘new’ rows are concatenated to the original train data (so more rows apparently).

In this way I expect that whatever model we train is forced to learn from variety of features, making their predictions robust.

Here is my experimental setup:

Data: [ [Numerai] train & validation with kazutsugi & nomi](<https://www.kaggle.com/code1110/numerai-train-validation-with-kazutsugi-nomi>)

This is an old data from you with both target_nomi and target_kazutsugi available. What’s good with this data is that the size is handful enough for me to experiment many things. Also the validation data is fixed so no update of the validation score every week.

Model: XGBoost

I compared validation scores from the baseline XGBoost and XGBoost with the cutout. Of course the only difference is whether there is a cutout or not.

The entire code is available:

  * [XGBoost baseline](<https://www.kaggle.com/code1110/numerai-xgb-baseline>)
  * [XGBoost with cutout](<https://www.kaggle.com/code1110/numerai-data-augmentation>)



The validation score from the baseline is this:

[![スクリーンショット 2022-03-03 20.22.02](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/4/40cbdca1565c223adb3aa96ca922deef4c972d21.png)スクリーンショット 2022-03-03 20.22.02427×212 30.7 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/4/40cbdca1565c223adb3aa96ca922deef4c972d21.png> "スクリーンショット 2022-03-03 20.22.02")

This is from the one with the cutout:

[![スクリーンショット 2022-03-03 20.22.53](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/4/4bbce436727a86c5817154b6342c2c423fe1da62.png)スクリーンショット 2022-03-03 20.22.53428×213 30.1 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/4/4bbce436727a86c5817154b6342c2c423fe1da62.png> "スクリーンショット 2022-03-03 20.22.53")

The validation period is split into two: era < 150 (val1) and era > 150 (val2). The val2 is harder to predict, which you should know.

We can see good improvements in Corr Sharpe and Max Feature Exposure in the both validation periods!

I have to say, this is still a wip but for me looks promising.

---

### Post #6 — **nyuton** | 2022-03-03 19:48 UTC _(reply to #2)_

Just got the TC scores on the above mentioned models.

[Numerai](<https://numer.ai/nyuton_test10>) is at 116 place on TC score  
[Numerai](<https://numer.ai/nyuton_test11>) which is a neutralized version of the same model is #78

Wen staking on TC???

---

### Post #7 — **orbitalteapot** | 2022-03-03 22:12 UTC

Can only contribute with some inspo atm…

[en.m.wikipedia.org](<https://en.m.wikipedia.org/wiki/Siamese_neural_network>)

### [Siamese neural network](<https://en.m.wikipedia.org/wiki/Siamese_neural_network>)

A Siamese neural network (sometimes called a twin neural network) is an artificial neural network that uses the same weights while working in tandem on two different input vectors to compute comparable output vectors. Often one of the output vectors is precomputed, thus forming a baseline against which the other output vector is compared. This is similar to comparing fingerprints but can be described more technically as a distance function for locality-sensitive hashing.[citation need It is possi...

And (from 47:15) for Yann LeCun explaing it (AI folk at Meta)

[ ![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/5/5fe5d44c54095f95373ab29e4fd0809de3b0b443.jpeg) ](<https://www.youtube.com/watch?v=SGzMElJ11Cc>)

---

### Post #8 — **richai** | 2022-03-04 19:49 UTC _(reply to #4)_

Very nice. It’s good to watch for a jump in FNC as FNC is the most correlated with True Contribution.

---

### Post #9 — **richai** | 2022-03-04 19:53 UTC _(reply to #3)_

Totally get it. This is just for people who are willing to publish and share their ideas.

---

### Post #10 — **maxchu** | 2022-03-05 00:46 UTC _(reply to #9)_

I think ppl can just DM you with their ideas. If it turns out to be a great idea, you offer them the prize, and then they need to share the idea.

---

### Post #11 — **sunkay** | 2022-03-05 02:13 UTC _(reply to #4)_

I also tried to use UMAP before. I used it on all the features and failed because of lack of ram space. Even apply it on medium feature set, it require a lot ram space, right?

---

### Post #12 — **nyuton** | 2022-03-05 07:18 UTC _(reply to #11)_

Yes [@sunkay](</u/sunkay>), that would be the whole purpose of this initiative and that is why I didn’t hesitate much to opensource it!

The idea works for sure! In fact, it’s proven to be valuable. My best Umap model ranks [#60](<https://numer.ai/nyuton_test11>) on TC at the time of writing, but it’s based on the LEGACY dataset.

I’ve got 64GB RAM with 24GB GPU and I can’t crack the full new dataset with this hardware.  
The medium featureset is barely doable with some tricks to save ram.

However if [@richai](</u/richai>) jumps in, he can make these features available for everyone. Including me ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=10)  
That’s the goal of these projects, right? Find valuable features and make them available for everybody for free.

If the legacy dataset brings a model to #60, the featureset on the full dataset can go even closer to the top.  
And while not everybody has the resources to calculate this featureset, it’s not going to break the bank at Numerai for sure. They have heavier workloads than this one.

---

### Post #13 — **katsu1110** | 2022-03-05 08:44 UTC _(reply to #5)_

[@richai](</u/richai>)  
Hi Richard, let me share my approach regarding the Project 1: Self-supervised learning.

My approach is again very simple: **factor analysis**. It is more like a feature engineering technique like PCA rather than SSL but I guess this can fit in this project category.

I expect the factor analysis to find ‘common factors’ which generate numerai features. If we could find out such ‘common factors’, those ‘factors’ would be something less noisy than the original numerai features but effectively captures what constitutes them.

My experimental setup is the same as my approach to the project 2.

Data: [ [Numerai] train & validation with kazutsugi & nomi](<https://www.kaggle.com/code1110/numerai-train-validation-with-kazutsugi-nomi>)

The entire code is again available:

  * [XGBoost baseline](<https://www.kaggle.com/code1110/numerai-xgb-baseline>)
  * [XGBoost with factor analysis](<https://www.kaggle.com/code1110/numerai-factor-analysis>)



The validation score from the baseline is this (same as the project 2):

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/4/4767f720ea6e4aef4026a38bde77fb6f3e47b0db.png)image423×208 29.6 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/4/4767f720ea6e4aef4026a38bde77fb6f3e47b0db.png> "image")

This is from the one with the factor analysis:

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/0/0c223c48f6d239a162f4446766ac6779cae72c8b.png)image423×207 30.2 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/0/0c223c48f6d239a162f4446766ac6779cae72c8b.png> "image")

The improvement in the Corr Sharpe can be seen again in the all validation periods!

In this post I would like to share that even a simple unsupervised learning technique can contribute to improving scores, so a more fancy SSL could improve them a lot!

---

### Post #14 — **sunkay** | 2022-03-05 11:29 UTC _(reply to #12)_

Based on my observations，the new dataset is much noisier than the legacy dataset. I think features generated by umap would be better if we do feature selection first and then apply umap to those features.

---

### Post #15 — **preparedzebra** | 2022-03-14 04:33 UTC

I am tackling the problem of creating synthetic features using a deep autoencoder.  
  
The autoencoder takes two inputs: the features for a single row, and the era number.  
The autoencoder does two kinds of augmentation to the inputs:

  * 1.) Maps them through a randomly initialized, frozen deep network. This is called [extreme learning](<https://ieeexplore.ieee.org/document/1380068>).
  * 2.) Concatenates the original features with 0.3 dropout to the “extreme” features.



The model encodes these inputs to a 12-dimensional latent space. Then it decodes the latent back to the full original feature space and is scored with mean squared error.  
I train only on train-data eras.  
I found it improved generalization to linearly interpolate eras from [0, ~550] down to [0, 12]. For example, era 200 will become era 5. During validation, era is set to the max value seen during training.

Once this model is trained, I create new features in two ways:

  * 1.) Use the 12 dimensional latent space as new features.
  * 2.) Use the argmax of the 12 dimensional latent space as a feature.



**Measuring the New Features**

  * Baseline: example model w/ LGBMRegressor, n_estimators = 2000
  * Baseline+Era: baseline + era feature
  * Synthetic Feature Raw: baseline + 12 synthetic features from autoencoder latent
  * Synthetic Feature Argmax: baseline + 1 synthetic feature, argmax of latent
  * Synthetic Feature Argmax+Era: above + era feature



Here are the validation scores:  


[![results_numerai_ssl_00](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/1/1c709b6e72605c6a2f532d9141ca79cb6d68d3f8.png)results_numerai_ssl_00781×127 9.17 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/1/1c709b6e72605c6a2f532d9141ca79cb6d68d3f8.png> "results_numerai_ssl_00")

The code is available on my github here:

[github.com](<https://github.com/bbrimacombe/ssl_numerai>)

![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/7/7f8f4c35864d2a455b9d5cefa9f724047e945550_2_690x344.png)

### [GitHub - bbrimacombe/ssl_numerai](<https://github.com/bbrimacombe/ssl_numerai>)

Contribute to bbrimacombe/ssl_numerai development by creating an account on GitHub.

---

### Post #16 — **preparedzebra** | 2022-03-14 04:39 UTC _(reply to #15)_

**Going Deeper**

Below are plots of the out of sample improvement over the baseline LGBMRegressor correlation.

The raw latent representation helps at first and quickly decays with time:  


[![synth_feat_raw_improvement](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/8/8223133a144416205dd17435116238d00a8c9da8_2_517x358.png)synth_feat_raw_improvement775×538 44.3 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/8/8223133a144416205dd17435116238d00a8c9da8.png> "synth_feat_raw_improvement")

Taking argmax helps:  


[![synth_feat_argmax_improvement](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/e/e93993d15225c0c2aeeb67704b2d224e2e32cfb9_2_517x365.png)synth_feat_argmax_improvement757×535 39.3 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/e/e93993d15225c0c2aeeb67704b2d224e2e32cfb9.png> "synth_feat_argmax_improvement")

Is the latent-argmax just secretely passing the era number to the model?  
No! Once we add in the era as well, it gets even better. This implies the learned representation is helping.  


[![synth_feat_argmax_era_improvement](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/1/1f3825bf666ad1228f596e12219db054e0d8896d_2_517x359.png)synth_feat_argmax_era_improvement749×521 40.5 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/1/1f3825bf666ad1228f596e12219db054e0d8896d.png> "synth_feat_argmax_era_improvement")

Baseline with era feature for comparison with above.  


[![baseline_era_improvement](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/a/a3330d4a1f175fd78d484942726504ca09e3cbb4_2_517x348.png)baseline_era_improvement765×515 37.6 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/a/a3330d4a1f175fd78d484942726504ca09e3cbb4.png> "baseline_era_improvement")

---

### Post #17 — **jefferythewind** | 2022-03-16 18:05 UTC

Wow some great work here already. [@nyuton](</u/nyuton>) thanks for the tip about UMAP, I was pondering the use of manifold learning methods for this project so I know what I’m going to try next!

I just wanted to post here I just tried a couple baseline ideas of adding 2 types of noise to the data. One is adding Gaussian noise and the other is to create new data by averaging data points. Both of these are simple ideas for create more rows of data.

For each case slight improvements can be seen in cross validation metrics when combining the raw data with the noisy data, but not just by using the noisy data. This seems consistent with some other conclusions above, where best performance is seen when attaching, or appending the new data to the original data, and not just replacing it outright.

[![Screen Shot 2022-03-16 at 2.03.21 PM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/c/c16e158b685ae1575842035b0e4ba69aa0db7ad7_2_690x99.png)Screen Shot 2022-03-16 at 2.03.21 PM2128×308 30.7 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/c/c16e158b685ae1575842035b0e4ba69aa0db7ad7.png> "Screen Shot 2022-03-16 at 2.03.21 PM")

For the Gaussian noise case, slight increase in mean is accompanied by higher variance, bring the sharpe down.

I just wanted to share for the sake of documentation. It doesn’t seem to make too much of a difference, to use either of these simple methods, especially when looking at the validation data.

Code available here: [GitHub - jefferythewind/numerai-sandbox: A Repo to Share Scripts for Numerai](<https://github.com/jefferythewind/numerai-sandbox>)

---

### Post #18 — **jefferythewind** | 2022-03-16 20:16 UTC _(reply to #6)_

I feel like you’ve really cracked a big part of the TC puzzle here. I’ve just tried some UMAP features per your instructions on the whole dataset. I definitely see the same kind of performance in the diagnostics, albeit without the MMC performance that yours showed. I would find it hard to be so sure that it would perform well on TC. Looking at your model scores, the TC sticks our by far as the best metric, top 100, where the others, even MMC are still pretty mediocre. Really interesting. A question I am having is why the correlation performance is so bad for the transformed data?

---

### Post #19 — **mdo** | 2022-03-16 22:14 UTC

Fun and simple idea for generating fake data: make a generative model of the features to target relationship. 1) fit a ridge regression model for each era 2) fit a Gaussian mixture model on all the learned regression weights 3) to generate new data take an era, sample the GMM to get beta weights, use features and beta weights to create fake raw return data, rank and bin to create new targets 4) repeat and train to infinity 5) profit! (South Park reference, not investment advice)  
[Here is a prototype for anyone interested](<https://gist.github.com/the-moliver/dcdd2862dc2c78dda600f1b449071c93>)

---

### Post #20 — **maxchu** | 2022-03-17 00:09 UTC _(reply to #17)_

your correlation mean is very high, is it a CV score?

---

### Post #21 — **jefferythewind** | 2022-03-17 00:13 UTC _(reply to #20)_

Yes CV score on the training data. It is the Light GBM model. It’s all in the notebook in the link.

---

### Post #22 — **maxchu** | 2022-03-17 00:14 UTC _(reply to #21)_

Great, your average method is something like this [[1710.09412] mixup: Beyond Empirical Risk Minimization](<https://arxiv.org/abs/1710.09412>) ?

---

### Post #23 — **jefferythewind** | 2022-03-17 00:18 UTC _(reply to #22)_

Yes it appears so. What I tried would be like setting lambda = 0.5 for every example. I will try this mixup too. Here were the results from that trial. Didn’t seem really to improve. These MMC stats aren’t accurate, but I image it would improve the MMC.  


[![Screen Shot 2022-03-16 at 8.19.45 PM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/2/2ae7240b7ceb976172b66e90221bce6d28a0018e_2_690x96.png)Screen Shot 2022-03-16 at 8.19.45 PM1994×280 48.1 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/2/2ae7240b7ceb976172b66e90221bce6d28a0018e.png> "Screen Shot 2022-03-16 at 8.19.45 PM")

---

### Post #24 — **nyuton** | 2022-03-17 07:57 UTC _(reply to #18)_

Jeffery,

TC is simple: your model has to have **some correlation with the target** and it **must be very different** from other models.

Check out the screenshot I posted above. It has ~0 correlation with the example prediction. The baseline model has 0.64 correlation. A model based on umap is very different from other methods. Not better, but different. That’s the key!

Umap gives a different representation of the data, it brings extra information to the metamodel, hence it’s value!

---

### Post #25 — **jefferythewind** | 2022-03-17 12:44 UTC _(reply to #24)_

Thanks for the explanation. Interesting thing that is a bit different from what Richard mentioned is that the models have relatively low FNC.

---

### Post #26 — **wigglemuse** | 2022-03-17 13:35 UTC

Is TC actually relatively easy to achieve? I’m beginning to think so. Up until now we’ve been trying to make overall strong models but that tends to make them converge somewhat to be alike. Whereas with TC it seems we can make quirky original models that don’t necessarily have to be generally strong (i.e. get good or even positive corr as raw predictions) as long as _**some part of them**_ is both relatively unique and _**that part of it**_ is correlated with the target (which might not obvious). So like arbitrage used to say with Signals “just submit a feature” – if it is a good, original, useful feature that may be enough.

So I think making generally strong models that also get decent TC is tough because that’s essentially just one more thing we are trying to be good at on top of what we have already been trying to do (make generally strong models). But if we don’t have to make generally strong models to get decent TC (and we are allowed to stake only on TC and the payout is structured is so that it is worth it) then that’s a much easier proposition, and possibly easier than what we have been doing up until now. At least at the beginning – once everybody is going for TC maybe it won’t be so easy.

Because after all, the metamodel itself is the only one that really needs to be generally strong. Using TC as the main metric turns the whole competition into boosting (in more of way than it was already) in that the component models will probably generally become weaker. It remains to be seen whether it follows that the metamodel will then become stronger than it is under current metrics, or whether it will be about the same by a different route, or actually weaken.

---

### Post #27 — **jefferythewind** | 2022-03-17 16:06 UTC _(reply to #26)_

Yes it is appearing TC is “easy” to achieve in that you don’t need to have particularly strong Corr/MMC to get high TC. This is working the way I thought MMC was supposed to originally, but I quickly learned that MMC only goes up if your Corr is in the top part of the range, that’s what it seemed to me at least. I think the catch here might be that you also have to stake Corr and/or MMC with the TC.

---

### Post #28 — **wigglemuse** | 2022-03-17 16:26 UTC _(reply to #27)_

If they require corr staking as well then they’ll be throwing away all that “new” TC that they want to capture. I’ve got some high TC models but they are not good corr models really, so I wouldn’t stake on them unless I could only do TC. It sounds like they want to go 100% TC at some point (which is fine, but would be a mistake to do too fast). But we’ll see what happens when it happens – some balance between different metrics may be best.

---

### Post #29 — **preparedzebra** | 2022-03-17 17:21 UTC

I have added a new script to my [ssl_numerai github repo](<https://github.com/bbrimacombe/ssl_numerai>) to create synthetic stocks and targets from uniform noise with a deep generative model.  
Training the LGBM baseline with 300,000 extra synthetic stocks improved sharpe from 0.715 to 0.718.  
Lots of ways to improve this. Hot tip: make the model autoregressive over features. Happy generating!

---

### Post #30 — **gammarat** | 2022-03-17 19:25 UTC _(reply to #28)_

I agree [@wigglemuse](</u/wigglemuse>) , as corr staking is the easiest thing to ~~draw in new marks~~ wrap one’s head around. Letting the payout factor continue to decrease while limiting the multiplier for corr but letting the multiplier for TC (if it works out) be high pretty much resolves the issue, afaics.

---

### Post #31 — **jefferythewind** | 2022-03-18 15:34 UTC

I used the code provided my [@mdo](</u/mdo>) and created fake targets for the entire data set and ran it through my previously-mentioned pipeline cross validation pipeline, which is in fact the same pipeline offered in the example scripts from Numerai. I just wanted to share the results here. Of course the beauty of a method like that is that we could create multiple unique copies of the data, so I am currently working on that idea, where this trial was just 1 copy of the data. I was hopeful based on the example notebook, which showed an increase in correlation on the validation set just from training on the fake data. It appears getting a performance increase on the cross validation isn’t so simple. Here we see a possible benefit of combining the fake data with a copy of the real data set. Here are the Light GBM model params:

> model_params = {“n_estimators”: 2000,  
>  “learning_rate”: 0.01,  
>  “max_depth”: 5,  
>  “num_leaves”: 2 ** 5,  
>  “colsample_bytree”: 0.1}

[![Screen Shot 2022-03-18 at 11.27.13 AM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/6/644a7ef48d1ebb8ec5932ae60c8d81a116d4be5e_2_690x107.png)Screen Shot 2022-03-18 at 11.27.13 AM2114×330 31.1 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/6/644a7ef48d1ebb8ec5932ae60c8d81a116d4be5e.png> "Screen Shot 2022-03-18 at 11.27.13 AM")

---

### Post #32 — **nyuton** | 2022-03-18 16:55 UTC

Siamese networks bring great results as well.

I created a proof-of-concept for siamese network on the “small” subset of the numerai dataset. The original idea comes from image similarity, but it can be adopted to the numerai dataset as well.  
The basic idea is to learn an embedding based on the similarity of training examples.  
Learning objective is that the euclidean distance of any two of the learned embeddings should be proportionate to the distance of the corresponding labels.

Results are the following:

  * Baseline XGB model on the small dataset:  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/a/a0be2817a8570032a4f6e7854a26dbe81b434469_2_659x500.png)image712×540 36.3 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/a/a0be2817a8570032a4f6e7854a26dbe81b434469.png> "image")

  * XGB model on the extended dataset (small subset + learned embeddings)  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/9/9756d93c41970dfe4c88027ae9a1d5f940851232_2_657x500.png)image708×538 36.2 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/9/9756d93c41970dfe4c88027ae9a1d5f940851232.png> "image")

  * XGB model on the learned embeddings only  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/4/4945d63417952359d17d4edfe733ec820929212c_2_653x500.png)image710×543 38.3 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/4/4945d63417952359d17d4edfe733ec820929212c.png> "image")




Concatenating the original dataset with the newly learned embeddings improves all validation metrics.  
Training a model on the embeddings only results in lower correlation with the metamodel and probably a higher TC. I don’t have it live yet.

Next task is to scale this up to the whole dataset.

Has anyone attempted a Numerai variant of DeepDream?  
We could dream new training examples based on the embeddings learnt here…

---

### Post #33 — **mdo** | 2022-03-18 20:20 UTC _(reply to #31)_

Hey, that’s a pretty great result IMO. I’m actually quite impressed the fake targets by themselves can work as well as they do since they are usually only about 5% correlated with the original targets for an era. So many way to improve from here, e.g. ensemble models trained on many copies of data, train single models much longer on more data, etc…

---

### Post #34 — **jefferythewind** | 2022-03-18 21:58 UTC _(reply to #31)_

Yes I agree, it is pretty interesting. I’m about to do a trial where I use 3-4 batches of synthetic training data to see what happens. Also, to me the interesting thing is the data set of coefficients. This data set is 574 rows (# of eras) and 1050 columns (# of features). I put it through a t-SNE projection and it appears there may be some manifold structure there, hard to tell the significance, but cool to look at. I think significantly we can see that there appear to be 7-8 distinct clusters.  


[![Screen Shot 2022-03-18 at 1.38.33 PM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/3/3ffe2f6f6ff6883712ef6add7f06af47cb44ef19_2_678x500.png)Screen Shot 2022-03-18 at 1.38.33 PM1858×1370 98.3 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/3/3ffe2f6f6ff6883712ef6add7f06af47cb44ef19.png> "Screen Shot 2022-03-18 at 1.38.33 PM")

---

### Post #36 — **mdo** | 2022-03-18 23:29 UTC _(reply to #34)_

Very pretty! I assume the filament structures are ordered eras so it would be cool to color by era number just to see where the discontinuities lie. Makes me think jump-diffusion type models might be interesting here, but I don’t really know much about them. Finding better ways of modeling and sampling that manifold might also work better than a GMM.

---

### Post #37 — **jefferythewind** | 2022-03-19 13:42 UTC _(reply to #36)_

The basic idea of tSNE is in low dimensional embedding both local and global distances are somewhat preserved. points that appear close together in the image should also be close together in the raw data and vice versa. I don’t think we can say anything about the ordering, but I will check. We only have 574 data points in 1050 dimensional space. I think it deserves further investigation. One extension could be to swap out a feed forward NN for the  
ridge regression but then our coefficients would have much larger dimensionality than just 1050.

---

### Post #38 — **wigglemuse** | 2022-03-19 14:07 UTC

I think you will find that the points next to each other in space are also next to each other in time.

---

### Post #39 — **mdo** | 2022-03-19 15:57 UTC _(reply to #37)_

Regression weights from adjacent eras are likely to be similar simply because the targets are based on 75% overlapping return data, and thus are likely to map to similar points in space. The filament breaks are then potentially good indicators of regime changes.  
The problem with replacing linear weights with a NN is that the weights from NNs trained on different eras will have no natural correspondence and consequently a dimensionality reduction on these weights makes no sense. If this is not obvious, just consider that you can change the ordering of hidden units (and appropriately swap their corresponding input and output weights) without changing the function the NN computes at all. A polynomial or spline expansion could work, but that would create **lots** more weights.

---

### Post #40 — **jefferythewind** | 2022-03-19 16:07 UTC _(reply to #39)_

Super interesting. I’m using google’s tSNE embedding projector. Works great with a small data set like what we have. They didn’t have away to color the points but I can label them by era… It seems both you and [@wigglemuse](</u/wigglemuse>) were right!

---

### Post #42 — **jefferythewind** | 2022-03-20 01:26 UTC

Here are the results of a trial using 4 copies of the data set with synthetic targets based on [@mdo](</u/mdo>)’s code (the targets are different for each copy). We see correlation (and MMC) now beating the raw data however sacrificing variance.  


[![Screen Shot 2022-03-19 at 9.23.27 PM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/8/8707119fcd316d48a3f930da5da0d2097028324f_2_690x109.png)Screen Shot 2022-03-19 at 9.23.27 PM2126×336 31 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/8/8707119fcd316d48a3f930da5da0d2097028324f.png> "Screen Shot 2022-03-19 at 9.23.27 PM")

---

### Post #43 — **of_s** | 2022-03-20 14:14 UTC _(reply to #38)_

Which is why releasing the targets from concluding rounds has been the single biggest improvement they could have done for the dataset, and ultimately scores.

---

### Post #44 — **jefferythewind** | 2022-03-20 14:23 UTC _(reply to #43)_

Excuse me, when and how have they done this?

---

### Post #45 — **of_s** | 2022-03-20 14:25 UTC _(reply to #44)_

_**could**_ have done…been arguing for it for years!

---

### Post #46 — **jefferythewind** | 2022-03-20 14:31 UTC _(reply to #45)_

yeah cause if you look at the tSNE image eras 5 steps apart aren’t too far from each other.

---

### Post #47 — **wigglemuse** | 2022-03-20 15:06 UTC

Well, maybe, maybe not. We’re just looking at the feature data here I think, not the relationship of the feature data to the targets. (Let’s see that visualization for regression weights of models trained on single eras – does it look so neat?) If you remove the overlaps between eras so they are at least 4 weeks apart (i.e. like the legacy dataset), if you train on era 120 to predict era 121, and train on era 122 to predict on era 123 and so on, do you do better than just training on eras 1-120? (I do know if you look at present eras and try to find similar eras from the distant past and weight them more heavily, that doesn’t seem helpful.)

But anyway, you probably do perform better weighting recent data heavily at least some of the time, maybe even most of the time. Therein lies the danger. Because then you will also have some catastrophic failures when things change because you are so overfit to recency. So it would be a high-risk high-variance strategy, and I think that is historically one reason they’ve wanted to hold back that recent data. (They used to say just that.) Of course, you can say that no no you’ll do it properly and with balance etc etc and I don’t doubt it, but that temptation to roll the dice on recency (especially when recent rounds have been getting big scores) will exist for everybody (not just sober-minded and uber-disciplined folks) and it is a real risk to the metamodel as a whole. (At least under corr scoring, not sure about TC.) And it is hard to see how this will not lead to increased variance of the metamodel, right? Anybody clamoring for an unending stream of the latest resolved targets can only intend to be using the latest resolved targets as they come in, right? i.e. They are planning on updating their models continuously (or fairly often) with the latest data, and this can only lead to weighting recency more and more – any time a trend develops it will prod those people to weight recency even more because that’s what’s winning right now and they will feel they are missing out. (Isn’t this how bubbles occur?)

Well, you can see where I’m going with this. I’m not saying they shouldn’t release this data, or that it will not be a net positive, but this idea that it is a slam-dunk obviously 100% correct thing to do that will most definitely be awesome is not supportable imo. And it could easily look great for a while…until it doesn’t. If you are a young market neutral fund doing well, and then doing even better, but then suddenly crash when things change…well that’s that, who’s going to trust you now? Remember the entire point of a fund of this type is to be invariant to market conditions and trends as much as possible – it is supposed to just chug along getting decent positive returns in all markets, and the more that recency controls the character of the models that make the predictions the more it is setting itself up to be catastrophically wrong when things suddenly change and all those (now) less-weighted lessons from the past are not saving us anymore. So there is certainly upside to more data, but with continuous availability of the most recent data let’s not pretend there is no potential downside.

But in any case, it sounds like within a month we’ll begin to find out what happens…

---

### Post #48 — **of_s** | 2022-03-20 15:49 UTC _(reply to #47)_

We’ve shared this difference of opinion before in RC and the “so overfit to recency” assumption implies our models degenerating into a simple martingale which has been shown to be a terrible practice in the finance literature. I don’t think anyone here subscribes to the EMH, otherwise they wouldn’t bother participating!

---

### Post #49 — **luee** | 2022-03-20 16:16 UTC _(reply to #47)_

This seems to go against the general ethos of crowdsourcing predictions which would be closer to “the swarm knows best” and further from “the swarm cannot be trusted and must be limited for its own good”. Not releasing the data is a huge design decision that is being made unilaterally without any input from “the swarm”, which if recent Numerai results are anything to go by, does know best when it comes to data science

---

### Post #50 — **wigglemuse** | 2022-03-20 16:18 UTC _(reply to #48)_

Which is exactly why in the above I put the bit about you can argue that YOU would do it properly, and I don’t doubt you. YOU are not everybody else. You are making an assumption also there are no degenerate gamblers (as we responsible gamblers like to affectionally call them) in the crowd here, or that we wouldn’t attract any. (We have even seen new people show up asking for the recent data to train on please because obviously that’s the most important thing.) And I know from many years experience that there are gamblers everywhere just waiting to pounce on anything that remotely seems like an easy score. (Like when the examples predictions do well, you’ll find more and model people just submitting the examples.) There will probably be people training on the most recent resolved era only, and then putting those preds up for sale on NumerBay as soon as they hit a lucky streak where recency reigns because sometimes it will. So there is no question that recency will become more of a factor, which is probably good. It creates a temptation to overweight it though because it is there and obvious and will do really well at times. People succumb to temptations – that’s the way people are. So basically, I really can’t see people on average landing on just the right balance, that just doesn’t pass the smell test. But right now we are overweighted to the past (since we have no choice). Moving the overweight to the recent past may or may not be better, and could well be worse. We’ll see…

---

### Post #51 — **wigglemuse** | 2022-03-20 16:21 UTC _(reply to #49)_

Yes, I agree actually. But is it like making weed legal or making heroin legal? You can compellingly argue personal freedom in both cases, but the second one still gives me pause as to whether that is really gonna be better or not…

---

### Post #52 — **luee** | 2022-03-20 16:23 UTC _(reply to #50)_

Emphasis on “swarm” here, individuals will always be found pushing their luck and blowing up, but now that reasonable capital is present and that 2-bits players have a limited impact on the meta-model, the group as a whole may be savvier/more risk-averse. Also, the opposite risk is definitely present, we cannot currently adapt to changing market conditions which may blow up the fund.

---

### Post #53 — **luee** | 2022-03-20 16:24 UTC

Yeah I don’t think we disagree, but we seem to have a different perspective

---

### Post #54 — **luee** | 2022-03-20 16:29 UTC _(reply to #51)_

I’ll be getting nitpicky here as I broadly agree, but I think the nuance here is that individuals tend to overweight short-term reward and underweight long-term risk, i.e. we may be seeing an uptick in heroin addiction that individuals would be net losers in. But, philosophically at least, I would consider something like Numerai to be more akin to a market where long term risk/reward are more accurately weighted, even if the individuals making up Numerai may blow up on risky setups

---

### Post #55 — **wigglemuse** | 2022-03-20 16:29 UTC _(reply to #52)_

The idea that people think they need to deftly and nimbly move their models to some new space to rapidly adapt to current conditions is exactly what worries me.

One of my favorite thinkers in the geopolitical space (Walter Russell Mead) uses an analogy about the stability of countries/societies that compares clipper ships to rafts. Clipper ships are fast and can get where they need to go quickly, they can change course at will, etc. They also tend to capsize in bad storms, crash on rocks, get themselves in bad situations due to arrogant captainship, etc. Whereas a raft is nearly unsinkable, but the price is it is slow, you can’t maneuver much, and your feet are always in the water. Sitting on the raft, the clipper ship seems much nicer…until it doesn’t. Bet on the raft to survive longer.

---

### Post #56 — **luee** | 2022-03-20 16:35 UTC _(reply to #55)_

That is probably the correct course for 9 years 11 months out of a decade, I think we just have different weights internally associated with different values (market solution, stability, long term vs short term, etc…), no arguing past that if your position is coherent with regards to what you care about and so is mine

---

### Post #57 — **wigglemuse** | 2022-03-20 16:36 UTC

Getting back to nuts and bolts – somebody show me that it is true. Make me the graph that shows unequivocally that recent market conditions predict soon upcoming market conditions better overall than not having that data. (But not just in the “more data = better models” sense – show me it HAS to be the most recent data.)

---

### Post #58 — **luee** | 2022-03-20 16:42 UTC _(reply to #57)_

Well first in general “more data = better models”, that’s why I want more data, because we have so little too begin with. But for fast adaptation, we want the swarm to figure that part out if there is anything to even figure out. The big issue that I’m seeing is that even if the scientific community has not found anything, we probably have a larger community and more “group intelligence” than any before for this specific problem, it may be that we need a group intelligence of a certain level to even be able to entertain certain solutions

---

### Post #59 — **wigglemuse** | 2022-03-20 16:53 UTC

Well, we are getting a lot more data in any case (the whole test set). But some seem intent that we MUST have the latest data, and it MUST keep coming every week or else how can we possibly be expected to make a decent model? Besides the fact that I think we’ve already proven you can make decent models without it, the idea that SOMETHING CHANGED LAST MONTH and so we must immediately change our models (basically so that they would have done better last month) is pretty much the exactly wrong thing to do but I think people will be doing it to the overall detriment of the metamodel. I know they will – I’ve seen it a million times. It doesn’t work like that.

---

### Post #60 — **jefferythewind** | 2022-03-20 16:55 UTC _(reply to #47)_

this is regressions of data to targets on single eras, like you said.

---

### Post #61 — **wigglemuse** | 2022-03-20 16:59 UTC _(reply to #60)_

Ooh, I missed the 3d version before.

---

### Post #62 — **wigglemuse** | 2022-03-20 17:07 UTC

Ok, on the version that moves I can see that there are just isolated clusters that move along in time for a while but then just stop not connected to anything else. (If you just do the feature data, I think it will be one unbroken string more or less.)

And that’s another aspect of it – the kinds of models will get dumber because linear models will work better on recent->live until it suddenly doesn’t, but the coefficients will be so specific to the wrong regime that the crash will be worse. Even if you personally are not reckless in these ways, it won’t matter if the fund goes down and your NMR is now worthless. Don’t just think that because you are personally smarter that an overall dumbing down of the metamodel isn’t risky for you. (Or in the worse-case scenario, unlikely but not impossible – a catastrophic crash that causes investors to flee.) TC may make all of this moot by simply making it unprofitable to be too like everybody else or too linear (or at all linear).

---

### Post #63 — **jefferythewind** | 2022-03-20 19:13 UTC

Just wanted to mention here that we are more interested in understanding the structure of the data and not in submitting linear model predictions trained on recent data. If we want to do that we are free to try it in Signals. In fact I think some top models there have employed various versions of simple momentum/mean reversion etc. All based on recent data each week. What’s interesting to me is to think about how the least square solutions (the regression weights) define the structure of an era to a certain extent. Summarizing the relationships in thousands of stocks.

---

### Post #64 — **gammarat** | 2022-03-20 20:59 UTC _(reply to #55)_

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/numerai.discourse.group/wigglemuse/48/3094_2.png) wigglemuse:

> Bet on the raft to survive longer.

Hmmm, is this Numerai in a few years?  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/b/b07f2a561efd1815891781fa622a48cf7251fbed_2_690x471.jpeg)image1920×1311 400 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/b/b07f2a561efd1815891781fa622a48cf7251fbed.jpeg> "image")

(The Raft of the Medusa, Gericault, 1818-1819).  
![:laughing:](https://emoji.discourse-cdn.com/twitter/laughing.png?v=13)

---

### Post #65 — **wigglemuse** | 2022-03-20 21:04 UTC _(reply to #64)_

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/1/1d359bdcb66601195b6b5f68e8c58b3ed9d0f6cd.jpeg)image307×221 28.3 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/1/1d359bdcb66601195b6b5f68e8c58b3ed9d0f6cd.jpeg> "image")

me

---

### Post #66 — **jefferythewind** | 2022-03-20 21:21 UTC

Here is a trial with 10x data with synthetic targets.  


[![Screen Shot 2022-03-20 at 5.21.02 PM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/1/12fc5733b3a471c12e33e1c426c56d6f945e0ac6_2_690x110.png)Screen Shot 2022-03-20 at 5.21.02 PM2126×340 30.6 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/1/12fc5733b3a471c12e33e1c426c56d6f945e0ac6.png> "Screen Shot 2022-03-20 at 5.21.02 PM")

**Update**  
Here is a trial with 6x fake data, and for the “both” trial I combined that with 6 copies of the training data, this seemed to balance out the affect of the fake data when combining the predictions. Attaining a mean correlation of 6% on this cross validation trial.

[![Screen Shot 2022-03-21 at 9.00.33 AM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/5/5c0333258fb4a09cf41266ef17e97c440e1c69b3_2_690x113.png)Screen Shot 2022-03-21 at 9.00.33 AM2148×352 31.2 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/5/5c0333258fb4a09cf41266ef17e97c440e1c69b3.png> "Screen Shot 2022-03-21 at 9.00.33 AM")

---

### Post #67 — **mdo** | 2022-03-21 18:44 UTC _(reply to #66)_

Looking great. Would love to see some validation metrics on these too!

---

### Post #68 — **mdo** | 2022-03-21 18:47 UTC _(reply to #2)_

Might also want to check out <https://pymde.org/>  
PyMDE is based on a simple but general framework for embedding, called _Minimum-Distortion Embedding_ (MDE). The MDE framework generalizes well-known methods like PCA, spectral embedding, multi-dimensional scaling, LargeVis, and UMAP. With PyMDE, it is easy to recreate well-known embeddings and to create new ones, tailored to your particular application.  
(From the guy behind cvxpylayers!)

---

### Post #69 — **mdo** | 2022-03-21 19:04 UTC _(reply to #40)_

Would be cool to make a generative model of these filaments and then use it to sample fake filaments in the embedding space. Then you could reverse the embedding transform to get the corresponding weights which could be used to make fake targets. This fake data might be more realistic than the GMM samples.

---

### Post #70 — **jefferythewind** | 2022-03-21 19:13 UTC _(reply to #67)_

Yes I just did a trial using 2x the fake targets with 1x real data on the entire large data set. Using 6x to 10x data wasn’t feasible in my setup with the entire data set. The cross validation was downsampling to every fifth row of data. The validation metrics look worse than the baseline model with only real data, unfortunately. It isn’t the first time I’ve seen something improve cross validation correlation without improving validation performance.

**Just Real Data - Baseline**

[![Screen Shot 2022-03-21 at 3.11.29 PM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/e/e19729de4cb1ad28ec7e6b9b6d6d6ca2e436bf55_2_690x489.png)Screen Shot 2022-03-21 at 3.11.29 PM1876×1332 214 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/e/e19729de4cb1ad28ec7e6b9b6d6d6ca2e436bf55.png> "Screen Shot 2022-03-21 at 3.11.29 PM")

** 2x Fake Targets with 1x Real Data **

[![Screen Shot 2022-03-21 at 3.12.08 PM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/c/c329e8daca8ca4aaa66d6c0f68c5d2c1ec32c0e2_2_690x495.png)Screen Shot 2022-03-21 at 3.12.08 PM1864×1338 217 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/c/c329e8daca8ca4aaa66d6c0f68c5d2c1ec32c0e2.png> "Screen Shot 2022-03-21 at 3.12.08 PM")

---

### Post #71 — **mdo** | 2022-03-21 22:06 UTC _(reply to #70)_

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/7/704201cef795890691fcc7e8bb25227cfd2524ce.jpeg)image576×433 59.9 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/7/704201cef795890691fcc7e8bb25227cfd2524ce.jpeg> "image")

---

### Post #72 — **of_s** | 2022-03-22 02:56 UTC _(reply to #57)_

This truism goes all the way back to RiskMetrics and the EWMA…  
<https://www.msci.com/documents/10199/d0905614-2771-46dc-b000-1a033146586a>

[![RM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/b/b9f2a42516c687bb045b7561c6b513e10c0c7bfa_2_566x500.png)RM970×856 174 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/b/b9f2a42516c687bb045b7561c6b513e10c0c7bfa.png> "RM")

---

### Post #73 — **wigglemuse** | 2022-03-22 04:06 UTC _(reply to #72)_

But we’re not actually talking about time-series data here. We can’t do time-series in the main tournament – not directly anyway. (And of course if you do Signals you can use all the most recent data because it is your data. But using the recent data as a necessary input is different from basing your model on the recent past.) With the data we’re given, we’re making models of the whole market as it were – predicting how we think markets are gonna go when the data _looks like this_. So that’s different. Obviously if you are picking the future of a specific stock you want to know what it has been doing lately, and general current info about the stock. And presumably we are getting that in each row of the data given – we don’t know quite what it means except that in some sense it represents the current state of the stock. So when we debate about whether we need the most recent data possible in the main tournament, we’re not talking about following along specific stocks and trending them out. (Again, presumably that data is more or less in the feature row given for that stock.) The debate is: Is the general example of recent era X as a market model better (as a market model) that less recent era Y simply because era X is more recent?

i.e. Do training eras become less useful for training the more they recede into the past simply because they’ve receded more into the past and they are teaching lessons that simply are no longer relevant (or less relatively relevant), and the most recent eras are therefore by definition the most useful / more relevant? And I think we all the know the basic answer – the most recent eras ARE more useful MOST OF THE TIME. And we can see it in that visualization – although we do see changes and ups and downs even in the connected strings (unclear what that means in practice for results). BUT, there are sudden gaps where what is happening now doesn’t seem connected at all to the recent past – those are the points where you are going to get burned from over-reliance on recent eras.

If you could have either have the last 1 year of data and that’s all, or 10 years of data but nothing from the last year, which would you choose? These are the kind of questions I’m muddling over here.

Nobody is saying don’t use recent data (at all) if you got it. But if somebody tells me they _MUST_ have the recent data, they are also telling me they are going to weight it heavily (or else why is it so important?). And I think that is inevitably going to lead to less well-rounded more superficial models exhibiting streaky success punctuated by fairly large sudden failures. And then what do you do in those transition periods where the market has obviously suddenly shifted and now your recent past data is not helping you at all and you don’t have any newer data yet that corresponds to the current regime? After such a failure, do you then fall back onto a more general well-rounded model you’ve been holding in reserve while waiting for a new trend to establish itself?

So the main question is – is it worth it? If the whole metamodel moves in the direction of recency being more and more heavily weighted – and when there is a decently long streak where a regime is holding steady and recency is winning it surely will move in that direction, of course it will --then it also follows that when that regime falls apart (which is often sudden), that the resulting drawdown is going to be bigger than it would have been otherwise. The drawdowns are what kill you. But maybe the previous gains will have been worth it? Maybe, but maybe not, especially since a lot of users will then be sitting on useless models (for a time) that are going to weight the now-not-so-instructive recent past and will either keep submitting bad predictions (for a time) or will have to switch to a fallback, or pull stakes, or something.

I’m well aware I’m probably overstating the dangers here to make my point, but these issues are actually real, and I have actually seen it a million times in various contexts where people are betting on things. It is a pretty reliable pattern, and it just seems like a recipe for metamodel volatility.

**tl;dr** I don’t trust trend following – it isn’t prediction, it is just following along until failure occurs.

---

### Post #74 — **aventurine** | 2022-03-22 05:15 UTC _(reply to #71)_

lol( 20 characters )

---

### Post #75 — **aventurine** | 2022-03-22 05:20 UTC _(reply to #74)_

Here is Richard when this is all over for everyone commenting on this post  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/7/73cc4401c0599f921773800fd8f8a82aaa46e1a6.jpeg)image486×486 69.4 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/7/73cc4401c0599f921773800fd8f8a82aaa46e1a6.jpeg> "image")

---

### Post #76 — **of_s** | 2022-03-22 11:55 UTC _(reply to #73)_

Trend following, as well as mean reversion, inherently requires a prediction that the current regime will continue. The notion of position sizing is a further testament to your main concern, that trends end and nothing persists ad infinitum. None of this negates the importance of current market conditions represented via the most recent data.

Ironically, this was the rationale behind my vocal Signals suggestion of maintaining both the 6d and 20d targets, and is quasi addressed with the multiple classic targets now.

![](http://forum.numer.ai/user_avatar/forum.numer.ai/wigglemuse/48/3094_2.png) wigglemuse:

> I don’t trust trend following – it isn’t prediction, it is just following along until failure occurs.

---

### Post #77 — **nyuton** | 2022-03-22 12:59 UTC

Hi [@richai](</u/richai>)

Google’s [DeepDream](<https://en.wikipedia.org/wiki/DeepDream>) inspired me to try to “dream” new rows for the dataset.

The idea behide DeepDream is to create a “dream” image that maximizes output of certain layers by gradually modifiying the original image. This is gradient ascent insted of decent.  
The resulting image is similar to the original, but maximizes certain activations in the network.

Can we use a similar method to create a “dream” version of the original dataset that actually increases perfomance? I’ve just did that!

My prodecure was the following:

  1. Train a wide-and-deep NN with the dataset
  2. Select an appropriate layer to maximize activations for
  3. Calculate an input vector (row) that maximizes activation of a selected layer by iteratively adding the gradient to the input
  4. Repeat for all rows in the training set.



I used a scaled down version of the dataset (“medium” featureset) for this proof-of-concept.

Results are the following:

XGB baseline:

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/0/01a2e197265cd0549950766639a22711be5d9775_2_690x164.png)image714×170 23.1 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/0/01a2e197265cd0549950766639a22711be5d9775.png> "image")

XGB model with extended dataset (10% increase of row count):

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/c/c99dc84a2d0521b41a163fb9e6f142ae383768ac_2_690x173.png)image708×178 22.7 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/c/c99dc84a2d0521b41a163fb9e6f142ae383768ac.png> "image")

Now, there is clearly more research to be done with this idea!  
The extended dataset improves all metrics by a small margin. Hope that using the full dataset will do better. Also increasing the dataset size by 10% helps, but adding more doesn’t improve results any further.

Still I find the results for a quick proof-of-concept promising.

---

### Post #78 — **mdo** | 2022-03-22 17:05 UTC _(reply to #77)_

Very cool! I’m curious if you tried different layers to maximize activations for and what effect they had. Lots of possible extensions there too, i.e. maximizing activations for individual hidden units or subsets of hidden units, etc. Also was the 10% of rows that you created alternate versions of randomly selected? Also were imagined rows rebinned or just kept as is after the “dream”?

---

### Post #79 — **nyuton** | 2022-03-22 18:08 UTC _(reply to #78)_

I experimented with different NN architechtures and layer selections. Some layers improve results to various degree, some don’t. There is still a lot to be tried, including individual units. The method basically generates new rows similar to the source row, where similarity is defined by the learnt parameters of the NN.

I created a “dream” version of the whole training set and randomly sampled 10% of it. This selection is then concatenated to the training set. I trained a XGBoost model on both datasets (with and without dream rows) to compare results.  
I didn’t rebin the “dream” rows. They are used as is. I only cut them down to the [0-1] range to keep the same scale.

These are still a very early results. Just started working on it yesterday, but it looks promising and I can’t keep my mouth shut ![:smiley:](http://forum.numer.ai/images/emoji/twitter/smiley.png?v=10) I need to implement a good cross validation to validate results. But it’s easier said then done, with this pipeline. I only used the standard validation dataset for now.

---

### Post #81 — **nyuton** | 2022-03-24 09:21 UTC

Hi,

some update on deaming. I opensourced my solutions. You can find it here:

![](https://github.githubassets.com/favicons/favicon.svg) [github.com](<https://github.com/nemethpeti/numerai/tree/main/DeepDream>)

### [numerai/DeepDream at main · nemethpeti/numerai](<https://github.com/nemethpeti/numerai/tree/main/DeepDream>)

Contribute to nemethpeti/numerai development by creating an account on GitHub.

With some experimentation I managed to achive somewhat better results:

  * XGB baseline (some parameters are updated, thus the different baseline now)



[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/8/84205c881307201be8dffe5988628ee0cc723c8a_2_690x166.png)image707×171 22.1 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/8/84205c881307201be8dffe5988628ee0cc723c8a.png> "image")

  * XGB model on the extended dataset



[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/4/4efd089b47151a1a9f3f4e685926d3c9ac51ef30_2_690x161.png)image713×167 22.5 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/4/4efd089b47151a1a9f3f4e685926d3c9ac51ef30.png> "image")

You can generate these files by running my example script.

It’s worth noting tough that this is just a more sophisticated way to add noise to the dataset, which is better(?) than gaussian noise. It helps with regularization, but unlike the previous solution I posted here, it doesn’t add any new information that helps the model learn.

It would be interesting to also experiment with other NNs. Anyone willing to contribute with a well trained keras model? Let me know!

---

### Post #82 — **jefferythewind** | 2022-03-24 19:01 UTC _(reply to #81)_

I like that boost in sharpe, from my experience it seems easier to generalize an increase in sharpe than just corr. Also impressive if this increase is from just 10% more data. I will see if I can contribute something to your work. Recently I’ve been struggling trying to train pytorch models. For some reason it seems my NNs perform especially bad on the validation set.

---

### Post #83 — **mdo** | 2022-03-24 19:02 UTC _(reply to #81)_

This is great [@nyuton](</u/nyuton>)! I actually think this method might be closer to true data augmentation (somewhat akin to using randomly rotated, color shifted, and zoomed versions of images for training an image classifier) than adding noise. The line between the two ideas isn’t super clear, but lots of recent progress on various benchmarks has been due to better data augmentation strategies, so I find your line of work here rather compelling.

---

### Post #84 — **mdo** | 2022-03-24 19:08 UTC _(reply to #82)_

Getting NNs to perform nearly as well as a GBM model is extremely challenging. NNs are super finicky and love to overfit in these low SNR, small data size regimes.

---

### Post #85 — **jefferythewind** | 2022-03-24 22:38 UTC _(reply to #84)_

I agree, and when I try techniques to keep them from over-fitting I find i hard to make progress during training, but I think that is to be expected.

---

### Post #86 — **richai** | 2022-03-25 15:40 UTC _(reply to #81)_

I really like how much activity we have on this topic. [@nyuton](</u/nyuton>) are you coming to NumerCon on April? We would love to help you make it.

For anyone else who has contributed here and wants to come, we or the CoE can help you get there.

Lots of Kaggle grandmasters will be there too: [NUMERCON • Numerai Conference 2022 • Tickets, Fri, Apr 1, 2022 at 1:00 PM | Eventbrite](<https://www.eventbrite.com/e/numercon-numerai-conference-2022-tickets-166200162159>)

---

### Post #87 — **jefferythewind** | 2022-03-25 16:22 UTC _(reply to #69)_

Yeah i’ve been working on this idea. Unfortunately it doesn’t seem possible to do an inverse projection in tSNE, however with UMAP, yes. So I’ve been working on this idea.

---

### Post #89 — **nyuton** | 2022-03-26 14:59 UTC

One other method for data augmentation is to train an NN with two objectives:

  * preserve information that predicts labels
  * output new rows that minimizes distance to the source row based on the preserved information.



I drew inspiration from the [Unet](<https://en.wikipedia.org/wiki/U-Net>) architectre that is used for image segmentation tasks. The result is a two-headed NN.

  * It has one output in the middle to predict target labels from the narrow hidden layer. It forces the first part of the NN to learn parameters that can predict the label.
  * Then there are upscaling layers which get information from the first layers as well. The second output layer has the same dimension as the input to create new augmented(?) rows.



Model architecture:
    
    
    def getModel():
        
        input_layer = tf.keras.layers.Input(shape=(n_features,))
    
        x = tf.keras.layers.Dense(420, activation='relu')(input_layer)
        x = tf.keras.layers.BatchNormalization()(x)
        x = tf.keras.layers.Dropout(0.1)(x)
    
        x = tf.keras.layers.Dense(128, activation='relu')(x)
        x = tf.keras.layers.BatchNormalization()(x)    
        x0 = tf.keras.layers.Dropout(0.1)(x)
    
        o = tf.keras.layers.Dense(16, activation='relu')(x0)
        o = tf.keras.layers.BatchNormalization()(o)
        o = tf.keras.layers.Dropout(0.1)(o)
    
        # first head output
        label_output = tf.keras.layers.Dense(1, activation='sigmoid', name='label_output')(o)
    
        # decoder layers
        x = tf.keras.layers.Dense(128, activation='relu')(o)
        x = tf.keras.layers.BatchNormalization()(x)    
        x = tf.keras.layers.Dropout(0.1)(x)
        
        x = tf.keras.layers.concatenate([x, x0], name='concat')
    
        decoder_output = tf.keras.layers.Dense(420, activation='sigmoid', name='decoder_output')(x)
         
    
        model = tf.keras.Model(input_layer, [label_output, decoder_output])
        model.compile(optimizer=tf.optimizers.Adam(0.001), loss='mse', loss_weights=[1, 3])
        
        return model
    

Results are similar to the previously detailed “dream” approach.  
While the improvements are not too big, these methods show that it is possible to generate augmented rows, contrary to many discussions in rocket chat. Also my scripts are in a proof-of-concept stage, with a lot of room for improvement.

  * Baseline



[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/9/90f2cb3ab63110f784704320d67146aca6440598_2_690x167.png)image710×172 22.2 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/9/90f2cb3ab63110f784704320d67146aca6440598.png> "image")

  * Augmented with +5% data



[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/8/8e1165762e083d07c48d739ceeb723a54343554b_2_690x165.png)image704×169 22.7 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/8/8e1165762e083d07c48d739ceeb723a54343554b.png> "image")

---

### Post #90 — **olivepossum** | 2022-03-26 19:19 UTC _(reply to #89)_

[@nyuton](</u/nyuton>) This method reminded me a bit to this one [AutoEncoder and multitask MLP on new dataset (from Kaggle Jane Street)](<http://forum.numer.ai/t/autoencoder-and-multitask-mlp-on-new-dataset-from-kaggle-jane-street/4338>)

---

### Post #91 — **aventurine** | 2022-03-26 20:12 UTC

Has anyone ever worked with the Synthetic Data Vault(SDV) before or thought about using these libraries in this application?  
The * [CTGAN Model](<https://sdv.dev/SDV/user_guides/single_table/ctgan.html#ctgan>) is a GAN-based Deep Learning data synthesizer that can generate synthetic tabular data with high fidelity according to the site  
They also have the `PAR` model which is an implementation of a Probabilistic AutoRegressive model that allows learning **multi-type, multivariate timeseries data** and later on generate new synthetic data that has the same format and properties as the learned one.

Something like this below will create a data frame around just era1 for example with only the feature columns seleted and create synthetic data of all features of just era1. Im sure you could do it to multiple selected eras and also selecting out individual whole features
    
    
    import pandas as pd
    import gc
    
    from numerapi import NumerAPI
    from halo import Halo
    
    
    napi = NumerAPI()
    spinner = Halo(text='', spinner='dots')
    current_round = napi.get_current_round(tournament=8)  # tournament 8 is the primary Numerai Tournament
    download_data(napi, 'numerai_training_data.parquet', 'numerai_training_data.parquet', round=current_round)
    spinner.start('Reading parquet data')
    training_data = pd.read_parquet('numerai_training_data.parquet')
    spinner.succeed()
    
    training_data.head()
    
    
    features = [c for c in training_data if c.startswith("feature")]
    print(len(features))
    
    era1 = training_data.loc[training_data['era'] == '0001']
    
    era1.head()
    
    
    era1_feature_columns = era1.loc[:, era1.columns.str.startswith("feature")]
    
    era1_feature_columns.head()
    
    
    
    from ctgan import CTGANSynthesizer
    
    ctgan = CTGANSynthesizer(verbose=True)
    ctgan.fit(era1_feature_columns, features, epochs=10)
    
    ctgan_synthetic_data = ctgan.sample(2070)
    ctgan_synthetic_data.head()
    

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/6/6b68378a7f11bd0d44a4b1d50ebd41611aa359d5.png)image696×373 8.84 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/6/6b68378a7f11bd0d44a4b1d50ebd41611aa359d5.png> "image")

  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/f/f50dbf98217cd6ea1d2ba8927f0324225a6e4f81.png)image551×232 4.06 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/f/f50dbf98217cd6ea1d2ba8927f0324225a6e4f81.png> "image")

---

### Post #92 — **aventurine** | 2022-03-26 20:15 UTC _(reply to #91)_

Also wanted to add that I think [NumerFrame | numerblox](<https://crowdcent.github.io/numerblox/numerframe.html>) can be very helpful in this project for cutting DFs up

---

### Post #93 — **jefferythewind** | 2022-03-27 00:01 UTC

I guess we’ll keep the flow going here. I tried generating entirely new rows of data, including all 20 target columns through a completely unsupervised method based on UMAP. It is different from what [@nyuton](</u/nyuton>) described above, however interestingly results look similar: super low correlation with metamodel and also some positive corr… the result may be some decent TC.

The idea is to take all the features and targets and embedded them into a low-dimensional space with UMAP. So the input here is 1070 dimensions, outputting to 2 dimensions. We then sample uniformly from the embedded space and leverage the inverse transform to then create entire synthetic rows of data.

The technique is exactly what was described in this tutorial [Inverse transforms — umap 0.5.8 documentation](<https://umap-learn.readthedocs.io/en/latest/inverse_transform.html>) Here is a shot showing how one can generate synthetic MNIST data.

[![Screen Shot 2022-03-26 at 7.52.47 PM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/3/35802fb5171da4a9cb7b3b858be4894a02f566e6_2_690x352.jpeg)Screen Shot 2022-03-26 at 7.52.47 PM1434×732 100 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/3/35802fb5171da4a9cb7b3b858be4894a02f566e6.jpeg> "Screen Shot 2022-03-26 at 7.52.47 PM")

The embedded geometry of the numerai data isn’t much to look at, could be tuned more.

[![Screen Shot 2022-03-26 at 7.51.53 PM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/3/3322c855c1af65d56dc8ba11aeb7b4b9673aa791_2_517x350.png)Screen Shot 2022-03-26 at 7.51.53 PM972×658 288 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/3/3322c855c1af65d56dc8ba11aeb7b4b9673aa791.png> "Screen Shot 2022-03-26 at 7.51.53 PM")

Training on only on the generated 10,000 rows give the following looking validation stats.

[![Screen Shot 2022-03-26 at 7.56.13 PM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/e/eebf31c5c69519e45e63b23cc1b3cd6c1008d7e5_2_517x366.png)Screen Shot 2022-03-26 at 7.56.13 PM1840×1302 236 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/e/eebf31c5c69519e45e63b23cc1b3cd6c1008d7e5.png> "Screen Shot 2022-03-26 at 7.56.13 PM")

[![Screen Shot 2022-03-26 at 7.56.32 PM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/5/550ce3a0fc06f87be14f541c8ee1c8e722a39ff0_2_517x364.png)Screen Shot 2022-03-26 at 7.56.32 PM1846×1302 239 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/5/550ce3a0fc06f87be14f541c8ee1c8e722a39ff0.png> "Screen Shot 2022-03-26 at 7.56.32 PM")

It takes a while to generate the rows. I was hoping to see Rapids AI supply an inverse-transform function, since that is real fast for computing UMAP in the forward direction, however it does not have this function. Interesting to see how similar the stats look to the technique based on embedding the input data and using that low dimensional data to train the model, maybe not so surprising.

---

### Post #94 — **jefferythewind** | 2022-03-27 00:17 UTC

Less is more.

We’re talking data augmentation. Instead of adding more features, why not take them away? Maybe it is something people have tried before. I tested removing 1 feature at a time individually from the data set (for all 1050 features) and running a full cross validation on the training set. This way we could see if removing a feature increases performance across the board. While it isn’t so sophisticated, it seems to work. Here was have results, showing Sharpe and Corr increases when removing many of the features on CV of the training set.  


[![Screen Shot 2022-03-26 at 8.12.17 PM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/6/6a4f702278f8d643521f4d50c0a357ee50a7cc89_2_690x148.png)Screen Shot 2022-03-26 at 8.12.17 PM2538×548 129 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/6/6a4f702278f8d643521f4d50c0a357ee50a7cc89.png> "Screen Shot 2022-03-26 at 8.12.17 PM")

Compare to the original  
![Screen Shot 2022-03-26 at 8.12.52 PM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/b/bbdae9f3b2661a04032cd2066bc242ec87876b09_2_690x25.png)

and I was able to then verify this improvement carries over to the validation set even just removing 1 feature. Here is the baseline training, following by a trial where I removed the top 5 features on the list. I find it pretty compelling.

[![Screen Shot 2022-03-26 at 8.15.44 PM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/2/2865f8ed13d027c5cfd9a833ac37bd76e429148b_2_690x488.png)Screen Shot 2022-03-26 at 8.15.44 PM1836×1300 220 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/2/2865f8ed13d027c5cfd9a833ac37bd76e429148b.png> "Screen Shot 2022-03-26 at 8.15.44 PM")

[![Screen Shot 2022-03-26 at 8.16.06 PM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/a/a67594472f6d71a775519516df23332980ed9140_2_690x486.png)Screen Shot 2022-03-26 at 8.16.06 PM1874×1320 220 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/a/a67594472f6d71a775519516df23332980ed9140.png> "Screen Shot 2022-03-26 at 8.16.06 PM")

---

### Post #95 — **nyuton** | 2022-03-28 07:54 UTC _(reply to #86)_

Yes, I’m coming! See you there [@richai](</u/richai>)

---

### Post #96 — **danzell** | 2022-03-30 15:15 UTC

Better late than never!

My models are all based on representation learning techniques.

I won the TPS January Challenge on Kaggle by using **D** enoising**A** uto**E** ncoders (DAEs) + representation learning.  
[Here is a short summary](<https://www.kaggle.com/code/springmanndaniel/1st-place-turn-your-data-into-daeta>)

All my numerai models use different 1st level autoencoder architectures like (deepstack, bottleneck, transformer based AE) as well as different noise effects to learn as much information of the dataset as possible. The learned weights of the DAE are then used for the final training.

Here are a few examples:  
[example model 1](<https://numer.ai/danzell_model3>)  
[example model 2](<https://numer.ai/danzell_linear>)  
[example model 3](<https://numer.ai/danzell_delta>)

Cheers,  
danzell

Edit: links

---

### Post #97 — **bieber_fever** | 2022-03-30 17:26 UTC

Has anyone tested [Sharpened Cosine Similarity](<https://e2eml.school/scs.html>)?

---

### Post #98 — **slowmoe** | 2022-04-12 11:40 UTC

I am quite fascinated by the idea of creating an alternate version of history in this context. My insights so far:  
It is useful to look at the covariance matrices per era. There is a sense in which they are continuous in time, as [@jefferythewind](</u/jefferythewind>) showed with tSNE. I used a UMAP embedding, but it gives the same kind of picture. I then picked a random point in the trajectory in the embedded space and went off along a new path. Visually it looks like this:  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/e/ed46bb9184133dc810cc4e497f18852cea9d1fc4_2_690x486.png)image715×504 78.9 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/e/ed46bb9184133dc810cc4e497f18852cea9d1fc4.png> "image")

  
Some remarks on this:

  * this is v3 data
  * the covariance matrix includes the target, so you can sample labeled data
  * there is a gap in the trajectory of trainig eras around era 100. My bet is that there is a time jump here
  * the trajectory seems to be some kind of random walk with inertia, so thats what I used as model to make a new one.
  * I like colors



Now, thanks to `inverse_transform` you can get new covariance matrices of completely synthetic eras for each point along the new trajectory. You can use those to get new labeled samples. So for the picture above, this gives you 200 new eras.

Below a summary sorted by sharpe, comparing LGBM models on data as-is (vanilla) and new data (synthetic), plus neutralized versions  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/2/228fa25aa259c52ded6068a26551e851f38272c0_2_690x88.png)image1575×202 171 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/2/228fa25aa259c52ded6068a26551e851f38272c0.png> "image")

TBH, it absolutely blows my mind that training on these samples has any predictive power at all. Like, you can just make stuff up that isn’t real and use that to make better decisions in real life?  
I experimented with other means of cooking up new covariance matrices, some of which seem even more promising. Super curious about live performance.

---

### Post #99 — **mdo** | 2022-04-14 15:46 UTC _(reply to #98)_

Very cool [@slowmoe](</u/slowmoe>), that’s exactly the sort of thing I was imagining. A few things I would try are:

  1. just use upper (or lower) triangular of covariance matrix if you aren’t already to reduce dimension and prevent double counting off diagonal
  2. include the additional targets in the covariance matrix so the embedding space includes more feature to target information
  3. use a higher than 2 dimensional embedding space (and then a path in that space) to retain more information
  4. use v4 data and then validate on the much longer test set you now have targets for



And there isn’t a time jump around era 100, could just be a major regime change. Interested to see if it breaks in the same place in higher dimensions.

---

### Post #100 — **wigglemuse** | 2022-04-14 16:01 UTC

Although non-intuitive when you come at it from a “this is random data I just made up” angle, it does make perfect sense that it has predictive power. The covariance matrix itself _is_ a model of the data, and so therefore is the fake data created from that model. And then you train a new model from that fake data and predict stuff – it is natural that it would retain a fair amount of predictive power even if somewhat watered down. But…is it going to be valuable alpha? Probably not – it seems to be more of a regularizer which I think is true of most of these types of methods. They are pure stats if that makes any sense. (Denoisers, essentially.) I immediately become interested in the stuff that is lost – is it just noise or is that where the real gold is? (Gold that will take more than summary stats to uncover.) I’d like to try using the covariance matrix approach as a neutralizer and then train on what’s left over and see if that holds anything interesting.

---

### Post #101 — **slowmoe** | 2022-04-15 20:58 UTC

happy to hear that the great [@mdo](</u/mdo>) identified the same next steps as I did ![:smiley:](http://forum.numer.ai/images/emoji/twitter/smiley.png?v=10)

On 2) I can already say that it helps (unsurprisingly) a good deal. 3) and 4) are on hold for now because I am running on a Dell laptop over Easter holidays… I hope to post an update on those once I have something.

Just as [@wigglemuse](</u/wigglemuse>) hinted to, I’ve come around to viewing this as a regularization technique. However, one observation makes me believe there is more to it: This particular model (covariance matrix) is in a sense evolving continuously in time. This suggests that if you know the recent past, you can rule out most of the space of possible states of the near future. That seems like a big deal to me.

---

### Post #102 — **olivepossum** | 2022-04-16 13:05 UTC _(reply to #2)_

Would it make sense to apply UMAP per era?

---

### Post #103 — **richai** | 2022-04-19 00:58 UTC _(reply to #96)_

Thank you! – and some nice TC on those models.

---

### Post #104 — **jefferythewind** | 2022-04-19 17:06 UTC _(reply to #98)_

[@slowmoe](</u/slowmoe>), very cool! That was a cool idea to use the covariance matrix as a representation of the era dynamics. It seems you haven’t completely described the data generation procedure, once you have the new covariance matrix for a new era? Or I haven’t picked it up. I had envisioned this idea with the regression coefficients but I couldn’t get the UMAP picture to look like a string. What kind of params did you use?

---

### Post #105 — **slowmoe** | 2022-04-24 22:15 UTC

Ok, some progress that warrants an update:

Re the cov-embedding:

  * Higher dimensions do not help at all.
  * inverse transforms do not generally yield valid (i.e. positive semi-definite) covariance matrices. This basically means you want to be really careful about the maths of any of this.



Re the “cov as a model or regularizer of a model” topic:  
Note that covariance itself does not tell you anything about the shape of the distribution. However, when sampling the cov matrix, you have to know the shape of the distribution you want your samples to be in. In numerai data, feature distribution is uniform, but targets seem normal.  
To answer [@jefferythewind](</u/jefferythewind>): you can use numpy.random.multivariate_normal() to make normally distributed samples with your cov matrix. You may write your own function to get different distributions. Also to your point: there seems to be something very peculiar to cov matrices. I tried embedding only its singular values or SVD decomposition, and others. None form any structure either. With covs, however, I could not find any parameters that do not yield a smooth string, even in higher dimensions.

On V4, I could not get anything that outperforms the vanilla data yet (something something signal decay on longer valid period?), but you still get significant decorrelation to the example predictions.

---

### Post #106 — **qstar** | 2022-05-04 04:01 UTC

Is this considered solved/closed? I started working on this recently and wanna know if it’s still worth working on or not

---

### Post #107 — **mdo** | 2022-05-15 18:26 UTC _(reply to #106)_

This is very much an open area of research!

---

### Post #108 — **nyuton** | 2022-12-20 07:50 UTC _(reply to #77)_

Haha, I was surprised to find my forum post in the investor presentation yesterday [@richai](</u/richai>) ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=12)  
For the record: I never managed to bring the deepdream idea to a statisfactory level. But I found another NN architecture that produces good augmented rows and have produced good results in the past months.

---

### Post #109 — **jacob_stahl** | 2022-12-21 03:50 UTC _(reply to #108)_

would that be a diffusion model?

---

### Post #110 — **liz** | 2022-12-25 22:15 UTC

haven’t read the entire thread but wanted to throw out the idea that when I was last active in the main tournament I did a pretty brainless data augmentation approach. I don’t remember exactly but I think I took 1000 random pairs of features (modifying the values so no 0’s to throw the logs) and made new features by taking one log the base of the other, and doing some sensible transformations after and then fit that data (joined with the original data). my model Urza did pretty well, not elite I think, but my point is fairly random and brainless data augmentation seemed to squeeze some extra juice out of the data available at the time (pre big data expansion), no academic exploration exerted.

---

### Post #111 — **qstar** | 2023-01-20 03:13 UTC

How long should the track record be for a model trained only on synth data?

---

### Post #112 — **svendaj** | 2023-01-21 17:30 UTC _(reply to #2)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/nyuton/48/687_2.png) nyuton:

> Unlike PCA, Umap works with the Numerai dataset.

![](http://forum.numer.ai/user_avatar/forum.numer.ai/richai/48/2493_2.png) richai:

> I don’t think PCA works especially well

Is there any analysis or examples of why PCA is not good for Numerai? Especially when Factor Analysis seems to work well for [@katsu1110](</u/katsu1110>) [[numerai] factor analysis | Kaggle](<https://www.kaggle.com/code/code1110/numerai-factor-analysis/notebook>)

---

### Post #113 — **olivepossum** | 2023-01-22 20:28 UTC _(reply to #112)_

If I recall, I think it’s related to PCA working on linear relationships and just linear stuff doesn’t perform very well on this dataset (but who knows if there is people out there having more success with it).

---

### Post #114 — **wigglemuse** | 2023-01-22 20:56 UTC _(reply to #113)_

If you are just targeting TC, throw all such advice out the window. But with CORR, yeah have had a hard time with pretty much any wholesale data transformations. (Augmentation working better than replacement.)

---

### Post #115 — **qstar** | 2023-02-14 22:58 UTC

If anyone is interested I developed a data generation process akin to the the tournaments data. **This model sees no real data**. Very little meta model corr and decent corr, and very promising seeming TC. See the [model starq_synth2 model here](<http://numer.ai/starq_synth2>) also [starq_synth here](<http://numer.ai/starq_synth>) (starq_synth seems to be more volatile, this model is only trained on some super old training data from a while ago)

---

### Post #116 — **kayeffnumeraitor** | 2023-02-15 09:40 UTC _(reply to #115)_

I don’t want to downplay your work as it could still be a very good model, but in my experience it takes way longer than one resolved era to fully assess the capabilities of a model. After a few months of resolved eras the picture will be more clear.

---

### Post #117 — **qstar** | 2023-02-15 14:56 UTC _(reply to #116)_

totally agree, although tbf I asked above how many rounds and no one said anything ![:laughing:](http://forum.numer.ai/images/emoji/twitter/laughing.png?v=12)

---

### Post #118 — **andralienware** | 2023-03-20 14:06 UTC _(reply to #105)_

Rather than embedding singular values of the cov matrix, it may worth trying to embed the square roots of the cov matrix since even if the square root is not symmetric, the sampled “square roots of cov matrices” times the transpose of such sampled matrices should still be symmetric. On the other hand if you were trying to use something like a DAE rather than just umap for embeddings, you could create some sort of “asymmetry error” to do unsupervised encoding or decoding training and then fine tune on some held-out real data.

---

### Post #119 — **qstar** | 2023-03-22 14:27 UTC _(reply to #115)_

[starq_synth](<https://numer.ai/starq_synth/submissions>) is trained on synthetic data, scored against some super old v4 data and randomly gets 99th percentiles. p interesting
