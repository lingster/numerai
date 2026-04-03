---
title: "Some code to get your models performances by round"
category: Tournament
url: https://forum.numer.ai/t/some-code-to-get-your-models-performances-by-round/3044
created_at: 2021-04-24T17:42:19.159000+00:00
last_posted_at: 2021-04-25T09:35:52.903000+00:00
posts_count: 3
views: 1130
tags: []
---

# Some code to get your models performances by round

---

### Post #1 — **ml_is_lyf** | 2021-04-24 17:42 UTC

I’ve been keeping track of my models performances in an Excel spreadsheet, but I found it quite tedious to copy the data from the website, so today I wrote some code to get the data from numerapi in the way I wanted, and thought I’d share it in case it helps anyone else.
    
    
    from tqdm.notebook import tqdm
    import datetime
    import pytz
    import pandas as pd
    import numpy as np
    from numerapi import NumerAPI, utils
    import math
    from collections import defaultdict
    
    class CachingNumerAPIWithPercentiles(NumerAPI):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.round_details_cache = {}
            self.daily_submissions_performance_with_percentiles_cache = {}
            self.competition_cache = None
    
        def round_details(self, round_num):
            if not self.round_details_cache.get(round_num):
                self.round_details_cache[round_num] = super().round_details(round_num)
            return self.round_details_cache[round_num]
    
        def daily_submissions_performance_with_percentiles(self, username):
            if not self.daily_submissions_performance_with_percentiles_cache.get(username):
                # this is the same as NumerAPI.daily_submissions_performance but we include the percentiles in the query
                query = """
                query($username: String!) {
                    v2UserProfile(username: $username) {
                        dailySubmissionPerformances {
                            date
                            roundNumber
                            correlation
                            corrPercentile
                            mmc
                            mmcPercentile
                            fnc
                            fncPercentile
                            correlationWithMetamodel
                        }
                    }
                }
                """
                arguments = {'username': username}
                data = self.raw_query(query, arguments)['data']['v2UserProfile']
                performances = data['dailySubmissionPerformances']
                # convert strings to python objects
                for perf in performances:
                    utils.replace(perf, "date", utils.parse_datetime_string)
                # remove useless items
                performances = [p for p in performances if any([p['correlation'], p['fnc'], p['mmc']])]
                self.daily_submissions_performance_with_percentiles_cache[username] = performances
            return self.daily_submissions_performance_with_percentiles_cache[username]
    
        def get_competitions(self):
            if not self.competition_cache:
                self.competition_cache = super().get_competitions()
            return self.competition_cache
    
        def round_summary(self, round_num):
            for some_round_summmary in self.get_competitions():
                if round_num == some_round_summmary["number"]:
                    return some_round_summmary
    
    class AdvancedNumerAPI(object):
        def __init__(self, napicache=None):
            self.napicache = napicache or CachingNumerAPIWithPercentiles()
    
        def get_current_scored_round(self):
            current_round = self.napicache.get_current_round()
            if not self.napicache.round_details(current_round):
                # if there are no details the round does not have any scored values yet
                current_round-=1
            return current_round
    
        def is_round_resolved(self, round_num):
            return self.napicache.round_summary(round_num)["resolvedStaking"]
    
        def get_user_names_for_rounds(self, round_min, round_max=None, disable_tqdm=False):
            round_max = round_max or self.get_current_scored_round()
            usernames = set()
            for round_num in tqdm(range(round_min, round_max+1), disable=disable_tqdm):
                for round_detail in self.napicache.round_details(round_num):
                    usernames.add(round_detail["username"])
            return usernames
    
        def get_user_performance_by_round(self, round_min, round_max=None, model_names=None, disable_tqdm=False):
            round_max = round_max or self.get_current_scored_round()
            model_names = model_names or self.get_user_names_for_rounds(round_min, round_max, disable_tqdm=True)
            user_performance_by_round = defaultdict(dict)
            for username in tqdm(model_names, disable=disable_tqdm):
                user_daily_submissions_performance = self.napicache.daily_submissions_performance_with_percentiles(username)
                for daily_submission_performance in user_daily_submissions_performance:
                    round_number = daily_submission_performance["roundNumber"]
                    if round_number < round_min or round_number > round_max:
                        continue
                    date_of_performance = daily_submission_performance["date"]
                    prev_date_of_performance = user_performance_by_round[round_number][username]["date"] if user_performance_by_round[round_number].get(username) else datetime.datetime.min.replace(tzinfo=pytz.UTC)
                    if date_of_performance > prev_date_of_performance:
                        user_performance_by_round[round_number][username] = daily_submission_performance
            return user_performance_by_round
    
        def get_leaderboard_for_round(self, round_num=None, by="correlation", model_names=None, pct_format=True, disable_tqdm=False):
            round_num = round_num or self.get_current_scored_round()
            round_leaderboard = pd.DataFrame.from_dict(self.get_user_performance_by_round(round_num, round_num, model_names=model_names, disable_tqdm=disable_tqdm)[round_num], orient="index")
            round_leaderboard.sort_values(by=by, inplace=True, ascending=by=="correlationWithMetamodel")
            round_leaderboard.drop(["date","roundNumber"], inplace=True, axis=1)
            for column in ["corrPercentile", "mmcPercentile", "fncPercentile"]:
                round_leaderboard[column] = round_leaderboard[column]*100
                if pct_format:
                    round_leaderboard[column] = pd.Series(["{:.1f}%".format(value) for value in round_leaderboard[column].values],index=round_leaderboard[column].index)
            round_leaderboard = round_leaderboard.reindex(sorted(round_leaderboard.columns), axis=1)
            return round_leaderboard
    
        def get_percentile_ranks_for_rounds(self, model_names, round_min, round_max=None, by="correlation", colour_if_resolved=True, pct_format=True, disable_tqdm=False):
            assert(by in ["mmc", "fnc", "corr"])
            round_max = round_max or self.get_current_scored_round()
            percentile_ranks_by_round = {}
            for round_num in tqdm(range(round_min, round_max+1), disable=disable_tqdm):
                leaderboard_for_round = self.get_leaderboard_for_round(round_num, model_names=model_names, pct_format=False, disable_tqdm=True)
                percentiles_for_round = {}
                average_percentiles_for_round = []
                for model_name in model_names:
                    if model_name not in leaderboard_for_round.index:
                        percentiles_for_round[model_name] = ""
                    else:
                        average_percentiles_for_round.append(leaderboard_for_round.loc[model_name]["{}Percentile".format(by)])
                        percentiles_for_round[model_name] = leaderboard_for_round.loc[model_name]["{}Percentile".format(by)]
                # capital A so that we handle the edge case of the user "average" :)
                percentiles_for_round["Average"] = np.mean(average_percentiles_for_round)
                if pct_format:
                    for model_name in model_names+["Average"]:
                        if percentiles_for_round[model_name]!="":
                            percentiles_for_round[model_name] = "{:.1f}%".format(percentiles_for_round[model_name])
                percentile_ranks_by_round[round_num] = percentiles_for_round
            percentiles_df = pd.DataFrame.from_dict(percentile_ranks_by_round, orient="index")
            if colour_if_resolved:
                def green_if_resolved_else_orange(row):
                    colour = "green" if self.is_round_resolved(row.name) else "orange"
                    return ["color: {}".format(colour) for _ in range(len(row))]
                percentiles_df = percentiles_df.style.apply(green_if_resolved_else_orange, axis=1)
            return percentiles_df
    

This allows you to get a pandas DataFrame of the percentile ranks of all your models for CORR like so:
    
    
    anapi = AdvancedNumerAPI()
    model_names = ["ml_is_lyf"]+["ml_is_lyf_{}".format(module_num) for module_num in range(1,14)] # list of your model names
    round_min = 251 # round you want the table to start at
    anapi.get_percentile_ranks_for_rounds(model_names, round_min, by="corr")
    

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/86b3b58a9bdfc9acc316c9da78e22a7e9531f0a9.png)image1235×248 11.1 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/86b3b58a9bdfc9acc316c9da78e22a7e9531f0a9.png> "image")

You can also get them for MMC like so:
    
    
    anapi.get_percentile_ranks_for_rounds(model_names, round_min, by="mmc")
    

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/31f026c4bdfc01c15b1d8803467db7618c69bbd1.png)image1229×247 10.9 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/31f026c4bdfc01c15b1d8803467db7618c69bbd1.png> "image")

For rounds that haven’t resolved the percentiles are just the latest in your daily scores. These queries each only take a few seconds to run, so its very quick to re-run it if you want to see your daily scores.

The percentiles generated in the tables above are exactly the same as if you go and hover over your CORR/MMC for each round on your profile. But I think its nicer to have them all-together as its easier to compare your models.

I also included an average column, which is just the average of your percentile ranks in the round, as I think this gives you a better picture of how you’re doing in the tournament.

I think it is also nice to be able to look at the performance of your models by round, which you can do like so:
    
    
    anapi.get_leaderboard_for_round(256, model_names=model_names)
    

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/22b9a1ffb97c5630e32b708716e0e02d9ff49df6.png)image910×445 19.4 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/22b9a1ffb97c5630e32b708716e0e02d9ff49df6.png> "image")

By default, they are sorted by correlation, but you can use the “by” argument to sort by any column, e.g.
    
    
    anapi.get_leaderboard_for_round(256, by="mmc", model_names=model_names)
    

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/1c07db94097d6d5c04f47298c4619375538616b3.png)image919×448 19.5 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/1c07db94097d6d5c04f47298c4619375538616b3.png> "image")

You can also get the leaderboard for all participants in the round if you don’t specify any model names, this takes over 40 minutes to build though as you have to make a query for every participant in the round.
    
    
    anapi.get_leaderboard_for_round(256)
    

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/f653752b97d0c08f16c9b7a466f5c135e2bed74f.png)image977×398 15.7 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/f653752b97d0c08f16c9b7a466f5c135e2bed74f.png> "image")

Here’s a Google Colab notebook with the code ready to go with the examples above:

![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/f/f6710ac7062c5240923c6951e1e4debadf42fc28.png) [colab.research.google.com](<https://colab.research.google.com/drive/18Eq8TqMwIBGAswNWQBjPpoowBSbRKkce?usp=sharing>) ![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/568c419c14aca7a2f68749c9fff9598dd1d7b5e1.png)

### [Google Colab](<https://colab.research.google.com/drive/18Eq8TqMwIBGAswNWQBjPpoowBSbRKkce?usp=sharing>)

Let me know if you find any bugs in the code or have any questions on it, hope this is useful to others ![:slight_smile:](https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=13)

---

### Post #2 — **rw227** | 2021-04-25 05:31 UTC

one suggestion would be to display Resolved Rounds in a different font colour. Thank you

---

### Post #3 — **ml_is_lyf** | 2021-04-25 09:35 UTC _(reply to #2)_

Nice idea, I’ve just edited the code to implement that as you can see above
