---
title: "How to break free of NMR price risk"
category: Numeraire
url: https://forum.numer.ai/t/how-to-break-free-of-nmr-price-risk/3178
created_at: 2021-05-03T07:39:58.787000+00:00
last_posted_at: 2024-06-01T07:44:19.988000+00:00
posts_count: 27
views: 5852
tags: []
---

# How to break free of NMR price risk

---

### Post #1 — **nyuton** | 2021-05-03 07:39 UTC

Hi,

there have been some discussion on the risk associated with the NMR price. As far as I know, no real solution has been posted so far.

So here is my solution:

  1. Buy (let say 100) NMR on Coinbase
  2. Stake that 100 NMR on you model
  3. Short sell 100 NMR on Coinbase ([pro.coinbase.com](<http://pro.coinbase.com>) let’s you do it)
  4. Make some profit with you model ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=9)



The result:

  * The two 100 NMR positions will cancel each other. You have no risk of volatility on that 100 NMR
  * The NMR you earn in the tournament is yours at the current NMR price level and it’s risk free
  * You pay a small fee for holing a short position
  * The two positions you hold are not going to push the NMR price any higher ![:frowning:](http://forum.numer.ai/images/emoji/twitter/frowning.png?v=9)
  * Staking more on the models, you are confient with could benefit Numerai on the long run
  * Yes, you will need 200 NMR worth of USD to do this. Still this solution is still better than no solution at all.



Enjoy and stake more!

---

### Post #2 — **ml_is_lyf** | 2021-05-03 08:28 UTC

This is a great idea. Being equally long and short makes a lot of sense in this context. I guess you could do this with DeFi too (if it was available), just buy an equal amount to that you borrow. I’ve had a quick look though and looks like this was only possible through margin trading on Coinbase, which looks like they discontinued?

<https://help.coinbase.com/en/pro/trading-and-funding/trading-rules-and-fees/margin-trading-faq>

---

### Post #3 — **nyuton** | 2021-05-03 08:31 UTC _(reply to #2)_

It’s possible, I’ve just checked it. I’m not sure, if it’s on margin.  
Anyway, if not Coinbase then some other exchange will do it for you.  
Coinbase is only my choice…

---

### Post #4 — **ml_is_lyf** | 2021-05-03 08:55 UTC _(reply to #3)_

Interesting, I didn’t realize other exchanges sold NMR. You can buy NMR on Binance and it seems to have the functionality to do this as discussed here:

<https://www.binance.com/en/support/articles/8b56bdc50b154385acec2af652b4ad10/>

I’m curious about Coinbase if you have any links of how to do it though. I couldn’t find any and it doesn’t seem obvious where it is in the UI.

---

### Post #5 — **mic** | 2021-05-03 09:32 UTC

Could you be exposed to a short squeeze? Would you need to liquidate your staked NMR quickly to cover it?

---

### Post #6 — **nyuton** | 2021-05-03 09:52 UTC _(reply to #5)_

As long as you don’t use hugh leverage, you are safe.  
You keep this position open long term, which means large price swings (up or down).  
So big leverage will kill your position quickly.

---

### Post #7 — **ml_is_lyf** | 2021-05-03 10:51 UTC

For anyone curious, I think this is a good explanation of how you can short on Binance

[ ![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/6d29682028f678456d99be989ead5224be79f0c1.jpeg) ](<https://www.youtube.com/watch?v=99ENjbOadPA>)

And here’s the pair for NMR and USDT

![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/6/649745d88dd9ae285ef01cedef96359c77af719e.png) [Binance](<https://www.binance.com/en/trade/NMR_USDT?layout=pro&type=isolated>)

![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/a/a50f9e57c8973d7b5f87733075ba369a293071f9_2_690x388.jpeg)

### [9.17 | NMR USDT | Numeraire to USDT – Binance Spot](<https://www.binance.com/en/trade/NMR_USDT?layout=pro&type=isolated>)

Trade NMR to USDT and other cryptocurrencies in the world’s largest cryptocurrency exchange. Find real-time live price with technical indicators to help you analyze NMR/USDT changes.

From my understanding (I might be wrong on some things here as I’ve never looked into this stuff before, this is just my understanding after some research and thought today). If you had 100 USDT to put into the tournament, you’d buy 75 USDT worth of NMR and stake it in the tournament, and then you’d put 25 USDT in your Binance margin wallet. Then you borrow NMR to sell using your 25 USDT, which means you’re now short NMR by 75 USDT (as 3x leverage). Hence you’re both short and long NMR by 75 USDT, so that’ll cancel out the currency risk. You’ll probably want more than 25 USDT in your margin wallet though as I think if the price rises by 50% (hence your loss is 25USDT) then your short position will be liquidated and you’ll lose your 25 USDT.

Of course, now we’ve introduced exchange risk, as if Binance gets hacked etc. then you could lose all your money in your Binance margin wallet. So it’s really a trade-off of NMR currency risk for all of your currency, vs exchange risk for a fraction of your currency and incurring interest on your short loan.

I guess how you weigh up those risks depends on your sentiment for the long-term prospects of NMR. Personally I think its probably better to just DCA/VCA your NMR purchases.

---

### Post #8 — **mindyoself** | 2021-05-04 21:26 UTC _(reply to #7)_

Useful info thanks. Looks like a sound approach.

Although how about transaction fees, is that something to factor into this or does that not matter match for the pair?

It may be better if you exchanged your USD to BNB and traded BNBNMR to eliminate the fees, provided there is BNBNMR listed on binance?

---

### Post #9 — **mindyoself** | 2021-05-04 21:35 UTC

Are there options available to hedge against the price?

---

### Post #10 — **ml_is_lyf** | 2021-05-04 22:12 UTC _(reply to #8)_

Transaction fees are probably going to be pretty small relative to the loan interest. Yeah, I think in the video they talk about using BNB to pay your fees. You wouldn’t want to borrow using BNB though, as then you’re exposed to the currency risk of BNB, e.g. if BNB falls against USDT then you lose out.

---

### Post #11 — **ml_is_lyf** | 2021-05-04 22:15 UTC _(reply to #9)_

I think being short and long is hedging? As then if the price of NMR falls, the price falling doesn’t hurt you so much as you profit on your short position

---

### Post #12 — **mindyoself** | 2021-05-04 22:18 UTC _(reply to #11)_

I think I meant using actual Options as another form of hedging. Is there a market for Options for numeraire? That could be a market.

---

### Post #13 — **mindyoself** | 2021-05-04 22:18 UTC _(reply to #10)_

That’s a good point.

---

### Post #14 — **ml_is_lyf** | 2021-05-08 08:11 UTC _(reply to #12)_

Hmm good point. Not sure. But options are used for risk management to lock in the price of an asset. So yeah options would probably be another good way to manage risk. Might also eliminate currency risk as I don’t think you need collateral for an options contract

---

### Post #15 — **nyuton** | 2021-05-10 09:33 UTC _(reply to #14)_

Yes, but I’m not aware of any NMR options.  
However you can short sell NMR at any exchange!  
Easy…

---

### Post #16 — **jay1100** | 2021-06-06 16:04 UTC

Is it still possible to short sell NMR at coinbase pro? I thought they stopped margin trading: <https://blog.coinbase.com/coinbase-pro-disables-margin-trading-42f5862f8a66>

---

### Post #17 — **jorijnsmit** | 2021-06-23 13:05 UTC

USDC-NMR lending/borrowing smart contract is available on Kashi now: <https://app.sushi.com/bento/kashi/borrow/0x7bee2161afa1aee4466e77bed826a41d5a28db46>

This also allows for leveraged/short positions, without introducing any centralised entity risk.

I wrote a post about it [here on the forum](<http://forum.numer.ai/t/proposal-provide-nmr-lending-liquidity-on-kashi/3633/10>) with a more in-depth explanation of its exact workings.

---

### Post #19 — **sunkay** | 2022-05-26 10:01 UTC

If the price of NMR continues to go down, then the NMR you earn back is is going to be less and less valuable.

If your stake doubles your NMR and you cannot get double the cash return, that’s not fair!

---

### Post #20 — **wigglemuse** | 2022-05-26 14:58 UTC _(reply to #19)_

Yeah, I was wondering about that too. Even if you have a mind to borrow NMR to protect your staking investment, the new NMR you make is still only worth so much (and is not protected). You have to commit to going long one way or another, right?

---

### Post #21 — **kayeffnumeraitor** | 2022-09-01 15:38 UTC

I am considering tying that out, I have one problem with it though: There is still the lockup time of the NMRs being staked.

Lets say NMRs go up from where I initially placed my short position. At some point the stop will trigger my short position to be cancelled eating away my collateral. To cover my loss from the short position, I would have to immediately liquidate my staked NMRs, which I cant do for 4 weeks, which is a rather long time in the crypto world. While waiting for the now unprotected NMRs being released, NMRs could fall down again losing me even more money.

So sudden price hikes as seen in the last months are killing this strategy.

A solution for this would be some sort of naked short selling, because you essentially always have the NMRs you borrowed (if your model did not lose money), just not right now, but I don’t think you can do that anywhere.

Another option would be that Numerai reworks their staking system, so that it is possible to immediately withdraw the entire staked NMRs from a model. Obviously you would have to introduce some sort of punishment for that, like automatically apply the maximum burn for the given round. Then you would basically limit the loss to the early withdrawal punishment + your model earnings/burns since staking + all transaction fees for trading, which would be an acceptable risk for me.

---

### Post #22 — **taori** | 2022-09-01 16:11 UTC _(reply to #21)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/kayeffnumeraitor/48/991_2.png) kayeffnumeraitor:

> like automatically apply the maximum burn for the given round.

That is 0.25, but an active model is typically exposed to 4 rounds simultaneously, which means the maximum burn is 100% of the stake

---

### Post #23 — **kayeffnumeraitor** | 2022-09-01 16:49 UTC _(reply to #22)_

I meant only for one round. Having 25% of your stake burned because you bail out early should be harsh enough… For 4 rounds compound burning that would be around 68% burned not 100%, by the way.  
Edit: I always forget that the payouts are applied 4 weeks afterwards… I was not even aware of the theoretical possibility that you can lose your entire stake if you have 4 unlucky rounds.

---

### Post #24 — **dzheng1887** | 2022-09-02 17:28 UTC

We really just need a consistent market maker that will be or find the counter parties to 4-week long NMR forward contracts for each round. Perhaps speculators who are willing to buy and hold for 4 weeks would be interested to long the contract. But the nicheness of NMR is maybe not interesting enough for someone to set up this mechanism in large volume with decent liquidity. I think I saw APR of over 100% on some of the NMR swaps on the Sushi/Kashi page. I also don’t understand all this enough to feel comfortable engaging in such a platform where I need to use my head a bit. Would always feel I am missing something.

---

### Post #25 — **sneaky** | 2022-09-05 21:31 UTC

I think its more dangerous than holding nmr. The price of NMR is so damn spiky. You can get liquidated in no time. What is worse you can get liquidated on both sides in one day. IMO it is not worth the risk.

In order to make it work, one must have some money as backup for liquidation calls, that means less money staked, which is less earned, and you can always lose everything.

And the liquidity of the gains is another issue, plus gass fees.

---

### Post #26 — **dzheng1887** | 2022-09-05 23:27 UTC

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/s/4bbf92/48.png) sneaky:

> holding nmr. The price of NMR is so damn spiky. You can get liquidated in no time. What is worse you can get liquidated on both side

Going short yeah, but I think a forward contract managed by a market maker wouldn’t need that liquidation provision for counter-party risk (I am not sure though?). I was thinking like upon the delivery of the NMR, the agreed upon price could easily be paid by the receiver of the NMR no matter the prevailing market price.

There is a bit of risk if the NMR round performance doesn’t line up with the expected NMR amount in the contract however. Perhaps can allow the quantity to be variable +/- 10% of some stated amount.

So like buy 100 NMR at $10/coin for $1000 at available spot price. Use that 100 NMR to stake 1 model for 4 weeks (liquidate the model after the round). At the same time, enter into a forward contract with some counterparty at the available forward price, let’s say $9.8/coin. Wait 4 weeks to get NMR distribution of 120 NMR let’s say (20% return). Sell 110 NMR at the contract forward price of $9.8 and the other 10 NMR at the prevailing spot price at the time. Do this with a different model slot for each of the 4 weeks.

---

### Post #27 — **sneaky** | 2022-09-07 17:39 UTC _(reply to #26)_

sorry, I forgot to reference the post I was writing about. My reaction is on the idea of staking on borrowed nmr, and or shorting nmr.

---

### Post #28 — **pumplerod** | 2024-06-01 07:44 UTC

Could there be a slow transition to a NMRUSD Stable coin if it went something like this…

  * At the time payouts need to be made, Numerai converts The payout NMR into a newly minted USDNMR at whatever the current market rate is. Ideally, all NMR currently at stake would get converted to this USDNMR in a single event, but this may be too costly for Numerai to pull off.
  * participants are allowed to stake both NMR and USDNMR in the tournament. Payouts always in USDNMR and burns first apply to NMR
  * When a participant wishes to withdraw funds, the USDNMR could either be transfered directly and sold on the open market, or unwrapped and, at the time of withdrawal the user walks away with USDC.



This should maintain price and liquidity for NMR on open exchanges because anyone willing to get into the tournament or increase their stake would need to buy NMR in order to stake.

The potential loss to Numerai is that they would have to swap NMR from the treasury into USDNMR, but realistically, if they are distributing NMR from the treasury then they have already lost the potential value of that NMR if they wanted to just sell it.

Over a very long period of time, eventually the NMR cache would slowly change over to USDNMR.

Also, by using a chain such as Solana, or Fantom to fascilitate the special USDNMR token, the transactions could happen much faster and and at less gas price to the current NMR Eth contract.

I’m no expert in this area, but it does seem that a slow transition to stable coin would add some much needed confidence in the program overall. The trick is really doing this without the bottom falling out of NMR, becuase Numerai needs this value regarding their large stash of NMR. Not to mention we the participants not wanting our investment going to zero.

I’m sure I’m missing something, but I’d like to hear from those in the know regarding blockchain tech if something like this is possible.
