---
title: "Per-Model Webhooks"
category: Announcements
url: https://forum.numer.ai/t/per-model-webhooks/2242
created_at: 2021-03-08T17:18:17.524000+00:00
last_posted_at: 2021-03-08T17:18:17.604000+00:00
posts_count: 1
views: 1461
tags: []
---

# Per-Model Webhooks

---

### Post #1 — **ark** | 2021-03-08 17:18 UTC

Numerai is landing an important change to how we do webhooks in preparation for the big Compute 0.3.0 release coming at the end of Q1 2021 (stay posted for the official release announcement coming soon). This change accompanies some amazing UI changes to the models page pushed recently, adding a fourth button to each model that allows you to configure that model’s webhook.

![webhook-demo](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/8adc574768b55c3ed15392b5cd08fe8fa3a96e93.gif)

Previously, our data scientists were forced to run all models from a single webhook, which is a problem if you have 15 models and each has a long run time. It’s a production nightmare to debug which model failed and why. Per-model webhooks won’t break your compute node, so if your account has a webhook configured, it has been moved to your oldest model and will still trigger at the same time every weekend.

This change now allows you to modularize your code and only run the model you want with that webhook. This means models can now run in parallel, resources can be used more efficiently, issues can be pinpointed to an individual model, and we can be prepared to Build the Numerai Network.
