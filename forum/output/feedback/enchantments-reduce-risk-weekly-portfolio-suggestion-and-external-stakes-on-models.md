---
title: "[Enchantments] Reduce risk - weekly portfolio suggestion and external stakes on models"
category: Feedback
url: https://forum.numer.ai/t/enchantments-reduce-risk-weekly-portfolio-suggestion-and-external-stakes-on-models/3893
created_at: 2021-08-02T09:03:43.424000+00:00
last_posted_at: 2021-08-04T17:57:03.170000+00:00
posts_count: 6
views: 1006
tags: []
---

# [Enchantments] Reduce risk - weekly portfolio suggestion and external stakes on models

---

### Post #1 — **pavelk** | 2021-08-02 09:03 UTC

Numerai competition is great fun. The possibility to make money while playing is really appealing. Rules and workflow are straightforward.  
However, there is one significant “but”. Numeraire NMR price is too volatile. It follows the trends of BTC. One day is up, the next day is down. You can win in the tournament, but lose money in reality.  
The associated risk is a blocker for bigger stakes. Low stake reduces the level of engagement to a “just for fun” level.  
I would like to invest more time and resources and make some real money.  
I have two ideas on how to improve the tournament experience. Hope they will make sense for the community and the company.

  1. **Trading advice based on model prediction**.  
When a submission is made the website will generate trading advice for the next week. The advice will be based only on the current model’s predictions. It will contain one or a few groups of stock IDs and buy/stop/sell price. Something like a portfolio for the week. For example:  
Portfolio suggestion 1 (risk 5%, gain: 20%):  
10% - GOOG - buy: 2600, sell: 2800, stop: 2550  
70% - LOGI - buy: 106, sell: 120, stop: 104  
20% - QRON - buy: 450, sell: 1000, stop: 420



With weekly portfolio suggestions, I will be able to stake in USD via Robinhood or Interactive brokers, or another platform.  
This will be a great incentive for me to continue improving my models and invest time and money.

  2. **Other people staking on a model in NMR**.  
Any person will be able to stake on any model in the tournament. If you stake on a model, the model owner decides what percentage of profits to share. This will be a model-level configuration. I could decide to give 70% of the profits from an external stake and keep 30% for me.  
Someone who is not afraid to invest in NMR can stake on my model. He will get 70% of the profits and I will keep 30% for me.  
This will reduce the risk for data scientists and will open the gates for investors without machine learning skills.



I hope the other participants will like the proposal.  
Any feedback will be great.  
Thank you!

---

### Post #2 — **valiunia** | 2021-08-03 11:39 UTC

while the problem you describe is the actual big problem, I dont think the solutions you suggest will work.

  1. If this is done, then you just profit from numerai data and they cant really make a profit, because they do not know if your predictions are good or not. They have stated before that without staking numerai did not work at all (Richard said that in Lex Fridman podcast). So basically 1. is not compatible with making profit.

  2. If other people stake on your model, then they go just with a statistics of the past rounds or with pure gamble - meta model here wont be good. But even if you restrict this to only models that have a good history - then there is still no guarantee that you wont mess up you model for the next round by introducing a bug, etc. So I dont really see how 2 would work either.

  3. Also if you could stake on other models, everyone would stake on top 10 models and meta model would be biased to those models and it would probably be worse than current meta model.




I think the only solution that is viable, is the one that doesnt worsen meta model. I cannot think of a way to achieve that without current staking approach.

The problem is really with the crypto and not with how numerai uses it for staking. I think staking is great idea but we just need to figure out how to get rid of volatility. It is not possible to use fiat, because it cannot be destroyed, and someone stands to gain if users make bad model. I am not expert in crypto, but maybe it would be possible to have smart contracts in a currency that is pegged to fiat? Thats probably nonsense?

It was suggested elsewhere in the forum how to hedge against volatility (you need to do complex trades with multiple legs so that whatever happens your net position is the same, less fees), but this will end up costing you in fees overtime anyway, so you are sort of betting on which will be greater - dips in crypto price or fees over time

---

### Post #3 — **kenfus** | 2021-08-03 11:40 UTC

I’d love that solution, but I don’t think there is a way for Numerai to give out stock-predictions without a lot of legal work involved. I think I’m hesitant to stake on my models because of the following reason:

  * 20% return in three months on a worthless token is not enough. What if Numerai dies? The value of NMR would instantly drop to 0 in a couple of hours. To get some nice cash from this, I would need to stake probably around 15-20k USD. This is just a risk I cannot take. Would Numerai pay out (again) BTC or ETH, I’d happily stake because I know that my ETH/BTC would keep their value.



Another proposition for your suggestion could be that Numerai pays out a bonus correlating to the drop in value of Numerai and the performance of their model, if your staking-value for that round was positive. This would finally make people really care about the performance of the hedge-fund because it would counteract the negative volatility of numerai.

---

### Post #4 — **jay1100** | 2021-08-03 12:16 UTC _(reply to #2)_

I guess it would easily work with fiat as well. Instead of burning stakes you could just donate them to some NGO. This way neither the model owner nor numerai would profit from a bad model.  
As far as I understand the main reason for using a crypto token is that you get it for free. Numerai now has several million worth of NMR for free. If you are the one to start a crypto token and the token becomes popular (this is the hard part) then you make a lot of money. This money is used to pay the participants of the tournament. If they would pay in FIAT they would need to get that money from investors, which is not so easy.

---

### Post #5 — **valiunia** | 2021-08-03 17:18 UTC _(reply to #4)_

True, they dont have the money if it was FIAT.

In case of donating to NGO, I thought that too, I think I wouldn’t mind that personally, but in practice it would require a lot of transparency and some would question the specific charity choice, etc, etc

As much as I hate current volatilty, the smart contract approach is game-theoretically sound aligning the goals and making it fair

---

### Post #6 — **pavelk** | 2021-08-04 17:57 UTC

Thank you all for sharing your opinions!

I think there is one line that describes the way many people feel, Valiunia’s reply: `the problem you describe is the actual big problem`

"The Measure of Intelligence is The Ability to Change"​ - Albert Einstein.
