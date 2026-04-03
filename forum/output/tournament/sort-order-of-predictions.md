---
title: "Sort order of predictions"
category: Tournament
url: https://forum.numer.ai/t/sort-order-of-predictions/2885
created_at: 2021-04-15T20:11:32.271000+00:00
last_posted_at: 2021-04-17T06:52:26.459000+00:00
posts_count: 8
views: 875
tags: []
---

# Sort order of predictions

---

### Post #1 — **flipperpie** | 2021-04-15 20:11 UTC

I went to upload my predictions for the first time, but I noticed it doesn’t like the sort order. How exactly should the predictions be sorted? My system doesn’t use the order of the records in the tournament data, in fact that information is lost.

is it sorted by id? or are there other fields in sort as well?

---

### Post #2 — **flipperpie** | 2021-04-15 20:37 UTC

it looks like the sort order is data_type descending , era, id ascending but even that doesn’t work.

---

### Post #3 — **ml_is_lyf** | 2021-04-15 20:45 UTC

Take a look at the example notebook and replicate how it does it, so you just have to put them back in the same order as you received them I guess. I didn’t actually know order mattered as I just copied their code for submitting.

![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/a/a6b40284b03b45900993e09243c4d60763d4bc52.png) [colab.research.google.com](<https://colab.research.google.com/github/numerai/example-scripts/blob/master/making-your-first-submission-on-numerai.ipynb>) ![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/568c419c14aca7a2f68749c9fff9598dd1d7b5e1.png)

### [Google Colab](<https://colab.research.google.com/github/numerai/example-scripts/blob/master/making-your-first-submission-on-numerai.ipynb>)

---

### Post #4 — **flipperpie** | 2021-04-15 21:15 UTC _(reply to #3)_

thanks, I’m not seeing the sort order in that notebook. I guess I need to iterate over the source file as I generate the predictions to get the sort order right.

my system loads the file and then does a lot of processing on it. So I’m trying to reconstruct the sort order but nothing I try seems to work

---

### Post #5 — **ml_is_lyf** | 2021-04-15 21:59 UTC _(reply to #4)_

This bit here
    
    
    predictions_df = tournament_data["id"].to_frame()
    predictions_df["prediction"] = predictions
    predictions_df.head()
    

So as they didn’t change the order before making the predictions, the predictions are in the same order as in tournament_data, so they can just add the predictions as a column next to the ids in tournament_data.

So if you’ve lost the orderings you can just cache the ids in the order in tournament_data, and then construct your predictions file using that ordering.

---

### Post #6 — **bcb** | 2021-04-16 15:41 UTC

The important part is to keep the relation of id <-> prediction as you need to provide both fields - no special ordering needed…

---

### Post #7 — **flipperpie** | 2021-04-17 02:26 UTC _(reply to #6)_

well, I did manage to get it upload by generating the prediction file using the same ID order as the data file. The prediction file must have the same IDs and be in the same order to be accepted.

---

### Post #8 — **orbitalteapot** | 2021-04-17 06:52 UTC _(reply to #7)_

If using pandas you can use reindex:

predictions.reindex(tournament_data.index)
