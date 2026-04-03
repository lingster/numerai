---
title: "Bull Case / Bear Case"
category: Numeraire
url: https://forum.numer.ai/t/bull-case-bear-case/4219
created_at: 2021-09-29T20:50:17.206000+00:00
last_posted_at: 2021-10-30T19:26:06.241000+00:00
posts_count: 36
views: 4133
tags: []
---

# Bull Case / Bear Case

---

### Post #1 — **nmr0** | 2021-09-29 20:50 UTC

Numerai hands out ~1m NMR per year, with a market value of $40mm USD.

They’ve raised maybe $20-30mm USD of capital in the fund itself, and have never exceeded $100m in gross positions (otherwise they’d be filing a 13F). This throws off maybe a million per year in fees, if we’re being generous.

Once the treasury of printed NMR runs out, they’re generating about 1/40th of what’s necessary to even maintain the current collapsing payout ratio, if somehow their entire team works for free.

* * *

The only case where this doesn’t go to zero are effectively:

  * people don’t care that payouts shrink 10x notional and maybe 100x on a ROR basis due to increasing NMR staked and no earnings with which to pay anyone
  * they suddenly, after five years of no success, get good at fundraising. Note that equity market neutral funds have been out of favor for a decade, most launch with more capital than Numerai has raised, and this will never be palatable to tax-free investors like pensions and endowments that are the actual capital base in the lowish-return EMN space.
  * they all renounce their US citizenship and start allowing stablecoin investments that can be used as an actual source of capital for trading



Short of some miraculous billion dollar capital raise, there’s nothing here to pay the bills, the team, and much less the model stakers. The current numerai valuation is supported only by new entrants enticed by potential triple digit returns that come from effectively printed money. As the payout ratio collapses, and the treasury runs out, it will be clear that the whole thing was only viable under the assumption they could print money or earn (and choose to share) tens of millions per year, while running a tiny hedge fund that never learned to capital raise.

---

### Post #2 — **liz** | 2021-09-29 21:01 UTC

this is so ham-fisted that it’s funny. to try to comment on what I think is the only piece worth anything, “people don’t care that payouts shrink 10x notional and maybe 100x on a ROR basis due to increasing NMR staked and no earnings with which to pay anyone” illuminates what I think is a real likelihood that folks don’t talk about much here; when treasury runs out, payouts are gonna drop, in my opinion.

---

### Post #3 — **nmr0** | 2021-09-29 21:27 UTC

Of course the bull case:

Numerai enters into a swap agreement where exchanges / dex let them trade cryptos, collaterized by staked NMR, and the whole thing becomes a mid-frequency crypto trading platform that is self-funding.

They figure out how to attract new token buyers who can effectively bet on other people’s models, thus enlarging the supply of buyers 10-1000x beyond aficionados of neural networks and gradient boosted trees. The more the price is bid up, the greater their trading lines and daily / weekly payout.

They wire a few mil nmr to ex SEC/CFTC commissioners and agree to stay away from equities and by some magic are able to avoid regulatory scrutiny.

If this happened, probably worth a few billion at least, as it becomes basically a risk mgmt and data overlay for crypto trading, and of interest to every dollar out there looking at dex, staking, etc. Feel free to wink twice if this is the case ![:wink:](http://forum.numer.ai/images/emoji/twitter/wink.png?v=9)

---

### Post #4 — **rigrog** | 2021-09-29 21:57 UTC

To raise more capital, they need to get better performance from the metamodel. Great metamodel ==> highly profitable trading ==> capital comes chasing _them_.

So far, the metamodel has been held back by the target-poor legacy tournament. Only about 27% of the rows have a value in the target columns, and _none_ of those are very close in time to the live era.

The super-massive tourney is a much more “target rich environment”, providing a target value for about 70% of the rows. The time gap, between the last val era and the live era, is still too long but shorter. So I anticipate a significant performance boost for most of our models, and thus for the metamodel. Perhaps enough to start attracting the billions needed, for long term viability.

Finally, in a month or three, R. Craib says that ALL non-live rows will have target values provided. They could and should have done this, at least for 1/4 to 1/2 of the test eras, as soon as they introduced staking (since they’re no longer using target performance to decide how much a model influences the metamodel).

When we finally go from the target rich environment, to the target saturated environment: that’s when I expect the _amazing_ performance to start. To the moon, baby!

---

### Post #5 — **kenfus** | 2021-09-29 22:23 UTC

I think you are somewhat right. However, NMR is a bit overvalued because of the crazy Cryptocurrency market. It is one of the very few coins which actually has real demand.

There are other ways Numerai could reduce the payout and thus save money. Should a very average Model, which is extremely highly staked, really be paid that much? Is there another investment, which has no diminishing returns? Of course, I’m biased because I will never stake more than $20k, so I would only profit from that. Currently, NMR is pretty free for Numerai, so it’s OK. However, will they really pay 5-8k a Week for a highly staked model which is worse than Integration Test?

---

### Post #6 — **objectscience** | 2021-09-29 23:58 UTC

My favorite scenario: Numerai ends up managing billions of investor’s funds and the rest figures itself out…

---

### Post #7 — **sirbradflies** | 2021-09-30 04:35 UTC _(reply to #5)_

Totally agree with the point about the Integration Test. I believe at some point the switch to MMC only is inevitable for the sustainability of the fund.

---

### Post #8 — **lackofintelligence** | 2021-09-30 05:39 UTC

Despite some negative comments, I think this is a great post because it gets us thinking about the number one problem that staking data scientists and Numer.ai itself must face. Numer.ai is in a race to become successful and well-funded before its NMR treasury runs out and before the price of NMR is forced to zero.

All present strategies to boost NMR price are backfiring. In particular limiting payouts while trying to

  1. increase the stake by attracting more staking data scientists,
  2. increase the amount of NMR staked by attracting outside stakers on models



are completely nonsensical retrogressive strategies that are only accelerating the rate that the Numer.ai treasury is being exhausted and is also accelerating the devaluation of the tournament and NMR itself by reducing ROI.

What solutions are to this ultimate conundrum? I think the most popular solution so far to insert value into the NMR ecosystem has been NMR buybacks. Of course, if Numer.ai does not have enough USD in its treasury to make regular buybacks then that is not a useful way to prop up the NMR token/ecosystem.

A few years ago when I first heard about Numer.ai and made my first submissions, I envisioned something a little different than what is actually happening. So I am going to share that vision, because it seemed so obvious to me back then.

  1. From its treasury of NMR, Numer.ai uses NMR to buy dollars in proportion to the amount staked.
  2. Numer.ai actually uses those USD to short and long stocks in the Hedge Fund.
  3. Hedge Fund profits are used to buy back NMR each week in proportion to the gain that is to be directed to those who wish to receive NMR payouts while USD payouts are sent to those in proportion to the amount that they wish to receive in USD.



Voila, real value has been injected into the NMR ecosystem at no cost to Numer.ai. It cannot be underestimated the effect this would have to decouple NMR from the rest of cryptocurrency purgatory.

By continuing to stake in NMR that activity can be logically separated from the Hedge Fund and in the meantime the value of NMR maintained. Furthermore to maintain the treasury Numer.ai can, as necessary, set limits either one way or the other how much of payouts can be made in USD or NMR (although hopefully that is not necessary). Note, again, there is logically no flow of NMR from staking data scientists to the Hedge Fund. But only flow of either NMR losses (burns actually go nowhere) or USD/NMR gains to stakers made from the Numer.ai treasury. The fact that the Hedge Fund uses some of its profits to buy NMR, or pays out some of our tournament gains in USD, well, those seem like technicalities that cannot break SEC regulations. This modus agendi also solves the problem of the success of Numer.ai. Having a way to pay data scientists that is guaranteed not to collapse to zero means that Numer.ai could last indefinitely while having a source of funds for the Hedge Fund that in my estimation is presently equal to or has already eclipsed the amount from outside investors. In that case it would make complete sense to engage in the first two activities listed above.

From what I know about the Hedge Fund, I guess my initial vision about the way Numer.ai could do things is not the way it is presently doing things. But I ask you now, why not?

---

### Post #9 — **zbieram_na_piwo** | 2021-09-30 05:50 UTC

IMO the most probable is the first option with little twist: there will be less payouts but more concentrated around participants that provides true value for the Fund. This will need some changes to payout structure and performance measure, but overally the shape of the tournament won’t change much.

---

### Post #10 — **wigglemuse** | 2021-09-30 15:07 UTC

![](http://forum.numer.ai/user_avatar/forum.numer.ai/lackofintelligence/48/774_2.png) lackofintelligence:

> All present strategies to boost NMR price are backfiring. In particular limiting payouts while trying to
> 
>   1. increase the stake by attracting more staking data scientists,
>   2. increase the amount of NMR staked by attracting outside stakers on models
> 

> 
> are completely nonsensical retrogressive strategies that are only accelerating the rate that the Numer.ai treasury is being exhausted and is also accelerating the devaluation of the tournament and NMR itself by reducing ROI.

The staking cap keeps the rate of the treasury depletion more or less constant – there is no acceleration (anymore) except by additional commitments from Numerai (like adding Signals with a whole separate staking pool accelerated it compared to only having the classic tournament). I don’t think trying to attract more data scientists is a strategy to “boost NMR price” – it is a strategy to attract more data scientists. And attracting outside stakers (which isn’t even a “Numerai” activity, but a user one) is also neither about NMR price – it is about users wanting to make more on their models without risking more themselves by capitalizing on the apparent demand from non-data scientists to get involved (i.e. people keep showing up and asking “how can I bet on the best models?” and now we have an option along those lines.) It is also a way of concentrating more stakes on the better models (which because of the staking cap puts a bigger squeeze on lesser models and maybe newbies – this could be good or bad for the metamodel.)

But anyway, Numerai is not going to engage in any activity for the main purpose of boosting NMR price as that could get them into trouble with security laws. And why would they anyway? It is fine for Numerai if the price is $5 or it is $50. Users complain both that it is too high and too low, some want it to go up and some want it to go down depending on their own situation.

![](http://forum.numer.ai/user_avatar/forum.numer.ai/lackofintelligence/48/774_2.png) lackofintelligence:

> A few years ago when I first heard about Numer.ai and made my first submissions, I envisioned something a little different than what is actually happening. So I am going to share that vision, because it seemed so obvious to me back then.
> 
>   1. From its treasury of NMR, Numer.ai uses NMR to buy dollars in proportion to the amount staked.
>   2. Numer.ai actually uses those USD to short and long stocks in the Hedge Fund.
>   3. Hedge Fund profits are used to buy back NMR each week in proportion to the gain that is to be directed to those who wish to receive NMR payouts while USD payouts are sent to those in proportion to the amount that they wish to receive in USD.
> 


Because that effectively puts us in the hedge fund, and that’s illegal. If it wasn’t an actual hedge fund, but a group investment activity (or crypto fund) then it could be something like that (and I think other groups are trying this?). But as an actual US-regulated fund, we can’t be in it unless we are actually invested in it as accredited investors! We can’t effectively be in it “but not really” either! (Not with Numerai paying us anyway – again users could try to make their own metamodel and their own trades though.) They simply aren’t going to expose themselves to the risk of getting shut down by trying to skirt regulations.

The data scientist-NMR ecosystem exists to solve problems with crowdsourcing. Staking is only part of it to separate the wheat from the chaff (i.e. “which predictions can be more trusted?”), NOT as an investment into the profit-making activity of the solved problem. Ideally (from Numerai’s perspective) it would be nice if there was no staking at all – they’d simply pay for the best predictions. But since that would involve vetting, track records, experience, education, etc – i.e. the traditional way to hire quants – and this is supposed to be an experiment in anybody who wants to being able to participate, they need to be able to know which predictions are more likely to be better than other predictions (and by how much) from the thousands that are submitted. That’s what staking is for. We get hung up on the idea of profiting “from the hedge fund” because it is a hedge fund (which doesn’t even make money yet!) But we could be doing medical research with the same system paid for by government grants and not some capitalistic enterprise and then maybe people wouldn’t be so obsessed about the other side of the wall.

---

### Post #11 — **nmr0** | 2021-09-30 20:11 UTC

Many great points here.

In most data science tournaments, payouts are winners-take-all. There’s a reasonable argument that depleting the treasury to pay weaker models for a sub-integration-test correlation shouldn’t be occuring at all. This change alone would push payouts back to those who add the most value and away from whale accounts that drain the payout ratios without adding any signal.

The plus of doing things things this way is numerai becomes not a “pass through pseudo investment product” (which it basically is when it indexes your payouts to correlation, aka trading returns) but just a data science tournament again, once payouts are mostly from model contribution and overall ranking.

Shifting back to a tournament also makes it much more viable to allow betting on others’ models, as it looks much less like investment advisory and more like a straightforward prediction competition on the MMC/rank of other models.

Ultimately many people have hit on the key idea, which is numerai only works (as an investment focused token) if they find a way to get trading leverage from the staked coins.

* * *

One other bull case remains taking over the machine learning competition space more generally. If their data encryption techniques are really that good, and they’ve built this community, why shouldn’t major companies be allocating six and seven figure budgets to pay for the best predictions–all done via API, staking, and distributed infererence, rather than the traditional single-deadline, often leaky, still have to deploy it style Kaggle competition.

---

### Post #12 — **lackofintelligence** | 2021-09-30 23:21 UTC _(reply to #10)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/wigglemuse/48/3094_2.png) wigglemuse:

> The staking cap keeps the rate of the treasury depletion more or less constant

Yup, I just double checked the formula. You are correct.

---

### Post #13 — **lackofintelligence** | 2021-09-30 23:28 UTC _(reply to #10)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/wigglemuse/48/3094_2.png) wigglemuse:

> Because that effectively puts us in the hedge fund, and that’s illegal.

I don’t think you read my suggestion very carefully. They would only buy and sell stocks using funds that they already have. They can generate those funds by selling NMR. There is no transfer of funds from us to them. Our NMR are always held as stake in their staking wallet and are treated as they are usually treated modulo the other suggestions that I have made. I repeat, they never touch our NMR.

---

### Post #14 — **lackofintelligence** | 2021-09-30 23:37 UTC _(reply to #10)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/wigglemuse/48/3094_2.png) wigglemuse:

> We can’t effectively be in it “but not really” either!

Our rewards are already correlated to how much the Hedge Fund actually gains and loses by our fraction of metamodel control. There are some execution factors and fees involved too but otherwise our stake weighted submissions are intimately connected to Hedge Fund returns.

---

### Post #15 — **wigglemuse** | 2021-09-30 23:49 UTC _(reply to #12)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/lackofintelligence/48/774_2.png) lackofintelligence:

> Yup, I just double checked the formula. You are correct.

To be more precise, I should have said the staking cap in combination with the payout factor.

![](http://forum.numer.ai/user_avatar/forum.numer.ai/lackofintelligence/48/774_2.png) lackofintelligence:

> I don’t think you read my suggestion very carefully. They would only buy and sell stocks using funds that they already have. They can generate those funds by selling NMR. There is no transfer of funds from us to them. Our NMR are always held as stake in their staking wallet and are treated as they are usually treated modulo the other suggestions that I have made. I repeat, they never touch our NMR.

I did, which is why in my careful reply I said, “We can’t effectively be in it ‘but not really’ either!” Playing a cute game of loopholes “so you aren’t really doing what you are doing” would be tempting fate and possibly the ire of the regulators. They aren’t going to play those games. (I very much doubt, of course I’m just speculating myself.) Our compensation will of course by necessity always be at least loosely tied to the hedge fund size/performance (just as it would if we were straight employees), but above and beyond that anything with the slightest hint of “investing in the hedge fund without investing in the hedge fund” (either by staking or just by holding NMR) is not going to fly.

---

### Post #16 — **lackofintelligence** | 2021-10-01 02:53 UTC _(reply to #15)_

I think you are representing a rather popular opinion about the present relationship between our stakes and the Hedge Fund. What I am saying is that this relationship is already much tighter than that opinion would admit.

The other aspect of this discussion, the actual purpose, is not solved by arguing the “standard response”. How would you propose to solve the problem of payouts and NMR price going to zero when the treasury runs out? Presumably at that point Numer.ai would have to use Hedge Fund profits to buy NMR to pay us. That implicit relationship has already been noted by esteemed CoE members speculating on the price of NMR. If not that, than what? And if that, then I would argue the only difference between that and my proposal is that it provides a modus agendi to generate funds for those payouts now instead of later. All of us would like to know what the answer to this question is, because if there is no answer then it implies that the lifespan of the tournament is limited.

---

### Post #17 — **rigrog** | 2021-10-01 14:49 UTC _(reply to #16)_

Just as Numerai minted Numeraire out of thin air, they could mint “Neweraire” (NWR) the same way.

Then they just carry on as if 1 NMR = 1 NWR, making payouts in only NWR (since that’s all they have), and accepting either NMR or NWR as stakes.

---

### Post #18 — **kenfus** | 2021-10-03 20:45 UTC _(reply to #17)_

But 1 NWR != NMR in value. I hope for you that you sold your NMR when the news for NWR comes out because it will crash like Bitconnect

---

### Post #19 — **mic** | 2021-10-03 22:08 UTC _(reply to #18)_

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/forum.numer.ai/kenfus/48/3397_2.png) kenfus:

> But 1 NWR != NMR in value

Yes it would, both 0.

Not going to happen.

---

### Post #20 — **rigrog** | 2021-10-03 22:46 UTC

Both NMR and NWR (if and when they happen) are made out of exactly the same thin air. The only value of either, is also exactly the same: the opportunity to turn some of them into more of them via staking. So I don’t see a case for valuing one any differently from the other.

If Numerai were to try it a third time, there might not be enough thin air left.

---

### Post #21 — **lackofintelligence** | 2021-10-04 02:09 UTC _(reply to #4)_

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/r/dec6dc/48.png) rigrog:

> To raise more capital, they need to get better performance from the metamodel. Great metamodel ==> highly profitable trading ==> capital comes chasing _them_.

Let’s say that we figure out how to capitalize on this new super saturated-target data set within the next year and the logical steps you have outlined follow shortly, i.e., Numerai is successful. That still does not explain how value will be injected into the NMR token ecosystem or in the long run how Numerai’s NMR treasury will be replenished.

---

### Post #22 — **richai** | 2021-10-04 02:28 UTC

Thanks for this thread [@nmr0](</u/nmr0>). I imagine many of these points come up around crypto VC board rooms when they contemplate NMR. When in doubt, remember we are always trying to do [the master plan](<https://medium.com/numerai/numerais-master-plan-1a00f133dba9>) and we are trying to mostly do it in order. Only a year ago did we start on part 2/4.

Numerai’s Master Plan

  1. Monopolize intelligence (I think we’re at the second largest data science community and highest paying in the world)
  2. Monopolize data (growing Numerai Signals from $0 to $3m in stakes in a year, and just recently 10xing Numerai’s data)
  3. Monopolize money (???)
  4. Decentralize the monopoly (???)



For sure monopolizing money is both performance and track record length dependent. It is also investor education dependent. The biggest investors/allocators in the world knew very little about machine learning and crypto in 2016, and now they know a little more but still not a lot. And very little know about both simultaneously (which they need to get their heads around Numerai). And with booms in every risk - being neutral to risk is a weird pitch but can also be a weird flex someday when those risks come off. As I mentioned on Twitter we’re going to start sharing some performance stuff soon which can help you think about the bull / bear case for Numerai’s hedge fund but not NMR which is a staking token not an investment product.

Some of your ideas around trading crypto seem to be good especially around part 4 of the master plan. One scenario where stocks are allowed (legally) to be traded on the blockchain (and we’re allowed to trade them) really makes part 4 (decentralize the monopoly) very very interesting.

---

### Post #23 — **rigrog** | 2021-10-04 17:16 UTC _(reply to #21)_

If Numerai’s hedge fund gets billions invested in it, then Numerai will be collecting comissions (at some normal rate) on those billions. That money can buy the NMR they’ll need, to keep paying us after the treasury runs out.

Or, as I suggested in another post on this thread, the could just mint “Neweraire” (NWR) out of the same thin air from which they minted NMR, and pay us those. Who knows, if the market would support NWR.

---

### Post #24 — **lackofintelligence** | 2021-10-05 16:07 UTC _(reply to #23)_

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/r/dec6dc/48.png) rigrog:

> If Numerai’s hedge fund gets billions invested in it, then Numerai will be collecting comissions (at some normal rate) on those billions. That money can buy the NMR they’ll need, to keep paying us after the treasury runs out.

[@richai](</u/richai>), will Numerai buy NMR using profits from the Hedge Fund?

---

### Post #25 — **eleven_sigma** | 2021-10-05 17:01 UTC _(reply to #24)_

This isn’t the only way. Numerai could use the predictions and signals, stacking them and selling signals to other players in the stock market, These sales would be in NMR so other players will need to buy NMR in the market and Numerai will get more NMR to pay us. Two objectives in one shot.

---

### Post #27 — **richai** | 2021-10-06 18:11 UTC

Some news on relevant news on fundraising for the fund:

<https://medium.com/numerai/numerai-outperforms-market-neutral-hedge-funds-by-29-raises-up-to-150m-9df9a0ce642>

---

### Post #28 — **mic** | 2021-10-07 04:40 UTC _(reply to #27)_

Wow! Well done Richard and all at Numerai!

---

### Post #29 — **lackofintelligence** | 2021-10-07 05:35 UTC _(reply to #25)_

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/e/8797f3/48.png) eleven_sigma:

> Numerai could use the predictions and signals, stacking them and selling signals to other players in the stock market, These sales would be in NMR so other players will need to buy NMR in the market and Numerai will get more NMR to pay us.

I don’t think so. While the [article that Richard just posted](<https://medium.com/numerai/numerai-outperforms-market-neutral-hedge-funds-by-29-raises-up-to-150m-9df9a0ce642>) does describe the possibility of a long strategy, I don’t think that is something that Numerai wants to sell. _Any_ strategy will stop working if too many Hedge Funds are using it, in the meantime, the corresponding symmetrical short strategy could be inferred by revealing the long strategy, since we already know which universe of stocks the predictions are in. Remember, we submit an _ordering_ of stocks – a stock strategy – it makes no sense to talk about individual stock price predictions in that context.

In regards to my other question in response to [@rigrog](</u/rigrog>):

![](http://forum.numer.ai/user_avatar/forum.numer.ai/lackofintelligence/48/774_2.png) lackofintelligence:

> ![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/r/dec6dc/48.png) rigrog:
>
>> If Numerai’s hedge fund gets billions invested in it, then Numerai will be collecting comissions (at some normal rate) on those billions. That money can buy the NMR they’ll need, to keep paying us after the treasury runs out.
> 
> [@richai](</u/richai>), will Numerai buy NMR using profits from the Hedge Fund?

I think Richard’s _answers_ are very clear:

  1. > _**NMR is a volatile cryptocurrency which moves up an down with other cryptocurrencies like Dogecoin based on supply and demand.**_

  2. > 


The first answer is at the end of the same article just referenced. I think this is a very clear statement that Numerai intends to let the crytocurrency market dictate the price of Numeraire only. The second answer is just the lack of response to my exceedingly clear question. It is a resounding _**NO**_.

---

### Post #30 — **sneaky** | 2021-10-07 09:22 UTC _(reply to #29)_

Just because they state that it is not the case now, it does not mean it cannot be done in the future.  
I cannot comprehend where you take your certainty. For example, they were not publishing any fund performance statistics until now. Everything has its time.

I think doubt has its place; however, from your text I feel that you have no doubt, you are certain. IMO being certain means being wrong.

---

### Post #31 — **lackofintelligence** | 2021-10-09 06:01 UTC _(reply to #30)_

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/s/4bbf92/48.png) sneaky:

> Just because they state that it is not the case now, it does not mean it cannot be done in the future.

Absolutely, and if they did so I would support it 100%.

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/s/4bbf92/48.png) sneaky:

> I cannot comprehend where you take your certainty.

Um, what should be the source of my uncertainty? If we were talking about probing inanimate objects then, clearly, I would have a good source of uncertainty, say derived from the statistics of some number of variable measurements. But we are not! The question is directed to actual people who _without doubt_ are capable enough to answer the question.

Wait, are you saying that I should infer that they are actually themselves uncertain about their future course of action? Perhaps they are taking some wait-and-see-what-happens approach? Well, in that case you might be right. But if they don’t want to project that uncertainty, why should I project it for them? Unfortunately, my abilities to telepathically grok that uncertainty are less than negligible. But may I infer from your statements, that despite their present negation, you expect that they will change their mind in the future and that they don’t want to reveal that possibiity now in case it turns out that they can’t do it and the whole enterprise fails when the NMR in the treasury dries up?

---

### Post #33 — **neosbrother** | 2021-10-20 14:12 UTC

> I think Richard’s _answers_ are very clear:  
>  _**NMR is a volatile cryptocurrency which moves up an down with other cryptocurrencies like Dogecoin based on supply and demand.**_

That really doesn’t seem like a clear answer, and I’m not sure how you read his comment to mean they won’t purchase NMR to maintain payouts once the treasury is exhausted.

Without payouts, the tournament falls apart and presumably the hedge fund would fail as well. Minting some new coin would screw over all the existing tournament participants and would likely severely damage their reputation and performance moving forward. The only other option I can think of is to purchase NMR on the market to keep the treasury full enough to maintain payouts.

When this happens, they could either reduce or increase payouts, depending entirely on how much cash they allocate to NMR purchases and the NMR price. Based on the current payout rate and NMR price, it would require roughly $40M a year. With the hedge fund’s 2/20 fee structure and current performance, they make about 4% of AUM in fees per year. This means they need roughly $1B AUM to maintain current payouts if they allocate 100% of income to this. Currently they have ~$50M AUM, meaning they need a 20-fold increase in AUM in the next 5 years. I know some are pessimistic about this, but given the size of the hedge fund industry and the need for a track record, which has been/is being established, I don’t think it’s unreasonable to think they could pull it off.

Edit: Of course, they need money to keep the lights on and pay investors who provided seed money for the hedge fund. So you can probably double the numbers I gave and you won’t be off by more than a magnitude of 2 (assuming they use at least 25% of revenue to pay for the tournament).

---

### Post #34 — **of_s** | 2021-10-20 16:20 UTC _(reply to #33)_

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/n/dec6dc/48.png) neosbrother:

> Without payouts, the tournament falls apart and presumably the hedge fund would fail as well. Minting some new coin would screw over all the existing tournament participants and would likely severely damage their reputation and performance moving forward.

I don’t think if the tournament falls apart the fund is materially impaired.

The meta-model correlations are absurdly high for most participants and the meta-model would ultimately just consist of whatever the team is able to think up and incorporate (which would look a lot like the meta-model today) if the tournament ended tomorrow.

---

### Post #35 — **neosbrother** | 2021-10-20 17:33 UTC _(reply to #34)_

That’s an interesting idea. I’m not sure if it’s really accurate though. It all depends on how much value is derived by the diversity of model predictions being staked upon, and only those inside Numerai can determine that.

---

### Post #37 — **xiafanaina** | 2021-10-30 08:50 UTC _(reply to #33)_

It is said that numerai is trading with 5.5 leverage. So I assume numerai only need 200M instead of 1B to payout NMR.

It was also said by Richard monthes ago that numerai need 500M to support current NMR, when the payout rate was around 0.7 and NMR was about 50. This also confirm the point.

---

### Post #38 — **neosbrother** | 2021-10-30 12:40 UTC _(reply to #37)_

They are paid for AUM, which doesn’t change based on how much leverage they use.

---

### Post #39 — **xiafanaina** | 2021-10-30 19:26 UTC _(reply to #38)_

Yes. You are right. I just confirm with Richard. The current 20% 2-year return contains leverage already. So it still needs 1B to payout NMR.
