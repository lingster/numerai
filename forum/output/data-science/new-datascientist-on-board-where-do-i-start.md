---
title: "New DataScientist on board - Where do I start?"
category: Data Science
url: https://forum.numer.ai/t/new-datascientist-on-board-where-do-i-start/6762
created_at: 2023-10-31T12:53:01.258000+00:00
last_posted_at: 2025-04-15T05:15:56.816000+00:00
posts_count: 4
views: 2423
tags: []
---

# New DataScientist on board - Where do I start?

---

### Post #1 — **nolyzlel** | 2023-10-31 12:53 UTC

Hello dear community.

I am completely new to the topic of stock market prediction.  
I understand the concept of Numerai and have worked as a Data Scientist for a tech company for multiple years. My specialties are RNNs, so I know a bit about time series.

I already build a classical LSTM model and let it run on the medium numerai dataset, however the results are not great.

Now I am asking for any kind of tips to get better.

As far as I understood the most popular model architectures are XGboost, Transformer and RNNs, right?  
Is there any github repo for a model that is performing decently?  
Any other ressources that you can recommend?

Thanks in advance!

---

### Post #2 — **zoliveres** | 2023-11-02 08:26 UTC

I can’t tell you what you’ll consider useful, but here’s what I considered useful, when I started (which was 4 months ago ![:stuck_out_tongue:](http://forum.numer.ai/images/emoji/twitter/stuck_out_tongue.png?v=12) ):

  1. I think you should go trough the [Numerai Example Scripts](<https://github.com/numerai/example-scripts>), that would guide you trough the whole process of training, submitting, etc.
  2. Then Check the Benchmark models of Numerai, this is really fresh information: [Benchmark Models - Numerai Tournament](<https://docs.numer.ai/numerai-tournament/benchmark_models>)
  3. Watch the [Numerai](<https://www.youtube.com/@Numerai/playlists>) content on YouTube, specifically the Quant Club and the Fireside chats to give you better context.
  4. Watch [StudyM8’ts Numerai Series](<https://www.youtube.com/watch?v=YeEpOm5JjFk&list=PLlOOibxKpQUlM28lqa4TiUTJ5gjLG5haQ>)
  5. Check the Grid Search article: [Super Massive LGBM Grid Search](<http://forum.numer.ai/t/super-massive-lgbm-grid-search/6463>) and in general, just search the forum if you happen to have questions
  6. Just hop into Discord, a lot of smart people discussing so many things, I picked up a lot there
  7. Marcos López de Prado: Advances in Financial Machine Learning book will give you so many new concept and basic understanding on what Numerai does or even Finance



As per what models are considered effective?  
I can’t really tell, most people are using GBT, there are a few people active on Discord who are using, Genetic Algorithms, Random Forests, Transformers, RNNs, but not much people are conversing about LSTMs.

---

### Post #3 — **nolyzlel** | 2023-11-02 15:43 UTC _(reply to #2)_

Amazing, thank you. That helps a lot ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=12) ![:+1:](http://forum.numer.ai/images/emoji/twitter/+1.png?v=12)

---

### Post #8 — **ruhiparveen** | 2025-04-15 05:15 UTC

Hey and welcome to Numerai!

Since you already have experience with RNNs and time series, you’re in a good spot—but Numerai is a bit different from classic time series problems. Even though the data has “eras” (which look like time), it’s more of a **tabular classification problem** than a true time series one. So LSTMs often don’t shine here.
