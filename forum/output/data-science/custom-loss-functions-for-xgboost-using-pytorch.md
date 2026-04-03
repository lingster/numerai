---
title: "Custom loss functions for XGBoost using PyTorch"
category: Data Science
url: https://forum.numer.ai/t/custom-loss-functions-for-xgboost-using-pytorch/960
created_at: 2020-09-19T09:28:20.740000+00:00
last_posted_at: 2022-07-16T02:19:21.631000+00:00
posts_count: 24
views: 20345
tags: []
---

# Custom loss functions for XGBoost using PyTorch

---

### Post #1 — **mdo** | 2020-09-19 09:28 UTC

Here is some code showing how you can use PyTorch to create custom objective functions for XGBoost. Objective functions for XGBoost must return a gradient and the diagonal of the Hessian (i.e. matrix of second derivatives). Internally XGBoost uses the Hessian diagonal to [rescale the gradient](<https://stats.stackexchange.com/questions/202858/xgboost-loss-function-approximation-with-taylor-expansion>). The Hessian is very expensive to compute, so we replace it with all ones. This basically forces XGBoost to do standard gradient descent rather than the fancier second order version it usually uses. It works fine, but makes it a bit more sensitive to step size, so watch things carefully. Below we make a function to use Adjusted Sharpe as a cost function for XGBoost. Because the Adjusted Sharpe calculation is not defined for a constant initial condition, we first fit a model using the standard least squares cost-function and then start from there (i.e. the base margin) and fit additional trees to improve the in-sample adjusted Sharpe. This should be enough to get you going, have fun!
    
    
    import numpy as np 
    import pandas as pd 
    from xgboost import XGBRegressor 
    import torch
    from torch.autograd import grad
    
    
    trainval=pd.read_parquet("numerai_training_validation_target_nomi.parquet")
    train = trainval[trainval.data_type=='train']
    
    target = "target_nomi" 
    feature_columns = [c for c in trainval if c.startswith("feature")] 
    
    # fit an initial model
    model_init = XGBRegressor(max_depth=5, learning_rate=0.01, n_estimators=2000, colsample_bytree=0.1, nthread=6)
    model_init.fit(train[feature_columns], train[target])
    
    # get prediction from initial model as starting point to improve upon
    base_margin = model_init.predict(train[feature_columns])
    
    # get indexes for each era
    era_idx = [np.where(train.era==uera)[0] for uera in train.era.unique()]
    
    
    # define adjusted sharpe in terms of cost adjusted numerai sharpe
    def numerai_sharpe(x):
        return (x.mean() -0.010415154) / x.std()
    
    def skew(x):
        mx = x.mean()
        m2 = ((x-mx)**2).mean()
        m3 = ((x-mx)**3).mean()
        return m3/(m2**1.5)    
    
    def kurtosis(x):
        mx = x.mean()
        m4 = ((x-mx)**4).mean()
        m2 = ((x-mx)**2).mean()
        return (m4/(m2**2))-3
    
    def adj_sharpe(x):
        return numerai_sharpe(x) * (1 + ((skew(x) / 6) * numerai_sharpe(x)) - ((kurtosis(x) / 24) * (numerai_sharpe(x) ** 2)))
    
    # use correlation as the measure of fit
    def corr(pred, target):
        pred_n = pred - pred.mean(dim=0)
        pred_n = pred_n / pred_n.norm(dim=0)
    
        target_n = target - target.mean(dim=0)
        target_n = target_n / target_n.norm(dim=0)
        l = torch.matmul(pred_n.T, target_n)
        return l
    
    # definte a custom objective for XGBoost
    def adj_sharpe_obj(ytrue, ypred):
        # convert to pytorch tensors
        ypred_th = torch.tensor(ypred, requires_grad=True)
        ytrue_th = torch.tensor(ytrue)
        all_corrs = []
    
        # get correlations in each era
        for ee in era_idx:
            score = corr(ypred_th[ee], ytrue_th[ee])
            all_corrs.append(score)
    
        all_corrs = torch.stack(all_corrs)
    
        # calculate adjusted sharpe using correlations
        loss = -adj_sharpe(all_corrs)
        print(f'Current loss:{loss}')
    
        # calculate gradient and convert to numpy
        loss_grads = grad(loss, ypred_th, create_graph=True)[0]
        loss_grads = loss_grads.detach().numpy()
    
        # return gradient and ones instead of Hessian diagonal
        return loss_grads, np.ones(loss_grads.shape)
    
    
    model_adj_sharpe = XGBRegressor(max_depth=5, learning_rate=0.01, n_estimators=200, nthread=6, colsample_bytree=0.1, objective=adj_sharpe_obj)
    model_adj_sharpe.fit(train[feature_columns], train[target], base_margin=base_margin)

---

### Post #2 — **jrdi** | 2020-09-19 10:32 UTC

Thank you [@mdo](</u/mdo>) for submitting this example! Minor comment, you forgot to `import numpy as np`.

---

### Post #3 — **nrichers** | 2020-10-05 01:14 UTC

Has someone tried to perform `cross validation` to this model?

The snippet below can replace the last line of mdo code…
    
    
    param_fit_grid = { 'base_margin' : base_margin}
    
    score = model_selection.cross_val_score(
                    model_adj_sharpe,
                    train[feature_columns],
                    train[target],
                    cv=3,
                    n_jobs=-1,
                    scoring=make_scorer(mean_squared_error),
                    fit_params=param_fit_grid,
                    error_score=123)
    
    print(score)
    

However, it returns my `error_score=123`, after some investigation I guess the problem occurs here:
    
    
        # get correlations in each era
        for ee in era_idx:
            score = corr(ypred_th[ee], ytrue_th[ee])
    

More exactly `ypred_th[ee]`, apparently after 1 successful cv-fold, it can´t find the the respective index on `ypred_th` tensor.

Moreover, if you replace de the objective function to `squared_log` example function as shown on [xgb docs](<https://xgboost.readthedocs.io/en/latest/tutorials/custom_metric_obj.html>) it works fine on cross_val_score.

**One more thing**

The order of the parameters in `adj_sharpe_obj(ytrue, ypred)` is flipped according to [xgb_docs](<https://xgboost.readthedocs.io/en/latest/tutorials/custom_metric_obj.html>) standards, not sure if it can create any noise.

---

### Post #4 — **mdo** | 2020-10-09 05:27 UTC _(reply to #3)_

I would just write your own cross validation code to make sure you know what it’s doing with a custom loss like this, and make sure you always to cross-validation era-wise, which it doesn’t look like you were trying to do.  
And you had me worried for a sec, but if check the custom loss documents for the sklearn api you’ll see that my code has it in the correct order:

[xgboost.readthedocs.io](<https://xgboost.readthedocs.io/en/latest/python/python_api.html#module-xgboost.sklearn>)

### [Python API Reference — xgboost 3.1.0-dev documentation](<https://xgboost.readthedocs.io/en/latest/python/python_api.html#module-xgboost.sklearn>)

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/bae2e93669f882af06830c4a0a5d25936773e0f4_2_690x358.png)image1548×804 79.6 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/bae2e93669f882af06830c4a0a5d25936773e0f4.png> "image")

  
It’s totally confusing that it is in the opposite order in the two api’s but what are you gonna do, ask for your money back? ![:man_shrugging:](https://emoji.discourse-cdn.com/twitter/man_shrugging.png?v=13)

---

### Post #5 — **jrb** | 2020-10-09 10:02 UTC _(reply to #4)_

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/forum.numer.ai/mdo/48/3398_2.png) mdo:

> It’s totally confusing that it is in the opposite order in the two api’s but what are you gonna do, ask for your money back? ![:man_shrugging:](https://emoji.discourse-cdn.com/twitter/man_shrugging.png?v=15)

Intel vs AT&T, all over again.

PS: Systems joke on a data science forum. ![:slight_smile:](https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=15)

---

### Post #6 — **nrichers** | 2020-10-13 16:55 UTC _(reply to #4)_

I am aware of era-wise cv, I let `cv=3` for for simplicity.

When you say “**write your own cross validation code** ”, you are suggesting to extend  
[BaseSearchCV](<https://github.com/scikit-learn/scikit-learn/blob/0fb307bf3/sklearn/model_selection/_search.py#L400>) class similarly you did [here](<http://forum.numer.ai/t/era-wise-time-series-cross-validation/791>)?
    
    
    class TimeSeriesSplitGroups(_BaseKFold)
    

Sorry about the confusion with xgb docs…

---

### Post #7 — **mdo** | 2020-10-13 17:51 UTC _(reply to #6)_

From your response " I am aware of era-wise cv, I let `cv=3` for for simplicity" I’m not sure you are getting what I mean. The number of folds is independent from what I mean by era-wise cv. By era-wise cv I mean all the break points between folds are at eras, so no folds contain partial eras. You have to use the groups argument in sklearn splitters to get that behavior. But I was suggesting not using the sklearn stuff and just doing the indexing yourself to make sure everything is working as expected.

---

### Post #8 — **nrichers** | 2020-10-13 21:20 UTC _(reply to #7)_

Hi michael, appreciate you attention, I believe I know what you mean…

from [example scripts](<https://github.com/numerai/example-scripts/blob/master/Cross_Validation_and_Model_Optimization.ipynb>)
    
    
    #Group K-fold
    CV = model_selection.GroupKFold(n_splits = 3)
    grp = list(CV.split(X = X_train, y = y_train,  groups = era_train)
    

Unless I’ missing something… but replace to `cv=grp` in my original snippet doesn’t change the output…

---

### Post #9 — **quantverse** | 2020-11-08 16:32 UTC

Experimenting a bit with the [JAX](<https://github.com/google/jax>) based implementation for LightGBM (my first JAX code ever haha):
    
    
    import lightgbm as lgb
    import numpy as np
    import jax.numpy as jnp
    from jax import jit, grad
    
    # functions numerai_sharpe, skew,  kurtosis. adj_sharpe are same as in the example above
    
    @jit
    def corr(ix, pred, target):
        pred_f = pred[ix]
        pred_n = pred_f - pred_f.mean()
        pred_n = pred_n / jnp.linalg.norm(pred_n)
       
        target_f = target[ix]
        target_n = target_f - target_f.mean()
        target_n = target_n / jnp.linalg.norm(target_n)
        l = jnp.matmul(pred_n, target_n)
        return l
    
    @jit
    def calculate_corrs(ypred_th, ytrue_th):
        all_corrs = []
        # get correlations in each era
        for ee in era_idx:
            score = corr(ee, ypred_th, ytrue_th)
            all_corrs.append(score)
        return jnp.array(all_corrs)
    
    def adj_sharpe_obj(ypred_th, ytrue_th):
        all_corrs = calculate_corrs(ypred_th, ytrue_th)
        # calculate adjusted sharpe using correlations
        loss = -adj_sharpe(all_corrs)
        return loss
    
    def sharpe_loss(y_pred, dataset_true):
        ypred_th = jnp.array(y_pred, float)
        ytrue_th = jnp.array(dataset_true.get_label(), float)
    
        # calculate gradients and convert to numpy
        loss_grads = grad(adj_sharpe_obj)(ypred_th, ytrue_th)
    
        # return gradient and ones instead of Hessian diagonal
        return np.array(loss_grads), np.ones(loss_grads.shape)
    
    dm_train = lgb.Dataset(x, label=y)
    bootstrap = lgb.train(some_params, dm_train, num_boost_round=1000, keep_training_booster=True)
    dm_train = lgb.Dataset(x, label=y)
    model = lgb.train(some_params, dm_train, num_boost_round=200, fobj=sharpe_loss,
                                            init_model=bootstrap)
    

Enjoy! It seems working, but there may be bugs of course and the code is most likely suboptimal. Runs on GPU though ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=9)

---

### Post #10 — **johnnyjohnny** | 2020-12-28 00:28 UTC

For me the code from OP gives a negative correlation on validation. I had to change it slightly as the tournament structure changed since the OP but I don’t think anything I did should effect the output.

Anyone else having this issue?

Also, would it be better for the open source models from numerai to be in github and not just in forum posts so that they can easily be maintained to stay current with the latest format of the tournament data?

---

### Post #11 — **shonumerai123** | 2020-12-28 22:02 UTC _(reply to #10)_

I made slight changes to the code so it runs at least. However, it didn’t learn very well as you said out of the box. I guess we need parameter tuning but haven’t been successful yet ![:pensive:](http://forum.numer.ai/images/emoji/twitter/pensive.png?v=9)

---

### Post #12 — **mdo** | 2020-12-28 22:30 UTC _(reply to #11)_

[@johnnyjohnny](</u/johnnyjohnny>) [@shonumerai123](</u/shonumerai123>) This was meant to be a proof of concept example of how one could optimize a fairly complex cost function with XGBoost. It was meant to inspire you to design your own cost functions and was not intended to be blindly copied and used as is. When using custom cost functions in this way, keep in mind issues such as: Is the loss going in the right direction? Does learning rate need to be adjusted? Does it become unstable at any point?  
Also you can always test different stopping points, e.g. before instability occurs, post training using the `ntree_limit` argument to the `predict` function.

---

### Post #13 — **johnnyjohnny** | 2020-12-28 22:51 UTC

Thanks for the clarification.[@mdo](</u/mdo>)

My intention wasn’t to blindly copy it, but to adapt it to my needs with a completely different loss function and use case. However, in my opinion, a good first step in adapting a new piece of code to your specific use case is to first run it in its original form and make sure it works to some degree so that if it doesn’t perform as you expect in your adapted use case you have an idea as to if you broke something that was functional or if the original example is potentially flawed. This is of particular importance when the original code is from an earlier version of the tournament and not compatible with the current data format.

Given that my understanding was that numerai specifically promised that the numerai team member models were to be all completely open source, I had assumed that if this code snippet ends up with a negative validation correlation that I had broken it on my end but it sounds like that’s not the case and this snippet was not designed to actually produce the result I had expected.

My feedback is that if the team is going to provide building blocks and example code to contestants to adapt to their use case that it is more helpful to provide and maintain a working example that does something reasonable and useful so as to clearly illustrate a practical application of the methodology and keep it on github so that the community can issue pull requests (so that for example shonumerai and I aren’t both separately updating it for compatibility with the new data format and instead, whichever of us did it first would have issued a pull request to github).

For example, you mentioned that we need to look at “Is the loss going in the right direction? Does learning rate need to be adjusted?”. Providing an example where the loss is going in the right direction and the learning rate is appropriate seems more helpful as a tool for enabling others to use this approach than not doing so.

---

### Post #14 — **quantverse** | 2020-12-29 17:11 UTC

I honestly think Sharpe Ratio is not a great objective for gradient-descent based training. I don’t use it anymore after experimenting with various better-suited custom objectives. But thanks a lot to [@mdo](</u/mdo>) for the snippet provided, it pointed me in a good direction.

I advice to experiment with:

  * feature exposure penalty as a part of the training objective (but prepare for very slow training times ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=9) )
  * truncated/trimmed correlation mean (you will need [differentiable sorting](<https://github.com/google-research/fast-soft-sort>)) - this actually represents an equivalent of “era boosting”
  * simple stuff like `mean_corr - 0.5 * std_dev_corr`

---

### Post #15 — **johnnyjohnny** | 2020-12-29 18:07 UTC _(reply to #14)_

Thanks, I actually wanted to use it for penalizing based on correlation with a different model so I don’t really care about sharpe at all. I was only curious if this code was supposed to converge and I broke it or not.

Anyways thanks for the help everyone.

FWIW you can make the sharpe ratio stable as a loss function by adding a constant to the denominator, (so divide by x.std() + 0.1 or something) which ensures differentiability, otherwise the behavior near a constant vector is unstable)

---

### Post #16 — **johnnyjohnny** | 2020-12-30 02:43 UTC

Also, in case it helps anyone, this is a fully functional example that converges reasonably and improves the validation sharpe from the example predictions by about 0.1. Its certainly not great and has some inefficient code in it, but it might be a decent building block for others and probably could be better with parameter tuning.

Here is the resulting validation scores (top is the example model, bottom is the result with the adjusted sharpe layered on, <https://gyazo.com/f451505106fc229b486fbc30df1a0b8f>, <https://gyazo.com/a48e13e070e31440c752779cbc3287c4>

Github link: <https://github.com/johnnyjohnny-cloud/numerai-examples>

---

### Post #17 — **restrading** | 2020-12-30 05:47 UTC _(reply to #16)_

Thank you for generously sharing your code. I have been experimenting custom obj myself also and have been struggling to get great results. To summarize your adjustments from the original post:

  1. Bumping learning rate to 5
  2. Bumping colsample to 0.15
  3. Adding 1 to the denominator of sharpe



Did I miss anything?

I am surprised by the following and would love to hear your explanations:

  1. Why bump the learning rate by so much? I suppose it’s to make it converge but this is so much higher than the original that I wonder if it would lead to overfitting
  2. Wouldn’t adding 1 to the denominator of sharpe skew the result too much?

---

### Post #18 — **johnnyjohnny** | 2020-12-30 06:03 UTC _(reply to #17)_

I think that’s most of it. The only other thing is making it explicit that you have to sum the predictions from the base_margin and the trained model when your done training and ready to predict.

The learning rate and colsample (as well as a low number of estimators) are due to the fact that overfit with the adjusted sharpe (and many metrics focused on variance reduction) tends to happen quite quickly so you often get better results with a high learning rate and a low number of steps. If your number of steps is small you often want a higher colsample. Its also relevant that altering the denominator makes the overall magnitude and derivative of the adj sharpe function lower which favors a higher learning rate to compensate. However, its entirely possible that there are better hyper parameter choices than what I put in, I didn’t do any significant fine tuning on those values.

Then the +1 to the denominator is fairly important as otherwise the sharpe tends + or - infinity when the std-deviation is near 0 (even if the correlation is also near 0), so you can get very unstable behavior near a constant vector of predictions. Adding 1 to the denominator doesn’t change the nature of the relationship but ensures that it is always finite and differentiable.

Hope this helps ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=9)

---

### Post #19 — **softeng** | 2022-07-15 16:18 UTC _(reply to #14)_

Do you think that Sharpe ratio is not a good objective when making stock return prediction? It seems to be the best objective. What else can you use? The most obvious way is to use MSE for predicted stock return vs. actual stock return. Given that stock returns are very noisy, I am not sure how good this is.

This paper [Deep Learning Statistical Arbitrage by Jorge Guijarro-Ordonez, Markus Pelger, Greg Zanotti :: SSRN](<https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3862004>) use Sharpe ratio as objective.

---

### Post #20 — **mdo** | 2022-07-15 17:00 UTC _(reply to #19)_

Ratios can be tricky as objectives with very flexible models because there are lots of degenerate solutions, like driving variance to ~0 in the case of the Sharpe ratio.

---

### Post #21 — **softeng** | 2022-07-15 18:17 UTC _(reply to #20)_

Yes. The objective can drive stddev to small value to inflate the Sharpe ratio.

So far, in my experiment this doesn’t seem to be an major issue yet.

My issue is that it seems to optimize for high turnover portfolio, this is even after I subtracted transaction cost from the return in objective function. I am trying artificially larger transaction cost to see if it helps.

There are papers suggesting machine learning based stock prediction typically will optimize toward high turnover, and many so called high return will be gone after taking into account the transaction cost.

---

### Post #22 — **softeng** | 2022-07-15 18:23 UTC _(reply to #20)_

How can I use hessian in your sample code? You used np.ones().

I asked the question here [python - Custom loss functions for XGBoost using PyTorch: hessian does not work - Stack Overflow](<https://stackoverflow.com/questions/72983421/custom-loss-functions-for-xgboost-using-pytorch-hessian-does-not-work>).

Thanks a lot.

---

### Post #23 — **mdo** | 2022-07-15 18:35 UTC _(reply to #22)_

You probably want to check out this as they got proper hessians working for this purpose: [JAX vs PyTorch: Automatic Differentiation for XGBoost | by Daniel Rosenberg | Towards Data Science](<https://towardsdatascience.com/jax-vs-pytorch-automatic-differentiation-for-xgboost-10222e1404ec>)

---

### Post #24 — **restrading** | 2022-07-16 02:19 UTC

[@mdo](</u/mdo>) thanks for sharing, their assumption is Hessian is diagonal, when does this usually hold?
