---
title: "Monetizing (further) your models"
category: Tournament
url: https://forum.numer.ai/t/monetizing-further-your-models/3197
created_at: 2021-05-04T06:41:08.614000+00:00
last_posted_at: 2021-05-19T22:06:53.416000+00:00
posts_count: 27
views: 4122
tags: []
---

# Monetizing (further) your models

---

### Post #1 — **sirbradflies** | 2021-05-04 06:41 UTC

Hi,

The NFT experiments of [@hb_scout](</u/hb_scout>) got me thinking on how to increase the value of your model without increasing your NMR exposure in case you can’t or don’t want to.

I would like your opinion (legal, economical and alignment with Numerai’s spirit) on these different approaches:

  1. **Sell your weekly predictions:** [@hb_scout](</u/hb_scout>) approach. Simple and straightforward, the sale can be promoted here in the forum and sold via OpenSea/NFT (although with high gas friction costs) or traditional ecommerce channels (ebay, shopify, plain old paypal)
  2. **Rent a model:** License your model and give access to the renter (maybe through stake/unstake-only API keys) while you keep submitting normally
  3. **Create a small fund:** Potentially by making a portfolio of your (and other participant’s?) models and stake investors’ money on their behalf, with the typical hedge fund compensation structure.



I understand this may not be in the spirit of Numerai’s tournament but there is a fair chance for good data scientists that could be burned by the NMR volatility or maybe don’t have the funds to invest in their promising model.

Let me know what you think!

---

### Post #2 — **nyuton** | 2021-05-04 07:01 UTC

This all goes into the wrong direction, in my opinion.  
Investors should invest in the hedge fund not in data scientists…

The real question is, when are we going to have a real accessible fully loaded hedge fund?  
That would make NMR also less volatile and probably individual models less profitable then the hedge fund itself!

---

### Post #3 — **sirbradflies** | 2021-05-04 09:43 UTC _(reply to #2)_

Hi nyuton,

For sure it would help and having a stable NMR (e.g. through hedging) would go a long way in making the tournament less risky.

My point however is a bit different: how can good data scientists be rewarded irrespective of the amount of money they are willing/able to invest?

I believe that most of the current NMR “whales” were here since the beginning and things are going great for them but what about the incentives for the newcomers?

Just throwing ideas, I don’t really have an answer for these questions!

---

### Post #4 — **nyuton** | 2021-05-04 17:01 UTC _(reply to #3)_

If a data scientist is not willing to bet some money on his model, then why should anyone do so?

---

### Post #5 — **liz** | 2021-05-04 17:23 UTC

I sell predictions privately to multiple clients currently. I would love to run a fund (with or without other modelers) that NMR investors could participate in but have been warned that it appears to be illegal, so I’m holding off on that right now.

---

### Post #6 — **gammarat** | 2021-05-04 19:36 UTC _(reply to #4)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/nyuton/48/687_2.png) nyuton:

> If a data scientist is not willing to bet some money on his model, then why should anyone do so?

Because they DS’s are already investing their time and energy. You see that a lot in science and hi-tech startups, for example (or at least you used to, I’ve been retired for over a decade).

---

### Post #7 — **mindyoself** | 2021-05-04 21:41 UTC _(reply to #4)_

[@nyuton](</u/nyuton>) is right an investor will probably not care about the data scientists time and energy, they want the roi, if you don’t show them you have confidence in your models by staking to prove it has that potential or at least that your models have the potential to through ascending up the ranks it will be hard for them to back it or even understand the need to back it.

---

### Post #8 — **mindyoself** | 2021-05-04 21:57 UTC

That said I have always wondered and even wrote a little post about it and became quite concerned about how the regulatory side would work as [@liz](</u/liz>) has just pointed out if one was thinking about a fund and also the legal framework you would need to go through. I am based in the UK so the regulator is FCA [Investment managers](<https://www.fca.org.uk/firms/investment-managers>), so one must be careful. I guess the same for FINRA or SEC for the USA, but the crypto side is unregulated for some tokens, I don’t know if numeraire as a utility token loses it’s status if one uses it as an investment. The difficulty as well is whether selling models to buyers fall under a similar remit needing regulation. But I think that provided the buyer of the models understand the disclaimer that they may lose their stake and there are no guarantees that’s okay. Do correct me there.

Different countries will have their rules about setting up a fund as well which muddies the water. Perhaps a future Numerai upgrade could be the ability to integrate the necessary governance and legal support and documentation for a subfund ecosystem to flourish. It will be interesting to see.

---

### Post #9 — **wigglemuse** | 2021-05-04 22:06 UTC

I don’t see why selling your predictions is a problem – possibly some disclaimers are needed – but in the U.S. you can’t just manage/control other people’s money without proper licenses and registrations. (There are some narrow exceptions, but generally it is a no-no.)

---

### Post #10 — **sirbradflies** | 2021-05-05 03:55 UTC _(reply to #5)_

Hi [@liz](</u/liz>), I am curious about that.  
Can I ask you where did you “promote” your models?  
Thanks

---

### Post #11 — **liz** | 2021-05-05 13:07 UTC _(reply to #10)_

I shared on a twitter post, my twitter profile, my strongest model profile, and conversations with friends who were already interested.

---

### Post #12 — **nrichers** | 2021-05-06 21:38 UTC _(reply to #5)_

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/numerai.discourse.group/liz/48/1103_2.png) liz:

> I sell predictions privately to multiple clients currently.

I am quite surprised with this statement, because at first I believe this market is targeted to beginner users who wants to leverage their gains, using better predictions…

I think it is very difficult to overcome the opportunity cost to stake in example predictions… The buyer need to have stake enough to compensate the cost of the predictions and discount it by example predictions performance assuming the risk to stake in an unknown model.

Otherwise as an intermediate level participant I see some value in late round predictions to see feature exposure profile… I mean, I won’t be able to stake but I still can check the veracity through daily scores and get the exposures…

You can see below the exposures from a LGBM model over the test data  
(obs: val2&3 truncated can cause some friction)

[![test_SF2_L1_new](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/2e55da84382b43e4651236c9268783efa546b615_2_690x399.png)test_SF2_L1_new1118×647 256 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/2e55da84382b43e4651236c9268783efa546b615.png> "test_SF2_L1_new")

---

### Post #13 — **sirbradflies** | 2021-05-07 02:11 UTC _(reply to #12)_

hi [@nrichers](</u/nrichers>), can you clarify how you produced this chart?  
Thanks

---

### Post #14 — **nrichers** | 2021-05-07 06:11 UTC _(reply to #13)_

You can get the exposures using the snippet below and then create a heatmap
    
    
    corr_series = df.groupby("era").apply(lambda d: d[feature_columns].corrwith(pred))

---

### Post #15 — **sirbradflies** | 2021-05-08 08:19 UTC _(reply to #14)_

Great [@nrichers](</u/nrichers>), thanks!

---

### Post #16 — **patrickl** | 2021-05-11 16:43 UTC _(reply to #5)_

I’m quite optimistic that legality should not be an issue if done correctly:  
If I look at the DeFi-Space certain “projects” promise yield farming, similarly the way we farm NMR yields when our predictions are correct.

So in direct comparison:

  1. NMR yield farming is a lot more transparent than most of those BSC-Coins… If we run a fund and let LPs invest, the LPs dont know what our models do, but at least they know what we do. in the BSC space nobody knows what anybody does… there is just money/APY falling from trees - don’t bite the hand that feeds you right?.
  2. Our yields do not depend on market/protocol liquidity, futures contango, arbitrage, etc. We perform every week regardless of what happens to the market, since our predictions are market neutral.



So how would we go about this? Launch a DeFi project?  
I’m seeing great similarities between a possible NMR model fund and what Unagi is doing ([Unagii App](<https://app.unagii.com/explore>)).  
Unagi takes your ETH or whatever coin and invests it according to certain risk/reward strategies (vault vs growth)… you could do the same with NMR models.  
On a technical level it looks like Unagi converts your coins into a staked version of your coin, hence ETH to sETH (which they trade on the Curve Protocol) and at the same time you receive a bearer asset, Unagi ETH or uETH, which allows you to redeem the sETH - all done via their smart contract.  
I’m pretty sure with the right technical knowledge one could set up the same version:

  1. Have certain strategies, depending on risk and return
  2. Allow people to invest their NMR, which then we, as the fund, handle as sNMR in our models
  3. And they get back uNMR (u doesnt fit well since its branded by Unagi, but you get the point) which they can redeem when they want to, according to our conditions (10% profit fee, 4 month min lock up, whatever).



All you need is the smart contract… and some big brain juice to fit it all together

This is just brainstorming / thinking out loud… if anybody has input let’s talk it through!

---

### Post #17 — **liz** | 2021-05-11 21:21 UTC _(reply to #16)_

I’m not sure if you’re asserting that other defi projects existing is a basis to believe that operating an investment fund without proper licensure etc is legal, but it kinda sounds like that. Regarding the idea that splitting aspects of the operation into different assets/processes etc, I am not aware of laws in other countries, but in my county (USA) “[structuring](<https://en.wikipedia.org/wiki/Structuring#:~:text=Structuring%20is%20the%20act%20of,by%20regulators%20and%20law%20enforcement.&text=Structuring%20appears%20in%20federal%20indictments,fraud%2C%20and%20other%20financial%20crimes.>)” is a crime. So, splitting up parts of a process that may be illegal, does not make it legal (for me).

I’d love to ask a lawyer about this kinda stuff, but the reward/capital available I have right now doesn’t allow for that.

It’s worth noting that my legal risk tolerance is extremely low because (a) I am domiciled in the USA and (b) I have had many friends lose their livelihood/have a huge portion of their assets frozen for years because they were seized as part of a legal action the poker community referred to as “Black Friday” (but for poker)

There may be others with different risk tolerance or different situation who may want to work on this stuff!

---

### Post #18 — **patrickl** | 2021-05-13 08:38 UTC _(reply to #17)_

I get your point, but the structuring shouldn’t be the focus… I think.

Basically, if somebody can offer 100% APY as an ERC-20/BSC token via a smart contract, why can’t we do the same? - I’m quite sure this should be possible, since there just isn’t a difference… or am I missing something??  
If anything we should have an advantage because our APY is stable, compared to most of those defi scams

---

### Post #19 — **liz** | 2021-05-13 11:47 UTC _(reply to #18)_

what makes you think returns here are stable? interesting idea. not really up my alley development-wise, I’d have to think more about the risks before joining a project like that.

---

### Post #20 — **patrickl** | 2021-05-13 14:50 UTC _(reply to #19)_

Well we can of course discuss “stable” and the definition of that… But surely our models returns, grouped together would generate quite a stable/steady return.

I am submitting 3-4 models on signals and have been outperforming the SnP with lower vol/risk. If I look at the DeFi… Apy’s go from 25% to 250% and just fluctuate. While my weekly return has been between 1.1% and 1.3% for >2 months now… The more models, the steadier right - typical diversification.

---

### Post #21 — **xkl4z** | 2021-05-18 19:35 UTC _(reply to #6)_

No, not everyone’s time and energy is valued equally. We have nothing to go on about any person on here except their internet profiles, which honestly doesn’t hold much water since we have no idea about the quality of their work. The only way to be certain is if they have skin in the game.

---

### Post #22 — **gammarat** | 2021-05-18 20:00 UTC _(reply to #21)_

I think scores and consistency say a lot more about the quality of the work. But to each their own.

---

### Post #23 — **xkl4z** | 2021-05-18 22:11 UTC _(reply to #22)_

That’s only during green runs. I’ve seen some top performing models that have appeared to be consistent until recently where they have slipped for several weeks in a row. Suppose one buys one of those predictions. If the developer suddenly stops staking, you can be sure they’ve lost some confidence in the model or something. It’s another signal. If they just never stake, you can’t really tell. I’m not saying it guarantees anything, but it’s like the various cryptocurrencies popping up everywhere where in some cases you know the identities behind the project and in others, you don’t. Not a guarantee, but definitely easier to buy into.

---

### Post #24 — **mic** | 2021-05-18 23:20 UTC _(reply to #20)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/patrickl/48/2994_2.png) patrickl:

> If I look at the DeFi… Apy’s go from 25% to 250% and just fluctuate

Can they go negative?

---

### Post #25 — **jackerparker** | 2021-05-19 10:45 UTC _(reply to #21)_

I disagree with you about “the only way to be certain is if they have skin in the game”. Even if someone stake a huge amount of money, you have no idea how risky this amount of NMR for that person. Some people spend a lot of money in casino just to feel excitement and not to make money.

And here is my example: my models were in top of the Numerai’s leaderboard and the workflow itself was “cross-validated” in similar competition on Kaggle (top 1% position in current live leaderboard). So, in general I’m pretty confident about the quality of my models, but I will not stake any NMR due to risks related to some local laws.

---

### Post #26 — **mindyoself** | 2021-05-19 19:34 UTC _(reply to #25)_

That is a fair point, your risk tolerance is a factor to consider too. [@jackerparker](</u/jackerparker>), welcome back, I remember reading once that you had to stop competing. Out of interest what was the rule in your country that stopped you monetizing your models or being part of the competition?

---

### Post #27 — **jackerparker** | 2021-05-19 22:06 UTC _(reply to #26)_

No restrictions actually for being part of the competition or any monetizing using fiat money, the only prohibits is for any cryptocurrency income for all kind of jobs, goods and services
