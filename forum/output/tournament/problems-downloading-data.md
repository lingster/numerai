---
title: "Problems downloading data"
category: Tournament
url: https://forum.numer.ai/t/problems-downloading-data/5986
created_at: 2022-12-29T22:23:19.406000+00:00
last_posted_at: 2023-06-19T22:53:34.017000+00:00
posts_count: 6
views: 765
tags: []
---

# Problems downloading data

---

### Post #1 — **javiermoral** | 2022-12-29 22:23 UTC

When I run `numerapi.NumerAPI().download_dataset("v4.1/train.parquet", "data/train.parquet")`I get the following message `requests.exceptions.HTTPError: 403 Client Error: Forbidden for url: https://numerai-datasets-us-west-2.s3.amazonaws.com/384/v4.1/train.parquet?`

When I try to donwload the files via [Numerai](<https://numer.ai/data/v4>) y get the following message: “Acces denied. The ciphertext refers to a customer master key that does not exist, does not exist in this region, or you are not allowed to access.”

What’s happening?

---

### Post #2 — **rdugh** | 2022-12-29 23:29 UTC

I am getting the same error.

---

### Post #4 — **mechanizd** | 2023-06-17 23:21 UTC

Same error here. Anybody figure this out ?

---

### Post #5 — **wigglemuse** | 2023-06-17 23:46 UTC _(reply to #4)_

Don’t think there is actually a problem (original post was 6 months ago), but maybe a glitch or regional issue. Can you download directly off the website? [Numerai](<https://numer.ai/data/v4.1>)

---

### Post #6 — **svendaj** | 2023-06-18 19:28 UTC _(reply to #5)_

I also believe it must have been just a temporary glitch. I have [public Kaggle notebook](<https://www.kaggle.com/code/svendaj/numerai-data>) triggered automatically at Saturday round opening, downloading whole V4 and V4.1 dataset with some logging and there was no report of issue:
    
    
    2023-06-17 15:22:30.365770  starting download for version v4.1/...
    v4.1/features.json: 703kB [00:00, 859kB/s]                           
    v4.1/live.parquet: 4.45MB [00:01, 3.76MB/s]                            
    v4.1/live_example_preds.csv: 178kB [00:00, 361kB/s]                           
    v4.1/live_example_preds.parquet: 134kB [00:00, 275kB/s]                           
    v4.1/live_int8.parquet: 4.45MB [00:01, 3.78MB/s]                            
    v4.1/meta_model.parquet: 21.4MB [00:02, 8.76MB/s]                            
    v4.1/train.parquet: 1.45GB [01:30, 16.0MB/s]                            
    v4.1/train_int8.parquet: 1.45GB [01:28, 16.4MB/s]                            
    v4.1/validation.parquet: 1.58GB [01:29, 17.7MB/s]                            
    v4.1/validation_example_preds.csv: 91.3MB [00:07, 13.0MB/s]                            
    v4.1/validation_example_preds.parquet: 59.3MB [00:04, 12.5MB/s]                            
    v4.1/validation_int8.parquet: 1.58GB [01:32, 17.1MB/s]                            
    2023-06-17 15:29:02.171250  downloads completed.

---

### Post #7 — **mechanizd** | 2023-06-19 22:53 UTC

Thank you. I figured my issue and got it working today. When I called download_dataset on the API I was changing the first parameter thinking I was changing the destination path but it was in fact the path to the data in AWS. Hence it could not find it. In my defense the old numerox API did work like that. I was trying to re-use my old code and looked normal to me.
