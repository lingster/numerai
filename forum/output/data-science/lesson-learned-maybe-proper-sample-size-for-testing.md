---
title: "Lesson Learned (maybe) - Proper Sample Size for Testing"
category: Data Science
url: https://forum.numer.ai/t/lesson-learned-maybe-proper-sample-size-for-testing/3132
created_at: 2021-04-29T16:21:13.742000+00:00
last_posted_at: 2021-04-29T18:10:17.074000+00:00
posts_count: 2
views: 1054
tags: []
---

# Lesson Learned (maybe) - Proper Sample Size for Testing

---

### Post #1 — **one5hot76** | 2021-04-29 16:21 UTC

First off, I am more of a hobbyist when it comes to AI, so I could be wrong. However, it seems to me that if I train a neural net on a small sample size and take the best weights that it is similar to assuming that I should only use the method in school where I was on a “winning streak” with X number of questions on my tests. It would also seem that the smaller the sample size, the shorter term focus of the model and vice versa. The larger the sample size, the longer term focus of the model. Its just a theory for me, but like I said this is more of a hobby. I haven’t done all the formal study that someone else may have. Any and all enlightenment is welcome. Thanks.

---

### Post #2 — **ml_is_lyf** | 2021-04-29 18:10 UTC

Yeah exactly. Your post actually reminded me of one of Andrew Ng’s videos in his Deep Learning specialization:

![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/c175b0ccf101d18f525be8ece457358086ac8a40.png) [Coursera](<https://www.coursera.org/lecture/neural-networks-deep-learning/why-is-deep-learning-taking-off-praGm>)

![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/ad60f30d38873d3168c758f56c6cc48ad8899944_2_690x361.jpeg)

### [Why is Deep Learning taking off? - Introduction to Deep Learning | Coursera](<https://www.coursera.org/lecture/neural-networks-deep-learning/why-is-deep-learning-taking-off-praGm>)

Video created by DeepLearning.AI for the course "Neural Networks and Deep Learning". Analyze the major trends driving the rise of deep learning, and give examples of where and how it is applied today.

As a TLDR this graph basically sums up the whole video

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/66282c1449f2bc36c74f94951cd50624cf2c9956.png)image480×234 60.9 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/66282c1449f2bc36c74f94951cd50624cf2c9956.png> "image")

So the more data you have, typically the more performant and bigger you can make your neural net. We’re definitely in the small neural net category in this competition, so make sure to utilize it well.

Notice the point about traditional learning algorithms, they tend to work better with less data. Seems like people are getting some good success with training on a small number of eras using traditional methods like xgboost, for instance look at BOR0 ranked number 2 at the time of writing:

![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/e/e2ed550eb9d7dd2db4d49e519b2f03cc1c053dbb.png) [numer.ai](<https://numer.ai/bor0>)

### [Numerai](<https://numer.ai/bor0>)

Even more important than having a large training set is having a large validation set. If you judge your model’s performance over a small number of eras, you’re not going to get a good idea of how your model really performs in the long run. That’s why personally I use cross-validation for the vast majority of my models now.
