---
title: "GFlowNets for Signal Miner: A New Way to Find Diverse, High-Performing Models"
category: Data Science
url: https://forum.numer.ai/t/gflownets-for-signal-miner-a-new-way-to-find-diverse-high-performing-models/7966
created_at: 2025-03-10T18:47:16.350000+00:00
last_posted_at: 2025-03-20T15:52:37.545000+00:00
posts_count: 2
views: 1683
tags: []
---

# GFlowNets for Signal Miner: A New Way to Find Diverse, High-Performing Models

---

### Post #1 — **jefferythewind** | 2025-03-10 18:47 UTC

Hey everyone,

I wanted to share something exciting I’ve been working on that could significantly improve the search for diverse, high-performing models in the Numerai ecosystem. If you’ve been using **Signal Miner** ([GitHub](<https://github.com/jefferythewind/signal_miner>)), you already know the key challenge: **predictive edge is small and fleeting**. Strong models might hit 5% correlation, maybe 10% at best, and poor performance (even negative correlation) is inevitable in certain rounds.

But one thing we do know: **multiple diverse competing solutions can exist and score well**. Having many well-scoring models is better than having just the single best one.

* * *

## **GFlowNets: A New Paradigm for Model Search**

Last week, I attended a talk by **Alex Hernandez-Garcia** introducing **GFlowNets** , a fascinating idea championed by **Yoshua and Emmanuel Bengio**. If you haven’t heard about them, check out:

  * [Alex’s GitHub](<https://github.com/alexhernandezgarcia/gflownet>)
  * [Recent paper: Multi-Fidelity Active Learning with GFlowNets](<https://arxiv.org/abs/2306.11715>)
  * [Introduction article: Flow Network based Generative Models for Non-Iterative Diverse Candidate Generation](<https://proceedings.neurips.cc/paper/2021/hash/e614f646836aaed9f89ce58e837e2310-Abstract.html>)
  * [Yoshua Bengio’s blog post on GFlowNets](<https://yoshuabengio.org/2022/03/05/generative-flow-networks/>)



### **Quote from Dr. Bengio:**

> _“I have rarely been as enthusiastic about a new research direction. We call them**GFlowNets** , for Generative Flow Networks. They live somewhere at the intersection of reinforcement learning, deep generative models, and energy-based probabilistic modeling. They are also related to variational models and inference, and I believe they open new doors for non-parametric Bayesian modeling, generative active learning, and unsupervised or self-supervised learning of abstract representations to disentangle both the explanatory causal factors and the mechanisms that relate them.”_

### **What makes GFlowNets special?**

Unlike traditional deterministic optimization, **GFlowNets are generative models trained to produce diverse outputs that all perform well on a given task**. Instead of just finding the best single solution, they learn a **probability distribution** over good solutions. This is incredibly useful for problems like drug discovery, where you need to explore many promising molecules rather than just one.

* * *

## **Applying GFlowNets to Signal Miner**

This approach is **exactly what we need for Signal Miner**. Right now, Signal Miner samples hyperparameters uniformly from LightGBM. But **what if, instead of uniform sampling, we trained a GFlowNet to generate hyperparameter sets that consistently produce high correlation with the Numerai target?**

### **From the NeurIPS paper:**

> _“This paper is about the problem of learning a stochastic policy for generating an object (like a molecular graph) from a sequence of actions, such that the probability of generating an object is proportional to a given positive reward for that object.”_

GFlowNets allow us to:

  * **Find a diverse set of benchmark-beating models** (instead of just one optimal set of hyperparameters).
  * **Adapt dynamically** to what works best, rather than relying on uniform random sampling.
  * **Speed up hyperparameter search** by focusing on promising regions instead of exhaustive grid search.



* * *

## **Implementation & First Results**

I built a **Signal Miner environment within the GFlowNet framework** , available here:  
![:link:](https://emoji.discourse-cdn.com/twitter/link.png?v=15) **[GitHub: GFlowNet Signal Miner](<https://github.com/jefferythewind/gflownet-signal-miner>)**

To train, just run:
    
    
    python main.py env=signalminer proxy=signalminer logger.do.online=True
    

This streams training results to Weights & Biases.

### **Early Findings**

I ran a lightweight experiment on a subset of Numerai Classic data and features. Each training batch evaluates and updates 10 sets of parameters. Over **12K rounds** have processed so far. (Clarification: _“reward”_ and _“proxy”_ mean the same thing.)

The trend is clear: **over time, the GFlowNet generates better hyperparameters** that achieve higher mean reward. Interestingly, **the max score has not increased significantly yet** , which suggests further tuning is needed. But for an initial test, this is very promising!

### **Example of GFlowNet-Generated Hyperparameters**

In GFlowNet terminology, model output is called a **state** , representing a sequence of actions that led to a final configuration. Here’s an example of what GFlowNets produce when searching for optimal hyperparameters:

**Final state:** `[1, 5, 10, 2, 3, 8, 7, 9]`  
**Sequence of actions:** `[(1,), (5,), (10,), (2,), (3,), (8,), (7,), (9,), (-1,)]`  
**Human-readable version:**  
`colsample_bytree: 0.34 | reg_lambda: 0.0 | learning_rate: 0.33334 | max_bin: 5 | max_depth: 9 | num_leaves: 18 | min_child_samples: 1000 | n_estimators: 23`

[![Training Stats](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/e/eb4ed7104bf972186e91052e0164f73c411aec45_2_690x145.jpeg)Training Stats1920×405 58.7 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/e/eb4ed7104bf972186e91052e0164f73c411aec45.jpeg> "Training Stats")

* * *

## **Why This Matters**

This experiment is just the beginning. **GFlowNets are generative AI beyond language models** —they use probabilistic reasoning to explore solution spaces efficiently. In our case, we want to **generate a field of diverse, high-performing models** , not just one single best model.

This aligns with principles of **ensemble learning and diversification** —critical to Numerai’s long-term success. It also aligns with the vision of Signal Miner: **mine for your own unique alpha. Everyone is a winner!**

* * *

## **Next Steps**

The main challenge now is **speed** —we need to evaluate many models to properly train the GFlowNet. However, **new research is showing how we can use cheaper (faster) low-fidelity proxies to help train GFlowNets more efficiently**.

Check out [Multi-Fidelity Active Learning with GFlowNets](<https://arxiv.org/abs/2306.11715>) for more on this. Incorporating this approach could make training significantly faster and more cost-effective, allowing us to explore even more parameter spaces efficiently.

But I’m excited about the potential. **This could be a powerful new tool for Numerai tournament participants.**

Would love to hear your thoughts! Have you tried GFlowNets? Do you think this approach could be applied elsewhere in the tournament? Let’s discuss! ![:rocket:](https://emoji.discourse-cdn.com/twitter/rocket.png?v=15)

---

### Post #2 — **jefferythewind** | 2025-03-20 15:52 UTC

**Update**

I got some feedback from Alex, the creator of the `gflownet` package that using an exponential function of the raw proxy may help the gflownet drive the random distribution towards higher max reward models, which is exactly what we want.

In each iteration, the GFlowNet helps us generate 10 random hyper parameter configurations for LightGBM training. The **proxy** is another name for the reward function. In this case, the raw proxy I used here is average era-wise correlation with the target. What Numerai calls CorrV2. However correlation can be negative, while the proxy shouldn’t be. So the exponential function helps with this as well. The proxy I implemented is:

`proxy = exp( mean_corr * 100 )`

Since correlation is like a percent, the 100 multiplier puts our correlation is range usually around += 5 percent. This is a decent range for the exponential function to work. This new proxy rewards the GFlowNet much more for producing higher correlation models, and penalizes less for low correlation. This promotes more experimental expansion in potentially high-corr areas of hyper-parameter space.

[![Exponential Function, By Peter John Acklam - Own work, CC BY-SA 3.0](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/e/e0bc19b2b974103d5ebe403927c0193f04198a4e_2_666x500.png)Exponential Function, By Peter John Acklam - Own work, CC BY-SA 3.02560×1920 155 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/e/e0bc19b2b974103d5ebe403927c0193f04198a4e.png> "Exponential Function, By Peter John Acklam - Own work, CC BY-SA 3.0")

I ran a small version of the numerai dataset. There were 10 models evaluated per iteration, and 50K iterations, for a total training of 500K models. It took about a week to complete, and I’ve produced what I think is a pretty cool Graphic.

It captures the main idea from the Signal Miner, that the more models you evaluate, you eventually uncover better and better performing models. The GFlowNet potentially accelerates the search! I think that is evident by the increasing mean proxy. I also highlight each time we break a new high-water mark. I put the training time on the log scale for better separation of the data.

[![Screenshot 2025-03-20 at 11.47.48 AM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/0/05c6887322f05bd0c510d4c4a1d005c78db6c124_2_690x383.jpeg)Screenshot 2025-03-20 at 11.47.48 AM1888×1048 127 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/0/05c6887322f05bd0c510d4c4a1d005c78db6c124.jpeg> "Screenshot 2025-03-20 at 11.47.48 AM")

GitHub Repo: [GitHub - jefferythewind/gflownet-signal-miner: GFlowNet Signal Miner](<https://github.com/jefferythewind/gflownet-signal-miner>)

Run it with the python command in the previous post.

This seems like a pretty cool way to push your hyper-parameter search toward better performing models. One could also use a different proxy altogether to drive the search in other directions. The problem is, for the wide and deep tree models that we are really interested in, with 30K + trees, training our GFlowNet will take too long. I’ve been waiting for month already and only evaluated this size model about 100 times. I’m currently thinking about how to speed up the GFlowNet training, and how to get more information back into it, so it learns from every model I evaluate.
