---
title: "GAS fees - are staking contracts really necessary?"
category: Feedback
url: https://forum.numer.ai/t/gas-fees-are-staking-contracts-really-necessary/2788
created_at: 2021-04-10T12:57:30.220000+00:00
last_posted_at: 2021-04-10T17:12:03.679000+00:00
posts_count: 13
views: 1604
tags: []
---

# GAS fees - are staking contracts really necessary?

---

### Post #1 — **minou** | 2021-04-10 12:57 UTC

This may come from a lack of understanding on my part so apologies for that, however in relation to the fees Numerai are paying for staking changes, couldn’t this largely be solved by not using contracts for staking in the first place? Given that numerai operates the wallet, if a member has a balance of say 100 NMR and an active stake of 10, can’t the maximum withdrawal simply be limited to 90? A stake increase would simply tie up more of the available balance, and need not involve the blockchain at all. When a loss is incurred, lose the funds in a cost effective way, or optionally allow it to be donated to a nominated charity. This could even be done lazily so the change in NMR doesn’t actually occur until some later point in time, when due to gains, reduction of NMR might no longer be required. So essentially, manipulate the amount of NMR the user has access to, while managing it more optimally behind the scenes.

---

### Post #2 — **ml_is_lyf** | 2021-04-10 13:23 UTC

For one I think the destruction of currency is in our best interests. If the supply of the currency is decreasing (which is caused by NMR being burnt in the tournament), and demand is constant or increasing, then prices will rise. The price rising is beneficial for us as it means our stakes are worth more.

I like the idea of donating our burns to charity. But if our burnt NMR is donated to charity, then presumably the charity will sell it immediately for fiat money. So that means when we’re burning a lot of NMR, a lot of NMR will also be being sold in exchanges. So the performance of the currency will have a positive correlation with the performance of the tournament, this is going to increase tournament participant’s risk, which I don’t think is desirable. Also even if the charity isn’t given the NMR immediately, when they are given the NMR the market will be flooded with supply which will devalue the currency.

With regard to whether we need contracts, I think that is an interesting question, as it is kind of weird that Numerai is the oracle for the contract and also the counterparty we make the contract with. So maybe in theory we don’t need contracts. But also I think contracts are nice as (I’m pretty sure) they add an extra layer of security, as I think if it wasn’t tied up in contracts, it’d be easier for hackers to steal our NMR.

---

### Post #3 — **minou** | 2021-04-10 14:02 UTC _(reply to #2)_

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/m/e56c9b/48.png) ml_is_lyf:

> it’d be easier for hackers to steal our NMR.

Thanks. I did consider this, however if Numerai has a security breach such that private keys could be accessed and backend code changed without their knowledge (hopefully there are tools in place to at least detect and report unauthorised code changes in real time, but ideally block changed code from execution too), then I suspect that funds tied in contracts would be just as much at risk as a basic wallet. If NMR increases as a result of burns, as would be expected, then that’s useful, though it almost feels like cheating.

---

### Post #4 — **ml_is_lyf** | 2021-04-10 14:37 UTC _(reply to #3)_

Yeah, good point. I guess it’s a side note, but interesting that there hasn’t been much discussion of cybersecurity. Seems like we could be a big target given the stake pool is now worth $20 million.

Yeah, does feel like cheating a bit. One of the advantages of building an economic system around the tournament ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=9)

---

### Post #5 — **gammarat** | 2021-04-10 14:46 UTC _(reply to #2)_

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/m/e56c9b/48.png) ml_is_lyf:

> If the supply of the currency is decreasing (which is caused by NMR being burnt in the tournament), and demand is constant or increasing, then prices will rise.

The underlying question though is “Why should demand remain constant or increase?”. NMR, after all, isn’t much use for anything other than the Tournament and Signals (has anyone ever bought anything other than crypto with it?), and it’s expensive to convert to a currency that is.

---

### Post #6 — **ml_is_lyf** | 2021-04-10 14:54 UTC _(reply to #5)_

Tell that to Grayscale ![:slight_smile:](https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=13)

![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/5/5c779d5dfce0a9e89c4f63417c1340b1b137d256.png) [Crypto Briefing – 26 Feb 21](<https://cryptobriefing.com/grayscale-opens-doors-to-altcoins-exploring-more-than-23-new-tokens/> "04:32PM - 26 February 2021")

![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/b7489c59b93e905f8ef6d9518fc6785d7e7a091a_2_690x362.png)

### [Grayscale Opens Doors to Altcoins, Exploring More Than 23 New Tokens](<https://cryptobriefing.com/grayscale-opens-doors-to-altcoins-exploring-more-than-23-new-tokens/>)

Grayscale is exploring new investment offerings with 23 cryptocurrencies which include DeFi tokens, Ethereum-killers, and other altcoins.

Est. reading time: 2 minutes

Also as the success of the tournament grows more people will want to participate. And as long term participants get older and wealthier they’ll have more money to put in the tournament.

---

### Post #7 — **minou** | 2021-04-10 14:54 UTC _(reply to #5)_

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/forum.numer.ai/gammarat/48/3281_2.png) gammarat:

> NMR, after all, isn’t much use for anything other than the Tournament and Signals

I have wondered if the value of NMR could fall to zero if a more favourable competition came along elsewhere.

---

### Post #8 — **ml_is_lyf** | 2021-04-10 15:02 UTC _(reply to #7)_

Surely you could say the same thing about the labour market right, there are lots of firm competing for the same talent pool. But firms don’t collapse because they can’t find talent. The data science competition labour market would have some equilibrium that competitions would approach.

---

### Post #9 — **minou** | 2021-04-10 15:14 UTC _(reply to #8)_

It’ll be interesting to see how things progress and how any viable competitors make an impact. Numerai sets a high bar already in this space with a great team and community, so I’m not really concerned about a zero valuation for NMR any time soon.

---

### Post #10 — **gammarat** | 2021-04-10 15:31 UTC _(reply to #7)_

I would actually pay a few bucks a month for a competition that simply provided clean data the way Numerai does, because the problem they present is interesting; what I learn from doing this I could apply to other problems for which people used to pay me real money for (I’ve been retired for a decade, and don’t need the money now. Just the intellectual stimulation ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=9) ). For example, I used to work in developing algorithms for evasive target tracking; but because the real data was classified and hence couldn’t be played with in my spare time, I used the FOREX market as a playground. Similarly, learning about Bayesian classification back in the 90’s gave me a useful framework for conceptualizing art.

---

### Post #11 — **mindyoself** | 2021-04-10 16:41 UTC

This is really interesting. I did not know that the burn was providing support for charity. If that’s the case then I don’t mind if my staked tokens are burnt. Numerai just got addition props in my eyes. Mind further blown! If the burnt tokens were going towards charitable courses [@richai](</u/richai>) an idea could be for the community to decide which charitable causes the burnt tokens went to? Is this something to consider or already happening? If not then it will be cool if every week we could vote or nominate which charity a percentage of the burnt tokens went to. That will be dope.

---

### Post #12 — **minou** | 2021-04-10 17:06 UTC _(reply to #11)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/mindyoself/48/795_2.png) mindyoself:

> I did not know that the burn was providing support for charity.

Sorry to mislead; it isn’t, but it was a suggestion related to how to avoid GAS fees.

---

### Post #13 — **mindyoself** | 2021-04-10 17:12 UTC _(reply to #12)_

I hear you. Surely though that must be something that the ethereum foundation should be considering if an ERC-type token is giving a percentage of token earnings to charity, that would be something worth considering in my eyes.
