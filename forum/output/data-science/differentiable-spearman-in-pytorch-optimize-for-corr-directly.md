---
title: "Differentiable Spearman in PyTorch (Optimize for CORR directly)"
category: Data Science
url: https://forum.numer.ai/t/differentiable-spearman-in-pytorch-optimize-for-corr-directly/2287
created_at: 2021-03-11T04:21:12.891000+00:00
last_posted_at: 2023-11-07T23:21:51.291000+00:00
posts_count: 31
views: 25220
tags: []
---

# Differentiable Spearman in PyTorch (Optimize for CORR directly)

---

### Post #1 — **teddykoker** | 2021-03-11 04:21 UTC

[@mdo](</u/mdo>) previously showed how to use a [custom loss function](<http://forum.numer.ai/t/custom-loss-functions-for-xgboost-using-pytorch/960>) which involved taking the gradient of the sharpe ratio of the Pearson correlations over different eras. Although Pearson and Spearman might return similar values, it _could_ be rewarding to optimize for Spearman directly (or Sharpe of Spearman). Since the ranked Spearman correlation needs a sort operation (which is not differentiable), it has not been possible to compute the gradient with respect to predictions, which eliminated the possibility of using Spearman as a loss function for GBM or neural nets.

A recent paper, [Fast Differentiable Sorting and Ranking](<https://github.com/google-research/fast-soft-sort/>), introduced a novel method for differentiable sorting and ranking, with the added bonus of O(n \log n) complexity (I would encourage reading the paper to learn more). We can leverage their open sourced code [google-research/fast-soft-sort](<https://github.com/google-research/fast-soft-sort/>) in order to implement a differentiable version of the Spearman metric used by Numerai:
    
    
    from fast_soft_sort.pytorch_ops import soft_rank
    
    def corrcoef(target, pred):
        # np.corrcoef in torch from @mdo
        # http://forum.numer.ai/t/custom-loss-functions-for-xgboost-using-pytorch/960
        pred_n = pred - pred.mean()
        target_n = target - target.mean()
        pred_n = pred_n / pred_n.norm()
        target_n = target_n / target_n.norm()
        return (pred_n * target_n).sum()
    
    
    def spearman(
        target,
        pred,
        regularization="l2",
        regularization_strength=1.0,
    ):
        # fast_soft_sort uses 1-based indexing, divide by len to compute percentage of rank
        pred = soft_rank(
            pred,
            regularization=regularization,
            regularization_strength=regularization_strength,
        )
        return corrcoef(target, pred / pred.shape[-1])
    

We can then use this function to find the gradients of a set of predictions with respect to the correlation and compare to the scoring metric introduced in the [scoring](<https://docs.numer.ai/tournament/learn#scoring>) section of the docs:
    
    
    def numerai_spearman(target, pred):
        # spearman used for numerai CORR
        return np.corrcoef(target, pred.rank(pct=True, method="first"))[0, 1]
    
    # my spearman requires having batch dimension as first.
    pred = torch.rand(1, 10, requires_grad=True)
    target = torch.rand(1, 10)
    
    print("Numerai CORR", numerai_spearman(
        pd.Series(target[0].detach().numpy()),
        pd.Series(pred[0].detach().numpy()),
    ))
    
    s = spearman(target, pred, regularization_strength=1e-3)
    gradient = torch.autograd.grad(s, pred)[0]
    print("Differentiable CORR", s.item())
    
    
    
    Numerai CORR 0.7355864488990377
    Differentiable CORR 0.735586404800415
    Gradient tensor([[0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]])
    

With a very small `regularization_strength`, you will obtain a very accurate correlation, but likely no gradients. To obtain proper gradients you will need to increase `regularization_strength`, which will also lead to slightly inaccurate correlation measures:
    
    
    s = spearman(target, pred, regularization_strength=1e-2)
    
    
    
    Numerai CORR 0.7355864488990377
    Differentiable CORR 0.7345704436302185
    Gradient tensor([[-2.9164,  0.0000,  0.0000,  0.0000,  0.0000,  1.7082,  2.9164,  0.0000,
              0.0000, -1.7082]])
    

Ultimately it seems something like this could be useful for neural network or gradient boosting models; I will update this model examples, but I am curious if anyone else has had success using something like this.

---

### Post #2 — **greenprophet** | 2021-03-11 06:24 UTC

I used just pearson in pytorch with success. By success I mean in optuna it chose to use it. Still waiting on live before I continue with overfitting NN and p hacking. Want to use spearman but thought the sort might be slower. Also want to try FNC loss directly when I go back to this.

But as [@robbo_the_fossil](</u/robbo_the_fossil>) pointed out in chat you can just neutralize your targets as pre processing. This is also what I did on NN models.

Also using [@mdo](</u/mdo>) feature reversal and dropout functions since they improved validation for me.

---

### Post #3 — **javiermoral** | 2021-03-11 10:23 UTC

I wrote a [post](<http://forum.numer.ai/t/objetive-function/2235>) discussing the same topic.  
I also tried differentiable Spearman’s on my PyTorch MLP and it worked horrible. I was also thinking of trying an approach like the one you have proposed using fast-soft-sort, but I am stuck writing the customized loss function for boosted models.I don’t know how I can define the gradient and the hessian from fast-soft-sort code.

---

### Post #4 — **teddykoker** | 2021-03-11 18:19 UTC _(reply to #3)_

This function should work (at least in theory) similar to [@mdo](</u/mdo>)’s method, using 1’s for the hessian:
    
    
    train_df = ...
    era_idx = [np.where(eras == e)[0] for e in np.unique(train_df.eras)]
    
    def loss_fn(target, pred):
        pred = torch.tensor(pred, requires_grad=True)
        target = torch.tensor(target)
        corrs = torch.stack([spearman(target[e], pred[e]) for e in era_idx])
        sharpe = adj_sharpe(corrs)
        gradient = torch.autograd.grad(sharpe, pred)[0].detach().numpy()
        hessian = np.ones_like(gradient)  # ones for hessian should be ~okay~
        return gradient, hessian
    
    model = XGBRegressor(objective=loss_fn)
    

I believe the `fast_soft_sort` code is currently incompatible with higher order derivatives (since it uses a conversion to numpy internally, I believe their JAX implementation might work however).

I think in order to get good results with something like this it will be necessary to pretrain a model to optimize MSE and then use it as a base margin/weight initialization for xgboost/neural nets.

---

### Post #5 — **robbo_the_fossil** | 2021-03-12 02:42 UTC _(reply to #2)_

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/g/da6949/48.png) greenprophet:

> But as [@robbo_the_fossil](</u/robbo_the_fossil>) pointed out in chat you can just neutralize your targets as pre processing. This is also what I did on NN models.

This did really amazing things to my sharpe - perhaps expected. However todays CORR, MMC and FNC are some of the worst I have ever gotten. Today was the first day I had a model deployed with this type of neutralization with live testing. Glad I didn’t stake. Is this working for you at all on live data, [@greenprophet](</u/greenprophet>) ?

---

### Post #6 — **greenprophet** | 2021-03-12 05:20 UTC _(reply to #5)_

I am new and have very little concrete to go on. Only have stable submissions for 253 and 254. My Feature neutralized training models have the best validation by a bit so they are weighted a bit more but it is not all of the models. And I also still had FE so I have post process neutralized some of them as well. Of 3 models and 2 rounds all are positive overall and on the day if that answers your question.

they are basically all the same though so I can see nuances of live. 1 is optimized blend with .5 post process neutralization, 1 is optimized blend with no post process neutralization, 1 is even blend with .5 post process neutralization,

Today was a different day for sure though. 254 is very positive for me but still completely crushed by integration_test and linear models. Also my non post processed model is out performing the other 2 which it is not on 253.

Really I have very little to go on so far. And today is the first day of 254 so going to be volatile.

---

### Post #7 — **robbo_the_fossil** | 2021-03-12 12:11 UTC _(reply to #6)_

Thanks for the reply. Sure, beginning of round is very volatile, but I dont think any of my models ever started so far away from 0 CORR and my FN did not help in that regard (opposite actually i=on the first day) - well there is just random things happening all the time I guess. We will see how much things move towards a happier mean (or not!) ![:wink:](http://forum.numer.ai/images/emoji/twitter/wink.png?v=9)

---

### Post #8 — **k1111** | 2021-03-14 14:50 UTC

Can I use this loss function on GPU??
    
    
    D:\DL\numerai\fast_soft_sort\pytorch_ops.py in forward(ctx, values)
     36       #values = values.to(device2)
     37       #
    ---> 38       obj = cls(values.detach().numpy(), **kwargs)
     39       ctx.numpy_obj = obj
     40       return torch.from_numpy(obj.compute())
    
    TypeError: can't convert cuda:0 device type tensor to numpy. Use Tensor.cpu() to copy the tensor to host memory first.

---

### Post #9 — **krm** | 2021-03-14 16:09 UTC _(reply to #8)_

I have run it on my CUDA 11 GPU without issue.

---

### Post #10 — **k1111** | 2021-03-16 08:47 UTC _(reply to #9)_

Thank you for your reply.  
I also ran my code on CUDA 11 GPU on google colaboratory, but I had a problem about GPU.
    
    
    !nvcc --version
    !git clone https://github.com/google-research/fast-soft-sort/
    
    import os
    path = './fast-soft-sort'
    os.chdir(path)
    
    import torch
    from fast_soft_sort.pytorch_ops import soft_rank, soft_sort
    
    device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
    print(device)
    values = torch.tensor([[5., 1., 2.], [2., 1., 5.]], dtype=torch.float64).to(device)
    soft_sort(values, regularization_strength=1.0)
    
    nvcc: NVIDIA (R) Cuda compiler driver
    Copyright (c) 2005-2020 NVIDIA Corporation
    Built on Wed_Jul_22_19:09:09_PDT_2020
    Cuda compilation tools, release 11.0, V11.0.221
    Build cuda_11.0_bu.TC445_37.28845127_0
    Cloning into 'fast-soft-sort'...
    remote: Enumerating objects: 76, done.
    remote: Counting objects: 100% (76/76), done.
    remote: Compressing objects: 100% (42/42), done.
    remote: Total 76 (delta 44), reused 64 (delta 33), pack-reused 0
    Unpacking objects: 100% (76/76), done.
    cuda:0
    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)
    <ipython-input-9-d7a59b351a2b> in <module>()
         12 print(device)
         13 values = torch.tensor([[5., 1., 2.], [2., 1., 5.]], dtype=torch.float64).to(device)
    ---> 14 soft_sort(values, regularization_strength=1.0)
    
    3 frames
    /content/fast-soft-sort/fast_soft_sort/pytorch_ops.py in forward(ctx, values)
         32     @staticmethod
         33     def forward(ctx, values):
    ---> 34       obj = cls(values.detach().numpy(), **kwargs)
         35       ctx.numpy_obj = obj
         36       return torch.from_numpy(obj.compute())
    
    TypeError: can't convert cuda:0 device type tensor to numpy. Use Tensor.cpu() to copy the tensor to host memory first.

---

### Post #11 — **krm** | 2021-03-16 14:22 UTC

I had that issue locally as well. I’m running inside of a docker container, so I just rebooted it and it worked. I’m not 100% sure what caused that issue.

How did you include fast_soft_sort? If you copied the files into your directory you could always modify that line of code to explicitly convert off the GPU as the error message mentions.

---

### Post #12 — **teddykoker** | 2021-03-16 15:18 UTC

According to a [github issue](<https://github.com/google-research/fast-soft-sort/issues/8#issuecomment-716544059>):

> At the moment we do not have a GPU implementation of the projection operators, which is the cause for the error. We decided not to do this conversion implicitly as we want the user to be aware that a device copy is necessary. If you want that behavior, can you write a small util function like
    
    
    def soft_sort(array):
       return pytorch_ops.soft_sort(array.cpu()).cuda()
    

This solution worked fine for me. Having to perform the operation on CPU is not ideal, but it didn’t seem to penalize training times too poorly.

---

### Post #13 — **teddykoker** | 2021-03-20 20:34 UTC

Update: I am currently working on a pure PyTorch implementation, [GitHub - teddykoker/torchsort: Fast, differentiable sorting and ranking in PyTorch](<https://github.com/teddykoker/torchsort>), of the differentiable sorting and ranking algorithm, which will allow for faster computation on GPU directly. It currently works, ~~but is slower than the original (I believe my C++ isotonic regression solver needs some optimization as it is slower than the Numba JIT’d python)~~ Edit: got an optimized version working, should be out soon. (GPU kernels are a pain ![:roll_eyes:](http://forum.numer.ai/images/emoji/twitter/roll_eyes.png?v=9))

---

### Post #14 — **evanhennis** | 2021-03-21 08:00 UTC

Has anyone pulled this off for TensorFlow? I would assume it shouldn’t be much work converting the existing PyTorch example.

I am just starting (submitted my first today) so I have a lot of work to do with my model.

---

### Post #15 — **teddykoker** | 2021-03-22 16:57 UTC

[![benchmark](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/b65f391e5307857e239e65ed1ef825fc533a200d_2_690x276.png)benchmark1000×400 50.6 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/b65f391e5307857e239e65ed1ef825fc533a200d.png> "benchmark")

Torchsort now has a speed on par with PyTorch’s built in sort (but is differentiable). Numerai spearman loss can be implemented like:
    
    
    import torchsort
    
    def corrcoef(target, pred):
        pred_n = pred - pred.mean()
        target_n = target - target.mean()
        pred_n = pred_n / pred_n.norm()
        target_n = target_n / target_n.norm()
        return (pred_n * target_n).sum()
    
    
    def spearman(
        target,
        pred,
        regularization="l2",
        regularization_strength=1.0,
    ):
        pred = torchsort.soft_rank(
            pred,
            regularization=regularization,
            regularization_strength=regularization_strength,
        )
        return corrcoef(target, pred / pred.shape[-1])
    

I implemented the CUDA kernel as well, it scales pretty well with batch size and sequence length:  


[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/8c7ac952eb1f950bf7667aae5e89ed94b74e0283_2_690x276.png)1000×400 41.5 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/8c7ac952eb1f950bf7667aae5e89ed94b74e0283.png>)

---

### Post #16 — **jeremy_berros** | 2021-03-25 18:51 UTC _(reply to #15)_

Thanks for sharing [@teddykoker](</u/teddykoker>). I have been willing to implement [Fast-Soft_Sort](<https://github.com/google-research/fast-soft-sort/>) for a few months now so that should help. I will play around with it and try to optimize on Corr/Sharpe/Custom functions over the weekend see what comes out of it. Did you experience any memory limitation implementing it?

---

### Post #17 — **k1111** | 2021-03-28 12:08 UTC _(reply to #12)_

Thank you for your reply. I could run soft_sort on my Colab.

---

### Post #18 — **paulito** | 2021-05-05 10:05 UTC _(reply to #14)_

Look at the source code. It already has a tensorflow implementation of fast_sort_soft. [GitHub - google-research/fast-soft-sort: Fast Differentiable Sorting and Ranking](<https://github.com/google-research/fast-soft-sort/>)

---

### Post #19 — **paulito** | 2021-05-05 10:12 UTC

I put this into a function that can be passed to xgboost as objective function (See [Custom Objective and Evaluation Metric — xgboost 1.5.0-SNAPSHOT documentation](<https://xgboost.readthedocs.io/en/latest/tutorials/custom_metric_obj.html>)). This is Proof of Concept and has not provided any meaningful result for me yet. But in case anyone is interested here is the (messy) code:
    
    
    from fast_soft_sort.pytorch_ops import soft_rank
    
    def corrcoef(target, pred):
        # np.corrcoef in torch from @mdo
        # http://forum.numer.ai/t/custom-loss-functions-for-xgboost-using-pytorch/960
        pred_n = pred - pred.mean()
        target_n = target - target.mean()
        pred_n = pred_n / pred_n.norm()
        target_n = target_n / target_n.norm()
        return (pred_n * target_n).sum()
    
    
    def spearman(
        target,
        pred,
        regularization="l2",
        regularization_strength=1.0,
    ):
        
        pred = soft_rank(
            pred,
            regularization=regularization,
            regularization_strength=regularization_strength,
        )
        return corrcoef(target, pred / pred.shape[-1])
    
    
    def custom_loss(ytrue, ypred):
        lenypred = ypred.shape[0]
        lenytrue = ytrue.shape[0]
    
        ypred_th = torch.tensor(ypred.reshape(1, lenypred), requires_grad=True)
        ytrue_th = torch.tensor(ytrue.reshape(1, lenytrue))
    
        loss = spearman(ytrue_th, ypred_th, regularization_strength=3)
        print(f'Current loss:{loss}')
    
        # calculate gradient and convert to numpy
        loss_grads = torch.autograd.grad(loss, ypred_th)[0]
        loss_grads = loss_grads.detach().numpy()
    
        # return gradient and ones instead of Hessian diagonal
        return loss_grads[0], np.ones(loss_grads.shape)[0]
    
    
    params["objective"] = custom_loss
    model = xgboost.XGBRegressor(**params).fit(X, y)
    

as [@teddykoker](</u/teddykoker>) mentioned, tuning the regularization might be one of the most important aspects. After all, I am still not convinced that it is actully useful to use spearman as objective function, but definitely worth a try.

---

### Post #20 — **hiromuhana** | 2021-06-18 16:29 UTC _(reply to #19)_

Has anyone reached good correlation with using the differentiable spearman custom objective?  
I tried with lightgbm, it made disaster…

It’s my optuna study trials. The vertical is differentiable spearman score.

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/0/0e6283bf02838f797df33ecae1185fa0407aebbd.png)image390×247 28.6 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/0/0e6283bf02838f797df33ecae1185fa0407aebbd.png> "image")

---

### Post #21 — **javiermoral** | 2021-06-21 07:40 UTC _(reply to #20)_

which code did yo try?

---

### Post #22 — **hiromuhana** | 2021-06-21 12:46 UTC _(reply to #21)_

I mixed [@paulito](</u/paulito>) & [@teddykoker](</u/teddykoker>) 's code for the objective in lightgbm as below.
    
    
    def spearman_loss_lgb(ytrue, ypred):
        
        def corrcoef(target, pred):
            pred_n = pred - pred.mean()
            target_n = target - target.mean()
            pred_n = pred_n / pred_n.norm()
            target_n = target_n / target_n.norm()
            return (pred_n * target_n).sum()
    
        def differentiable_spearman(target, pred, regularization="l2", regularization_strength=1.0,):
            pred = torchsort.soft_rank(
                pred,
                regularization=regularization,
                regularization_strength=regularization_strength,
            )
            return corrcoef(target, pred / pred.shape[-1])
        
        lenypred = ypred.shape[0]
        lenytrue = ytrue.shape[0]
    
        ypred_th = torch.tensor(ypred.reshape(1, lenypred), requires_grad=True)
        ytrue_th = torch.tensor(ytrue.reshape(1, lenytrue))
    
        loss = differentiable_spearman(ytrue_th, ypred_th, regularization_strength=1e-2)
        # print(f'Current loss:{loss}')
    
        # calculate gradient and convert to numpy
        loss_grads = torch.autograd.grad(loss, ypred_th)[0]
        loss_grads = loss_grads.to('cpu').detach().numpy()
    
        # return gradient and ones instead of Hessian diagonal
        return loss_grads[0], np.ones(loss_grads.shape)[0]

---

### Post #23 — **gbrecht** | 2022-01-03 19:55 UTC _(reply to #20)_

And by disaster you mean the huge swings in the score?  
Maybe it is just me but it looks like it is converging … have you tried simply running 300 more trials?

---

### Post #24 — **gbrecht** | 2022-01-03 19:58 UTC _(reply to #15)_

terribly stupid question: Is this a loss or do we have to return -corrcoef(…) when we want to use this as a loss function?

---

### Post #25 — **pumplerod** | 2022-01-05 20:30 UTC

At the risk of exposing a complete lack of understanding, I hope someone here can clear up a little confusion I have regarding torch_sort.soft_rank().

I have been using this in pytorch, with some success, but I’m wondering if I may still be implementing the loss incorrectly and simply getting lucky.

I notice in the example docs that torch.autograd.grad() is used to compute the gradient. What I do not understand is whether this is needed for a full torch implementation or if this is being done for people to extract the gradient and use in another tool set, such as XGB.

In a fully torch module, if I calculate the correlation Loss and then apply loss.backward(), is there really any need for me to extract the gradient myself?

Here is my code:
    
    
    import torchsort
    def t_corrcoef(target, pred):
        pred_n = pred - pred.mean()
        target_n = target - target.mean()
        pred_n = pred_n / pred_n.norm()
        target_n = target_n / target_n.norm()
        return (pred_n * target_n).sum()
    
    #
    # FUNCTION: t_spearman()
    #   - to calculate differentiable spearman corr for torch training
    #
    def t_spearman( target, pred, regularization="l2", regularization_strength=1.0):
        # fast_soft_sort uses 1-based indexing, divide by len to compute percentage of rank
    
        pred = torchsort.soft_rank( pred.cpu(),
                                    regularization=regularization,
                                    regularization_strength=regularization_strength )
        return t_corrcoef(target, pred.to( target.device) / pred.to( target.device).shape[-1])
    
    

so my understanding is that calculating corr_loss would follow:
    
    
    corr = t_spearman( batch[ 'Y'].unsqueeze(0), preds.unsqueeze(0), regularization="l2", regularization_strength=1.0)
    loss = 1.0 - corr
    loss.backward()
    

Is this correct? If so, might there be a way to apply sample based weights to the loss. Similar to using torch.nn.MSELoss( reduction=‘none’), in order to provide a greater penalty to samples based on the non-uniform distribution?

---

### Post #26 — **adalseno** | 2022-01-20 00:01 UTC

Hi [@teddykoker](</u/teddykoker>) , thank you very much for your code. I was trying to use it for a loss custom function to be used with [TabNet](<https://github.com/dreamquark-ai/tabnet>) but I had an issue that took me sometime to debug. Your function expects a tensor in the form (1,X) while TabNet passes it in the form (X,1) so I had to reshape them. The function uses the default regularization (that is “l2”) and seems to work fine.
    
    
    def spearman(pred, target):
    
        x = 1e-2
        pred = torchsort.soft_rank(pred.reshape(1,-1),regularization_strength=x)
        target = torchsort.soft_rank(target.reshape(1,-1),regularization_strength=x)
        pred = pred - pred.mean()
        pred = pred / pred.norm()
        target = target - target.mean()
        target = target / target.norm()
    
        return (pred * target).sum()
    

In case someone needs also a metric this one should work:
    
    
    class Sprme_Metric(Metric):
        """
        sprme.
        """
    
        def __init__(self):
            self._name = "sprme" # write an understandable name here
            self._maximize = True
    
        def __call__(self, y_true, y_score):
            """
            Compute Spearman Correlation of predictions.
    
            Parameters
            ----------
            y_true: np.ndarray
                Target matrix or vector
            y_score: np.ndarray
                Score matrix or vector
    
            Returns
            -------
                float
                Spearman of predictions vs targets.
            """
            return spearman(torch.from_numpy(y_score), torch.from_numpy(y_true)).item()

---

### Post #27 — **adalseno** | 2022-01-24 20:33 UTC _(reply to #26)_

I have a kind of Hamlet doubt: in regression we should try to minimise the loss. In such a case the loss should return `1 - ret` instead of just `ret`. Since the Spearman index goes from -1 to +1, `1 - ret` will be zero when the index is +1 (what we want, perfect positive correlation) and will be maximum when the index is -1 (that we don’t want, perfect negative correlation). So to minimise the loss we should find an index close to 1.  
Am I wrong? ![:thinking:](http://forum.numer.ai/images/emoji/twitter/thinking.png?v=10)  
In such a case the metric should return `1 - ret`. In fact we want to maximise the metric and the value will be maximum when `ret` is zero (that is when the index is 1, what we want), and will be the minimum when `ret` is equal to two (that is when the index is -1 that we don’t want). Otherwise we can simply return the amended loss (1-ret) and set `_maximize = False`.  
What do you think?

here the revised code:
    
    
    def spearman(pred, target):
    
        x = 1e-3
        pred = torchsort.soft_rank(pred.reshape(1,-1),regularization_strength=x)
        target = torchsort.soft_rank(target.reshape(1,-1),regularization_strength=x)
        pred = pred - pred.mean()
        pred = pred / pred.norm()
        target = target - target.mean()
        target = target / target.norm()
        ret = 1- (pred * target).sum()
        return ret
    

In my case `x = 1e-3` gave better results. And for the metric (the simplest form):
    
    
    class Sprme_Metric(Metric):
        """
        sprme.
        """
    
        def __init__(self):
            self._name = "sprme" # write an understandable name here
            self._maximize = False
    
        def __call__(self, y_true, y_score):
            """
            Compute Spearman Correlation of predictions.
    
            Parameters
            ----------
            y_true: np.ndarray
                Target matrix or vector
            y_score: np.ndarray
                Score matrix or vector
    
            Returns
            -------
                float
                Spearman of predictions vs targets.
            """
            return spearman(torch.from_numpy(y_score), torch.from_numpy(y_true)).item()

---

### Post #29 — **ervinjason** | 2022-05-30 18:57 UTC

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/numerai.discourse.group/pumplerod/48/2891_2.png) pumplerod:

> At the risk of exposing a complete lack of understanding, I hope someone here can clear up a little confusion I have regarding torch_sort.soft_rank().
> 
> I have been using this in pytorch, with some success, but I’m wondering if I may still be implementing the loss incorrectly and simply getting lucky.
> 
> I notice in the example docs that torch.autograd.grad() is used to compute the gradient. What I do not understand is whether this is needed for a full torch implementation or if this is being done for people to extract the gradient and use in another tool set, such as XGB.  
>  [ ![alight motion app](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/5/51721d0475a7ace5373de331fdc97cd36f137777.jpeg)  
>  ](<https://alightmotionapk.co/>)  
>  In a fully torch module, if I calculate the correlation Loss and then apply loss.backward(), is there really any need for me to extract the gradient myself?
> 
> Here is my code:
>     
>     
>     import torchsort
>     def t_corrcoef(target, pred):
>         pred_n = pred - pred.mean()
>         target_n = target - target.mean()
>         pred_n = pred_n / pred_n.norm()
>         target_n = target_n / target_n.norm()
>         return (pred_n * target_n).sum()
>     
>     #
>     # FUNCTION: t_spearman()
>     #   - to calculate differentiable spearman corr for torch training
>     #
>     def t_spearman( target, pred, regularization="l2", regularization_strength=1.0):
>         # fast_soft_sort uses 1-based indexing, divide by len to compute percentage of rank
>     
>         pred = torchsort.soft_rank( pred.cpu(),
>                                     regularization=regularization,
>                                     regularization_strength=regularization_strength )
>         return t_corrcoef(target, pred.to( target.device) / pred.to( target.device).shape[-1])
>     
>     
> 
> so my understanding is that calculating corr_loss would follow:
>     
>     
>     corr = t_spearman( batch[ 'Y'].unsqueeze(0), preds.unsqueeze(0), regularization="l2", regularization_strength=1.0)
>     loss = 1.0 - corr
>     loss.backward()
>     
> 
> Is this correct? If so, might there be a way to apply sample based weights to the loss. Similar to using torch.nn.MSELoss( reduction=‘none’), in order to provide a greater penalty to samples based on the non-uniform distribution?

I am new and have very little concrete to go on. Only have stable submissions for 253 and 254. My Feature neutralized training models have the best validation by a bit so they are weighted a bit more but it is not all of the models. And I also still had FE so I have post process neutralized some of them as well. Of 3 models and 2 rounds all are positive overall and on the day if that answers your question.

they are basically all the same though so I can see nuances of live. 1 is optimized blend with .5 post process neutralization, 1 is optimized blend with no post process neutralization, 1 is even blend with .5 post process neutralization,

Today was a different day for sure though. 254 is very positive for me but still completely crushed by integration_test and linear models. Also my non post processed model is out performing the other 2 which it is not on 253.

Really I have very little to go on so far. And today is the first day of 254 so going to be volatile.

---

### Post #31 — **gbrecht** | 2023-01-30 14:24 UTC _(reply to #4)_

Is there feature neutralization code for pytorch?  
I did some trials but never got it to work. Furthest I got was that there is no GPU implementation for least squares.

---

### Post #32 — **oraculum** | 2023-02-01 21:12 UTC _(reply to #31)_

There is a code for neutralization with pytorch in this thread by [@mdo](</u/mdo>) (in the training loop using pytorch’s pinverse):

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/forum.numer.ai/mdo/48/3398_2.png)

[Optimizing for FNC and TB scores](<http://forum.numer.ai/t/optimizing-for-fnc-and-tb-scores/5132>) [Tournament](</c/tournament/7>)

> With the advent of TC many users may wonder how to optimize for metrics beyond correlation and mean-squared error. Here we will show how to directly optimize for metrics like TB200 and FNC. This is intended to be a proof of concept and source of inspiration, not a set of instructions. A previous [forum post](<http://forum.numer.ai/t/differentiable-spearman-in-pytorch-optimize-for-corr-directly/2287>) demonstrated how to optimize for Spearman correlation directly. This work can be extended fairly simply to allow for the optimization of a top/bottom correlation (e.g. TB200) where only the m…

---

### Post #33 — **f58c** | 2023-11-07 23:21 UTC _(reply to #13)_

Hi Teddy, training models for corr is interesting- but have you compared model performance vs. training for the cyrus_v4_20 target? i’d think that a model that can predict cyrus_v4_20 should also rank well for corr20v2. the hiccup i’ve been running up against is that sometimes high corr20v2 performance results in negative tc. i’d love to hear your thoughts on this.
