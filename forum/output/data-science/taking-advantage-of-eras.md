---
title: "Taking advantage of Eras"
category: Data Science
url: https://forum.numer.ai/t/taking-advantage-of-eras/3269
created_at: 2021-05-11T01:31:09.214000+00:00
last_posted_at: 2021-06-10T17:57:34.028000+00:00
posts_count: 7
views: 3509
tags: []
---

# Taking advantage of Eras

---

### Post #1 — **ryendu** | 2021-05-11 01:31 UTC

Hi there, I just started working with numerai and I have seen quite a few other topics discussing eras in numerai, and I’d like to start a topic for sharing tips about what can be done with the era column (aside from era-boosting which was covered by another topic). From what I understand, the era column goes from era1 to era120 in the training set, each era has a varying amount of data points, and it is basically impossible to track specific stocks across eras (or is it? if it’s possible, can someone please point that out).

I have tried to leverage the Era feature by batching the training data by era (1 batch per era), and batching each era-batch into mini-batches since my computer’s ram can’t handle 1 whole era worth of data at once. I trained a model with this method, and it did slightly (very slightly), better (which could just be my deluded brain refusing to believe that it didn’t even if it had the same performance as models trained normally).

Here is the code I used for the pytorch training pipeline:
    
    
    #era column to int
    train_era_indexes = training_data["era"].unique()
    training_data["era"]=training_data["era"].map(lambda a: np.where(train_era_indexes==a)[0][0]+1)
    tourn_era_indexes = tournament_data["era"].unique()
    tournament_data["era"]=tournament_data["era"].map(lambda a: np.where(tourn_era_indexes==a)[0][0]+1)
    #training
    optimizer = torch.optim.Adam(model.parameters(),lr=0.01)
    #epochs
    for e in range(10):
    	#each era
        for era in range(1,training_data['era'].unique().shape[0]+1):
            era_training_data = training_data[training_data['era'] == era]
            x_train = era_training_data[feature_names].to_numpy()
            target_era = era_training_data["target"]
            y_train = target_era.to_numpy()
            batch=get_batch_size(y_train.shape[0])
            x_train = x_train.reshape(-1,batch, 310)
            y_train = y_train.reshape(-1,batch)
            #each epoch within a era
            for era_e in range(3):
                for b in range(x_train.shape[0]):
                    optimizer.zero_grad() 
                    inp = torch.from_numpy(np.array(x_train[b])).float().view(-1,1,310)
                    y_pred = model(inp).float()
                    y_real = torch.from_numpy(np.array(y_train[b])).float().view(-1,1,1)
                    loss = F.mse(y_pred,y_real)
                    loss.backward()
                    optimizer.step()
            #heres where you might print and log some stuff
            print(f'era {era}/epoch {e}- loss: {loss}')
    

There isn’t much more I can think of to leverage the era column as it wouldn’t really be possible to use it to train a time-series model, and I am slightly confused by era-boosting models. It seems as if era-boosting is simply allowing the xgboost model to overfit better to eras that it did bad on. How do fixing bad eras in training really have much of an impact in real life / validation data? What are some tips you’d like to share on the topic of eras? ![:nerd_face:](http://forum.numer.ai/images/emoji/twitter/nerd_face.png?v=9)

---

### Post #2 — **paulito** | 2021-05-11 12:16 UTC

Agree with what you said above. Handling Eras is also something I am still quiet confused about.

I think what most diqualifies the era coloumn as real temporal data is that live data does not reveal its era, so its basically not useable for live prediction and therefore useless. Since validation data contains eras and eras are the following 28 eras after the 120 training eras, a time-series model would be able to yield meaningful predictions. But since this does not apply to live data I don’t see, how this holds any value.

I think eras could potentially be used for feature engineering, but I am still figuring out how this might work. This becomes even harder, because feature aggregates across eras are more ore less identical. If you would find a heuristic that allows to infer which era is in live data and what temporal relation it has to train and validation, that would maybe work. But sure no easy thing to do.

IMO the most benefitial ways to use Eras are:

  * Cross Validation (e.g. TimeSeriesSplit, GroupedSplit, Purged Time Series, or something similar based on Eras)
  * Batch Training (as described above)

---

### Post #3 — **ml_is_lyf** | 2021-05-13 17:58 UTC

![](https://avatars.discourse-cdn.com/v4/letter/r/e68b1a/48.png) ryendu:

> `loss = F.mse(y_pred,y_real)`

This is where you can get some performance gains with some improvements. We’re evaluated on our correlation, so why not use correlation in your loss function. Take a look at this post for some tips:

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/forum.numer.ai/mdo/48/3398_2.png)

[Custom loss functions for XGBoost using PyTorch](<http://forum.numer.ai/t/custom-loss-functions-for-xgboost-using-pytorch/960>) [Data Science](</c/data-science/5>)

> Here is some code showing how you can use PyTorch to create custom objective functions for XGBoost. Objective functions for XGBoost must return a gradient and the diagonal of the Hessian (i.e. matrix of second derivatives). Internally XGBoost uses the Hessian diagonal to [rescale the gradient](<https://stats.stackexchange.com/questions/202858/xgboost-loss-function-approximation-with-taylor-expansion>). The Hessian is very expensive to compute, so we replace it with all ones. This basically forces XGBoost to do standard gradient descent rather than the fancier second order version it usually uses. It works… 

In my experience, you still want to include MSE. But theoretically and practically there are merits to including in your loss function the thing we’re evaluated on

Then it becomes clear why you want them ordered by era, as correlation doesn’t make much sense unless you’re looking at an era (tbf trying correlation with random samples could be interesting, but I don’t think it has as good theoretical merits)

You can also train different models on differents eras and then ensemble them

There are actually lots of things you can do with eras, thankfully a lot of helpful have shared their ideas in Arbitrage’s office hours, so make sure to go watch all of them:

![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/f/f2f961d525288bddde31c573b06faec25d0c2a8e.png) [YouTube](<https://www.youtube.com/c/Numerai/videos>) ![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/080e9cd2a5cca45023fa98526e730e058604dd65_2_500x500.jpeg)

### [Numerai](<https://www.youtube.com/c/Numerai/videos>)

An artificial intelligence hedge fund built by a community of anonymous data scientists

Also Arbitrage has some good suggestions about how to use eras in his intro video series:

![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/0/07c72b3c0c148113f508d433a08aef5fc0fb709d_2_690x388.jpeg)

---

### Post #4 — **swarm** | 2021-06-10 01:33 UTC

Hi, I’m new and working on my first model, and naturally I guess eras was the first thing I searched. I haven’t incorporated it into my model yet, but here are some ideas I’m thinking of.

Perhaps instead of using era as a “category” input, one thing could be to subtract the per-era mean from each input before feeding it into a neural network etc. Currently I’m just putting the inputs as is.

Maybe there can be a neural network that identifies type of market per era? Bull, bear, choppy, calm. It doesn’t have to label, it could also encode it as input to another neural network.

So maybe it could take as inputs the per era input means and standard deviations, and maybe it can encode type of market and be used as input into another neural network that acts on the individual samples, or maybe weight between several different types of neural networks.

Or it doesn’t even need to be a neural network, I imagine a rough market would just have large deviations between inputs.

---

### Post #5 — **chaotician** | 2021-06-10 11:28 UTC

The main limitation of how the data features are presented is that ‘id’ which is a unique identifier for an asset is also unique per ‘era’. and therefore one cannot group by asset by era, only universe by era. So unless the features also represent lagged values, one cannot truly model it as a time series per asset.

---

### Post #6 — **ml_is_lyf** | 2021-06-10 17:21 UTC _(reply to #4)_

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/s/9de053/48.png) swarm:

> So maybe it could take as inputs the per era input means and standard deviations

Nice idea, but sounds like you haven’t watched Arbitrage’s series (I would recommend it if not as it’s a good place to start). Unfortunately, the mean and standard deviation of all features are equal for any given era, as discussed at this timestamp:

---

### Post #7 — **gammarat** | 2021-06-10 17:57 UTC _(reply to #3)_

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/m/e56c9b/48.png) ml_is_lyf:

> (tbf trying correlation with random samples could be interesting, but I don’t think it has as good theoretical merits)

I’ve gotten decent results with it. I think the reason is that the distribution of variance in the test and live rounds is significantly different from that of the training data; selecting samples randomly for training helps prevent a model from becoming fixated on structure particular to just a few eras.
