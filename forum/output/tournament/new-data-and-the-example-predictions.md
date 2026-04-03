---
title: "New data and the example predictions"
category: Tournament
url: https://forum.numer.ai/t/new-data-and-the-example-predictions/4733
created_at: 2022-01-05T19:59:58.269000+00:00
last_posted_at: 2022-01-06T01:40:23.221000+00:00
posts_count: 5
views: 1417
tags: []
---

# New data and the example predictions

---

### Post #1 — **pumplerod** | 2022-01-05 19:59 UTC

I may well be missing something elementary, but my recollection is that I used to use the “example_predictions” provided by Numerai as a gauge to assist in measuring my model’s relative performance.

Recently I tried to merge the example_predicitons.csv and example_validation_predictions.csv into my train/valid df files as I used to do, however none of the 'id’s for the example predictions exist within the new data set. Is this working as intended? Or have I made some mistake coming back to this after so many months?

My hope is to have a set of predictions, supplied by the Numerai team, which is a reasonable approximation of the meta-model. This would allow me to compare my models to a known entity and hopefully leverage that information while I tune my performance.

Is there a way to go about creating this information? I can train my own model as a base line, but I would like to use something more official.

---

### Post #2 — **mic** | 2022-01-05 20:51 UTC

DId you see this one?

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/forum.numer.ai/master_key/48/3343_2.png)

[Super Massive Data Release: Deep Dive](<http://forum.numer.ai/t/super-massive-data-release-deep-dive/4053>) [Data Science](</c/data-science/5>)

> Highlights We have just released the biggest upgrade to Numerai’s dataset ever. The new dataset has 4x the number of rows, more than 3x the number of features, and 20 optional targets. The fastest way to get started with the new dataset is to run through the [new example scripts](<https://github.com/numerai/example-scripts>) You can continue to use the old dataset in the same way but models on the new dataset have much higher scores in historical tests. The website’s “Download Data” button will only download new data. The legacy data can sti… 

The new data sets contain different eras than before. Numerai publish example predictions parquet files (not csv) for the updated example model on the new data sets.

---

### Post #3 — **pumplerod** | 2022-01-05 23:30 UTC _(reply to #2)_

I see, and am using the new data .parquet files. However, I’m looking for the `example_predictions` and `example_validation_predictions` files which I still only see .csv files for. And, unless I’m missing something, these files do not correspond with the indices in the new .parquet files.

---

### Post #4 — **mic** | 2022-01-06 00:48 UTC _(reply to #3)_

You can get parquet for those files too.

For example when using numerapi, something like:
    
    
    napi.download_dataset("example_predictions.parquet", "example_predictions.parquet")
    

I think they match the new data.

---

### Post #5 — **mic** | 2022-01-06 01:40 UTC

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/o/e480ec/48.png) [Super Massive Data Release: Deep Dive](<http://forum.numer.ai/t/super-massive-data-release-deep-dive/4053/69>) [Data Science](</c/data-science/5>)

> from numerapi import NumerAPI # NumerAPI napi = NumerAPI() # (file, filename) datasets = [('numerai_training_data_int8.parquet', 'training_data.parquet'), ('numerai_tournament_data_int8.parquet', 'tournament_data.parquet'), ('numerai_validation_data_int8.parquet', 'validation_data.parquet'), ('numerai_live_data_int8.parquet', 'live_data.parquet'), ('example_validation_predictions.parquet', 'example_val_pred.parquet'), ] # Download datase…
