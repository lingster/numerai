---
title: "Daily Signals upload"
category: Tournament
url: https://forum.numer.ai/t/daily-signals-upload/6585
created_at: 2023-07-27T10:23:12.228000+00:00
last_posted_at: 2024-08-26T18:46:07.707000+00:00
posts_count: 5
views: 986
tags: []
---

# Daily Signals upload

---

### Post #1 — **stepan** | 2023-07-27 10:23 UTC

Hi all!  
There is a question for daily upload in Numerai Signals.

I am downloading last_universe from this [link]((<https://numerai-signals-public-data.s3-us-west-2.amazonaws.com/latest_universe.csv>) and when I try to submit the prediction I get an error  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/f/f2e5c96c735ef8a9df3188abc416419afbaaca6f_2_690x114.jpeg)image1280×212 47.5 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/f/f2e5c96c735ef8a9df3188abc416419afbaaca6f.jpeg> "image")

But you can see that my submit file has all required columns.  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/a/ae589c02c178fd8355313edfcb53d67fac0866fe_2_502x500.jpeg)image772×768 81 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/a/ae589c02c178fd8355313edfcb53d67fac0866fe.jpeg> "image")

I can submit a prediction when I download the universe from this [link] (<https://numerai-signals-public-data.s3-us-west-2.amazonaws.com/latest.csv>) with validation samples and it’s a bit weird .

Tell me, please, how to do it right?

---

### Post #2 — **rdr91h** | 2023-07-28 06:55 UTC

I think bloomberg_ticker has to be the index, and you have to drop ‘Unnamed:0’ column before upload

---

### Post #3 — **degerhan** | 2023-07-28 07:59 UTC

I think adding a `data_type` column might resolve your issue. Alternatively, remove `friday_date` and the numeric index, keeping only `bloomberg_ticker` and `signal`.

See [submissions](<https://docs.numer.ai/numerai-signals/signals-overview#submissions>):

  * “Submissions with only two columns are assumed to correspond to the current `live` time period.”
  * Submissions that include the `validation` time period must include two extra columns: `friday_date` and `data_type`

---

### Post #4 — **n1k** | 2023-07-28 17:40 UTC

Guys, I have the same problem. And options that were defined above have not worked ((

---

### Post #7 — **datahunter** | 2024-08-26 18:46 UTC _(reply to #4)_

Were you able to fix it, btw?
