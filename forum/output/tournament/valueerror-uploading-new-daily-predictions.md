---
title: "ValueError uploading new daily predictions"
category: Tournament
url: https://forum.numer.ai/t/valueerror-uploading-new-daily-predictions/5787
created_at: 2022-10-25T14:20:33.610000+00:00
last_posted_at: 2022-10-25T15:18:17.504000+00:00
posts_count: 8
views: 853
tags: []
---

# ValueError uploading new daily predictions

---

### Post #1 — **corsair** | 2022-10-25 14:20 UTC

using napi.upload_predictions() for predictions file uploading

file top:
    
    
    id,prediction
    n0003aa52cab36c2,0.484971
    n000920ed083903f,0.493027
    n0038e640522c4a6,0.528606
    

error:  
“You must provide predictions for the current live IDs. Make sure you are using the latest live data.”

previous weekly uploading - ok.

---

### Post #3 — **ark** | 2022-10-25 14:26 UTC

Hey, can you provide some more context as to how you are generating predictions? If you’re using a live-only feature data file, then you should have no issues.

---

### Post #4 — **sunkay** | 2022-10-25 14:31 UTC

I have the same problem at first and fixed it by using live data:

napi.download_dataset(“numerai_live_data.parquet”, f"numerai_live_data_{current_round}.parquet")

---

### Post #5 — **corsair** | 2022-10-25 14:36 UTC _(reply to #3)_

I used 2-years python notebook for weekly tournament, long story short:

  * current 340 round
  * numerai_training_data.csv for model training
  * numerai_tournament_data.csv for predicting (full, with all test/validation/live data types)



I’ve tried also tournament.data_type == ‘live’ filtered dataset for predictions - same error.

---

### Post #6 — **kayeffnumeraitor** | 2022-10-25 14:40 UTC

When did you download the live data? The round today opened late, I received the round open mail at 13:26 UTC, so if you downloaded prior to that, you have the wrong file

---

### Post #7 — **corsair** | 2022-10-25 14:52 UTC _(reply to #6)_

after napi.check_new_round() returned true, about 13:02 UTC.

I’ve tried now reload data (after removing downloaded zip archive) - same error.

---

### Post #8 — **shatteredx** | 2022-10-25 15:10 UTC _(reply to #7)_

Hi. I had this same error.

numerai_tournament_data.csv is not updated for daily rounds.

You need to download v2 live data like this:
    
    
    napi.download_dataset('v2/numerai_live_data.csv', f"live_{current_round}_v2.csv")

---

### Post #9 — **corsair** | 2022-10-25 15:18 UTC _(reply to #8)_

Yes, my bad

> *V2, V3, V4 data files and signals universe will be available daily via the API but the legacy dataset zips will only be available for Saturday rounds and not the new weekday rounds.

Great Thanks!
