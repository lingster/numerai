# Numerai Utils

This contains a collection of python tools to allow you to compare models and benchmark your models against others in the tournament

## Installation
You will need to have python install and also install uv. Then run:
``` bash
uv sync
```

To run a comparison run:
You will need either the model name(if you own it or to look up the model id, which
is normally a UUID

You can use chrome dev tools and peek at the http/fetch/xhr requests in one of the payloads you should see something like this:

{"query":"\n  query v2RoundModelPerformances($modelId: String, $roundNumber__eq: Int, $roundNumber__gte: Int, $tournament: Int, $distinctOnRound: Boolean, $lastNRounds: Int, $submittedOnly: Boolean, $resolvedOnly: Boolean, $resolvedWithinLastNDays: Int, $scoredWithinLastNDays: Int) {\n    v2RoundModelPerformances(\n        modelId: $modelId,\n        roundNumber__eq: $roundNumber__eq,\n        roundNumber__gte: $roundNumber__gte,\n        lastNRounds: $lastNRounds,\n        distinctOnRound: $distinctOnRound,\n        tournament: $tournament,\n        submittedOnly: $submittedOnly,\n        resolvedOnly: $resolvedOnly,\n        resolvedWithinLastNDays: $resolvedWithinLastNDays,\n        scoredWithinLastNDays: $scoredWithinLastNDays\n      ) {\n      roundNumber\n      roundResolveTime\n      roundCloseStakingTime\n      roundDataDatestamp\n      roundPayoutFactor\n      roundScoreTime\n      roundResolved\n      roundTarget\n      atRisk\n      corrMultiplier\n      mmcMultiplier\n      tcMultiplier\n      churnThreshold\n      prevWeekChurnMax\n      turnoverThreshold\n      prevWeekTurnoverMax\n      submissionScores {\n        date\n        day\n        resolveDate\n        resolved\n        displayName\n        value\n        percentile\n        payoutPending\n        payoutSettled\n      }\n    }\n  }\n  ","variables":{"modelId":"6d99fd48-cb99-409f-966f-fe6a75ea2a34","roundNumber__eq":null,"roundNumber__gte":null,"lastNRounds":null,"distinctOnRound":true,"tournament":8,"submittedOnly":false,"resolvedOnly":false,"resolvedWithinLastNDays":421,"scoredWithinLastNDays":null}}


Then look for the fields modelId.


uv run compare_models.py compare --output <fn> --rounds 100 <model_a> <model_b> 



``` bash
uv run compare_models.py compare --output "t1_witchyai.csv" --rounds 100 fnc_imp_01 d7a95775-3f93-4969-bd0e-c85cd9f57c14

```



After running the command this will output a report summary should which rounds it could find and match between the 2 models as well as a csv file comparing corr and mmc values.


