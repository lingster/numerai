---
title: "Numerai Tournament Example code using Pytorch NN and Optuna"
category: Tournament
url: https://forum.numer.ai/t/numerai-tournament-example-code-using-pytorch-nn-and-optuna/4639
created_at: 2021-12-17T07:56:28.643000+00:00
last_posted_at: 2022-04-25T08:12:11.105000+00:00
posts_count: 14
views: 2813
tags: []
---

# Numerai Tournament Example code using Pytorch NN and Optuna

---

### Post #1 — **meaten12121** | 2021-12-17 07:56 UTC

Hi,

I dived into this numerai community nine months ago and keep developing my tournament code.  
There are many example scripts from this community, but I wanted to share my code base to get feedback from this community.  
Hope some newcomers find this helpful.

[github.com](<https://github.com/meaten/numerai_NN_example>)

### [GitHub - meaten/numerai_NN_example: Numerai tournament example scripts using NN and...](<https://github.com/meaten/numerai_NN_example>)

Numerai tournament example scripts using NN and optuna

Features:

  * era-boosted train, time-series cross-validation
  * era-batches training
  * model hyperparameter tuning on pytorch NN and GBDT model
  * several tips on Numerai Forum are also included



Thanks!

---

### Post #2 — **objectscience** | 2021-12-17 15:50 UTC

Very nice work!.

I’m going to ping the CoE on this to see if it will qualify for a bounty.

I know for me personally, the day I can actually afford a couple of good GPU’s, this is going to be really useful.

---

### Post #3 — **aventurine** | 2021-12-17 18:42 UTC

Very nice. Also love the model name. Might want to try and fix the model link though because its not taking into account the _ and its going to one of my models [Numerai](<https://numer.ai/emerald>) and not [Numerai](<https://numer.ai/emerald_>) ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=10)

---

### Post #4 — **meaten12121** | 2021-12-18 06:45 UTC _(reply to #2)_

Thanks for your comment!  
Bounty? I didn’t know that system. I appreciate it if you ping the CoE!

The example models I added are simple and don’t need good GPUs. (about 1GB GPU memory consumption)  
I hope you will get some after this significant GPU shortage.

---

### Post #5 — **meaten12121** | 2021-12-18 06:49 UTC _(reply to #3)_

Sorry for the mistake on url parsing ![:fearful:](http://forum.numer.ai/images/emoji/twitter/fearful.png?v=10) I already fixed it.

---

### Post #6 — **gbrecht** | 2021-12-24 08:01 UTC _(reply to #2)_

I use vast.ai to use cloud GPUs. Even with normal GPU prices there is economically no reason to get one ourself. I wrote a forum post on my setup. Please give me a ping if you want some more details.

---

### Post #7 — **stoicism** | 2021-12-24 09:52 UTC

Hi mate, many thanks for sharing your hard work with us. Can you please explain what era-boosted training and era-batches training is? It would be booster shot for the newcomers!

---

### Post #8 — **gbrecht** | 2021-12-24 09:57 UTC _(reply to #7)_

Era Boosting is

  * Training on all eras
  * In sample prediction of all eras
  * Selecting a subset of all eras to train on based on in sample performance (usually bottom half)
  * Resume training with only the selected eras



Era Batches apply to neural networks and there the common sense is that it is good to train in batches equivalent to eras. I.e. forward for one era and then backward. and then the next era and so on.

---

### Post #9 — **stoicism** | 2021-12-24 10:01 UTC _(reply to #8)_

So instead of treating batch-size as a hyper parameter, the era sizes (number of data points in each era) are assigned as the batch size, is that correct? Thanks for the detailed response [@gbrecht](</u/gbrecht>) !

---

### Post #10 — **gbrecht** | 2021-12-24 10:02 UTC _(reply to #9)_

That is correct. I personally use pytorch where you define a DataSet class and it is dead easy to return an era as the next batch. With keras I never got it to work.  
And I am sure it is super easy in JAX but despite [@jrb](</u/jrb>) pep talk I have never gotten something to run…

---

### Post #11 — **stoicism** | 2021-12-24 10:06 UTC _(reply to #10)_

Thanks for the clarification. One less hyperparameter to worry about. Although, I am interested to see if treating batch-size as a hyperparam yield something equivalent to era size or not.

---

### Post #12 — **jrb** | 2021-12-24 17:15 UTC _(reply to #10)_

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/forum.numer.ai/gbrecht/48/3456_2.png) gbrecht:

> With keras I never got it to work.

If you’re using `tf.keras`, subclassing [`tf.keras.utils.Sequence`](<https://www.tensorflow.org/api_docs/python/tf/keras/utils/Sequence>) is the way to go. The next method I’ll describe is more universal and works with `tf.keras`, Tensorflow and JAX.

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/forum.numer.ai/gbrecht/48/3456_2.png) gbrecht:

> And I am sure it is super easy in JAX but despite [@jrb](</u/jrb>) pep talk I have never gotten something to run…

If you’re using Tensorflow without the keras training loop, or even if you are using keras: Start by converting your data into a [RaggedTensor](<https://www.tensorflow.org/guide/ragged_tensor>) first. You can then turn the RaggedTensor into a [`tf.data.Dataset`](<https://www.tensorflow.org/api_docs/python/tf/data/Dataset>) using the `from_tensor_slices` method. And then, Bob’s your uncle!

If you’re using JAX, use the [`as_numpy_iterator`](<https://www.tensorflow.org/api_docs/python/tf/data/Dataset#as_numpy_iterator>) method on the `tf.data.Dataset` object.

One thing to bear in mind is that the JAX jit caches its traces based on the shapes of the tensors passed in. So, if you’re using eras as batches with the jit, your first epoch is going to be super slow because it has to jit your training loop for every era (because they all have different number of rows).

This is the case with Tensorflow AutoGraph as well, but the `experimental_relax_shapes` argument to the [`tf.function`](<https://www.tensorflow.org/api_docs/python/tf/function>) decorator helps alleviate this issue.

Using JAX without `jit` and Tensorflow in eager mode are perfectly feasible options. Empirically, I’ve observed that both are a bit faster than PyTorch. Although, I haven’t tried using PyTorch’s jit.

In any case, you can efficiently mix and match Tensorflow, JAX (and even PyTorch, if you really want to) using [dlpack](<https://github.com/dmlc/dlpack>) tensors. All 3 frameworks support it. Heck, even XGBoost supports it. ![:slight_smile:](https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=15)

---

### Post #13 — **jrb** | 2021-12-24 17:17 UTC _(reply to #8)_

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/forum.numer.ai/gbrecht/48/3456_2.png) gbrecht:

> Era Batches apply to neural networks and there the common sense is that it is good to train in batches equivalent to eras. I.e. forward for one era and then backward. and then the next era and so on.

Alternatively, use minibatches, but ensure that each minibatch does not contain data from more than one era.

---

### Post #14 — **meaten12121** | 2022-04-25 08:12 UTC

Hi,

I’ve just updated the above GitHub repository to adopt the changes below:

  * 10x Faster MLP models compared to the initial commit (nn.ModuleList → nn.Sequential)
  * use numerai v4 dataset



I know there will be benchmark models ( talked at numeracon April 2022) and my example should be obsolete soon but I decided to continue updating for a while for the sake of my learning and who forked my repository ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=10)

Future plan:

  * Transformer model to extract new features different from MLP or GBDT
  * Xfeat([GitHub - pfnet-research/xfeat: Flexible Feature Engineering & Exploration Library using GPUs and Optuna.](<https://github.com/pfnet-research/xfeat>)) to automate feature engineering



Any advice or proposals for future updates are welcome. Thanks!
