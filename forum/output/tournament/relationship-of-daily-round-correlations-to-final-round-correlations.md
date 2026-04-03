---
title: "Relationship of daily round correlations to final round correlations"
category: Tournament
url: https://forum.numer.ai/t/relationship-of-daily-round-correlations-to-final-round-correlations/1176
created_at: 2020-11-12T02:25:55.646000+00:00
last_posted_at: 2022-06-29T18:39:03.028000+00:00
posts_count: 48
views: 6158
tags: []
---

# Relationship of daily round correlations to final round correlations

---

### Post #1 — **mugamma** | 2020-11-12 02:25 UTC

Is the relationship between the daily round correlations and the final submission correlations documented anywhere? I’ve noticed that the last daily correlation of a submission seems to always match with the submission’s correlation. This makes me curious what we are watching in the charts for individual rounds.

Related question and part of why I was looking at the daily round correlations - why don’t recent rounds have correlations in the API any more?

---

### Post #2 — **wigglemuse** | 2020-11-13 00:55 UTC

The first part of your question is unclear to me, but it sounds like you may have a misunderstanding of what the scores mean. In any case, can you re-phrase or give an example so we are sure what you are talking about?

And as far as the API, again not sure what you are referring to? (I pull the scores from the API every day no problem. We are talking about the Numerai tournament, not signals, right?)

---

### Post #3 — **mugamma** | 2020-11-13 01:33 UTC

Re: the first question, look at these screenshots from [Numerai](<https://numer.ai/integration_test>) . The first shows the current correlations of the last 8 rounds. Then the next 8 switch to the round view, and the most recent date always matches the correlation from the first screenshot. I’ve noticed this on my models and a few others that I spot checked, so it doesn’t seem like an accident that the most recent date and the submission correlation match.

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/7cbc83adc52dbaf77faa219fb5a03f556ea6b310_2_333x500.png)image570×854 33.6 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/7cbc83adc52dbaf77faa219fb5a03f556ea6b310.png> "image")

Round 237:  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/abab3cda1855db8ad03562d036ec40143a3bab0a_2_690x85.png)image1054×130 5.84 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/abab3cda1855db8ad03562d036ec40143a3bab0a.png> "image")

Round 236:  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/e53d3de962090ed89ac91c9a0f8366c349148b93_2_690x236.png)image1026×352 14.1 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/e53d3de962090ed89ac91c9a0f8366c349148b93.png> "image")

Round 235:  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/fe4febe347a4c0a8241f4beb820b8c065ecf5f33_2_690x247.png)image1016×364 14.9 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/fe4febe347a4c0a8241f4beb820b8c065ecf5f33.png> "image")

Round 234:  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/82fd0dae078a56e134e655ade69d49916f1b87c4_2_690x243.png)image1052×372 16 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/82fd0dae078a56e134e655ade69d49916f1b87c4.png> "image")

Round 233:  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/16d06ea668cef9d1c49ebf0ac88e4d45e7a0db43_2_690x256.png)image1016×378 14.6 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/16d06ea668cef9d1c49ebf0ac88e4d45e7a0db43.png> "image")

Round 232:  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/d90c4e8bca8193012ab802ce950aaeb00dcd6c3c_2_690x233.png)image1064×360 14.8 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/d90c4e8bca8193012ab802ce950aaeb00dcd6c3c.png> "image")

Round 231:  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/786ff05a9be4084e8737111018b8aee39472b4b0_2_690x246.png)image1008×360 15.1 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/786ff05a9be4084e8737111018b8aee39472b4b0.png> "image")

Round 230:  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/6484dcffa6e8911fd822aab090218d4296134b8c_2_690x231.png)image1044×350 15.6 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/6484dcffa6e8911fd822aab090218d4296134b8c.png> "image")

---

### Post #4 — **mugamma** | 2020-11-13 01:42 UTC

For the second question, this code in Colab outputs a list of round/correlation pairs, but the correlations are all None from round185.
    
    
    napi = numerapi.NumerAPI(public_id=public_id, secret_key=secret_key)
    sorted([(r["roundNumber"], r["submission"]["liveCorrelation"]) for r in napi.get_user_activities("integration_test")])
    

returns
    
    
    [(168, -0.033684549296499416),
     (169, -0.05988718140443864),
     (170, -0.0553602620696002),
     (171, -0.049266679898113),
     (172, -0.03630719909101644),
     (173, 0.025985500504023682),
     (174, 0.019309163665860288),
     (175, 0.017878789613636287),
     (176, 0.024122615017301122),
     (177, -0.010733890025773116),
     (178, -0.04190927753899791),
     (179, 0.0073781890375614724),
     (180, 0.0015480821870788558),
     (181, 0.008458966549655554),
     (182, 0.0553799401902486),
     (183, 0.04973214110776211),
     (184, 0.053386781798264636),
     (185, None),
     (186, None),
     (187, None),
     (188, None),
     (189, None),
     (190, None),
     (191, None),
     (192, None),
     (193, None),
     (194, None),
     (195, None),
     (196, None),
     (197, None),
     (198, None),
     (199, None),
     (200, None),
     (201, None),
     (202, None),
     (203, None),
     (204, None),
     (205, None),
     (206, None),
     (207, None),
     (208, None),
     (209, None),
     (210, None),
     (211, None),
     (212, None),
     (213, None),
     (214, None),
     (215, None),
     (216, None),
     (217, None),
     (218, None),
     (219, None),
     (220, None),
     (221, None),
     (222, None),
     (223, None),
     (224, None),
     (225, None),
     (226, None),
     (227, None),
     (228, None),
     (229, None),
     (230, None),
     (231, None),
     (232, None),
     (233, None),
     (234, None),
     (235, None),
     (236, None),
     (237, None)]

---

### Post #5 — **wigglemuse** | 2020-11-13 02:32 UTC _(reply to #4)_

I can’t answer your API question exactly, but that must be a deprecated field you’re pulling. (I get correlations from v2RoundDetails but I don’t use numerAPI – might want to ask that in the rocketchat “api” channel.)

As to the first question, it does seem like you’ve got a fundamental misunderstanding there because of course they match – the most recent daily score and what you are calling the “submission’s correlation” are the same thing. The daily scores you see on the “round” dropdown for each round are snapshots in time of that day. They are not cumulative or anything like that. Each day your predictions are compared to the live results as they stand on that day (which is actually a lag of 2 days from the live stock market, but that’s another complication). So only the last day of the round when it “resolves” (i.e. the 20th score after 4 weeks) actually means anything – that’s the day you are scored on for payment. All the other days are just something to look at in the meantime. So for each round you have 19 scores and “payouts” that tell you WHAT YOU WOULD HAVE GOTTEN FOR THAT ROUND _IF_ THAT ROUND HAD ENDED ON THAT DAY. Of course it didn’t end on any of those days, so again they are just something to look at and follow along with as the round progresses. Only the final 20th day means anything. And so that explains why the most recent score is always listed on the “submission” page – the submission page is simply the summary of your final scores (for all rounds except the most recent 4) and also in-progress scores on the 4 most recent rounds (which are open, not resolved, except on Wednesdays which is the last day of a round then the 4th one back is a final score for that round).

SO… exactly one score per week actually is final (i.e. is the only one that counts for real payment or burn) – this week it was yesterday’s (Nov 11) score for round 233 as that is the round that finished/resolved this week. And then today (Nov 12) we got a score for round 237 for the first time and so rounds 234-237 are currently open and still in-progress.

Starting to make sense?

---

### Post #6 — **mugamma** | 2020-11-13 03:27 UTC _(reply to #5)_

This is exactly why I asked if there was documentation!

![](http://forum.numer.ai/user_avatar/forum.numer.ai/wigglemuse/48/3094_2.png) wigglemuse:

> As to the first question, it does seem like you’ve got a fundamental misunderstanding there because of course they match – the most recent daily score and what you are calling the “submission’s correlation” are the same thing.

This was actually my understanding before posting, but I wanted to get official (or veteran) confirmation of that understanding. Just looking at the round charts, it is very easy to assume that those are the correlations of that round on that day’s data. Because the label is “correlation”, not “correlation update”, “correlation so far”, “cumulative correlation” or “correlation snapshot”. I looked at those charts for months before realizing I was reading them wrong.

The closest thing I found to a definition in the official docs is just “Each submission will receive daily updated scores starting from the first Thursday after the submission deadline to the Wednesday 4 weeks after.” and “But only your final score and final payout will count.” The latter nixes the naive interpretation just looking at the official chart labels, but does not say how the intermediate updates are calculated. Two obvious candidates to me are calculating over resolved days, and assuming zeros for unresolved days. The former seems a little more intuitive to me.

---

### Post #7 — **wigglemuse** | 2020-11-13 03:38 UTC _(reply to #6)_

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/m/c57346/48.png) mugamma:

> Just looking at the round charts, it is very easy to assume that those are the correlations of that round on that day’s data.

So just clarifying – that’s exactly what it is. The correlation of your predictions to the state of the market on that day (with 2 day lag from the real life market – Wednesday scores are from Monday’s market, etc). It is just that if it isn’t the final day of the round, that day doesn’t mean anything. When figuring final scores, your intermediate daily scores don’t enter in that calculation whatsoever – again they are just there to look at, nothing else. It used to be we got a single score for each round after waiting a month and having zero idea how the round was shaping up. So that made people crazy with anticipation and now we’ve got something to pass the days. But still, the only score that matters each week is that final score on Wednesday for the 4th most recent round.

---

### Post #8 — **mugamma** | 2020-11-13 04:17 UTC _(reply to #7)_

Ah, that’s where I got confused. The daily labels tricked me into thinking some of the round was resolving early (i.e. not everything was predicting four weeks out). The updates are more “pretend we resolved the same bets early”. I guess some predictions could be less than four weeks long, but not a helpful way to think about it now. Thanks!

---

### Post #9 — **wigglemuse** | 2020-11-13 14:07 UTC _(reply to #8)_

Yes, correct. I’m not sure we’ve ever got a definitive answer on whether anything is actually resolved before the final date, but it doesn’t seem like it. “Pretend it is all resolved” each day before the final day is exactly right – it is just pretend until the final day. Usually your scores track and what you are getting in the final week is pretty close to what you are going to end up with, but not always. Just this week there was a big change for many on the final day as it corresponded with huge market shift on Monday (vaccine announcement, I think). So there is a component of luck there too…

---

### Post #10 — **jrai** | 2020-11-13 20:17 UTC

I don’t believe daily scores are indicative of your final _resolved_ score until at least the 15th day (3rd week) of each 20 day (4 week) round. In fact, I think we put way too much weight into daily scores. Here’s my unscientific analysis to answer the question:

This chart shows a different line for every round. The y-axis shows how far each day’s score is from the final score your model gets on that round. The x-axis shows which day of the round you’re on. On the final day of the round, each round’s lines converges to 0 because that is your final score! The dashed line is the average distance for each day over all rounds. Although the average distance of daily scores from final scores over time looks to be 0, that’s only because it’s completely random whether or not my daily scores are higher or lower than what my final score will be.  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/5cf9ec3b3029f81ec896c0d11b969a80d46c0758_2_690x299.png)image859×373 156 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/5cf9ec3b3029f81ec896c0d11b969a80d46c0758.png> "image")

What’s more important is the absolute value of the difference in your distance from your final day score, which looks like this chart below. Clearly, it’s downward sloping. What this tells me is that on the first day of every round, my daily score will be ~0.03 correlation points away from my final score. It’s not until roughly the 15th day that my daily scores are within 0.01 correlation points of my final score. In some cases, even on the 15th day, my daily score can be as much as 0.04 points away from my final score.  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/67f0d4d5e166610969bb4b4311c39e23e9d5c19a.png)image631×338 140 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/67f0d4d5e166610969bb4b4311c39e23e9d5c19a.png> "image")

And here’s the code if you’d like to check your own models’ “consistencies.” I’ve found most models exhibit the same behavior, though. There is likely something interesting to be found in different models’ changes over daily scores. The same analysis can be done for mmc by changing all references to “correlation” to “mmc”:
    
    
    napi = numerapi.NumerAPI()
    df = pd.DataFrame(napi.daily_submissions_performances("jrai")).set_index("date")
    df = df[df["roundNumber"] < 233]
    
    df["distance"] = (
        df["correlation"] - df.groupby("roundNumber")["correlation"].transform("last")
    ).values
    
    df = (
        df.groupby("roundNumber")
        .apply(lambda x: x.reset_index(drop=True))
        .drop("roundNumber", axis=1)
        .reset_index()
    )
    
    #plot distances
    df.set_index("level_1").pivot(columns="roundNumber", values="distance").plot(
        figsize=(10, 5), title="Daily Scoring Distance from Final Day Score"
    )
    
    df.groupby("level_1").mean().distance.plot(style="k--")
    
    plt.xlim(0, 20)
    plt.legend(bbox_to_anchor=(1.4, 1), loc="upper right", ncol=3)
    plt.ylabel("Distance from Final Day Score")
    plt.xlabel("Days into Round")
    plt.figure()
    
    #plot absolute distances
    df.abs().set_index("level_1").pivot(columns="roundNumber", values="distance").plot(
        figsize=(10, 5), title="Daily Scoring Absolute Distance from Final Day Score"
    )
    
    df.abs().groupby("level_1").median().distance.plot(style="k--", legend=None)
    
    plt.xlim(0, 20)
    plt.ylabel("Distance from Final Day Score")
    plt.legend(bbox_to_anchor=(2, 1), loc="upper right", ncol=3)
    
    plt.xlabel("Days into Round")
    plt.figure()
    

Edit: I just realized that the absolute distance graph is actually showing the median distance, which might be a better measure than mean distance anyway. I was switching between mean/median and forgot to switch it back. Change any reference between “.median()” and “.mean()” to see the differences.

---

### Post #11 — **bor1** | 2020-11-16 07:07 UTC _(reply to #10)_

Thanks [@jrai](</u/jrai>), great stuff! A related question to the usefulness of the daily scores you might know the answer to:

_how reliable is the qualitative difference in daily score between two models submitted in the same week? (i.e. is model X that looked better than model Y in week 1, indeed better than model Y at round resolution)_. Do you happen to have an analysis/intuition on that as well?

The above question makes sense under the assumption that Model X and Y are models that are build in compatible ways and with compatible aims (basically hyperparameter tuning), i.e. not a P 1-P model kind of model :-).

---

### Post #12 — **profricecake** | 2021-03-07 21:19 UTC _(reply to #5)_

Hi all -

As a relative Numerai newcomer I’ve been trying to understand the daily scores as well.  
Based on the limited docs, the posts in this thread, and my own explorations, I have another interpretation that I thought I’d share here for discussion.

Note I’ve only really considered the daily corr score in this post, but I suspect that mmc follows similar logic.

To my mind, easiest way to explain why the daily score converges on the final score (as per the plot from [@jrai](</u/jrai>)) is that they _are_ indeed cumulative. In other words, the daily corr score for day N is the mean daily corr between each day’s predictions and that same day’s actual targets, averaged across N days.

This interpretation goes against the following claim from [@wigglemuse](</u/wigglemuse>):

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/numerai.discourse.group/wigglemuse/48/3094_2.png) wigglemuse:

> They are not cumulative or anything like that.

But actually jibes with their emphatic later claim:

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/numerai.discourse.group/wigglemuse/48/3094_2.png) wigglemuse:

> So for each round you have 19 scores and “payouts” that tell you WHAT YOU WOULD HAVE GOTTEN FOR THAT ROUND _IF_ THAT ROUND HAD ENDED ON THAT DAY.

There’s a logical basis behind this interpretation of the daily scores. If there are 20 days in a competition round, why would Numerai reward only the last day’s performance? It makes more sense to reward overall performance across the full 20 days, which suggests that the daily score on the last day–aka the final score–somehow includes contributions from the daily scores of all days. This and the observed convergence of the daily score to the final score all seem to point to the daily scores indeed being cumulative.

Assuming my interpretation is true, I wrote some code to extract daily corr values from these cumulative daily scores. On day 1, the daily corr score would actually be day 1’s mean corr since there is only one day of data available. But day 2’s daily score = (day 1 corr mean + day 2 corr mean) / 2. Solve this equation for day 2 corr mean and iterate across the remaining days and you can extract the mean corr for each day in the round.

Below is a plot of the daily scores for the 4 most recent completed rounds for the [@benchmark_models](</u/benchmark_models>) model. I have not centered them on the final score as was done in [@jrai](</u/jrai>)’s plot.

[![Screen Shot 2021-03-07 at 12.54.26 PM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/a40c2199299955c88d068dadb53eac12bb2dd733_2_690x291.png)Screen Shot 2021-03-07 at 12.54.26 PM895×378 35.7 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/a40c2199299955c88d068dadb53eac12bb2dd733.png> "Screen Shot 2021-03-07 at 12.54.26 PM")

Here is a plot of what I suspect are the daily corrs for this model, extracted using the approach outlined above:

[![Screen Shot 2021-03-07 at 12.54.55 PM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/acbd303749b02f7a382c5a60ea23b3e2b9872072_2_690x291.png)Screen Shot 2021-03-07 at 12.54.55 PM895×378 47.2 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/acbd303749b02f7a382c5a60ea23b3e2b9872072.png> "Screen Shot 2021-03-07 at 12.54.55 PM")

A few things to note:

  * The daily corr values range roughly between -0.2 and 0.2 for this particular model.
  * If this model hasn’t changed across these 4 rounds (which is the assumption given that it submits the example predictions) and if my interpretation and math are correct, then Numerai must use somewhat different data to evaluate each model on a given day in a given round since the daily corr values are not identical.
  * Diving deeper into the previous conclusion, there is likely some overlap in the data used to evaluate the models on a given date since so many appear to make correlated moves - aka notice how often the direction of the daily change (positive or negative) is consistent across rounds.



If this interpretation of the daily score is accurate, aka that it is a cumulative mean score across all of the finished days of a given round, users could use this daily corr extraction process to understand a little better how their models perform in the wild. They could compute their own daily mean and sharpe values from these live results thereby getting better metric data than is currently available from the end-of-round numbers and the metrics computed upon model upload.

Of course this might all be wrong so I’d love to hear what you all think.

Whether or not I’m right or wrong I have a suggestion for Numerai: you provide us with a dashboard of information to help us understand how our models are doing. Daily scores are a big part of that information. Given the ongoing confusion about what these daily scores actually are, please consider updating the documentation with an unambiguous definition! I was unable to find one.

Cheers,

PRC

---

### Post #13 — **wigglemuse** | 2021-03-07 21:33 UTC _(reply to #12)_

I’m afraid not. They are not cumulative – at all. This has been asked directly to the team and answered unambiguously (since I posted about it above). I could even find it for you on video if you give me some time. The intermediate days have no bearing on your score. Another way to put this is if we had two alternative universes and the market snapshot was identical on the final day of scoring but the intermediate days were all completely different, would you get the same score? YES. Do they even need to have the intermediate market data to calculate your score? NO. _**Only the last day matters**_

As far as the docs, I’m right now working on a comprehensive FAQ and other materials that answer all these common questions and confusions. Hoping to the get the first part of it up today, but annoying things keep happening in my house the last couple weeks to delay me. (Watch this section: [Understanding Numerai - Numerai Tournament](<https://docs.numer.ai/community-content/understanding-numerai>))

---

### Post #14 — **profricecake** | 2021-03-07 22:31 UTC _(reply to #13)_

Thanks for your input. Would be interested in seeing the video. Would be more interested in seeing the Numerai folks answer these basic questions in the docs instead of having generous users like you have to assemble an FAQ. If these Qs are FA, after all, then it’s probably a sign that the documentation is lacking.

Also: do you have any theories about why the daily score converges towards the final score if what you say is true about the intervening days not mattering?

---

### Post #15 — **wigglemuse** | 2021-03-07 22:43 UTC _(reply to #14)_

As far as the docs, they kind of enlisted me for that, so me making an FAQ is in part their action and in part mine (and is hosted on their site). So they did recognize the need.

Why do the scores converge? Because each daily score is generated from a snapshot of a market day, and any given market day is most likely going to be pretty similar to the day before it unless there was a major market shock. And so the score of the day prior to the final day is most likely gonna be closer to the final day score than the day before it, and so on. The farther back in time you go, the less likely you are to be sitting on the final day score. That is all the graph is showing. You _always_ end up with the final score after all – just because it is the final score.

---

### Post #16 — **profricecake** | 2021-03-08 05:57 UTC _(reply to #15)_

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/numerai.discourse.group/wigglemuse/48/3094_2.png) wigglemuse:

> Why do the scores converge? Because each daily score is generated from a snapshot of a market day, and any given market day is most likely going to be pretty similar to the day before it unless there was a major market shock. And so the score of the day prior to the final day is most likely gonna be closer to the final day score than the day before it, and so on. The farther back in time you go, the less likely you are to be sitting on the final day score. That is all the graph is showing. You _always_ end up with the final score after all – just because it is the final score.

This would indeed explain convergence towards the final score.

However, if it is true that the differences between consecutive daily scores are the result of typical daily market variation and not the averaging that I proposed, then we would expect to see statistically similar average variation between any two consecutive daily tournament scores.

In other words, if your explanation is true, then the market delta between days 19 and 20 of a tournament are not “special” aka they should not be statistically different from the delta between days 1 and 2 or any two consecutive days for that matter, barring the major market shocks you reference (and perhaps other issues like weekend breaks and so on).

Luckily, we have plenty of data to consider to investigate this. I took all 82 completed rounds of [@benchmark_models](</u/benchmark_models>) and computed the daily score change. Here is a plot of the standard deviation of that change per tournament day over all 82 rounds.

[![Screen Shot 2021-03-07 at 9.27.03 PM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/ab6371fb442a09a3eb60db168ab11b62822f6d9d.png)Screen Shot 2021-03-07 at 9.27.03 PM392×292 13.9 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/ab6371fb442a09a3eb60db168ab11b62822f6d9d.png> "Screen Shot 2021-03-07 at 9.27.03 PM")

This appears to counter your claim that the change between the last two daily score corr values is due solely to daily market movement, unless magically the market moves less on the final days of a Numerai tournament than it does on the starting days. Which of course it doesn’t.

Below is a plot where I generated 82 Gaussian-distributed fake “daily corr” values and computed the daily difference between them, then plotted the std of those differences. It comes out much more like what I’d expect from the daily scores if what you wrote was true, namely, that the delta between consecutive daily scores has nothing to do with the tournament day and is more of a measure of typical daily market movement.

[![Screen Shot 2021-03-07 at 9.27.12 PM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/a9b13220a00df68536ab2573213f90c5b13accb0.png)Screen Shot 2021-03-07 at 9.27.12 PM392×292 13.3 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/a9b13220a00df68536ab2573213f90c5b13accb0.png> "Screen Shot 2021-03-07 at 9.27.12 PM")

So just to re-make my case, since your explanation for the convergence isn’t explained by the data, here is a plot where I took 82 rounds of Gaussian-distributed fake “daily corr” values and averaged them over each day, aka, I’m simulating what I proposed in my post about what I think the daily scores might really represent. You’ll see an std curve that gets lower over the course of the tournament, as we saw in the first plot, and as one would expect if the convergence is due to temporal averaging rather than daily market movement.

[![Screen Shot 2021-03-07 at 9.27.20 PM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/566c9c02a904376e287bcab15710fb713a778af8.png)Screen Shot 2021-03-07 at 9.27.20 PM392×292 13.5 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/566c9c02a904376e287bcab15710fb713a778af8.png> "Screen Shot 2021-03-07 at 9.27.20 PM")

In the spirit of getting to the bottom of this, there is at least one explanation that would reconcile both the convergence over time towards the final score, the ever-shrinking std of the daily scores, and your belief that the score on the final day is truly independent of the scores on the previous days.

That explanation is this: each model is evaluated using 20 different days worth of data. On day 1 of a tournament, only _some_ of day 1’s live data is used to compute the corr, the rest is embargoed for later use. On day 2, only _some_ of day 2’s live data is used (and the average is computed between days 1 and 2 and presented as the daily score). This continues until the final day when all the previously-embargoed live data is folded in to one big final score calculation. The idea here is that the model performs similarly enough on the separate chunks of each day’s data that the daily scores are predictive/indicative of the final score, but the final score is also truly independent of the prior scores.

Obviously enough data could be embargoed that each day’s score could be computed the same way (aka, day 2’s cumulative score includes embargoed data from day 1 and some from day 2) thus keeping all daily scores truly independent of each other.

Maybe this is it, maybe not. Regardless, I hope you see why I’m not ready to accept your explanation for the convergence. It’s simply not supported by the evidence. So I’ll re-state my desire to have Numerai officials give us the real answer, or tell us why they won’t and thus keep this investigation going!

---

### Post #17 — **mugamma** | 2021-03-09 04:30 UTC _(reply to #16)_

Since I originally asked this question, this has come up a number of times in Rocket Chat without correction by the team, and [@wigglemuse](</u/wigglemuse>) satisfied me earlier that I was misinterpreting what was going on.

Specifically in regards to what you said here,

![](http://forum.numer.ai/user_avatar/forum.numer.ai/profricecake/48/2528_2.png) profricecake:

> In other words, if your explanation is true, then the market delta between days 19 and 20 of a tournament are not “special” aka they should not be statistically different from the delta between days 1 and 2 or any two consecutive days for that matter, barring the major market shocks you reference (and perhaps other issues like weekend breaks and so on).

I am confident that this is incorrect. It might be correct if the hedge fund was only looking at stock prices. However, it does not work if any derivatives with expiration dates are involved. For options specifically, the premium baked into the price will vary based on the time remaining before they expire, and will tend to get smaller as the options get closer to the expiration date. I think that by itself will lead to the smaller price movements and lower daily variation leading to the decreasing trend you see.

---

### Post #18 — **profricecake** | 2021-03-09 06:12 UTC _(reply to #17)_

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/m/c57346/48.png) mugamma:

> I am confident that this is incorrect. It might be correct if the hedge fund was only looking at stock prices. However, it does not work if any derivatives with expiration dates are involved. For options specifically, the premium baked into the price will vary based on the time remaining before they expire, and will tend to get smaller as the options get closer to the expiration date. I think that by itself will lead to the smaller price movements and lower daily variation leading to the decreasing trend you see.

Thanks for raising this possibility. Varying expiration dates of certain financial instruments could certainly explain a wider variance in the daily market deltas than I included in my simple simulation.

I’m not ready to accept “it does not work if any derivatives with expiration dates are involved” because after all, if a small percentage of the fund’s holding are in expiring derivatives they wouldn’t move the needle very much.

But let’s assume for a moment that fund is exclusively built from these kinds of expiring instruments. And since we observe steady convergence in every round even though rounds X and X+1 overlap for 15 days, I believe this also would imply that each tournament round must have its own independent holdings that expire during said round.

Yours is certainly a viable theory when combined with assumptions like this about the nature of the fund’s holdings. Perhaps those assumptions are why the Numerai team isn’t chiming in to answer this question about the daily scores, but I’ll still continue the plea. Courtesy of the [The humans of Numerai](<http://forum.numer.ai/t/the-humans-of-numerai/54>) thread, I’m calling out some Numerai staff explicitly here, wondering if [@slyfox](</u/slyfox>), [@master_key](</u/master_key>), [@mdo](</u/mdo>), or [@son_sioux](</u/son_sioux>) could offer more insight and/or help us rectify some of the contradictory theories that have appeared in this thread.

What remains clear is that the early daily scores are not very predictive of the final score. Just look at [@jrai](</u/jrai>)’s original plot. So why are they presented to us at all? What kind of value are we supposed to get from them if they have no bearing on the final score as some have claimed, and (as of yet) no unambiguous meaning? I would hope the staff could offer a “safe” answer to that question that does not expose information about the fund’s internal operation. I mean, if you’re going to put a speedometer on the car, please let us drivers know how to read it. Or maybe just add some error bars based on the tournament day so that we know how much faith to put into those scores.

Thanks, all, for your continued input!

---

### Post #19 — **mugamma** | 2021-03-09 12:15 UTC _(reply to #18)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/profricecake/48/2528_2.png) profricecake:

> So why are they presented to us at all?

Because the previous setup we had zero feedback for 4 weeks. This is better than that.

---

### Post #20 — **minou** | 2021-03-09 13:17 UTC _(reply to #18)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/profricecake/48/2528_2.png) profricecake:

> What remains clear is that the early daily scores are not very predictive of the final score

Given that we are aiming to predict the state of play for 4 weeks time and not for every day leading up to that point, is there any reason why we _would_ expect early scores to be indicative of the outcome? The day that’s most likely to look like the final one in the markets relative to the starting point is the one before, and the further away from the goal you go, the more discrepancy there would inevitably be. Or am I missing something with this reasoning (which I accept is entirely possible!)

---

### Post #21 — **wigglemuse** | 2021-03-09 14:49 UTC _(reply to #16)_

Could maybe be just because they are predictions, and we are looking at models that did fairly well (although NO models ever really get high correlations). Be interesting to check on random models.

But please let’s quit with the idea that the team is hiding something or there is big conspiracy. I ASKED THEM THESE EXACT QUESTIONS and Richard directly answered them (and you can go watch it). There has been no evasion on this topic whatsoever. It has always been stated that we are predicting the market 4 weeks hence but since this question gets talked about sometimes I just wanted to clarify with the team that nothing that happens in the intermediate days could affect the score. And he did confirm that. So the question is pretty much settled – we are predicting 4 weeks hence exactly as they always said. The only confusion brought into this is really by users that wondered if that was strictly true. Turns out it is. They’ve been 100% open about it – nobody ever directly asked them before and when I did, Richard answered me.

I mean, I guess he could be straight up lying, or he doesn’t actually know how it works, or there is a bug and our scores have been wrong since forever – all technically in the realm of possibility I suppose. But come on…

---

### Post #22 — **jrai** | 2021-03-09 15:01 UTC _(reply to #18)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/profricecake/48/2528_2.png) profricecake:

> This appears to counter your claim that the change between the last two daily score corr values is due solely to daily market movement, unless magically the market moves less on the final days of a Numerai tournament than it does on the starting days. Which of course it doesn’t.

Since we are predicting what the market will look like only on day 20, it could stand to reason that, as the round progresses, each day becomes more similar to day 20. I’d expect the difference between day 1 to day 2 to have a lot of noise because they are both the least like day 20 and maybe in different ways. The difference between day 18 and day 19 should have less noise because they are both most like day 20. “There are many ways to be different, but only one way to be the same” might apply? All of this only figures “on average and over time” as of course there could be large shocks later on in rounds on some occasions.

![](http://forum.numer.ai/user_avatar/forum.numer.ai/profricecake/48/2528_2.png) profricecake:

> What remains clear is that the early daily scores are not very predictive of the final score. Just look at [@jrai](</u/jrai>)’s original plot. So why are they presented to us at all? What kind of value are we supposed to get from them if they have no bearing on the final score as some have claimed, and (as of yet) no unambiguous meaning?

If we didn’t have daily scores, how would we become addicted to refreshing the leaderboard and profile pages? It’s just gamification. Cooler heads should pay little attention to it in the long run, except if we discover some information can be gleaned from a model’s intraround volatility: [Sharpe and Sortino ratios on live performance of your models](<http://forum.numer.ai/t/sharpe-and-sortino-ratios-on-live-performance-of-your-models/1551>) ([@degerhan](</u/degerhan>)’s post still hasn’t gotten enough attention).

---

### Post #23 — **wigglemuse** | 2021-03-09 15:06 UTC

Consider also that day 1 is the closest to the data as we get it at the start of the round, and that might give you hint of a way you could actually use the daily scores to improve your models – although we aren’t given the targets at any point, knowing how much movement there actually is in an average round is potentially actionable information.

---

### Post #24 — **mugamma** | 2021-03-09 15:16 UTC _(reply to #21)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/wigglemuse/48/3094_2.png) wigglemuse:

> I mean, I guess he could be straight up lying, or he doesn’t actually know how it works,

[@profricecake](</u/profricecake>) If this is a concern, you should not be participating in the tournament. In contrast to the very long conversation in Rocket Chat yesterday (and many times before) about trusting third party model staking where there are big trust issues between users, this is about trusting the system.

---

### Post #25 — **zwk** | 2021-03-09 16:51 UTC _(reply to #23)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/wigglemuse/48/3094_2.png) wigglemuse:

> Consider also that day 1 is the closest to the data as we get it at the start of the round, and that might give you hint of a way you could actually use the daily scores to improve your models

That makes a lot of senses. But for the sake of transparency, revealing the score calculation method should not be a red-line vis-à-vis the hedge fund operation. Transparency is heart of the defi, right ![:grinning:](http://forum.numer.ai/images/emoji/twitter/grinning.png?v=12)?

---

### Post #26 — **wigglemuse** | 2021-03-09 16:53 UTC _(reply to #25)_

We don’t even know what the target is. So that could have a lot to do with it.

I did look at the data for ALL models and then filtered in a few ways but the basic pattern always holds. First day average change is much bigger than others, and then generally decreases. I think a lot of us have noticed that the first day is way off, and will often reverse the second or third day before it gets even a semblance of a trajectory towards where it is going to end up. Probably down again to how the target is created. We have once in a while we’ve seen some radical changes in scores on the very last day or two though…

---

### Post #28 — **pumplerod** | 2021-03-09 18:27 UTC _(reply to #26)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/wigglemuse/48/3094_2.png) wigglemuse:

> It has always been stated that we are predicting the market 4 weeks hence but since this question gets talked about sometimes I just wanted to clarify with the team that nothing that happens in the intermediate days could affect the score. And he did confirm that. So the question is pretty much settled

I’m not reading into this discussion that anyone is questioning the integrity of the team. And I very much appreciate your insight and discovery [@wigglemuse](</u/wigglemuse>) however, while you mention that the issue is pretty much settled, I cannot find any information in the official documentation regarding details on the subject. I trust that you did ask and that Richard did respond, but it seems reasonable to want these details in a readily available point of reference as part of the official documentation, rather than to have to scour the forums and chat rooms. Especially as a newcomer.

What [@profricecake](</u/profricecake>) has proposed seems like an utterly reasonable possibility for a method of calculation. It may not, in fact, be what is happening but I, for one, would love to see clear easily accessible documentation from the official numerai team, which doesn’t seem like a big ask. If presenting that level of detail would pose some level of data leakage or security risk, then stating so would be sufficient. It’s in all of our interests for each of us to have great performance, so I certainly don’t think anything sneaky or untoward is going on. Probably just a squeeze on resources. I love the tournament, and the community. I believe a push toward more clear and available official documentation gives all of us some bedrock to stand on and would allow for our guessing to focus more on how we can improve predictions and less on the mechanics of the tournament.

---

### Post #29 — **wigglemuse** | 2021-03-09 18:51 UTC

My point is that they’ve only ever said it is one way, so there isn’t really any more detail needed in order for it to be the plain truth. The need to clarify it only comes from users essentially asking “Is the way you say it is actually the way it is?” They obviously aren’t going to document every esoteric detail that it is NOT. Things get documented above and beyond the basics when they are continuing questions about them, and that applies here. But the questions come before the documentation because otherwise it is not known which things are points of confusion that need additional clarification. In any case, I am working on that exact documentation, and should be doing that right now instead of posting on the forum. So once that project is more or less complete (complete enough to post anyway), if and when any more questions about esoteric details come up that I haven’t answered, I will be then happy to add to it (with a quick response time) pretty much any reasonable question people have and then it will be there to point to. And in fact, that’s exactly why I made sure to clarify this once and for all directly with the team, because anything I put in those docs I will make sure is correct.

So the entire point of my documentation project is specifically so users (new users especially) do not have to scour all of these sources for all these questions they have, and it will be in one place. We started the project about a month too late, because just as we got this flood of Lex Fridman podcast newbies flooding the place with their questions was about the same day I started working on that. I wish it was ready already, but it will be quite soon.

---

### Post #30 — **wigglemuse** | 2021-03-09 19:18 UTC _(reply to #29)_

Even Richard thinks it should say it better on the website. Here’s the bit of the video I was referring to from last fireside chat. (51:06)

[ ![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/3b71b2c10e78e4e6f8da0a07dea7eac227cb6cb0.jpeg) ](<https://www.youtube.com/watch?v=hb3GeT7czO8&t=84s>)

Guess it won’t jump to the right place when embedded, if you open up on youtube and expand the “show more” you can see all the questions and that one at 51:06

---

### Post #31 — **profricecake** | 2021-03-09 19:37 UTC _(reply to #24)_

Hi all.

I came to this thread in search of explanations. I’m not making accusations, I’m offering theories and challenging those that are either unsupported by evidence or that don’t seem to jibe with my readings of the data (or both).

Please try to remember that you Numerai vetrans were here once too. Not everyone participating in the tournament has been exposed to the same information about the tournament. Apparently some of you have been in direct contact with members of the staff, others like me have just started their involvement and know only what’s on the website.

![](http://forum.numer.ai/user_avatar/forum.numer.ai/wigglemuse/48/3094_2.png) wigglemuse:

> But please let’s quit with the idea that the team is hiding something or there is big conspiracy. I ASKED THEM THESE EXACT QUESTIONS and Richard directly answered them (and you can go watch it).

First of all: I’d love to watch it! It sounds like it has all the answers. But you still haven’t shared it yet.

Second: Hiding things is a core part of the Numerai concept. They strip all identifying materials from the data set to keep the competition more data science and less finance. I understand and accept this. They’ve documented it clearly on the website. But the daily scores are the opposite of hidden: they’re front and center for all the world to see, but they are only thinly documented (hence this thread).

Third: Conspiracy? Why did you bring that word up? Just because I’m not ready to accept _your_ claims without evidence? Again, please try and remember that I haven’t had the same access to the primary sources that you’ve had and - like you - just want to hear answers from a source I can trust. Just because you feel that you understand things with great certainty doesn’t automatically make you a trustworthy source, since you are not a Numerai employee nor have (yet) offered any evidence beyond hearsay in support of your claims.

If you post that video that you keep referencing, I would greatly appreciate it. Then it will be available for anyone who has the same questions in the future and who want to hear it straight from Richard’s mouth. This is less ideal than an update to the official Numerai docs but still a big step in the right direction.

Looking ahead, I hope you plan to cite (and make available) your sources in your upcoming FAQ. This is historically how knowledge is built, and for good reason.

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/m/c57346/48.png) mugamma:

> ![](http://forum.numer.ai/user_avatar/forum.numer.ai/profricecake/48/2528_2.png) profricecake:
>
>> So why are they presented to us at all?
> 
> Because the previous setup we had zero feedback for 4 weeks. This is better than that.

Thanks for sharing this. I didn’t know that there was a complete lack of feedback in an earlier incarnation of the tournament. Daily feedback would certainly be an improvement on that, for sure, even if the early days are not indicative of the final score.

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/m/c57346/48.png) mugamma:

> ![](http://forum.numer.ai/user_avatar/forum.numer.ai/wigglemuse/48/3094_2.png) wigglemuse:
>
>> I mean, I guess he could be straight up lying, or he doesn’t actually know how it works,
> 
> [@profricecake](</u/profricecake>) If this is a concern, you should not be participating in the tournament.

This is pretty funny. The thing I’ve asked for most in my posts is a trusted source of information (like Richard) to chime in on this topic. Please don’t misinterpret my skepticism of unfounded claims made by Numerai outsiders as a lack of trust in Numerai’s leadership. There is no connection between the two, which is of course the source of my skepticism in the first place.

---

### Post #32 — **profricecake** | 2021-03-09 19:37 UTC _(reply to #31)_

Aha! I see the video was posted while I was drafting my last message. I’m looking forward to watching it, [@wigglemuse](</u/wigglemuse>). Thank you for sharing it.

---

### Post #33 — **wigglemuse** | 2021-03-09 19:53 UTC

My FAQ may have a few links in it to existing materials, but it certainly isn’t going to source and footnote every little thing as that would be almost impossible. But no implementation details I describe will be in there that I’m not sure about or haven’t verified. And it is all public info – no insider access required other than occasionally asking an insider about something (which they are only going to answer if it is ok to be public). But feel free to ask about any additional details, or if something remains confusing, that’s the whole point.

---

### Post #34 — **profricecake** | 2021-03-09 20:32 UTC _(reply to #32)_

The video answered some questions unambiguously for me so I thought I’d share what I’ve learned here so others might benefit.

  * Although daily scores are provided, Richard confirmed that “ultimately you get scored on the last day [of each round] only”, and “there’s nothing in the middle that could affect your performance.” Although he did go on to acknowledge that companies going bankrupt or some other large-scale market disruption could certainly change performance during a tournament round.

  * The daily scores, as Richard describes them in the video, are “just an estimate” of what your final daily returns will be if Numerai was forced to give you an estimate even many days out from the actual tournament end.




These statements resonate with the observations from this thread that it’s easier to make a prediction when you’re closer to the actual scoring day, and hence why the daily scores seem to converge towards the final score (because, as many have noted, the market state on day 20 is likely to be more similar to the market state on day 19 than on day 1).

Based on this information, I’m confident that the idea I posted about daily scores being daily correlations is off-base. Here’s to learning!

In the wake of this informative thread, I would like to make three simple suggestions to Numerai to disambiguate this daily score stuff for others in the future.

  1. Call them “daily estimates of your final score” instead of “daily scores” (or something similar that would highlight the fact that they’re estimates)
  2. Add error bars to the website graphs based on what I’m sure is plenty of available data on the variance of the estimated scores relative to the final score. Bars would vanish for all completed rounds, of course, but the IP rounds would each have them, and they would grow progressively larger as we approach the latest round.
  3. Revise some of the documentation under Scoring on [this page](<https://docs.numer.ai/tournament/learn>).



In an attempt to be helpful regarding #3, below are some suggested revisions to the existing docs.

Here’s a current (confusing) paragraph:

> Each submission will be scored over the ~4 week duration of the round. Submissions will receive its first score starting on the Thursday after the Monday deadline and final score on Wednesday 4 weeks later for a total of 20 scores.

Here is a clearer and more informative version based on what I gleaned from the video:

> Each submission will be scored on the final day of the ~4 week round. Submissions will receive estimates of their final score starting on the Thursday after the Monday deadline that will continue until Wednesday 4 weeks later when the final score will be released. These estimates will be provided on what we call “scoring days” (weekdays M-F minus market holidays). The estimates tend to grow more accurate as predictors of the final score as the tournament round draws to a close, but they are merely estimates. Only the score on the final day counts for the competition.

While I’m at it, I’ll offer a revision to the next paragraph too. Original:

> Since a round takes ~4 weeks to resolve, if you submit new predictions every week, you will receive multiple (up to 4) overlapping scores on each scoring day from the 4 ongoing rounds.

Proposed revision:

> Since a round takes ~4 weeks to resolve, if you submit new predictions every week, you will receive multiple (up to 4) overlapping score estimates on each scoring day from the 4 ongoing rounds.

Thanks to all who offered their input on this one!

---

### Post #35 — **orbitalteapot** | 2021-04-13 21:06 UTC

Maybe I’m just beating a dead horse by bumping this… But here’s my take, code below.

Daily score is nothing more than the correlation between prediction vs realized target on that day. The realized target is some form of cumulative return until that point (might be market neutralized, scaled by risk etc).

So it can be fairly well modelled by 5000 (or however many stocks are traded) brownian motions. Each day these are ordered and that order is compared to your ordering.

A change in daily score is not triggered directly by returns of stocks, but by the change in order caused by the change in cumulative returns. As [@wigglemuse](</u/wigglemuse>) points out the score will per defintion converge to the final score.

Now to the fun part… The reason why the absolute changes in increments (or std for us preferring l2 norms) decrease as the round progresses is because the average distance between the 1d diffusion processes increase. Higher distance = lower chance of change in the rank correlation between prediction and target.

The standard deviation of increments in daily scores goes down in magnitude by approximately 1/sqrt(day of round + 1).

Code to a simple monte carlo simulation of this:

![](https://pastebin.com/favicon.ico) [Pastebin](<https://pastebin.com/BNr6wR8Y>)

### [decreasing variance of increments - Pastebin.com](<https://pastebin.com/BNr6wR8Y>)

Pastebin.com is the number one paste tool since 2002. Pastebin is a website where you can store text online for a set period of time.

---

### Post #36 — **mindyoself** | 2021-08-17 11:28 UTC _(reply to #10)_

Thanks [@jrai](</u/jrai>) this is really useful. ![:ok_hand:](http://forum.numer.ai/images/emoji/twitter/ok_hand.png?v=9)

---

### Post #37 — **jrai** | 2022-01-04 01:31 UTC _(reply to #10)_

Despite how little we know about early daily scores, our obsession with them will forever endure. Here’s a quick update on this post including Signals data and some better code in a colab notebook so you can test your models, do comparisons, and more/better analysis: [Google Colab](<https://colab.research.google.com/drive/1HkAohCeBWvN3ODDYFoHaoNzDAQ8ZMFk8#scrollTo=j4PDKlpxDT-M>)

The high level conclusions are still the same:

  * you can expect roughly .02 - .03 correlation difference from the first day of a round’s score and the final resolved day of a round’s score (aka your actual score which is the only one that matters) **on average** but could range much higher than that.
  * scores are only somewhat informative around the 15th day into a round



The figures show a single model and a different color transparent line for each round with the daily scores distance from the resolved score for that individual round as the round progresses. Then we chart an average line (in red) and a band of +/1 standard deviation across all rounds. First Signals:  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/f/fc1ee9270fcb89bfcb018830cfa260d38456161b_2_690x275.png)image833×333 86.6 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/f/fc1ee9270fcb89bfcb018830cfa260d38456161b.png> "image")

  
And then Classic Tournament:  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/3/35cdfd13a10ad0ca13453851ddfd3e87f9d943a4_2_690x275.png)image833×333 79.3 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/3/35cdfd13a10ad0ca13453851ddfd3e87f9d943a4.png> "image")

_For these two models_ across the tournaments and the same rounds 279-292, Signals and Classic daily distances are similar on average, but different rounds exhibited very different daily distances between the two tournaments (which is probably a good thing if you want to diversify risk by competing in both).

Comparing across some top Classic leaderboard positions, and pulling in more rounds so we can get a clearer picture of the mean (20d corr is only available for Signals starting at round 279), we can also see some more volatility (i.e. higher early daily score distances from final score), which may be a common factor at the top of the leaderboard?  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/2/29dc1a38469acb6799b96ab3b7d59aeaa4938511_2_690x275.jpeg)image833×333 74.9 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/2/29dc1a38469acb6799b96ab3b7d59aeaa4938511.jpeg> "image")

We can see the same looking at some top Signals leaderboard positions (onlyatest for example is just submitting ranked momentum predictions and is understandably very volatile):  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/1/144b4566e15a60bb74480c8d766b139e636b5076_2_690x275.png)image833×333 71.4 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/1/144b4566e15a60bb74480c8d766b139e636b5076.png> "image")

Shoutout to [@robo_boi](</u/robo_boi>) for having some incredibly volatile Signals models, anything you are willing to share about why? My guess would be testing out single features? Perhaps not, because [@arbitrage](</u/arbitrage>) is also submitting a single feature to his model “leverage” and it has some of the lowest distances on average I’ve seen:  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/5/53815b1488c93a35339dbfaf4958e026dad7e20a_2_690x273.png)image840×333 96.5 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/5/53815b1488c93a35339dbfaf4958e026dad7e20a.png> "image")

Questions to still answer:

  * Is there a relationship between rank and initial distance from final day score (i.e. volatility)? What about between FNC rank and initial distance?
  * Same question that [@bor1](</u/bor1>) asked: _how reliable is the qualitative difference in daily score between two models submitted in the same week? (i.e. is model X that looked better than model Y in week 1, indeed better than model Y at round resolution)_ "  
**I did find that MMC tends to follow a slightly tighter path, so generally I think percentile ranks can hold a bit more steadily through time, but it would be interesting to chart that out too.

---

### Post #38 — **arbitrage** | 2022-01-05 17:52 UTC _(reply to #37)_

My guess is that my factor is very similar to one of theirs, but sufficiently different that I can still register a non-zero corr. I’d further guess that if I were able to calculate my measure for the entire universe that my score would increase in volatility. Good analysis [@jrai](</u/jrai>) these posts are always very interesting!

---

### Post #39 — **jrai** | 2022-01-05 19:32 UTC _(reply to #38)_

That makes sense, good point. Submitting a smaller universe almost certainly brings down daily score distance volatility (just because a lot more 0.5s diluting everything in the first place) and submitting a heavily neutralized factor would also probably decrease intraround volatility. Conveniently, the next post is about neutralized corr vs unneutralized corr (UNC) in signals. With UNC eventually in the API, we can go more in-depth and look at everyone’s “neutralization effects.” I think the range we see is going to be pretty interesting.

---

### Post #40 — **profricecake** | 2022-01-06 17:03 UTC _(reply to #37)_

Cool analysis - thank you!

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/forum.numer.ai/jrai/48/3291_2.png) jrai:

>   * scores are only somewhat informative around the 15th day into a round
> 


Would love to dig into this a little more deeply. Can you put any numbers to “somewhat informative”? How’d you pick day 15?

You’re using absolute distance; are the scores N days prior to the final day equally likely to be below as they are to be above that final score? (aka is there a trend up or down as we converge to the final score?)

Thx

---

### Post #41 — **jrai** | 2022-01-06 21:42 UTC _(reply to #40)_

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/numerai.discourse.group/profricecake/48/2528_2.png) profricecake:

> Would love to dig into this a little more deeply. Can you put any numbers to “somewhat informative”? How’d you pick day 15?

Good question, it’s completely made up. Day 15 is generally where I saw the average absolute distance at around 0.01 where std also accelerated its shrinking to +/ .01. At that point, I felt like it deserved to be called “somewhat informative,” but it was a pretty subjective landmark.

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/numerai.discourse.group/profricecake/48/2528_2.png) profricecake:

> You’re using absolute distance; are the scores N days prior to the final day equally likely to be below as they are to be above that final score? (aka is there a trend up or down as we converge to the final score?)

When I first did the analysis, the daily distances looked to be about 0, but now with many more rounds included and a check across more models, it actually looks like very early daily score distances have a significant negative skew, especially in the extreme cases (i.e. see the standard deviation bands). In other words, I guess scores may trend up, on average, as we converge to the final score. It may be possible this negative skew is just from a few extreme rounds in this sample, but it also makes sense that predictions would get “better” as they get closer to what they’re trying to predict in the first place.

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/8/8b1062c89571f5179a076f26b3392c8559fcb0cd_2_620x500.jpeg)image848×683 116 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/8/8b1062c89571f5179a076f26b3392c8559fcb0cd.jpeg> "image")

---

### Post #42 — **profricecake** | 2022-01-07 00:23 UTC _(reply to #41)_

Thanks for the extra info!

BTW are your ‘scores’ for your classic tourney data pure corr values or are they corr/mmc combos?

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/forum.numer.ai/jrai/48/3291_2.png) jrai:

> it actually looks like very early daily score distances have a significant negative skew, especially in the extreme cases

Since you clearly have the data loaded and available, I wonder if you might be willing to go further with this.

I suspect I’m not alone in hoping for positive scores each week, and that I value any positive final score greater than any negative final score. So in the wake of your latest post I’m curious:

  * If early scores are negative, what chance do I have that they’ll turn positive? And of course the opposite: if early scores are positive, what are the chances they’ll go negative? We could call this the “outcome reversal” probability. It is of course 0% on the final day of the round, but what is its value on day 15, 16, etc?
  * At what day during the round do most (say 95%) of the daily scores lie on the same side of zero as their final day counterparts? Aka, if my score is negative on day 15, what are the odds it will still be negative on the final day too? I guess this is just 1.0 minus the outcome reversal odds, so it’s really the same number.
  * Does the negative skew on early scores still exist if you separate the data into two chunks: final scores that were net positive (earns) and final scores that were net negative (burns)? Testing this would help support (or not) your intriguing suggestion that perhaps the negative skew is because our predictions get better as we get close to what we’re trying to predict.

---

### Post #44 — **jrai** | 2022-01-07 17:48 UTC _(reply to #42)_

Posted from wrong account.

This is pure corr. MMC tends to have less volatility, but is an interesting analysis on its own. Also, all good questions that hopefully I/we can answer soon. All of the code for this post is public in this notebook if you want to play around: [Google Colab](<https://colab.research.google.com/drive/1HkAohCeBWvN3ODDYFoHaoNzDAQ8ZMFk8#scrollTo=j4PDKlpxDT-M>)

---

### Post #45 — **profricecake** | 2022-01-07 20:18 UTC _(reply to #44)_

Thx for the Colab link.

Here are two really simple plots (using data from your jrai model) where I estimate the probability for each scoring day of the final score being a complete reversal of the daily reported score. In other words, if on day 1 the scores are positive, what are the odds that on day 20 the score will be negative? And so on throughout all 20 days.

Here is the plot for final scores that were positive:

[![posswap](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/d/d08b98fe99d19fca89838bd5333664546d17d803.png)posswap497×264 10.9 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/d/d08b98fe99d19fca89838bd5333664546d17d803.png> "posswap")

And here is the plot for final scores that were negative:

[![negswap](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/f/f70a9419bf55233a1a5858a68a525f823703f02f.png)negswap503×264 11.5 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/f/f70a9419bf55233a1a5858a68a525f823703f02f.png> "negswap")

They seem pretty similar on the whole. Here are my takeaway points:

  1. There is roughly a 35% chance that your final round score will have the opposite sign of your day 1 score (aka a day 1 burn has a 35% chance of becoming a day 20 earn, and vice versa)
  2. By approximately scoring day 11, you’re down to a 10% chance of a complete reversal.



I’d like to continue this analysis with magnitude of the correlation in mind. Aka, I suspect that higher absolute value corr values (either pos or neg) will result in less fate swapping by the end.

---

### Post #46 — **jrai** | 2022-01-19 18:56 UTC _(reply to #45)_

I would love to see some sort of marker of uncertainty added to the UI for the “out-rounds” that considers +/- 1 standard deviation scores given how many days are left in the round. Something like this:  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/8/8da97dcec38ece18f53a2d8320943c358b99c97f_2_690x201.png)image922×269 22.7 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/8/8da97dcec38ece18f53a2d8320943c358b99c97f.png> "image")

---

### Post #47 — **wigglemuse** | 2022-01-19 18:59 UTC _(reply to #46)_

Maybe a shaded area.

---

### Post #48 — **jrai** | 2022-06-19 23:57 UTC

Now that we have many more completed rounds with daily TC scores, this daily difference from resolution analysis seems like it can be extended to that metric. And, we also have percentile scores in the API, which is something I had wanted to look at for a while.

In sum, I’ve found that (on average across most models, but there are always exceptions) your TC percentile early on in a round is closer to your final day TC percentile as compared to that of your CORR percentile early on in a round relative to its final day percentile. In other words, if your first day TC score is in the 50th percentile, on average your final TC score will likely end up in the 30% - 70% range. However, if your first day CORR score is in the 50th percentile, on average your final CORR score will likely end up in the 15% - 85% range. I haven’t taken a closer/rigorous look at the tails, but I imagine there is different behavior there (i.e. if you start in the 100th percentile, will the daily paths be very different?)

Here are charts for all of integration_test’s rounds for TC percentile values and CORR percentile values:  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/3/3d842daa8f1e425ce0bff30df6273827d44b4035_2_690x277.png)image827×333 95.5 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/3/3d842daa8f1e425ce0bff30df6273827d44b4035.png> "image")

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/5/5e1a4bb29692a13f693918a131f5035e4df25c2e_2_690x277.png)image827×333 102 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/5/5e1a4bb29692a13f693918a131f5035e4df25c2e.png> "image")

---

### Post #49 — **pumplerod** | 2022-06-24 19:22 UTC _(reply to #45)_

Would love to see this, now charted against TC scores.

---

### Post #50 — **dev0n** | 2022-06-29 18:39 UTC _(reply to #48)_

Some anecdata that supports your conclusion: I’ve noticed my Corr swinging from pos to neg day to day but TC being more stable.

Example:

Screenshot of chart on June 28:  


[![Screen Shot 2022-06-29 at 11.34.37 AM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/7/730ac7139503e7b8f7e816a668430dc1b600f3d9_2_690x356.png)Screen Shot 2022-06-29 at 11.34.37 AM1852×956 95 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/7/730ac7139503e7b8f7e816a668430dc1b600f3d9.png> "Screen Shot 2022-06-29 at 11.34.37 AM")

Screenshot of chart on June 29:  


[![Screen Shot 2022-06-29 at 11.34.45 AM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/3/3afe943f6cd372ea935bb50bf327ec7e2d551ef9_2_690x354.png)Screen Shot 2022-06-29 at 11.34.45 AM1842×946 94.5 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/3/3afe943f6cd372ea935bb50bf327ec7e2d551ef9.png> "Screen Shot 2022-06-29 at 11.34.45 AM")
