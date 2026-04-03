---
title: "Self supervised learning on pseudo labels"
category: Data Science
url: https://forum.numer.ai/t/self-supervised-learning-on-pseudo-labels/3371
created_at: 2021-05-21T06:53:53.952000+00:00
last_posted_at: 2021-10-05T05:55:58.468000+00:00
posts_count: 3
views: 1014
tags: []
---

# Self supervised learning on pseudo labels

---

### Post #1 — **nyuton** | 2021-05-21 06:53 UTC

Hi,

I would like to share one of my new experiemnts. I tried to pre-train a NN on pseudo labels. I took the predictions of my ensemble and traind the model on them. To my surprise it achieves higher validation CORR than models trained on the training data.

What I did:

  * get predictions on the tournament data (test set)
  * cut out the validation part
  * minmax scale the predictions
  * train NN on the “new” dataset
  * fine-tune on training set



Validation score is great and the first live results are also promising.  
I guess good quality predictions on the test set are key to this exercise.  
The new dataset gives great validation corr even without fine-tuning on the training set.

Have a great day!

---

### Post #2 — **sunkay** | 2021-10-05 01:58 UTC

Pseudo labels would be very different from the origin labels even if you minmax scale them.

I found this in rocket chat:  


[![tdrygxfhfghd](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/2/206f508d1ec0feb727e2e69ba2c28fbcf11aaae3.png)tdrygxfhfghd490×155 8.04 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/2/206f508d1ec0feb727e2e69ba2c28fbcf11aaae3.png> "tdrygxfhfghd")

I think binning pseudo labels in [0,0.25,0.5,0.75,1.0] would be better and I would start my experiemnts too.

---

### Post #3 — **sirbradflies** | 2021-10-05 05:55 UTC

Hi Nyuton, I just saw this post but thanks for sharing this.  
Any thought on why that happened? Is the trend continuing by the way?

It seems that you generated synthetic dataset from the test features and that helps the overall training. I still struggle to see how the test predictions of a model trained on the training dataset could squeeze more information useful to improve the model performance.  
I guess however this is more of a philosophical question about synthetic data itself…
