---
title: "Very, very strange TC behavior"
category: Tournament
url: https://forum.numer.ai/t/very-very-strange-tc-behavior/5364
created_at: 2022-05-08T10:29:13.588000+00:00
last_posted_at: 2023-01-13T23:28:30.689000+00:00
posts_count: 38
views: 3197
tags: []
---

# Very, very strange TC behavior

---

### Post #1 — **eleven_sigma** | 2022-05-08 10:29 UTC

I have a V3 model performing very well a weeks ago respect to TC.  
In last three round its TC is lower than percentile 5.

But is strange as the model itself seems not bad:

![Captura](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/d/dc2b1f8e780e7fcce898878d3cd08b299b9cb869_2_690x30.jpeg)

These are the percentiles:  
CORR 87.5  
MMC 81.7  
FNC 92.3  
FNCv3 90.5

And the magic of TC: -0.0854 (Percentile 2.2).

Very dissapointed with TC as seems this is like a lottery.  
Someone with similar experience?

---

### Post #2 — **johnnywhippet** | 2022-05-08 10:47 UTC

Yes. Couple of gold medals then 1st percentile for TC. simultaneously, some of my secret no-hoper models have gone from mid-range TC performance to massive TC scores. I’m buying some dice and a coin-flipping machine to help with predictions for the up-coming rounds.

---

### Post #3 — **taiyaki** | 2022-05-08 12:58 UTC

I am in the same situation. I posted the same information today ( [Why are my TC scores worse after V4 data? Is volatility with a high TC score good for participants?](<http://forum.numer.ai/t/why-are-my-tc-scores-worse-after-v4-data-is-volatility-with-a-high-tc-score-good-for-participants/5362>) ). If you have time, please take a look through it. It is the exact same situation.

To be honest, I too am disappointed at the TC score. I don’t think a score that fluctuates so much is a legitimate metric.

---

### Post #4 — **jay1100** | 2022-05-09 08:32 UTC

I have another possible explanation: The massive TC drop correlates quite well with the time when TC staking was enabled. So probably there was a big change in the models people stake on, because they shifted their stake to their high TC models. This resulted in a big change of the meta model. Since TC is calculated against the meta model, it would make sense that your TC changed a lot.

---

### Post #5 — **johnnywhippet** | 2022-05-09 11:08 UTC _(reply to #4)_

and yet other models, from a quick perusal, would not seem to have suffered the same fate.

---

### Post #6 — **sunkay** | 2022-05-09 12:26 UTC _(reply to #4)_

It seems eleven_sigma’s model is good. Hard to imagine it having a negative contribution.

---

### Post #7 — **eleven_sigma** | 2022-05-09 12:28 UTC _(reply to #6)_

No negative, Percentile 2.2 of TC.

---

### Post #8 — **sunkay** | 2022-05-09 12:32 UTC _(reply to #7)_

-0.0854 is your TC score, 2.2 is TC Percentile

---

### Post #9 — **eleven_sigma** | 2022-05-09 12:38 UTC

And this is other model:  
![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/5/572bc5831dee999f618175107abc26d2c1e78f74.png)  
having  
5.1 PCT CORR  
6.6 PCT MMC  
7.2 PCT FNC  
38.1 PCT FNCV3

The magic of TC: 0.1646 with PCT 99.99

It’s a JOKE

---

### Post #10 — **eleven_sigma** | 2022-05-09 12:46 UTC

[@mdo](</u/mdo>) are you really confident in gradient is measuring what we supposed?

Could you please do a fast and clean test? Check if the gradient is working well.

Compute the metamodel without this last model (with 0.1646 of TC) and see how much  
the metamodel is worst.

---

### Post #11 — **smilence666** | 2022-05-09 15:01 UTC

20% down in one day… not sure what happened the last day of last week.  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/3/35725dfd118a16f2d85267133de802579debfbef_2_690x366.png)image992×527 50.9 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/3/35725dfd118a16f2d85267133de802579debfbef.png> "image")

---

### Post #12 — **smilence666** | 2022-05-10 23:01 UTC _(reply to #11)_

ok…then the following day i got 17% increase  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/d/d0b141d1d9de492514880d4a2e052f2c663f9b05_2_690x339.png)image996×490 52.7 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/d/d0b141d1d9de492514880d4a2e052f2c663f9b05.png> "image")

---

### Post #13 — **mdo** | 2022-05-10 23:32 UTC _(reply to #12)_

Yeah markets are quite volatile at the moment and a metric based on portfolio returns (i.e. the returns of a subset of the stocks) is going to be much choppier than correlation to a normalized target across all stocks. With lots of stocks making double digit moves such things are to be expected.

---

### Post #14 — **johnnywhippet** | 2022-05-11 10:27 UTC _(reply to #12)_

ditto.

* * *
    
    
         __     __                    _      ____   _               __ 
     __ / /__  / /  ___  ___  __ __  | | /| / / /  (_)__  ___  ___ / /_
    / // / _ \/ _ \/ _ \/ _ \/ // /  | |/ |/ / _ \/ / _ \/ _ \/ -_) __/
    \___/\___/_//_/_//_/_//_/\_, /   |__/|__/_//_/_/ .__/ .__/\__/\__/ 
                            /___/                 /_/  /_/

---

### Post #15 — **liborty** | 2022-05-15 03:02 UTC

Surely, the actual predictive performance (correlation) is all that should matter.  
I can see the usefulness of these additional arbitrary measures for the building of the ‘metamodel’ internally but not for the individual predictors.

---

### Post #16 — **rigrog** | 2022-05-15 06:05 UTC _(reply to #15)_

I agree that it _seems_ that way… but only Numerai _sees_ the “actual predictive performance”, by taking market positions. And based on what they see, they adjust the incentive package. And _re_ -adjust, about half a dozen times already.

Still though, you can choose to ignore TC and stake only on CORR.

I have no idea, how I could aim my model design toward high TC. But if my model somehow _hits_ positive TC, I’ll respond to Numerai’s incentive signal and stake on it.

---

### Post #17 — **wigglemuse** | 2022-05-15 16:12 UTC

Ensembles only thrive with diverse components. TC will certainly incentivize more diversity. It is just a question of how much accuracy is given up (component-wise) to get it. First, let’s assume that a large portion of modellers switch to striving primarily for TC (which may not even happen). Even if they do, it is quite possible an ensemble based (largely) on TC feedback will turn out to be about the same as the one that was based on CORR/MMC feedback (even though the components will be quite different than before). Or it could be a lot better, or modestly better, or worse. We’ll just have to see. Given the way TC is made, worse seems unlikely so this is probably a good bet on Numerai’s behalf. But nothing is guaranteed, and if the users hate it then maybe it won’t work out even though it technically should. I imagine with the huge magnitudes TC is capable of paying compared to CORR that it would be a good incentive, but then again the burns can be just as big. In a bad round, you’ll be thankful for a low payoff factor if you are betting on 2x TC. (Your earn/burn is capped by the 0.25 round payoff/burn limit * payoff factor, so if payoff factor is 0.45, what could have been a 25% burn will only be 0.25*0.45 = .1125 which is bad enough.)

On the question of “can you optimize for TC?” In the sense of can you just put TC into a loss function, then no you can’t do that, but that doesn’t mean you are 100% in the dark. You can certainly make educated guesses about the types of methods and niches you could explore that you could reasonably expect not many others to be exploring, i.e. maybe don’t make a vanilla xgboost model if you are shooting for high TC. Although even if you do, you’ll probably be at least positive on TC over time (the integration_test models both have positive TC) – a “normal” straightforward model with fairly high metamodel correlation getting decent CORR scores probably won’t lose (on average) betting 0.5x or 1x TC along with CORR. But to really excel on TC you’re gonna have to do something weirder (and be ok with more volatility in results). If you must absolutely have a definite function to optimize on, FNC3 looks like the one (or make a custom one that is similar). Some high TC models are doing very bad on FNC3 (and CORR), but very few high FNC3 models are getting negative TC so that seems fairly safe. Could be a moving target though…

---

### Post #18 — **qeintelligence** | 2022-05-15 19:13 UTC _(reply to #17)_

Totally agree with [@wigglemuse](</u/wigglemuse>) , I got 2 models in the top 100 (one currently at nr5), and I remember I put those models out there as a shot in the dark, like just try something bananas ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=10) Guess it works a bit for now, that said it can also be over in a heartbeat, I had another model also top30 TC, and within 1-2 weeks its totally gone (as in bad TC performance on all rounds suddenly). At least I got a bit lucky this time, lol.

---

### Post #19 — **kayeffnumeraitor** | 2022-05-16 06:33 UTC

To me it seems models that are very sure to not have negative correlations regardless of how miniscule the mean correlation is (< 0.01), tend to get high TC values. My guess is to not optimise for a high mean of correlation, but rather the probability for the correlation to be positive across eras will lead to a high TC value.

---

### Post #20 — **d3monw3st** | 2022-05-19 19:58 UTC

Looks like a totally random model does quite well with TC, wonder if it’s a fluke or if it’ll keep going.  
<https://numer.ai/totally_random>

---

### Post #21 — **sunkay** | 2022-05-20 03:08 UTC _(reply to #20)_

It seems that low CORR W/METAMODEL model tent to get high TC.

Top TC models on the leaderboard have very low CORR W/METAMODEL.

---

### Post #22 — **eleven_sigma** | 2022-05-20 11:29 UTC _(reply to #20)_

This could makes sense, as a random model will have in average 0 CORR with response and 0 CORR with metamodel if you give more importance in TC to uniqueness than correlation the balance will be positive.  
This is a sign of overfitting in the TC computation if random noise added to the metamodel improves it.

---

### Post #23 — **wigglemuse** | 2022-05-20 14:32 UTC

There are random models and then there are random predictions. It is not weird at all that randomness will have good rounds – but it should also have equally bad rounds. And if it is a random MODEL, meaning that it was randomly created but once created remains the same model, then it is also not weird that it would exhibit streaks of goodness or badness because there is high auto-correlation between round results (at least much of the time). Any random model will settle somewhere over time – most likely right around zero, but a randomly-made model can also be randomly good or bad (but again, not likely to be strongly one thing or another unless it isn’t as random as you thought – some “random” methods make very good models). (And do we have any information about what this example actually is?)

If there is no model and there are just random PREDICTIONS created fresh each round, then the first thing holds but there should be less streakiness involved because now the predictions would have no auto-correlation with themselves. But streaks appear randomly too, and those streaks can be much longer than your intuition would think.

As far as being less correlated with the metamodel leading to greater TC, of course it does, no surprise there and the team has pointed that out repeatedly and has been encouraging more original models. However, this uncorrelation BY ITSELF won’t give you TC riches, but it is more like it is increasing the potential TC capacity of your model, i.e. it still has to be a good model – your potential for high negative TC grows with your potential for high positive TC as you become less correlated with everybody else.

---

### Post #24 — **robo_boi** | 2022-05-21 11:56 UTC _(reply to #23)_

I’ve been doing random predictions for signals for awhile: [Numerai](<https://signals.numer.ai/jersey_devil>)

Like wigglemuse said, there are good runs and bad runs. Overall it’s down about 30%

---

### Post #25 — **liborty** | 2022-11-16 05:16 UTC

Rightly or wrongly, these tournaments are beginning to look deeply suspect, like so many enterprises based on crypto coins.

Some time back, I was getting really poor 1% on TC. The correlation was more stable but not much better and my Numeraires were getting burnt off at an alarming rate. So, partly as an experiment, I cancelled the stake. As soon as I had done that, my TC shot up to 95%+. So I turned the staking back on and now TC has again fallen back to around 1%. I am not talking about one-off week here but several weeks running in each case. Deliberate or not? I guess we will never know. It is certainly in no way transparent.

---

### Post #26 — **wigglemuse** | 2022-11-16 14:22 UTC _(reply to #25)_

Mean reversion. If your NMR is burning at an “alarming” rate you are staking beyond your risk tolerance (and possibly beyond what math would sensibly indicate). When bad periods inevitably arrive, you shouldn’t be panicked – it’s a bad period and it will pass. If you have staked too much (or at too high a multiple) that those periods are going to freak you out and make you pull stakes, then also inevitably you are going to miss the following upswing. This is pretty much a universal pattern in betting/gambling. Strong emotions (up or down) attached to particular outcomes in short time-frames shouldn’t happen – they are a sign of over-staking (psychologically and probably mathematically) – and they lead to hasty emotional decisions.

But I’d just point out this isn’t a casino – there is no motive to rig the game. Numerai has nothing to gain by you losing. They do well when we do well – by extension when you do well. When you burn, do they gain anything? Nope, that means they are suffering also. So…TC is a black box to us, it’s true. (Hopefully that won’t be true forever.) Bugs or incorrect calculations are a possibility (just from the fact that we can’t independently verify). But…“deeply suspect, like so many enterprises based on crypto coins”…that sounds like an implication of deliberate tampering with results. Again, there is no motive, it is contrary to their interests to do that.

---

### Post #27 — **liborty** | 2022-11-17 07:30 UTC _(reply to #26)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/wigglemuse/48/3094_2.png) wigglemuse:

> Numerai has nothing to gain by you losing.

Except my money, of course.

It is only alarming in as much as it may take me out of playing in these tournaments.  
I am not that stupid to consider NMR as some kind of an investment.  
Anyway, the degree of my alarm is not really the main point here.

---

### Post #28 — **magic101** | 2022-11-17 13:55 UTC

Having participated for 75 rounds and reviewed the performance against CORR and TC, I now believe the tournament has essentially shot itself in the foot by moving to an unpredictable target. When looked at in combination with the ever decreasing payout factor, the volatility of the token in relation to fiat, and changes to the structure which sometimes need manual recoding to stay “competitive”, it becomes apparent that there is no point in spending time continually improving a model when the reward is not directly linked to its individual performance. That is simply gambling, and there are many easier ways to do that.

---

### Post #29 — **restrading** | 2022-11-17 14:04 UTC _(reply to #27)_

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/l/b4bc9f/48.png) liborty:

> Except my money, of course.

NMR burns go to the burn address, not Numerai’s treasury. They don’t gain from your burning.

---

### Post #30 — **wigglemuse** | 2022-11-17 15:11 UTC

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/l/b4bc9f/48.png) liborty:

> Except my money, of course.

They do not get your money, that’s my point.

If you want to criticize TC for being terrible (like [@magic101](</u/magic101>) above) and a mistake and a bad idea, etc, I won’t argue with you. That’s a legit argument. But when you imply they are running a scam or stealing from you by manipulating scores, there is nothing to support that and again zero reason to do it. They want the fund to to well – to drive people away making good models by tinkering with their scores to no benefit to themselves (and losing the benefit of your good model) doesn’t make any sense at all.

---

### Post #31 — **murkyautomata** | 2022-11-17 22:45 UTC _(reply to #28)_

The decreasing payout factor is a necessary consequence of CORR staking. Anyone who can copy a sample notebook can farm NMR staking on CORR, so naturally total CORR stakes increase. Unless you expect numerai to provide exponentially larger payouts over time, CORR staking must require a diminishing payout factor.

TC being more of a competition does not have this problem, but for the same reason it is more difficult. TC is not random. We know that it correlates with CORR at around something like 0.25, and if you submit a model that outperforms the rest of the meta-model, a positive TC is a certainty. Reasoning about what creates a positive TC may be more theoretical than what many data scientists are used to, but it can be done and many on the leaderboard have managed a fairly consistent return on TC.

---

### Post #32 — **liborty** | 2022-11-17 23:16 UTC _(reply to #30)_

Well, let us hope so. My main argument is that with a ‘black box’, with obfuscated inputs and obfuscated outputs, it can never be more than just a hope.

---

### Post #33 — **murkyautomata** | 2022-11-17 23:45 UTC _(reply to #32)_

The advantage of smart contracts is that everyone can see what they will do. The smart contract, which dictates what happens to burned NMR, is not a black box.

---

### Post #34 — **liborty** | 2023-01-13 00:42 UTC

Nowadays, I am getting corr20 over 90% and corr with metamodel negative. Are these not the circumstances, from which the metamodel should be learning and therefore TC ought to be high? Yet, I am still getting poor TC. Could you please explain to me what is going on?

---

### Post #35 — **kayeffnumeraitor** | 2023-01-13 12:13 UTC _(reply to #34)_

Someone did a post (I think 2 months ago?) where it can be seen that low corr with meta model will also increase TC volatility up to a point where your mean TC has to be really high otherwise you have basically random TC.

Another thing that I found during my experimentation (I am still waiting a few weeks to have more definive results) that TC seems to be more related to ranking metrics than pure correlation. Imagine having an onlineshop where your search will lead to 5000 products that might be of related to your query. Nobody is interested if the products somewhere on page 50 are accurately ordered by your preferences, but only the top results are important. In case of Numerai, it seems that both top and bottom results are equally important, especially for TC. So TC is a really different metric, more so than other metrics.

Another thing is that TC is a gradient, not a global optimum, which can be quite confusing, at least it was (still kinda is) like that for me. It means increasing your weight in the meta model ensemble just ever so slightly while also considering risk constraints makes the MM worse, eventhough your model alone might be better in this round. There still can be a local performance minimum in the direction of your model weight. eventhough the maximum behind it might be higher than in its current configuration.

---

### Post #36 — **jrai** | 2023-01-13 13:29 UTC _(reply to #35)_

you probably need to separate out the different types of models that have low corr with meta model for that analysis to be right. the two types being an actual model that just happens to have low corr and a random seed that by definition has low corr

---

### Post #37 — **wigglemuse** | 2023-01-13 15:59 UTC _(reply to #35)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/kayeffnumeraitor/48/991_2.png) kayeffnumeraitor:

> Someone did a post (I think 2 months ago?) where it can be seen that low corr with meta model will also increase TC volatility up to a point where your mean TC has to be really high otherwise you have basically random TC.

While they did show some stats about mean and corr w/ meta model (CWMM) that would be consistent with that conclusion based on those two things alone, nevertheless that conclusion is not warranted, at all. It only tells you that lowering your CWMM will not automatically give you a higher TC mean, but it will probably give you higher volatility. (And this is not really news.)

---

### Post #38 — **liborty** | 2023-01-13 23:28 UTC _(reply to #35)_

Whatever the actual mysteries of TC are, the ranking kind of makes sense. That is why I referred above to percentages of my corr20.

Could it be that my actual model nonetheless produces random results? Hmmm. Something to ponder.
