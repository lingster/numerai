---
title: "[Discussion] NumerBay Direct Staking w/ Profit Sharing"
category: Council of Elders
url: https://forum.numer.ai/t/discussion-numerbay-direct-staking-w-profit-sharing/4984
created_at: 2022-02-22T11:22:21.406000+00:00
last_posted_at: 2022-03-25T06:32:10.504000+00:00
posts_count: 16
views: 1505
tags: []
---

# [Discussion] NumerBay Direct Staking w/ Profit Sharing

---

### Post #1 — **restrading** | 2022-02-22 11:22 UTC

This is by far the most requested feature for [NumerBay](<https://numerbay.ai/>) and probably the most difficult to implement: **the ability to stake on others’ models directly with profit sharing**.

I’m starting this thread to brainstorm user requirements and ideas for implementation. Feel free to comment below.

* * *

## Some things to think about

  * **Features** : What functionalities should it support?
  * **Design** : 
    * What would be the ideal user experience and UI?
    * Is there a similar DeFi project that can be used as reference for design?
  * **Implementation** : 
    * How can the smart contract be implemented?
    * What are some of the libraries and frameworks that we can leverage to make things easier?
    * How to minimize gas?
  * **Numerai** : What feature requests are there for Numerai? What should Numerai implement to make this work?
  * **Impact** : How to make it such that it benefits the meta-model?
  * **Regulation** : Given the nature of this feature, what would be some regulatory concerns? How to minimize the regulatory risk?
  * **Security** : What security practices should be followed to avoid hacking and attacks?



* * *

## What about the “stake mode” that’s already available on NumerBay?

If you’ve been following the NumerBay project, you may notice there’s already a “stake mode” for listings. The way it’s built allows sellers to submit for buyers without distributing the submissions files, and optionally a stake limit can be set.

The existing stake mode allows for laddered fixed pricing, which can be used for approximating profit sharing in a prepaid manner (e.g. sell for 1 NMR with 200 NMR stake limit, 2 NMR with 500 NMR stake limit, etc.). The lack of direct post-profit attribution is not ideal but it alleviates some regulatory problems (since it’s technically a product sale, instead of an investment).

* * *

## Call for contribution

I don’t have experience with Solidity. If you happen to have the skill and would like to step up, it would be awesome and I would be happy to collaborate with you. In the mean time, I will also refresh my skills so hopefully we can get the implementation started.

* * *

# Scratch pad

_This section will be updated regularly to summarize community inputs._

To kick off the discussion, here’s my two cents on some of the topics above:

  * Features: 
    * Model owners should be able to set laddered fees (both fixed fees and profit-based fees) based on staker amount.
    * Model owners should be able to set minimum commitment period and also adjust fees based on that.
    * Stakers should be able to manage a portfolio of models they stake on, and preferably with some automation toolings.
    * Stakers should be able to track and verify consistency of the models they stake on. (And probably insurance for consistency using Erasure?)
  * Implementation: 
    * The main difficulty is the Solidity smart contract. I don’t have the skill to make this happen yet and would like to call for contribution.
  * Numerai: 
    * It could be helpful it Numerai allows for BYOW (bring your own wallet). This would allow for message signing, etc.
    * It could be helpful if Numerai allows for a way of tracking model consistency for non-owners. E.g. a staker may want to know the model they stake on actually submits the same model across rounds.
  * Impact: 
    * To benefit the meta-model we should probably avoid having too much stake concentrated on too few correlated models. One way to help would be to allow for some sort of ensemble building mechanism. E.g. a recommendation engine that tells a buyer/staker which models would ensemble well with their model or existing portfolio.
  * Regulation: 
    * It can be problematic (for me) if this feature makes NumerBay an investment platform or if it makes Numerai or CoE legally liable for stuff. (I’m not a legal professional).
    * The feature likely needs to be designed such that the responsibility for compliance is up to the users. Similar to how some ecommerce platforms offload VAT/GST burdens to their sellers.

---

### Post #2 — **aventurine** | 2022-03-01 09:16 UTC

Maybe we can have a long discussion on this with a possible special Twitter space soon? I can get with the other CoE members about it

---

### Post #3 — **restrading** | 2022-03-01 09:43 UTC _(reply to #2)_

Sounds good, do you need me to join the space?

---

### Post #4 — **aventurine** | 2022-03-01 09:46 UTC _(reply to #3)_

Yah maybe either this week or next week we can do a 4pm PST/12am UTC space again you can join up on. I will get with the others to see which is better. Would that work for you?

---

### Post #5 — **newmarkrisk** | 2022-03-02 16:47 UTC _(reply to #4)_

Do you have a link to your twitter or the spaces? Would love to get more involved

---

### Post #6 — **aventurine** | 2022-03-02 17:23 UTC _(reply to #5)_

You can follow the COE twitter at: @NumeraiCoE. We will post the Spaces on there and in the rocketchat channels as well

---

### Post #7 — **gbrecht** | 2022-03-12 16:56 UTC

My number 1 reason for wanting this (if I grasp the concept correctly) is to decouple the buyers risk from the seller uploading dedicated artifacts each round.  
Right now the buyer has to

  * pay upfront
  * handle the submission of the artifact
  * live with the fact that the seller is a nameless stranger on the internet

---

### Post #8 — **autratec** | 2022-03-13 12:28 UTC _(reply to #7)_

I dont think new feature will address your concern. The main benefit to seller is now they can share the profit of using their prediction, with an agreed precent, say 20%. Rather charge a fixed fee to provide signal.

---

### Post #9 — **gbrecht** | 2022-03-13 17:47 UTC _(reply to #8)_

I agree that solving my concern would be a secondary implementation detail. If at all, I could imagine that direct staking works e.g. with a dedicated model slot or any other automation measure, where the trigger is with the seller, so that I do not run into the situation that

  1. Round opens, compute node runs, compute node submits artifacts
  2. Sales happen
  3. I have to manually run the compute node again otherwise the buyer does not get the artifact.

---

### Post #10 — **restrading** | 2022-03-15 13:11 UTC _(reply to #9)_

There will be no concept of sale and file delivery for direct staking. The vault contract holding the stake will act as any normal Numerai user, the data scientist has control for submission to Numerai, others can stake, and the contract should handle profit attribution.

---

### Post #11 — **gbrecht** | 2022-03-15 19:39 UTC _(reply to #10)_

That sounds like it will help me a lot. Detail question: Round opens ==> webhook of the vault contract triggers ==> submission is done.

Now there is still time till between stake closure. Will it require an action by the seller if another sale happens in that period?

---

### Post #12 — **restrading** | 2022-03-16 00:56 UTC _(reply to #11)_

I don’t think so, it would just be like any other model slots you have. Staking is a separate thing and doesn’t impact submissions

---

### Post #13 — **mic** | 2022-03-24 23:25 UTC

A lot of good ideas. I hope Numerbay can keep focus on its core service, doing it well and keeping it simple. Are you looking to service power users already highly expert on Numerai and know what they are doing or new users who are not so into the details but want to be part of the game? I’m not sure complex power user features are going to drive usage and demand, at least not at this stage.

A missing feature is the charging as a performance fee. I know that can’t be done without significant new work and changes, but perhaps a similar alternative is “fee based on stake”.

For example, if a seller sets a 1% fee, and buyer decides to pay 1 NMR, then the buyer can stake up to 100 NMR. This is like an upgrade to the “stake limit” option you already have and maybe could replace it.

---

### Post #14 — **restrading** | 2022-03-25 06:12 UTC _(reply to #13)_

[@mic](</u/mic>) you can currently achieve stake-tiered pricing using the existing features by setting multiple pricing options with different stake limits.

This topic is directed towards non DS users who just want to stake on others’ models, and achieving performance fee distribution on-chain.

And yes, it’s important to make existing service robust, I’m trying my best.

---

### Post #15 — **mic** | 2022-03-25 06:30 UTC _(reply to #14)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/restrading/48/2928_2.png) restrading:

> You can currently achieve stake-tiered pricing using the existing features by setting multiple pricing options with different stake limits.

That sounds like a good work around

![](http://forum.numer.ai/user_avatar/forum.numer.ai/restrading/48/2928_2.png) restrading:

> And yes, it’s important to make existing service robust, I’m trying my best.

Oh, sorry, I wasn’t meaning to comment on any existing issues, it was just a general comment.

---

### Post #16 — **restrading** | 2022-03-25 06:32 UTC _(reply to #15)_

[@mic](</u/mic>) no worries, I agree with your comments. The stake limit can only be loosely enforced right now, so use at your own risk.
