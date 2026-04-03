---
title: "[Community Release] Automated Numerai Tournament weekly submission pipeline for free, using Azure functions and python"
category: Tournament
url: https://forum.numer.ai/t/community-release-automated-numerai-tournament-weekly-submission-pipeline-for-free-using-azure-functions-and-python/5432
created_at: 2022-05-23T12:53:59.678000+00:00
last_posted_at: 2022-05-23T17:56:04.067000+00:00
posts_count: 2
views: 789
tags: []
---

# [Community Release] Automated Numerai Tournament weekly submission pipeline for free, using Azure functions and python

---

### Post #1 — **papaemman** | 2022-05-23 12:53 UTC

Hello guys,

I know that many people are struggling to set up the Numerai Compute either because they don’t have an AWS account or because numerai-cli seems strange.  
Anyway, I just published a Medium article describing “How I automated my Numerai weekly submission pipeline for free, using Azure functions and python”.

![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/0/0f95de5840ff0771b84ea77cfa42a1e98b4f1614.png) [Medium – 23 May 22](<https://medium.com/@papaemman.pan/how-i-automated-my-numerai-weekly-submissions-pipeline-for-free-using-azure-functions-and-python-9bcf8382af1c> "09:56AM - 23 May 2022")

![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/b/ba31d9578ab6005b70e2d7ddf765e32ce38463de_2_690x171.png)

### [How I automated my Numerai weekly submissions pipeline for free, using Azure...](<https://medium.com/@papaemman.pan/how-i-automated-my-numerai-weekly-submissions-pipeline-for-free-using-azure-functions-and-python-9bcf8382af1c>)

This guide describes how I set up my own weekly submission pipeline from scratch, using Microsoft Azure and python for free. 🚀

Reading time: 8 min read

Here is the source code: [GitHub - papaemman/azure-functions-with-python: A complete guide on developing and deploying Azure functions with Python, using VSCode and Azure extension.](<https://github.com/papaemman/azure-functions-with-python>)

I’d love to know what you think.

Thanks!

---

### Post #2 — **qeintelligence** | 2022-05-23 17:56 UTC

Nice going there!, you can also use for example the webhook from numerai instead of timed triggers so your pipeline will start after the new data is available. I am wondering though if you are in any way limited with the free tier at the moment with the V4 dataset? I can imagine that when using a lot of features of the V4 and also neutralization for example you will run into memory problems.
