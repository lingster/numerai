---
title: "Which dataset should I use?"
category: Tournament
url: https://forum.numer.ai/t/which-dataset-should-i-use/5696
created_at: 2022-09-18T11:53:15.338000+00:00
last_posted_at: 2022-09-18T19:02:22.548000+00:00
posts_count: 2
views: 652
tags: []
---

# Which dataset should I use?

---

### Post #1 — **ryo_matsuzaka** | 2022-09-18 11:53 UTC

Hello. I am newbie of NUMERAI.  
I started NUMERAI today.  
I have a question about the dataset.

I found three options to download dataset.

  1. Using API  
Like this:  
`napi.download_dataset("v4/train.parquet")`



ref: <https://github.com/numerai/example-scripts/blob/master/example_model.py>

  2. From S3 backet  
Like this:  
`training_data = pd.read_csv("https://numerai-public-datasets.s3-us-west-2.amazonaws.com/latest_numerai_training_data.csv.xz")`



ref: [Numerai](<https://numer.ai/notebook>)

  3. From NUMERAI dashboard



[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/4/43686caedcad099496859c3f8156a29aade187e6.png)image401×434 13.9 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/4/43686caedcad099496859c3f8156a29aade187e6.png> "image")

I tried to use all dataset for creating prediction.csv but I could succeed in running diagnostic tool when I chose prediction with 2nd option. For others, I got the message:

> Your upload seems to be invalid:
> 
> high_invalid_ticker_count: Looks like your upload had 0% of the correct IDs.Make sure you’re predicting on the newest Validation data for round 334.

Which dataset should I use?

---

### Post #2 — **kayeffnumeraitor** | 2022-09-18 19:02 UTC

In the end, it is your own decision which data to use. If you want to use the latest dataset, use the v4 dataset (your first option). If you want to try things out and get started quickly you can use the legacy “v2” dataset, as it is less memory hungry. You could also start with the [example scripts](<https://github.com/numerai/example-scripts>). I haven’t tried to run them, but they are at least a source of some basic ideas, probably also which dataset to use.
