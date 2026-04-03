---
title: "Super Massive LGBM Grid Search"
category: Tournament
url: https://forum.numer.ai/t/super-massive-lgbm-grid-search/6463
created_at: 2023-06-15T13:48:33.858000+00:00
last_posted_at: 2023-07-06T09:28:52.932000+00:00
posts_count: 11
views: 3903
tags: []
---

# Super Massive LGBM Grid Search

---

### Post #1 — **maul** | 2023-06-15 13:48 UTC

# Introduction

We at Numerai have spent the last couple of weeks conducting a new grid search on the Sunshine V4.1 data set. We have built hundreds of models with different hyperparameters on the V4.1 dataset focussed on target_cyrus_v4_20 which we believe is the best single target at present for our hedge fund strategy.

We are sharing the best of these grid searched results in terms of correlation and correlation Sharpe to enable users to benefit from the grid search and either use these results directly in their models or allow them to do more targeted searches of their own around the sweet spots.

# Experimental Setup

We did the grid search using the following parameters:-

Features = all the features in the V4.1 dataset

Target = target_cyrus_v4_20

Algorithm = Scikit-learn API LGBMRegressor

Hyperparameter ranges for the better results are shared below:-

n_estimators = 30k - 60k

learning_rate = 0.001

max_depth = 5, 6, 7

num_leaves = 2**max_depth - 1

colsample_bytree = 0.1

# Results

The first plot below contains the correlation and the second the correlation Sharpe computed using the out of sample predictions from era 578 to 1059 inclusive. The training period was from era1 to era 574 inclusive.

**

[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/7/7701075d801ab6492986c72657e4a71e3afd5173_2_522x500.png)804×769 64.9 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/7/7701075d801ab6492986c72657e4a71e3afd5173.png>)

**

Table 1 below contains the 20 best correlation results.

Table1  
**

[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/f/fc6c8fb1de192da64ecee82aa10be10e7e51098f.png)611×424 6.09 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/f/fc6c8fb1de192da64ecee82aa10be10e7e51098f.png>)

**

Table 2 below contains the 20 best correlation Sharpe results.

Table 2  
**

[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/9/95a483fbdd394079f467f806999f9d78e87cb743.png)601×423 6.72 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/9/95a483fbdd394079f467f806999f9d78e87cb743.png>)

**

**The plot below shows the cumulative correlation of

  1. The sunshine recommended param model with learning_rate = 0.001, n_estimators = 20K and  
max_depth = 6.

  2. The best correlation model from the above table.

  3. The 2 best correlation Sharpe models from the above table.




**

[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/3/355455ad2e9c5e408dd4d6e9a9061d122e50e81f.png)565×428 31 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/3/355455ad2e9c5e408dd4d6e9a9061d122e50e81f.png>)

**

# Alternate hyperparameters for less compute

The above parameters require 6 hours to compute for a tree of max_depth = 6 , a learning rate of 0.001 and n_estimators = 100k on a 24 core processor. This may be a heavy compute burden for users.

We show below parameters that work with lower compute using a learning rate of 0.01, n_estimators = 20k and columnsample_bytree = 0.1. This reduces the compute time to less than 2 hours.

**

[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/e/e44d09ab251e00fd880f56b6b3cebbe33391afeb_2_545x500.png)830×761 78.4 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/e/e44d09ab251e00fd880f56b6b3cebbe33391afeb.png>)

**

# Conclusion

The above results are very competitive in correlation Sharpe space while slightly worse in terms of pure correlation but with significant compute saving.

---

### Post #2 — **thomasxthomas** | 2023-06-16 13:48 UTC

Is that possible to rerun the best hyper-parameters for 5 different random seeds and report the mean and standard deviation of Corr and Sharpe for each hyper-parameter?

---

### Post #3 — **lcrmorin** | 2023-06-17 12:11 UTC _(reply to #2)_

Came here to say that. Results are usually really sensitive to seed. Also I am pretty sure l1, l2 reg, boosting mode, allowing for regression on the last level can change the results.

---

### Post #4 — **dzheng1887** | 2023-06-18 19:51 UTC

Has anyone tried using a log loss cost function instead of a regression? That’ll just be reducing the log loss on that where actuals are 0, 0.25, 0.5, 0.75, and 1 instead of just 0/1. Wondering if probability conversion helps with fitting due to the curvature in the cost function.

It also has other interesting properties like 0.5 guess on any observation is the same cost regardless of the true label, kind of “standardizing” 0.5 as an acceptable placeholder guess.

Also, the comparative improvement of going from the worst prediction to okay compared to going from okay to perfect is higher using the log loss cost function than squared error. This seems to incentivize a model to find more “average” parameters that benefits the overall group of assets more than an individual asset. To illustrate, look at the actual == 0 observation

  * 10x improvement to go from 0.999 to 0.5 for log loss, 4x improvement for sq err
  * 693x improvement to go from 0.5 to 0.001 for log loss, 250,000x improvement for sq err



|  | predicted |  |  |  |   
---|---|---|---|---|---|---  
| log loss | 0.001 | 0.25 | 0.5 | 0.75 | 0.999  
actual | 0 | 0.001 | 0.288 | 0.693 | 1.386 | 6.908  
| 0.25 | 1.728 | 0.562 | 0.693 | 1.112 | 5.181  
| 0.5 | 3.454 | 0.837 | 0.693 | 0.837 | 3.454  
| 0.75 | 5.181 | 1.112 | 0.693 | 0.562 | 1.728  
| 1 | 6.908 | 1.386 | 0.693 | 0.288 | 0.001  
|  |  |  |  |  |   
|  |  |  |  |  |   
|  | predicted |  |  |  |   
| sq err | 0.001 | 0.25 | 0.5 | 0.75 | 0.999  
actual | 0 | 0.000 | 0.063 | 0.250 | 0.563 | 0.998  
| 0.25 | 0.062 | 0.000 | 0.063 | 0.250 | 0.561  
| 0.5 | 0.249 | 0.063 | 0.000 | 0.063 | 0.249  
| 0.75 | 0.561 | 0.250 | 0.063 | 0.000 | 0.062  
| 1 | 0.998 | 0.563 | 0.250 | 0.063 | 0.000

---

### Post #5 — **shatteredx** | 2023-06-19 15:32 UTC

Cool experiment!

The case for 20,000+ tree models seems dubious. Maybe a gain of +0.0010 Corr? Glad you guys showed the results for sub 20k tree models.

More important question: how many trees for good TC?

EDIT: OK fine, I will admit the 20k+ tree models are generally more stable at higher depths.

---

### Post #6 — **svendaj** | 2023-06-22 19:28 UTC

Thanks guys. Can you publish the tables for less compute version?

---

### Post #7 — **svendaj** | 2023-06-23 17:18 UTC

… also: are you considering grid search for XGBoost? Especially for low compute settings?

---

### Post #8 — **thomasxthomas** | 2023-06-23 20:56 UTC _(reply to #7)_

Maybe this preprint can help? [[2303.07925] Robust incremental learning pipelines for temporal tabular datasets with distribution shifts](<https://arxiv.org/abs/2303.07925>)

---

### Post #9 — **richai** | 2023-06-26 07:36 UTC _(reply to #8)_

How did the approaches in your preprint work in May [@thomasxthomas](</u/thomasxthomas>). Did you have models which reliably avoided the drawdown so many models experienced? Which approach worked best?

---

### Post #10 — **gbrecht** | 2023-06-26 18:28 UTC

Is there a reason:

  * a full grid search was done and not a more sophisticated method of hyperparameter search?
  * important lightgbm parameters like `min_data_in_leaf` or regularization was not included?

---

### Post #11 — **mantz** | 2023-07-06 09:28 UTC

I don’t understand this experiments, since better results were published here:

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/forum.numer.ai/master_key/48/3343_2.png)

[Target Cyrus - New Primary Target](<http://forum.numer.ai/t/target-cyrus-new-primary-target/6303>) [Announcements](</c/announcements/8>)

> Overview 4 new target variations are being released on Numerai. There are 20D and 60D versions of each, for a total of 8 new targets. They will be released in the v4.1 dataset starting with the round opening on April 18. One of them, target Cyrus, will become the official target used for payouts in one month, beginning with the round opening on May 13. Along with this change, we are also implementing a change in the way correlation is calculated. This change weights your lowest and highest p… 

What is the reason why you perform a huge grid search and get worse results?
