---
title: "Introducing Queued Submissions & Submission Statuses"
category: Tournament
url: https://forum.numer.ai/t/introducing-queued-submissions-submission-statuses/6253
created_at: 2023-03-29T21:16:58.401000+00:00
last_posted_at: 2024-04-04T03:04:31.539000+00:00
posts_count: 9
views: 1287
tags: []
---

# Introducing Queued Submissions & Submission Statuses

---

### Post #1 — **ark** | 2023-03-29 21:16 UTC

# Queued Submissions

Models across all tournaments can now queue a submission for the next round. Whether or not the model has an on-time submission, it can now upload a late submission that will be automatically queued to be an on-time submission for the next round.

At the start of each new round (from round 452 onwards), queued submissions from the previous round are automatically converted to on-time submissions for the new round. You can then overwrite this on-time submission as normal if you choose.

Possible FAQs

  * What happens if I already have on-time submissions?

    * Your most recent late submission is queued for the next round and is ignored otherwise.
  * What happens if I have no submissions for a round, then submit late?

    * Your most recent late submission is treated normally (it will have all non-TC scores calculated) and is also considered queued for next round. Eventually we will stop scoring late submissions and only treat them as queued.
  * What happens if I make multiple late submissions?

    * Only your most recent late submission is considered to be queued, so all other late submissions will be ignored.



# Submission Statuses

In support of Queued Submissions, we also released a new website feature that displays basic information about each of your models recent submissions. You can find it in the models page on both the overview and submissions tables as shown here:

[![Screenshot 2023-03-29 at 2.09.57 PM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/5/51ed8bf5325571a46c476292bb94d11f8a6d7e42_2_690x359.png)Screenshot 2023-03-29 at 2.09.57 PM2332×1214 265 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/5/51ed8bf5325571a46c476292bb94d11f8a6d7e42.png> "Screenshot 2023-03-29 at 2.09.57 PM")

[![Screenshot 2023-03-29 at 2.10.10 PM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/7/731f78ae915f5324e984357812c48c2060ee14b9_2_690x358.png)Screenshot 2023-03-29 at 2.10.10 PM2330×1210 279 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/7/731f78ae915f5324e984357812c48c2060ee14b9.png> "Screenshot 2023-03-29 at 2.10.10 PM")

Here is an example of how to get this data from our GraphQL API:

Example query:
    
    
    query account {
      account {
        models {
          username
          tournament
          latestSubmissions {
            roundNumber
            roundCloseStaking
            roundClose
            roundOpen
            filename
            status
            timestamp
          }
        }
      }
    }
    

Example Response:
    
    
    {
      "data": {
        "account": {
          "models": [
            {
              "latestSubmissions": [
                {
                  "filename": null,
                  "roundClose": "2023-03-30",
                  "roundCloseStaking": "2023-03-29",
                  "roundNumber": 451,
                  "roundOpen": "2023-03-29",
                  "status": "none",
                  "timestamp": null
                },
                {
                  "filename": "numerai_example_predictions_data-TurVb05zpZGr.csv",
                  "roundClose": "2023-03-29",
                  "roundCloseStaking": "2023-03-28",
                  "roundNumber": 450,
                  "roundOpen": "2023-03-28",
                  "status": "on-time",
                  "timestamp": "2023-03-28T13:12:59Z"
                },
                {
                  "filename": "numerai_example_predictions_data-xCS8SjRTdJTy.csv",
                  "roundClose": "2023-03-28",
                  "roundCloseStaking": "2023-03-27",
                  "roundNumber": 449,
                  "roundOpen": "2023-03-25",
                  "status": "on-time",
                  "timestamp": "2023-03-25T15:12:28Z"
                }
              ],
              "tournament": 8,
              "username": "integration_test"
            },
    ...

---

### Post #2 — **qeintelligence** | 2023-03-30 18:10 UTC

Hi [@ark](</u/ark>), looks good, I assume that the time-window can still shift depending on whether or not your data providers are on-time and your pipelines have no issues? And anything outside of the 1-hour window will be considered a late submission?

---

### Post #3 — **ark** | 2023-03-30 21:03 UTC _(reply to #2)_

Yes that’s correct, for the weekend anything after 14:00 UTC Monday is considered late and for weekdays anything outside of the 1-hour window (starting no earlier than 13 UTC) is considered late.

---

### Post #4 — **thomasxthomas** | 2023-03-31 12:43 UTC _(reply to #3)_

Is that possible to carry over predictions made during weekend (the Monday submission) for 4 more daily rounds? So that data scientists who prefer to make submission at weekends only can have their predictions automatically copied into the daily rounds in weekdays?

---

### Post #5 — **ark** | 2023-04-03 15:58 UTC _(reply to #4)_

We have discussed offering this support for signals, but at this point we are confident that submissions older than 1 round will be significantly less useful to the Meta Model.

---

### Post #6 — **invalid_datatype** | 2024-04-04 00:29 UTC

Is there a way to remove a queued submission so that I can submit a proper prediction the next day?

---

### Post #7 — **wigglemuse** | 2024-04-04 01:00 UTC _(reply to #6)_

No need to remove. Just submit the proper one on time in the proper window.

---

### Post #8 — **invalid_datatype** | 2024-04-04 01:14 UTC _(reply to #7)_

Oh nice. Thanks a lot.

---

### Post #9 — **wigglemuse** | 2024-04-04 03:04 UTC

Yeah, whatever you upload last (that is accepted for the round you want it for) is the one that counts, and since “late” submissions are actually late from the previous day, if you do an on-time submission after that in the morning when the new round opens you’re all good. And I know at least some people are submitting late submissions everyday just to make sure they submit something if their pipeline breaks during the critical window. (And then there are people like me that submit late most of the time with the intention of it being used, proper or not.)
