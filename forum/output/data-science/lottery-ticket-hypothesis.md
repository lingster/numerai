---
title: "Lottery Ticket Hypothesis"
category: Data Science
url: https://forum.numer.ai/t/lottery-ticket-hypothesis/358
created_at: 2020-05-08T23:26:17.828000+00:00
last_posted_at: 2020-05-08T23:26:17.970000+00:00
posts_count: 1
views: 1744
tags: []
---

# Lottery Ticket Hypothesis

---

### Post #1 — **objectscience** | 2020-05-08 23:26 UTC

## From “datascience” in RocketChat: Search for “facebookresearch”

**arbitrage**

[github.com](<https://github.com/facebookresearch/open_lth>)

![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/3/3787f8a577b5c65676f09d928f85742b150b024b_2_690x344.png)

### [GitHub - facebookresearch/open_lth: A repository in preparation for open-sourcing...](<https://github.com/facebookresearch/open_lth>)

A repository in preparation for open-sourcing lottery ticket hypothesis code.

**jrb**  
Not to downplay the importance of the lottery ticket hypothesis paper, but the results from “Training BatchNorm and Only BatchNorm” paper (linked in that repo) are some of the most mind blowing results I’ve seen in DL literature, lately.

**arbitrage**  
abstract: “Batch normalization (BatchNorm) has become an indispensable tool for training deep neural networks, yet it is still poorly understood. Although previous work has typically focused on its normalization component, BatchNorm also adds two per-feature trainable parameters: a coefficient and a bias. However, the role and expressive power of these parameters remains unclear. To study this question, we investigate the performance achieved when training only these parameters and freezing all others at their random initializations. We find that doing so leads to surprisingly high performance. For example, a sufficiently deep ResNet reaches 83% accuracy on CIFAR-10 in this configuration. Interestingly, BatchNorm achieves this performance in part by naturally learning to disable around a third of the random features without any changes to the training objective. Not only do these results highlight the under-appreciated role of the affine parameters in BatchNorm, but - in a broader sense - they characterize the expressive power of neural networks constructed simply by shifting and rescaling random features.”

**jrb**  
In other words, a randomly initialized network with frozen weights, can be trained to 83% accuracy by just learning the batch mean and variance at every layer. That’s bizarre and a completely unexpected result!

**on CIFAR-10** with a CNN.

**bor**  
isn’t that pretty close to what that paper found on evolving really weird neural network architectures. Didn’t really need to train the NN’s.  
high on my todo list ![:slightly_smiling_face:](https://emoji.discourse-cdn.com/twitter/slightly_smiling_face.png?v=15)  
not sure if this was the paper, but something along these lines

![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/d/dfb1be996c3a12b2bde5024398a7e3750ad0e86a.png) [research.google](<https://research.google/blog/using-evolutionary-automl-to-discover-neural-network-architectures/>)

![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/9/98850be3d2908a2f23dfd1bad480d984cdaf6348.jpeg)

### [Using Evolutionary AutoML to Discover Neural Network Architectures](<https://research.google/blog/using-evolutionary-automl-to-discover-neural-network-architectures/>)

Posted by Esteban Real, Senior Software Engineer, Google Brain TeamThe brain has evolved over a long time, from very simple worm brains 500 million...

![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/d/dfb1be996c3a12b2bde5024398a7e3750ad0e86a.png) [research.google](<https://research.google/blog/>)

![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/a/a0585730e7653a820751ab56139b8c839a0dfef9_2_690x362.jpeg)

### [Latest News from Google Research Blog - Google Research](<https://research.google/blog/>)

Using Evolutionary AutoML to Discover Neural Network Architectures  
Posted by Esteban Real, Senior Software Engineer, Google Brain Team The brain has evolved over a long time, from very simple worm brains 500…  
evolution baby ![:slightly_smiling_face:](https://emoji.discourse-cdn.com/twitter/slightly_smiling_face.png?v=15)  
I see that way back wsouza is doing something like that already - evolving neural networks

**vantratone**  
Extreme Learning Machines just make a single-layer NN with random weights (sort of) and they can work amazingly well (on some things)

**bor**  
feed the mmc ![:slightly_smiling_face:](https://emoji.discourse-cdn.com/twitter/slightly_smiling_face.png?v=15)

**jrb**  
vantratone Rocket is similar to ELMs but with 1d covolutions for time series data.  
Evolutionary computing is great for finding novel architectures. But it’s nowhere near competitive to gradient descent in terms of training efficiency.  
Why not do both? ![:slightly_smiling_face:](https://emoji.discourse-cdn.com/twitter/slightly_smiling_face.png?v=15)
