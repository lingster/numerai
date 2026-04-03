---
title: "Live prediction ids do not match. IDs must match current tournament data exactly, including ordering. Make sure you are using the latest tournament data"
category: Tournament
url: https://forum.numer.ai/t/live-prediction-ids-do-not-match-ids-must-match-current-tournament-data-exactly-including-ordering-make-sure-you-are-using-the-latest-tournament-data/5060
created_at: 2022-03-09T11:08:43.112000+00:00
last_posted_at: 2022-03-09T19:37:23.809000+00:00
posts_count: 4
views: 635
tags: []
---

# Live prediction ids do not match. IDs must match current tournament data exactly, including ordering. Make sure you are using the latest tournament data

---

### Post #1 — **nyuton** | 2022-03-09 11:08 UTC

Hi,

I need help…  
I download the latest live dataset through the api  
napi.download_dataset(‘numerai_live_data_int8.parquet’, ‘numerai_live_data_int8.parquet’)

Then I make the prediction and upload the results.  
Same IDs, same order.

Still I get this error message:  
`Live prediction ids do not match. IDs must match current tournament data exactly, including ordering. Make sure you are using the latest tournament data.`

Does anyone have a clue why???

Thanks

---

### Post #2 — **wigglemuse** | 2022-03-09 13:31 UTC

You still have to upload the test set predictions too (for the time being). Are you only uploading live set predictions?

---

### Post #3 — **rigrog** | 2022-03-09 17:48 UTC

Your command doesn’t explicitly pass a round number, so maybe it ran with the wrong round number.

I believe there’s a keyword parameter you can pass, something like “round_number = 306”.

---

### Post #4 — **rappenlager** | 2022-03-09 19:37 UTC

Round 306 contains era1000 (the first 4-digit number), this breakes my legacy pipeline which ignores era1000, and this results in the same error message you got.
