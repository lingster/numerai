---
title: "Download v2/dataset for daily uploads (Numerai Classic)"
category: Tournament
url: https://forum.numer.ai/t/download-v2-dataset-for-daily-uploads-numerai-classic/5815
created_at: 2022-11-01T15:08:47.458000+00:00
last_posted_at: 2022-11-03T14:13:30.150000+00:00
posts_count: 10
views: 1048
tags: []
---

# Download v2/dataset for daily uploads (Numerai Classic)

---

### Post #1 — **stepan** | 2022-11-01 15:08 UTC

Hello everyone!  
I have problem with download and upload predictions for daily tournamets (Numerai Classic)  
My model work on the v2 version dataset and in weekly tournament I use this code:
    
    
    df = pd.read_csv(f'https://numerai-public-datasets.s3-us-west-2.amazonaws.com/latest_numerai_training_data.csv.xz')
    df_live = pd.read_csv(f'https://numerai-public-datasets.s3-us-west-2.amazonaws.com/latest_numerai_tournament_data.csv.xz'
    

But when I upload predictions I took arror that upload not current dataset.

Model with v4 version uploaded correct becourse I downloaded data from NumerAPI()  
In NumerAPI() I didn’t find 2 version with train dataset.  
Who use v2 version for daily tournaments help me.

---

### Post #2 — **shatteredx** | 2022-11-01 20:32 UTC

Hi. I had this same error.

numerai_training_data.csv and numerai_tournament_data.csv are not updated for daily rounds.

You need to download v2 live data like this:
    
    
    napi.download_dataset('v2/numerai_live_data.csv', f"live_{current_round}_v2.csv")

---

### Post #3 — **stepan** | 2022-11-02 07:46 UTC _(reply to #2)_

Thanks!  
Am I correct that I’m not retraining my model (only training on the weekly dataset), I’m just making a prediction for the new live dataset?

---

### Post #4 — **autratec** | 2022-11-02 09:19 UTC _(reply to #2)_

i am using:

napi.download_dataset(“v2/numerai_live_data.parquet”, “numerai_live_data.parquet”)

should it get latest data or i need to specify current round ?

---

### Post #5 — **wigglemuse** | 2022-11-02 13:23 UTC _(reply to #3)_

The training data never changes. The v2 validation data doesn’t even get updated. Same with v3 data I think. So you NEVER need to retrain, and never have. It’s the same data every week. That is, unless you are doing something weird with relating the live data to the training data and re-training based on that, i.e. if you are changing the training data yourself depending on what you are predicting that week. Barring that nothing has changed so no retraining needed.

The v4 “training” data also doesn’t change. So the only reason to even download anything other than the live era is:

– if you are using v4 data  
– and you are incorporating the latest validation eras with targets into your training

v4 validation data does get added to weekly (most weeks), but the older versions do not – not with targets anyway. (Anybody correct me if I’m wrong about that with v3, but I don’t think they are adding new eras with targets on v3, right?)

---

### Post #6 — **shatteredx** | 2022-11-02 13:38 UTC _(reply to #3)_

[@stepan](</u/stepan>) wigglemuse is correct. The only data file that gets updated every week with new target values is the v4 validation file. v2 tournament gets new test eras but target column will be NaN.

[@autratec](</u/autratec>) You are fine. The second argument just renames the file, so my code renames the file with the round number.

---

### Post #7 — **kayeffnumeraitor** | 2022-11-02 16:58 UTC _(reply to #3)_

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/s/848f3c/48.png) stepan:

> Am I correct that I’m not retraining my model

To give you a little bit more context to this question, the “train” data provided by numerai contains 574 eras, which are the 574 weeks (11 years) starting from the first week of 2003 until the first week of 2014, while the “validation” data contains the remaining weeks of labeled data until 6 weeks from today.  
For learning/testing purposes I think this train/validation split is fine, but I think it is debatable whether a model trained on data between 2003-2014 can or cannot be applied on data from 2022.

---

### Post #8 — **wigglemuse** | 2022-11-02 17:35 UTC _(reply to #7)_

Except v2 data which has monthly non-overlapping eras. (120 eras in the training set = 10 years plus there is at least 1 more year in the validation set with targets).

---

### Post #9 — **autratec** | 2022-11-03 08:59 UTC _(reply to #5)_

it is good reminder that training data set never change. is there any document or previous discussion to provide more details ?

---

### Post #10 — **wigglemuse** | 2022-11-03 14:13 UTC _(reply to #9)_

More details that it doesn’t change? Other than wholesale new datasets (i.e. v2, v3, v4) they have never changed training sets, and the ones we have are all based on the same time period. (Before v4 the validation set would get some extra eras every once in a while.) The idea is to come up with stuff that doesn’t necessarily depend on recent trends, and they didn’t want us overfit to recency. Anybody that ever thought that the training data gets updated regularly was operating on a unfounded assumption and doing a lot of wasteful downloading and retraining on the same data over and over.

They have however softened on that idea because they also have a competing idea that we just should have as much data as possible, and now finally with v4 we can get data from the fairly recent past as it comes in. (Marked as “validation” – the “training” set still is static but labels are just labels – you can train on whatever you want.) But the most recent data is still only _fairly_ recent because it has to be at least 4 weeks old to get any targets. If you want to react to what the market is doing in the past few days or a week, then Signals is your game.
