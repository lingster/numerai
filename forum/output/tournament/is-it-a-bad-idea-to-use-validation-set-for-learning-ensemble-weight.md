---
title: "Is it a bad idea to use validation set for learning ensemble weight?"
category: Tournament
url: https://forum.numer.ai/t/is-it-a-bad-idea-to-use-validation-set-for-learning-ensemble-weight/4324
created_at: 2021-10-12T07:18:58.407000+00:00
last_posted_at: 2021-10-12T12:42:40.937000+00:00
posts_count: 2
views: 1278
tags: []
---

# Is it a bad idea to use validation set for learning ensemble weight?

---

### Post #1 — **maxchu** | 2021-10-12 07:18 UTC

First of all, i have trained a bunch of tree models. Then I tried to fit a linear model on those tree models without any constraints to maximize the Sharpe ratio. The optimization cannot converge but during the training process, the sharpe can be increased to a crazy high value (I stopped the optimization halfway around 100 iterations, the sharpe is already at around 8).  
After thinking a bit more, i think we at least need to put constraints on using positive weight only as it doesn’t make sense to have negative weight. Below are the result (i also include the ensemble of selection top 25 models based on sharpe):  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/3/341e6bf231cfd50a35714a90c6ad4db53c4f88b3.png)image1891×478 50.3 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/3/341e6bf231cfd50a35714a90c6ad4db53c4f88b3.png> "image")

---

### Post #2 — **degerhan** | 2021-10-12 12:42 UTC

[@maxchu](</u/maxchu>) the moment you use the validation set for anything (e.g. learning ensemble weights, early stopping on your training base learners, picking tree architecture, etc) it ceases to become an out-of-sample and the test results are not meaningful. If you want to utilize the validation data for live models, I would suggest:

  * first cut the training set into train-train, and train-validation
  * automate your training, optimization, architecture selection there
  * feed the validation set “once” to this pipeline, and if you like the results
  * rebuild the models with the same pipeline using the train and validation sets and deploy



I think the [MLDP book](<https://www.wiley.com/en-us/Advances+in+Financial+Machine+Learning-p-9781119482086>) had a section on quantifying how much each “look” at your out-of-sample test reduces the reliability of the test results.
