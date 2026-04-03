---
title: "Model Upload Beta!"
category: Announcements
url: https://forum.numer.ai/t/model-upload-beta/6445
created_at: 2023-06-08T19:27:27.418000+00:00
last_posted_at: 2023-06-19T07:20:10.672000+00:00
posts_count: 10
views: 1699
tags: []
---

# Model Upload Beta!

---

### Post #1 — **slyfox** | 2023-06-08 19:27 UTC

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/1/13f712b24fdc27400bb6b7feff5568536ded38e9_2_500x500.jpeg)image1000×1000 173 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/1/13f712b24fdc27400bb6b7feff5568536ded38e9.jpeg> "image")

Hello all!

This morning during the fireside chat I presented on our newest automation feature - model uploads.

> Model Upload allows you to upload your entire prediction pipeline to Numerai. Once uploaded, Numerai will take care of running it every day to generate live submissions.
> 
> Unlike other automation options, Model Upload is completely free and does not require you to set up any infrastructure.

Here are the [slides](<https://docs.google.com/presentation/d/1kY_fKDy8g7Ls_vEAA_oG2VzkDMxmheGEcidSBLlodNk/edit?usp=sharing>) and here are the [instructions](<https://docs.google.com/document/d/1T75KrWbayOUSbLSkgSZEg7VGPrulK8ZkofheENTxABA/edit?usp=sharing>) on how to join the beta test. Please direct all model upload feedback to this [channel on discord](<https://discord.gg/Q9SfSB39>).

We welcome everyone to join the beta test and let us know what you think of this new feature!

---

### Post #2 — **ageonsen** | 2023-06-10 02:50 UTC

Thanks for the new feature! Will the feature neutralization be also supported?

---

### Post #3 — **agorog** | 2023-06-12 07:21 UTC _(reply to #2)_

You can probably add the neutralization to your predict function:

> def predict(live_features: pd.DataFrame) → pd.DataFrame:  
>  live_predictions = model.predict(live_features[feature_cols])  
>  …do some neutralization  
>  submission = pd.Series(live_predictions, index=live_features.index)  
>  return submission.to_frame(“prediction”)

---

### Post #4 — **slyfox** | 2023-06-12 20:21 UTC _(reply to #2)_

Yep [@agorog](</u/agorog>) is correct, you can any code you want inside your predict function, including neutralization.

---

### Post #5 — **agorog** | 2023-06-13 07:04 UTC

Is there a way to control the submission file name through this method? If not, what submission file name will these submissions get?

---

### Post #6 — **surajp** | 2023-06-14 19:46 UTC _(reply to #2)_

[models_assemble_numerai_upload.ipynb](<https://colab.research.google.com/drive/1jLe8TfFbgrZTzehJhyUEYLJEuWvlIqch?usp=sharing>)

---

### Post #7 — **pschork** | 2023-06-16 19:03 UTC _(reply to #5)_

The submission filenames are formatted as `live_predictions-[random 12-digits].csv` and partitioned by the `model_uuid` when uploaded to S3.  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/0/067e36f625c1b5a60110a28400f088a76a3d7918_2_690x370.png)image2338×1256 308 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/0/067e36f625c1b5a60110a28400f088a76a3d7918.png> "image")

---

### Post #8 — **svendaj** | 2023-06-18 20:07 UTC

Fantastic feature! Thanks [@slyfox](</u/slyfox>) and whole Numerai team!

To test it and possibly to show how easy is it to join Numerai for newcomers, I have created [public Kaggle notebook](<https://www.kaggle.com/code/svendaj/hello-numerai-automated>) based on your [`hello_numerai.ipynb` example](<https://github.com/numerai/example-scripts/blob/master/hello_numerai.ipynb>). Output folder of the notebook contains pickled model for download/upload. I have created [new model JOS_KAGGLE_TEST](<https://numer.ai/jos_kaggle_test>), uploaded result and voilà yesterday it was submitting predictions at 17:24.

Kagglers now can just create Numerai account, new model and upload pickled model even without forking their own version of [Hello Numerai notebook](<https://www.kaggle.com/code/svendaj/hello-numerai-automated>). Obviously, they will get sub-par performance (although who knows where will be this model on leaderboard), but they can easily tweak it so that they will get better results and can start staking.

On the downside: I will now need to rewrite my about 20 models ![:crazy_face:](http://forum.numer.ai/images/emoji/twitter/crazy_face.png?v=12), but I think it’s absolutely worth it as it frees me from automation tinkering, which prevented me from spending more time on modelling and data science.

---

### Post #9 — **svendaj** | 2023-06-18 23:30 UTC

I am not able to give feedback on [Discord](<https://discord.gg/Q9SfSB39>), so at least here:

I am training my models on int8 datasets (memory constrains) and predictions are produced on `live_int8.parquet`. Could pickled predict function take as argument type of live data (float or int)? Otherwise I would need to convert live data to int, which is unnecessary when the int data are published anyway…

---

### Post #10 — **agorog** | 2023-06-19 07:20 UTC _(reply to #7)_

That is sad for me, because I evaluate my models based on their submission names ![:frowning:](http://forum.numer.ai/images/emoji/twitter/frowning.png?v=12)  
It is a stupid idea, but we weren’t allowed to change the name of the models + at the beginning we didn’t had 70 submission slots, so I had to keep track somehow, what is what.
