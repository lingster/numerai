---
title: "Era Splitting - Invariant Learning for Gradient Boosted Decision Trees"
category: Data Science
url: https://forum.numer.ai/t/era-splitting-invariant-learning-for-gradient-boosted-decision-trees/6690
created_at: 2023-09-27T15:12:31.883000+00:00
last_posted_at: 2023-10-03T10:16:29.473000+00:00
posts_count: 6
views: 1792
tags: []
---

# Era Splitting - Invariant Learning for Gradient Boosted Decision Trees

---

### Post #1 — **jefferythewind** | 2023-09-27 15:12 UTC

**Era Splitting** paper and code are now open source and available online.

Paper: [[2309.14496] Era Splitting: Invariant Learning for Decision Trees](<https://arxiv.org/abs/2309.14496>)  
Implementation: [GitHub - jefferythewind/scikit-learn-erasplit](<https://github.com/jefferythewind/scikit-learn-erasplit>)  
Notebooks: [GitHub - jefferythewind/era-splitting-notebook-examples: Example Notebooks to Replicate Experiments from Era Splitting Paper](<https://github.com/jefferythewind/era-splitting-notebook-examples>)

Quant Club: <https://www.youtube.com/watch?v=HOmHxuRQy18>

This project was a deep dive into the inner workings of one of our favorite ML algorithms: gradient boosted decision trees, but is applicable to decision tree-based models in general. In this new algorithm, which you can install via the second link above, we incorporate the _era-wise_ information into two new splitting criteria: _**era splitting**_ and _**directional era splitting**_. Details are outlined in the paper and also the youtube feature from the Quant Club.

Since the Quant Club presentation, I’ve developed more the directional era splitting criterion, and I’ve applied the algorithm to another synthetic data set that is designed to test this kind of algorithm. It is called the synthetic memorization data set from the paper: [* Learning explanations that are hard to vary*, by Parascandolo et. al.](<https://arxiv.org/abs/2009.00329>). This data set is designed to confound and befuddle naive ML models. A complex invariant swirl signal is embedded in the data along with simple spurious signals that shift from one era to another. In the test set the swirl remains but the spurious signals disappear completely. Naive models learn the spurious signals, and at test time performance is poor since they did not learn the invariant signal. Indeed this is what happens with common gradient boosted decision tree models. However with directional era splitting, we are able to perform almost perfectly on the test set, meaning our model has ignored the spurious signals and learnt the invariant swirl signal. Era splitting also performs better than the naive model. Here is an excerpt figure from the paper.

[![Screen Shot 2023-09-27 at 10.52.56 AM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/6/6eea615dfd9f419b69e0d9375c8fe8695e1b39ad_2_690x477.jpeg)Screen Shot 2023-09-27 at 10.52.56 AM1724×1192 233 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/6/6eea615dfd9f419b69e0d9375c8fe8695e1b39ad.jpeg> "Screen Shot 2023-09-27 at 10.52.56 AM")

This good result comes on top of meaningful results on another synthetic data set (the shifted sine wave), as well as good results discussed in the Quant Club video on the Numerai data set. However our goal with this project was really to improve considerably on the baseline LGBM model that is used commonly in the example notebooks. We wanted to really blow it out of the water. This goal proved hard to achieve. I believe the ideas are worthwhile. I hope some member of the community and help push forward this research.

**Time Complexity**

On major issue is that these new splitting techniques introduce increased time complexity on the order of the number of eras in the training data. We have to perform that many more operations per split to compute our desired criteria. Improving the algorithm to reduce this time complexity would make it much nicer to work with when you want to tackle big data sets like the Rain data with all the features and eras. For the Numerai result posted in the paper, it took a couple of days to train. However the toy examples in the notebooks are fast and easy to get started.

**Signals**

Why not try it out on your signals model? The era splitting helped mine out more than on the classic data. This also took less time to train since I use less features and a lower number of iterations.

**Era Groups**

Can we group eras together in a smart way to reduce the number of eras (computations) while improving the out of sample performance? This is an idea I played around with and seems to improve performance in certain cases. It seems like also a simple way to get speed up in run time.

**Feedback**

Please let me know with any bugs or feedback, I’ll do my best to support the project.

Happy Coding ![:slight_smile:](https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=13)

---

### Post #2 — **perfect_fit** | 2023-09-28 18:22 UTC

Amazing! Thank you for sharing the concept in such detail! Especially the scikit-learn implementation! ![:star_struck:](http://forum.numer.ai/images/emoji/twitter/star_struck.png?v=12)

Have you already started discussing this implementation with the scikit-learn, LightGBM or XGBoost core developers? Would be great to have it integrated without needing the full scikit-learn fork.

---

### Post #3 — **jefferythewind** | 2023-09-29 15:00 UTC _(reply to #2)_

Yes I agree that would be great. I’m just updating the repository with more detailed installation instructions, and then I want to merge in the latest updates from scikit learn and make it compatible with the newest python versions. It would be awesome to get some attention from the LGBM team, I’m working on it.

---

### Post #4 — **perfect_fit** | 2023-10-02 16:28 UTC _(reply to #3)_

Do you have a lightweight version to install `EraHistGradientBoostingRegressor` (without having to install the full scikit-learn library with it)?

Would love to test how it integrates within scikit-learn `Pipeline`, `FeatureUnion`, `ColumnTransformer`, [NumerBlox 1.0](<http://forum.numer.ai/t/preview-numerblox-1-0/6696>) and other libraries compatible with scikit-learn. I know `HistGradientBoostingRegressor` works well in pipelines so the era version should also be fine, unless there are some issues because of needing to pass eras in the fit step.

We have a similar thing in [BayesianGMMTargetProcessor](<https://github.com/crowdcent/numerblox/blob/rewrite/numerbloxv1/docs/targets.md#bayesiangmmtargetprocessor>) where `.fit` requires an `eras` argument and got that to work with `sklearn.pipeline.Pipeline`.

---

### Post #5 — **jefferythewind** | 2023-10-02 19:24 UTC _(reply to #4)_

The forked version of sklearn is not that outdated at the moment. I would say give it a try with the versions of Pipeline that are available in the forked version. In the mean time I need to come up with a better solution. I guess I could try to strip it down to the bare essentials and it could be installed as a separate package, as you suggest.

And yes, the caveat with the model, is that `.fit` receives another argument besides just x and y, but also `eras` which is a vector the same length as x and y but holds the integer era id for each row of data.

**Edit**  
Just thinking about it, maybe just creating a different name space for this installation will allow you to install this along side the core Scikit-Learn. Like if you could

`import sklearn-erasplit`

---

### Post #6 — **perfect_fit** | 2023-10-03 10:16 UTC _(reply to #5)_

Nice! Yes the different namespace would suffice for tests. ![:+1:](http://forum.numer.ai/images/emoji/twitter/+1.png?v=12)
