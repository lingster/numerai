---
title: "Staking on Other Users’ Models: A System for Success"
category: Feedback
url: https://forum.numer.ai/t/staking-on-other-users-models-a-system-for-success/1546
created_at: 2021-01-31T22:27:28.398000+00:00
last_posted_at: 2021-05-23T22:31:55.661000+00:00
posts_count: 25
views: 6949
tags: []
---

# Staking on Other Users’ Models: A System for Success

---

### Post #1 — **arbitrage** | 2021-01-31 22:27 UTC

For a long time now, users have asked about the ability to stake on other user’s models. Such an idea at face value sounds reasonable to an outsider, but from Numerai’s perspective, this is not ideal.

How does Numerai benefit from such a system? Without more detail, and assuming this naïve case, they do not benefit.

What if a user could solicit backers? Here’s a thought experiment.

I am willing to accept a backer as long as they agree to a payout ratio of my choosing (where I keep X % of profit) and a sufficient lockup period to prevent backers from chasing short-term gains.

The backer is going to want some assurances of model stability; this would come from some type of vetting process between the user and the backer. Numerai would have nothing to do with this part of the process, but benefits directly, because backers would only select users who could sufficiently satisfy them that the user won’t be swapping submission files and other risky behaviors. Backers therefore would select the users with the best disclosure and communication, which should also translate to the most performant models gaining representation in the stake weighted meta model.

Why have a lockup? First, the user doesn’t want to lose backers after only a few rounds. For such a system to work, the backer has to stick around for a while. The backer benefits from a lockup as well. If the user and the backer share in gains, then they should share in losses, too. Murphy’s Law suggests that most backers would start their lockup at the beginning of a burn sequence, so a long window helps to smooth out the return series in the case of entering during a burn. A claw-back provision could exist, or even a high-water mark. A user could signal their confidence (and justify a high profit sharing ratio) by offering a claw-back or high-water mark just as hedge funds do. This also benefits Numerai because, again, the highest-quality users would offer such terms, and therefore attract larger backers, thus weighing more heavily in the stake-weighted meta model. Again, Numerai benefits in this scenario.

This system requires a few features:

1 – a payout ratio

2 – a lockup period

3 – burn reserve or mechanism for shared burn expensing

4 – a UX for the user to establish the terms of the agreement

Users should offer terms and not the other way around. Users can establish unit sizes for backers so that custom amounts are not required. For instance, every agreement is for a fixed amount of NMR, and the backer can choose how many units to fund. They should be sufficiently large to avoid high ETH gas cost but also small enough to allow for backers to diversify their stakes across a number of models.

I believe the third option is the most difficult only because I haven’t thought about it as much as the other components. Some analysis should be done to ensure that a claw-back or high-water-mark is fair for the model owner but not at the expense of signal value to Numerai.

Here’s a full example.

I offer a 50% profit share with a 4-month lockup. I will only accept units of 100NMR. Stakes compound for 3 months, with a 1-month wind-down to withdraw the NMR to pay the backer and the user. If the net return was 40 NMR, then 20 NMR goes to the user, and 120 NMR goes to the backer. Now the backer can choose to fund another agreement.

What happens if there’s a burn? Here’s where I am unsure of how this would work mechanically.

Same deal terms, but now there’s a burn. If I offer a 50% profit share, then I must be willing to also take part in the burns. This could be funded by the modeler’s personal stake. Surely a backer would not stake on a model that has no stake of their own? If the net burn was 20 NMR, then I would owe the backer 10 NMR. Either a reserve could be established at the start, such that the backer’s stake plus some amount of NMR from the modeler gets locked up together, or upon the initiation of the wind-down process, an amount is withdrawn against the user’s stake to fund the burn share.

Since profit is shared alongside burns, users are limited to the amount of NMR that can be staked against them. This is also good for Numerai, since a single user would be unlikely to attract all of the available NMR for outside staking. A limit exists where the user’s own NMR must be sufficient to fund their agreements with backers in the case of burns.

What about cheap payout ratios? This is sub-optimal for all parties. If I offer a 10% profit share, then the backer is taking 90% of the risk. If I offer a 90% profit share, then the backer may not receive enough return to justify the agreement. At 90%, I’d need to have 90 NMR available on a 100 NMR backer agreement in the event of a full burn, if the agreement called for a full reserve. Leverage, therefore, is controlled by the amount required in reserve. In the vetting process, a user and backer can determine a sufficient reserve requirement. Smaller reserves allow for higher leverage, but more risk for the backer. Again, the vetting and due diligence process benefits all parties; users unwilling to communicate will not receive lower reserve requirements.

Spence (1973) theorized that the greater the cost of a market signal, the greater the trust (creatively summarized). Anonymity is free. Therefore, anonymous users are not likely to attract capital, whereas users who provide a vast amount of data and communication for backers to digest will receive the highest allocations. This, again, is beneficial to all parties, and especially Numerai.

This is simply a thought experiment resulting from discussions that I’ve had over time, and is not a full proposal. I welcome your comments and discourse to improve upon these ideas. Remember, anything that you suggest MUST be additive to the performance of the meta model. Anything that does not benefit Numerai will NOT be accepted. Makes sense, right? They’ve got to do the work to design such a system, after all…

---

### Post #2 — **succulent** | 2021-02-01 13:02 UTC

Assuming enough are open to this, this would also enable creating a fund consisting of the top n models.

---

### Post #3 — **wigglemuse** | 2021-02-01 19:28 UTC

I would say most or all of this proposal could be done as a private deal, i.e. it is something you could do right now. So I think a key question is: is there some version of outside staking that REQUIRES Numerai’s explicit facilitation of such deals, or would it just be essentially a convenience matching service/marketplace with boilerplate rules? (People that don’t like some detail in the set-up could and probably would go and make a private deal instead with terms they liked better.) It seems the benefit would have to be undeniable and sufficiently large for them to do a bunch of work to set-up a system. They don’t want to do some huge project and have 3 people use it.

As to the specifics here, I’m not sure I like reserve requirements and so forth that from the POV of the model-maker turns it into simply a form of leverage where as usual it is all about the rich getting richer. The whole point is to get capital flowing to the best models regardless of the modeler’s ability to stake largely on them. If they have to provide large collateral backstops to the backers to attract said backers, then that’s just more money staked on the existing big stakers and none on the brilliant broke person at the top of the leaderboard. So I think any system has to be geared to a net flattening of the staking landscape (towards existing low stakers with high-quality models) rather than further unbalancing towards the existing whales. Whales could participate too, but for them I think it would more about a risk transfer to the backer while for the low staker it is just a way to make enough money to justify the time spent doing the work – it would be a mechanism that allows them to keep participating period. And that’s where the real benefit to the metamodel would come from.

---

### Post #4 — **succulent** | 2021-02-02 07:44 UTC _(reply to #3)_

I thought about this too, and I think the one thing missing from numerai is being able to verify ownership of a model to the third party. Although one could perhaps do this with model names somehow. I agree, and I think this is too close to hedge-fund territory for numerai to set up the full system, judging by their decisions so far, but maybe nothing speaks against allowing third parties to do this. I think it’s impossible to avoid the “rich model imbalance” problem.

---

### Post #5 — **halsmith99** | 2021-02-03 06:41 UTC

displaying model diagnostic history would enable a potential staker to establish whether the model submission is the same as what has generated the performance history.

i’d suggest something simple like an upfront fee as a percentage of the stake. after the fee is paid the risk/reward is all on the purchaser. and the rest of tournament operates as normal for the purchaser.

---

### Post #6 — **bcb** | 2021-02-03 12:28 UTC

When reading this i thought of what Darwinex is offering as a service for investing in talents (see <https://www.darwinex.com/algorithmic-trading/darwin-api> for short intro).

---

### Post #7 — **liz** | 2021-02-04 03:35 UTC _(reply to #4)_

[@succulent](</u/succulent>), I think a bit of a trust would be in order, as in most kinds of staking relationships I’m familiar with.

Regarding the “rich model imbalance” problem, if I’m understanding you correctly, I think [@wigglemuse](</u/wigglemuse>) was pointing out how to raise the floor, so to speak, rather than limit the distribution. So strong modelers without much money (they exist!) can make their time investment worth it, and at the same time contribute more meaningfully to the metamodel. Richard talked some about wanting to help elevate strong modelers without much money, in a recent fireside chat.

---

### Post #8 — **wigglemuse** | 2021-02-04 03:48 UTC

Yeah, it seems like the only way to go for a public system is more of a free-for-all where backers are essentially playing fantasy football and can bet on what they want week-to-week. If you want a complicated contract agreement with percentages and lockups and clawbacks and high-water marks and guarantees, then that seems like it should just be a private deal. Put a note on your model like that one person (“Buy this model for 1 BTC!”) that it is for sale or rent, contact to discuss terms. But those kind of deals probably aren’t going to help the metamodel in any big way. If it isn’t all about pumping up good models (many of them) with little to nothing staked on them I don’t see the point for Numerai itself to even think about this.

---

### Post #9 — **wigglemuse** | 2021-02-04 04:05 UTC

We’ve also been discussing this as if there is a separate “backer class” where this extra staking will come from (and there is), but if there is a more frictionless system, then all of us existing modellers and stakers can spread around our own stakes on other people’s models easily as well. So if you want to hedge or diversify or you don’t have enough good models of your own yet, then you can bet on models that are obviously different from what you are doing, etc etc. Can’t see how it would not help allocate stakes better. The modellers would have to opt-in I suppose, and then there would have to be a discussion about limits, effect on MMC, etc.

---

### Post #10 — **degerhan** | 2021-02-04 13:40 UTC

I have been using [Interactive Brokers Friend and Family Account](<https://www.interactivebrokers.com/en/index.php?f=46391>) for over a decade to manage a few accounts. Scroll to the Account Structure section to take a look. The account ownership stays with the person, and the trades I make in the master account are allocated across all the accounts in the structure.

IB provides a way to automatically calculate and transfer management and performance fees quarterly from each person’s account to mine, but I have never used it. I believe the moment you start charging advisory fees you would have to register with a state or federal agency as an investment adviser.

I think what [@arbitrage](</u/arbitrage>) is proposing could work by providing a numerai account holder a way to designate some of their 15 accounts as ‘managed-by’ another numerai account. The wallet management stays with the person, weekly submission permissions are granted to the manager account, and performance fees are calculated and transferred regularly.

I suspect the moment you charge advisory fees you would need to register as an investment advisor. And numerai would need to check credentials to allow it on their platform. But I am not really qualitied to comment on those topics.

---

### Post #11 — **succulent** | 2021-02-06 10:40 UTC _(reply to #7)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/liz/48/1103_2.png) liz:

> [@succulent](</u/succulent>), I think a bit of a trust would be in order, as in most kinds of staking relationships I’m familiar with.

This seems like a nice thought, but since everything here is theoretically based on a cryptocurrency and anonymity I feel like we should pursue the philosophy/methodology within and leave nothing up to trust, as evidenced by the huge amount of trust violations in this space.

[@wigglemuse](</u/wigglemuse>) I agree on the free-for-all being a necessity, but I would bet (hah) that this will introduce a lot of instability to the numerai fund. We would then have models to decide which models to bet on, and perhaps even people “gambling it all” on one model. I think it would create some very big stakes on a few models (and they may have been poor before). Then again the stock market seems to “work” so…

I also thought about buying the predictions directly, as a type of private subscription deal, but I’m not sure if people are willing to part with these so easily, there may be a lot of information in them?

---

### Post #12 — **wigglemuse** | 2021-02-06 15:00 UTC _(reply to #11)_

Gambling and prediction markets tell us crowd betting works. But there has to be a mechanism of cost/odds to it – the best models need to be the most expensive to bet on, and/or pay less return (but with a higher likelihood of doing so). I don’t really expect any of this stuff to happen, btw, but if it did those are the kinds of things you’d have to build into such a system.

---

### Post #13 — **no_formal_agreement** | 2021-02-11 23:10 UTC

What problem is “allow users to stake on models that aren’t theirs” solving, and who benefits from having that problem solved? It’s not as if there isn’t enough nmr being staked currently, as users had already come to the previous staking limit last year and will probably be hitting the new staking limit well before the end of this year. What I haven’t seen mentioned here is the fact that structurally speaking there is effectively a competition over a limited amount of staking space and that the current users are already able to meet that demand. Even if the numerai hedge fund begins doing so well that they have an effectively unlimited budget, there will still need to be a max stake in the tournament that is only a fraction of the total circulating nmr in order for there to be nmr availabe for numerai to purchase on the open market, and that max amount will shrink as nmr is burned through tournament activity. I don’t see how opening up to non-participants will benefit anyone other than aspiring free-riders, who of course seem to be the main demographic pushing for this feature.

Ultimately I would highly recommend numerai put their limited time and effort towards other ends.

---

### Post #14 — **wigglemuse** | 2021-02-12 00:01 UTC _(reply to #13)_

I would tend to agree that it really isn’t needed, although I could see how if it was set up properly it would make for a better weighted metamodel as well as help out those users who don’t have a ton to stake but are nevertheless making valuable models. But mainly it gets talked about because it is so often the first question from newbies who don’t plan on modeling, and just want to bet on things.

---

### Post #15 — **robbo_the_fossil** | 2021-02-13 03:45 UTC _(reply to #12)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/wigglemuse/48/3094_2.png) wigglemuse:

> Gambling and prediction markets tell us crowd betting works. But there has to be a mechanism of cost/odds to it – the best models need to be the most expensive to bet on, and/or pay less return (but with a higher likelihood of doing so).

I think this would have to be essential to control volatility. There has to be an incentive to maintain diversity of opinion.

TL;DR - I think this idea increases volatility and that is a bad thing. I remain open to counter-arguments.

First reading this idea I was concerned. It’s taken me a good part of today to figure out why. I think I can articulate it now. The metamodel works because of diversity of opinion, or to put it another colloquial way, the metamodel works because of the wisdom of the crowd.

One of the classic stories told to describe the notion of the wisdom of the crowd is guessing the number of jelly beans in a jar. Collect guesses, average them, and that average is usually quite accurate. It seems to me the reason this works is not because the average is correct, it is almost never exactly correct, but because this method controls variance or volatility of that average guess. It will be wrong, but it wont be wrong by much because the variance of the guess is controlled so long as guesses can be made based on some knowledge of the truth. Guessers can see the size of the jar and won’t guess a kajillion jelly beans for a jar they can hold in their hand, nor will they guess 0 or a negative number - making guessing more [Poisson distributed](<https://en.wikipedia.org/wiki/Poisson_distribution>) I guess, rather than [Bernoulli](<https://en.wikipedia.org/wiki/Bernoulli_distribution>) (Discrete but approximately Gaussian) - but nonetheless, guesses are based on some knowledge.

The variance (square of the standard deviation if you will) or volatility (economic parlance) is only controlled or mathematically well defined when the multiple decisions (guesses) are independent ([independent and identically distributed or i.i.d](<https://en.wikipedia.org/wiki/Independent_and_identically_distributed_random_variables>)). If others can stake based on other peoples staking models, i.i.d would not apply to the crowd, the [central limit theorem](<https://en.wikipedia.org/wiki/Central_limit_theorem>) would be violated and the system’s volatility _could_ blow up.

To bring this back to our jar of jelly beans: if the crowd is watching others make guesses and have decided that person X is a good guesser because she got other counts correct and then start betting on her, but they do not know why she is getting it right, they certainly won’t be able to foretell when she will inevitably get it wrong. (Side note: if the crowd does understand why she is right because her model is open and the crowd likes it, then why bet _with_ her? Run your own copied model at no cost). Presumably nor will she be able to tell when she will get it wrong. Backing bets will increase until she fails -_she will fail eventually_ \- and things blow up… badly… this is volatility.

The counter argument is that if people are staking real money they have “skin in the game”. _**I think I felt Taleb’s ears burn**_. Perhaps; but they don’t have their mind. They don’t have their wisdom in the game at hand (predicting stock outcomes/jelly bean counts). The only ‘wisdom’ is deciding so-and-so is a good guesser. This reinforces opinion. It does not diversify it. Again, things will be great until it blows up. I could list a series of infamous stock market dates, but at this point I should not have to.

OK - but what do I know? I’ve read “The Black Swan” and “The Physics of Wall Street” - that is it. I don’t claim to know a lot. If there is solid research and experimental data that argues against what I just said I’d be happy to read it and reevaluate my position.

---

### Post #16 — **wigglemuse** | 2021-02-13 04:15 UTC

Sports gambling markets are highly accurate. Not on an single-event basis, but on average. It would be the same thing. Yes, the money would tend to just follow whoever was doing well recently, but that’s the same thing that happens in any betting market (and it works at lot of the time too). So as long as the more people piled onto certain models, that proposition became less and less desirable as it does in any betting market – the payout odds go down to the point where you are risking a lot to win a little and then people will go looking for better paying propositions higher-risk higher-reward, i.e. long shots. Such markets are generally self-regulating. But again, the idea that we could actually set up such a market is the longest shot of all…

---

### Post #17 — **robbo_the_fossil** | 2021-02-13 05:37 UTC _(reply to #16)_

This makes sense. I recall reading somewhere how sports betting, especially horse race betting has diversity of bets encouraged by manipulation of the odds - just like you are saying. Too much money on a single horse is too volatile for bookies. This is why the long shot is 200/1, to get people to put some money on it that they will almost surely lose to the bookie. As you said it’s self-regulating. So Numerai would have to adjust odds/payout to encourage betting on ‘dark horse’ models and then have to actually stake that money in the real market using dark horse models! I suddenly like this idea but I also doubt that they will implement it.

---

### Post #18 — **nrichers** | 2021-03-07 02:21 UTC

**Disclaimer: I am not an expert on crypto, smart contract, protocols and etc … Just a poor data scientist trying to leverage his earnings.**

I understand the arguments set out above about the issues of creating an external staking mechanism. It seems to me that arbitrage suggests implementing a “stake” button, where an external agent could transfer their NMR directly to the model’s wallet, and it can only be implemented by numerai itself.

However, I believe that the demand for private deals is actually repressed due to the lack of a trusted agent and formal instruments (smart contracts ??) which could ease the deal. Currently, I have some difficulty in attracting any amount even from friends and family due to the difficulty of explaining the whole operation and the lack of an instrument that formalizes the negotiation, I believe that I am not the only one.

So what prevents a third party company capable of acting as a facilitator of this operation to emerge? “Arbitrage registry”, perhaps? The community itself would be able to investigate potential fraud and service failures. Then the service provider would quickly gain a reputation.

Finally, would it be interesting for numerai to see other companies emerging within its own ecosystem? Wouldn’t creating this mechanism itself be a better way to maintain control? Something tells me that the erasure protocol could be used for this purpose, but I’m just speculating …

---

### Post #19 — **blurmeter** | 2021-03-16 17:20 UTC

Newbie with 4 coins and a willingness to learn, but can tell this is far above my pay grade. I would love to be able to see some data / predictions from X models and then stake based on the one I think will do best.

I don’t know how that could be done, but I’d jump on the opportunity.

Thank you all. Learning tiny bits at a time.

---

### Post #20 — **hb_scout** | 2021-03-16 18:46 UTC _(reply to #19)_

People on this thread might be interested in my current experiment to sell predictions for Round 256 as NFTs on [Opeansea.io](<https://opensea.io/collection/hb-numerai-predictions>). I don’t think it’ll make sense for 4 NMR because the max earn for a single round’s prediction is 25% = 1 NMR, the average earn is 2.5% = 0.1 NMR, while the gas cost alone will be ~$20. So really this experiment is aimed for some whales given the cost of ETH transactions.

See the forum post I made here:

![](http://forum.numer.ai/user_avatar/forum.numer.ai/hb_scout/48/138_2.png) [NFT Experiment -- You could stake on my predictions for Round 256](<http://forum.numer.ai/t/nft-experiment-you-could-stake-on-my-predictions-for-round-256/2379/2>) [Tournament](</c/tournament/7>)

> The sale prices will decrease over the course of the week, getting cheaper as the round approaches. Average submissions on Numerai are earning about 2.5% after the 1-month lockup period. Therefore, an average submission is worth $100 per 100 NMR staked assuming $40/NMR. Past performance does not predict future returns and there is high variation from week-to-week. Staking on other peoples’ model could work out very poorly. It’s a gamble.

---

### Post #21 — **bensch** | 2021-03-26 20:33 UTC

Also going to put this here for anybody that wants to check it out and give their feedback, you can reach me in rocket chat my name is “bensch” there. [Steak on Kovan Test Network](<https://benschreyer.github.io/Steak/>)  
Still working on it so currently it only supports being used on a development test network but I am hoping to get it all working for people to use on the main ETH network (if gas prices permit)

---

### Post #22 — **mindyoself** | 2021-04-10 17:18 UTC

While a great idea, I suspect this is already happening right. However, could this not open a new can of worms with regulation for the numerai token? Rather than it becoming utility. Will the regulators course issue for it.

---

### Post #23 — **schnetzlerjoe** | 2021-05-23 19:49 UTC

Hello. I have been working on a beta version for something almost exactly what you are describing. Everything you are suggesting is similar or semi-similar to what I am building, the only difference I would say is, like any investment fund or asset managed by a third party (unless you partake in a Buffet Partnership like agreement), the model “manager” (or model builder) does not currently burn in any way. The idea behind such a model is like any investment fund, a fund (or staking on someone else’s model) is just another asset (a derivative of your numeral staking model) and thus you as the backer are taking a risk. The idea is you should do your due diligence and invest in someone’s model that has a track record of success or your backer is a family member, friend, etc (which is why I started building this in the first place). If you are interested in becoming a beta user I am popping up the beta sign-up page this week. Would love for you to try!

Best,  
Joe

---

### Post #24 — **liz** | 2021-05-23 20:32 UTC _(reply to #23)_

please do share the link when it goes live! ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=9)

---

### Post #25 — **schnetzlerjoe** | 2021-05-23 22:31 UTC _(reply to #24)_

[@liz](</u/liz>) Awesome. Will do!
