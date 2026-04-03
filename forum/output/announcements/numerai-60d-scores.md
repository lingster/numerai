---
title: "Numerai 60D Scores"
category: Announcements
url: https://forum.numer.ai/t/numerai-60d-scores/8037
created_at: 2025-05-05T23:44:49.603000+00:00
last_posted_at: 2025-05-05T23:44:49.674000+00:00
posts_count: 1
views: 1393
tags: []
---

# Numerai 60D Scores

---

### Post #1 — **ark** | 2025-05-05 23:44 UTC

[![Screenshot 2025-05-05 at 14.49.48](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/b/b40afab55e52023e9a8b8bb2b490e780e59bbbda_2_690x196.png)Screenshot 2025-05-05 at 14.49.483062×872 232 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/b/b40afab55e52023e9a8b8bb2b490e780e59bbbda.png> "Screenshot 2025-05-05 at 14.49.48")

Numerai has updated our website to focus on 4 scores:

  * two existing 20D2L scores used for payouts, CORR20 and MMC20
  * two new 60D2L scores, CORR60 and MMC60.



At this time, there is no plan to change payouts or season scores to a 60-day payout scheme.

Given that the Numerai hedge fund operates on a long time horizon, research has shown that high correlation with both 20-day and 60-day targets is more easily monetizable. This is why we’ve updated the website to focus solely on the 4 scores we deeply care about.

We can immediately notice that 60D scores tend to be generally higher magnitude than 20D scores - just look at the CORR chart of the Numerai SWMM:

[![Screenshot 2025-05-05 at 16.20.08](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/b/b89b0b5d564dbb05500e5743b445f035205ff857_2_690x184.png)Screenshot 2025-05-05 at 16.20.083084×824 202 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/b/b89b0b5d564dbb05500e5743b445f035205ff857.png> "Screenshot 2025-05-05 at 16.20.08")

You can see that, while CORR20 has some flat periods, CORR60 seems to have higher return and lower volatility, leading to a much higher Sharpe Ratio:

  * CORR20 Sharpe is 1.86
  * CORR60 Sharpe is 2.97



Before today, we concentrated on showing a variety of 20-day scores such as FNCv3, BMC, and CORT20 as well as a 60-day score - CORJ60. We believed offering these scores would help users identify performant models. However, these “auxiliary” scores are less relevant for all users and could end up distracting newcomers. Also, some use older concepts or targets that are not directly aligned with our goal: high performance on the cyrus target over multiple time horizons.

We will still continue calculating these auxiliary metrics and they will be available via the scoring page and the API, but we will not be displaying them as a primary focus of our leaderboards or profile pages as they are not generally valuable as primary metrics.
