---
title: "On the existence of NMR"
category: Numeraire
url: https://forum.numer.ai/t/on-the-existence-of-nmr/4658
created_at: 2021-12-21T18:38:25.515000+00:00
last_posted_at: 2021-12-27T22:12:53.139000+00:00
posts_count: 18
views: 1977
tags: []
---

# On the existence of NMR

---

### Post #1 — **mundan** | 2021-12-21 18:38 UTC

Hello everyone,

I find more complicated to solve the **financial problem** than to develop ML models. But it is a stage I have to go through.

My question is, why to use NMR at all?  
Using NMR has disadvantages: volatility in NMR price, correlation between NMR and the cryptocurrency market (not all of us are bullish on this), transaction fees (usually too high for low stakes), and usability (I can’t buy stuff with NMR).

It seems to me that _fintech + crypto + machine learning_ sounded great for a startup. But I can only think about avoiding legal problems as an advantage.

thanks for any explanation!

---

### Post #2 — **rigrog** | 2021-12-21 19:32 UTC

“My question is, why to use NMR at all?”

I believe the decisive factor, is that Numerai could mint NMR out of thin air.

---

### Post #3 — **themicon** | 2021-12-21 21:20 UTC _(reply to #2)_

The ability to burn NMR was also required.

---

### Post #4 — **rigrog** | 2021-12-21 22:06 UTC _(reply to #3)_

Any currency _can_ be burned (by losing a crypto key, or _literally burning_ cash).

I guess what you mean, is that burning of NMR is built in to the ETH smart contract, when they’re staked on a negative performing model. But I have a couple of questions about that.

  1. When a round resolves, how much NMR _actually_ ceases to exist?



I have a vague recollection, of reading that NMR lost by losing stakes, become the NMR won by the winning stakes. So if the total lost is less than the total won, then Numerai pays (total won) - (total lost) from their treasury; otherwise only (total lost) - (total won) is _actually_ burned.

Or, does the entire (total lost) get burned, and the entire (total won) get paid out from the treasury?

  2. _Should_ those losses (wether the gross or the net) be burned away? It seems rather drastic to me, but I’d love hear the pros and cons discussed here in this forum.

---

### Post #5 — **valiunia** | 2021-12-23 11:00 UTC _(reply to #4)_

I agree with your points above, but

  1. burning cash is illegal
  2. I dont trust anyone burning my cash
  3. You cannot prove to me you have burned the cash
  4. If you can cheat me into thinking you have burned cash, then you have incentive to tell me my predictions were bad, so that you can keep the cash instead.
  5. If you use NMR, with all of its problems, all agents in this system whatever their intentions, have aligned goals, the only way for everyone to make money is buy staking on good predictions and those predictions actually being good and generating money for the fund

---

### Post #6 — **mundan** | 2021-12-23 13:21 UTC

Thanks everyone for pointing out the burning. I understand the alignment of interests argument, but at the same time, behind any mechanism there is trust involved.

My question now would be “why is burning necessary?”. And a followup would be “what’s the difference between trusting the fund to keep and honor the current rules and trusting the fund to take USD instead of burning NMR?”.

---

### Post #7 — **rigrog** | 2021-12-23 19:26 UTC _(reply to #5)_

Your point #4 does lend some support, to _contractual_ burning of NMR… instead of _claiming_ to burn, whatever currency or asset.

I’m still skeptical, about the need to do any burning. If Numerai cheats a good modeler out of their earned rewards, that good modeler just gives up, and Numerai loses the value of their model.

---

### Post #8 — **themicon** | 2021-12-24 06:32 UTC _(reply to #7)_

There has to be some way of “punishing” bad models or predictions, hence the NMR burning. Otherwise anyone could submit junk / random predictions many millions of times and not face any consequences for doing so. They could then simply choose the models that performed well and do the same thing over and over again without loosing anything and not helping Numerai in the process.

We’ve seen this kind of “attack” in the past, before staking and burning was a thing. There has to be a mechanism for punishing bad behaviour, otherwise the hedge fund would be over very quickly.

“Skin in the game” is the only way this tournament works for everyone.

---

### Post #9 — **rigrog** | 2021-12-24 06:44 UTC _(reply to #8)_

That’s why the bad modeler should _lose_ those NMR… _not_ why they should be burned. Instead of being burned, they could be transferred to Numerai’s treasury.

---

### Post #10 — **themicon** | 2021-12-24 06:46 UTC _(reply to #9)_

And then people who paid for their NMR will complain that Numerai stole the NMR for their own purposes. You can’t just take someone’s money. The “money” needs to be destroyed in a verifiable way, not transferred and just used for something else.

---

### Post #11 — **rigrog** | 2021-12-24 07:12 UTC _(reply to #10)_

Numerai apparently agrees with you.

I think it could work just as well, for Numerai to reclaim (instead of burn) what a modeler loses. I trust that Numerai _wants_ to reward the good models, so that the modeler will keep submitting it. If they _don’t_ reward those modelers, or even rob them… then those modelers just go away.

Do you know whether _all_ the NMR lost, are burned? I _think_ I recall reading, somewhere, that a round’s “burned” NMR are first transferred to the winning models, and only if burnings > earnings is the excess _actually_ burned. Have you read anything like that?

---

### Post #12 — **restrading** | 2021-12-24 07:34 UTC _(reply to #11)_

Reclaiming instead of burning creates perverse incentive or at least the appearance of it such that participants may wonder if the game is tilted against them

---

### Post #13 — **wigglemuse** | 2021-12-24 17:12 UTC

Numerai just taking the money would turn the whole thing into a casino, which of course would be highly illegal. (We are already in a somewhat legal gray area methinks, but that would put us unambiguously on the wrong side of settled law.) Numerai can’t have an incentive (and reward) for us losing.

But yes, it doesn’t seem like actual NMR burned and forever lost (actually reducing the supply) happens very much as they are keeping it off-chain until you cash out and so are forced to reconcile. I don’t think this is properly thought of as “transferring to the winners” but maybe that argument can be made. Nobody has 100% clarified how this occurs, when real burns happen, etc. (Someone could probably examine the blockchain trail of transactions and figure it out.) It is my assumption that Numerai simply doesn’t do anything on-chain until it is necessary on an individual basis – if you cash out and take your NMR (at a profit), they have to pay out from the treasury, but not until you cash out to your wallet. If you cash out at a loss, then there ought to be a proper burn. (I’ve not seen this verified though.) But most of the time people aren’t 100% cashing out, but withdrawing some partial amount of their stake. So some sort of FIFO or other rule would then have to dictate which gives me a headache. It is not super important to me personally that we be (truly) burning NMR all the time, but maybe it should be as it would in theory put upward pressure on the token price. Feel free to bug the team to get clarification on how this all happens as it really should be known and clear info.

---

### Post #14 — **mic** | 2021-12-24 18:44 UTC _(reply to #13)_

and to add to wigglemuses reply, the reason for keeping the burns off chain and applying them later is to try to save on gas, which has been too high for a long time now.

---

### Post #15 — **wigglemuse** | 2021-12-25 23:12 UTC

One of the team members just posted on RC yesterday indicating that yes, if a burn is needed when you cash out, that amount is sent to a dead/unrecoverable address (that’s how you burn crypto – send it to where nobody can ever get it).

---

### Post #16 — **bor1** | 2021-12-26 15:19 UTC

Here you see transactions where NMR is sent to what is a common “burn” address for ethereum tokens

<https://etherscan.io/token/0x1776e1f26f98b1a5df9cd347953a26dd3cb46671?a=0x000000000000000000000000000000000000dead>

---

### Post #17 — **rigrog** | 2021-12-27 22:08 UTC _(reply to #15)_

So when a user cashes out: do his burns get matched with, and cancelled by, his earns? Or is each negative earning, for each of his models, for each round, added up to a total burn? The implied ethos of burning would seem to require the latter.

---

### Post #18 — **wigglemuse** | 2021-12-27 22:12 UTC _(reply to #17)_

Former, I think. Netted out.
