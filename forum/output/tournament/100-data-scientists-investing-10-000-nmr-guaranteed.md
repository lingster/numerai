---
title: "100 Data Scientists Investing 10,000 NMR - Guaranteed"
category: Tournament
url: https://forum.numer.ai/t/100-data-scientists-investing-10-000-nmr-guaranteed/1107
created_at: 2020-10-28T19:38:36.015000+00:00
last_posted_at: 2020-12-14T02:41:08.861000+00:00
posts_count: 22
views: 3584
tags: []
---

# 100 Data Scientists Investing 10,000 NMR - Guaranteed

---

### Post #1 — **lackofintelligence** | 2020-10-28 19:38 UTC

I have been puzzling over several issues important to Numer.ai and its contributing data scientists:

  1. The need of Numer.ai to have highly staked and consistent predictions for the indefinite future.
  2. The need of staking data scientists who are confident in their models to not have their gains wiped out by NMR price fluctuations.



Given that NMR price fluctuates to the market, neither of the above needs can easily be satisfied.

Well there _is_ a way to basically guarantee that at least 100 confident data scientists will stake 10,000 NMR and I am not talking about an air drop. That would defeat the purpose. We want data scientists to have skin in the game. Yet we want to guarantee them high price stability. There is a very easy way to do all of this.

How?

Sell NMR crypto contracts for $1 per NMR. The contracts stipulate that all of the NMR is held by Numer.ai in the model name of the data scientists choosing for 3 years before the data scientist can make any withdrawal. After the special sale, the price of the NMR is determined by the market. If a data scientist fails to make any weekly submission then that week counts as a loss of 1 percent of the stake exactly as though the model had achieved a correlation score of -0.01. Otherwise the earnings are just normal nomi earnings. Can these rules be squeezed into the NMR contract?

Notes:

  1. The actual value of the sale price TBD, but a valuation of between $1 and $5 would be fair.
  2. The actual holding period of 3 years TBD. But anything much more than 3 years may be difficult to achieve in practice. Also, the price and the time period of the holding are coupled, but $1 for 3 years is acceptable, maybe $5 for 2 years scaled logarithmically if more choices desired.
  3. The actual weekly default loss for a missed round should probably be closer to 3 percent for reasons I will discuss in the answer to [@nasdaqjockey](</u/nasdaqjockey>), below.

---

### Post #2 — **nasdaqjockey** | 2020-10-28 23:49 UTC

I’m not following what this does. Can you explain the contract concept more? $1 for an NMR seems very cheap right now. Could you buy a contract with existing NMR?

---

### Post #3 — **lackofintelligence** | 2020-10-29 02:47 UTC

In this context the concept of contract (say that 3 times in a row) has two related definitions:

  1. a contract is an agreement the terms of which are outlined,
  2. a contract is very specifically a crytographic contract that is written into the block chain.



For our purposes what is most important about a contract is that its possible to arrive at a set of rules that can be agreed upon and executed. Its probably secondary that these things can be defined in the block-chain, but NMR is a cryptocurrency, so if this proposal is very interesting than why not rigorously place the rules there?

For arguments sake let’s assume that there are _at least_ 100 data scientists who are aching to stake big on their model right now. They want to, but it does not seem like the right time. Why not? Because they can see the price of NMR varying by 100-200% over the course of weeks. If they invest now, they feel like they might lose big, just because of price fluctuations, no matter how much faith they have in their model.

The solution is to sell to these data scientists NMR at a low price. Then let the value of the NMR rise to its natural level. One can never ever be sure of anything, but based on the full history of NMR, if anybody were lucky to buy at $1 they could be fairly certain that their investment would not lose value _through the cryptocurrency market_.

Ah, but there is the rub.

How do we distinguish these serious committed data scientists from folks that just want to get rich quick by buying NMR at $1 and then tomorrow selling at $25? Well the rules of the contract dictate that they can’t sell, they cannot even withdraw that NMR from a specific model name (they can do whatever they want with the model). The contract rules dictate that the entire amount will be staked for the next 3 years, no if-ands-or-buts. And that NMR is at risk of taking a very serious hit, since if the person buying these contracts thoughtlessly forgets (or does not know) that they have to submit a working model every week for the next 3 years then they will come out of it with a significant loss to their investment.

EXAMPLE:

Let’s assume that the agreed weekly loss amount for a missed round is 3% and that in 3 years the price of NMR floats up to $50. Then an investor who does nothing more than buys 10,000 NMR at $1 and just sells it after 3 years will end up with

> $10,000 \times \frac{1\mathrm{NMR}}{\$1} \times (1 - 0.03)^{3\times52} \times \frac{\$50}{\mathrm{NMR}} = $5185 .

Which is half of their original investment. This is _not_ a good deal for anybody except a seriously committed data scientist. Does this make sense?

---

### Post #4 — **kkk** | 2020-10-29 09:10 UTC _(reply to #3)_

Fixing 1$ in this special contract sounds interesting, however, there are two issues to consider : first, you cannot guarantee that the market price of NMR will never drop below 1$, the downside of cryto has no limit, once you increase the entry level of NMR, it will soon lose interest of the market ! Second, 2-3 years appear a long ‘locking’ horizon to which participants would like to commit, it’s like that you invest into something even less lliquid than a VC but assume much larger reward uncertainty, even if NMR grands interest during the lock period, it seems not a quite effective incentive.

If we want to put in place a sort of “skin in the game” mechanism, it should break the limit between tournament and the real hedge fund, letting the top performers share X% of the annual performance fees of the fund, which can be stake-weighted among contributors. Does it sound logic ?

---

### Post #5 — **lackofintelligence** | 2020-11-02 04:24 UTC _(reply to #4)_

The fact that you cannot eliminate risk is something we agree on. Recognize that there are at least three sources of risk:

  1. Model performance relative to the stock market
  2. Price fluctuations of NMR relative to the cryptocurrency market and broader market.
  3. The opportunity risk of committing long term to a project that may or may not pan out.



None of these risks can be eliminated. The first source of risk is what the Numer.ai data scientist’s model is all about. That model cannot affect the other sources of risk. However, the mechanism discussed here _can_ reduce the 2nd and 3rd sources of risk. We _can_ plausibly reduce the risk that a price drop destroys our investments by setting the buy-in price low. Consider that data scientists who are already staked are pretty well locked in already, why not reduce the opportunity risk by granting them a reward for sticking it out long term? That reward is given in exchange for an agreement that they will submit their best model every week or either incur penalties or losses for the duration.

I am not sure that answers your question because you seem to think higher potential rewards are not worth a sustained effort. But that is exactly when higher potential rewards should be engineered.

---

### Post #6 — **wigglemuse** | 2020-11-02 04:52 UTC

Over a long time-span I’d allow skipped weeks (sometimes there is just a hurricane or you break your leg or whatever) and so instead of a fixed period on the calendar make it a fixed period in number of submissions.

---

### Post #7 — **lackofintelligence** | 2020-11-18 23:22 UTC

Let me talk a little more about the 3rd source of risk mentioned above.

The main content of this proposal minimizes that risk infinitesimally, or really only indirectly. Whereas the knowledge pool of the data scientists staking NMR is pretty large, within that pool, except for some insider data scientists, there is very little knowledge of how the actual business is running. How successful is the Hedge Fund? How much investment does it have? We only have very sparse, general and positive outlook type remarks fed to us. This is really the biggest imbalance between all of the risks Numer.ai data scientists are taking for Numer.ai and the services that those data scientists provide to Numer.ai. If you are _certain_ that Numer.ai will succeed then it is because you have insider knowledge that is not being clearly disseminated to the rest of the data scientists (rocket and fireside chats do not count either in strength of media or content). Note that you cannot infer how well the company is being run based on observing insider data scientist staking behavior and neither from company advertisements for hiring (long known to be a practice of indirection in many industries).

So even if the main part of this proposal is thought to be extravagant either because of the length of time data scientists would have to be committed to it or because of the outlandishly good price struck in the proposed deal, I still think Numer.ai owes quarterly email reports on the company outlook to data scientists who have been continuously staking for more than a year so that they can continue to be confident in staking on their models with respect to the 3rd source of risk presently addressed.

---

### Post #8 — **photovore** | 2020-11-19 03:08 UTC

I am seeking skills to achieve this. Hope it helps anyone who may already posses these skills… Data Scientist

[![Capture](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/9a33ac60f834714304784c2c851e14396e879e39_2_690x207.jpeg)Capture1002×302 28.7 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/9a33ac60f834714304784c2c851e14396e879e39.jpeg> "Capture")

  


[![Capture1](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/3ff0a67ecdc3322826242a5fa17c0dff480dbc4d_2_690x134.jpeg)Capture1936×182 10.5 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/3ff0a67ecdc3322826242a5fa17c0dff480dbc4d.jpeg> "Capture1")

---

### Post #9 — **jrai** | 2020-11-19 16:56 UTC

Seems like an over-engineered solution to a problem that doesn’t really exist. There are so many parameters to tune on this that nobody will ever be happy. In sum, I can sell all of my existing NMR to re-buy at a >90% discount? Are you sure you want that?

---

### Post #10 — **lackofintelligence** | 2020-11-19 17:40 UTC _(reply to #9)_

[@jrai](</u/jrai>), if you are referring to the $1 buy, yes, this is what you and Numer.ai should want. But as has been noted by myself and others, this is actually a tough bargain for you or anybody else who would enter into it. You have to submit a model every week for 3 years, with some forgiveness only given in case of extreme natural disasters (the sea level rose into all redundant data centers) or you take a penalty equivalent to a big loss for that week. Its a pretty serious hook because you can’t put your hands on that NMR for 3 years and the business could even go under in that time. One usually locks cash up in investments more secure than this, so I see this as a trade that is more than fair for them. The more I think about it the more I think that the time commitment is hard. One would certainly want everything automated before entering into such an agreement. Then have the heart to just forget it all in case it all fails.

In regards to the idea of lots of different parameters to tune, there are many monetary instruments out there that all use “advanced” formulas for determining a fair price. But we are not the ones defining these. Numer.ai is the one. They can provide multiple instruments with different prices and different time period commitments. Then it is up to us to select one that we think we can work with. My gut feeling is that they do not see any of these options as good for them because they can’t see that far into the future. That’s something I can appreciate, but I would love to be proved wrong on that.

---

### Post #11 — **of_s** | 2020-11-19 18:10 UTC _(reply to #10)_

If the time commitment represents sufficient skin in the game, then why not adopt a prop trading model?

Fund participants with ??? NMR and remove the ability to withdraw any _**profits**_ until the adequate time elapses.

---

### Post #12 — **lackofintelligence** | 2020-11-19 19:54 UTC

If you give away the NMR, then the data scientist really has nothing to lose. The quality of the submitted model can be zilch. Its the combination of real cash locked up for a long time that makes the deal poignant and thus worthwhile for both sides. The purpose here is to reduce exterior risk without compromising model quality.

---

### Post #13 — **of_s** | 2020-11-19 20:15 UTC _(reply to #12)_

How has the NMR been given away if the data scientist is unable to withdraw it? If they submit a zero quality model and earn 0 NMR, then they are entitled to zilch. Model quality is ultimately proven over time.

---

### Post #14 — **lackofintelligence** | 2020-11-19 20:56 UTC

A mechanism is needed to fine tune the amount “given away”. Otherwise at $0 per NMR you are giving away infinite NMR to infinite “data scientists” and with limited NMR existing from day one and who knows what fraction of it getting burned, that system does not seem to work to me. How do you handle that? A finite price (presently the actual market price) is thought to be the correct mechanism for handling evaporating NMR.

You might consider the crypto-economics, the business aspect to Numer.ai and what it might take to convince them that your suggestion is worthwhile.

---

### Post #15 — **lackofintelligence** | 2020-11-19 20:59 UTC _(reply to #14)_

Maybe that NMR gets recycled? Still at $0 per NMR it will quickly become locked up and liquidity will drop to zero. There is a huge gulf between one and zero.

---

### Post #16 — **of_s** | 2020-11-19 21:50 UTC _(reply to #15)_

No NMR would actually be created or destroyed, it would all be bookkeeping on Numer.ai’s end until that proving period expires.

Numer.ai could restrict the number of participants or amount of NMR to participate with in order to protect against locking up all existing NMR…which would actually be a good thing considering it would be an artifact of positive correlations (or MMC if they so chose to move to that metric exclusively).

---

### Post #17 — **lackofintelligence** | 2020-11-20 04:29 UTC

I think its an interesting idea. The issue is that the mechanism for controlling the number of accounts or the evaporating NMR keeps backing up. You still have not fully described it. For instance, how does Numer.ai restrict the number of participants? You have not described a system that does that fairly. What _is_ working at the moment is setting a finite price on NMR using the market to decide the price. My entire argument has been that that method is far from ideal, yet I believe it is far better than just giving NMR away.

---

### Post #18 — **of_s** | 2020-11-21 15:03 UTC _(reply to #17)_

The prop trading model is fairly well established in the fund industry who have less flexibility due to finite fiat resources. Numer.ai has more room to operate due to NMR as medium of payment, no margin requirements for positions, etc. NMR is not being given away, it is ultimately being earned by the data scientist over time.

---

### Post #19 — **lackofintelligence** | 2020-11-21 16:58 UTC _(reply to #18)_

Its the other way around. Fiat sources are infinite, remember? That is why we have inflation and it is one reason crypto-currencies were invented. On the other hand NMR is finite, payouts are precisely measured and they are presently even capped.

I would again suggest that you describe the mechanism for distributing “???” NMR with a clear strawman example so that we can see how this works.

---

### Post #20 — **of_s** | 2020-11-21 17:35 UTC _(reply to #19)_

A fund with $100mm or whatever Numer.ai equivalent in AUM (finite fiat) is far less flexible than Numer.ai…

What is so difficult to envision a first come first served allotment of NMR to qualified data scientists?

---

### Post #21 — **lackofintelligence** | 2020-11-22 03:56 UTC

Sorry, I can’t seem to answer your question satisfactorily. I welcome you to make a forum post about your idea. The idea I am presenting here seems very different to me. I also apologize in advance for not trying to answer any more questions about your proposal. I’ll try to stick to answering questions about the one I am presenting.

---

### Post #22 — **lackofintelligence** | 2020-12-14 02:41 UTC

Maybe the biggest argument against this proposal is the idea that it would drive the price of NMR down to a dollar.
