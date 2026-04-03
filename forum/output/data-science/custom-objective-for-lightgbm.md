---
title: "Custom Objective for LightGBM"
category: Data Science
url: https://forum.numer.ai/t/custom-objective-for-lightgbm/4677
created_at: 2021-12-24T13:52:58.578000+00:00
last_posted_at: 2022-01-13T09:52:29.798000+00:00
posts_count: 13
views: 8257
tags: []
---

# Custom Objective for LightGBM

---

### Post #1 — **gbrecht** | 2021-12-24 13:52 UTC

Similar to the legendary post for XGBoost

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/n/8e7dd6/48.png) [Custom loss functions for XGBoost using PyTorch](<http://forum.numer.ai/t/custom-loss-functions-for-xgboost-using-pytorch/960/3>) [Data Science](</c/data-science/5>)

> Has someone tried to perform cross validation to this model? The snippet below can replace the last line of mdo code… param_fit_grid = { 'base_margin' : base_margin} score = model_selection.cross_val_score( model_adj_sharpe, train[feature_columns], train[target], cv=3, n_jobs=-1, scoring=make_scorer(mean_squared_error), fit_params=param_fit_grid, error_score=123) pr… 

I try to implement a custom loss function for lightgbm. My problem is that it always returns NaN as the predictions it gets passed are always 0. I am looking for any hint what the problem might be. The following code should be executable if you have a utils.read_training_data or obtain the train dataframe otherwise.
    
    
    import lightgbm
    import numpy as np
    import pandas as pd
    from utils import read_training_data
    import torch
    from torch.autograd import grad
    
    train = read_training_data()
    era_idx = [np.where(train.erano==uera)[0] for uera in train.erano.unique()]
    features = [c for c in train.columns if c.startswith('feature_')]
    
    # define adjusted sharpe in terms of cost adjusted numerai sharpe
    def numerai_sharpe(x):
        return (x.mean() -0.010415154) / (x.std()+1)
    
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
        l = torch.matmul(pred_n, target_n)
        return l
    
    def lgbm_train_fobj(preds, train_data):
        # convert to pytorch tensors
        ypred_th = torch.tensor(preds, requires_grad=True)
        ytrue_th = torch.tensor(train_data.get_label().astype(float))
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
    
    def lgbm_train_eval(preds, train_data):
        ypred_th = torch.tensor(preds, requires_grad=True)
        ytrue_th = torch.tensor(train_data.get_label().astype(float))
        all_corrs = []
        # get correlations in each era
        for ee in era_idx:
            score = corr(ypred_th[ee], ytrue_th[ee])
            all_corrs.append(score)
        all_corrs = torch.stack(all_corrs)
        return 'corr', all_corrs.mean(), True
    
    bster = lightgbm.train(
        {
            'max_depth':5,
            'learning_rate':0.01,
            'colsample_bytree':0.1,
            'num_leaves':32,
            'random_state':666,
        },
        lightgbm.Dataset(train[features], label=train['target']),
        num_boost_round=10,
        fobj=lgbm_train_fobj,
        feval = lgbm_train_eval
    )
    

The output reads:
    
    
    [LightGBM] [Warning] Using self-defined objective function
    [LightGBM] [Warning] Auto-choosing row-wise multi-threading, the overhead of testing was 0.002556 seconds.
    You can set `force_row_wise=true` to remove the overhead.
    And if memory is not enough, you can set `force_col_wise=true`.
    [LightGBM] [Info] Total Bins 5250
    [LightGBM] [Info] Number of data points in the train set: 21177, number of used features: 1050
    [LightGBM] [Warning] Using self-defined objective function
    Current loss:nan
    [LightGBM] [Warning] No further splits with positive gain, best gain: -inf
    [LightGBM] [Warning] Stopped training because there are no more leaves that meet the split requirements
    Current loss:nan
    (repeated, so omitted)
    

Thank you very much!

---

### Post #2 — **smilence666** | 2021-12-26 03:52 UTC

thanks for the posting. i didn’t know we could use pytorch to build LGBM custom objective function. I kept deriving grad and hess during the holiday…

---

### Post #3 — **gbrecht** | 2021-12-27 08:14 UTC _(reply to #2)_

For future reference if anybody has a similar problem. I created a minimal example and noticed that the predictions in the first round always arrive as [0,0,…,0] in the objective function. Well, the correlation is not defined for an all-constant array.  
So what I did is a small hack in the objective function
    
    
    if preds constant:
        randomize preds
    

which seems to do the trick but feels … dirty. I searched the docs for an option to initialize the training, but found nothing.

[@smilence666](</u/smilence666>) May I ask what you mean by “deriving grad and hess”? Do you mean as a closed expression? The code uses an automatic gradient calculation library

---

### Post #5 — **smilence666** | 2021-12-27 22:28 UTC _(reply to #3)_

[@gbrecht](</u/gbrecht>)  
yes i know that pytorch is based on autograd which automatically calculate the gradient - just didn’t know we can use it for lightGBM usage. For correlation and some other objective function, we can actually derive the mathematical formula (gradient and hessian) and put it to the custom objective function so XGB or LGBM can use it, which should be faster than autograd.

I also encounter the same error when i used the formulas i derived and i just set correlation to be 1 if the prediction vector is a unique constant.

---

### Post #6 — **gbrecht** | 2021-12-28 10:49 UTC _(reply to #5)_

Thank you very much. If you could share the mathematical formulas would be highly appreciated, as my attempts with autograd are stalled.  
I got a run going with autograd (jax) gradient. That took _VERY_ long to complete and the performance was attrocious. With autograd (again jax) for gradient and hessian the process gets killed because too much RAM before a single boosting round. I guess it is because hessian requires functions from jax.nn and … that requests a lot of memory.

As for using autograd with xgboost/lighgbm: You can mix them together as much as you like/see fitting. The original post uses pytorch, I tried jax.

---

### Post #7 — **smilence666** | 2021-12-28 15:39 UTC _(reply to #6)_

Just realized your goal was to get the grad and hess of Sharpe, sorry about my misunderstanding - i thought you were trying to get that of correlation. Then it’s probably hard to derive the mathematical formulas. But personally i don’t think Sharpe as a objective function will generalize well, but i could be completely wrong.

---

### Post #8 — **lcrmorin** | 2022-01-09 09:46 UTC _(reply to #7)_

What about using tf autodiff ?

> def custom_lgbm_loss(y_hat, y_true):
>     
>     
>     y_hat = tf.Variable(y_hat)
>     y_true = tf.Variable(y_true)
>     
>     with tf.GradientTape() as t1:
>         with tf.GradientTape() as t2:
>             L = custom_tf_loss(y_hat, y_true)
>         grad = t2.gradient(L, y_hat)
>     hess = t1.gradient(grad, y_hat)
>     
>     return grad.numpy(), hess.numpy()
>     

I have found it to work with simple tf loss (L2), but not more complex ones;

---

### Post #9 — **gbrecht** | 2022-01-10 20:32 UTC

when you say “simple tf loss” I assume you mean the line
    
    
    L = custom_tf_loss(y_hat, y_true)
    

right?  
I have to admit I never used tensorflow autodiff, but the stub that you posted looks definetly interesting. The problem I see with more complex functions is that the custom_tf_loss function has to be differentiable. So we are back to using torchsort which imho defeats the purpose of switching from torch to tf…

---

### Post #10 — **baslaa** | 2022-01-12 14:58 UTC _(reply to #3)_

Hi bigbertha,

I found some stuff on init_score in LightGBM, but there is very little info on it. Have you looked at that?  
BTW, how has this loss function with this hack been working for you?

---

### Post #11 — **gbrecht** | 2022-01-12 15:31 UTC

Hallo [@baslaa](</u/baslaa>)

I had not heard of init_score but that is very interesting. I kind of wonder how it compares to boosting for some rounds with another target function. the difference is that not the trees are present in the final model, but only the trees that came after the initial score.  
For me these custom loss functions have not been doing well. I have had much more success with optimizing parameters based on oos metrics than direct optimization for a different gradient. It might very well be due to my technical deficiencies.

---

### Post #12 — **baslaa** | 2022-01-12 15:54 UTC _(reply to #11)_

Hi [@gbrecht](</u/gbrecht>) ,  
So I’ve been trying to get the correlation / sharpe loss to work a little bit today, and what I noticed is this:  
XGBoost (like in that post) has the parameter base_margin, which sets the initial predictions. This is really what we would need instead of the randomized prediction. However, the dumb thing is that this init_score param only exists for lgb.fit() , not lgb.train(). But lgb.fit() doesn’t support custom loss functions.

Now I’ve been trying to do it like this: make a base model on rmse, predict on train data (bootstrap_preds), then in the custom loss function set:
    
    
    if np.all(preds == 0):
             preds = bootstrap_preds
    

However, now I’m having problems with indexing again, with the index ypred_th[ee] being out of bounds.  
In short, a lot of hassle…

What mix of metrics have you been using for parameters, may I ask?

---

### Post #13 — **gbrecht** | 2022-01-12 16:59 UTC _(reply to #12)_

I believe in lgbm.train you pass a params array and there you should be able to pass init_score. I would be really surprised if the sklearn interact was more powerful than the training API.

I have encountered index out of bounds in ypred_th[ee] countless times, always for the same reason: the loss function makes use of the global information of the era => index mapping. So if you do not train on the full data, you get this error.

You may of course ask. There is a thread here call “more metrics for ya” (or similar, by arbitrage) where you find stuff like smart_sortino, smart_sharpe etc but I also played around with corr minus max feature exposure or the number of negative eras

---

### Post #14 — **baslaa** | 2022-01-13 09:52 UTC _(reply to #13)_

So, I’ve been hacking on it for a few hours, and what I’m seeing is that after running a base model on RMSE for around 1000 rounds, the correlation loss function just cannot improve on the base model anymore (it gets stopped out byearly stopping in like 20 rounds).

So I’ve pretty much come to the same conclusion, it doesn’t give much of a benefit…
