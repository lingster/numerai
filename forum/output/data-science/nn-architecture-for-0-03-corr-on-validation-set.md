---
title: "NN architecture for >0.03 CORR on validation set"
category: Data Science
url: https://forum.numer.ai/t/nn-architecture-for-0-03-corr-on-validation-set/3145
created_at: 2021-05-01T09:28:34.203000+00:00
last_posted_at: 2021-08-26T17:22:22.197000+00:00
posts_count: 53
views: 8443
tags: []
---

# NN architecture for >0.03 CORR on validation set

---

### Post #1 — **nyuton** | 2021-05-01 09:28 UTC

Hi,

I wanted to share an article I found recently.  
It’s a simple and elegant solution for automated feature engineering.

In my experiemnts it easily pushes the CORR on validation above 0.03, which is pretty good.  
I don’t have evidence yet, how it performs in forward testing, but it’s promising!

Here it goes:

![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/d/dd62a55b837439e27df1d866705fc95eb0d5b4be.png) [Towards Data Science – 26 Feb 21](<https://towardsdatascience.com/automated-feature-engineering-using-neural-networks-5310d6d4280a/> "11:36PM - 26 February 2021")

![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/1/165c7e369a564d5df042726d992e7c775e822519_2_671x499.jpeg)

### [Automated Feature Engineering Using Neural Networks | Towards Data Science](<https://towardsdatascience.com/automated-feature-engineering-using-neural-networks-5310d6d4280a/>)

How to automate and greatly improve one of the most tedious steps in data modeling

Est. reading time: 17 minutes

The concept can easily be applied to the tournament dataset.  
The key concept is on this diagram:  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/17a27b6c4917114e3761cf0ada271d12931da383_2_524x500.jpeg)image722×688 133 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/17a27b6c4917114e3761cf0ada271d12931da383.jpeg> "image")

---

### Post #2 — **mindyoself** | 2021-05-02 13:26 UTC

[@nyuton](</u/nyuton>) Thanks for that,

Out of interest were/are any of our neural net modellers also using feature embeddings and have they found usefulness with it already? I thought was only NLP focused but perhaps not.

The previous article by the same author was interesting too for feature engineers

<https://towardsdatascience.com/why-you-should-always-use-feature-embeddings-with-structured-datasets-7f280b40e716>

---

### Post #3 — **lysk** | 2021-05-02 18:13 UTC _(reply to #2)_

From a NN perspective this is a bit surprising. One benefit of using NN is to learn cross feature relationships (non-linear ones). Here the author is forcing the network to learn some relationships before injecting that knowledge into a bigger network, which begs the question why not work with a big network in the first place? (such as a wide&deep architecture)  
I am not familiar with the dataset used in the blog post to evaluate the result by myself (error rate from 37.6% down to 37.2%). I wish the author would have given additional examples.

Feature embedding can be quite effective outside NLP. I have been using it at work when working with sparse features. It goes like this: train an auto encoder to reconstruct the sparse features then use the encoder part (and set the weights to “non trainable”), now the spare features can have a dense representation. So far I have not been successful in applying this idea to the tournament.

Embedding categorical features is often a good strategy, you can have some intuition about how it works by looking at it as a sequence of: (1) associate an integer to each variable (2) one-hot encode the variable (now this can be super sparse) then (3) apply a smaller dense layer on the one-hot encoding. Which is what the author have implemented with `tf.feature_column` functions and the `DenseFeatures` input layer.

---

### Post #4 — **paulito** | 2021-05-03 06:17 UTC _(reply to #2)_

I don’t think using embedding layers makes a lot of sense for numerai tournament. Embeddings are useful when handling categorical data, sparse data, or otherwise one hot encoded data. If you are dealing with intervall-scaled data, there is not really a need for that and most higher-order interactions will be learned by the model itself. The embedding layer helps most when you want to reduce the dimensionality of a really big matrix. For the tournament I don’nt see the need for that.

---

### Post #5 — **nyuton** | 2021-05-03 09:56 UTC

Here it comes. The highest validation corr I’ve seen so far.  
The above mentioned architecture with around 100 features (I don’t have enough RAM to use all of them)  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/2194fb523fbdc2c8c1814ddd7225d7120181b317.png)image280×489 15.8 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/2194fb523fbdc2c8c1814ddd7225d7120181b317.png> "image")

---

### Post #6 — **clem74** | 2021-05-03 10:33 UTC

Congrats ! And thanks for the article ! A few questions for achieving good results

  * Are you overfitting on the training data ( by how much? )
  * what is your fitness function ( mse, or are you using sorted differential lib to run spearman, or a mix )
  * batch norm/ dropouts ?
  * SGD batch size ( I’ve experimented with eras as minibatch, which worked better than smaller size on my case, but quickly limited by 16Gb or RAM… for fully connected layers)



Would love to hear what moved the needle for you with this architecture.

---

### Post #7 — **mindyoself** | 2021-05-03 17:36 UTC _(reply to #5)_

[@nyuton](</u/nyuton>) Presumably with neutralisation or off the cuff? Also are you overfitting if you’re seeing straight greens for your model?

---

### Post #8 — **nyuton** | 2021-05-03 18:23 UTC _(reply to #7)_

There is no neutralisation involved here.

---

### Post #9 — **mindyoself** | 2021-05-03 18:29 UTC _(reply to #8)_

Congrats. That’s really interesting. Will be good to see how that performs in production.

---

### Post #10 — **greenprophet** | 2021-05-03 19:21 UTC

Thanks for sharing. I have been meaning to try exactly this at some point but it is a bit intensive. I have gotten similar metrics as this with a blend of NN that have some embedding ideas but nothing this complete brute force way. Live results on 9 rounds are also promising. Really going to have to get back to trying this way.

Two things you could do to get all the features involved. You can just pass through the ones you don’t embed to the final layers. Also you can cycle the groups individually like just intelligence, dexterity etc.

So for example if you just pass through constitution which is mostly shitty features and then cycle the other groups individually you probably will have a manageable number of embedding heads with all the features involved.

---

### Post #11 — **jacob_stahl** | 2021-05-03 19:49 UTC _(reply to #3)_

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/l/8e8cbc/48.png) lysk:

> One benefit of using NN is to learn cross feature relationships (non-linear ones). Here the author is forcing the network to learn some relationships before injecting that knowledge into a bigger network, which begs the question why not work with a big network in the first place? (such as a wide&deep architecture)

While neural networks are fantastic at finding non-linear patterns, even a big network will always follow the path of least resistance during training. Meaning, it will it might only find a few strong relationships during training and ignore weaker ones. Training a single neural network to find as many relationships as possible is like kicking water uphill.

The feature embeddings in the article are able to extract patterns in from the dataset that would otherwise be drown out by stronger ones more directly correlated with the targets.

---

### Post #12 — **lysk** | 2021-05-03 20:11 UTC _(reply to #11)_

[@jacob_stahl](</u/jacob_stahl>) possibly yes, so far with regularization I was able to achieve ok-ish results. I haven’t check all the implementation in details but it could be useful to set those small feature-networks to `non-trainable` when they are added to the final model, otherwise there is a risk to “erase” what they learnt during training.

---

### Post #13 — **jacob_stahl** | 2021-05-03 20:31 UTC _(reply to #12)_

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/l/8e8cbc/48.png) lysk:

> could be useful to set those small feature-networks to `non-trainable` when they are added to the final model, otherwise there is a risk to “erase” what they learnt during training.

That’s the approach I’m taking right now. Since the weights on the small networks are frozen, the outputs don’t change. You can through the entire dataset and cache the outputs, and use them to train other models. I will probably try replacing the big network with an XGBoost model and see what happens.

---

### Post #14 — **nyuton** | 2021-05-05 14:09 UTC

This goes beyond my wildest dreams ![:slight_smile:](https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=13)  
I guess it’s a big overfit, but I don’t see why.  
Please share your results as well.  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/7cfe8732ede2af3f58669e2fc549459706aa3983.png)image278×503 15.6 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/7cfe8732ede2af3f58669e2fc549459706aa3983.png> "image")

---

### Post #15 — **schot** | 2021-05-05 14:40 UTC _(reply to #14)_

I’ve been trying to combine this technique with my NN, but I can’t get high val corr. Did you made any change to the code introduced in the article?

---

### Post #16 — **nyuton** | 2021-05-05 14:42 UTC _(reply to #15)_

Sure I did, I rewrote the whole thing ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=9)  
But the basic idea is the same!

---

### Post #17 — **olivepossum** | 2021-05-05 16:04 UTC

[@nyuton](</u/nyuton>) impressive diagnostics! Do you use early stopping agains validation data?

---

### Post #18 — **nyuton** | 2021-05-05 16:25 UTC _(reply to #17)_

Sure, I always do!  
Otherwise it start overfitting soon.

---

### Post #19 — **senadorancap** | 2021-05-05 20:45 UTC _(reply to #14)_

How do you chosen the 100 features subset? It was the Lopez de Prado MDA?

---

### Post #20 — **mindyoself** | 2021-05-07 10:48 UTC _(reply to #14)_

[@nyuton](</u/nyuton>) I think you should also consider neutralising it to improve your feature exposure and validation SD. This is awesome, but that will be a kickass super-model. It might improve your drawdown as well.

---

### Post #21 — **olivepossum** | 2021-05-10 22:43 UTC

Hi,

I want to implement a test for this in Pytorch. My idea is to select, let’s say, 50 features (based on MDA, xgboost’s feature importance or any other criteria) and then build 50 models to create the extra features. Each model would have 49 of the 50 features as input features and would try to predict the one left. I would save the values of the last intermediate layer of each model and these values would be the engineered features used in my final model.

The flow would be something like this:  
1.- Build a model for each feature to predict that feature using the rest of the features as input, and store the last intermediate layer of each model.  
2.- Merge/Join intermediate layer values with the initial dataset (train_data). It would contain the initial features and the engineered ones.  
3.- Train a final model with all those features and predicting the target.

But reading the article it says:  
_The trick is making sure that the feature networks train with the final model rather than a separate process._

My approach would definitely not do that so I guess I’m missing something. Why is this important?

The article also says:  
_Because we have several auxiliary outputs, we need to tell TensorFlow how much weight to give each one in determining how to adjust the model to improve accuracy. I personally like to give 50% weight to the auxiliary predictions (total) and 50% the the target prediction. Some might find it strange to give any weight to the auxiliary predictions since they are discarded at the loss calculation step. The problem is, if we do not give them any weight, the model will mostly ignore them, preventing it from learning useful features._

Again, I wouldn’t be doing anything like that so I’m wondering if an approach like what I have in mind make sense at all or I’m missing something (I do not have deep knowledge on NN).

Thanks!

---

### Post #22 — **nyuton** | 2021-05-11 07:57 UTC _(reply to #21)_

Why don’t you just try to implement, what’s in the article? It works…

---

### Post #23 — **olivepossum** | 2021-05-11 12:44 UTC _(reply to #22)_

My approach seems easier to implement in PyTorch to me but as I mentioned I’m not an expert in the subject. If conceptually my approach makes sense I would go for it but if not, I would do more research to replicate the implementation of the article.

---

### Post #24 — **paulito** | 2021-05-19 08:52 UTC _(reply to #5)_

So if you don’t mind asking, how is that model doing on live data?

---

### Post #25 — **nyuton** | 2021-05-19 09:30 UTC _(reply to #24)_

You can check it out here: [Numerai](<https://numer.ai/nyuton_test14>)

---

### Post #26 — **paulito** | 2021-05-19 10:22 UTC _(reply to #25)_

Cool. Thanks for sharing. Performance seems ok, given that the last rounds were kind of weird anyway, but maybe not as good as your validation results promised?

---

### Post #27 — **nyuton** | 2021-05-19 11:13 UTC _(reply to #26)_

It needs some more time until we figure it out…

---

### Post #28 — **minou** | 2021-05-19 12:09 UTC _(reply to #27)_

It is a long game for sure. At a quick glance your test6 is outperforming test14. If you can say, was the corr on val2 and diagnostics with test6 higher than for 14, or is 6 returning higher corr at the moment despite having a lower corr on val?

---

### Post #29 — **nyuton** | 2021-05-19 15:33 UTC _(reply to #28)_

6 has lower validation corr and higher live corr than 14. At least for the last 2 weeks, which doesn’t say much…

---

### Post #30 — **mindyoself** | 2021-05-19 19:31 UTC _(reply to #25)_

Looking good at least for the first two score, but needs more time.

---

### Post #31 — **willmcnally1** | 2021-05-20 19:44 UTC

[@nyuton](</u/nyuton>) thanks for sharing! I am going to implement it. Can you share any details regarding your network architecture? E.g., how many layers / hidden units did you use in each of your 100 feature networks?

---

### Post #32 — **nyuton** | 2021-05-23 07:58 UTC _(reply to #31)_

Hi,

sorry, I keep that for myself ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=9)  
But the model is for sale! Someone just asked it. Contact me in private if you are interested.

---

### Post #33 — **bensch** | 2021-05-24 02:05 UTC

trying a variation of this and reading the article you linked he mentions _The trick is making sure that the feature networks train _**with**_ the final model rather than a separate process._ . Does anyone here have an intuition or data to show why this makes sense? if your feature producing networks are changing during the training of the main network isn’t that just going to make it more difficult for the main network to find any connections? Also what was your reasoning for doing 100 features rather than something like 10?

---

### Post #34 — **jacob_stahl** | 2021-05-24 03:31 UTC _(reply to #33)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/bensch/48/757_2.png) bensch:

> _The trick is making sure that the feature networks train _**with**_ the final model rather than a separate process._ . Does anyone here have an intuition or data to show why this makes sense? if your feature producing networks are changing during the training of the main network isn’t that just going to make it more difficult for the main network to find any connections?

I’ve been trying to cache the outputs of the smaller networks to save memory and reduce training time but I am considering switching to an end-to-end model like the one in the article.

Training the feature extractors with the main network in one cohesive unit MIGHT slow down training, but it shouldn’t prevent it from converging. Each extractor is basically trying to minimize 2 loss functions, its given feature and the target further down the network. There are quite a few neural network architectures that optimize multiple loss functions like VAEs GANs, and YOLO. I suppose you could think of the extractors as trying to predict a given feature while maintaining some “relevance” to the target.

Since the hidden layers being passed from each extractor to the big network are changing constantly during training, I suspect that feeding the big network the original features too helps with stability. It has something static to learn from while the extractors converge to a state that is more stable. Maybe that instablity also has a a regularizing effect like dropout or noise? I’m not sure.

---

### Post #35 — **nyuton** | 2021-05-24 05:55 UTC _(reply to #33)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/bensch/48/757_2.png) bensch:

> Also what was your reasoning for doing 100 features rather than something like 10?

I have already established a set of highly relevant 100 features from previous experiments. And it’s also much faster to train with 100 then with 310.  
Using all 310 features also gives good result, but 100 is slightly better and a lot faster.

10 features are not enough to get anywhere…

---

### Post #36 — **jackerparker** | 2021-05-24 06:41 UTC _(reply to #35)_

Hi nyuton,

What is your Val COR when you train a model using this set of 100 chosen features without the metod described in the article? Can’t be the selected features be a key for high validation rather than described method? I’m asking that because: 1. I have a set of features which provides me 0.03 val COR with simple lightgbm boosting 2. That would explain why nobody else can get desent results with the method from article.

Mark

---

### Post #37 — **nyuton** | 2021-05-24 07:27 UTC

Hi JackerParker,

This model is stronger then any other model I have, when trained on the full dataset. I experimented with tuned XGB, RF and MLP models.  
But the feature selection definitely improves performance! No doubt about it.

---

### Post #38 — **crownholder** | 2021-05-24 08:25 UTC _(reply to #22)_

Am I missing something? If its a competition why would you teach everyone to make the same model? In my opinion it takes away the fun of it. Just my opinion.

---

### Post #39 — **minou** | 2021-05-24 10:04 UTC _(reply to #38)_

[@crownholder](</u/crownholder>) There’s are many aspects to a model and training that can make a big difference to performance beyond the basic choice of architecture; e.g. choice of loss function, which activation function, the kernel initialiser, any regularisation, optimiser selection, random seed, learning rate strategy, batch size, early stopping settings… Then there’s the data itself, do you train on everything, a subset (which subset) and so on. So describing a basic approach to an architecture and giving that to 100 people will inevitably result in 100 different models that could perform very differently. And, part of the fun is becoming aware of what could be a new approach, having a go at implementing it, and perhaps putting one’s own spin on it.

---

### Post #40 — **olivepossum** | 2021-05-24 10:32 UTC _(reply to #33)_

I’m also working on a [variation](<http://forum.numer.ai/t/nn-architecture-for-0-03-corr-on-validation-set/3145/21>), precisely because don’t know how to implement what you mention with Pytorch:  
_The trick is making sure that the feature networks train _**with**_ the final model rather than a separate process_  
Any reading resource to train nn with other nn with Pytorch is more than welcome!  
Regarding features, I select a subset of features using Marcos Lopez de Prado MDA technique. My subset is slightly more than 100.

---

### Post #41 — **bensch** | 2021-05-24 12:06 UTC _(reply to #35)_

im not sure if we are on the same page, but I meant using sets of 10 for individual feature discovery units, which is where I was mixed up I think, you actually meant you didn’t bother to include 210 of the features in anything since you have deemed them to correlated to other features etc…

---

### Post #42 — **nyuton** | 2021-05-24 14:40 UTC _(reply to #38)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/crownholder/48/1743_2.png) crownholder:

> If its a competition

This is not a classical competition! We are paid in NMR, which is nothing more than monkey money if the hedgefund fails.

Sharing ideas is vital to help others, improve the fund performance. This exchange of ideas gives NMR value on the long run…

[@minou](</u/minou>) stated correctly. It’s very unlikely that you would end up with a similar model given the information I shared. But this idea can certainly add up and improve your models’ performance.

---

### Post #43 — **edu** | 2021-05-30 12:06 UTC

Here’s a minimalistic Keras implementation of the model described in the article. With a bit of tuning, it works better than XGBoost but far from the 0.03 corr. I guess the feature selection plays an important role here.
    
    
    import tensorflow as tf
    import numpy as np
    
    class Regressor(tf.keras.layers.Layer):
    
        def __init__(self, dims=[32, 8]):
            super(Regressor, self).__init__()
    
            self.dims = dims
            for i, d in enumerate(self.dims):
                setattr(self, f'dense_{i}', tf.keras.layers.Dense(d))
            setattr(self, f'dense_{i+1}', tf.keras.layers.Dense(1))
    
        def call(self, inputs):
    
            x = inputs
            for i, _ in enumerate(self.dims):
                x = getattr(self, f'dense_{i}')(x)
                x = tf.nn.relu(x)
            x = getattr(self, f'dense_{i+1}')(x)
            x = tf.nn.sigmoid(x)
    
            return x
    
    
    class FeatureRegressor(Regressor):
    
        def __init__(self, dims=[32, 8], latent_idx=1):
            super(FeatureRegressor, self).__init__(dims)
            self.latent_idx = latent_idx
    
        def call(self, inputs):
    
            x = inputs
            for i, _ in enumerate(self.dims):
                x = getattr(self, f'dense_{i}')(x)
                if i == self.latent_idx:
                    latent = x
                x = tf.nn.relu(x)
    
            return latent, getattr(self, f'dense_{i+1}')(x)
    
    
    class Model(tf.keras.Model):
    
        def __init__(self,
            input_dims=10,
            feature_regressor_dims=[32, 8],
            feature_latent_idx=1,
            target_regressor_dims=[32, 8]):
            super(Model, self).__init__()
    
            self.input_dims = input_dims
            self.feature_regressor_dims = feature_regressor_dims
            self.target_regressor_dims = target_regressor_dims
    
            for i in range(input_dims):
                setattr(self, f'feature_regressor_{i}', FeatureRegressor(feature_regressor_dims, feature_latent_idx))
    
            self.target_regressor = Regressor(target_regressor_dims)
    
        def call(self, inputs):
    
            # Perform feature regressor inference
            features_latens = []
            features_preds = []
            for f in range(self.input_dims):
                # Prepare input without target feature
                mask = np.array([d != f for d in range(self.input_dims)])
                input_feature = tf.boolean_mask(inputs, mask, axis=1)
                # Regress target feature
                feature_latent, feature_pred = getattr(self, f'feature_regressor_{f}')(input_feature)
                features_latens.append(feature_latent)
                features_preds.append(feature_pred)
    
            # Perform target regressor inference
            features_latens = tf.concat(features_latens, axis=-1)
            input_target = tf.concat([inputs, features_latens], axis=-1)
            target_pred = self.target_regressor(input_target)
    
            # Concat predictions
            output = tf.concat(features_preds + [target_pred], axis=-1)
    
            return output

---

### Post #44 — **nyuton** | 2021-05-31 17:09 UTC _(reply to #43)_

Hi, I haven’t tried your code, but I noticed that you left all the BatchNorm and Dropout layers from the original! You can reach 0.03 with this model, if you follow, what’s in the article.

---

### Post #45 — **olivepossum** | 2021-05-31 17:35 UTC _(reply to #44)_

Hi [@nyuton](</u/nyuton>), when you tuned your model, did you do folded cross validation or just trained with the whole training dataset using validation for early stopping?

---

### Post #46 — **edu** | 2021-05-31 19:39 UTC _(reply to #44)_

Thanks [@nyuton](</u/nyuton>) ! Sure, this just exemplifies how to easily implement the simultaneous training of the feature regressors and the targets regressor, which I think it’s the key part. But of course, neural nets design and train is a subtle art.

---

### Post #47 — **nyuton** | 2021-06-01 07:46 UTC _(reply to #45)_

Just trained with the trainin set. Normally I do cross validation, but this model takes too long to train…

---

### Post #48 — **juhuu** | 2021-06-01 11:25 UTC _(reply to #43)_

Thanks for sharing. It’s a neat way of summarizing the extensive concept code.

However if I am not mistaken the tf.concat will lead to a single output whereas the paper tries to optimise multiple outputs. This way it seems also not possible to weight the individual outputs. The paper had the target to weight the loss of the main output (target_pred in your case) by 50%. Achieving this would probably lead to higher correlation.

---

### Post #49 — **edu** | 2021-06-01 12:10 UTC _(reply to #48)_

Thanks [@juhuu](</u/juhuu>) ! What you noted can be easily handled by the loss. For instance:
    
    
    def loss(beta):
        def f(y_true, y_pred):
            target_loss = tf.keras.losses.MSE(y_true[:,-1:], y_pred[:,-1:])
            feat_loss = tf.keras.losses.MSE(y_true[:,:-1], y_pred[:,:-1])
            return beta * target_loss + (1-beta) * feat_loss
        return f
    

In fact, in my opinion, this way is better since you can use different losses for the targets and for the features. Here I’m using the same though.

---

### Post #50 — **olivepossum** | 2021-06-01 14:36 UTC _(reply to #49)_

Hi [@edu](</u/edu>) this loss(beta) function is the one you would call in the Model(tf.keras.Model) model?

---

### Post #51 — **edu** | 2021-06-01 18:38 UTC _(reply to #50)_

Exactly [@olivepossum](</u/olivepossum>), for instance:
    
    
    model = Model(...)
    model.compile(loss=loss(beta=0.5), optimizer='adam', ..., run_eagerly=True)
    model.fit(...)

---

### Post #53 — **nyuton** | 2021-08-20 09:56 UTC

Hi!

If you liked this post and would like to buy actual good performing models, you can do it now at NumerBay.ai!  
Two of my models are available here: <https://numerbay.ai/c/numerai-predictions>

Nyuton

---

### Post #54 — **johnnywhippet** | 2021-08-26 17:22 UTC _(reply to #35)_

Mint, what was your highest Val CORR before you used this architecture?
