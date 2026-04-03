---
title: "Numerai Datasets url"
category: Data Science
url: https://forum.numer.ai/t/numerai-datasets-url/5516
created_at: 2022-06-17T20:27:22.085000+00:00
last_posted_at: 2022-06-18T06:29:09.059000+00:00
posts_count: 3
views: 1033
tags: []
---

# Numerai Datasets url

---

### Post #1 — **gradyt** | 2022-06-17 20:27 UTC

So I noticed when I downloaded the Live Data it came from numerai_datasets s3 bucket.

Without downloading the entire files for Validation or training I could not see their respective endpoints.

My question…  
What are the urls for the training,live and validation datasets?

I want to pull all of the data by their URL. I assume they are all in a s3 bucket and that maybe I would have to point to the specific folder.

Exact endpoints anyone?

---

### Post #2 — **wigglemuse** | 2022-06-17 20:38 UTC

If you do an api query like this:
    
    
    query {
    	listDatasets(round:320)
    }
    

you’ll get a result like this:
    
    
    {
      "data": {
        "listDatasets": [
          "v2/numerai_datasets.zip",
          "v2/numerai_live_data.csv",
          "v2/numerai_live_data.csv.xz",
          "v2/numerai_live_data.parquet",
          "v3/example_predictions.csv",
          "v3/example_predictions.parquet",
          "v3/example_validation_predictions.csv",
          "v3/example_validation_predictions.parquet",
          "v3/features.json",
          "v3/numerai_datasets.zip",
          "v3/numerai_live_data.csv",
          "v3/numerai_live_data.parquet",
          "v3/numerai_live_data_int8.csv",
          "v3/numerai_live_data_int8.parquet",
          "v3/numerai_tournament_data.csv",
          "v3/numerai_tournament_data.parquet",
          "v3/numerai_tournament_data_int8.csv",
          "v3/numerai_tournament_data_int8.parquet",
          "v3/numerai_training_data.csv",
          "v3/numerai_training_data.parquet",
          "v3/numerai_training_data_int8.csv",
          "v3/numerai_training_data_int8.parquet",
          "v3/numerai_validation_data.csv",
          "v3/numerai_validation_data.parquet",
          "v3/numerai_validation_data_int8.csv",
          "v3/numerai_validation_data_int8.parquet",
          "v4/features.json",
          "v4/live.parquet",
          "v4/live_example_preds.parquet",
          "v4/live_int8.parquet",
          "v4/train.parquet",
          "v4/train_int8.parquet",
          "v4/validation.parquet",
          "v4/validation_example_preds.parquet",
          "v4/validation_int8.parquet"
        ]
      }
    }
    

And then to get the download link for the file you want, do another query like this:
    
    
    query {
    	dataset(filename:"v3/numerai_live_data.csv",round:320)
    }
    

to get your s3 aws link:
    
    
    {
      "data": {
        "dataset": "https://numerai-datasets.s3.amazonaws.com/320/v3/numerai_live_data.csv?response-content-disposition=attachment%3B%20filename%3D320_v3_numerai_live_data.csv&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIJRTTNQLX2AQCKYA%2F20220617%2Fus-west-1%2Fs3%2Faws4_request&X-Amz-Date=20220617T203925Z&X-Amz-Expires=600&X-Amz-SignedHeaders=host&X-Amz-Signature=680abf22809567a21ded36f2537fef94df8de75e5df3ab6a930ff852cbb3b7f0"
      }
    }
    

api at : <https://api-tournament.numer.ai/>

---

### Post #3 — **uuazed** | 2022-06-18 06:29 UTC

If you are using Python:
    
    
    pip install numerapi
    

to get all available datasets
    
    
    import numerapi
    napi = numerapi.NumerAPI()
    napi.list_datasets()
    

to download one of them:
    
    
    napi.download_dataset("v4/live.parquet", "live.parquet")
    

numerapi documentation: [numerapi package — numerapi 2.12.0 documentation](<https://numerapi.readthedocs.io/en/latest/api/numerapi.html#module-numerapi.numerapi>)
