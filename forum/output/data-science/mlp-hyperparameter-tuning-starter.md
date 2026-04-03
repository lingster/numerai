---
title: "MLP hyperparameter tuning starter"
category: Data Science
url: https://forum.numer.ai/t/mlp-hyperparameter-tuning-starter/1496
created_at: 2021-01-20T00:45:02.392000+00:00
last_posted_at: 2021-03-04T08:36:14.328000+00:00
posts_count: 6
views: 1794
tags: []
---

# MLP hyperparameter tuning starter

---

### Post #1 — **katsu1110** | 2021-01-20 00:45 UTC

Hi all,

I share my kaggle notebook to build a simple neural network (multi-layer perceptron) to fit the Numerai Tournament data.

[[numerai] MLP with KerasTuner Starter](<https://www.kaggle.com/code1110/numerai-mlp-with-kerastuner-starter/notebook>)

Since for beginners, hyperparameters in a NN are hard to tune, I also demonstrate how to use the [KerasTuner](<https://www.tensorflow.org/tutorials/keras/keras_tuner>) to automatically fine-tune the hyperparameters of a NN in the same notebook.

Hopefully this notebook can help someone who gets bored with an integration_test-like model and is willing to try out NN.

---

### Post #2 — **load_2021** | 2021-02-24 08:16 UTC

Thank you for your contribution. I upvoted the notebook. Hope that helps for my first sumission in Numerai.

By the way, how did you do in the “Jane Street Market Prediction” competition? Could you compare and contrast the two competitions so that I would understand what Numerai is like more easily?

Thank you very much

---

### Post #3 — **katsu1110** | 2021-02-24 13:58 UTC _(reply to #2)_

I will share my approach in the JaneStreet competition in Kaggle, not here, only if I will be victorious in the end. Otherwise there is no point sharing my approach for anyone.

Numerai is simply easier to work on than the JaneStreet, as there is no TimeSeriesAPI complication. Also there is quite a bit of resources for new starters, so you might want to have a look.

<https://docs.numer.ai/tournament/new-users>

---

### Post #4 — **load_2021** | 2021-02-25 03:55 UTC _(reply to #3)_

Thank you for your advice.

---

### Post #5 — **juanigp** | 2021-03-03 18:26 UTC

Hi, thank u this is actually pretty useful.

I am training a MLP, and I get similar learning curves and a similar histogram of predictions, yet when I upload my predictions I have a lower Validation Corr (between 0.0005 and 0.002), considerably smaller than the metrics you show by the end of the notebook.

Do you know why it may be? Is there something I am missing in between predicting with the MLP and submitting the predictions?

Thank you

---

### Post #6 — **katsu1110** | 2021-03-04 08:36 UTC _(reply to #5)_

I don’t know, but NN’s performance is hyperparameter sensitive, so I am not surprised. Maybe increase the batch size.
