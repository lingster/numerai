---
title: "A True Contribution backtest"
category: Tournament
url: https://forum.numer.ai/t/a-true-contribution-backtest/5154
created_at: 2022-03-27T15:02:22.598000+00:00
last_posted_at: 2022-04-12T15:55:12.420000+00:00
posts_count: 30
views: 3799
tags: []
---

# A True Contribution backtest

---

### Post #1 — **bvmcheckking** | 2022-03-27 15:02 UTC

# Summary (because long post):

TC is planned to be rolled out in 2 weeks. Although we have been given a reason why TC should be a better metric and been shown that it correlates with other metrics in the same round there is one problem. A positive score for TC in one round has practically no correlation with your TC score in the future. A positive MMC score or a positive FNC score in a round more strongly correlates with future positive TC scores. TC seems extremely noisy, if the goal of numer.ai is to improve performance on TC, it makes more sense to payout based on MMC/FNC.

# Intro

Although Numer.ai has had great performances as a hedge fund over these last years, they always seem to strive to improve. We have seen this over the last years with for example Signals and with the increased dataset size + the new targets. Numer.ai now seems to have another innovation in place, True Contribution (TC). The idea behind this is to pay users more closely to what they contribute by estimating how much increasing their model to the meta model would have increased profits, taking into account how their optimizer would have had reacted to this new meta model.

The main argument in favor of this is aligning incentives between the users and the hedge fund performance, which should be fairer due to a user earning only if his result has had a positive impact on the performance and also that this should increase the performance of the hedge fund. A lot of theoretical backings have been made both explaining the [math behind it](<http://forum.numer.ai/t/true-contribution-details/5128/24>) and also the more high-level [Alien Stock Market Intelligence medium post by Richard](<https://medium.com/numerai/alien-stock-market-intelligence-numerais-true-contribution-6bc7652bd6ac>). From the start it has been pushed pretty heavily as make or break for Numer.ai, even when it was in a non-functioning state.

In general it feels to me like this had been decided before results were able to be gathered, and even now that they can be gathered I am a bit disappointed that the data is still missing. We have been shown some of the correlations between metrics with TC. But this is not the same as a backtest, what would have happened if you pay out on TC. We have, to my knowledge, still not received any backtest of the results of TC. In general I have the fear that the TC decision was made because it looks cool and impressive and is thus very marketable, but I feel less importance has been placed on both the effect this has on the future results of the hedge fund and the effect on the participants.

# Backtest

So what is the goal of TC? The goal is probably by increasing stakes of people with high TC, to increase future performance of the hedge fund. A model that contributed positively to the hedge fund’s performance is also more likely to do so in the future, right? Well, how can we test this? If a person has positive TC in a round that just ended, Numer.ai wants to give him a higher payout, with the idea that he performs better next round. But is this so?

Using Numer.ai’s GraphiQL API I have downloaded all round results of round 285 up 304. So a few rounds after the last big change happened, the increased dataset size, and up to the last resolved round.  
Then I attempt to figure out if users used the same model while submitting, by assuming that somebody switched models if the correlation with meta model is higher than 5% from one round to the next.

Using this data I am able to do some simple checks to see whether TC correlates with other metrics. In general for my analysis I filter everybody above a certain quantile in some metric and see how they would perform on the TC metric. For example, if a person performs well on CORR, is he likely to perform well on TC as well? You can see in the bottom left underneath that having a positive score in a round has a positive effect on the TC as well in that round. Similar effects can be seen for MMC and FNC, with FNC correlating most strongly. This all seems to be in line with the post made by MDO

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/f/f24698ace93ae0473b274105f887da5008a30578_2_690x202.png)image2142×630 92.8 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/f/f24698ace93ae0473b274105f887da5008a30578.png> "image")

Yet for all of them, the correlation is pretty weak. The top 20% of CORR only performs as top 40% of TC. If you were to compare CORR with MMC, you will get very different results. The top 20% of CORR performs top 15% of MMC (see picture below).

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/d/de68f062816d3dd2938bf4dbc37b0dd0016ae9e7_2_432x499.png)image536×620 41.5 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/d/de68f062816d3dd2938bf4dbc37b0dd0016ae9e7.png> "image")

So this all gets me pretty scared, especially if you keep in mind that this is not the question we want to answer. We aren’t interested in the in-round correlation between the metrics. But whether positive TC in one round means better performance on TC for the next round. I have also made that analysis, and you can see the graph’s about this underneath.

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/0/01c76684670fbe6e0917f7acfe3797efe11717e2_2_690x204.png)image2158×640 108 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/0/01c76684670fbe6e0917f7acfe3797efe11717e2.png> "image")

As we can see here the relation between TC in one round and in the next round is extremely weak. The slope does not seem to be increasing for better performance. It is basically a flat line with some small ups and downs. We can also see that positive CORR in one round does not lead to a positive CORR in the next round. Positive MMC in one round seems to work better, as MMC performance increases so does TC, albeit slightly. But the best measure for payout to optimize future TC performance seems to be FNC.

So knowing that TC in one round does not seem really predictive of TC, what does that mean? Well first of all that the payout system will not benefit the hedge fund’s performance. The TC reward seems to be distributed in a way that does not improve future TC, so it is basically given away at random. If the goal is to increase the future TC performance, rewarding FNC and MMC seems a lot more like the way to go.

What do these graphs mean for the participant’s? Well first of all, I am pretty disappointed to say, but it seems that your models with positive TC’s can not be trusted very much to generate future positive TC’s. For example I have some models with TC’s of 4%, but that information does not seem to mean anything. Every other metric is more stable and would be preferable for the participants:  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/e/e4e10aaee141e952577cd994815bbf4027e58e4f_2_690x215.png)image2232×696 141 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/e/e4e10aaee141e952577cd994815bbf4027e58e4f.png> "image")

# How is this possible?

It might seem a bit weird that a metric is not most predictive of it’s future performance. Especially since the other metrics are very predictive of their own future performances. I think this is due to the huge noise generated in the optimization process combined with the great reduction of stocks that are in the end traded on. If you were to get the FnC on 50 stocks randomly picked, this metric would show huge variance. If you wanted to predict which model is most likely to score high on this metric for next week’s round, you wouldn’t pick the model performing best on this FnC_50, but you would pick the performance on the normal FnC. Although TC might directly measure what we want, the huge noise generated in this measure makes this a very undesirable measure.

Another field where you generally see this concept is in poker. I used to play this professionally and one of the most important things you have to keep in mind when analyzing your game is the difference between outcome and expected outcome. A simplified example: Imagine if you go all-in and you have 50% to win and 50% to lose. Either way the outcome will not reflect the true value of the all-in. If you were to lose the all-in the conclusion that this was a bad all-in or if you would have won and that this was a great all-in don’t seem correct so mentally rewarding the all-in based on the outcome seems not the best thing to do. What you would want to do is look at the metric of the expected outcome, which in this case would be the expected win percentage.

If you were to take this example back to Numer.ai, you might come to the conclusion that the difference between outcomes and expected outcome can also be huge. It seems that the predictive power of the models expressed in FNC (predictions are neutralized before used) and MMC do drive the true outcome, so they can be seen as the expected outcome in this case. Then you wouldn’t want to look at the outcome of the effect of using the predictions, the TC, because the variance that gets added to the true drivers is huge. It is a lot more efficient to look at the true drivers, FNC and MMC (or better metrics yet to be found).

# Other TC Problems

  * TC calculations seem complicated what are the chances bugs are created in this process?
  * TC will reduce the ability of the participants to confirm the correctness of payouts.
  * TC payouts make the generated signal dependent on the optimizer, locking in the optimizer. Likely this optimizer is not optimal, but changing the optimizer would then change the rewards of all the players and disrupt the entire tournament. This seems undesirable. Also the optimizer seems clearly not optimal. Looking at the results of a round you will generally see multiple people in the top 20 with negative TC’s. See our [most recent round](<https://numer.ai/round/304>) for example. Not being able to use this signal seems to be a mistake in the optimizer to me, not in their predictions.
  * Due to the complexity and unclear feedback loop and lack of real data regarding this, the expected improvement in models will be low.



# Possible better idea

Change the metric to something that is more verifiable, more consistent and has a better correlation with future TC such as FNC v3

# Code

Will be posted underneath this post.

# Feedback

In general I have not seen a lot of discussion recently on the effects of using TC as the new MMC or possibly in the future as the main metric. I would like to hear other people’s thoughts/perspectives/analysis on this.

---

### Post #2 — **bvmcheckking** | 2022-03-27 15:09 UTC

I have separated my script in two files, one to download the data and one to analyze the data. The download took a decent amount of memory, challenging the 32GB RAM I have. Also these days the Numerai server seems at times to have some problems handling requests, causing errors as well.  
If you want to receive the data from the download script, feel free to send me a message and I will send it to you.

Code could also be a bit cleaner, depending on interest x complaints I can refactor it a bit.

Download.ipynb:
    
    
    from multiprocessing.pool import Pool
    from numerapi import NumerAPI
    import pandas as pd
    import json
    
    from tqdm import tqdm
    
    from itertools import product
    from pathlib import Path
    
    napi = NumerAPI()
    
    
    
    START_ROUND = 285
    END_ROUND = 304
    
    
    
    round_query = """
    query($roundNumber: Int!, $tournament: Int!) {
      RoundDetails(roundNumber: $roundNumber, tournament: $tournament) {
        openTime,
        roundResolveTime
      }
    }
    """
    
    
    
    def download_round_info(round_number):
        data = napi.raw_query(round_query, 
                            {'roundNumber': round_number, 'tournament': 8})
    
        data = data['data']['RoundDetails']               
        data['roundNumber'] = round_number
        return data
    
    def download_rounds_info(start_round, end_round):
        data = [download_round_info(round_number) for round_number in range(start_round, end_round + 1)]
        df = pd.DataFrame(data)
        df.to_csv("round_info.csv", index=False)
    
    
    
    download_rounds_info(START_ROUND, END_ROUND)
    
    
    
    def get_all_users(start_round, end_round):
        users = []
    
        for round_number in tqdm(range(start_round, end_round + 1)):
            round_details = napi.round_details(round_number)
            users_round = pd.DataFrame(round_details).username.to_list()
            users.extend(users_round)
        
        users = set(users)
    
        return users
    
    
    
    
    unique_users = get_all_users(START_ROUND, END_ROUND)
    
    
    
    user_query = """
    query($username: String!) {
      v2UserProfile(username: $username) {
        dailySubmissionPerformances {
          changeRequestActualAmount,
          changeRequestAmount,
          changeRequestType,
          corrMultiplier,
          corrPercentile,
          correlation,
          correlationWithMetamodel,
          date,
          fnc,
          fncPercentile,
          leaderboardBonus,
          mmc,
          mmcMultiplier,
          mmcPercentile,
          payoutPending,
          payoutPendingDelta,
          payoutSettled,
          roundNumber,
          roundOpenTime,
          roundPayoutFactor,
          roundResolveTime,
          roundResolved,
          selectedStakeValue,
          tc,
          tcPercentile,
          tournamentName,
          weekPayoutSelection
        }
      }
    }
    """
    
    def download_username(username):
        data = napi.raw_query(user_query, 
                            {'username': username})
    
        json_file_name = f'data/{username}.json'
        with open(json_file_name, 'w') as f:
            json.dump(data, f)
    
    
    
    
    with Pool(32) as p:
        p.map(download_username, unique_users)
    
    
    
    data_path = Path('data')
    
    
    
    all_performances = []
    
    for file in tqdm(data_path.iterdir()):
        
        username = file.name.split('.')[0]
    
        try:
            with open(file, 'r') as f:
                data = json.load(f)
        except:
            print(f'file not found {file}')
    
        try:
            daily_performances = data['data']['v2UserProfile']['dailySubmissionPerformances']
        except:
            continue
    
        daily_performances_df = pd.DataFrame(daily_performances)
        daily_performances_df = daily_performances_df[daily_performances_df.roundNumber > START_ROUND]
        daily_performances_df['username'] = username
    
        all_performances.append(daily_performances_df)
    
    
    
    all_performances = pd.concat(all_performances)
    all_performances.to_csv('all_performances.csv', index=False)

---

### Post #3 — **bvmcheckking** | 2022-03-27 15:11 UTC

Code update, 2022-04-03.

  * Clearer code, more documentation.
  * Allow the top users in the quantiles on past performance and the future performance to be based on multiple rounds. (As in post 29th of March).
  * Split the code in helperfunctions.py and analysis.ipynb.
  * Changed the analysis.ipynb to create the graphs on the same rounds for all graphs. (If you look at 5 rounds in the past, and 5 rounds in the future you have to exclude for more rounds than if you only look at 1 round in the past and 5 in the future, I think the graphs are better to compare if you make them all based on the same rounds).



analysis.ipynb:
    
    
    import pandas as pd
    import matplotlib.pyplot as plt
    import importlib
    import helperfunctions
    importlib.reload(helperfunctions)
    from helperfunctions import MetricAnalyzer, PERCENTILE_COLUMNS
    
    
    
    ma = MetricAnalyzer('data/all_performances.parquet', start_round=289, end_round=295)
    
    
    
    rounds_past = 1
    rounds_next = 5
    
    fig, axs = plt.subplots(nrows=1, ncols=4)
    fig.set_size_inches(18.5, 6)
    
    for c, metric in enumerate(PERCENTILE_COLUMNS):
        quantile_results = ma.get_quantile_mean_results_next(
            metric=metric, 
            rounds_past=rounds_past,
            rounds_next=rounds_next)
    
        ax = axs[c]
        ax.plot(quantile_results.tcPercentile)
        
        ax.set_ylim(0.48, 0.55)
        ax.set_xlabel(f'last top {metric} quantile')
        ax.set_ylabel('next 5 tcs quantile')
        ax.set_title(f'last {metric} vs next 5 tcs')
    
    
    
    rounds_past = 5
    rounds_next = 1
    
    fig, axs = plt.subplots(nrows=1, ncols=4)
    fig.set_size_inches(18.5, 6)
    
    for c, metric in enumerate(PERCENTILE_COLUMNS):
        quantile_results = ma.get_quantile_mean_results_next(
            metric=metric, 
            rounds_past=rounds_past,
            rounds_next=rounds_next)
    
        ax = axs[c]
        ax.plot(quantile_results.tcPercentile)
        
        ax.set_ylim(0.48, 0.55)
        ax.set_xlabel(f'last top {metric} quantile')
        ax.set_ylabel('next 5 tcs quantile')
        ax.set_title(f'last {metric} vs next 5 tcs')
    
    
    
    rounds_past = 5
    rounds_next = 5
    
    fig, axs = plt.subplots(nrows=1, ncols=4)
    fig.set_size_inches(18.5, 6)
    
    for c, metric in enumerate(PERCENTILE_COLUMNS):
        quantile_results = ma.get_quantile_mean_results_next(
            metric=metric, 
            rounds_past=rounds_past,
            rounds_next=rounds_next)
    
        ax = axs[c]
        ax.plot(quantile_results.tcPercentile)
        
        ax.set_ylim(0.48, 0.55)
        ax.set_xlabel(f'last top {metric} quantile')
        ax.set_ylabel('next 5 tcs quantile')
        ax.set_title(f'last {metric} vs next 5 tcs')
    

helperfunctions.py
    
    
    import pandas as pd
    from functools import reduce
    
    
    DEFAULT_START_ROUND = 260
    DEFAULT_END_ROUND = 303
    DEFAULT_CORR_W_MM_THRESHOLD = 0.05
    
    PERCENTILE_COLUMNS = ['corrPercentile', 'mmcPercentile', 'fncPercentile', 'tcPercentile']
    
    
    class MetricAnalyzer:
        def __init__(self, performances_path, start_round=DEFAULT_START_ROUND,
                     end_round=DEFAULT_END_ROUND,
                     corr_w_mm_threshold=DEFAULT_CORR_W_MM_THRESHOLD):
            """Analyzes how metric percentiles correlate with future or same round metric performances.
    
            Parameters
            ----------
            performances_path : str
                Path to performances parquet
            start_round : int, optional
                First round to start analysis on, by default DEFAULT_START_ROUND
            end_round : int, optional
                Last round to end analysis with, by default DEFAULT_END_ROUND
            corr_w_mm_threshold : float, optional
                Parameter that decides when a model is assumed to have been swapped,
                by default DEFAULT_CORR_W_MM_THRESHOLD
            """
    
            self.performance_per_round = self._get_final_performance_per_round(
                performances_path, corr_w_mm_threshold)
            self.set_rounds(start_round, end_round)
    
        def _get_final_performance_per_round(self, performances_path, corr_w_mm_threshold):
            """ Select the last performance of each round.
            
            Only resolved rounds are used in the analysis.
            """
            df = pd.read_parquet(performances_path)
            df = self._filter_performance_df(df)
            df_per_round = self._get_last_performance(df)
            df_per_round['model_number'] = self._compute_model_number(df_per_round, corr_w_mm_threshold)
            return df_per_round
    
        def _filter_performance_df(self, df):
            """Filter performance df.
    
            Filter all rows for which correlation is NA, with rounds that are resolved
            and only select the columns from the dataframe that are relevant."""
            df = df[df.correlation.notna()]
            df = df[df.roundResolved]
    
            df = df[['roundNumber', 'username', 'date', 'correlationWithMetamodel',
                     'correlation', 'corrPercentile', 'mmc', 'mmcPercentile',
                     'fnc', 'fncPercentile', 'tc', 'tcPercentile']]
    
            return df
    
        def _get_last_performance(self, df):
            """Obtain the last performance per round.
            """
            last_performance = df.groupby(['roundNumber'], as_index=False).apply(
                lambda x: x[x.date == x.date.max()])
            return last_performance
    
        def _compute_model_number(self, df_per_round, corr_w_mm_threshold):
            """Computes model number.
            Every round a users score differs more than corr_w_mm_threshold, it is assumed the
            user changed the model."""
            model_number = (
                df_per_round
                .groupby('username', group_keys=False)
                .apply(lambda x: (x.correlationWithMetamodel.diff().abs()
                                  > corr_w_mm_threshold).cumsum())
            )
            return model_number
    
        def set_rounds(self, start_round, end_round):
            """Set the start and end round.
    
            Parameters
            ----------
            start_round : int
                First round to start analysis on.
            end_round : int
                Last round to start analysis on.
            """
            self.set_start_round(start_round)
            self.set_end_round(end_round)
    
        def set_start_round(self, start_round):
            """Set the start round.
    
            Parameters
            ----------
            start_round : int
                First round to start analysis on.
            """
            assert(start_round in self.performance_per_round.roundNumber.values)
            self.start_round = start_round
    
        def set_end_round(self, end_round):
            """Set the end round.
    
            Parameters
            ----------
            end_round : int
                Last round to start analysis on.
            """
            assert(end_round in self.performance_per_round.roundNumber.values)
            self.end_round = end_round
    
        def _get_relevant_rounds(self):
            """Retrieve rounds needed for analysis."""
            relevant_rounds = pd.Series(range(self.start_round, self.end_round + 1), name='roundNumber')
            assert(relevant_rounds.isin(self.performance_per_round.roundNumber).all())
            return relevant_rounds
    
        def get_mean_top_quantile_same_round_performance(self, metric='tcPercentile', quantile=0.5):
            """Get mean performance of top users in some metric at some quantiles for each metric.
    
            Parameters
            ----------
            metric : str, optional
                Metric to select top users for, by default 'tcPercentile'
            quantile : float, optional
                Top quantile to select, by default 0.5
    
            Returns
            -------
            pandas Series.
                Mean performance of top users in that round.
            """
            df_per_round = self.get_top_quantile_same_round_performance(metric, quantile)
            df_mean = df_per_round[PERCENTILE_COLUMNS].mean()
            df_mean['quantile'] = quantile
            return df_mean
    
        def get_top_quantile_same_round_performance(self, metric='tcPercentile', quantile=0.5):
            """Get performance per round of top users in some metric at some quantiles for each metric.
    
            Parameters
            ----------
            metric : str, optional
                Metric to select top users for, by default 'tcPercentile'
            quantile : float, optional
                Top quantile to select, by default 0.5
    
            Returns
            -------
            pandas DataFrame.
                Performance of top users per round.
            """
            relevant_rounds = self._get_relevant_rounds()
            df = relevant_rounds.apply(
                lambda x:  self._get_top_quantile_same_round_performance(x, metric, quantile))
            return df
    
        def get_mean_top_quantile_next_round_performance(self, rounds_past=1, rounds_next=1,
                                                         metric='tcPercentile', quantile=0.5):
            """Get future mean performance of top users, for some number of rounds for some metric 
            at some quantile, for each metric.
    
            Parameters
            ----------
            rounds_past : int, optional
                Number of past rounds to decide past performance on, by default 1.
            rounds_next : int, optional
                Number of future rounds to decide next performance on, by default 1.
            metric : str, optional
                The metric for which to decide the top users by, by default 'tcPercentile'.
            quantile : float, optional
                The top quantile of users to select, by default 0.5.
    
            Returns
            -------
            pandas Series.
                Mean performance of top users in future rounds.
            """
    
            df_per_round = self.get_top_quantile_next_round_performance(
                rounds_past, rounds_next, metric, quantile)
            df_mean = df_per_round[PERCENTILE_COLUMNS].mean()
            df_mean['quantile'] = quantile
            return df_mean
    
        def get_top_quantile_next_round_performance(self, rounds_past=1, rounds_next=1,
                                                    metric='tcPercentile', quantile=0.5):
            """Get future performance of top users, for some number of rounds for some metric 
            at some quantile, per round for each metric.
    
            Parameters
            ----------
            rounds_past : int, optional
                Number of past rounds to decide past performance on, by default 1.
            rounds_next : int, optional
                Number of future rounds to decide next performance on, by default 1.
            metric : str, optional
                The metric for which to decide the top users by, by default 'tcPercentile'.
            quantile : float, optional
                The top quantile of users to select, by default 0.5.
    
            Returns
            -------
            pandas Dataframe.
                Performance of top users in future rounds per round.
            """
            relevant_rounds = self._get_relevant_rounds()
            df = relevant_rounds.apply(
                lambda x:  self._get_top_quantile_next_rounds_performance(
                    x, rounds_past, rounds_next, metric, quantile)
                    )
            return df
    
        def _get_top_quantile_same_round_performance(self, round_number, metric, quantile):
            """Get performance of top quantile users for a round.
            """
            df_round = self._get_performance_data_of_round(round_number)
            top_users = self._get_top_users(df_round, metric, quantile)
            mean_scores_top_users = self._get_mean_scores_users(df_round, top_users)
    
            mean_scores_top_users['roundNumber'] = round_number
            mean_scores_top_users['quantile_metric'] = metric
            mean_scores_top_users['quantile'] = quantile
    
            return mean_scores_top_users
    
        def _get_performance_data_of_round(self, round_number):
            """Get performance data for a round."""
            df = self.performance_per_round[self.performance_per_round.roundNumber == round_number]
            return df
    
        def _get_top_quantile_next_rounds_performance(self, round_number, rounds_past, rounds_next,
                                                      metric, quantile):
            """Get future performance of top quantile users for a round."""
    
            # find bounds past and next rounds
            first_round_forward = self._get_first_round_after_resolve(round_number)
            past_round_bounds = (round_number - (rounds_past - 1), round_number)
            next_round_bounds = (first_round_forward, first_round_forward + (rounds_next - 1))
    
            # Filter by rounds bound and same model number
            df_relevant_rounds = self.performance_per_round[
                self.performance_per_round.roundNumber.between(*past_round_bounds) |
                self.performance_per_round.roundNumber.between(*next_round_bounds)
            ]
    
            df_relevant_rounds = self._filter_same_model_number(df_relevant_rounds)
    
            # Get top users past rounds
            self._assert_all_rounds_in_df(df_relevant_rounds, *past_round_bounds)
            df_past_rounds = self._filter_df_by_round_bounds(df_relevant_rounds, *past_round_bounds)
            top_users = self._get_top_users(df_past_rounds, metric, quantile)
    
            # Get top users next rounds
            self._assert_all_rounds_in_df(df_relevant_rounds, *next_round_bounds)
            df_future_rounds = self._filter_df_by_round_bounds(df_relevant_rounds, *next_round_bounds)
            mean_scores_top_users = self._get_mean_scores_users(df_future_rounds, top_users)
            mean_scores_top_users['quantile_metric'] = metric
            mean_scores_top_users['quantile'] = quantile
            mean_scores_top_users['past_rounds_min'] = past_round_bounds[0]
            mean_scores_top_users['past_rounds_max'] = past_round_bounds[1]
            mean_scores_top_users['next_rounds_min'] = next_round_bounds[0]
            mean_scores_top_users['next_rounds_max'] = next_round_bounds[1]
    
            return mean_scores_top_users
    
        def get_quantile_mean_results_next(self, rounds_past, rounds_next, metric):
            """For each quantile from 0.00 to 0.95 (steps 0.01), get mean top performance
            for future rounds.
    
            Parameters
            ----------
            rounds_past : int
                Number of rounds to rank past performance on.
            rounds_next : int
                Number of rounds to rank future performance on.
            metric : str
                Metric to rank users on.
    
            Returns
            -------
            pandas DataFrame
                Per quantile the future mean performance of users.
            """
            relevant_quantiles = pd.Series([q / 100 for q in range(96)])
    
            df = relevant_quantiles.apply(
                    lambda x:  self.get_mean_top_quantile_next_round_performance(
                        rounds_past, rounds_next, metric, x)
                        )
    
            df = df.set_index('quantile')
            return df
    
        def get_quantile_results_same(self, metric):
            """For each quantile from 0.00 to 0.95 (steps 0.01), get mean top performance
            for same rounds
    
            Parameters
            ----------
            metric : str
                Metric to rank users on.
    
            Returns
            -------
            pandas DataFrame
                Per quantile the same round mean performance of users.
            """
            relevant_quantiles = pd.Series([q / 100 for q in range(96)])
    
            df = relevant_quantiles.apply(
                    lambda q:  self.get_mean_top_quantile_same_round_performance(
                        metric, q)
                        )
    
            df = df.set_index('quantile')
            return df
    
        def _filter_df_by_round_bounds(self, df, min_round, max_round):
            """Filter df to be within given bounds"""
            return df[df.roundNumber.between(min_round, max_round)]
    
        def _filter_same_model_number(self, df):
            """Filter the df to only contain data from users who had the same model_number in all the rounds
            """
            pivot_df = df.pivot(index='username', columns='roundNumber', values='model_number')
            pivot_df = pivot_df[pivot_df.notna().all(axis=1)]
            same_model_users = pivot_df.index[pivot_df.min(axis=1) == pivot_df.max(axis=1)]
            return df[df.username.isin(same_model_users)]
    
        def _get_first_round_after_resolve(self, round_number):
            """Finds the next round after round_number resolved"""
            return round_number + 5
    
        def _get_mean_multiple_same_pandas_objects(self, df_list):
            """For pandas objects with similar index/columns, find the mean of the objects.
            """
            sum_df = reduce(lambda x, y: x + y, df_list)
            mean_df = sum_df / len(df_list)
            return mean_df
    
        def _get_top_users(self, df_per_round, metric, quantile):
            """Retrieve top users in a round given a metric and by some quantile cutoff"""
            scores_agg = df_per_round.groupby('username')[metric].mean()
            score_threshold = scores_agg.quantile(quantile)
            top_users = scores_agg.index[scores_agg > score_threshold]
            return top_users
    
        def _get_mean_scores_users(self, df_per_round, users):
            """Compute mean scores of users in a specific round"""
            scores_agg = df_per_round.groupby('username')[PERCENTILE_COLUMNS].mean()
            rounds_quantile_scores = scores_agg.rank(pct=True)
    
            round_quantile_top_users = rounds_quantile_scores.loc[users]
            mean_scores_top_users = round_quantile_top_users.mean()
            return mean_scores_top_users
    
        def _assert_all_rounds_in_df(self, df, min_round_range, max_round_range):
            """Assert that all required rounds are in the DataFrame."""
            rounds = pd.Series(range(min_round_range, max_round_range + 1))
            try:
                assert(rounds.isin(df.roundNumber).all())
            except AssertionError as e:
                for round_ in rounds:
                    if round_ not in df.roundNumber.values:
                        print(f'{round_} is missing')
                raise(e)

---

### Post #4 — **wigglemuse** | 2022-03-27 15:58 UTC

Some very interesting analysis. Thank you!

What resonates most for me is the expected value vs actual outcome discussion. If you can calculate expected value (which is a stable measure) and then compare it to actual individual outcomes over time (which are unstable with a lot of randomness), of course eventually they should converge with the average actual outcome conforming to your calculated expected value. Expected value is what you should be based your betting on, but still in poker you get paid on the actual results of the hands as played, not for your expected value calculation. And so transferring the analogy to Numerai, you’d get paid on TC (individual results) not on the measure you used to decide whether one bet was better than another. Does the result of one poker hand predict the result of the next poker hand? No, right? Yet that’s how you get paid in poker, one hand at a time. (So Numerai and poker are maybe more similar than you were getting at there.)

_However_ , if it could really be shown conclusively that something like FNCv3 eventually converges to be equivalent (or better) to TC in the long-run, then using that more stable measure probably would be best.

If they drop corr payouts entirely, I think that might make things too unstable and create an unnecessarily moving target. I keep coming around to the idea that dropping straight corr in favor of FNC might be better, but with there being no longer payouts on MMC which is so dependent on corr ranking that’s less important. (Betting on MMC tends to incentivize straight corr over FNC, whereas TC is neutralized as part of the process so that won’t matter so much.)

And then there is the fact that nobody has been trying to optimize for TC so far, so we really don’t know what that looks like – it could be much more stable once people do. I will certainly be moving away from my more stable corr models to ones that are obviously more stable on TC. (And I do see that there are differences in stability of TC between models, but the better TC models aren’t the same models I’m betting on under current scheme.) Though I do worry about possible major TC variance causing some massive drawdowns that will put people off.

---

### Post #5 — **luee** | 2022-03-27 16:01 UTC

Awesome work, hmm I guess to steelman TC it may be that the fact we are not currently incentivized to maximize it causes it to be so unstable.

Essentially, a model that does not compete on pure corr right now but is very differentiated and still positive would not be part of your sample (since we have no incentive to stake those models) and may have stable TC. As long as the Numerai team is open to iterating within a quarter or so it seems like an interesting experiment in promoting diversity of models

---

### Post #6 — **johnnywhippet** | 2022-03-27 17:41 UTC

Excellent.

——————-  
JW.

---

### Post #7 — **gammarat** | 2022-03-27 21:18 UTC

II quite appreciate your analysis [@johnnywhippet](</u/johnnywhippet>). But I think that I approach TC from a slightly different perspective: if Numerai thinks TC is the best possible target indicator (at the moment) to improve hedge fund performance, then I’ll work with that.

As for the noisiness of TC, it’s probably a good idea to make full use of all the models one can (currently 50), and not rely too much on history from one, or a few models.

NB. I’ve only been in this for a year or so, and change architectures pretty often. It’s pretty instructive to go back and look at which ones have done well on TC, and which haven’t.

---

### Post #8 — **johnnywhippet** | 2022-03-27 21:52 UTC _(reply to #7)_

Thanks [@gammarat](</u/gammarat>). GAMMARAT36 seems to be doing very nicely for TC so well done. I don’t think this analysis will change Numerai’s mind, they’ve gone with it and I agree with you, we’ll have to work with it. I have a couple of decent models with reasonable TC and I think they’ll cut it. Maybe. As for improving TC for those models, honest answer is I’m not confident as I don’t fully understand TC yet and I’m trying to avoid a petulant “can’t be arsed with it now” mindset as it may be beyond me and I’m midway through exam season. I’m a wannabe social/political scientist not a data scientist so I’ll leave it for now and come back to it. I’m disappointed TC has dropped so quickly though and I’m really disappointed at having to retire BillyWhizz and BearsBritches so soon. Though they’ve served me well they just won’t cut it under the new regime.

NB: My first full year is coming up soon… and I’ve made a point of architecting my models differently too.

---

### Post #9 — **wigglemuse** | 2022-03-27 22:41 UTC

You can always bet on CORR only as a transition. I think Numerai will be willing to change their mind if it obviously isn’t working, but they’ll have to see it not working first.

---

### Post #10 — **johnnywhippet** | 2022-03-27 23:02 UTC _(reply to #9)_

Yeah, I can but the returns will be poor enough to make doing it nigh on pointless. Very poor if the last 6 rounds are anything to go by. I have three models with _decent_ CORR & TC scores I could use but as yet haven’t yet got the understanding to improve them though I have some ideas but not the time to put them to the test. Time will tell with TC. For sure, Numerai will do whatever is appropriate for them, I just would’ve liked a longer transition period.

---

### Post #11 — **gammarat** | 2022-03-28 01:33 UTC _(reply to #8)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/johnnywhippet/48/2803_2.png) johnnywhippet:

> I’m a wannabe social/political scientist not a data scientist

![:laughing:](http://forum.numer.ai/images/emoji/twitter/laughing.png?v=12) I’m a retired applied math guy (12+ years now) so I’ve got lots of time to play…But right now my general architecture is based on a genetic algorithm determining parameters for a Gaussian Mixture model approach for individual models (models 1-25) and ganged models (26-50). It’s been fascinating to watch populations of models rise, fall, and then disappear over thousands of generations looking for a handful that might be robust…And I have yet to incorporate feature neutralization and the like. So I’ll be at this for awhile. Impoverished, but entertained ![:+1:](http://forum.numer.ai/images/emoji/twitter/+1.png?v=12)

---

### Post #12 — **richai** | 2022-03-28 01:52 UTC

A post worthy of a retroactive bounty from the Council of Elders if I ever saw one! Excellent work.

In your analysis where you looked at round to round correlation of these metrics did you exclude overlapping rounds? It might be worth dropping 3/4th of the rounds to make it non-overlapping.

Have you tried extending the periods in your analysis? For example, instead of looking a someone’s TC in round k and comparing it to their TC in round k+1, does it work to instead take someone’s _TC Reputation_ (20 round average of TC) to predict their _TC Reputation_ for the next 20 rounds? This might smooth the results (more hands of poker reveals the better players). Is TC Reputation still much less predictive of FNC Reputation? I’m guess FNC Reputation still might win for the reasons you point out.

We ran some simulations where we simulated user payouts assuming everyone was staking on CORR + 1x TC, and backtests on this evolving meta model do make more return than paying on CORR alone. These simulations of course don’t show the whole picture because they can’t simulate the changes users would have made to their models or stakes under this TC feedback.

---

### Post #13 — **aventurine** | 2022-03-28 05:06 UTC _(reply to #12)_

I feel like this defiantly fits in with this under discussion [[Proposal] Bounty for high quality data science posts - #5 by aventurine](<http://forum.numer.ai/t/proposal-bounty-for-high-quality-data-science-posts/3996/5>)

---

### Post #14 — **bvmcheckking** | 2022-03-28 05:53 UTC _(reply to #12)_

Thank you for the nice words Richard. I have been excluding overlapping rounds indeed, so I would be comparing for example (if they were finished) round 304 with round 309.

Looking both forwards 20 rounds and backwards 20 rounds would get me into the problem of wanting to use data with no big change in there. I suspect for example that the historical performance of models mattered less when the 10x data got into play. I think especially what is missing is at looking more rounds afterwards, since the payment on one round cares not just about one round after but all rounds after. I will make an extension to this when I have time, hopefully tonight.

Ah good to hear about your backtests. My CORR vs next TC graph also seems to indicate that paying for CORR to optimize future TC (which should equate to higher returns) does not seem to be the best. Maybe comparing one payout (CORR) versus 2 payouts (CORR + 1x TC) is not the most clean way to compare results. Maybe it makes more sense to compare CORR + 1x TC with CORR + 1x MMC?

---

### Post #15 — **mdo** | 2022-03-28 19:16 UTC _(reply to #14)_

[@bvmcheckking](</u/bvmcheckking>) Thanks for the analysis! We did indeed compare backtest simulations using lots of permutations of payout systems including both CORR + 1x MMC and CORR + 2x MMC. The best ones were either TC alone or in addition to CORR.

There are a few reasons we would rather not use FNC is the payout metric. We don’t want to completely disincientize any feature exposure. Some amount of feature exposure and/or feature timing models can be beneficial and thus TC can incentivize a much wider range of possible models. Furthermore, TC helps reward originality in a way that FNC does not.

I’ve also done some analyses that are complementary to what you’ve done, but don’t seem quite as dire and add a bit of color to the situation.  
These histogram of correlations of the scores of all users at a given era with the score at the next non-overlapped future era.  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/d/d7bc5216d646eb302f09ddd8e961057c83c49cfc.png)image487×397 10.9 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/d/d7bc5216d646eb302f09ddd8e961057c83c49cfc.png> "image")

  
The above plot suggests to me that both FNC and TC are decent proxies for future TC, but the relationship is of course noisy.

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/3/370cfca7f8a6592adc4e55c6c1e5b34c3d1f2db5.png)image487×397 4.93 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/3/370cfca7f8a6592adc4e55c6c1e5b34c3d1f2db5.png> "image")

  
I find the above plot quite interesting. It agrees with your analysis that, on average, FNC decently predicts future FNC. _But_ , there are a large number of times where the relationship is strongly negatively correlated, <-0.1, many more than in the above plots involving TC.  
So, all in all, TC still seems like a good payout metric to me and targeting good FNC scores still seems like a good way to get there.

Also, FWIW the TC code is actually fairly simple, it’s all in the original post.

Thanks again for the thoughtful analysis and further discussion is of course most welcome!

---

### Post #16 — **aventurine** | 2022-03-28 20:25 UTC _(reply to #3)_

Can you tell me a round about amount of time in hours it took you too code this and put this post together? Could spark more discussion and a possible approval of the Bounty for high quality data science posts if the rest of the community wants to see more community members doing this type of work.

---

### Post #17 — **bvmcheckking** | 2022-03-29 20:57 UTC _(reply to #12)_

# Goals extension

I tried thinking a bit more about the reasons of increasing the number of last/past rounds for determining the top quantiles, or for increasing the numbers of the next/future rounds. I think the following makes sense:

For the backtest we should take into account that we get paid for our results in individual rounds and not multiple rounds, but that these payouts do have effect on all future rounds. So for the backtest we are interested in adding more future rounds, but not per se in increasing the number of past rounds.

As participants we are interested in how we can most accurately estimate our future performance. We would definitely want to add extra past rounds to see if that more accurately predicts the future. For adding future rounds I think it depends a bit on your goal. Personally I update my staking ensemble on a weekly basis so I am interested to see how predictive a multitude of past rounds are to predict the next round. Other participants might prefer to re-decide their staking model on a less frequent basis. Those participants are more interested in looking at the past results of multiple rounds to predict the future results of multiple rounds.

So keeping this in mind I am going to show graphs of these 3 situations. I have relatively arbitrarily decided to set the number of multiple rounds at 5. This due to computational time required to create these graphs so not wanting to check too many options, not wanting to pick a number too big which would reduce the number of comparisons I can make and wanting too have at least one completely not overlapping round.

# Graphs

### ‘Backtest’ / last vs next 5 TC

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/c/c8e49a56a9ebf7279ed6c06e2304eddb1a6b147a_2_690x249.png)image2236×810 128 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/c/c8e49a56a9ebf7279ed6c06e2304eddb1a6b147a.png> "image")

In here we can see again that FNC again seems most predictive, corr is doing pretty well now as well, mmc not that well. TC seems to be doing fine, up to the top 20%-5% (I cut off the top 4%-1% for all graphs due to instability of results due too few users in this top). The not so great performance of TC in the top quantile is not that great, especially due to TC seeming to be a metric which pays out a lot more top-heavy than the other metrics.

### ‘Participant evaluating, frequent rebalancing’/ last 5 vs next TC

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/a/a3108eabc754d9c65980205206430e080db1609c_2_690x245.png)image2222×790 129 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/a/a3108eabc754d9c65980205206430e080db1609c.png> "image")

Now FNC and MMC seem to be most predictive, followed by TC and then CORR. So for making your weekly rebalancing in the coming TC period, it might make sense to look at a combination of your FNC and MMC past results.

### ‘Participant evaluating, infrequent rebalancing’/ last 5 vs next 5 TC

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/0/0a0cb8794ac05bd3b71d693b39e774740c119720_2_690x244.png)image2204×782 135 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/0/0a0cb8794ac05bd3b71d693b39e774740c119720.png> "image")

… This seems not very in line with previous results. CORR and MMC performing exceptionally bad, and MMC performing off the chart (slightly), performing well at the top as well.

# Explanation

Unfortunately, I don’t really have one. So I am hoping somebody else is able to make sense of it. A prime contender for the most likely cause would in my mind be a bug. But I think this might not be so. I have done some extra testing and also created the graph for metrics vs themselves and to me these non-TC graphs seem very plausible:  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/e/e29da8fa7e221d6ef4350a0c901892a14ac1bf9f_2_690x245.png)image2216×788 159 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/e/e29da8fa7e221d6ef4350a0c901892a14ac1bf9f.png> "image")

# Details

The quantiles for metrics of multiple rounds are defined by looking at the best average performances by quantile (e.g. good score for MMC quantile would be 95%), not by the metric (e.g. good score for MMC would be 0.04) itself. An argument could also be made defining quantiles by the avg. metric score, but the way my code was set up it was easiest to extend it in this manner.

# Code update

Because this potential bug is bothering me a bit I will refactor the code a bit and then edit the previous code (the 2nd and 3rd comment). If I do find a bug I will notify you guys

---

### Post #18 — **bvmcheckking** | 2022-03-29 21:08 UTC

[@aventurine](</u/aventurine>), thank you for lobbying for this/me ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=10) . I would have wanted to respond earlier but I felt like I had to first create the reply to Richard that I promised before and that took a bit longer due overestimating the time I would have and underestimating the time it would take to create that reply ![:wink:](http://forum.numer.ai/images/emoji/twitter/wink.png?v=10) . Anyways, creating the initial forum post + code took me about 16 hours.

[@mdo](</u/mdo>) very nice to see some of the results, thank you. If I am looking at your results I think to see as well that FNC → TC has a bit higher average correlation, but also higher variance per round. I wonder if this is the same in the rounds where I looked at (I think your analysis takes all rounds up to a few years back?). Maybe this higher variance could be a potential cause for the confusing last 5 vs next 5 graph I produced. Will need to think / delve into that one a bit more.

---

### Post #19 — **richai** | 2022-03-29 21:45 UTC _(reply to #17)_

This looks like a good result for TC to me.

The idea is that yes TC can be noisy in single rounds but taking the last non-overlapping 5 rounds (or longer) of average TC scores can give a good sense of how good the subsequent TC of a model will be.

Based on your results, it seems like a model with high TC on a TC-ranked leaderboard is more likely stay high than a high CORR model on a CORR leaderboard. I think this is a really good thing.

---

### Post #20 — **of_s** | 2022-03-29 23:00 UTC

The volatility drag associated from the weekly TC noise is a serious concern for staking and should not be smoothed for analysis as this alternative scenario will not materialize to realized returns.

[en.wikipedia.org](<https://en.wikipedia.org/wiki/Volatility_tax>)

### [Volatility tax](<https://en.wikipedia.org/wiki/Volatility_tax>)

The volatility tax is a mathematical finance term, formalized by hedge fund manager Mark Spitznagel, describing the effect of large investment losses (or volatility) on compound returns. It has also been called volatility drag, volatility decay or variance drain. This is not literally a tax in the sense of a levy imposed by a government, but the mathematical difference between geometric averages compared to arithmetic averages. This difference resembles a tax due to the mathematics whic As Spitz...

---

### Post #21 — **aventurine** | 2022-03-29 23:01 UTC _(reply to #18)_

The CoE will get together before Numercon in person and go over this and then possibly get the Bounty for High Quality Data Science Posts passed once we frame it the right way. Possible we can try to do retro bounty for this and in the future once the Bounty for High Quality Data Science Posts passes, community members would write up a short summaries of what they want to work on for a project and time required and we can do approvals before articles are written if that makes sense.

---

### Post #22 — **mic** | 2022-03-30 00:55 UTC

I understand the key point you are debating is the randomness and volatility of TC (or not).

But just a couple of comments on the “other problems”:

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/numerai.discourse.group/bvmcheckking/48/1412_2.png) bvmcheckking:

> TC will reduce the ability of the participants to confirm the correctness of payouts.

Could you elaborate on this? I’m not sure how payout correctness can be confirmed under any of the metrics.

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/numerai.discourse.group/bvmcheckking/48/1412_2.png) bvmcheckking:

> Looking at the results of a round you will generally see multiple people in the top 20 with negative TC’s

There are some negative TCs up there, but many of them appear to be duplicate submissions. The number might drop significantly if you delete the duplicates. (Maybe this has an effect on the analysis?)

[![Screenshot from 2022-03-30 11-44-14](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/6/673437ca14b52378988b47b2f22f841b8515cbab_2_262x500.png)Screenshot from 2022-03-30 11-44-14594×1133 99.9 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/6/673437ca14b52378988b47b2f22f841b8515cbab.png> "Screenshot from 2022-03-30 11-44-14")

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/numerai.discourse.group/bvmcheckking/48/1412_2.png) bvmcheckking:

> Not being able to use this signal seems to be a mistake in the optimizer to me, not in their predictions

I’m not sure negative TC (or near zero, even more so) means the optimiser is unable to use the signal. If the signal is unique, then yes, the optimiser doesn’t want to use it. But if the signal is common, then it means it is already used optimally, or too much, and using it more won’t help.

---

### Post #23 — **bvmcheckking** | 2022-03-30 17:20 UTC _(reply to #22)_

> Blockquote  
>  Could you elaborate on this? I’m not sure how payout correctness can be confirmed under any of the metrics.

With this I actually meant the correctness of the scores/metrics. It would still be pretty hard but if a few participants who use 50 models were to collaborate they could use the predictions of their hundreds of model to see if there would be any possible realized results of the stocks we predict that make sense with the correlation score they got in the end. With TC something like this seems impossible to me.

> Blockquote  
>  There are some negative TCs up there, but many of them appear to be duplicate submissions. The number might drop significantly if you delete the duplicates. (Maybe this has an effect on the analysis?)

About the duplicates I don’t think it changes it that much, because I think any would already be very weird. Randomly eyeballing a few rounds I came up on [round 295](<https://numer.ai/round/295>), where I am counting 6 unique negative TC scores in the top 20. Actually another thing which is pretty surprising is looking at kwak_09 and kwak_10 at round 295.

![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/4/4b97b3b9c925305558a074f344c755226cae8c57_2_690x26.png)  
![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/d/dd330e81f0fdc389b83e079131d4529b31fea7ca_2_690x28.png)

**The names, the CORR, the MMC, the FNC, FNCv3 and Corr with meta model seem to indicate that these models are very similar. But the percentile scores are 29 and 78, going from -0.0159 to 0.0326.**

> Blockquote  
>  I’m not sure negative TC (or near zero, even more so) means the optimiser is unable to use the signal. If the signal is unique, then yes, the optimiser doesn’t want to use it. But if the signal is common, then it means it is already used optimally, or too much, and using it more won’t help.

Many models at the top 20 also don’t have real stakes on it either. For example looking at the top 20 of round 295 again, you can see that none of these models have a stake higher than 0.021 so they are basically unused. So these signals are unused, and for some reason the TC implies they won’t help either. Also I went through them and all of them were also very unique as well, CORR with meta model all below 0.5 with many around 0.2.

**And this is all just very weird to me. Models whose individual predictions probably highly outperformed the meta model and also being very unique signals are seen as not contributing to the meta model. These models, as indicated by MMC, are extremely valuable for improving the meta model’s performance. Normally I would think this is exactly what a hedge fund looks for, but apparently, according to numerai’s new metric to judge these models they would rather be a drag on the ecosystem instead of a great asset.**

---

### Post #24 — **bvmcheckking** | 2022-03-30 17:34 UTC _(reply to #19)_

I agree that long-term stability is a good thing for the participant’s perspective. For the back test / hedge fund’s performance I think this matters less, since you pay out for weekly results, and not for the average of multiple rounds.

Although TC seems on a 5 round basis more stable than CORR, currently we are replacing MMC with TC and not CORR with TC, so I am not sure how important this is. MMC seems slightly more stable on this metric as well. If this type of stability is a big concern, then these graphs indicate that FNC is a very interesting choice because it blows the other metrics out of the water on this aspect.

Also, I would like to get the thing I pointed out in the other post under your attention as well. That I randomly stumbled on a model that performs hugely similar in a round on every metric, but very differently under TC. Specifically round 295 kwak_9 and kwak_10.

---

### Post #25 — **gammarat** | 2022-03-30 21:10 UTC _(reply to #23)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/bvmcheckking/48/1412_2.png) bvmcheckking:

> Models whose individual predictions probably highly outperformed the meta model and also being very unique signals are seen as not contributing to the meta model.

That might happen if the model, while correlated to the market, was quite different from the meta model, and that if one were to trace a path from one to the other, there might be local minima? If that were the case, then the slight perturbation used to determine the TC would result in a negative result, while a large perturbation might be positive.

As for your idea for those of us with large numbers of models collaborating, I would be happy to contribute. Right now I’m playing with genetic algorithms and looking at resultant (Spearman) correlations between my submissions. In the Tournament they are performing abysmally, but they are giving me some understanding of TC.

---

### Post #26 — **bvmcheckking** | 2022-04-03 18:15 UTC

Hey all. I updated the code because I had some fear of having created a bug earlier, due to some surprising results for me. Having updated the code I don’t think the previous contained any bug.

It also made me realize how few rounds I used to create some graphs. Originally I wanted to only use data after the latest change, the 10X data. This only allowed me to have rounds from round 285-304 in my analysis. Now if you want to take the last 5 rounds, skip 4 rounds due to that being the first round where those 5 rounds are available, and then take the average of the next 5 rounds. You basically only can do this for 6 rounds. (First round you can start is when you take 285-289 as the past performance rounds, and last one being where you take 291-295 as past performance and thus 300-304 as future performance).

**Because of this I decided to recreate the graphs as well using the data from round 251-304, allowing me to use 41 rounds of data.** This would reduce the variance of these graphs by a lot, but also might cause bias due to both old rounds being less relevant in general (e.g. not having the 10x data) and also I feel that the moments where a new change was introduced are unfair to compare percentiles over rounds with.

### ‘Backtest’ / last vs next 5 TC

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/b/b92e26b0183bc3e4203b6702d333690142dd2ec4_2_690x239.png)image1868×648 140 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/b/b92e26b0183bc3e4203b6702d333690142dd2ec4.png> "image")

### ‘Participant evaluating, frequent rebalancing’/ last 5 vs next TC

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/b/b266f1c80729be21a47a600e2d4023e9159f28d4_2_690x237.png)image2202×758 117 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/b/b266f1c80729be21a47a600e2d4023e9159f28d4.png> "image")

### ‘Participant evaluating, infrequent rebalancing’/ last 5 vs next 5 TC

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/1/1d601c44d2abd8cab64dd116359e4fbd6852e2a3_2_690x246.png)image2202×788 126 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/1/1d601c44d2abd8cab64dd116359e4fbd6852e2a3.png> "image")

**Adding this extra data in general show that last year both Corr and MMC have not performed well on future TC. TC’s performance has increased w.r.t. the recent date in general. TC and FNC seem to have performed on a similar level, with TC performing slightly better. Maybe FNCv3 would outperform TC.**

### Metric vs own metric, last 5 vs next 5

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/1/12df10ed8c34c5e6610f3fa23164fdf021d4033f_2_690x244.png)image1826×648 145 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/1/12df10ed8c34c5e6610f3fa23164fdf021d4033f.png> "image")

This shows that in the last year TC was the least stable metric of the four last year.

# Conclusion

**Taking the whole last year it seems that TC is the best metric to optimize future TC when looking 5 rounds ahead and taking 5 rounds of past performances. FNC seems to perform on a similar level, but slightly worse. Corr and MMC don’t seem to work very well.**

**Past performances of TC seem least predictive for future performance for its own metric. So TC can be seen as the least stable of the four. So one can expect bigger variance in this metric then you were used to in the past.**

**I personally also expect some higher variance in TC compared to normal at the start of the implementation 9th of April, because people will be picking different models to stake on due to the new payout structure.**

---

### Post #27 — **aventurine** | 2022-04-04 17:58 UTC _(reply to #26)_

Please DM me a wallet address. Retro bounty will be queued up. Bounty for High Quality data science posts we are working the details but we might ask for your help in the next couple weeks to transfer this over to another section of forums or putting it in an article format for sending out in the newsletter but we will get back to you. Thanks for the detailed post! We will want to see more of these types of posts soon!

---

### Post #28 — **richai** | 2022-04-09 03:35 UTC _(reply to #26)_

Thank you for this!

I had an idea you might be interested in checking. Is the last 5 rounds (or longer) Sharpe of TC more predictive of future TC than the last 5 rounds mean of TC? Sharpe meaning mean(TC)/std(TC).

I think it makes sense to a lot of people that high CORR Sharpe might be more predictive of future CORR than high mean CORR so maybe a similar thing applies to TC.

When I look at user profiles, I find myself switching their TC graph to cumulative mode to see that it’s a straight line up with low “TC drawdowns” and consistent upward TC i.e. high Sharpe. Maybe this is something we can display on profiles.

---

### Post #29 — **greyone** | 2022-04-11 14:30 UTC

TC Factor Analysis for 22 Rounds from 285 to 306. Used non-overlapping Rounds to see how factors would predict TC in future round. For example, for round 306, used rounds 296-301. Factors were total TC for 3,4,5 and 6 rounds, Sharpe for 5 and 6 rounds, Standard Dev for 6 rounds and Momentum (TC of nearest 3 rounds - TC from furthest 3 rounds). Factors were quintiled and average TC of future round was calculated and linked together over 22 rounds. Then graphed as Quintile index / Average Index. Here are results:  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/d/dc8482fdaabd86350a2893ccae7e59915c928167_2_690x302.png)image1501×658 47.5 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/d/dc8482fdaabd86350a2893ccae7e59915c928167.png> "image")

  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/4/4497f140e4e116f9a95efd14af83fdd93e8a0257_2_690x296.png)image1514×650 50 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/4/4497f140e4e116f9a95efd14af83fdd93e8a0257.png> "image")

  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/5/5f940d87efcf1682cbef4d857265d676056e5144_2_690x301.png)image1501×656 51.5 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/5/5f940d87efcf1682cbef4d857265d676056e5144.png> "image")

  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/4/4b78bfd028e42f9d1f86c38db7d30119c231d815_2_690x297.png)image1509×650 52.6 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/4/4b78bfd028e42f9d1f86c38db7d30119c231d815.png> "image")

  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/c/c14e849be6779f4564eb76bf95943477dfe953a0_2_690x301.png)image1497×654 50.6 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/c/c14e849be6779f4564eb76bf95943477dfe953a0.png> "image")

  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/d/dec630739ea6ec015b0b409f703165270e072c1b_2_690x302.png)image1503×659 54.8 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/d/dec630739ea6ec015b0b409f703165270e072c1b.png> "image")

  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/d/d75bd963e2a06e0261108d36df029123370a7e21_2_690x303.png)image1512×665 56.9 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/d/d75bd963e2a06e0261108d36df029123370a7e21.png> "image")

  
I can explain more later…need to spend some time today at homefront.

---

### Post #30 — **greyone** | 2022-04-12 15:55 UTC

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/9/907cdffcf651c91d58dbd3bfd9ec771c99eab0aa_2_677x500.png)image828×611 27.4 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/9/907cdffcf651c91d58dbd3bfd9ec771c99eab0aa.png> "image")

  
In the spirit of biased pattern recognition, 3 past quintile series were chosen that preceded Sharpe6 Q1’s decline. Selecting series for -TC6 Q4, -SD6 Q2 and -Mo Q2, scaling to be equivalent to Sharpe6 Q1 and then averaging the 3 series produces as surefire leading Sharpe6 Q1 indicator of era change! :))
