---
title: "Discrepancy in versioning between Numerai database and NumerAPI?"
category: Tournament
url: https://forum.numer.ai/t/discrepancy-in-versioning-between-numerai-database-and-numerapi/5168
created_at: 2022-03-29T09:19:07.108000+00:00
last_posted_at: 2022-03-31T21:16:58.398000+00:00
posts_count: 6
views: 957
tags: []
---

# Discrepancy in versioning between Numerai database and NumerAPI?

---

### Post #1 — **perfect_fit** | 2022-03-29 09:19 UTC

The new [v4 version data announcement](<http://forum.numer.ai/t/v4-tournament-data-announcement/5163>) looks great! However, it refers to legacy data (310 features) as “v2”, while [in NumerAPI it is referred to as v1](<https://github.com/uuazed/numerapi/blob/1f64b1e1910a4cba2481736f0c8a7e5690b13195/numerapi/numerapi.py#L564>). The 1050+ features dataset is referred to version 2 in NumerAPI, so v4 would be version 3 in NumerAPI?

Am I missing something or is there a discrepancy between how the Numerai team does versioning and how NumerAPI is structured?

Currently, the API changes are breaking pipelines, so it would be great to have clarity on this.  


[![breaking_numerai_api_example](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/7/74aecd03dfae2017e3345367bcc8cbf4083e52b2_2_690x128.png)breaking_numerai_api_example1115×207 52 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/7/74aecd03dfae2017e3345367bcc8cbf4083e52b2.png> "breaking_numerai_api_example")

---

### Post #2 — **master_key** | 2022-03-29 17:30 UTC

Looking into this now and will get it sorted and reply here, thank you!

---

### Post #3 — **perfect_fit** | 2022-03-29 17:39 UTC _(reply to #2)_

Awesome, thank you for the heads up!

---

### Post #4 — **ark** | 2022-03-29 18:23 UTC

Hey, apologies that your pipeline broke.

In reference to the error you reported:  
Can you provide the NumerAPI code snippet that is throwing this error? AFAIK all of our example predictions and example models are able to download data normally.

In reference to versioning:  
The version you’re referencing is the submission endpoint version not the dataset version. We did, however, recently remove the need for a version argument, so it doesn’t matter what you give NumerAPI during upload. I’ll work on a PR to remove this version argument so it stops causing confusion.

---

### Post #5 — **perfect_fit** | 2022-03-31 03:24 UTC _(reply to #4)_

Hey, thanks for the message. I see now that the error occurs from an assert statement my side. I assert that the filename is in `NumerAPI().list_datasets()`, which breaks because of the v2 and v3 prefixes. Can download files without this assert.

Thanks for the heads up on the submission versioning! So for downloading the version arguments are aligned (v2 = legacy dataset, v3 = 1050+ features dataset)?

---

### Post #6 — **ark** | 2022-03-31 21:16 UTC _(reply to #5)_

There’s no version argument for downloading, just the filename prefixed with `v2/` for legacy and `v3/` for current. `v4/` will be listed upon the v4 data release!
