---
title: "Midnight Data Release"
category: Announcements
url: https://forum.numer.ai/t/midnight-data-release/6954
created_at: 2024-01-13T01:18:03.383000+00:00
last_posted_at: 2024-01-24T04:12:51.289000+00:00
posts_count: 3
views: 1901
tags: []
---

# Midnight Data Release

---

### Post #1 — **master_key** | 2024-01-13 01:18 UTC

[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/1/140347f75772e0e7e23a272f641311430aedb44a_2_502x500.jpeg)1600×1594 354 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/1/140347f75772e0e7e23a272f641311430aedb44a.jpeg>)

# Overview

The Midnight dataset is out now. Midnight contains 244 new features for a total of 2376 features.

Models trained on Midnight outperform models trained on any previous dataset in nearly every measurable dimension.

These 244 features are created out of completely new data sources, and so are very complementary to the existing features despite the relatively small number of features added.

# Model Performance

Here we can see the performance improvement of Midnight over all previous datasets.

[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/9/9eb2e495778e3c95381881b8ad049b7af732f646_2_690x478.jpeg)1600×1110 162 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/9/9eb2e495778e3c95381881b8ad049b7af732f646.jpeg>)

In particular, Midnight improves on Rain consistently over the last 300 eras.

Here is the cumulative correlation difference between a Midnight Model and a Rain Model.

[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/e/e98047132e0135ef1685d01f1b53574348319550_2_690x481.png)1600×1116 111 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/e/e98047132e0135ef1685d01f1b53574348319550.png>)

# Model Uploads and Benchmark Models

Going forward, Model Uploads will only support the Midnight dataset.

Model Uploads now supports the live_benchmark_models file, so you can incorporate those into your models.

Along with this, there have been several Midnight (v43) Benchmark Models added to the benchmark model files and [Benchmark Model Account](<https://numer.ai/~benchmark_models>)

Learn more about Benchmark Models [here](<http://forum.numer.ai/t/benchmark-models/6754>).  
See an example of how to use Benchmark Models in model uploads [here](<https://github.com/numerai/example-scripts/blob/master/target_ensemble.ipynb>).

We’ve also pushed some other updates to the Model Uploads runtime environment.

Here is a quick change log:

  * add support for passing in live_benchmark_models to the predict function
  * add more testing and improve reliability
  * package updates: 
    * add mlxtend
    * add statsmodels
    * add tensorflow-decision-forests
    * update tensorflow and supporting packages (ie keras) to 2.15.0



Existing models in Model Uploads will continue working normally.

# Removing Targets

We’ve kept many targets around for years now, typically only ever adding targets. This is because, in the past, we expect all of the targets we make to be different and additive to all of the previous targets.

However as our understanding of the problem has evolved, our targets have gotten more and more advanced, to the point that we believe our newer targets are strictly better than several of our older targets.

For this reason, Midnight removes 16 target columns which we don’t think will be beneficial to train on anymore, even in the context of an ensemble with minimal weight on these targets.

# What Next

We’ve been moving at a crazy pace for the last year or so, releasing new data or targets or payouts every couple of months, and we know some of you have whiplash trying to keep up.

There are no other target or data releases on our immediate calendar.

Our mindset has been to get everything exactly how we want it by 2024, and then to give you all time to work. As always, we can’t guarantee that we won’t find something urgent tomorrow that we have to update as soon as we can.

However, if you’re one of those people who has been hesitant to get to work for fear of imminent change, or if you’re waiting for a cue to spend the time to build your best model ever, then this is that cue. Download Midnight and start modeling.

You can get started training a model with Midnight data here: [example-scripts/example_model.ipynb at master · numerai/example-scripts · GitHub](<https://github.com/numerai/example-scripts/blob/master/example_model.ipynb>)  
Download the data from the website or from the API here:  
<https://numer.ai/data>

We hope you find the new features useful. See you on the leaderboard.

---

### Post #2 — **eleven_sigma** | 2024-01-13 11:16 UTC

I am concerned about how much overfitting is being introduced into the data by adding and selecting responses and adding predictors, many of which use information from the entire period up to era 574. Initially, if information from eras after 574 are not used, everything seems correct, but the testing and selection process of promising predictors and targets itself introduces a selection bias that generates overfitting. I hope Numerai has taken all of this into account.

---

### Post #4 — **andralienware** | 2024-01-24 04:12 UTC

This may be a stupid question, but there used to be targets that took on more than 5 different values and my pipeline sees that all targets now only take on 5 values, is this the case? (And is it likely that in the future all targets will take on 5 different values (excluding missing)). There are also no more missing values for features (filled in as 2), right?
