---
title: "Example script failure in Colab"
category: Tournament
url: https://forum.numer.ai/t/example-script-failure-in-colab/4230
created_at: 2021-10-01T15:45:00.396000+00:00
last_posted_at: 2021-10-01T18:35:38.864000+00:00
posts_count: 2
views: 595
tags: []
---

# Example script failure in Colab

---

### Post #1 — **thekizoch** | 2021-10-01 15:45 UTC

Just wishing to verify my issue:

When I copy the example script straight from github, and run it in Colab Pro (25 GB of RAM), the example_model.py fails as the instance crashes due to RAM. See here: <https://prnt.sc/1uddvgy>

Is it that I need even more RAM? or do I have another issue?

Thanks in advance.

---

### Post #2 — **shatteredx** | 2021-10-01 18:35 UTC

First, you can try using the int8 data files which use less RAM:

numerai_training_data_int8.parquet  
numerai_tournament_data_int8.parquet  
numerai_validation_data_int8.parquet

You might still need more RAM though. I think my model uses somewhere between 28 to 38 GB of memory.
