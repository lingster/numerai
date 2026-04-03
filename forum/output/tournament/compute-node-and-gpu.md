---
title: "Compute Node and GPU"
category: Tournament
url: https://forum.numer.ai/t/compute-node-and-gpu/4536
created_at: 2021-11-22T20:50:50.100000+00:00
last_posted_at: 2021-11-24T04:18:22.217000+00:00
posts_count: 3
views: 762
tags: []
---

# Compute Node and GPU

---

### Post #1 — **pumplerod** | 2021-11-22 20:50 UTC

I’ve recently begun developing models which rely more heavily on the GPU and I’d like to have them integrated into the compute node so that they’ll run automatically each week.

Is there any way to get an instance on the aws/terraform network which includes GPU support?

---

### Post #2 — **rtachinardi** | 2021-11-24 04:10 UTC

Check out AWS EC2 instances such as the P3, G3, P4 and G4 series. You should also take a look at the machines and services provided by Google Cloud Platform, they are really strong in the Machine Learning space and provide a lot of free credits.

---

### Post #3 — **pumplerod** | 2021-11-24 04:18 UTC _(reply to #2)_

thank you [@rtachinardi](</u/rtachinardi>), however are these instances able to be used with the numerai compute node setup? I thought, when using the numerai-cli tool we only had a small list of options, of which mem-lg being the most robust, but no GPU support. Is there a way to configure with one of the other options you mention when configuring a node?
    
    
    numerai node -m [MODEL NAME] -s config -s mem-lg
