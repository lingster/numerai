---
title: "Advice on setup for training new models"
category: Data Science
url: https://forum.numer.ai/t/advice-on-setup-for-training-new-models/7066
created_at: 2024-02-29T12:52:10.274000+00:00
last_posted_at: 2024-03-03T23:15:42.546000+00:00
posts_count: 2
views: 522
tags: []
---

# Advice on setup for training new models

---

### Post #1 — **nickthesailor** | 2024-02-29 12:52 UTC

Hey everyone!

I’m new to the Numerai competition and I’m eager to explore ways to work with medium to large Numerai datasets more efficiently. I’m currently considering using AWS EC2 instances or Amazon SageMaker for this purpose. My primary goals are to improve model training speed and having a more robust setup where I don’t have to load the dataset from the API every time I want to continue my research etc.

Any advice would be greatly appreciated!

---

### Post #2 — **autratec** | 2024-03-03 23:15 UTC

Assuming your referring to tournament, you don’t need to load your data every time though api. You can just store your data locally and use them for any kind of test and comparison.
