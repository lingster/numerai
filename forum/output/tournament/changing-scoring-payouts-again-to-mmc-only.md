---
title: "Changing Scoring & Payouts Again To MMC Only"
category: Tournament
url: https://forum.numer.ai/t/changing-scoring-payouts-again-to-mmc-only/6794
created_at: 2023-11-15T04:03:37.974000+00:00
last_posted_at: 2023-11-29T05:36:56.093000+00:00
posts_count: 30
views: 3996
tags: []
---

# Changing Scoring & Payouts Again To MMC Only

---

### Post #1 — **richai** | 2023-11-15 04:03 UTC

tl;dr Numerai will no longer make payouts based on CORR or TC, all payouts will be on MMC only on a new upcoming target called Teager starting the end of this year.

Numerai has made payouts in a number of different ways over the years as this meme from RocketChat shows. I mentioned in the Fireside chat, we need to make changes to payouts to discourage poor performing models from staking. [I went through different ideas](<https://youtu.be/hyMpAeBLHPg?si=shTB_Vd9mFm9BCoc&t=4293>) but I think we’ve settled on something. Thanks [@murkyautomata](</u/murkyautomata>) for your help.

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/0/0b04785bd7167ff261f26325bc926c107398e26a_2_690x486.jpeg)image1503×1060 493 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/0/0b04785bd7167ff261f26325bc926c107398e26a.jpeg> "image")

On the one hand, it seems natural to pay Numerai participants based on their predictions’ correlation to the target Numerai defines. On the other hand, Numerai already has [benchmark models](<http://forum.numer.ai/t/benchmark-models/6754>) which already have very good correlation with the targets see: [Numerai](<https://numer.ai/~benchmark_models>).

Another payout mechanism which seems natural is True Contribution (TC): how much your staked predictions improve the post-optimization portfolio returns for Numerai. However, TC has some weaknesses in that it is blackbox and also tied to certain optimizer settings. The optimizer settings for Numerai One and Supreme are different from each other and change from time to time. To have TC stay “True” the whole time would require constant alterations to it — even the size of the funds influence TC. So TC is challenging to maintain without becoming even more blackbox and mysterious.

MMC ([MMC2 Announcement](<http://forum.numer.ai/t/mmc2-announcement/93>)) was the previous way we solved the problem of incentivizing orthogonal signals that are actually contributing to the Meta Model. We take the Meta Model predictions and ask: does a small weight on your signal when added to the Stake Weighted Meta Model improve or hurt its correlation with the target? (This is equivalent to the residual-MMC discussed in the old MMC2 post).

In the past, MMC had some weaknesses. It used to be computed against old targets without feature penalization or without liquidity adjustments (many small stocks need a liquidity adjustment to reflect that a decent size hedge fund can’t buy them in large size). Because MMC on old targets had these weaknesses, we developed TC. However, we are now almost ready with a new target (called Teager) which does almost all the important transformations that the optimizer does within the target making MMC on this target a great measurement of contribution. In other words, _MMC on this target is quite close to having TC_ under new minimal optimizer settings Numerai intends to move to. Also important to note: Numerai now gives out the Meta Model signal so MMC is not a blackbox any more and can be computed locally.

_So why change to MMC only payouts? Why can’t it be optional? Why can’t you keep CORR or TC?_  
In the past MMC and TC were optional to stake on. Many users would simply stake CORR with a large stake and not stake MMC or TC at all. The problem is many large stakers this year have had persistently negative TC & far worse TC than benchmark models. This would be fine if these models were being burned away but if they weren’t staking TC this year, they would hardly burn at all if their CORR was okay or flat. The point of payouts is to get feedback into the stakes so that the Stake Weighted Meta Model can improve. Users persistently hurting the Meta Model but doing okay on CORR shouldn’t be able to earn a positive return on their stake; they should earn a strongly and persistently negative return on their stake.

_How much payout multiplier will be available on MMC?_  
We think MMCx2 is probably makes sense. Whatever multiplier we choose there will only be one multiplier. For example, if we choose MMCx2 everyone who stakes will have to stake with that multiplier and there will be no option for MMCx0.5 or MMCx3. This puts all staked NMR on a level playing field for earnings.

_Aren’t you worried this will cause many users to unstake because earning MMC is too hard?_  
We are not worried in fact _we sincerely hope_ fewer users stake on Numerai after this change. Clearly, unlike any web service I can think of, Numerai can actually benefit from losing users if they aren’t good. Of course, we are hurt badly if we lose the best data scientists i.e. the data scientists who will be the best going forward at MMC. But by making the tournament harder and getting users who _don’t even believe they have any MMC_ to stop staking, we are going to get to a world where the payout factor is far higher for the top data scientists who remain. And of course, users who don’t think they have MMC can still submit unstaked predictions to Numerai until they feel confident enough that they have MMC that they are prepared to stake on it.

To put it even more simply: Numerai data scientists can currently earn NMR even though they hurt the fund performance (they had bad TC but didn’t stake it) and performed far worse than Benchmark Models (on CORR or any other metric we display). Does it make sense for Numerai to reward models like this? What for? It’s a bad incentive. You can see the problem by noting the average return on stakes on Numerai is 30.65% over a year where the Meta Model and fund performance has been poor. Clearly, payouts are too generous in aggregate at the moment to make any sense for us or you in the long term. We were happy to have generous payouts to seed the data science community but going into next season, we need to have much closer alignment. Producing a contributive model to the Meta Model is very difficult; earning payouts on Numerai has to be exactly as difficult.

[![Screenshot 2023-11-14 at 7.02.19 PM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/3/357d405053705bdf084a558ee731400fa4572d29.png)Screenshot 2023-11-14 at 7.02.19 PM426×232 8.76 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/3/357d405053705bdf084a558ee731400fa4572d29.png> "Screenshot 2023-11-14 at 7.02.19 PM")

[![Screenshot 2023-11-14 at 7.27.03 PM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/7/74ad0c628f15736d75e6d7a149e8f28a173c6401_2_690x446.png)Screenshot 2023-11-14 at 7.27.03 PM1302×842 82.6 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/7/74ad0c628f15736d75e6d7a149e8f28a173c6401.png> "Screenshot 2023-11-14 at 7.27.03 PM")

_What about Signals?_  
There are no changes planned for Signals just yet. Numerai Signals already has payouts on the stricter FNC rather than CORR. Though it is possible the TC payouts on Signals could change to something more MMC-like in the future as well.

More details to follow and we plan to release the new Teager target by the end of the month.

---

### Post #2 — **unsentient** | 2023-11-15 06:36 UTC

Sounds good. Thanks for the heads up. I’ve never understood why optional multipliers were allowed. I think Crowdcent and Atol would have changed tack or de-staked a long time ago if they had been forced to stake on 1xCorr+3xTC. I will say that I’ve always thought the fact that we couldn’t back test for TC was actually a good thing for the fund as it removed or reduced the possibility of introducing overfitting error into the MM.

---

### Post #3 — **wigglemuse** | 2023-11-15 06:48 UTC

Sounds basically right, yes. Confused about the multiplier a bit – if it is all one multiplier then means essentially no multiplier needed, right? (Or are you saying they’ll still be a 1x and a 2x?) In other words, the magnitude of the metric would just be set to whatever you thought correct and no multipliers needed (which are a weird thing – basically a hack – and confusing for newbies anyway). From what I remember the last version of MMC had a scaling factor that was supposed to make it about equivalent to corr (which then wasn’t adjusted when the target changed and mmc magnitudes went down by 10% so think about that.)

So as long as the math is right sounds good. There was that thing (that I was never quite convinced of but others were) that in negative corr environments you’d get bad mmc if you were too far away from the crowd (even if your corr was better than most) and therefore originality was being punished just at the time it was most needed. Hopefully we’ll have this up and running with enough time to see what it is like before staking? (With backfill hopefully? This should be way less expensive to calcuate than TC, eh?)

---

### Post #4 — **unsentient** | 2023-11-15 07:33 UTC

Another thought… removing “optional multipliers” seems to be the best of the coming changes… I did a little plotting and found that the current regime of “optional-multipliers” has not produced any meaning full change to the stake weighting of the MM.

Take a look at the top 10 stakes over the last year…

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/3/34a68680ba9ca0877814e9403bd19b828fd767ff_2_690x428.png)image1218×757 111 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/3/34a68680ba9ca0877814e9403bd19b828fd767ff.png> "image")

the whales have just been allowed to sit and take up space. They’re diluting good signal.

(also kudos to Mistreated for taking profits.)  
… and the code for anyone to play with…
    
    
    import pandas as pd
    import matplotlib.pyplot as plt
    from numerapi import NumerAPI
    napi = NumerAPI()
    
    list_of_usernames = ['crowdcent', 'atol', 'shatteredx', 'mistreated', 'efficient_meerkat', 'aininja', 'halsmith99', 'phorex', 'yoshiso','ummon']
    
    
    def get_account_profile_details(username, tournament=8):
        query = """
            query($tournament: Int!, $username: String!) {
              accountProfile(tournament: $tournament, username: $username) {
                totalStakeTs {
                  date
                  delta
                  time
                  value
                }
              }
            }
            """
        args = {'tournament': tournament, 'username': username}
        account_data = napi.raw_query(query, args)['data']['accountProfile']
        return account_data
    
    all_profiles = pd.DataFrame()
    
    for username in list_of_usernames:
        profile_data = get_account_profile_details(username, tournament=8)
        profile_totalStakeTs = profile_data['totalStakeTs']
    
        # Convert to DataFrame and process
        df = pd.DataFrame(profile_totalStakeTs)
        df['date'] = pd.to_datetime(df['date'])
        df.set_index('date', inplace=True)
        
        # Aggregate data
        all_profiles[username] = df['value']
    
    # Handle any missing dates
    all_profiles = all_profiles.fillna(method='ffill').astype('float')
    
    # Plotting the data
    plt.figure(figsize=(15, 10))
    for username in list_of_usernames:
        all_profiles[username].plot(label=username)
    
    plt.title('Account Values Over Time')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.legend()
    plt.show()

---

### Post #5 — **svendaj** | 2023-11-15 08:06 UTC

Excuse my Numeraic ignorance, but I was not around when MMC was used as payout multiplier. First to be sure: is it the same as current CWMM metric in dashboard? Second can you provide more reading links on evolution of MMC and how to optimize model MMC performance?

---

### Post #6 — **unsentient** | 2023-11-15 08:12 UTC

If we we’re to split the top 10 stakes into two groups – ones that beat the 1yr average and ones that did not – we see that it could still take a year or two for the competitive models to come to prominence. Numerai should be enforcing a high multiplier not a lowering it.

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/5/5b6ba37b2c0330ae1dcfde4a3f764654d3d79d7d_2_690x431.png)image1218×761 61.3 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/5/5b6ba37b2c0330ae1dcfde4a3f764654d3d79d7d.png> "image")
    
    
    columns_to_sum = ['crowdcent', 'atol', 'efficient_meerkat', 'ummon']
    all_profiles['lame_ducks'] = all_profiles[columns_to_sum].sum(axis=1)
    columns_to_sum = ['shatteredx', 'mistreated', 'aininja', 'halsmith99', 'phorex', 'yoshiso',]
    all_profiles['winners'] = all_profiles[columns_to_sum].sum(axis=1)
    
    plt.figure(figsize=(15, 10))
    for username in ['lame_ducks','winners']:
        all_profiles[username].plot(label=username)
    
    plt.title('Account Values Over Time')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.legend()
    plt.show() ```

---

### Post #7 — **unsentient** | 2023-11-15 08:57 UTC

The gap widens even more when you look at the top 20 stakes…

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/2/23b89f3abbe714107d74a77de9ae10d168d19c3d_2_690x431.png)image1218×762 57.3 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/2/23b89f3abbe714107d74a77de9ae10d168d19c3d.png> "image")

at present the top 20 stakes control 50.6% of the meta model. The 12 lame ducks control 38.8%  
The 8 winners control just 11.8%.

---

### Post #8 — **unsentient** | 2023-11-15 09:59 UTC

I went ahead and ran it for the top 50 stakes… I’d say that’s a pretty damn representative sample.

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/f/f5b10aeea26d46e052eb24751f0b3cef115b42b6_2_690x433.png)image1217×765 58.9 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/f/f5b10aeea26d46e052eb24751f0b3cef115b42b6.png> "image")

at present the top 50 stakes control 63.3% of the meta model. The 33 lame ducks control 48.7%. The 17 winners control just 14.7%.

I’m actually shocked at results… Half of the meta model is controlled by users that can’t figure out how to get in the 50th percentile!

look at the graph… It’ll take years for meta model to sort itself out!

my point is this… don’t keep cutting the payout multipliers. That would be a huge disappointment and bad for the fund. There’s one type of user that’s BIG problem for the fund… the ones with more money than sense. Why not just crank up and enforce a big multiplier? It doesn’t really matter what metric you use to score predictions… Corr, MMC, TC… what ever… halt of the meta model is controlled by people aren’t even coming close to hitting the mark.

Why not MMCx5? Why not x10? the multiplier and PF are two absolutely arbitrary coefficients and you let them control your MM’s learning rate?! I never got the payout factor… why let the public decide how fast or slow the stake weighted meta model adjusts its self?

---

### Post #9 — **sneaky** | 2023-11-15 10:00 UTC _(reply to #5)_

MMC != CWMM. MMC is well described here: <http://forum.numer.ai/t/mmc2-announcement/93>. MMC used to be calculated as performance of leave one (your model) out - performance of meta model. MMC2 is basically performance of your model’s residuals against the target.

---

### Post #10 — **svendaj** | 2023-11-15 11:16 UTC _(reply to #9)_

So MMC score is not calculated and published right now? How can we check our past MMC performance?

---

### Post #11 — **danzell** | 2023-11-15 11:20 UTC _(reply to #10)_

Lets hope MMC scores get backfilled soon ![:face_with_spiral_eyes:](http://forum.numer.ai/images/emoji/twitter/face_with_spiral_eyes.png?v=12)

---

### Post #12 — **sneaky** | 2023-11-15 11:37 UTC _(reply to #10)_

I think the idea is that you can calculate MMC on your own against the historical meta model predictions.

---

### Post #13 — **danzell** | 2023-11-15 11:40 UTC _(reply to #12)_

But I dont want to “reevaluate” all of my 100 models on my own. I would prefer Numerai to do just backfill and show MMC scores + no way to compare your MMC to other MMC scores without Numerai backfilling the metric.

---

### Post #14 — **sneaky** | 2023-11-15 11:48 UTC

I think this is going to backfire. You are changing the tournament from: “make models that predict the target” to: “retrain models every round to farm whatever residuum is left”. It is like doing gradient descent without momentum. IMO you should keep corr as part of the reward. If the models that are highly correlated with the target doesn’t help your fund, than it is the target fault.  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/e/e557e9997a52f7db560c0c13503fa383cca9be1e_2_690x180.jpeg)image1382×362 72.2 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/e/e557e9997a52f7db560c0c13503fa383cca9be1e.jpeg> "image")

---

### Post #15 — **wigglemuse** | 2023-11-15 17:04 UTC _(reply to #8)_

The magnitude of the risk is controlled by the magnitudes of the scores, i.e. the multiplier/scaling level, but again if there is only one level we don’t need that concept. Anyway, if the risk is too high relative to the probability of being positive each round (and by how much), then everybody is guaranteed to go bankrupt no matter how good their model is. This is a simple Kelly criterion calculation. If everyone is forced to “overbet” then we all go broke…mathematically guaranteed. (We can’t only focus on getting rid of bad performers – you can do that by getting rid of everybody. Good performers must be rewarded and not ground into dust also.)

---

### Post #16 — **wigglemuse** | 2023-11-15 17:33 UTC

The big danger with MMC only (and we discussed this a alot back in the MMC days the first time) is without a “center” of corr (or something absolute) the metamodel will just move around (in predictive space or whatever that would be called – the direction of the preditions) for no other reason than people are constantly moving their models around chasing the residuals since that is all there is. (Most likely it would oscillate between two or three main directions that match the inductive biases of the underlying models.) However, since the market is a moving target to begin with and it is all very complex, this dynamic is not quite guaranteed, we’ll just see. The old MMC tended to be just an extension/magnifier of whatever your corr was most of the time. It behaved nothing like TC – we’ll have to see on a new target.

But if it is a zero-sumish game, then it comes down to something like “you must be right at least 52% of the time” (or some X%). This is how sports bettors think – meet that that mark or else you’re losing. And if the math/magnitude of the scores and the risk controls we are offered are not worked out to be just right (if they even can be in such a crazy game) then there is definitely a danger of enforced losing for everybody – it will simply be impossible to make any reward except by luck in the short-term. (Time for an asymmetrical score perhaps?)

So far they have stubbornly refused to give us any real risk controls (i.e. stake management, which Richard explicitly refused in the last fireside) and of course automatic compounding is great if you’re winning, but it is also an excellent way to drive you straight into that overbetting zone where you are guaranteed to lose. (AGAIN, even with a good model! Overbetting kills everybody – good and bad.)

So while I’m actually cautiously optimistic that this general idea _can_ be made to work…well their track record of thinking these things through is unfortunately undeniably at this point…not great. And they always seem to be in a mad rush to implement the new thing and dump the old thing before we can really tell how it is going to go. Like…why not actually see how it goes instead of just jumping off the cliff and hoping? (_EVERY_ policy has its price and its unintended consequences – we could all 100% agree that “whatever plan” sounds great and the math is perfect, etc and it still has some fatal flaw nobody thought of but is easily seen in practice…if you only give it some time in practice to find out (before totally abandoning the old thing). Too many nasty rug pulls and there just won’t be anybody left…and we’ve already had one or maybe two this year depending on how you count them…

---

### Post #17 — **mantz** | 2023-11-15 19:33 UTC _(reply to #1)_

Numerai will no longer make payouts based on CORR or TC, all payouts will be on MMC only on a new upcoming target called Teager **starting the end of this year**.

With this you mean that the scoring system will change to a new target with a “new-old” metric in the next month? or just that the new target will be released?

I think that some overlap is needed to let people adjust or create new models. If lots of people unstake their models not because they are performing bad, but because they don’t know how are they going to perform, that could be very dangerous for the MM performance.

---

### Post #18 — **gammarat** | 2023-11-15 22:01 UTC _(reply to #16)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/wigglemuse/48/3094_2.png) wigglemuse:

> well their track record of thinking these things through is unfortunately undeniably at this point…not great.

The approach does feel disappointingly haphazard and _ad hoc_. If Numerai and @richardai want longer term commitments (as stated in the linked video), I think they can foster that by acheiving greatere stability in the way the competitions are organized.

For example, several months before introducing a substantial change, perhaps Numerai could open a third competition–let’s call it Playground (to go with Classic and Signals)–where everyone recognizes that things could change quickly, and there would be no staking. Just some gold stars for consistent participation, or maybe some credits to apply to the staked competitions.

The purpose would be to provide an area where there really isn’t any risk, so Numerai could beta test their ideas and competitors could get a handle on what they need to do to compete in the Tournament given a proposed update. Then if Numerai finds that the Playground results are leaning towards an improvement in the Tournament, and the bugs have been worked out, then switching that into the main Tournament would be easy.

And when their are no proposed updates, just let the Playground run under the the same process as the Tournament, but without staking.

---

### Post #19 — **bridgeface** | 2023-11-16 18:33 UTC

[![Screenshot 2023-11-16 122651-3](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/5/5415bd8f010b399ce8a173f273d4e3f6f3547184_2_460x500.jpeg)Screenshot 2023-11-16 122651-3666×723 55.6 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/5/5415bd8f010b399ce8a173f273d4e3f6f3547184.jpeg> "Screenshot 2023-11-16 122651-3")

My Numerai Tourney experience lately.  
Sometimes you eat the Bear, sometimes the Bear eats you.

---

### Post #20 — **nasdaqjockey** | 2023-11-16 21:17 UTC

So if we are now going to have a new Target and MMC to evaluate our predictions, how do I calculate MMC?

---

### Post #21 — **liborty** | 2023-11-16 23:33 UTC

Your fund is performing poorly compared to the metrics? I would be very surprised if it was otherwise. This is the Representation Problem: whatever metrics you may design and model, the unpredictable markets will always end up being worse for you. This goes against your core belief, more of an unfounded ‘chartist’ hype really, that you can make money with trading robots. (In other ways than instantaneous reactions to data that the suckers out there have not even seen yet). So you struggle on, fiddling endlessly with the metrics. “Let us just adjust the numerous ‘targets’ again and everything will be good”.

Moving onto a concrete question. I have TC= 0.0104 and CORRV2=0.0058 but negative  
CWMM=-0.0175. Am I going to be penalised by these changes, or am I going to benefit?

---

### Post #22 — **cataclanca** | 2023-11-17 16:48 UTC

![giphy](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/1/1f08e46648b79c7f9dc228f121c2228ddb6e39f4.gif)

Best regards for everyone!

---

### Post #23 — **edubergeek** | 2023-11-20 19:44 UTC

1. What current target best approximates the new “teager” target?
  2. When will we see our CWMM rank in the tournament?

---

### Post #25 — **martinshkreli** | 2023-11-22 04:01 UTC

Anyone have a quick code snippet to test, just for example, the MMC of example preds? I’ve tried using the new contributive_correlation function but am not quite sure I’m doing it right.

---

### Post #26 — **selowan** | 2023-11-22 10:34 UTC

As long as we’re able to accurately test our models with MMC internally, this should be a great change.

---

### Post #27 — **minou** | 2023-11-22 11:16 UTC _(reply to #18)_

I don’t think it’s a coincidence that things started to go down hill for numerai and the fund when they introduced new datasets and tinkered with scoring earlier in the year. They appear to have been scrambling and floundering ever since to pick things up again, but to no avail and the detriment of the competition as a whole. I can’t help but wonder how the fund and competition would be doing if they had simply left well alone this year and kept things stable, and if a burgeoning fear of standing still and stagnating gave rise to an irresistible urge to experiment that couldn’t be avoided, by all means introduce a new higher risk fund, more targets and datasets to see how that would work out, but keep what was already working well. Changing multiple aspects of the competition at the same time seems highly problematic; if there is a well founded hypothesis that scoring on MMC will improve fund performance, make the change, but don’t change anything else and let it run for 6 months to a year. If there’s another idea, do that in a separate experiment and run in parallel. But if scoring, targets and probably features are changed all at the same time, how can you know what really works and makes a difference.

---

### Post #28 — **kenfus** | 2023-11-26 19:05 UTC _(reply to #22)_

I don’t think no Corr is good. What about only corr and mmc? Without corr, the goal is to maximize MMC. Is maximizing MMC, even on the new target, really in the best interest of the fund? You could also fix the multiplier to have at least 1x corr and 1x mmc, so that nobody can ignore and just focus on something.

---

### Post #29 — **nasdaqjockey** | 2023-11-26 20:53 UTC

When we get the new target at the end of the month will we also get new diagnostics?

---

### Post #30 — **wigglemuse** | 2023-11-26 23:01 UTC _(reply to #29)_

Sounds like we are sticking with Cyrus for scoring. (re ark in discord)

---

### Post #31 — **anthill** | 2023-11-29 05:36 UTC _(reply to #27)_

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/m/bcef8e/48.png) minou:

> I don’t think it’s a coincidence that things started to go down hill for numerai and the fund when they introduced new datasets and tinkered with scoring earlier in the year.

This is possible, but personally I am more suspicious that the sudden drop in performance also correlates with the sudden rise in interest rates. Our training data comes from a period of time where interest rates were very low and it’s not clear that the strategies we have developed that worked well in that era will continue to work in this new environment.

But I agree with the broader point — if you change a lot of things too quickly it’s very hard to work out what actually had an impact. Maybe it’s interest rates, or maybe it was changing the dataset, or maybe it was changing the metrics. Since everything got changed in quick succession it’s hard to know.
