---
title: "Expected 'Score' Value"
category: Tournament
url: https://forum.numer.ai/t/expected-score-value/2441
created_at: 2021-03-18T20:09:12.348000+00:00
last_posted_at: 2021-03-20T15:44:41.256000+00:00
posts_count: 3
views: 771
tags: []
---

# Expected "Score" Value

---

### Post #1 — **evanhennis** | 2021-03-18 20:09 UTC

I am just starting out creating a model. What should I be trying to hit when I run the “Score” method against the [data_type == ‘validation’] data? I see the top 100 people in the tournament are >0.03 but that seems like a high goal at the start.
    
    
    # Submissions are scored by spearman correlation
    def correlation(predictions, targets):
        ranked_preds = predictions.rank(pct=True, method="first")
        return np.corrcoef(ranked_preds, targets)[0, 1]
    
    # convenience method for scoring
    def score(df):
        return correlation(df[PREDICTION_NAME], df[TARGET_NAME])

---

### Post #2 — **profricecake** | 2021-03-18 22:17 UTC

![](http://forum.numer.ai/user_avatar/forum.numer.ai/evanhennis/48/702_2.png) evanhennis:

> What should I be trying to hit when I run the “Score” method against the [data_type == ‘validation’] data?

I recommend loading up the example predictions and computing the spearman correlation of those predictions against the validation data. Take note of that number (and please post it here as I’m curious what it is but have never computed it myself), then compare it to the historical performance of the [@benchmark_models](</u/benchmark_models>) model.

I call your attention to that model in particular because it just posts the example predictions each week. By looking at this one example’s performance against both validation data and the live data, you might get a sense of what to expect in the competition. Of course there’s no saying that your model will experience similar variance to [@benchmark_models](</u/benchmark_models>), but it’s at least a place to start trying to answer your question.

Good luck!

---

### Post #3 — **evanhennis** | 2021-03-20 15:44 UTC

I did see that model so that probably would be a good start. I am trying to create a neural net solution. My first run will be with no feature modification to get a baseline. Then I will try and crunch the numbers to get a real solution.
