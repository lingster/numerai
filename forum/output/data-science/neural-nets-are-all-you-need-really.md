---
title: "Neural Nets are all you need. Really?"
category: Data Science
url: https://forum.numer.ai/t/neural-nets-are-all-you-need-really/1064
created_at: 2020-10-13T05:13:30.203000+00:00
last_posted_at: 2020-10-14T03:50:12.604000+00:00
posts_count: 3
views: 4331
tags: []
---

# Neural Nets are all you need. Really?

---

### Post #1 — **surajp** | 2020-10-13 05:13 UTC

[correlator’s question on Neural nets in RocketChat](<https://community.numer.ai/channel/datascience?msg=sAhmGfuK55cBPPABx>)

> On the Numerai data, Tree based models are easier to develop than Neural nets as the latter requires more finetuning. I tried a live model (NN) for a some weeks and then gave up as it was consistently below 0 corr. Assuming that most of the tournament models are tree based models (I am pretty sure they are), it will help Numerai if people build other kinds of models such as Neural nets.  
>  It would help if someone could give pointers to building a first cut NN model which works at par with the example model. [@mdo](</u/mdo>) [@jrb](</u/jrb>) [@surajp](</u/surajp>)

I thought why not answer it on forum as we can discuss on this broadly here.

I think there are a lot of Neural Nets in the tournament.

First thing to consider when trying out Neural nets for modelling is the fact that they are called “Universal function approximators”. You can perform all sorts fancy experiments with it. A sufficiently parameterized model will eventually over-fit on the training data.

  * I’d recommend going through this paper, “[Understanding deep learning requires rethinking generalization](<https://arxiv.org/abs/1611.03530>)” after every few months ![:face_with_monocle:](http://forum.numer.ai/images/emoji/twitter/face_with_monocle.png?v=12)(might give you some ideas as well)



You can approximate (or even distillate) your best of tree based models by a sufficiently parameterized neural net. Which implies that NNs are capable of learning similar patterns as Trees. You just need to find an appropriate architecture for the data.

  * [@mdo](</u/mdo>) recently answered this in recent OhWA [OHwA S03E02 (Slido question 9)](<https://docs.numer.ai/office-hours-with-arbitrage/office-hours-recaps-season-3/ohwa-s03e02>)



Next step is to incorporate **correlated variety** (the closest word I could think of) if you are considering ensembling. With that, you now have a whole new pallet of choices. You can ensemble on different architectures, initialization, training on different subsets of eras and what not!  
You need a combination of models that can generalize well when combined OR Instead of ensembling, you can learn another model that is uncorrelated to all of these (this also applies to learning an orthogonal model to your best Tree based model) ([“Beating the wisdom of the crowds is harder than recognizing faces or driving cars”](<https://twitter.com/parmarsuraj99/status/1313697215148257280?s=20>)). You need to give a Boost to your models ![:deciduous_tree:](http://forum.numer.ai/images/emoji/twitter/deciduous_tree.png?v=12).

  * I wasn’t a big fan of ensembles of big models in production because of resource constraints but turns out we can reduce the size and inference time by pruning and distillation without sacrificing much of the original model’s performance. Which can somehow reduce overfitting.

  * [Deep Ensembles: A Loss Landscape Perspective](<https://arxiv.org/abs/1912.02757>) This paper changed my perspective on ensembling NNs! (You might get some ideas from here too)




The most important thing is choosing a **loss function**! There is a lot of discussion on loss functions on the forum. This is where NNs shines (pretraining => finetuning). Remember, predictions are scored on correlation. **You should develop your own loss function to get better on MMC** (that’s your secret sauce)!

  * you can also choose from a wide range of optimizers that comes with DL libraries [Descending through a Crowded Valley – Benchmarking Deep Learning Optimizers](<https://arxiv.org/abs/2007.01547>)



**NOTE:**

  * NNs have a factor of luck with initialization, so you should develop some kind of quick evaluation framework/functions. That way you can experiment faster.
  * I haven’t considered any kind of pre-processing to data.



Instead of a neural only model(s), you can combine a good tree based model (for CORR) with a flexible NN trained on originality of predictions (corr+ MMC).

With this, I have (almost) opened up all of my core ideas around NNs for the tournament. I haven’t done anything new in particular, it’s just accumulation of interesting RocketChat and forum posts. I guess I have previously discussed about some specific things too at both places. and there are some direct references in this posts that simply indicate what my models are! ![:innocent:](http://forum.numer.ai/images/emoji/twitter/innocent.png?v=12)

To answer,  
Yes, Its possible to beat example predictions with NNs. ![:smiley:](http://forum.numer.ai/images/emoji/twitter/smiley.png?v=12)

Above points are good enough to get you started with a really good basic model that you can later improve. Also,there is a lot of space for pre and post-processing!

[numer.ai/parmars](<https://numer.ai/parmars>) is Neural ensemble from 232  
[numer.ai/dhi](<https://numer.ai/dhi>) (meaning intelligence/understanding) is a single NN model from 232.

So (here), Neural Nets are (almost) all you need ![:wink:](http://forum.numer.ai/images/emoji/twitter/wink.png?v=12)! Hope this helps  
All the best ![:+1:](http://forum.numer.ai/images/emoji/twitter/+1.png?v=12)

---

### Post #2 — **jrb** | 2020-10-13 20:52 UTC

![](http://forum.numer.ai/user_avatar/forum.numer.ai/surajp/48/2961_2.png) surajp:

> I wasn’t a big fan of ensembles in production(but turns out pruning and distillation can improve generalization. Is it true [@jrb](</u/jrb>)?)

I don’t quite understand. What do model pruning and model distillation have to do with ensembling? Unless of course, if you’re talking about using model distillation to train a smaller student model using an ensemble of larger models as the teacher model.

---

### Post #3 — **surajp** | 2020-10-14 03:50 UTC _(reply to #2)_

Maybe I was unclear. I was referring to my experience of using ensemble of some big models like BERT(as seen in so many NLP competitions) in production. But distilling and making them efficient helped in efficient ensemble in production.

This also suggests there is a space for some architectural improvements.
