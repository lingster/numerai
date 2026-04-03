---
title: "The real problem with TC is Optimizer Misalignment"
category: Tournament
url: https://forum.numer.ai/t/the-real-problem-with-tc-is-optimizer-misalignment/6242
created_at: 2023-03-28T01:37:03.974000+00:00
last_posted_at: 2023-05-03T02:42:57.614000+00:00
posts_count: 9
views: 2028
tags: []
---

# The real problem with TC is Optimizer Misalignment

---

### Post #1 — **murkyautomata** | 2023-03-28 01:37 UTC

I want to discuss a specific and fixable problem with TC that has not yet been brought up: that of optimizer misalignment.

We actually do know a lot about how TC works. To summarize it briefly, TC is a gradient with respect to user stake size of the following process:

  1. User predictions are gaussianized
  2. A stake-weighted mean prediction is taken, the meta-model prediction
  3. The meta-model prediction is normalized
  4. The meta-model prediction is raised to an exponent of 1.5 (mmp = mmp*abs(mmp)**0.5)
  5. The meta-model prediction is input to a cvxpy layer (“the optimizer”) with costs and constraints related to feature and factor exposure, allocation constraints, long-short neutrality, maximum position sizes, and whatever others.
  6. The output of the cvxpy layer is a theoretical portfolio that would adopted if not for a couple additional costs/constraints used in live trading that are excluded
  7. The return of our theoretical portfolio is calculated ( dot(position_sizes, market_returns) ). This is the value of which TC a gradient



Although the cvxpy layer is a bit of a black box, there is still quite a bit we can infer about it. Here is an example portfolio optimization problem from cvxpy that includes feature exposure and volatility costs as well as constraints related to asset allocation and long short neutrality:
    
    
    # Factor model portfolio optimization.
    w = cp.Variable(n)
    f = cp.Variable(m)
    gamma = cp.Parameter(nonneg=True)
    Lmax = cp.Parameter()
    ret = mu.T @ w
    risk = cp.quad_form(f, Sigma_tilde) + cp.sum_squares(np.sqrt(D) @ w)
    prob_factor = cp.Problem(
        cp.Maximize(ret - gamma * risk),
        [cp.sum(w) == 0, f == F.T @ w, cp.norm(w, 1) <= Lmax],
    )
    
    # Solve the factor model problem.
    Lmax.value = 2
    gamma.value = 0.1
    prob_factor.solve(verbose=True)

We can see that this problem maximizes ( expected return – costs ) subject to some constraints. Expected return being equal to dot(stock_expected_return, stock_position_size). I think Numerai likely does something similar with the meta-model prediction in the place of expected return. The meta-model prediction isn’t necessarily being optimized to be a good estimate of expected return however which poses a problem. I will explain why I think that is and how to fix it next.

The problem is this: because TC optimizes only for return (and not return minus costs,) TC will optimize toward cvxpy layer inputs that maximize the expected return of the cvxpy layer output instead of inputs that best represent expected return. To understand the significance of this consider for example what would happen if user predictions and the meta-model were not normalized, in that case TC would drive the input to the cvxpy layer to have an arbitrarily large scale because a large enough input would render any costs in the optimizer irrelevant, then expected return would increase but at the expense of taking on arbitrarily high feature exposure and ignoring any other costs as well.

Of course the meta-model is normalized, but that does not prevent other adversarial inputs to the optimizer. The optimizer only adopts positions in a couple hundred stocks, so the input values for the majority of the stocks, those that do not get positions, are irrelevant. Therefore, although we cannot change the scale of the meta-model prediction (because it is normalized), we can allocate more of the scale towards those stocks that the optimizer will adopt positions in to the same effect (increased expected returns at the expense of ignoring costs). This suggests that TC will tend to punish users who allocate a lot scale to stocks that the optimizer does not adopt positions in. Thus it may be that TC punishes more novel predictions if they do not assign enough scale to the stocks that others do assign large scales to (as those are the stocks the optimizer is likely to take positions in.)

So far I have speculated about some of the qualities I expect that an adversarial input to the optimizer might have, however it can be very difficult to predict what an adversarial input will look like especially without knowing the exact costs that the optimizer uses. The fact that an adversarial input is possible is more important than the details of what such an input might look like, as whatever adversarial qualities TC rewards, it does so at the expense of failing to properly reward the best predictions.

**How to Fix It**

The source of our problem is that TC and the optimizer optimize for different things, TC maximizing return and the optimizer maximizing “expected return” minus costs. If TC were to maximize return minus costs instead, then the best possible input to the optimizer would be the best possible estimate of expected return and adversarial inputs are no longer possible. However normalizing the meta-model complicates this. Normalizing the prediction risks making the prediction magnitude too large and taking on too much cost, potential creating a situation where TC rewards a worse prediction direction that gets less cost. One solution might be to make TC based on normalized return minus costs, but then our expected return (meta-model prediction) would have to be normalized to a much smaller magnitude than actual returns because the fraction of returns that is actually predictable is very small. Alternatively, we could drop normalization entirely, but this would require a larger reworking of the Numerai system.

---

### Post #2 — **murkyautomata** | 2023-03-28 08:30 UTC

Regarding the question of whether to normalize the meta-model, there is another point I forgot to make: normalization has the unfortunate effect of destroying the gradient vector component in the direction of the meta-model. Thus because the meta-model is normalized, it doesn’t matter if your model agrees with the meta-model when the meta-model is correct and disagrees with it when it is wrong or vice-versa, only the meta-model orthogonal component of your prediction can affect your TC. This likely accounts for some of the noisiness we see in TC as well as some of the cases where models that out-perform the meta-model in corr end up with negative TC. Really it is best that we drop normalization entirely despite what a big change that would entail.

Fixing optimizer misalignment allows us to drop meta-model normalization. Dropping meta-model normalization gives us more consistent TC scores. More consistent TC scores train the meta-model more efficiently.

---

### Post #4 — **mdo** | 2023-03-31 05:48 UTC

We could (and may) put a cost estimate for each portfolio weight to be subtracted from the returns before computing the gradient. We didn’t before, partly because you don’t have access to costs and the optimization does take costs into account, so the portfolio generated is cost aware, but I see your point of how the optimization effected by TC on the stakes could bias it towards more expensive signals. Will definitely consider this for TCv2 which we are about to start work on.  
Regarding normalization, removing it is pretty much a non-starter. In order for the optimizer to properly penalize costs, the metamodel has to be on a consistent scale. Frankly things are much, much too noisy to map from an unnormalized metamodel to expected returns, which determines the scale of the cost penalties. I understand your point about how TC considers only the orthogonal component, and how component co-linear to the metamodel is discarded regardless of direction. Fair enough, though I think the issue is really more theoretically problematic than actually a serious issue. Another way of stating things that I think is equally accurate, but better captures our motivation, is that TC rewards the components of your signal that would beneficially modify (without completely reversing) the ordering of stocks in the metamodel. The component of your signal that would give an identical ordering or exact opposite ordering is discarded. The component that would give the identical ordering is obviously not useful, and the component that would give the exact opposite ordering is highly unlikely to actually come from a good model.  
In any case, I think some of the ideas we are considering for TCv2 would address this concern as well, though in a different way than you are suggesting here.  
Thanks for the thoughtful feedback, it is much appreciated!

---

### Post #5 — **murkyautomata** | 2023-03-31 07:29 UTC _(reply to #4)_

Thanks for your response, mdo. I’d like to start by focusing on one point you made:

> We could (and may) put a cost estimate for each portfolio weight to be subtracted from the returns before computing the gradient. We didn’t before, partly because you don’t have access to costs

I think you’re misunderstanding the effect that aligned costs have. Aligned costs do not require any special consideration from participants, rather participants have more reason to be concerned with the costs in the optimizer when they aren’t also in the gradient. I’ll explain why with an example:

Suppose our only optimizer penalty can be defined as `C(p) = ½ p.T A p` where `A` is some positive definite matrix. For instance if we were only penalizing L2 and feature exposure we could use `A = I + X X.T`. In this case our optimizer would be performing `O(p) = A^-1 p.`

Then our unaligned objective is: `L = y.T O(p) = ½ y.T A^-1 p`  
and our aligned objective is:  
`L = y.T O(p) - C(O(p)) `  
` = y.T A^-1 p - ½ (p.T A^-1) A (A^-1 p)`  
` = y.T A^-1 p - ½ p.T A^-1 p`  
` = ( y.T A^-1 p - ½ p.T A^-1 p – ½ y.T A^-1 y ) + ½ y.T A^-1 y`  
` = -½ (y-p).T A^-1 (y-p) + ½ y.T A^-1 y`

Any terms that depend only on y are of course irrelevant to the gradient so this is equivalent to:  
`L = -½ (y-p).T A^-1 (y – p)`.  
So we have unaligned objective: `L = ½ y.T A^-1 p`  
And aligned objective: `L = -½ (y-p).T A^-1 (y-p)`

So you can see that the unaligned objective not only provides no bounds on `p`, but also if `p` is normalized, the objective isn’t even maximized when `p` points in the directions of `y` but instead `A^-1 y`.

On the other hand the aligned objective is maximized when `p = y` and the cost only serves to reduce the importance of differences in eigenvector directions that have large eigenvalues in `A`.

This is exactly why you should be using an aligned objective, it means that participants do not need to worry about the costs in the optimizer.

I’ll be working on a response to the rest of your post, but I wanted to start with this point because it is so crucial.

---

### Post #6 — **mdo** | 2023-03-31 16:06 UTC _(reply to #5)_

I think we are talking past each other. By costs I mean the costs involved with trading each stock (which could be subtracted from returns). This has nothing to do with feature exposures.

---

### Post #7 — **murkyautomata** | 2023-03-31 19:12 UTC _(reply to #6)_

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/forum.numer.ai/mdo/48/3398_2.png) mdo:

> I think we are talking past each other. By costs I mean the costs involved with trading each stock (which could be subtracted from returns).

I think we are then. When I talked about “costs” in the original post I meant the sum of every penalty that the optimizer uses ie `Optimizer(p) = argmax_q( p.T q - costs(q) )`. It is my contention that all of these costs should be subtracted from return including those for feature exposure, volatility exposure, factor exposure, trading cost, and whatever others the optimizer uses.

The tournament participants need to be more concerned about the penalties the optimizer uses (including the penalty for trading costs) if they are **not** subtracted from returns. Here is a proof of that:

**A proof that an aligned objective is maximized when the input to the optimizer is the expected value of the target:**

Suppose our target `y` is a probabilistic random variable with expected value `ym`. Our optimizer has costs `C(q)` and performs `O(p) = argmax_q( p.T q – C(q) )`. Our aligned objective is `L(q,y) = y.T q – C(q)`

Our expected aligned objective value with respect to the optimizer output is then:

`Lm(q) = mean[ y.T q – C(q)]`  
` = mean[ y.T q ] – C(q)`  
` = mean[ y ].T q – C(q)`  
` = ym.T q – C(q)`

The optimizer output that maximizes the expected value of the objective is then:

`argmax_q[Lm] = argmax_q[ ym.T q – C(q) ] = O(ym)` ( by the definition of our optimizer function O(x) )

Thus I have shown that the expected value of an aligned objective is maximized when the output of the optimizer is that output that is produced when the input is the expected value of the target. My previous post already gave an example that demonstrates that this isn’t necessarily the case with an unaligned objective.

So when the objective is aligned with the optimizer, the incentive is to create a meta-model that is a good estimate of expected returns. When the optimizer is unaligned, the incentive is create a meta-model with properties that are dependent on the penalties in the optimizer.

Users have to worry about the penalties in the optimizer when they are **not** subtracted from returns.

---

### Post #8 — **gbrecht** | 2023-04-03 11:12 UTC

Thank you very much for your work.  
In absence of exact information on optimizer cost: There is a “numerai” sharpe that

a) annualized (not really relvant here I think) and  
b) subtractred a fixed cost of 0.010415154 from the mean to reflect the cost for trading

At the time I failed to see how reducing the mean by 1% is providing a different optimization objective, but maybe this is a first heuristic for optimizer alignment?  
Now, that for sure does not address all the costs (murky conotation) the optimizer imposes on the predictions but maybe it is a start?

---

### Post #9 — **jefferythewind** | 2023-05-02 15:42 UTC

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/m/e79b87/48.png) murkyautomata:

> `risk = cp.quad_form(f, Sigma_tilde) + cp.sum_squares(np.sqrt(D) @ w)`

Hi Murky, Just one thing I’m not quite getting here is the definition of the risk term. I assume `D` is a matrix of stock-specific risk exposures, but what are `f` and `Sigma_tilde` and what is the effect of this quadratic programming problem here?

---

### Post #10 — **murkyautomata** | 2023-05-03 02:42 UTC _(reply to #9)_

Hi Jeffery, that code comes from cvxpy’s portfolio optimization example. [Google Colab](<https://colab.research.google.com/github/cvxgrp/cvx_short_course/blob/master/applications/portfolio_optimization.ipynb>)

f is factor exposure, sigma is factor covariance, and D is stock idiosyncratic risk.
