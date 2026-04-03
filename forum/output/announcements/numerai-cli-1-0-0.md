---
title: "Numerai CLI 1.0.0"
category: Announcements
url: https://forum.numer.ai/t/numerai-cli-1-0-0/6796
created_at: 2023-11-16T17:10:07.360000+00:00
last_posted_at: 2023-11-20T11:10:05.589000+00:00
posts_count: 2
views: 799
tags: []
---

# Numerai CLI 1.0.0

---

### Post #1 — **ark** | 2023-11-16 17:10 UTC

Over 2.5 years ago, my first project here at Numerai was to overhaul the (at the time) only automation tool available to our community. I released [Numerai CLI 0.3.0](<http://forum.numer.ai/t/numerai-cli-0-3-0/2627>) and with it came a flood of requests for bug fixes, support for other data providers, better customization, deeper integration with cloud services, etc.

Several versions of Numerai CLI (aka Compute Heavy) have become available since then including Compute Lite, which recently was replaced with [Model Uploads](<https://docs.numer.ai/numerai-tournament/submissions/model-uploads>) \- a free, zero-setup automation method that comes at a cost: customization and control. Many users request features or packages that take us a month or longer to implement.

Compute Heavy remains the automation solution where you are in full control, and is [open-sourced](<https://github.com/numerai/numerai-cli>) so the community can keep the architecture modern by adding tooling to support modern modeling methods. Today, we are announcing the introduction of some major improvements:

  * Add support for Google Cloud
  * Add support for Microsoft Azure
  * Switch AWS from ECS to Batch



With Numerai CLI v1.0, you have more control than ever, including choice over cloud provider and - in the case of AWS - resource consumption.

To upgrade your version today, run
    
    
    pip install --upgrade numerai-cli
    

If you’d like to use GCP follow the steps [here](<https://github.com/numerai/numerai-cli/blob/master/docs/gcp_setup_guide.md>), then run
    
    
    numerai setup --provider gcp
    

If you’d like to use Azure follow the steps [here](<https://github.com/numerai/numerai-cli/blob/master/docs/azure_setup_guide.md>), then run
    
    
    numerai setup --provider azure
    

If you’d like to use the new AWS Batch architecture, you’ll need to replace your terraform and your nodes using:
    
    
    numerai setup --provider aws
    numerai destroy-all
    numerai node -m [model-name-1] config [options]
    numerai node -m [model-name-1] deploy
    numerai node -m [model-name-2] config [options]
    numerai node -m [model-name-2] deploy
    ...
    

AWS Batch offers a host of benefits including custom instance sizing, queueing, auto-retries, and more. It’s what we use for Model Uploads and now you can set up similar architecture in your own environment.

---

### Post #2 — **ia_ai** | 2023-11-20 11:10 UTC

Yeah, I remember the release of CLI 0.3.0 ![:wink:](https://emoji.discourse-cdn.com/twitter/wink.png?v=13)

<https://twitter.com/matlabulous/status/1377739948703555587>

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/c/cf6a4b512f906797c41318fbb9d40e1b5ca3790a_2_393x500.jpeg)image595×756 92.8 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/c/cf6a4b512f906797c41318fbb9d40e1b5ca3790a.jpeg> "image")
