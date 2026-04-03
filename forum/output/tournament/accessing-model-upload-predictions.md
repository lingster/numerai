---
title: "Accessing Model Upload predictions?"
category: Tournament
url: https://forum.numer.ai/t/accessing-model-upload-predictions/7218
created_at: 2024-04-04T11:09:16.282000+00:00
last_posted_at: 2024-04-04T14:25:36.732000+00:00
posts_count: 2
views: 348
tags: []
---

# Accessing Model Upload predictions?

---

### Post #1 — **rpica** | 2024-04-04 11:09 UTC

Is it possible to retrieve the predictions calculated by a model that we uploaded (to [Model Uploads](<https://docs.numer.ai/numerai-tournament/submissions/model-uploads>))?

The use case is to make an ensembling (a meta model) without repeating calculations.

If so, can the predictions be accessed by another Model Upload? It would be important that the one mixing predictions runs after, of course.

---

### Post #2 — **wigglemuse** | 2024-04-04 14:25 UTC

I believe current answer is yes to the first (you can now get your preds back from the api) and no to the second – model uploads need to be totally self-contained so far I think (only using the live data).
