---
title: "Neural Networks for Numerai Signals"
category: Signals
url: https://forum.numer.ai/t/neural-networks-for-numerai-signals/6334
created_at: 2023-05-01T15:51:37.466000+00:00
last_posted_at: 2023-05-05T16:23:54.315000+00:00
posts_count: 3
views: 1021
tags: []
---

# Neural Networks for Numerai Signals

---

### Post #1 — **mikamiyusuke** | 2023-05-01 15:51 UTC

As you may know, NN model doesn’t perform well for tabular data which consists of technical indicators, rather than that, decision trees outperform in most cases.

Also, at least in my experimental environment, NN’s performance on raw stock price data is terrible to solve Numerai Signals.

I know there are some papers and articles that support this fact with great experiments and I already tried NN approaches on raw price data and technical indicators, then unfortunately I completely agree with these facts.

**However, I don’t want to stop to believe the power of Neural Networks, I want to explore their extraordinal capability to move forward to the next step.**

Especially, I’m now focusing on representation learning for time series data, like, [TS2Vec](<https://arxiv.org/pdf/2106.10466.pdf>), [Multi-Task Self-Supervised Time-Series Representation Learning](<https://www.researchgate.net/publication/368934981_Multi-Task_Self-Supervised_Time-Series_Representation_Learning>), [Unsupervised Time-Series Representation Learning with Iterative Bilinear Temporal-Spectral Fusion](<https://proceedings.mlr.press/v162/yang22e/yang22e.pdf>), [FEAT: A GENERAL FRAMEWORK FOR FEATURE-AWARE MULTIVARIATE TIME-SERIES REPRESENTATION LEARNING](<https://openreview.net/pdf?id=n9iRY8XFfXW>).  
Can we use or modify these ideas for stock price?

So here is [an idea posted on Reddit](<https://www.reddit.com/r/deeplearning/comments/1330i60/selfsupervised_learning_for_stock_return/?utm_source=share&utm_medium=web2x&context=3>), however, my brain is very limited, so I want to hear other approaches with NN which probably works for stock price data.

I know these methods cannot be shared with other people because they cannot keep their originality, however, I think it’s good to discuss a new approach.

---

### Post #2 — **degerhan** | 2023-05-02 13:22 UTC

I don’t use Neural Nets or a time series approach for the signals tournament, but I’ve seen interesting results in another world with the winning entry of the [M4 competition](<https://www.sciencedirect.com/journal/international-journal-of-forecasting/vol/36/issue/1>): A hybrid method of exponential smoothing and recurrent neural networks for time series forecasting, Slawek Smyl. It uses Neural Networks to tune exponential smoothing parameters.

If you can’t find the paper he has a walkthrough [here](<https://www.uber.com/blog/m4-forecasting-competition/>). There are some semi-accurate python implementations in CPU and GPU, but beware that this approach is compute heavy.

Also, when dealing with equity models, one often uses return series instead of prices. Many people here will have good reasons to dislike E.P. Chan, but if you are new in quant finance you may find his [books](<https://epchan.com/books/>) helpful to get a feel for how to treat financial data.

---

### Post #3 — **surajp** | 2023-05-05 16:23 UTC

I believe the idea in below linked post is much more applicable to Signals than classic tournament since we can embed stock name and sector and what not in the features and then let the Transformer learn the underlying relationships. This should be able to process raw time-series returns as well.

[“Eras” of Transformer for Numerai](<https://parmarsuraj99.medium.com/era-of-transformers-792e5960e287>)
