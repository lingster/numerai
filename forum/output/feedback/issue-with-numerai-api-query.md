---
title: "Issue with Numerai API query"
category: Feedback
url: https://forum.numer.ai/t/issue-with-numerai-api-query/1438
created_at: 2021-01-09T10:14:12.192000+00:00
last_posted_at: 2021-01-09T10:14:12.302000+00:00
posts_count: 1
views: 769
tags: []
---

# Issue with Numerai API query

---

### Post #1 — **sirbradflies** | 2021-01-09 10:14 UTC

Hi,

I hope this is the right place to ask a question about Numerai API. I am trying to form a simple query to extract live and validation correlation and mmc for a specific submission.

I put together on GraphQL the following query for a submission already resolved:
    
    
    query {
      submissions(modelId: "MYMODELID", 
        id: "MYSUBMISSIONID") {
        liveCorrelation
        validationCorrelation
        validationMmcMean
        validationSharpe
        validationFeatureExposure
        validationCorrelation
        validationCorrelationRating
        validationSharpe
        validationSharpeRating
        validationFeatureNeutralMean
        validationFeatureNeutralMeanRating
        validationStd
        validationStdRating
        validationMaxFeatureExposure
        validationMaxFeatureExposureRating
        validationMaxDrawdown
        validationMaxDrawdownRating
        validationCorrPlusMmcSharpe
        validationCorrPlusMmcSharpeRating
        validationMmcMeanRating
        validationCorrPlusMmcSharpeDiff
        validationCorrPlusMmcSharpeDiffRating
      }
    }
    

And I get the correct results except I always get a NULL for live correlation even though the round is resolved
    
    
    {
      "data": {
        "submissions": [
          {
            "liveCorrelation": null,
            "validationCorrPlusMmcSharpe": 0.33750748411748777,
            "validationCorrPlusMmcSharpeDiff": -0.1592271021361118,
            "validationCorrPlusMmcSharpeDiffRating": 0.1815457957277764,
            "validationCorrPlusMmcSharpeRating": 0,
            "validationCorrelation": 0.007451875776995888,
            "validationCorrelationRating": 0,
            "validationFeatureExposure": null,
            "validationFeatureNeutralMean": 0.007338636949468362,
            "validationFeatureNeutralMeanRating": 0.08366480934177264,
            "validationMaxDrawdown": -0.0484167076222366,
            "validationMaxDrawdownRating": 0.7398143597529268,
            "validationMaxFeatureExposure": 0.20584137319000068,
            "validationMaxFeatureExposureRating": 0.5814873519317141,
            "validationMmcMean": 0.0011484435484292288,
            "validationMmcMeanRating": 0.5717777217768267,
            "validationSharpe": 0.49673458625359956,
            "validationSharpeRating": 0,
            "validationStd": 0.015001725233586729,
            "validationStdRating": 1
          }
        ]
      }
    }
    

Any idea how to get also the live correlation and mmc for each round?

Thank you
