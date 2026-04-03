---
title: "SQL and the Dataset"
category: Data Science
url: https://forum.numer.ai/t/sql-and-the-dataset/5283
created_at: 2022-04-19T02:49:01.181000+00:00
last_posted_at: 2022-06-10T11:58:39.819000+00:00
posts_count: 6
views: 999
tags: []
---

# SQL and the Dataset

---

### Post #1 — **crownholder** | 2022-04-19 02:49 UTC

I have a question…

How can I find out the records and fields for the dataset?  
Can anyone point me to the information?

---

### Post #2 — **autratec** | 2022-04-19 03:27 UTC

have you tried to download a copy of dataset first ?

---

### Post #3 — **crownholder** | 2022-04-19 03:31 UTC _(reply to #2)_

I have and when I try to open my laptop locks up, not sure why. It feels like I can remember being able to open the file.

---

### Post #4 — **by256** | 2022-04-19 08:54 UTC _(reply to #3)_

The dataset is much bigger now so you might be maxing out your laptop’s RAM.

---

### Post #5 — **jefferythewind** | 2022-04-19 16:51 UTC

It’s best to use the API. You can then get a smaller version of the data. The best thing to try is by way of the github repository: [Numerai · GitHub](<https://github.com/numerai>).

You can use this chunk from `example_scripts/example_model.py`, change the `"medium"` to `"small"` for the smallest version of the data.
    
    
    print('Reading minimal training data')
    # read the feature metadata and get a feature set (or all the features)
    with open("v4/features.json", "r") as f:
        feature_metadata = json.load(f)
    # features = list(feature_metadata["feature_stats"].keys()) # get all the features
    # features = feature_metadata["feature_sets"]["small"] # get the small feature set
    features = feature_metadata["feature_sets"]["medium"] # get the medium feature set
    # read in just those features along with era and target columns
    read_columns = features + [ERA_COL, DATA_TYPE_COL, TARGET_COL]
    
    # note: sometimes when trying to read the downloaded data you get an error about invalid magic parquet bytes...
    # if so, delete the file and rerun the napi.download_dataset to fix the corrupted file
    training_data = pd.read_parquet('v4/train.parquet',
                                    columns=read_columns)
    validation_data = pd.read_parquet('v4/validation.parquet',
                                      columns=read_columns)
    live_data = pd.read_parquet(f'v4/live_{current_round}.parquet',
                                      columns=read_columns)

---

### Post #7 — **svendaj** | 2022-06-10 11:58 UTC

Latest dataset size makes it almost impossible to do meaningful work in google colab with 12GB RAM. I am using kaggle notebooks to get 16GB RAM and so far so good.  
I have made public my [kaggle download notebook](<https://www.kaggle.com/code/svendaj/numerai-data>) with dataset of current round. If you would be running in your kaggle notebook, you can chain notebooks and use already downloaded data from output of my notebook.
