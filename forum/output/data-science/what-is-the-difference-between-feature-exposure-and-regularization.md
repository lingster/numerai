---
title: "What is the difference between feature exposure and regularization?"
category: Data Science
url: https://forum.numer.ai/t/what-is-the-difference-between-feature-exposure-and-regularization/5713
created_at: 2022-09-24T08:22:48.075000+00:00
last_posted_at: 2022-09-24T11:13:06.550000+00:00
posts_count: 2
views: 1093
tags: []
---

# What is the difference between feature exposure and regularization?

---

### Post #1 — **ryo_matsuzaka** | 2022-09-24 08:22 UTC

Hello. I learned the concept of **feature exposure** thanks to several threads and a script:

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/b/22d042/48.png) [An introduction to feature neutralization / exposure](<http://forum.numer.ai/t/an-introduction-to-feature-neutralization-exposure/4955>) [Tournament](</c/tournament/7>)

> Hello everyone, From my research on feature neutralization and feature exposure I’ve prepared a basic introduction note for myself and think it may help start-off anyone researching the topic, hope it’s helpful. References: this post is basically a mush-up of the following links [Our Experience with Numerai. Introduction to Numerai | by Saahil Barai | Analytics Vidhya | Medium](<https://medium.com/analytics-vidhya/our-experience-with-numerai-2b0777acc12e>) [Model Diagnostics: Feature Exposure - Data Science - Numerai Forum](<http://forum.numer.ai/t/model-diagnostics-feature-exposure/899>) [What exactly is neutralization? - Data Scie…](<http://forum.numer.ai/t/what-exactly-is-neutralization/2016/7>)

![](http://forum.numer.ai/user_avatar/forum.numer.ai/jrb/48/2767_2.png) [Model Diagnostics: Feature Exposure](<http://forum.numer.ai/t/model-diagnostics-feature-exposure/899>) [Data Science](</c/data-science/5>)

> This post is about feature exposure. I’ll try explain the intuition behind feature exposure, and why it matters. I’ll also discuss ways to reduce feature exposure (regularization and feature neutralization). Feature Exposure The idea behind feature exposure is as follows: Any supervised ML model from a very high level perspective, is a function that takes an input feature vector (X) and outputs a prediction (y). At training time, the model learns a mapping between input features and the predict… 

[github.com](<https://github.com/numerai/example-scripts/blob/838bfd1788feaf40362d6bedb3e4683832a9dbb1/utils.py#L106>)

#### [numerai/example-scripts/blob/838bfd1788feaf40362d6bedb3e4683832a9dbb1/utils.py#L106](<https://github.com/numerai/example-scripts/blob/838bfd1788feaf40362d6bedb3e4683832a9dbb1/utils.py#L106>)
    
    
          
    
    
              
        96.         # To be consistent for all targets, let's embargo everything by 60/5 == 12 eras.
    
              
        97.         train_split = [e for e in train_split_not_embargoed if
    
              
        98.                        abs(int(e) - test_split_max) > embargo and abs(int(e) - test_split_min) > embargo]
    
              
        99.         train_splits.append(train_split)
    
              
        100. 
              
        101.     # convenient way to iterate over train and test splits
    
              
        102.     train_test_zip = zip(train_splits, test_splits)
    
              
        103.     return train_test_zip
    
              
        104. 
              
        105. 
              
        106. def neutralize(df,
    
              
        107.                columns,
    
              
        108.                neutralizers=None,
    
              
        109.                proportion=1.0,
    
              
        110.                normalize=True,
    
              
        111.                era_col="era"):
    
              
        112.     if neutralizers is None:
    
              
        113.         neutralizers = []
    
              
        114.     unique_eras = df[era_col].unique()
    
              
        115.     computed = []
    
              
        116.     for u in unique_eras:
    
          
    
        

When I saw the concepts, I remembered **regularization**.  
The goal and basic concept of **feature exposure** is the same as the ones of **regularization**?

---

### Post #2 — **taori** | 2022-09-24 11:13 UTC

In the post you linked, **regularization** and **feature neutralization** are two different methods used to reduce **feature exposure**.

**regularization** is used during model training to prevent the model from giving too much importance (and consequently exposure) to single features. This method depends on the particular model/algorithm in use and different models/algorithms might have (or not have) different parameters that control regularization.

**feature neutralization** is used on the model predictions (and so after training). It doesn’t depend on the model/algorithm in use. This method computes the exposure (e.g. using linear regression) of the predictions to a set of risky features and then removes this exposure while keeping the residuals.

Broadly speaking that is how I see the relationship between the two technincs.
