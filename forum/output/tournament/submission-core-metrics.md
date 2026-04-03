---
title: "Submission core metrics"
category: Tournament
url: https://forum.numer.ai/t/submission-core-metrics/744
created_at: 2020-08-02T18:06:39.572000+00:00
last_posted_at: 2020-10-02T12:30:19.710000+00:00
posts_count: 4
views: 1793
tags: []
---

# Submission core metrics

---

### Post #1 — **olivepossum** | 2020-08-02 18:06 UTC

Hi,  
I wanted to clarify some doubts about the basic metrics shown after a submission is done:

_**Validation correlation:** The mean of your per-era correlations._  
Is this computed using the predictions of the validation data set and the real targets of the validation dataset?  
The code should look like (got it from the github examples):
    
    
    def score(df):
        pct_ranks = df[PREDICTION_NAME].rank(pct=True, method="first")
        targets = df[TARGET_NAME]
        return np.corrcoef(targets, pct_ranks)[0, 1]
    
    validation_data = tournament_data[tournament_data.data_type == "validation"]
    validation_correlations = validation_data.groupby("era").apply(score)
    validation_correlations_web = validation_correlations.mean()
    

_**Validation Sharpe:** This is the mean of your per-era correlations divided by the standard-deviation of your per era correlations._  
Based on what I mentioned above regarding Validation Correlation, Validation Sharpe should look like:

`validation_sharpe_web = validation_correlations.mean() / validation_correlations.std()`

Is that right?

_**Corr With Example Preds:** This is the correlation between your model and the example predictions._  
Which are the example predictions and agains which dataset are calculated?

Thanks in advance.

---

### Post #2 — **correlator** | 2020-08-04 18:32 UTC

Your understanding of val corr and val sharpe is correct. Regarding the example preds, the example predictions is already included in the downloaded numerai data as a csv file so you can compare it with your preds using the corr metric. These example preds are generated using the example_model.py file also included in the downloaded data.

---

### Post #3 — **aif** | 2020-10-02 10:09 UTC _(reply to #2)_

What is considered a good correlation between my model’s predictions and the example predictions? Is it a high or a low correlation more appropriate?

---

### Post #4 — **themicon** | 2020-10-02 12:30 UTC _(reply to #3)_

There is no real good answer to that question. If your correlation is close to the example prediction, then you will most probably not have good MMC. If the correlation is very low between these two, you might have high MMC, but very bad CORR on the live data. You could have very low correlation to the example predictions (be completely orthogonal to it) get good MMC and good CORR. There really isn’t any way to know for sure. Some models have done really well having high correlation with the example predictions, some have done really well that have very low correlation.
