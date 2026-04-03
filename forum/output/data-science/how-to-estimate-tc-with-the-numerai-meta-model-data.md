---
title: "How to estimate TC with the numerai meta model data"
category: Data Science
url: https://forum.numer.ai/t/how-to-estimate-tc-with-the-numerai-meta-model-data/6032
created_at: 2023-01-12T07:46:43.385000+00:00
last_posted_at: 2023-01-12T20:49:04.201000+00:00
posts_count: 3
views: 1363
tags: []
---

# How to estimate TC with the numerai meta model data

---

### Post #1 — **nyuton** | 2023-01-12 07:46 UTC

Hi,

TC is a metric that shows, how much your model improves the meta model.  
That means that ensembling the predictions of my model with the metamodel should improve the meta model metrics like corr and sharpe. The fund also picks trades from the stocks, where the metamodel has the most confidence (top/bottom 200).

With that in mind, we can estimate the (past) TC of a model with the following script:

> validation[‘my_prediction’] = my_model.predict(validation[features])
> 
> mm = pd.read_parquet(‘v4.1_meta_model.parquet’)  
>  validation= validation.join(mm[‘numerai_meta_model’])
> 
> validation.loc[:, “mm_ensemble”] = validation[[‘era’, ‘my_prediction’, ‘numerai_meta_model’]].dropna().groupby(‘era’).rank(pct=True).mean(axis=1)
> 
> validation_stats = validation_metrics(  
>  validation,  
>  [‘my_prediction’, ‘mm_ensemble’, ‘numerai_meta_model’],  
>  example_col=EXAMPLE_PREDS_COL,  
>  fast_mode=False,  
>  target_col=TARGET_COL,  
>  )  
>  print(validation_stats[[‘mean’, ‘sharpe’, ‘tb200_mean’, ‘tb200_sharpe’]])

So TC should be correlated with the gain of the meta model after ensembling.  
I guess, if the tb200_mean of the ensemble is lower than the that of the metamodel, then there is no TC to expect from that model.  
Ideally, the ensemble should outperforms both of it’s components.

Do you think that the above estimation method is correct?  
Has anyone came up with a better estimation?

---

### Post #2 — **jmrichardson** | 2023-01-12 16:19 UTC

That seems reasonable to me. I believe I remember hearing that it was actually top and bottom 500 (instead of 200)?

---

### Post #3 — **olivepossum** | 2023-01-12 20:49 UTC _(reply to #2)_

I think it’s 200 but MDO shared a post optimizing for 500 as mentioned it overfitted less [Optimizing for FNC and TB scores](<http://forum.numer.ai/t/optimizing-for-fnc-and-tb-scores/5132>)
