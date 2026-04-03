---
title: "Demo: How to Train an NN on FNC TB200 Directly"
category: Data Science
url: https://forum.numer.ai/t/demo-how-to-train-an-nn-on-fnc-tb200-directly/6258
created_at: 2023-03-31T03:43:18.216000+00:00
last_posted_at: 2023-04-29T05:58:11.803000+00:00
posts_count: 6
views: 1747
tags: []
---

# Demo: How to Train an NN on FNC TB200 Directly

---

### Post #1 — **murkyautomata** | 2023-03-31 03:43 UTC

I made this colab notebook to show how we can train a neural network on FNC TB200 directly using a convex solver layer and to demonstrate that the way TC trains with a convex solver has a serious problem. I explain the problem with TC in detail in [this thread](<http://forum.numer.ai/t/the-real-problem-with-tc-is-optimizer-misalignment/6242/2>).

<https://drive.google.com/file/d/1KmYyMjbTejKfstrhcRa8Pm-t-rRord7j/view?usp=sharing>

---

### Post #2 — **mdo** | 2023-03-31 05:20 UTC

That’s very cool Murky, nice work. I’ll address some of the TC concerns in the other thread.

---

### Post #3 — **murkyautomata** | 2023-03-31 23:23 UTC

**Why objective alignment makes this work and what this accomplishes:**

I feel I haven’t yet sufficiently explained why it is necessary to add the convex solver costs to the loss function or what exactly training with a convex solver and aligned loss function accomplishes. I will do so now.

I will use `p` to refer to the prediction from the NN that is fed to the convex solver, and `q` to refer to the output of the convex solver that is fed to the loss function.

`q = Solver(p) = argmax_x( p.T x - costs(x) )`

To answer the first point: adding the solver costs to the objective ensure that minimizing `aligned_objective(y,q)` also minimizes `mse(y,p)` and vice versa (proof 2 below).

This is necessary because we designed the convex solver to operate on a prediction of y. If the input to the solver is not a prediction of y, what meaning can we say the output has? None. If our objective is not aligned with our solver, we are training the model to subvert the solver ie. to produce whatever predictions most effectively get through the solver’s cost ie. to perform an adversarial attack on the solver.

Now you might ask: if minimizing `mse(y,p)` also minimizes `aligned_objective(y,q)`, why don’t we just train on `mse(y,p)`? The answer is that by training on `aligned_objective(y,q)` we put more weight on the feature neutral top and bottom of our prediction than we would training on mse.

The gradient of `mse(y,p)` wrt. `p` is `( p – y )` but the gradient of `aligned_objective(y, q(p) )` wrt. `p` is `H^-1 ( p – y )` where `H` is the hessian of our solver’s cost function `C(q)` at `q` (proof 1 below). The inverse hessian term in the gradient puts more weight on those components of our prediction that are not penalized by the solver. For instance those predictions that are sent nearly to zero by our soft L1 cost in the solver will have very big entries in the diagonal of the hessian and thus end up with very little gradient.

_**Proofs**_

**Proof 1:** `grad_p[ aligned_objective(y, q(p) ) ] = H^-1 ( p – y )` where `H = hessian_q[ C(q) ]`

_Lemma 1:_ `grad_q[ C(q) ] = p`

By definition `q = argmax_x[ p.T x – C(x) ] `

At a maximum the gradient is zero therefore:

`grad_q[ p.T q – C(q) ] = 0`

`grad_q[ p.T q ] = grad_q[ C(q) ]`

` p = grad_q[C(q)]`

_Lemma 2:_ `Jacobian_p[ q ] = H^-1`

`p = grad_q[ C(q) ]` (Lemma 1)

`Jacobian_q[p] = Jacobian_q[ grad_q[ C(q) ] ]`

`Jacobian_q[p] = Hessian_q[ C(q) ]`

` Jacobian_q[p] = H`

`Jacobian_p[q] = H^-1`

_Solution:_

`grad_p[ aligned_objective(y, q(p) ) ] = grad_p[ -y.T q(p) + C(q(p))]`

`= - Jacobian_p[q] y + grad_p[ C(q(p)) ] `

`= - Jacobian_p[q] y + Jacobian_p[q] grad_q[ C(q(p)) ] `

`= - H^-1 y + H^-1 grad_q[ C(q(p)) ]` (Lemma 2)

`= - H^-1 y + H^-1 p` (Lemma 1)

`= H^-1(p – y)`

QED

**Proof 2:** minimizing `aligned_objective(y, q)` minimizes `mse(y,p)`

From proof 1 we have `grad_p[aligned_objective(y, q)] = H^-1( p – y )`

The objective is minimized when the gradient = 0 and the gradient = 0 when p=y QED.

You can also find an alternative proof in this post: [The real problem with TC is Optimizer Misalignment - #7 by murkyautomata](<http://forum.numer.ai/t/the-real-problem-with-tc-is-optimizer-misalignment/6242/7>)

---

### Post #4 — **murkyautomata** | 2023-04-08 02:05 UTC

Here is somewhat faster version that uses the closed form I derived in the above post to calculate the gradient without differentiating through the convex solver: [custom_gradient lstsq_tb200nn.ipynb - Google Drive](<https://drive.google.com/file/d/1pUROXh6Ncdbz4B-gIt4W7sQR-tPCCm5c/view?usp=sharing>)

---

### Post #5 — **jefferythewind** | 2023-04-11 20:11 UTC

This is absolute fire.

---

### Post #6 — **richai** | 2023-04-29 05:58 UTC

Super impressive. Let’s talk.
