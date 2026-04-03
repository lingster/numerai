---
title: "Experiment Report: using V3 models to infer on V4 data"
category: Data Science
url: https://forum.numer.ai/t/experiment-report-using-v3-models-to-infer-on-v4-data/5413
created_at: 2022-05-18T10:05:02.843000+00:00
last_posted_at: 2022-05-25T04:49:18.440000+00:00
posts_count: 3
views: 923
tags: []
---

# Experiment Report: using V3 models to infer on V4 data

---

### Post #1 — **yxbot** | 2022-05-18 10:05 UTC

Hello Fam:

The publication of [V4 Tournament Data](<http://forum.numer.ai/t/v4-tournament-data-announcement/5163>) allows us a lot more eras to validate our model performance, however one of the challenges is the lack of an explicit 1-to-1 mapping between V2/V3 to V4 features - in that strictly speaking it wouldn’t make sense to use the additional V4 validation eras to check out our trained V3 models.

Thanks to [@mic](</u/mic>), we have an [unofficial mapping](<http://forum.numer.ai/t/mapping-of-feature-names-from-legacy-to-new/4661>), so I decided to go ahead to do a small experiment - this was inspired by one of our discussions over in [RC](<https://rocketchat.numer.ai/channel/support?msg=3T39pXoGNRgHThDv8>)

The main questions that I want to explore with this experiment:  
**Q1.** can we get decent results (i.e. not disastrous result) if we don’t use exact same features group during inference time  
**Q2.** provided that Q1 is positive, how do V3 models - trained with V3 training data and validated on 105 V3 validation eras, generalise to the much wider 433 V4 validation eras (including V3 all val. eras + 328 newly available val. eras)

IMO, the answer to Q1 would give us some new insights on how much this dataset would allow us to mess around with substituting columns and approximating stuff - for instance [using synthetic data] ([Numerai Self-Supervised Learning & Data Augmentation Projects](<http://forum.numer.ai/t/numerai-self-supervised-learning-data-augmentation-projects/5003>)) that approximate actual features and targets , meanwhile answer to Q2 would shed some new use cases for the much richer and ever expanding Q4 validation data.

The experiment steps are the following:

  1. take V3 data, and the [V3 to V4 feature mapping file](<https://github.com/miciasto/numerai/blob/main/v3_to_v4_feature_mapping.csv>)
  2. rename the v4 data columns to their v3 counterpart according to the feature mapping
  3. for a given V3 trained model, use it to perform inference on the renamed V4 data with V3 feature names
  4. check the correlation score on validation eras in following era groups: corr/sharpe for eras present in V3, corr/sharpe for eras only existing V4, overall corr/sharpe in V4, and if available corr/sharpe of live performance (rounds 286-314)



I run the above on 7 models, and the results are shown in the following tables  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/f/f2f2736522d692a5c110735c86737b22a96b11f2.png)image736×173 19.7 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/f/f2f2736522d692a5c110735c86737b22a96b11f2.png> "image")

As shown above, the main result groups are:

  * **v3 - v3 val eras:** validation result using V3 data on V3 validation Eras
  * **v4 - v3 val eras:** validation result using feature mapping, inferred with V4 data on V3 validation eras
  * **v4 - v4 only val eras:** validation result using feature mapping, inferred with V4 data on validation eras **NOT included** in v3 data
  * **v4 val eras overall:** validation result using feature mapping inferred on the full V4 validation set
  * **Live rounds perf. 286-314:** for deployed model only, live performance from rounds 286-314



Some “contextual factors” about the models featured in this study:

  * Models 1 and 3 used the same feature set, with model 3 using more well-tuned parameters (smaller learning rate, etc).
  * Model 1 basically used the most “loosed” parameters compare to any of models 2-6
  * Models 2-6 used subsets of the 1050 V3 features - with set sizes ranging from 200~400, each trained with different targets
  * Model 7 is an ensemble of models 2-6



Here are some of the observations that I can draw from the presented results:

  1. To answer Q1, seems we **can** get decent results as long as the features are well correlated to those the model trained with.
  2. the comparative performance with V3 eras and V4 only eras using v4 data are quite interesting - model 1 with the lowest corer and sharpe in V3 eras are doing much more competitively on V4 only eras, it also has the best live performance from rounds 286-314 - this is strong evidence that it generalises well compared to others
  3. I strongly suspect that model 6 is overfitting on V3 val eras - the drop in sharp v3 eras to v4 only eras is quite big - not sure if or how much feature mapping and use of alternative target had an impact on this - one way to find out is to retrain completely using V4 and repeat this experiment.
  4. The ensemble model 7 turns out to be the most stable which is as expected, it is nice to see that it generalised well in both the v4 only val. eras, and more importantly in live - it is the most stable model in this collection.



Some further interesting things that is worth doing building on this little exercise:

  1. take live V4 data, mapped to V3 features, and use V3 model to generate live submission - it might well add some nice diversity bonus, maybe even TC ![:slight_smile:](https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=13)
  2. use of comparative metric for model selection - with V2 data I used to select models by checking their corr/sharpe ratio between validation 1 and validation 2, I think the same approach could be useful here - to look for models that can generalise well in the ever-expanding v4 validation set.



Hope the above is interesting for you guys, please share any idea you have to build upon this ![:slight_smile:](https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=13)

---

### Post #2 — **mic** | 2022-05-21 13:21 UTC

Thanks for the report [@yxbot](</u/yxbot>).

As you know, the v4 features aren’t all exact copies of the v3 original features. For a few features, the correlation drops down towards 0.8 or even lower. If your model is putting more importance on those features, then there is more chance of a change in performance. Maybe you see that with model 6.

---

### Post #3 — **yxbot** | 2022-05-25 04:49 UTC _(reply to #2)_

good point, will make a note and revisit this ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=10)  
thanks for sharing the mappings, without these my little investigation wouldn’t be possible
