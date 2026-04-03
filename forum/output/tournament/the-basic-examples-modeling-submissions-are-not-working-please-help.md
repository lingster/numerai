---
title: "The basic examples Modeling/Submissions are not working, please help"
category: Tournament
url: https://forum.numer.ai/t/the-basic-examples-modeling-submissions-are-not-working-please-help/5760
created_at: 2022-10-20T19:30:38.071000+00:00
last_posted_at: 2022-10-21T18:50:37.550000+00:00
posts_count: 7
views: 729
tags: []
---

# The basic examples Modeling/Submissions are not working, please help

---

### Post #1 — **edddie** | 2022-10-20 19:30 UTC

The code below yields the following error message:

* * *

AttributeError Traceback (most recent call last)  
~\AppData\Local\Temp/ipykernel_11660/55592206.py in   
1 # submit predictions to numer.ai  
2 predictions = model.predict(tournament_data[feature_names])  
\----> 3 predictions.to_csv(“predictions.csv”)

AttributeError: ‘numpy.ndarray’ object has no attribute ‘to_csv’

##########################################################################

import pandas as pd  
from xgboost import XGBRegressor

# training data contains features and targets

training_data = pd.read_csv(“numerai_training_data.csv”).set_index(“id”)

# tournament data contains features only

tournament_data = pd.read_csv(“numerai_tournament_data.csv”).set_index(“id”)  
feature_names = [f for f in training_data.columns if “feature” in f]

# train a model to make predictions on tournament data

model = XGBRegressor(max_depth=5, learning_rate=0.01,   
n_estimators=2000, colsample_bytree=0.1)  
model.fit(training_data[feature_names], training_data[“target”])

# submit predictions to numer.ai

predictions = model.predict(tournament_data[feature_names])  
predictions.to_csv(“predictions.csv”)

---

### Post #2 — **edddie** | 2022-10-20 19:34 UTC

I solved the issue above with: pd.DataFrame(predictions).to_csv(“predictions.csv”)  
But then comes the next problem. Uploading of the predictions is not working.  
This line of code:  
napi.upload_predictions(“predictions.csv”, model_id=“my model”)  
yields the following error message:  
Specified model_id is not a UUID

---

### Post #3 — **edddie** | 2022-10-20 19:38 UTC

I tried this:

import uuid  
model = str(uuid.uuid4())  
napi.upload_predictions(“predictions.csv”, model_id=model)

This yields the following error message:  
Unable to resolve model from id.

---

### Post #4 — **shatteredx** | 2022-10-20 19:41 UTC _(reply to #3)_

You need to pass your actual model id that you can get from [Numerai](<https://numer.ai/models>)

---

### Post #5 — **edddie** | 2022-10-20 19:47 UTC _(reply to #4)_

Thanks a lot, now I have the next problem:

Invalid submission headers. Headers must be id and prediction.

---

### Post #6 — **shatteredx** | 2022-10-20 20:04 UTC _(reply to #5)_

OK, you need to do something like this to put id and predictions headers in your submission csv:
    
    
    #download live data
    current_round = napi.get_current_round(tournament=8)
    napi.download_dataset("v4/live_int8.parquet", f"live_{current_round}_int8.parquet")
    live_data = pd.read_parquet(f"live_{current_round}_int8.parquet")
    
    #put predictions into live data dataframe
    live_data["prediction"] = model.predict(live_data[feature_names])
    
    #make new dataframe with only the index (contains ids)
    predictions_df = live_data.index.to_frame()
    #copy predictions into new dataframe
    predictions_df["prediction"] = live_data["prediction"].copy()
    
    #csv file will have only id and prediction headers/columns
    predictions_df.to_csv("predictions.csv", index=False)
    submission_id = napi.upload_predictions("predictions.csv", model_id=model_id)
    

I’m sure there’s more elegant code to do this. This is just my amateur hack code.

---

### Post #7 — **edddie** | 2022-10-21 18:50 UTC _(reply to #6)_

Thank you very much, I will try it out! ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=12)
