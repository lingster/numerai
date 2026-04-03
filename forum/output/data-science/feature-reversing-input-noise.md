---
title: "Feature reversing input noise"
category: Data Science
url: https://forum.numer.ai/t/feature-reversing-input-noise/1416
created_at: 2021-01-05T21:29:02.284000+00:00
last_posted_at: 2021-05-18T07:00:37.622000+00:00
posts_count: 22
views: 6294
tags: []
---

# Feature reversing input noise

---

### Post #1 — **mdo** | 2021-01-05 21:29 UTC

A powerful way to regularize neural networks is by applying noise during training, whether it be to the inputs, hidden-unit activations, weights, or gradients. An early example of this is additive Gaussian noise applied to the inputs of denoising autoencoders. A more recent example is Dropout, in which multiplicative binomial noise is applied to inputs or hidden unit activations. While training a network to be invariant or robust to these types of noise can be beneficial, such noise lacks structure that we may wish to be invariant/robust to as well. For example, in image classification it is common to randomly generate variants of images in the training set by rotating, rescaling, color shifting, etc. in order to encourage the network to learn classification rules that are invariant to semantically trivial changes in the images. Is there an analogue to this type of data augmentation that could be used with Numerai data? I don’t think there’s anything quite as conceptually clean, but I think we can do better than standard types of noise.  
A major concern when modeling the data is taking on too much feature exposure because a feature could unexpectedly reverse the sign of its correlation with the target and over-dependence on that feature would then wreck prediction performance. Ideally, we would like our models to be robust to feature reversals. It is of course impossible to be completely robust to an extreme (and hopefully unlikely) situation where all of the features reverse their correlation with the target. But I have found that training a network while reversing the sign of a randomly selected 25% of features at each iteration to be quite beneficial during training. The network naturally learns to reduce its maximum feature exposure and tends to spread exposure across many features rather than relying mostly on only a few. Interestingly different choices of network architecture can lead to networks that perform similarly on validation, but have very different feature exposure profiles. Below are plots from four models showing their feature exposure (i.e. feature correlation with prediction per era) for each validation era. It is clear that the exposure patterns are quite different and often strongly opposing. The max feature exposures were also generally < 0.2 which is usually difficult to obtain without explicitly applying a penalty on exposure of applying feature neutralization.  
Try it yourself and let me know what you think. It should be combinable with other ideas as well. I like to follow training using this by further reducing feature exposure as described in my response here: [Model Diagnostics: Feature Exposure - #12 by mdo](<http://forum.numer.ai/t/model-diagnostics-feature-exposure/899/12>)

Practical tips and suggestions:

  * Make sure your features and targets are centered at 0, by subtracting 0.5 from each. (You should already be doing something like this if you’re training neural networks. If not, SHAME!)
  * Use early stopping
  * Use other kinds of noise in your network as well, e.g. DropOut and/or the CoupledGaussianDropout I invented and put below because I’m feeling generous
  * Use eras as mini-batches
  * Try different optimizers. I really like Follow The Moving Leader (easily found using Google for your favorite NN framework)
  * Experiment with different architectures, standard feedforward and nets with residual connections work IME
  * I like training neural networks like making good BBQ: low (learning rate) and slow (many epochs)



**

[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/04dd87024a369a1321e9352090a7a17eb235a018.png)849×231 25.9 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/04dd87024a369a1321e9352090a7a17eb235a018.png>)

**  
**

[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/3b0487275d71ed9975b4a1c5dd3bec65d2a0ee0a_2_624x169.png)849×231 26.3 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/3b0487275d71ed9975b4a1c5dd3bec65d2a0ee0a.png>)

**  
**

[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/107b6d12d71c7f4b87e4a6434f615834d8b45379_2_624x169.png)849×231 26.3 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/107b6d12d71c7f4b87e4a6434f615834d8b45379.png>)

**  
**

[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/f8fa1858982b383f170098ae54ec2c3f2cce545a.png)849×231 26 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/f8fa1858982b383f170098ae54ec2c3f2cce545a.png>)

**
    
    
    ## To be used on input to neural network. Make sure input is centered at 0!
    class FeatureReversalNoise(nn.Module):
        def __init__(self, p=0.25):
            super(FeatureReversalNoise, self).__init__()
            if p < 0 or p > 1:
                raise ValueError("probability has to be between 0 and 1, " "but got {}".format(p))
            self.p = p
    
        def forward(self, x):
            if self.training:
                binomial = torch.distributions.binomial.Binomial(probs=1-self.p)
                noise = 2*binomial.sample((1,x.shape[1])) - 1
                return x * noise.cuda()
            else:
                return x
    
    
    
    # This is used to add noise to neural net activations. It differs from the Gaussian Dropout suggested
    # in the original Dropout paper in that the scale of the noise is proportional to the activation such
    # that activation level equals the variance of noise (times alpha). Kinda like how real neurons have 
    # Poisson-ish noise
    class CoupledGaussianDropout(nn.Module):
        def __init__(self, alpha=1.0):
            super(CoupledGaussianDropout, self).__init__()
            self.alpha = alpha
    
        def forward(self, x):
            if self.training:
                stddev = torch.sqrt(torch.clamp(torch.abs(x), min=1e-6)).detach()
                epsilon = torch.randn_like(x) * self.alpha
    
                epsilon = epsilon * stddev
    
                return x + epsilon
            else:
                return x

---

### Post #2 — **mdo** | 2021-01-05 23:45 UTC

Also rather than choose one of the four models above, I ensembled them all, along with my XGBoost model (⅕ weight each) to produce a final prediction and then reduced maximum feature exposure down to 0.075. Given the good validation performance I was seeing for this model, I uploaded it under my NMRO account for round 245. The metrics are below and overall look better than any other model I have, so I’m fairly optimistic about it. (The exposure number below is higher than 0.075 because I reranked the predictions after doing the exposure reduction optimization)

**

[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/2df40801fdcbd2dcdb26849d0b6cd23f97543979_2_301x500.png)347×577 22.5 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/2df40801fdcbd2dcdb26849d0b6cd23f97543979.png>)

**

---

### Post #3 — **loracle** | 2021-01-06 10:33 UTC _(reply to #2)_

With such a high val mean and low feature exposure, I would expect MMC to be a lot higher, that’s surprising.

---

### Post #4 — **senadorancap** | 2021-01-07 00:08 UTC

Hi, it’s me! The craziest brazilian newbie ever.

I’m from the ghetho and ghettoboys don’t have enough compute power to run those Michael Oliver’s super cool NNs. But i have imagination and had prepared some adjustment for those folks like me who are taking limited computing power but still wanna get rich… i mean improve the metamodel of course.

What i did was took the Michael Oliver’s idea and consider as a general regularization method than can be perfectally used with a boosted trees algorithm (for example), i also noticed that the conceptual structure fits well with the boosted eras algorithm.

So those are my adaptions:

  * Forget NN’s and special custom loss functions, ghetoboys uses XGBoost and classical Feature Neutralization

  * Before you start with the random reversing thing you can train your XGBoost for some iterations (50, 100 or 200 is enough), as a kind of bootstrap or something

  * And when doing the random reversing training part you can iterate for more than just one time before reversing random features again. That’s why a said that “fits well with the boosted eras algorithm”




Ok, so taking those adjustments i was able to produce this little guy here:

[![lg](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/061702a360927dda7639aca5b260e8d3902e5063_2_213x375.png)lg290×509 17.4 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/061702a360927dda7639aca5b260e8d3902e5063.png> "lg")

I’ve made a function for doing the reversing thing (in R):
    
    
    random_slicer <- function(features, slice_percent){
    
    train_slice <- features[,4:313]
    feat_list <- sort(sample(1:310,round(310*slice_percent)))
    
     for(i in length(feat_list)){
        train_slice[,feat_list[i]] <- (-1)*(train_slice[,feat_list[i]] - 0.5) + 0.5
        }    
     train_slice  
    }

---

### Post #5 — **mdo** | 2021-01-07 00:57 UTC _(reply to #4)_

Very nice! I was hoping someone would try this with XGBoost as well ![:grinning:](http://forum.numer.ai/images/emoji/twitter/grinning.png?v=9) Looks like you got it working pretty nicely and have a great Feature Neutral Mean score, congrats!

---

### Post #6 — **senadorancap** | 2021-01-08 12:43 UTC

Thank you Michael. Hope contribute more with the community by the next months and years, my quant skills became extremely more professionals after i’ve joined the tournament as an active community’s member. So i still have a lot to retribute!

I’ll work on something new related whith this method, gonna share if succed.

For now i have to provide the Diagnostics A/B test for i’ve done in the results of my previous reply. By the left is the model without the technique and on the rigth the model with the technique. Both with the same xgb parameters, total iterations and 100% FN.

[![lg_base](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/618a776560fd1e2a2ce4f7b674b8f2374cfeaa85_2_144x250.png)lg_base295×511 17.5 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/618a776560fd1e2a2ce4f7b674b8f2374cfeaa85.png> "lg_base")

[![lg](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/061702a360927dda7639aca5b260e8d3902e5063_2_142x250.png)lg290×509 17.4 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/061702a360927dda7639aca5b260e8d3902e5063.png> "lg")

Regards  
Eric Reis

---

### Post #7 — **sirbradflies** | 2021-01-11 17:14 UTC

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/forum.numer.ai/mdo/48/3398_2.png) mdo:

> Make sure your features and targets are centered at 0, by subtracting 0.5 from each. (You should already be doing something like this if you’re training neural networks. If not, SHAME!)

Hi MDO,

Thanks for the interesting post. Regarding the feature and target centering when using NN shouldn’t this step be unnecessary if the NN layers have biases?

Thanks

---

### Post #8 — **mdo** | 2021-01-11 19:23 UTC _(reply to #7)_

It generally helps convergence since you don’t have to move biases as much and in this case you really want them to be centered if you’re multiplied by -1.

---

### Post #9 — **jeremy_berros** | 2021-01-20 21:28 UTC

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/forum.numer.ai/mdo/48/3398_2.png) mdo:

> I like training neural networks like making good BBQ: low (learning rate) and slow (many epochs)

This last statement almost sounds like a commercial from Arby’s ![:cut_of_meat:](https://emoji.discourse-cdn.com/twitter/cut_of_meat.png?v=15) ![:cowboy_hat_face:](https://emoji.discourse-cdn.com/twitter/cowboy_hat_face.png?v=15)

---

### Post #10 — **halsmith99** | 2021-02-12 13:06 UTC _(reply to #2)_

is this still running in NMRO? rd 245 resolution didn’t look too good.

---

### Post #11 — **mdo** | 2021-02-12 18:30 UTC _(reply to #10)_

Judging anything based on one round is a bad idea. The recent rounds have also been especially weird.

---

### Post #12 — **wtd** | 2021-02-16 13:45 UTC

These are great insights!

I’ve been working with XGBoost and sklearn a bit on numerai data, but I’m new to PyTorch.

Any pointers on how would I go about creating the mini batches from the eras as you suggest?

---

### Post #13 — **silentj** | 2021-02-17 10:27 UTC

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/forum.numer.ai/mdo/48/3398_2.png) mdo:

> Use eras as mini-batches

Thank you for the tips!  
What is the intuition behind eras as mini-batches? Wouldn’t we want each step to be in the direction of lower loss values in more eras, as opposed to one era? I’ve been using quite large batches on shuffled data and it seemed to result in better risk metrics performance over non-shuffled data (which is different than eras as mini-batches but similar)

---

### Post #14 — **wtd** | 2021-02-19 17:37 UTC

Can anyone point to some code with pytorch where we use the eras as mini batches? Been cracking my head about this for 1 week now.

---

### Post #15 — **belzebot** | 2021-02-21 19:45 UTC _(reply to #14)_

eras = df.era.unique()
    np.random.shuffle(eras)
    for era in eras:
       dfs = df[df.era == era]
       x = torch.from_numpy(dfs[features].values).float()
       y = torch.from_numpy(dfs.target.values).float()

---

### Post #16 — **javiermoral** | 2021-05-10 15:40 UTC

Can a kind soul share the code that generates the mini batches by iterating through eras for a Keras model?

---

### Post #17 — **nyuton** | 2021-05-11 08:02 UTC _(reply to #16)_

class DataSequence(tf.keras.utils.Sequence):
    
        def __init__(self, df, features, erasPerBatch=1, shuffle=True):
            self.df = df
            self.features = features
            self.shuffle = shuffle
            self.eras = df.era.unique()
            
            if self.shuffle == True:
                np.random.shuffle(self.eras)
                
            self.erasPerBatch = erasPerBatch
            
            self.df['target_aux'] = self.df[target]
            
      
        def __len__(self):
            return len(self.eras) // self.erasPerBatch
    
        def on_epoch_end(self):
            if self.shuffle == True:
                self.df = self.df.sample(frac=1).reset_index(drop=True)
                np.random.shuffle(self.eras)
    
    
        def __getitem__(self, idx):
    
            myEras = []
           
            for i in range(self.erasPerBatch):
                myEras.append( self.eras[idx*self.erasPerBatch+i] )
            
            #print(myEras)
                              
            X = self.df.loc[self.df.era.isin(myEras), self.features].values
            y = self.df.loc[self.df.era.isin(myEras), self.features + ['target_aux', 'target']].values
            
            X = np.split(X, X.shape[1], axis=1)
            y = np.split(y, y.shape[1], axis=1)
            
          
            return X, y

---

### Post #18 — **paulito** | 2021-05-11 08:22 UTC

you say you use residual layers, which I would suppose need some temporal dimension. Do you use eras as temporal information? If so, what is your reasoning about having no information about the era for the live data? Is there another way to implement rnns without temporal dimension (which would seem weird to me), or is there a heuristic how you infer the live era?

---

### Post #19 — **olivepossum** | 2021-05-16 08:30 UTC

Hi [@mdo](</u/mdo>) when you mention nets with residual connections you mean to skip connections? Would this forward function represent it or you are referring to more complex nets with Blocks and Bottlenecks?
    
    
      def forward(self, x):
          x = self.linear0(x)
          x1 = x 
          x = F.relu(x)
          x = self.dropout(x)
          x = F.relu(self.linear1(x))
          x = self.dropout(x)
          x = F.relu(self.linear2(x))
          x = self.dropout(x)
          x = F.relu(self.linear3(x))
          x = self.dropout(x)
          x = torch.add(x, x1)
          x = F.relu(self.linear4(x))
          x = self.sigmoid(x)
          return x
    

Thanks!

---

### Post #20 — **greenprophet** | 2021-05-17 18:20 UTC _(reply to #19)_

[@olivepossum](</u/olivepossum>) I would look to use torch.cat or max pooling instead of torch.add. Cat is more versatile to a bunch of output dimensions.

---

### Post #21 — **mdo** | 2021-05-17 18:58 UTC _(reply to #20)_

[@olivepossum](</u/olivepossum>) [@greenprophet](</u/greenprophet>) `add` and `cat` would do different things, `add` is what the residual networks typically use. I usually just do it as `x = x + x1`  
Also you have two nonlinearities back-to-back at the end there, a `relu` followed by a `sigmoid`, which I’m guessing is probably not what you want, unless for some reason you want your outputs to be between 0.5 and 1

---

### Post #22 — **olivepossum** | 2021-05-18 07:00 UTC _(reply to #21)_

[@mdo](</u/mdo>) thanks for the clarification and to point to the two back-to-back nonlinearities, as you mentioned it’s not what I wanted.

Thanks!
