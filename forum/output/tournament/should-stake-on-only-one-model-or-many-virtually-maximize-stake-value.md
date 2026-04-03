---
title: "Should stake on only one model or many? (virtually maximize stake value)"
category: Tournament
url: https://forum.numer.ai/t/should-stake-on-only-one-model-or-many-virtually-maximize-stake-value/4667
created_at: 2021-12-23T03:41:13.165000+00:00
last_posted_at: 2021-12-23T15:26:29.124000+00:00
posts_count: 4
views: 861
tags: []
---

# Should stake on only one model or many? (virtually maximize stake value)

---

### Post #1 — **meaten12121** | 2021-12-23 03:41 UTC

Hi, everyone.  
The numerai website continuously reminds me to stake multiple models as follows (little annoying for me ![:sweat_smile:](https://emoji.discourse-cdn.com/twitter/sweat_smile.png?v=13)).  
![Screenshot from 2021-12-23 12-17-44](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/f/fa9e16f86af5f928d87c2080b66304718974e982_2_690x53.png)

But I prefer to stake **only one model** and choose the actual submission file from other non-staked models based on their performances.  
We can choose the submission file from non-staked models by the code below.
    
    
    napi = NumerAPI(public_id=cfg.NUMERAI.ID, secret_key=cfg.NUMERAI.KEY)
    dict_performance, dict_performance_2xmmc = {}, {}
    models = ["model1", "model2", "model3"] # non-staked models
    n_rounds_to_mean = 4
    for k in models:
        performance = np.mean([round['corr'] for round
                               in napi.round_model_performances(k)[:n_rounds_to_mean] if round['payout'] is not None])
        performance_2xmmc = np.mean([round['corr'] + 2*round['mmc'] for round
                                     in napi.round_model_performances(k)[:n_rounds_to_mean] if round['payout'] is not None])
        dict_performance[k] = performance if not np.isnan(performance) else -0.25
        dict_performance_2xmmc[k] = performance_2xmmc if not np.isnan(performance_2xmmc) else -0.25
    best_2xmmc = sorted(dict_performance_2xmmc, key=dict_performance_2xmmc.get)[-1]
    best_corr = sorted(dict_performance, key=dict_performance.get)[-1]
    

This tactic can deal with earning/burning eras and virtually maximize your stake value by removing the four-week delay. I assume many participants follow this tactic but I want to hear your opinions.

Thanks!

---

### Post #2 — **autratec** | 2021-12-23 04:30 UTC

considering it took 4-5 weeks to get your money moving from one model to another, it is more faster to move strategy to another, staking more models is a right way.

---

### Post #3 — **meaten12121** | 2021-12-23 06:16 UTC _(reply to #2)_

Thanks for your reply.  
But, I don’t quite understand “move strategy to another.”  
I proposed to stake only one virtual model ( this model doesn’t correspond to specific gbdt or NN model) and choose the best submission on recent rounds from non-staked models ( these models actually correspond to specific gbdt or NN models.)  
I choose the model to submit instead of moving money.

---

### Post #4 — **objectscience** | 2021-12-23 15:26 UTC

Essentially you’re trying to time the market with Stake Switching (moving a model to a staked account). Some of us have done that successfully in the past (I’m guilty of this), but I doubt any of us have done it long enough to actually prove it works over the long term.

If you trust that Numerai’s targets are meaningful, spreading your capital across them is likely a much better solution. Building and funding two low correlated models for each target, or some subset, is better still.
