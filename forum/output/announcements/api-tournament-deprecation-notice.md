---
title: "Api-tournament deprecation notice"
category: Announcements
url: https://forum.numer.ai/t/api-tournament-deprecation-notice/5942
created_at: 2022-12-15T20:43:58.648000+00:00
last_posted_at: 2023-01-15T10:46:42.516000+00:00
posts_count: 4
views: 1147
tags: []
---

# Api-tournament deprecation notice

---

### Post #1 — **chanes** | 2022-12-15 20:43 UTC

Following endpoints will stop getting new data end of next week, and will be removed completely on Jan. 31, 2023

  * `v2UserProfile`
  * `signalsUserProfile`



Any usage of these endpoints should be changed to use `v3UserProfile` or `v2SignalsProfile`

The following queries are no longer supported, any usage should be changed to use `v3UserProfile.RoundModelPerformances` or `v2SignalsProfile.RoundModelPerformances`:

  * `v2RoundDetails`
  * `RoundSubmissionPerformance`
  * `SignalsRoundSubmissionPerformance`



The following fields are no longer supported and will be removed completely next week:

  * `account.totalPendingPayouts`
  * `tournamentOverview.totalNetEarningsToday`



Ping me (@2chanes) on Rocketchat for any questions/help. We will be deprecating more endpoints/fields related to payouts in the coming weeks and will announce those once they are known.

---

### Post #2 — **kayeffnumeraitor** | 2023-01-10 11:57 UTC

At the time of this post I did not realize the full extent of these changes, but it did break a model pipeline of mine, or lets say it “freezed” my model which is the reason why it took me a while to realize.

I am using the `NumerAPI` python client from the `numerapi` package, and I want to retrieve from a given model the daily (preliminary) scores (CORR, FNC, TC, etc) from a certain round, so basically the same information like on this page: [kayeffnumeraitor daily scores](<https://numer.ai/kayeffnumeraitor/submissions/369>)

With the previous `numerapi` package, this was possible via the function “daily_submission_performance”. Now that this function is non-existent, how is the preferred way of retrieving said information?

---

### Post #3 — **chanes** | 2023-01-11 14:20 UTC _(reply to #2)_

The query we use on the frontend is:
    
    
    query v2RoundModelPerformances(modelId: "{model_id}", roundNumber__eq:330) {
      intraRoundSubmissionScores {
        date
        day
        displayName
        value
        percentile
      }
    }
    

we plan on changing this endpoint in the coming weeks to be more “flat” so API users don’t have to parse the list of scores. Let me know if that doesn’t work for you or if you have any other questions.

---

### Post #4 — **kayeffnumeraitor** | 2023-01-15 10:46 UTC _(reply to #3)_

Hello [@chanes](</u/chanes>),

thanks for the reply, and yes that works for me. If there are changes please keep us updated as always.

For those that use the python `numerapi` client, this is the code that retrieves the daily preliminary scores:
    
    
    public_id = "<Your public ID>"
    secret_key = "<Your secret key>"
    
    api = NumerAPI(public_id, secret_key)
    
    model_id = "<Your model ID>"
    round_number = 370
    
    query = """
      query($model_id: String!, $round_number: Int) {
        v2RoundModelPerformances(modelId: $model_id, roundNumber__eq:$round_number) {
          intraRoundSubmissionScores {
            date
            day
            displayName
            value
            percentile
          }
        }
      }
    """
    args = {
        'model_id': model_id,
        "round_number": round_number
    }
    api.raw_query(query, args)['data']['v2RoundModelPerformances'][0]['intraRoundSubmissionScores']
