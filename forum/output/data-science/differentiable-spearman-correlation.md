---
title: "Differentiable Spearman Correlation"
category: Data Science
url: https://forum.numer.ai/t/differentiable-spearman-correlation/2588
created_at: 2021-03-29T14:29:24.792000+00:00
last_posted_at: 2021-03-30T13:52:07.512000+00:00
posts_count: 3
views: 4457
tags: []
---

# Differentiable Spearman Correlation

---

### Post #1 — **gaugesym** | 2021-03-29 14:29 UTC

I want to try out to directly train on the ‘corr’ on which we are scored on. For this I would have to implement the Spearman correlation and get the gradient and hessian to be able to use it as a custom loss function in xgboost (or keras etc.). So far I was able to implement it in tensorflow and also get the gradient but the hessian does not work yet. I created a question with the details on stackoverflow:

[stackoverflow.com](<https://stackoverflow.com/questions/66854994/hessians-for-spearman-rank-correlation>) [ ![GaugeSym](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/a/a0d7e2642eade115e5f2436ee8bf8d26b5c07792.png) ](<https://stackoverflow.com/users/13672947/gaugesym>)

####  [Hessians for Spearman Rank Correlation](<https://stackoverflow.com/questions/66854994/hessians-for-spearman-rank-correlation>)

**python, tensorflow, gradient, hessian**

asked by [ GaugeSym ](<https://stackoverflow.com/users/13672947/gaugesym>) on [01:21PM - 29 Mar 21 UTC](<https://stackoverflow.com/questions/66854994/hessians-for-spearman-rank-correlation>)

Maybe someone of you has already tried to do something similar and knows why my code isn’t quite right yet.

---

### Post #2 — **oiboy** | 2021-03-29 23:38 UTC

A couple people have been trying this. Check out

![](http://forum.numer.ai/user_avatar/forum.numer.ai/teddykoker/48/722_2.png) [Differentiable Spearman in PyTorch (Optimize for CORR directly)](<http://forum.numer.ai/t/differentiable-spearman-in-pytorch-optimize-for-corr-directly/2287>) [Data Science](</c/data-science/5>)

> [@mdo](</u/mdo>) previously showed how to use a [custom loss function](<http://forum.numer.ai/t/custom-loss-functions-for-xgboost-using-pytorch/960>) which involved taking the gradient of the sharpe ratio of the Pearson correlations over different eras. Although Pearson and Spearman might return similar values, it could be rewarding to optimize for Spearman directly (or Sharpe of Spearman). Since the ranked Spearman correlation needs a sort operation (which is not differentiable), it has not been possible to compute the gradient with respect to predictions, which eliminated the possibil… 

and

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/j/bbe5ce/48.png) [Objetive Function](<http://forum.numer.ai/t/objetive-function/2235>) [Data Science](</c/data-science/5>)

> Just writing this to share which target functions you use the most when training your models. I was thinking of customizing an Objective Function for boosted models in order to beat the common methods already developed. I know Spearman’s correlation is non-differentiable due to sort and rank steps, but I found some references to try to deal with these problems: [SoDeep](<https://github.com/technicolor-research/sodeep>) [fast-soft-sort](<https://github.com/google-research/fast-soft-sort/tree/master/fast_soft_sort>) I’ve tried to use SoDeep loss functions when training my MLPs and it was a complete disaster. So it would be ni… 

I can’t find where I read it, but I believe the fast-soft-sort package’s Spearman function is only differentiable once, which would cause your `None` issue. You could try [@mdo](</u/mdo>)’s [solution, which is to just use a matrix of ones as the Hessian](<http://forum.numer.ai/t/custom-loss-functions-for-xgboost-using-pytorch/960>).

---

### Post #3 — **gaugesym** | 2021-03-30 13:52 UTC _(reply to #2)_

Thanks for the reply. I got it working by setting the hessians to 1 instead of actually calculating them. I’m able to train with it in xgboost but even after quite some parameter tuning I’m so far not able to get better results than from just using rmse or similar standard loss functions.
