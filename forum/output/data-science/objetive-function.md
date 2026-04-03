---
title: "Objetive Function"
category: Data Science
url: https://forum.numer.ai/t/objetive-function/2235
created_at: 2021-03-08T12:36:01.474000+00:00
last_posted_at: 2021-04-13T17:41:35.326000+00:00
posts_count: 8
views: 2607
tags: []
---

# Objetive Function

---

### Post #1 — **javiermoral** | 2021-03-08 12:36 UTC

Just writing this to share which target functions you use the most when training your models. I was thinking of customizing an Objective Function for boosted models in order to beat the common methods already developed. I know Spearman’s correlation is non-differentiable due to sort and rank steps, but I found some references to try to deal with these problems:

  * [SoDeep](<https://github.com/technicolor-research/sodeep>)
  * [fast-soft-sort](<https://github.com/google-research/fast-soft-sort/tree/master/fast_soft_sort>)



I’ve tried to use SoDeep loss functions when training my MLPs and it was a complete disaster. So it would be nice to hear some tips from you all. Do you keep going with RMSE, MSE, MAE. MAPE, LOGLOSS…?

---

### Post #2 — **silentj** | 2021-03-08 18:14 UTC

I’ve tried using KL Divergence for learning to rank (see here: <https://theiconic.tech/learning-to-rank-is-good-for-your-ml-career-part-2-lets-implement-listnet-11af69d1704>). Ended up getting slightly worse results than just regular MSE so I didn’t explore it too much. I might come back to it eventually, seemed cool at the time

---

### Post #3 — **greenprophet** | 2021-03-09 02:13 UTC

I just used pearsonr since it seemed close enough without the sort. With NN and pytorch era batches i got better validation with pearsonr + mseloss than just mseloss. Only have a couple rounds started on live though.

Would like to eventually get some ranking and feature neutralization directly in the loss.

---

### Post #4 — **javiermoral** | 2021-03-10 10:41 UTC _(reply to #3)_

Did you code yourself the person correlation loss function? Or is it implemented elsewhere?

---

### Post #5 — **greenprophet** | 2021-03-10 18:31 UTC

I used this code

[gist.github.com](<https://gist.github.com/ncullen93/58e71c4303b89e420bd8e0b0aa54bf48>)

#### <https://gist.github.com/ncullen93/58e71c4303b89e420bd8e0b0aa54bf48>

##### pytorch_correlations.py
    
    
    def pearsonr(x, y):
        """
        Mimics `scipy.stats.pearsonr`
    
        Arguments
        ---------
        x : 1D torch.Tensor
        y : 1D torch.Tensor
    
        Returns

This file has been truncated. [show original](<https://gist.github.com/ncullen93/58e71c4303b89e420bd8e0b0aa54bf48>)

define the function variables
    
    
        criterion = nn.MSELoss()
        corr_loss_fn = pearsonr
    

then in pytorch loop with loss functions I called like this. but depending on your modelling results might be different indexing. Also not sure if constants on losses are relevant. I get confused about this.
    
    
    preds = model(x)                                
                                        loss = criterion(preds[0], y)
                                        corr_loss = 1 - corr_loss_fn(preds[0].squeeze(), y.squeeze())
                                        if USE_CORR_LOSS:
                                            loss += corr_loss * 0.05
                                        if phase=='train':
                                            loss.backward()
                                            optimizer.step()

---

### Post #6 — **lucky_chicken** | 2021-03-14 00:25 UTC _(reply to #1)_

I’m using fast-soft-sort for my neural nets, is better than MSE for me, but still worse than simple xgboost. I must be doing something wrong.

---

### Post #7 — **javiermoral** | 2021-03-28 15:44 UTC _(reply to #6)_

Same for me, it does not work as good as expected.

---

### Post #8 — **javiermoral** | 2021-04-13 17:41 UTC _(reply to #5)_

I can’t see how the gradient and the hessian are computed in your code
