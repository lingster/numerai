---
title: "Historial Numeraire Data"
category: Numeraire
url: https://forum.numer.ai/t/historial-numeraire-data/4562
created_at: 2021-11-27T15:10:02.350000+00:00
last_posted_at: 2022-01-18T02:00:57.229000+00:00
posts_count: 13
views: 1757
tags: []
---

# Historial Numeraire Data

---

### Post #1 — **ganon** | 2021-11-27 15:10 UTC

I have been doing a little bit of historical research on NMR and trying to figure out basic questions like “How much NMR is still owned by the hedge fund?”, “How much NMR has been burned?”, and “How much NMR is distributed/burned on average per week?”. My hope is that if I can answer these questions, I can answer bigger questions like “How long until the hedge fund (probably) runs out of NMR?” and “How much NMR will (probably) be burned in a year? 2 years? 3 years?”

Now, as part of that research, I have been looking at round performance data for all users in the tournament, however I noticed that from round 201 and before, there is no payout data, despite there having been payouts (I think.) So I wanted to know why this is the case? I could just calculate the payout with the corr/mmc, payout factor, and modifiers, but I know I’d still be wondering about this.

Additionally, why is there no data at all before round 168? From what I have read, it sounds like NMR was originally conceived in Feb 2017 and people started to have it in June 2017, but the round data goes back to August 2017 so what happened in between?

---

### Post #2 — **profricecake** | 2021-11-27 15:27 UTC

Making sure you know about this: <https://numer.ai/nmr>

---

### Post #3 — **ganon** | 2021-11-27 15:34 UTC _(reply to #2)_

Yeah I do, thanks. I don’t think all that information is up-to-date (for example, it shows about 30,000 NMR having been burned when, at least according to my research, at least 100,000 NMR has been burned in the tournament (I have not done signals yet and don’t have all the information, but that’s a good floor for now.).)

---

### Post #4 — **wigglemuse** | 2021-11-27 15:53 UTC

Burns in the tournament don’t translate to on-chain burns of NMR most of the time, i.e. if I have a bad week this week and “burn”, that NMR is not burned on-chain. Only if I cash out at a net loss will it burn really (even then it is somewhat unclear). So genuine burning seems rare.

I believe the stuff at: <https://numer.ai/nmr> is up-to-date (check back often and see if it is changing).

As far as your other questions, the entire tournament format and payout systems have changed a number of times, and so that’s why they are not on the display as they don’t quite fit into the current scheme (round 168 was the start of this general format – 201 was I’m guessing the end of the era when they were paying bonuses or something to do with overlapping changed, not sure)

The key question to be looking at is how much they have in their treasury, and how fast they are depleting it (which is now limited since they have a payout factor that decreases as stakes increase).

---

### Post #5 — **ganon** | 2021-11-27 16:10 UTC _(reply to #4)_

Wait, let me see if I understand what you are saying. Can you corroborate this example?

  1. I join the tournament with 100 NMR, starry-eyed and ready to be a millionaire by next month
  2. I make very bad predictions using my astrological signs and lose 50 NMR
  3. I go to data scientists anonymous, get my models in order, and eventually get my stake up to 150 NMR
  4. I decide to cash out because this ML business is too hot-and-heavy (and bad for my acid reflux)
  5. ??



There are two possibilities for 5:  
The first is the NMR that was originally lost by me is truly burned, and then the hedge fund pays me 100 NMR.  
The second is that the hedge fund pays me 50 NMR and nothing is burned.

My original understanding is that the first happens, but are you saying the second happens?

---

### Post #6 — **wigglemuse** | 2021-11-27 16:20 UTC _(reply to #5)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/ganon/48/2267_2.png) ganon:

> NMR that was originally lost by me is truly burned, and then the hedge fund pays me 100 NMR.  
>  The second is that the hedge fund pays me 50 NMR and nothin

Yes – the second one, as long as you never withdrew all your remaining stakes in the interim. (And again, even if you did I’m not completely sure that NMR would be actually burned in that case either. It should, I think, but I’ve never gotten firm confirmation on that.) But in the first case if you just let it ride down and then back up the Numerai NMR treasury would only be down 50, yes.

There was a time when this wasn’t true (or at least wasn’t the plan), but all those gas fees for all those transactions were just too much so now it is netted out.

---

### Post #7 — **ganon** | 2021-11-27 16:28 UTC _(reply to #6)_

Hm. Doesn’t that benefit the hedge fund unfairly, like a lot?

With the previous example, you can see that in situation 1, the hedge fund would have to pay 100 NMR with its treasury. However, in situation 2, the hedge fund would only have to pay 50 NMR with its treasury, which is objectively less?

In this example, people having burns in their models that are not genuine burns benefits the hedge fund! In that way, it also introduces an incentive for the hedge fund to actually burn more often, to save NMR (I’m not saying that they are or would do that, I’m just commenting on it from a game theory perspective, ignoring other aspects like wanting to reward the people who help them the most.)

I thought that burns were supposed to be a way to disincentive bad behavior/predictions while at the same time not rewarding the party doing the burning either. In other words, it is supposed to be neutral to both parties. Otherwise, the hedge fund is effectively getting the value of the burns, in some cases, which is contrarian to the point, right?

---

### Post #8 — **wigglemuse** | 2021-11-27 17:03 UTC

mmmmm… I don’t know. Let’s make things less confusing.

Firstly, put “the hedge fund” aside as none of this strictly comes from the actual hedge fund per se. Just say Numerai. Numerai has a treasury of NMR. It exists to pay us, not for Numerai to buy things. A few times though they have sold NMR (with a lockup period) to investors directly (people investing in the NMR token, not investing in the hedge fund). So it seems it doesn’t exist STRICTLY to pay us, but basically that is what it is there for.

Now, whats a burn? We use the term “burn” in two senses around here. One, the ordinary everyday “I burned today” or “I burned this round”. This first one has (almost) no meaning whatsoever since daily scores are just pretend anyway (except for one score a week for the round that resolves). The second one means the user actually lost some of their stake with a negative round. So that’s a real burn for the user – that stake is gone. They may earn enough later to make it back, but they well and truly lost it just like any other bet you might lose. So both of these are the first sense of the term – the user lost some of his stake and it is no longer theirs.

The second sense of “burn” is that the underlying NMR is destroyed forever – nobody ever gets to have it again and the total amount of NMR that exists in the world is now less. It is in this sense that I am talking about when I say “real” burns are rare – actual NMR being destroyed forever.

And so what’s happening generally when an individual burns is the first type – they lost it, but no NMR is lost from the world forever.

But I should have clarified further because the first scenario you posited when Numerai is out 100 from their treasury is not something that would happen even if real burns happened every week. If you lose NMR, nothing comes out of Numerai’s treasury, why would it? It is _YOUR_ NMR that you lose when you burn, not Numerai’s. It was NMR you had acquired on the open market and staked. If it was really burned, then Numerai loses nothing and gains nothing – there is just less NMR in the world. Numerai only loses NMR when you win and they have to pay out, not when you lose. (Whether the burns are “real” or not doesn’t matter to that.) Which is why in theory if you lose and then completely cash out, that lost NMR should really be burned, because otherwise where is it? If it isn’t yours anymore and it isn’t destroyed, then somebody else must now have control over it, right? Except that’s not right – that shouldn’t happen, so it should be burned for real (and that’s all “being destroyed” means – it means the NMR is sent somewhere that nobody ever has access to). But possibly they are netting it out over all users or something and it still isn’t really burned as long as they are paying out in total. It is all to do with ETH contracts and I don’t understand it. So we need the technical explanation of what actually happens there from the team.

So to sum up, however burning occurs, it is always YOUR stake that burns and burns don’t cost Numerai anything except for the bad trades they might make from your crappy predictions that burned.

---

### Post #9 — **ganon** | 2021-11-27 18:00 UTC _(reply to #8)_

Okay, I understand the distinction between burn in the colloquial sense (doing badly on a particular day) and the formal sense (NMR actually being burned, for realsies.)

Now, that being said, I’d like to return to my earlier example and get another clarification.

![](http://forum.numer.ai/user_avatar/forum.numer.ai/wigglemuse/48/3094_2.png) wigglemuse:

> But I should have clarified further because the first scenario you posited when Numerai is out 100 from their treasury is not something that would happen even if real burns happened every week.

You said that in the first scenario I gave, Numerai would never have been out 100 NMR in the first place even if true burns happened in real-time. I was not suggesting that NMR owned by Numerai was being burned, but rather, the NMR that I had staked was burned. That is, I had started with 100 NMR, lost 50 NMR (in which case, it should be true burned, lost forever) and then continued staking with that remaining 50 NMR until I had eventually earned 100 NMR, ending with a final account value of 150 NMR. Then, I decide I have had enough and withdraw.

How would, in this case, Numerai not pay out that 100 NMR? Since the account had 50 of its own NMR burned, Numerai would have to pay 100 NMR, less the account would not be credited its due. The only way for Numerai to not pay 100 NMR would be for the burns to not be true burns, to have not actually happened. If that is the case, then Numerai would have benefitted from that, since less NMR is required to be paid out of the treasury and the total supply would not have lessened.

I’ll just mention that I glanced at the smart contracts and the only logic they contain is the operations on the chain (which makes sense.) That would mean that how much NMR is burned and distributed from the treasury is determined by some backend logic on Numerai’s servers, along with where they keep track of which models burned and earned NMR (among other things.)

---

### Post #10 — **wigglemuse** | 2021-11-27 18:09 UTC

Oh yes, sorry, I guess you didn’t say that. I was concentrating on the second part and should wait to comment until I finish my coffee. But yeah, anyway, what I’m saying is that it is all on paper until you cash out, and then anything you’ve made over and above what you put in is what it actually costs Numerai. (How exactly this is calculated with partial withdrawals I don’t know.) But we can see that real burning doesn’t occur very much at all or else that total supply would be a lot less and decreasing every period we have a bad run, and it doesn’t. The vast majority of people either are not cashing out or are cashing out as net winners. (Which has not been difficult in this current incarnation of the tournament if you have stuck around any decent length of time, even though there have been bad burns once in a while for most everybody.)

---

### Post #11 — **ganon** | 2021-11-27 18:27 UTC _(reply to #10)_

Hm. Okay, I appreciate the clarification. Based on that, I stand by my sentiment that only burning on cashed-out net-losses is beneficial to Numerai and Numerai alone, since that means that in some cases, the treasury will retain more NMR than it would have with real-time, true burns.

After all, isn’t Numeraire supposed to be scarce? We should not be afraid of burning too much of it because of some bad periods because that just means that whoever is left owning some of it afterwards will be better off than those that made bad predictions and lost some. If the team is concerned about the supply being too low and it negatively affecting other areas, then they could adjust those areas. For example, payout factor comes to mind. Instead of being a hard cap of 300,000 NMR, it could scale down with burns as they are made. So, for example, if the supply of NMR decreases by 1 million NMR, then it would have seen about a 9% reduction so the cap could be reduced to about 272,728.

It’s important to do it like this because there needs to be a way to punish bad predictions neutrally, without it benefitting anyone. I would argue it benefits Numerai now with the current system.

---

### Post #12 — **wigglemuse** | 2021-11-27 19:06 UTC

Eh…maybe. Have to think about that on a day when I can think better. You’re isolating one detail (Who says the burn/earn time horizon should be weekly, or monthly, or whatever, and not just net total when you cash out? It is somewhat arbitrary.) Overall the system is actually stacked in our favor – they absorb lots of costs in gas fees (10s of thousands USD a week at one point – don’t know what it is like now), and with overlapping staking we actually get to essentially stake with leverage (the full amount of our stake is staked on 4 rounds at once – there are 25% payout/burn caps each round to keep this within reality, but in practice nobody ever gets near them). So far the tournament has been a massive giveaway to the users – they’ve cut back on that aspect over time out of necessity, but still I’m not sure “Numerai benefitting” in the case of our losing followed by our winning is a concern. I want a healthy prospering Numerai after all. If they were “the house” and just got to keep our losses, that’d be an actual problem, but netting out the calculation over time doesn’t give them an incentive to want us to lose, which is the important thing. They only truly benefit (i.e. make good trades) when we benefit also, and if we are burning so is the hedge fund…

---

### Post #13 — **thekizoch** | 2022-01-18 02:00 UTC _(reply to #5)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/ganon/48/2267_2.png) ganon:

> has been burned?”, and “How much NMR is distributed/burned on average per week?”. My hope is that if I can answer these questions, I can answer bigger questions like “How long until the hedge fund (probably) runs out of NMR?” and “How much NMR will (probably) be burned in a year? 2 years? 3 years?”
> 
> Now, as part of that research, I have been looking at round performance data for all users in the tournament, however I noticed that from round 201 and before, there is no payout data, despite there having been payouts (I think.) So I wanted to know why this is the case? I could just calculate the payout with the corr/mmc, payout factor, and modifiers, but I know I’d still be wondering about this.
> 
> Additionally, why is there no data at all before round 168? From what I have read, it sounds like NMR was originally conceived in Feb 2017 and people started to have it in June 2017, but the round data goes back to August 2017 so what happened in between?

you’re so funny man, I love reading how you write. thanks for be entertaining as you enlighten all of us with clarification. ![:grinning_face_with_smiling_eyes:](http://forum.numer.ai/images/emoji/twitter/grinning_face_with_smiling_eyes.png?v=12)
