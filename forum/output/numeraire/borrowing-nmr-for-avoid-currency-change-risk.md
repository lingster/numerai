---
title: "Borrowing NMR for avoid currency change risk"
category: Numeraire
url: https://forum.numer.ai/t/borrowing-nmr-for-avoid-currency-change-risk/2866
created_at: 2021-04-14T17:38:24.237000+00:00
last_posted_at: 2025-12-28T09:16:03.379000+00:00
posts_count: 27
views: 4096
tags: []
---

# Borrowing NMR for avoid currency change risk

---

### Post #1 — **eleven_sigma** | 2021-04-14 17:38 UTC

Hi, I’m interested in stack up to 50K - 100K USD to my predictions. I know what I need is to buy NMR, but I don’t want to deal with currency change risk. I accept the rules of the Numerai game and I’m confident in my models, but I don’t know when the crypto bubble can explode.

Is there a way of taking borrowed an amount of NMR, as if I wanted to short sell them, but use for stacking to predictions?

---

### Post #2 — **ml_is_lyf** | 2021-04-15 11:24 UTC

Can’t you do this with DeFi? Just take a DeFi loan of NMR and collateralize it with some other crypto you have more confidence in (USDT probably would be best in your case from the sound of it). I guess the problem is then you’re taking on the risks that come with DeFi, but I think that sounds like the best solution. Richard was suggesting this in one of the Fireside chats for people who don’t want exposure to NMR.

---

### Post #3 — **epsilon0_5** | 2021-04-15 14:10 UTC _(reply to #2)_

Some people can/would want to, others likely not so much. For the hedge fund/numerai to perform well in the long run you’d like as many people as possible to tinker with it (bad tinkerers lose money and exit the system, good ones stay increaisng fund performance).

Both currency risk as well as as well as having to do the loan yourself (figuring out which crypto that would be & doing the operations that come along with it) are barriers to entry.

The most user friendly approach would likely be to allow users to stake any crypto, and secure the network via numeraire, and have staking pay overall dividends of the fund to incentivise staking (if you’re more confident in numeraire as a whole, hold numeraire, if more in your own model, use whatever currency you’re comfortable with).

this would likely require a complete overhoal though…

---

### Post #4 — **ml_is_lyf** | 2021-04-15 19:04 UTC _(reply to #3)_

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/e/2bfe46/48.png) epsilon0_5:

> The most user friendly approach would likely be to allow users to stake any crypto, and secure the network via numeraire, and have staking pay overall dividends of the fund to incentivise staking (if you’re more confident in numeraire as a whole, hold numeraire, if more in your own model, use whatever currency you’re comfortable with).

The problem with this though is if you allow people to stake in different currencies how do you build the metamodel? For example NMR this week depreciated 1% against BTC, whereas XLM rose 17.4%. Should an XLM stake be weighted more at the end of this week because it appreciated more than NMR? Clearly not, as then the stake weighting in the metamodel is susceptible to currency swings.

The only way I can think of to avoid this is to treat a stake as the value of the currency in NMR at the point of staking. But then the incentive model starts to get weird. ETH is up 70% this year against BTC, whereas NMR is down 54% against BTC. Someone who staked in NMR will be more inclined to up their stake as it has depreciated in value, whereas someone who staked in ETH will be more inclined to sell. These incentives are external to the competition, so again this seems like it’d break stake weighting.

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/e/2bfe46/48.png) epsilon0_5:

> Both currency risk as well as as well as having to do the loan yourself (figuring out which crypto that would be & doing the operations that come along with it) are barriers to entry.

I agree the currency risks are concerning. I wouldn’t say they’re barriers to entry though, they’re more barriers to people making huge stakes like the OP is looking to do. It just means though you have to treat this as a very high-risk investment like any other crypto, hence don’t stake significant amounts of your savings unless you like high risks, and also dollar cost average your NMR purchases. When you start to think about how model returns compound though you don’t need that huge a stake to earn a decent return.

---

### Post #5 — **epsilon0_5** | 2021-04-15 21:07 UTC _(reply to #4)_

Yeah the implementaiton is a really big issue, and I sadly don’t have a solution for it.

I personally disagree about crypto in general being high risk. I consider it, and any single specific crypto, very risky, but outside events such as IMF worldwide bans on cryptocurrency safer than traditional investments, if my working hypothesis is correct* .

let me put it this way: I don’t know what could happen, but I’m not putting more than 10% if my investment funds into any single crypto, and will be diversifying towards things outside crypto once I acumulate a bit more capital in crypto (in hope nothing happens before I accumulate some basic amoutn of capital, which is required for some things, sigh). if you fully trust that nothing could happen to the value of numeraire in the short term (at any point in time I mean, i have no reason to doubt it in the short term particularly now), or will be continually purchasing & using through DCA then I guess that’s fine. but if you buy some to try it out, and the price drops I’m afraid I might raitonalize myself into going on untill my cash is back up to the original level (difficulty seeing numeraire as reference currency I guess).

I’m a bit of a paranoid person though, so it might not be a big a problem as I think for others.

*about which I’m not sure and only time will tell because we’re in a bullrun & historical data is expensive so backtesting isn’t really an option for me atm. (would need data on all publicly traded stocks currencies & a graph of their dependencies, so yeah :l )

---

### Post #6 — **mindyoself** | 2021-04-18 23:39 UTC

Wouldn’t another legit strategy be holding a fully diversified non-correlated crypto asset portfolio as hegde against the risk exposure of your NMR stake? I mean until we have better risk management tools it seems wise to not put a lot in a single basket. I have always invasaged an NMR stake as a long term investment gig so why not treat the staking process as such to help eliminate the emotion linked to the burn? So consider the problem as a supply demand construct where as the NMR supply falls the value of stake will appreciate to offset any initial value-related losses you might have acrued. Your incentive to mitigate loss is to generate better models that will elevate the funds success and as long as you are achieving that goal you can take emotion out it and protect your stake using other methods. It still does to acquire and accrue NMR at a lower price. The DEFI method sounds like a neat idea to explore as well so will look into it thanks [@ml_is_lyf](</u/ml_is_lyf>), [@epsilon0_5](</u/epsilon0_5>) and [@eleven_sigma](</u/eleven_sigma>) for a stimulating chat.

---

### Post #7 — **ml_is_lyf** | 2021-04-19 20:01 UTC _(reply to #6)_

Yeah definitely. I consider Numerai as diversification for my investment portfolio as well. You can fix the percentage of your portfolio you want to allocate (e.g. 70% equities, 15% crypto, 15% Numerai, or whatever you fancy), and then do periodic rebalances (e.g. once a year or once a month). This way when Numerai is doing well you’ll take the money out and put it into your other investments, and when it does badly you’ll put more money into Numerai. Given Numerai for now at least seems to significantly outperform other asset classes, with this approach it seems that you’ll very quickly end up selling more Numerai than you’ve bought, then your percentage return is effectively infinite as your acquisition cost is 0 ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=9)

---

### Post #8 — **sirbradflies** | 2021-04-20 04:21 UTC _(reply to #7)_

This is a question I have been struggling with for a while as I would like to stake more. I am quite confident about my models but not as much on NMR stability. I don’t think putting money in other crypto currencies is a real diversification; most crypto are significantly correlated and when a crypto-crash will happen NMR and the others will go down in tandem as they are now going up.

It would be good to have an hedging tool to be able to isolate model’s from NMR performance.

---

### Post #9 — **nyuton** | 2021-04-20 12:48 UTC _(reply to #2)_

Can you please point to a platform, where a NMR loan is possible? I haven’t found any yet!  
thanks

---

### Post #10 — **ml_is_lyf** | 2021-04-20 16:58 UTC _(reply to #9)_

Good point. Surprisingly doesn’t look like there are any at the moment. I guess that makes sense as NMR is a pretty small cap, maybe if the cap gets bigger someone might make it lendable.

[@sirbradflies](</u/sirbradflies>) point here might help with this though.

![](http://forum.numer.ai/user_avatar/forum.numer.ai/sirbradflies/48/2766_2.png) sirbradflies:

> I don’t think putting money in other crypto currencies is a real diversification; most crypto are significantly correlated and when a crypto-crash will happen NMR and the others will go down in tandem as they are now going up.

You could just borrow a coin that highly correlates with NMR, and then trade that coin for NMR. That should help mitigate the risks of a total market crash, and help mitigate some of the risk of a Numeraire crash. But of course, the downside is you’re adding the risk of another crypto to the mix.

---

### Post #11 — **sirbradflies** | 2021-04-21 05:14 UTC _(reply to #10)_

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/m/e56c9b/48.png) ml_is_lyf:

> You could just borrow a coin that highly correlates with NMR, and then trade that coin for NMR. That should help mitigate the risks of a total market crash, and help mitigate some of the risk of a Numeraire crash. But of course, the downside is you’re adding the risk of another crypto to the mix.

Do you mean something like USD → XXX (random crypto) → NMR? Why would that be more hedged than USD → NMR?

---

### Post #12 — **ml_is_lyf** | 2021-04-21 08:15 UTC _(reply to #11)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/sirbradflies/48/2766_2.png) sirbradflies:

> Do you mean something like USD → XXX (random crypto) → NMR? Why would that be more hedged than USD → NMR?

Yeah, USD → NMR hedging is definitely way better. But no one seems to be loaning NMR at the moment so that’s not possible to do right now. USD → XXX (random crypto) → NMR is a suggestion if anyone wants to do this now. Just have to be aware that if XXX rises against NMR then you’re going to get burnt.

---

### Post #13 — **eleven_sigma** | 2021-04-21 08:20 UTC _(reply to #12)_

How do you see if someone offer NMR to loan?

---

### Post #14 — **ml_is_lyf** | 2021-04-21 16:20 UTC _(reply to #13)_

I just did a quick Google for DeFi lending platforms and then took a look at the most popular ones. No one offering NMR at the moment looks like

---

### Post #15 — **jorijnsmit** | 2021-04-21 17:51 UTC

I don’t understand how lending NMR changes your exposure to NMR. You will still need to settle that loan someday right, at market prices? What’s the difference with buying NMR?

---

### Post #16 — **wigglemuse** | 2021-04-21 18:18 UTC _(reply to #15)_

You just give back the NMR, in NMR. Presumably after having generated even more NMR in the tournament (the extra you keep as your profit). As long as you didn’t burn it, the underlying price doesn’t matter – you return what you borrowed.

---

### Post #17 — **ml_is_lyf** | 2021-04-21 18:21 UTC _(reply to #15)_

Also, you collateralize your loan with another crypto. So when you return the money you borrowed you get all of your collateral back. So if your collateral is in a stable coin like USDT, if there was a market crash then that wouldn’t affect the value of your collateral. Whereas if you’d bought the NMR with USD, then if you want to sell back your NMR for USD after a market crash you won’t get back as much USD as you paid for the NMR orginally.

![](http://forum.numer.ai/user_avatar/forum.numer.ai/jorijnsmit/48/2305_2.png) jorijnsmit:

> I don’t understand how lending NMR

Slight nuance here, but yeah lending someone your NMR wouldn’t protect you. Lending makes sense if your’re HODLing NMR and you want to get some interest, you could loan it to someone else. I don’t think that would make sense for tournament participants though, as if you lend it you can’t stake the NMR.

---

### Post #18 — **eleven_sigma** | 2021-04-21 20:10 UTC _(reply to #17)_

Suppose I buy 1000 NMR at 70 USD, so I invest 70K USD and I plan to stay one year fitting models.  
I earn during this year 1000 NMR so I’m very happy!  
I sell the 2000 NMR that at that moment is at 25 USD so I will have 50K USD. I will loss 20K USD.

Now with a loan:  
I take a loan of 1000 NMR at 10% of yearly interest. If NMR is at 70 USD this cost 7K USD.  
I earn 1000 NMR during a year. At the end I give back the loan of 1000 NMR and have 1000 NMR that assuming is at 25 USD represent 25K USD minus the cost of loan I would earn 18K.

For me the advantage of loan respect buy is clear in this scenario.  
Obviously if in a year NMR is at 100 USD then the option of buy is better, but if you want haven’t exposure to NMR the loan is the way.

---

### Post #19 — **74_545** | 2021-04-24 06:42 UTC _(reply to #18)_

Why not ask NMR holders for NMR? You can offer them % of your returns if your model is successful. Like a marketplace where an owner of a prediction can offer a StakeOnMyPrediction contract. Anyone can see the performance history of predictions and can stake their NMR in this contract.

---

### Post #20 — **lucky_chicken** | 2021-04-24 16:31 UTC _(reply to #18)_

But if you look at it from the person loaning your the NMR it would not make a lot of sense to give you an NMR loan at yearly 10%. Especially given the fluctuation fo NMR and the fact that you can make much more than 10% by just staking the example submissions. It seems that you would have to pay significantly more. 200%?

---

### Post #21 — **ml_is_lyf** | 2021-04-25 21:58 UTC

Was just watching the Fireside Chat for Q1 2021 and Richard discusses borrowing NMR, here’s the timestamp:

[ ![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/3b71b2c10e78e4e6f8da0a07dea7eac227cb6cb0.jpeg) ](<https://www.youtube.com/watch?v=hb3GeT7czO8&t=945>)

---

### Post #22 — **nyuton** | 2021-05-03 07:57 UTC

Check out this post to see how to get NMR without the price risk: [How to break free of NMR price risk](<http://forum.numer.ai/t/how-to-break-free-of-nmr-price-risk/3178>)

---

### Post #23 — **sdimov101** | 2021-06-23 12:06 UTC _(reply to #9)_

You might want to up-vote this proposal to AAVE [ARC: Add support for NMR - New Asset - Aave](<https://governance.aave.com/t/arc-add-support-for-nmr/3982>) It increases the chance of NMR getting accepted and be loan-able there.

---

### Post #24 — **jorijnsmit** | 2021-06-23 13:06 UTC

Not to spam too much but I think this forum post is very relevant to this discussion: [[Proposal] Provide NMR lending liquidity on Kashi - #10 by giulianociccone](<http://forum.numer.ai/t/proposal-provide-nmr-lending-liquidity-on-kashi/3633/10>)

---

### Post #25 — **taylor2** | 2025-11-17 15:02 UTC

Hello! Has there been any update on hedging NMR price risk since these posts from 2021? What would be the best practice nowadays?

---

### Post #26 — **wigglemuse** | 2025-11-17 23:37 UTC _(reply to #25)_

It was recently listed on this perp exchange <https://lighter.xyz/>, so that’s something. (That’s not a recommendation, I don’t know much about the place yet.)

---

### Post #28 — **correlator** | 2025-12-28 09:16 UTC

Related, recent post: [NMR price hedging: 2026 edition](<https://forum.numer.ai/t/nmr-price-hedging-2026-edition/8213>)
