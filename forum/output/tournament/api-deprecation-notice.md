---
title: "API Deprecation Notice"
category: Tournament
url: https://forum.numer.ai/t/api-deprecation-notice/6273
created_at: 2023-04-04T22:08:15.839000+00:00
last_posted_at: 2023-04-04T22:08:15.972000+00:00
posts_count: 1
views: 643
tags: []
---

# API Deprecation Notice

---

### Post #1 — **ark** | 2023-04-04 22:08 UTC

API DEPRECATION NOTICE

As of tomorrow morning, April 5, 2023, we are deprecating the following APIs; we will be removing them May 1, 2023. They will still operate at some capacity until removed, but will not return the same type of data:

  * account.models.submissions is replacing:

    * account.models.signals_submissions
  * account.models.latestSubmissions is replacing:

    * account.models.latest_submission
    * account.models.latest_signals_submission
    * account.models.latest_submission_v2
    * account.models.latest_signals_submission_v2
  * tournamentOverview.totalNetEarnings will return null

    * tournamentOverview.returns.allTimeNmr can be used instead, but only considers staking 2.0 returns and doesn’t include 1M NMR airdrop.



Additionally, when querying any of the above APIs for any “submission” objects (does NOT affect diagnostics objects) the following fields are deprecated and will only return nil / null:

  * hasDiagnostics

  * trainedOnVal

  * diagnosticStatus

  * errorInfo

  * filteredCount

  * firstEffectiveDate

  * hasHistoric

  * historicMaxDrawdown

  * historicMean

  * historicSharpe

  * historicStd

  * invalidTickers

  * status (not including the new latest_submissions API)

  * submissionIp

  * submittedCount

  * validationApy

  * validationErasAccepted

  * validationErasSubmitted

  * validationTickersAccepted

  * validationTickersSubmitted

  * validationCorrPlusMmcSharpeDiffRating

  * validationCorrelation

  * validationCorrelationRating

  * validationFeatureNeutralMean

  * validationFeatureNeutralMeanRating

  * validationSharpe

  * validationSharpeRating

  * validationStd

  * validationStdRating

  * validationMaxDrawdown

  * validationMaxDrawdownRating

  * validationMaxFeatureExposure

  * validationMaxFeatureExposureRating

  * corrWithExamplePreds

  * validationMmcMean

  * validationMmcMeanRating

  * validationCorrPlusMmcSharpe

  * validationCorrPlusMmcSharpeRating

  * validationCorrPlusMmcMean

  * validationCorrPlusMmcMeanRating

  * validationCorrPlusMmcSharpeDiff




If anything is missing in the new api that existed in the deprecated APIs, please suggest what you need below and it will be added at our earliest opportunity. Otherwise the listed deprecated APIs and fields will be removed May 1, 2023.
