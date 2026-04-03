---
title: "Validation data missing ids?"
category: Tournament
url: https://forum.numer.ai/t/validation-data-missing-ids/8241
created_at: 2026-02-07T16:37:34.780000+00:00
last_posted_at: 2026-02-09T16:18:16.711000+00:00
posts_count: 2
views: 59
tags: []
---

# Validation data missing ids?

---

### Post #1 — **fasec** | 2026-02-07 16:37 UTC

Hi! I’m trying to get back to Numerai after a long time. I noticed that there are no ids in the validation data. It’s just [None] when I try to print index or id fields. Is this some bug or is there a reason why ids have been stripped from validation data? Maybe I’m missing something here.

I’m asking about the ids because I want to diagnose my new models using the validation data. The diagnostic tool of course doesn’t accept the CSVs with empty id fields.

---

### Post #2 — **svendaj** | 2026-02-09 16:18 UTC

`validation.parquet` file (there are no CSV validation files) have `id` column used as index. So, if you are converting it to CSV, you should do it like
    
    
    valid_df = pandas.read_parquet(path_to_validation_parquet)
    valid_df.to_csv(path_to_validation_csv, index=True)
    

Please mention that `index` param is default `True`, so it could be omitted.
