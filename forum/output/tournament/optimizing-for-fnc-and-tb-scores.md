---
title: "Optimizing for FNC and TB scores"
category: Tournament
url: https://forum.numer.ai/t/optimizing-for-fnc-and-tb-scores/5132
created_at: 2022-03-22T22:21:59.244000+00:00
last_posted_at: 2022-05-26T21:42:01.254000+00:00
posts_count: 32
views: 6613
tags: []
---

# Optimizing for FNC and TB scores

---

### Post #1 — **mdo** | 2022-03-22 22:21 UTC

With the advent of TC many users may wonder how to optimize for metrics beyond correlation and mean-squared error. Here we will show how to directly optimize for metrics like TB200 and FNC. This is intended to be a proof of concept and source of inspiration, not a set of instructions.

A previous [forum post](<http://forum.numer.ai/t/differentiable-spearman-in-pytorch-optimize-for-corr-directly/2287>) demonstrated how to optimize for Spearman correlation directly. This work can be extended fairly simply to allow for the optimization of a top/bottom correlation (e.g. TB200) where only the most extreme values of the prediction are used in the correlation function.
    
    
    import torch
    import pandas as pd
    import numpy as np
    import torchsort
    from torch.distributions import Normal
    from torch.functional import F
    import torch.optim as optim
    from torch import nn
    
    normal = Normal(0,1)
    
    def numerair_tb(pred, target, tb=None, gaussianize=False, regularization_strength=.0001):
        # Computes and returns a differentiable Numerai score with option to use only 
        # the top and bottom tb values. Use the gaussianize option to perform Gauss-rank 
        # instead of just rank transform on predictions
        
        pred = pred.reshape(1, -1)
        target = target.reshape(1, -1)
        
        # get sorted indicies
        rr = torchsort.soft_rank(pred, regularization_strength=regularization_strength)
        
        # change pred to uniform distribution
        pred = (rr - .5)/rr.shape[1]
        
        # convert uniform to gaussian distribution
        if gaussianize:
            pred = normal.icdf(pred)
            
        # select top/bottom indices
        if tb is not None:
            tbidx = torch.bitwise_xor(rr<=tb, rr > (rr.shape[1]-tb))
            pred = pred[tbidx]
            target = target[tbidx]
        
        # Pearson correlation
        pred = pred - pred.mean()
        pred = pred / pred.norm()
        target = target - target.mean()
        target = target / target.norm()
        return (pred * target).sum()
    

If we want to control feature exposure of the top/bottom part of the signal, it can be helpful to have the correlation function return this exposure as well so it can be incorporated into the overall cost function. A modified version of the above to return the total feature exposure:
    
    
    import torch
    import pandas as pd
    import numpy as np
    import torchsort
    from torch.distributions import Normal
    from torch.functional import F
    import torch.optim as optim
    from torch import nn
    
    normal = Normal(0,1)
    
    def numerai_r_tb_exposure(pred, target, features, tb=None, gaussianize=False, regularization_strength=.0001):
        # Computes and returns a Numerai score and feature exposure
        
        pred = pred.reshape(1, -1)
        target = target.reshape(1, -1)
        
        # get sorted indicies
        rr = torchsort.soft_rank(pred, regularization_strength=regularization_strength)
        # change pred to uniform distribution
        pred = (rr - .5)/rr.shape[1]
        
        # convert uniform to gaussian distribution
        if gaussianize:
            pred = normal.icdf(pred)
            
        # select top/bottom indicies
        if tb is not None:
            tbidx = torch.bitwise_xor(rr<=tb, rr > (rr.shape[1]-tb))
            pred = pred[tbidx]
            target = target[tbidx]
            features = features[tbidx[0]]
        
        # Pearson correlation
        pred = pred - pred.mean()
        pred = pred / pred.norm()
        target = target - target.mean()
        target = target / target.norm()
        
        return (pred * target).sum(), ((pred @ features)**2).sum()
    

We can use the above cost functions to compute CORR and TB scores as well as feature penalty terms. The inclusion of a differentiable version of the psudoinverse in Pytorch, means we can feature-neutralize a model’s predictions and directly optimize for FNC as well. Now we will show how to train a simple neural network on a cost function optimizing for FNC, FNC TB500, CORR, while penalizing feature exposure in the prediction and the top/bottom 500 of the neutralized prediction. (We’ve found TB500 a bit more stable to use for optimization as TB200 tends to overfit easily.) We initialize a simple neural network like:
    
    
    class Net(nn.Module):
        def __init__(self):
            super(Net, self).__init__()
            self.lin1 = nn.Linear(1050, 100)
            self.lin2 = nn.Linear(100, 30)
            self.lin3 = nn.Linear(30, 1)
            self.bn = nn.BatchNorm1d(1)
            self.do1 = nn.Dropout(0.5)
            self.do2 = nn.Dropout(0.5)
    
        def forward(self, x):
            x = self.lin1(x)
            x = self.do1(F.mish(x))
            x = self.lin2(x)
            x = self.do2(F.mish(x))
            output = self.bn(self.lin3(x))
            return output
    

We can then set up a training loop as follows to optimize for this multi-part cost function.
    
    
    for epoch in range(epochs):
        np.random.shuffle(era_list)
        for ii, era in enumerate(era_list):
            # get features and target from data and put in tensors
            features = torch.tensor(training_data[training_data.era == era].filter(like='feature').values) - .5
            target = torch.tensor(training_data[training_data.era == era]['target'])
    
            # zero gradient buffer and get model output
            optimizer.zero_grad()
            model.train()
            output = model(features)
    
            # neutralize model output
            b = features.pinverse(rcond=1e-6) @ output
            linear_pred = features @ b
            neutralized_output = output - linear_pred
    
            
            neut_tb_loss, neut_tb_exp = numerai_r_tb_exposure(neutralized_output, target, features, tb=500)
            neut_loss = numerair_tb(neutralized_output, target)
            orig_loss, orig_exp = numerai_r_tb_exposure(output, target, features)
            
            # loss = -tb500 corr for neutralized output - corr for neutralized output - corr + tb500 exposure + exposure
            loss = -neut_tb_loss - neut_loss - orig_loss \
                    + neut_tb_exp/1e3 + orig_exp/1e4
    
            loss.backward()
            optimizer.step()
    

We’ve trained a model using this code and have submitted it [here](<https://numer.ai/covid19>). The validation statistics for this model are here. Again this is far from optimized and is meant only to show what is possible, but it seems fairly decent already. Cheers and good luck!

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/0/0c763b3a4d05e29f8518f38a2072e8e06e561fe1_2_690x209.png)image750×228 26.3 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/0/0c763b3a4d05e29f8518f38a2072e8e06e561fe1.png> "image")

  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/6/626e4dfa703a68596ab1ec704fea5c4e3e054248_2_690x156.png)image749×170 22.8 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/6/626e4dfa703a68596ab1ec704fea5c4e3e054248.png> "image")

---

### Post #2 — **perfect_fit** | 2022-03-23 12:03 UTC

Awesome! I suppose the same process can be applied when optimizing for FNCv3? Do I understand correctly that the only difference is the feature set we are neutralizing against?

---

### Post #3 — **mdo** | 2022-03-23 17:16 UTC _(reply to #2)_

Yup that is correct. The old FNC was using the old 310 features.

---

### Post #4 — **perfect_fit** | 2022-03-23 19:08 UTC _(reply to #3)_

That’s clear, thank you!

---

### Post #5 — **bguberfain** | 2022-03-24 15:04 UTC

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/forum.numer.ai/mdo/48/3398_2.png) mdo:

> `for ii, era in enumerate(era_list):`

Thanks for sharing! I was wondering if there is any special meaning on training per era, like if the loss functions only make sense when used this way.

Do you think that a random batch or more than one era per batch would penalize the convergence of the model?

---

### Post #6 — **mdo** | 2022-03-24 15:38 UTC _(reply to #5)_

Feature neutralization makes the most sense on a per-era basis.

---

### Post #7 — **olivepossum** | 2022-03-24 21:44 UTC _(reply to #2)_

What number of features does include FNCv3? And v2 and v1?

Thanks!

---

### Post #8 — **gbrecht** | 2022-03-25 07:15 UTC _(reply to #7)_

FNCv3 is the 420 features of the “medium” featureset they released.  
On RC they announced that code for FNCv3 will be released soon

---

### Post #9 — **gbrecht** | 2022-03-25 07:17 UTC

[@mdo](</u/mdo>) What is the purpose of the gaussianize switch? What effect would it have to make the uniform distribution of the prediction a gaussian distribution?

---

### Post #10 — **olivepossum** | 2022-03-25 15:53 UTC

When using validation data for early stopping, does it make sense to do use eras as batches or shouldn’t make a difference there?  
Thanks!

---

### Post #11 — **gbrecht** | 2022-03-25 18:36 UTC _(reply to #10)_

You do check for early stopping at the end of an epoch, right?  
If so, I say it is a good idea to use era-batches for training.

---

### Post #12 — **olivepossum** | 2022-03-25 19:25 UTC _(reply to #11)_

> You do check for early stopping at the end of an epoch, right?  
>  Yes, I do. At the end of each epoch I use validation data to check for early stopping. My doubt is if I should calculate the total loss on the validation data by using batches per era there or it does not really matter (I would use per era batches with the train data but not for the validation_data used for early stopping).

---

### Post #13 — **gbrecht** | 2022-03-25 19:47 UTC _(reply to #12)_

you calculate the corr score per era but I do not see a reason why you should predict in batches.

---

### Post #14 — **olivepossum** | 2022-03-25 23:49 UTC _(reply to #13)_

My doubt is if at the end of each training epoch, it makes sense to do an early stopping check using validation data with validation eras like this:
    
    
    def validation_early_stopping(val_data, model):
        model.eval()
        era_list = eras_validation.unique()
        np.random.shuffle(era_list)
        batch_count = 0
        acc_loss_val = 10000
        
        with torch.no_grad(): 
          for era in era_list:
              batch_count += 1
              # get features and target from data and put in tensors
              features = torch.tensor(val_data[val_data.erano == era].filter(items=feature_names).values) - .5
              target = torch.tensor(val_data[val_data.erano == era]['target'])
              features = features.cuda()
              target = target.cuda()
    
              output = model(features)
              
              # neutralize model output
              b = features.pinverse(rcond=1e-6) @ output
              linear_pred = features @ b
              neutralized_output = output - linear_pred
    
              neut_tb_loss, neut_tb_exp = numerai_r_tb_exposure(neutralized_output, target, features, tb=500)
              neut_loss = numerair_tb(neutralized_output, target)
              orig_loss, orig_exp = numerai_r_tb_exposure(output, target, features)
              
              loss = -neut_tb_loss - neut_loss - orig_loss + neut_tb_exp/1e3 + orig_exp/1e4
              
              acc_loss_val += loss
    
          loss_val = acc_loss_val / batch_count
          return loss_val.item()
    
    

As we are using TB500, I’m not sure if the size or the composition of the validation batches matters here of if it’s even conceptually correct to check early stopping like this in this case.

---

### Post #15 — **dzheng1887** | 2022-03-26 21:56 UTC

Would there be an update soon for the numerai tournament? I wasn’t sure if something had already changed but I did not notice. I am not sure where to go for big notices like that.

---

### Post #16 — **pumplerod** | 2022-03-28 00:25 UTC _(reply to #14)_

Perhaps I misunderstand the meaning for TB500. I believe that to reference the Top/Bottom 500 prediction values. This is indeed a smaller subset than the full era, however in the code it looks like the TB500 samples are being used in their neutralized form as an addition to the full set of sample losses. Effectively adding extra pressure to the top and bottom 500 to improve performance.

Unless I’m reading this code incorrectly ( very possible), the `neut_loss` ( effectively the corr for the entire set of neutralized predictions) and the `orig_loss` ( corr for the entire set of raw predictions) are being maximized due to the “-” when they are included in the final `loss` calculation. This is also where the additional loss from the tb500 are included.

If I’m reading this wrong however, I would love a clear breakdown of the process.

---

### Post #17 — **mdo** | 2022-03-28 19:11 UTC _(reply to #16)_

Sounds like you’ve got it!

---

### Post #18 — **pumplerod** | 2022-04-05 16:42 UTC _(reply to #17)_

[@mdo](</u/mdo>) if Numerai is performing Feature Neutralization on our predictions before TC calculations, would it not help to know which features the team is using to neutralize with? As Numerai is not aware of which features we may have used to generate predictions, how have they determined the best features to use in neutralization? Or do they use them all?

I see above a mention:

> FNCv3 is the 420 features of the “medium” featureset they released.  
>  On RC they announced that code for FNCv3 will be released soon

is this information public somewhere? I don’t find it on ‘Neutralization’ section of the Docs.

---

### Post #19 — **mdo** | 2022-04-06 23:55 UTC _(reply to #18)_

Predictions are **not** neutralized before TC calculations, just Gauss-rank transformed.

---

### Post #20 — **wigglemuse** | 2022-04-07 03:36 UTC _(reply to #19)_

Isn’t neutralization part of the optimizer though?

---

### Post #21 — **profricecake** | 2022-04-07 05:52 UTC

Hi [@mdo](</u/mdo>) and [@jrb](</u/jrb>), I have a question about calculating exposure.

Earlier in this thread [@mdo](</u/mdo>) uses this:

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/forum.numer.ai/mdo/48/3398_2.png) mdo:

> 
>     ((pred @ features)**2).sum()
>     

And in a different thread ([Model Diagnostics: Feature Exposure](<http://forum.numer.ai/t/model-diagnostics-feature-exposure/899>)) [@jrb](</u/jrb>) used something a little different:

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/forum.numer.ai/jrb/48/2767_2.png)[Model Diagnostics: Feature Exposure](<https://forum.numer.ai/t/model-diagnostics-feature-exposure/899/1>)

> 
>     def feature_exposures(df):
>         feature_names = [f for f in df.columns
>                          if f.startswith("feature")]
>         exposures = []
>         for f in feature_names:
>             fe = spearmanr(df[PREDICTION_NAME], df[f])[0]
>             exposures.append(fe)
>         return np.array(exposures)
>     
>     def feature_exposure(df):
>         return np.sqrt(np.mean(np.square(feature_exposures(df))))
>     
>     

Both go up as exposure goes up, and both stop at zero if exposure is zero. But to me, [@jrb](</u/jrb>)’s version has the nice additional quality of being bound to lie between 0-1.0 no matter how many features are being considered.

Are there other reasons you might choose one over the other? Such as accuracy, or speed, or … ?

Thanks,

prc

---

### Post #22 — **richai** | 2022-04-09 01:45 UTC _(reply to #20)_

Yes “penalization” of features is part of the optimizer. We allow some feature exposure but not a lot. Actually the reason we gave FNCv3 is because those are the features the optimizer is penalizing. But this is obviously a lot else going on in the optimizer to which affects TC.

---

### Post #23 — **wigglemuse** | 2022-04-09 03:46 UTC _(reply to #22)_

Why this might be important from a user perspective is that it seems (to me anyway) that since we can still bet on CORR as well as TC, we can unquestionably get higher CORR on average with less neutralized predictions. However, neutralization may help with TC. But if the neutralization is happening anyway as part of the process, then maybe we can get away with submitting unneutralized predictions, i.e. we don’t have to do that neutralization ourselves. So if submitting unneutralized preds vs submitting preds neutralized to the FNCv3 set are substantially the same in terms of the resulting TC scores, then unneutralized is the way to go because that will get higher corr results (in general). Whether that’s actually true or not (neutralized vs unneutralized getting more or less equal TC) depends on the order of operations in the whole TC/optimizer process I suppose.

---

### Post #24 — **richai** | 2022-04-09 03:51 UTC _(reply to #23)_

I think that’s a fine approach. I think you can reduce the TC of a model with feature neutralization. Because the optimizer does some penalization not full neutralization so some exposure to features will help if those features work on live (especially ones the Meta Model is not already exposed to). MDO showed in the past the optimal level of feature neutralization did not appear to be 100%. I think it’s good to have models with high FNC and high CORR. I think it’s models with super high CORR due to one huge feature exposure that the Meta Model already has exposure to that can do very well on CORR in some rounds but get very negative TC.

---

### Post #25 — **olivepossum** | 2022-04-21 20:00 UTC

[@mdo](</u/mdo>) you are centering features at 0 but not the targets (or I don’t see where). What would be the reason to not apply the -.5 also to the targets?

---

### Post #26 — **mdo** | 2022-04-21 23:45 UTC _(reply to #25)_

The loss is correlation based and is centering the target as part of the formula.

---

### Post #27 — **sneaky** | 2022-04-27 07:19 UTC

I didn’t like the idea to neutralize every backprob, because neutralization is very slow on my pc. So I though what would happen if I would neutralize the target instead of neutralizing the predictions. I neutralized only the target in the training data and left the validation target unchanged. I didn’t train the models fully, so it is possible that they can flip later in the training.

Validation [edited version - without bug hopefully]:  


[![Screenshot from 2022-04-29 17-51-47](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/f/f5d72411f42708d89d211cd46960489591df36ab.png)Screenshot from 2022-04-29 17-51-47530×125 9.33 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/f/f5d72411f42708d89d211cd46960489591df36ab.png> "Screenshot from 2022-04-29 17-51-47")

_Version of data: V4_  
_Validation data: eras that were validation eras in V3_  
_Training data: All eras - Valuation eras_  
_Loss: mean erawise rank correlation_  
_Number of iterations: 1000 (low, I usually train 20000+)_  
_Model: LGBM_

---

### Post #28 — **miguelpf** | 2022-05-15 13:53 UTC

[@mdo](</u/mdo>) in your code you have:
    
    
    rr = torchsort.soft_rank(pred, regularization_strength=regularization_strength)
    # change pred to uniform distribution
    pred = (rr - .5)/rr.shape[1]
    

However this is assuming that rr returns the ranked results from 0…size-1, after installing torchsort and trying a couple of times I was surprised to see that the soft_rank returns a ranking that not necessarily starts at 0.

Check the following tests:
    
    
    import pytest
    import torch
    from torchsort import soft_rank, soft_sort
    
    
    def test_less_than_one_numbers():
        z = torch.tensor([[0.4385, 0.4385, 0.4385, 0.5649]])
        ranked = soft_rank(z)
        print(ranked)
        assert ranked.min() == 0
    
    
    def test_bigger_than_one_numbers():
        z = torch.tensor([[5000, 10, 20, 34, ]])
        ranked = soft_rank(z)
        print(ranked)
        assert ranked.min() == 0
    
        ranked = soft_rank(torch.tensor([[5000, 5000, 10, 20, 5000, 34, 10, 20, 34, ]]))
        print(ranked)
        assert ranked.min() == 0
    
    def test_mix_big_small_numbers():
        z = torch.tensor([[5000, 10, 0.01, 0.4385, 0.5649, 20, 34, ]])
        print(soft_rank(z))
        ranked = soft_rank(z)
        assert ranked.min() == 0
    

This makes the correlation unrealiable I think, can you tell me exactly which library did you use for torchsort?  
I’m using [torchsort · PyPI](<https://pypi.org/project/torchsort/>) for this tests.

Also, in ```  
pred = (rr - .5)/rr.shape[1]
    
    
    Any help to understand all this is greatly appreciated.

---

### Post #29 — **mdo** | 2022-05-15 18:29 UTC _(reply to #28)_

The output of soft_rank depends on the scale of the input. You need to adjust the `regularization_strength` parameter to make it give sensible results for the scale of your input data.

---

### Post #30 — **miguelpf** | 2022-05-17 09:44 UTC _(reply to #29)_

Thank you, you are right, I have perform more experiments to see the effect of the regularization_strength,  
my conclusion is that while regularization_strength approximates it more to a hard ranking it doesn’t guarantee a hard ranking. On the contrary there are cases where two things happen, the starting value for the soft ranking >> 0 and second the difference between consecutive values !=1.

With that in mind I have the following comments:

  1. 

    
    
    pred = (rr - .5)/rr.shape[1]  
    

rr starts at a random number between 0 and len(pred) substracting .5 doesn’t make sense  
dividing by rr.shape[1] does restrict the range to 0…1

* * *

  2. 

    
    
        if tb is not None:
            tbidx = torch.bitwise_xor(rr<=tb, rr > (rr.shape[1]-tb))  ## problem
    

rr is soft ranking, we cannot rely on the ranking starting at 0 and increasing by 1. Therefore the masking  
is not neccesarily working.

---

### Post #31 — **olivepossum** | 2022-05-26 10:33 UTC

Hi,

After reading the post, I thought it could also be interesting to add feature dissimilarity to the loss calculation. As I’m not sure how to compute the dataframe’s .corrwith(…) function with pytorch, I implemented a very inefficient approach that can not run on GPU (just using numpy and not the pytorch tensor tools).  
Any feedback on the idea or how to implement it properly?
    
    
    for f in feature_cols:
      train_data[f] -= 0.5
    
    for epoch in range(epochs):
        np.random.shuffle(era_list)
        batch_count = 0
        acc_loss_train = 0
        for era in era_list:
            batch_count += 1
    
            # get features and target from data and put in tensors
            features = torch.tensor(train_data[train_data.erano == era].filter(like='feature').values)
            target = torch.tensor(train_data[train_data.erano == era]['target'])
    
            # zero gradient buffer and get model output
            optimizer.zero_grad()
            model.train()
            model_output = model(features)
    
            orig_loss = -numerair_tb(model_output, target)
    
            #dissimilarity
            train_era = train_data[train_data.erano == era]
            example_preds = train_era[example_col].values 
            example_preds = (example_preds - np.mean(example_preds)) / np.std(example_preds)
    
            train_era['example_preds'] = example_preds
            train_era['preds'] = model_output.numpy()
    
            u = train_era[feature_cols].corrwith(train_era['preds'])
            e = train_era[feature_cols].corrwith(train_era['example_preds'])
            dissimilarity = np.sum((np.dot(u,e)/np.dot(e,e)))
    
            #final loss
            loss = - orig_loss + torch.tensor(dissimilarity)
    
            acc_loss_train += loss 
            loss.backward()
            optimizer.step()
    
        loss_train = acc_loss_train / batch_count

---

### Post #32 — **olivepossum** | 2022-05-26 21:42 UTC _(reply to #31)_

Think I came up with an implementation that would work on GPU as uses PyTorch. However, reading this post [True Contribution Details](<http://forum.numer.ai/t/true-contribution-details/5128>), exposure dissimilarity seems to be relevant just combined with FNCv3 on a multiplicative way so it might not make sense to use it without it.  
Any feedback is more than welcome!
    
    
    for f in feature_cols:
      train_data[f] -= 0.5
    
    for epoch in range(epochs):
        np.random.shuffle(era_list)
        batch_count = 0
        acc_loss_train = 0
        for era in era_list:
            batch_count += 1
    
            # get features and target from data and put in tensors
            features = torch.tensor(train_data[train_data.erano == era].filter(like='feature').values)
            target = torch.tensor(train_data[train_data.erano == era]['target'])
    
            # zero gradient buffer and get model output
            optimizer.zero_grad()
            model.train()
            model_output = model(features)
    
            orig_loss = -numerair_tb(model_output, target)
    
            #dissimilarity
            train_era = train_data[train_data.erano == era]
    
            example_preds = torch.as_tensor(train_era['example_preds'].values) #Needs to be created previously
            example_preds = example_preds - example_preds.mean()
            corr_example_preds = (features.T * example_preds).sum(dim=1) / ((features.T * features.T).sum(dim=1) * (example_preds * example_preds).sum()).sqrt()
    
            preds = model_output
            preds = preds - preds.mean()
            corr_preds = (features.T * preds).sum(dim=1) / ((features.T * features.T).sum(dim=1) * (preds * preds).sum()).sqrt()
    
            num = corr_preds.pinverse(rcond=1e-6).dot(corr_example_preds)
            denom = corr_example_preds.pinverse(rcond=1e-6).dot(corr_example_preds)
    
            dissimilarity = (num/denom).sum()
    
            #final loss
            loss = - orig_loss + dissimilarity
    
            acc_loss_train += loss 
            loss.backward()
            optimizer.step()
    
        loss_train = acc_loss_train / batch_count
