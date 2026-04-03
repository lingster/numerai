---
title: "Model Evaluation Metrics"
category: Data Science
url: https://forum.numer.ai/t/model-evaluation-metrics/337
created_at: 2020-05-06T00:01:34.530000+00:00
last_posted_at: 2021-03-25T20:59:00.640000+00:00
posts_count: 18
views: 9490
tags: []
---

# Model Evaluation Metrics

---

### Post #1 — **joakim** | 2020-05-06 00:01 UTC

I’m curious to understand what the best evaluation metrics are for regression models on the Numerai dataset and problem. The potential ones I’m aware of are (by eras):

  * Spearman Rank correlation coefficient (Monotonic)
  * Pearson correlation coefficient (Linear)
  * Sharpe (mean correlation over StdDev of correlation)
  * Feature Exposure (how does one calculate this?)
  * MAE?
  * MSE/RMSE?
  * R^2?
  * Max Drawdown length & depth? (not sure how to do this)



Any other key ones I’m missing? Do some make more/less sense than others? What about for a multi-class classification model?

Basically I’m using the XGBoost example model (@integration_test) as my baseline, and I’d like to know which metrics to use to compare my model vs the baseline on training & validation. Any/all feedback appreciated!

---

### Post #2 — **bor1** | 2020-05-06 07:33 UTC

I would say to keep in mind you want to optimize your payment. You are evaluated on the Spearman Rank Correlation between your predictions and the live data. So train your models with whatever metric you want, but in the end, check how well they do on spearman :-).

For calculating feature exposure:  
Calculate the pearson correlation between feature 1 and your predictions, between feature 2 and your predictions, … …, between feature 310 and your predictions.

Take the standard deviation over that list of pearson correlations and you have your feature exposure.

---

### Post #3 — **kaleidoscopekosmos** | 2020-05-06 07:50 UTC

Mean Absolute Percentage Error (MAPE) could be added to the list, (although I have never found it useful). Another one that I have heard of that wouldn’t work for this competition is the number of days that your algorithm had new _all-time-highs_ (in contrast to minimizing drawdown—a proxy for this could be a _cumprod()_ of validation era correlation values clipped at 0.2 and normalized as percentages to give a rough estimate of portfolio growth).

It is anecdotal to my own workflow but I find that any time I deviate from MSE I keep returning to MSE. Right now my neural network gradient descent optimizes for MSE and then I usually visually note the sharpe value of the model while doing a lot of baby-sitting to find a model that I like (<https://numer.ai/kaleidoscopekloud>). I need to be more procedural about the process.

Thanks **bor** for explaining the feature exposure!

---

### Post #4 — **quantverse** | 2020-05-06 09:42 UTC _(reply to #2)_

> Take the standard deviation over that list of pearson correlations and you have your feature exposure.

I think it is better to calculate the norm of the whole correlation vector: `sqrt(a^2 + b^2 + c^2 + ...)` instead of stddev

---

### Post #5 — **quantverse** | 2020-05-06 09:48 UTC

I also use `logcosh` as a loss function for training. Nice overview of loss functions here: <https://medium.com/@phuctrt/loss-functions-why-what-where-or-when-189815343d3f>

For optimization I also use **smart sharpe ratio** and **smart sortino ratio** (sharpe/sortino ratio with an autocorrelation penalty). These were discussed in another thread of this forum.

---

### Post #6 — **player1** | 2020-05-06 20:34 UTC

Awesome, thanks guys! Think I’ll go with these ones, for now anyway:

  * Spearman rank
  * Smart Sharpe
  * Smart Sortino
  * Feature Exposure
  * MSE



Found the post that discusses [Smart Sharpe, Sortino etc.](<http://forum.numer.ai/t/performance-stationarity/151/2>)

---

### Post #7 — **kainsama** | 2020-05-06 21:01 UTC

Hey Joakim, a prediction problem in machine learning usually is reduced to an optimization problem. So we need to minimize or maximize a function; for example, in case of regression problems, RMSE, MAE, or R^2 are very popular. We can define **objective function** as a function that has first (Gradient) and second (Hessian) derivatives, whereas a **metric function** does not need to be differentiable. We need the objective to be differentiable, so algorithms like gradient boosting (hence the name!) and neural nets (for backpropagation) or even simple linear regression could be trained. In your list of metrics, only RMSE and MSE are differentiable (there are some proxy functions for some metrics like MAE that can be used as an objective) and the rest can only be used as metrics.

Here in this tournament, the choice of metric is predefined (Spearman Rank Correlation), so we are solving a ranking problem. Our selection of the objective function to be minimized or maximized by our algorithms is an open problem that should be addressed. To pick a proper objective function, first, we need to choose a validation scheme that we trust like k-fold cross-validation, time-split validation, adversarial validation, etc. This is a simple but essential step; without appropriate validation, all our efforts are useless! After that, we can try a list of objective functions to see if one of them improves our validation Spearman Rank Correlation score or not compared to the rest.

As for trying multiclass classification, after we set up our validation we can validate our ideas regarding multiclass classification (for example, ordinal multiclass classification with logistic regression).

**Note:** We can define our custom objective function in XGBoost or LightGBM easily (we can set our proxy Gradient and Hessian and feed them to the algorithm).

---

### Post #8 — **player1** | 2020-05-07 00:55 UTC _(reply to #7)_

Thanks [@Kainsama](</u/kainsama>), I find this SUPER helpful!!

---

### Post #9 — **jrb** | 2020-05-07 17:54 UTC _(reply to #7)_

I must add that it is possible to build differentiable versions or near equivalents of ranking functions (Spearman’s rank correlation coefficient, Pearson correlation coefficient etc) and let the optimization algorithm directly optimize for it.

---

### Post #10 — **kainsama** | 2020-05-07 18:31 UTC _(reply to #9)_

Yep, You are right. I’ve personally never seen many people do that but sure it is a possibilty. Here’s discussion about appiximating MAE with a differentiable proxy function if anyone is interested: <https://www.kaggle.com/c/allstate-claims-severity/discussion/24520>

---

### Post #11 — **sahrenity** | 2020-06-03 14:17 UTC _(reply to #6)_

Thank you for this information!!! ![:raised_hand_with_fingers_splayed:](https://emoji.discourse-cdn.com/twitter/raised_hand_with_fingers_splayed.png?v=13)

---

### Post #12 — **mwangbq** | 2020-11-19 08:04 UTC

def pearson_cumsom_loss(y_true, y_pred):
        '''
        optmize negative pearson coefficient loss
        :param y_true:
        :param y_pred:
        :return:
        '''
        if isinstance(y_true, pd.Series):
            y_true = y_true.values
        if isinstance(y_pred, pd.Series):
            y_pred = y_pred.values
        n = len(y_true)
        y_bar = y_true.mean()
        yhat_bar = y_pred.mean()
        c = 1 / ((y_true - y_bar) ** 2).sum().sqrt()  # constant variable
        b = ((y_pred - yhat_bar) ** 2).sum().sqrt()  # std of pred
    
        a_i = y_true - y_bar
        d_i = y_pred - yhat_bar
        a = (a_i * d_i).sum()
        gradient = c * (a_i / b - a * d_i / b**3)
        hessian = - (np.matmul(a_i.reshape(-1, 1), d_i.reshape(1, -1)) + np.matmul(d_i.reshape(-1, 1), a_i.reshape(1, -1))) / b ** 3 + \
                  3 * a * np.matmul(d_i.reshape(-1, 1), d_i.reshape(1, -1)) / b**5 + a/(n*b**3)
        hessian = hessian - np.ones(shape=(n, n)) * a/b**3
        hessian *= c
        return -gradient, -hessian
    

I create cumsom pearson coefficient loss for tree-based models

---

### Post #13 — **jeremy_berros** | 2020-11-20 23:45 UTC

I thought I would share a discussion I had with [@perfect_fit](</u/perfect_fit>) on implementing Spearman Correlation Custom Loss Function in TF 2.0 [here](<https://www.kaggle.com/carlolepelaars/understanding-the-metric-spearman-s-rho/comments>) and the comment from [@mdo](</u/mdo>) on Rocket.Chat [here](<https://community.numer.ai/channel/datascience?msg=DNHhPqRTyJaoSzKWt>) about Fast Differentiable Sorting and Ranking:

[github.com](<https://github.com/google-research/fast-soft-sort>)

![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/9/966288867f3ef4c0de2f6358c7288a6e95adaced_2_690x344.png)

### [GitHub - google-research/fast-soft-sort: Fast Differentiable Sorting and Ranking](<https://github.com/google-research/fast-soft-sort>)

Fast Differentiable Sorting and Ranking

Now I need to find a way to try this out in my Custom Loss ![:nerd_face:](https://emoji.discourse-cdn.com/twitter/nerd_face.png?v=13)

---

### Post #14 — **javiermoral** | 2021-03-09 08:04 UTC _(reply to #13)_

Did you find out the way to implement it??? I am trying so hard…

---

### Post #15 — **jeremy_berros** | 2021-03-09 17:00 UTC _(reply to #14)_

Not yet. I went another direction. But I will keep you posted when I implement it.

---

### Post #16 — **javiermoral** | 2021-03-10 10:53 UTC _(reply to #12)_

Getting this error (using XGBRegressor):
    
    
    c = 1 / ((y_true - y_bar) ** 2).sum().sqrt()  # constant variable
    

AttributeError: ‘numpy.float32’ object has no attribute ‘sqrt’

---

### Post #17 — **greenprophet** | 2021-03-10 18:21 UTC

maybe try

np.sqrt(((y_true - y_bar) ** 2).sum())

---

### Post #18 — **jeremy_berros** | 2021-03-25 20:59 UTC _(reply to #14)_

Here is an implementation [differentiable-spearman-in-pytorch-optimize-for-corr-directly](<http://forum.numer.ai/t/differentiable-spearman-in-pytorch-optimize-for-corr-directly/2287>) by [@teddykoker](</u/teddykoker>) with his `torchsort` in Pytorch.
