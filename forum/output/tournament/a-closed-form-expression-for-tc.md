---
title: "A Closed-Form Expression for TC"
category: Tournament
url: https://forum.numer.ai/t/a-closed-form-expression-for-tc/6280
created_at: 2023-04-06T16:23:38.929000+00:00
last_posted_at: 2023-11-17T16:46:54.573000+00:00
posts_count: 3
views: 1005
tags: []
---

# A Closed-Form Expression for TC

---

### Post #1 — **murkyautomata** | 2023-04-06 16:23 UTC

I recently realized that it’s possible to derive a closed form expression for TC in terms of the meta-model prediction, user prediction, target, and the optimizer cost hessian. In this post I will analyze the closed-form expression for TC, why it doesn’t work as it should, and what makes it vulnerable to an adversarial attack. I will also compare it to two better alternatives. In the next post I will show you how I derived these expressions.

Note I will be ignoring the x^1.5 step in the TC calculation to simplify things. I suggest that this step would be better used applied to user predictions than the meta-model.

**The Current TC**

The current closed-form for user TC is:

`TC(p) = 1/norm(m)*( p – m ).T ( H^-1 y – ( m.T H^-1 y) / ( m.T m ) m )`

with the gradient form TC is defined as:

`TC = SWG[p, fobj(y, m): y.T O( m/norm(m) ) ]`

Where `m` is the un-normalized meta-model prediction, `p` is the user prediction, `y` is the actual return, `H` is the hessian of the optimizer penalty function C(x), SWG() is a stake-weighted gradient operator, and O(x) is the optimizer output for x.

This closed-form is somewhat messy and it may be hard to recognize what is wrong with it. Let’s start by looking at a nicer version of TC with a simple closed-form and then come back to it.

**Optimizer Aligned Un-Normalized MM TC**

The closed-form for our modified TC is:

`TC(p) = ( p - m ).T H^-1 ( y – m )`

with modified gradient form TC:

`TC = SWG[ p, fobj(y,m): y.T O( m ) - C( O(m) )]`

Here we have a beautiful closed-form and frankly it is a tragedy that this is not our current TC. If not for the inverse hessian term in the middle it would simply be the dot product between the difference from user prediction to meta-model and the difference from target to meta-model. The inverse hessian term serves to reduce the importance of linear components of the prediction in in directions punished by the optimizer cost function (we can say the inverse hessian only performs scaling because it is positive semi-definite). For example we can expect predictions sent nearly to zero by an L1 penalty in the optimizer to have very large entries in the diagonal of the hessian and hence very little weight in the inverse hessian.

Two changes were required to achieve this closed-form, first we dropped meta-model normalization, second we subtracted the optimizer penalties from returns to align the optimizer’s incentives with TC (more on that idea here: [The real problem with TC is Optimizer Misalignment](<http://forum.numer.ai/t/the-real-problem-with-tc-is-optimizer-misalignment/6242>)). Numerai insists that dropping normalization is not workable, but I very much doubt that it cannot be made to work. There are many different ways to do a TC without normalization. For example if we absolutely must not rely on users to predict the magnitude of returns we can still do:

gradient: `SWG[ p, fobj(y,m): y.T O( m ) - norm(y) C( O(m) )]`  
closed-form: `( p - m ).T H^-1 ( y – norm(y) m )`

With the above the norm of the meta-model should be between 0 and 1 depending on the confidence in the meta-model predictions.

The effectiveness of the optimizer should also be increased by dropping MM-normalization as the MM norm can then be used as a signal to the optimizer that there is or isn’t enough confidence in a particular prediction to justify a trade.

And if Numerai’s concern is that without normalizing the meta-model prediction is incentivized to grow unbounded, that is already solved by subtracting the optimizer penalties from returns to align the optimizer incentive.

**The Problem with the Current TC**

`TC(p) = 1/norm(m)*( p – m ).T ( H^-1 y – ( m.T H^-1 y) / ( m.T m ) m )`

The current TC has some similarities with the cleaner TC, but instead of applying the inverse hessian to meta-model minus returns, the inverse hessian is applied to the raw returns then the meta-model is deprojected from that. This is a problem because it is not appropriate to subtract a meta-model prediction that is not projected into inverse hessian space from raw returns that are. More importantly, having derived the closed-form expression will allow us to examine how and why our current TC is vulnerable to adversarial attack. That is what I will focus on here. I discuss the other problems with the current TC more in this thread: [The real problem with TC is Optimizer Misalignment](<http://forum.numer.ai/t/the-real-problem-with-tc-is-optimizer-misalignment/6242>)

**Why the Current TC is Vulnerable to Adversarial Attack**

I consider an adversarial attack an approach where we maximize our score without providing new information to the meta-model by exploiting the problems with TC. This is a kind of approach where we could achieve a high TC just by modifying the example predictions. For my proof of the vulnerability, I will assume that we can make a reasonably good estimate of the meta-model and the best prediction of the target we can make is merely our prediction of the target. I’ll call this ym. That is expected_value(y)=expected_value(m)=ym. Now let’s see how we can tune our prediction to maximize out TC:

`argmax_p[ expected_value( TC(p) ) ] ) = `  
`= argmax_p[ expected_value( 1/norm(m) ( p – m ).T ( H^-1 y – ( m.T H^-1 y) / ( m.T m ) m ) ]`  
`= argmax_p[ expected_value( p.T ( H^-1 y – ( m.T H^-1 y) / ( m.T m ) m ) - m.T ( H^-1 y – ( m.T H^-1 y) / ( m.T m ) m ) ) ]`  
`= argmax_p[ expected_value( p.T ( H^-1 y – ( m.T H^-1 y) / ( m.T m ) m ) ) ]`  
` = argmax_p[ p.T expected_value( H^-1 y – ( m.T H^-1 y) / ( m.T m ) m ) ) ]`  
`= argmax_p[ p.T deproject( H^-1 ym, ym ) ]`  
`= deproject( H^-1 ym, ym )`

So if we can estimate the value of the inverse cost hessian matrix, we can perform an adversarial attack on TC by applying the inverse hessian to our prediction and deprojecting our prediction of the meta-model. Such an adversarial attack would trick the optimizer in to taking on more costs than it otherwise would as I discuss in the other thread.

**Optimizer Aligned Normalized MM TC**

This next form of TC is not vulnerable to adversarial attack, but it still faces the problem of subtracting a value that is not in inverse hessian space from one that is.

The closed-form for our modified TC is:

`TC(p) = 1/(norm(m))*( p – m ).T ( H^-1 (y-norm(y)/norm(m)*m) – ( m.T H^-1 (y-norm(y)/norm(m)*m) ) / ( m.T m ) m )`

with modified gradient form TC:

`SWG(p, fobj(y,m): y.T O( m/norm(m) ) - norm(y) C( O(m/norm(m) ) )`

This solves the vulnerability to adversarial attack because we cannot find a non-zero expected value for (y-norm(y)/norm(m) m) without some novel signal in our prediction. It is still a pretty ugly formula however and I expect the deprojection term on the right to make user-TC excessively sensitive to meta-model composition.

---

### Post #2 — **murkyautomata** | 2023-04-06 16:24 UTC

**Proofs**

for the purpose of these proofs, our user prediction is `p`, the realized market returns are `y`, the meta-model prediction is `m`, our optimizer performs O(x) = argmax_x[ y.T x – C(x) ] = r. SWG[p, fobj(y,m)] is the stake-weighted gradient operator, and norm(x) = sum(x**2)**0.5

Lemma 0.1: SWG[p, fobj(y,m)] = ( p – m ).T grad_m[ fobj(y,m) ]

by definition:

SWG[p, fobj(y,m)] = sum(stakes) * grad_stakes[ fobj( y, sum(stakes*preds)/sum(stakes) )] [p].T

= sum(stakes)*grad_m[ fobj(y, m) ]_grad_stakes[ sum(stakes_ preds)/sum(stakes) ][p].T

= sum(stakes)_grad_m[ fobj(y, m) ]_[ preds/sum(stakes) – sum(stakes*preds)/sum(stakes)**2 ][p].T

= grad_m[ fobj(y, m) ]_[ preds – sum(stakes_ preds)/sum(stakes) ][p].T

= grad_m[ fobj(y, m) ].T*( p – m )

_Lemma 0.2:_ `grad_r[ C(r) ] = m`

By definition `r = argmax_x[ m.T x – C(x) ]`

At a maximum the gradient is zero therefore:

`grad_r[ m.T r – C(r) ] = 0`

`grad_r[ m.T r ] = grad_r[ C(r) ]`

`m = grad_r[C(r)]`

_Lemma 0.3:_ `Jacobian_m[ r ] = H^-1`

`m = grad_r[ C(r) ]` (Lemma 0.2)

`Jacobian_r[m] = Jacobian_r[ grad_r[ C(r) ] ]`

`Jacobian_r[m] = Hessian_r[ C(r) ]`

`Jacobian_r[m] = H`

`Jacobian_m[r] = H^-1`

`Lemma 0.4: grad_x[ f( x/norm(x) ) ] `

`= 1/norm(x) ( grad_x[f(x/norm(x))] – ( x.T grad_x[f(x/norm(x))] ) / ( x.T x ) x )`

**Proof 1:`SWG[ p, {fobj(y,m): y.T O( m ) - C( O(m) )}] = ( p - m ).T H^-1 ( y – m )`**

Lemma 1.1 : grad_m[ y.T O( m ) - C( O(m) ) ] = ( p - m ).T H^-1 ( y – m )

`grad_m[y.T O( m ) - C( O(m) ) ] = grad_m[ -y.T r(m) + C(r(m))]`

`=

  * Jacobian_m[r] y + grad_m[ C(r(m)) ]`



`=

  * Jacobian_m[r] y + Jacobian_m[r] grad_r[ C(r(m)) ]`



`=

  * H^-1 y + H^-1 grad_r[ C(r(m)) ]` (Lemma 0.3)



`=

  * H^-1 y + H^-1 m ` (Lemma 0.2)



`= H^-1(m – y)`

Proof:

`SWG[ p, {fobj(y,m): y.T O( m ) - C( O(m) )}] = `( p – m ).T grad_m[ y.T O( m ) - C( O(m) ) ]` (Lemma 0.1)

`( p – m ).T H^-1 (y – m)` (Lemma 1.1)

QED

**Proof 2:`SWG[ p, {fobj(y,m): y.T O( m/norm(m) ) )}] = ( p - m ).T ( H^-1 y – (m.T H^-1 y)/(m.T m) m )`**

`Lemma 2.1: grad_m[ y.T O(m) ] = H^-1 y `

`grad_m[ y.T O(m) ] = grad_m[ -y.T r(m) ]`

`=

  * Jacobian_m[r] y `



`=

  * Jacobian_m[r] y `



`=

  * H^-1 y ` (Lemma 0.3)



`=

  * H^-1 y `



`= H^-1 y`

`Lemma  
2.2: grad_p[ y.T O( m/norm(m) ) ] = ( H^-1 y – (m.T H^-1 y)/(m.T m)  
m )``

`grad_p[ y.T O( m/norm(m) ) ] = ( H^-1 y – (m.T H^-1 y)/(m.T m) m )` (Lemma  
1.1 and Lemma 0.4)`

Proof:

`SWG[ p, {fobj(y,m): y.T O( m/norm(m) ) )}] = `( p – m ).T grad_m[ y.T O( m ) - C( O(m) ) ]`

`SWG[ p, {fobj(y,m): y.T O( m/norm(m) ) )}]

=`( p – m ).T H^-1 `(  
H^-1 y – (m.T H^-1 y)/(m.T m) m )`` (Lemma 0.1 and Lemma 2.2)

---

### Post #3 — **cataclanca** | 2023-11-17 16:46 UTC

[via GIPHY](<https://giphy.com/gifs/editingandlayout-the-office-michael-scott-5wWf7H89PisM6An8UAU>)
