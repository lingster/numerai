---
title: "Basic CORR vs TC payout question"
category: Tournament
url: https://forum.numer.ai/t/basic-corr-vs-tc-payout-question/6281
created_at: 2023-04-08T11:19:55.804000+00:00
last_posted_at: 2023-04-17T07:42:00.313000+00:00
posts_count: 12
views: 1372
tags: []
---

# Basic CORR vs TC payout question

---

### Post #1 — **silvark** | 2023-04-08 11:19 UTC

So I am new and have been trying to get caught up on the current payout structure.

From what I see, payouts used to be based only on CORR, and then there has been an attempt to transition to TC.

It seems odd that someone could be staking model with a negative TC and still receive a payout by setting the TC multiplier to 0x.

Is there a reason why CORR is still maintained in the current payout structure? Is it to encourage newcomers, or to stabilize the NMR price during the transition to TC?

---

### Post #2 — **krizmanic** | 2023-04-09 12:46 UTC

Corr is basically in aggregate how close you come to solving the problem in its entirety. Corr can be trained for, and is actually a truly objective assessment for rightness of a model. This “rightness” principle was actually first implemented by using logloss. logloss had a strange numeric result, but it was strictly win vs lose at the time and that was fine. Corr came in a little later to represent the same rightness, and due to its range of -1 to +1 it could map easily to an earn or burn percentage. It is quite elegant.

TC represents whatever the hedge fund does to execute on the information. In real life, execution matters more than overall rightness, so TC is more heavily incentivized, to have us find answers that benefit the overall system more. In terms of how to train for TC, that’s an interesting conversation with no shortage of theories.

---

### Post #3 — **silvark** | 2023-04-09 15:35 UTC _(reply to #2)_

I feel like this doesn’t tackle the heart of my question at all.

If 5000 users all submitted identical models with a CORR of .03 using a 1x CORR and 0x TC payout structure, wouldn’t they all receive payouts despite none of them providing useful information?

I think I answered my question a bit. If you add up the TC of the top 1000 staked models, it adds up to around 7. That total of 7 is comprised of a large number of models with a positive TC totaling 8.4, and a small number of models with a negative TC totaling -1.5. From what I understand, this means that there is a minority of users taking advantage of the 1x CORR and 0x TC in order to receive payouts despite negatively influencing the final model.

---

### Post #4 — **anthill** | 2023-04-13 21:36 UTC

I think it’s probably hard to get good CORR but very bad TC — if you were in that situation you could just flip your predictions to get good TC. So users who optimize for CORR are probably on average getting pretty close to 0 on TC; they’re neither helping nor hurting the metamodel.

---

### Post #5 — **sneaky** | 2023-04-14 08:17 UTC _(reply to #4)_

I don’t think that flipping your predictions will give you opposite TC. Also, I do optimize for corr, and my TC is not close to 0 [Numerai](<https://numer.ai/minmax2/>)

---

### Post #6 — **wigglemuse** | 2023-04-14 15:38 UTC _(reply to #5)_

Flipping your predictions (i.e. 1-p) will absolutely give you the opposite TC. And Corr.

---

### Post #7 — **anthill** | 2023-04-14 16:43 UTC

Yes, and you don’t have to take our word for it. You can make two dummy models that have opposite predictions and wait a few weeks. (I’ve been doing this for a little while now.) You’ll find that they have opposite CORR & TC.

---

### Post #8 — **taori** | 2023-04-14 17:05 UTC

CORR is the only fair metric on which you can base the payout at the moment. I say fair because you can train a model on it and get paid accordingly.

TC is useful for the fund, but it is unfair for the users because you cannot train a model on that metrics and, more importantly, TC doesn’t express how much a model is useful to the fund, instead it indicates the CHANGE of a model usefulness. The payout should be a function of a model usefulness, not the first derivative of it. I have already said it in [here](<http://forum.numer.ai/t/true-contribution-for-dummies>)…

That’s why I hope they never get rid of CORR payout, unless they fund another fair payout scheme.

---

### Post #9 — **taori** | 2023-04-14 17:22 UTC _(reply to #8)_

One thing that I really don’t like is that people really think that CORR is bad, useless, detrimental for the fund. Hey, wake up! it’s our models that generate the metamodel. We are providing Numerai with precious data, trained at our expenses. So unless Numerai computes the metamodel itself, we need to be paid for the CORR, because payout based on TC do not take into account the cost of generating the metamodel. TC rewards useful changes w.r.t. to the metamodel, it doesn’t reward the metamodel creation. That’s way payout on CORR is required.

---

### Post #10 — **silvark** | 2023-04-14 22:12 UTC _(reply to #9)_

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/t/ebca7d/48.png) taori:

> it’s our models that generate the metamodel on which CORR is computed.

The CORR of a model is it’s correlation with the targets, which is distinct from the metamodel, right?

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/t/ebca7d/48.png) taori:

> CORR is the only fair metric on which you can base the payout at the moment. I say fair because you can train a model on it and get paid accordingly.

The point I was trying to get at earlier was this:

Let’s imagine that there is only one model being staked. It’s a basic XGB model like the one given in the example docs and has a CORR of .03.

Then, let’s then say that a second model comes along. This second model has a CORR of .02 and a negative TC (Its TC is negative because it is a very similar model to the one with CORR of .03, but slightly worse in all regards.).

In this scenario, the model with a CORR .02 will receive a payout. Also, if it is being staked, it will actually be hurting the metamodel because it will be skewing the metamodel towards itself and it has a lower CORR than the other model.

Someone please let me know if this is incorrect.

Now, as far as TC goes, is it based on the gradient around a given stake? ( i.e. a model can be extremely strong and beneficial to the portfolio, but be slightly over staked, such that it receives a negative TC because staking it for slightly less would actually benefit the portfolio.)

If that is the case, it seems like allowing for 0x TC is detrimental to the portfolio in the case of such a model, as you would want the negative TC to incentivize the owner of the model to lower to the optimal stake.

---

### Post #11 — **taori** | 2023-04-15 08:48 UTC

> The CORR of a model is it’s correlation with the targets, which is distinct from the metamodel, right?

You are right and I edited my post.

Your example is interesting and I basically agree with almost everything you say. It explains why TC is important for Numerai’s fund. Then why do I insist that CORR should be kept? Because being good for the fund doesn’t necessarily mean being fair for the users.

Consider your example, and let’s imagine staking on CORR was not possible and only TC staking was available. The model with CORR 0.02 would receive negative TC until its stake became 0. At that point the model with CORR 0.03 would receive TC=0 (this is the important stuff). Do you think is fair to not being paid even though the model predictions are usuful? I don’t like that and that’s why I want staking on CORR too. Maybe I could accept a mandatory stake on TC while keeping the stake on CORR.

This issue was firstly explained [here](<http://forum.numer.ai/t/question-on-tc-is-it-true-contribution-or-something-else>).

One last minor detail. The model with CORR 0.02 in reality might get a higher TC because its predictions (or its predictions combined with other models’ predictions) could fit better the portfolio optimizer. You can indeed see models with negative CORR receive positive TC.

---

### Post #12 — **sneaky** | 2023-04-17 07:42 UTC _(reply to #6)_

My bad you are right.
