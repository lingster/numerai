---
title: "Joblib or pickel model files into compute?"
category: Tournament
url: https://forum.numer.ai/t/joblib-or-pickel-model-files-into-compute/3335
created_at: 2021-05-17T18:37:14.209000+00:00
last_posted_at: 2021-11-22T20:46:06.232000+00:00
posts_count: 3
views: 859
tags: []
---

# Joblib or pickel model files into compute?

---

### Post #1 — **elon_ai** | 2021-05-17 18:37 UTC

I searched through documentation/tutorials and couldn’t see anything about using an existing model for predicting on compute node. I’m hoping to avoid retraining, and just ssh this file to the AWS EC2 docker instance i set up for Compute.  
Any thoughts or help greatly appreciated!  
Thanks

---

### Post #2 — **lucky_chicken** | 2021-05-17 22:20 UTC

If is it just the model file, you can include it in the docker container.

---

### Post #3 — **pumplerod** | 2021-11-22 20:46 UTC

I, generally, keep a version of my model stored on aws S3 storage, then use boto3 to load the model from the compute node. Perhaps this would work for you as well. What I like about it is that I can make adjustments to my model and upload a new version to aws without having to wrestle with the compute node setup again. By far the most difficult aspect of this tournament, I’ve found, is to get the compute node setup.
