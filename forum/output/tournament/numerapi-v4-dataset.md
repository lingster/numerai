---
title: "Numerapi v4 dataset"
category: Tournament
url: https://forum.numer.ai/t/numerapi-v4-dataset/5682
created_at: 2022-09-04T19:34:46.737000+00:00
last_posted_at: 2022-09-05T20:34:14.297000+00:00
posts_count: 6
views: 1290
tags: []
---

# Numerapi v4 dataset

---

### Post #1 — **dzheng1887** | 2022-09-04 19:34 UTC

Is there anything in particular we should know about when using the numerapi to download data and upload predictions using models built on v4 data? The performance of my v4 models is much worse than I would have expected so I suspect I may have a bug in my code. But reviewing doesn’t help me find anything that was obviously wrong.

---

### Post #2 — **dzheng1887** | 2022-09-04 19:42 UTC

Like for example, a long time ago, I had to include this “version” argument to have this work for v3 data. But when I look at the numerapi docs, I don’t find this parameter used anymore.
    
    
    `napi.upload_predictions(folder_path+'/tournament_'+model_name+'.csv', model_id=napi_model_id, version=2)`

---

### Post #3 — **kayeffnumeraitor** | 2022-09-05 06:19 UTC

I use these lines of code to connect to the numerapi, download and upload files, and they work just fine:
    
    
    napi = NumerAPI("<MY PUBLIC ID>", "<MY SECRET ID>")
    napi.download_dataset("v4/live.parquet", "live.parquet")
    napi.upload_predictions("my_prediction.csv", model_id="<MY MODEL ID>")

---

### Post #4 — **dzheng1887** | 2022-09-05 18:50 UTC _(reply to #3)_

Thanks, I think that should work too according to docs I find online. Maybe it’s just bad luck on my side. 3 weeks of less than 10 percentile results for CORR and TC. Feel I made an error someone and sent like random predictions.

---

### Post #5 — **kayeffnumeraitor** | 2022-09-05 19:56 UTC _(reply to #4)_

Try to optimize for consistently not having less than zero correlation, rather than for maximum correlation. The signal is remarkably weak, in fact it is so weak that I repeatedly questioned myself if there is any signal at all. Random targets will have correlation in the ballpark of ~ 0.00 +/- 0.01, while the signal is somewhere at 0.03 +/- 0.02. It takes a lot of experimentation, but I can confirm there is a signal to optimize for. The Jerome 20 day target seems to be rather good for corr, but does not work so well for TC for me.

What is also helping is to try to make your model independent against single features. Lets say you create predictions with your model with standard data, and with data where you replace one feature with random numbers. Both predictions should have a high correlation (> 0.95), otherwise your model is too dependent on a single feature. Reason for that is that Numerai drops most of the ~5000 assets you are creating predictions for, especially if the feature exposure is too high. Now imagine the feature that your model is so dependent on is actually the reason for excluding some of the stocks, making all of your models other predictions basically trash.

Also you have to take the train/test split in the official data with a grain of salt. Each era is in the v4 dataset is one week, 4 eras are one month, 12*4 = 48 eras is one year. IIRC, the train set is around 500-600 eras, and the test set is also around 500-600 eras which are roughly 10 years train data + 10 years test data. If you train your model on the train data only, you basically have a model from 2012 trying to predict stocks in 2022. What makes this even worse, is that there are at least 5 features, that have a high correlation with the target in the train set, but zero correlation in the test set (see [this post](<http://forum.numer.ai/t/removing-dangerous-features/5627>)).

And even after considering all of that, while your CORR and FNC might improve, TC can still be consistently bad.

---

### Post #6 — **dzheng1887** | 2022-09-05 20:34 UTC _(reply to #5)_

Hey kayeffnumeraitor, thank you for this thoughtful response. I will consider what you recommend for my models to improve upon them.

I was also just very surprised of the first 3 weeks of results for my two sets of models based on v4 data. The diagnostics looked pretty good, in line and better with what I have done for my v3 data models. Toss it up to random chance I guess for now. Also perhaps due to other items you pointed out here.
