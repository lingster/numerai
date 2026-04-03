---
title: "A few simple newb questions"
category: Tournament
url: https://forum.numer.ai/t/a-few-simple-newb-questions/4653
created_at: 2021-12-20T18:52:07.785000+00:00
last_posted_at: 2021-12-21T22:39:24.751000+00:00
posts_count: 4
views: 854
tags: []
---

# A few simple newb questions

---

### Post #1 — **blinkin** | 2021-12-20 18:52 UTC

Hi everyone! I’m fairly new to Numerai, and am working on getting my first model up and running. I’d like to try the NN approach, for my own learning, though I know XGB and other methods are more popular. I’m confused about a couple of things in the dataset:

  1. The “ID”. Is that unique to each asset & consistent throughout eras? Or in the obfuscation does each asset get a unique ID every new era? Just curious if those could be used to construct a history of a particular asset and train a time-based RNN or something

  2. The “target” values we are training to are binned to one of 5 values (or 7 values for some targets), i.e. 0, .25, .5, .75, 1. How should I construct the output of my neural network when predicting targets for submission? Should they be:  
a. Also binned to match the training set bins? So construct a multi-class classifier that only outputs 0, .25, etc.  
b. Or a continuous prediction between 0 and 1. Most of the examples I’ve seen use a Sigmoid activation as the final layer to achieve this.

  3. I’ve noticed my starter models VERY quickly overfit compared to validation. I’m not subsampling the eras as of yet, so is this likely the main cause of the overfitting? Any good strategies for tackling this? Is shuffling the data in my DataLoader a good first step? Or do I need to subsample? Do you use all 4 eras every epoch? Or cycle eras through epochs? Or throw out 3/4 of the data altogether?




Thanks for any tips you’re willing to offer!

---

### Post #2 — **rigrog** | 2021-12-20 20:27 UTC

1. If/when the same stock appears in several eras, the id’s will differ as randomly as all the other id’s.

  2. Your predictions can be any real number x, 0 < x < 1\. Because your predictions are scored ONLY by their ordering: you don’t want your predictions in 5 or 7 bins, since you can’t control how the 5 or 7 massive multiway ties will be broken (Numerai will break them for you, according to their order in the text file).

  3. [opinion] that overfitting is a consequence of all the given target data being years out of date. That _may_ be about to change, on 12/25/21.

---

### Post #3 — **blinkin** | 2021-12-21 22:16 UTC _(reply to #2)_

Got it, thank you! That sounds a bit different than what I was picturing, super helpful. So it sounds like our “target” numbers are more like a rank ordering prediction of stocks from best to worst, rather than a more direct prediction of performance?

Looking forward to the newest data, I hope that helps. Didn’t we get a bunch of new data this summer as well? Or was that mostly old data, just with extra features and rows interspersed?

---

### Post #4 — **rigrog** | 2021-12-21 22:39 UTC _(reply to #3)_

According to the latest post on “# announcements” (in the chat room), the newest data was just put off until March. It is to include a few new features, and “all of the test targets”.

There was new (“super massive”) data released in late summer. It changed the number of features from 310 to 1050, and also added rows (mostly, I think, by making four era-specific rows, out of each “train” or “validation” row). But the 1050 features seem to be quite redundant: [I tried to put a hyperlink here, to the “tips and tricks” github page. see the graph that follows “Out[7]” ].
