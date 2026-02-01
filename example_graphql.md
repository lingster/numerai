## get user/model performance:

The following graph ql query gets the performance of a model:
request payload:
{"query":"\n    query getV3UserProfile($username: String!, $tournament: Int!) {\n      v3UserProfile(modelName: $username, tournament: $tournament) {\n        id\n        accountName\n        username\n        startDate\n        profileUrl\n        bio\n        stakeValue\n        control\n        team\n        isActive\n        linkText\n        linkUrl\n        latestReps {\n          corr\n          corr20V2\n          mmc\n          bmc\n          corr60\n          mmc60\n          corrV4\n          fncV4\n          icV2\n          ric\n          alpha\n          mpc\n        }\n        latestRanks {\n          corr\n          corr20V2\n          mmc\n          bmc\n          corr60\n          mmc60\n          corrV4\n          fncV4\n          icV2\n          ric\n          alpha\n          mpc\n        }\n        latestReturns{\n          oneDay\n          threeMonths\n          oneYear\n          allTime\n        }\n        latestUserScores {\n          displayName\n          rank\n          reputation\n        }\n        latestSubmissionScores {\n          displayName\n          value\n          percentile\n        }\n        stakeInfo {\n          corrMultiplier\n          mmcMultiplier\n          tcMultiplier\n        }\n      }\n    }\n  ","variables":{"username":"mdel0017","tournament":8}}

response:
{
    "data": {
        "v3UserProfile": {
            "accountName": "earlie",
            "bio": null,
            "control": null,
            "id": "6d99fd48-cb99-409f-966f-fe6a75ea2a34",
            "isActive": false,
            "latestRanks": {
                "alpha": null,
                "bmc": 153,
                "corr": 4274,
                "corr20V2": 4274,
                "corr60": 5869,
                "corrV4": null,
                "fncV4": null,
                "icV2": null,
                "mmc": 1,
                "mmc60": 179,
                "mpc": null,
                "ric": null
            },
            "latestReps": {
                "alpha": null,
                "bmc": 0.010255893772717139,
                "corr": 0.009879032819174637,
                "corr20V2": 0.009879032819174637,
                "corr60": 0.008095113222276122,
                "corrV4": null,
                "fncV4": null,
                "icV2": null,
                "mmc": 0.009091994592438375,
                "mmc60": 0.008103201393141642,
                "mpc": null,
                "ric": null
            },
            "latestReturns": null,
            "latestSubmissionScores": [
                {
                    "displayName": "apcwnm",
                    "percentile": 0.0051416819012797075,
                    "value": -0.06132044119039216
                },
                {
                    "displayName": "bmc",
                    "percentile": 0.19553332557869024,
                    "value": -0.010454804245528181
                },
                {
                    "displayName": "canon_bmc",
                    "percentile": 0.3746227072208033,
                    "value": -0.004248908722171622
                },
                {
                    "displayName": "canon_corj60",
                    "percentile": 0.7830614370010414,
                    "value": -0.002775250516530696
                },
                {
                    "displayName": "canon_corr",
                    "percentile": 0.16834142486169132,
                    "value": -0.01593839186790369
                },
                {
                    "displayName": "canon_corr60",
                    "percentile": 0.9850991286778633,
                    "value": 0.030157681329479453
                },
                {
                    "displayName": "canon_cort20",
                    "percentile": 0.48263486918268117,
                    "value": -0.0037451884636736624
                },
                {
                    "displayName": "canon_fnc_v3",
                    "percentile": 0.007293354943273906,
                    "value": -0.0293881553530175
                },
                {
                    "displayName": "canon_mmc",
                    "percentile": 0.5198399085191538,
                    "value": 4.036320203754083e-4
                },
                {
                    "displayName": "canon_mmc60",
                    "percentile": 0.9038056278666171,
                    "value": 0.011093645432638721
                },
                {
                    "displayName": "canon_tc",
                    "percentile": 0.47245889,
                    "value": 0.02297871
                },
                {
                    "displayName": "corj60",
                    "percentile": 0.4875458338601593,
                    "value": 0.0039379500804706015
                },
                {
                    "displayName": "corr60",
                    "percentile": 0.5082434610140076,
                    "value": 0.008948329468700111
                },
                {
                    "displayName": "corr_w_meta_model",
                    "percentile": 0.009358752166377816,
                    "value": -0.06621410503057146
                },
                {
                    "displayName": "cort20",
                    "percentile": 0.7051311817970746,
                    "value": 0.002894905650398329
                },
                {
                    "displayName": "fnc_v3",
                    "percentile": 0.40674671240708976,
                    "value": -0.010055808563244315
                },
                {
                    "displayName": "mcwnm",
                    "percentile": 0.15412353146446434,
                    "value": 0.44760009619185015
                },
                {
                    "displayName": "mmc",
                    "percentile": 0.18189339321593193,
                    "value": -0.006529259667715148
                },
                {
                    "displayName": "mmc60",
                    "percentile": 0.9828119203660195,
                    "value": 0.01808411030279995
                },
                {
                    "displayName": "season_score",
                    "percentile": 0.4586370473215319,
                    "value": -0.0058576208177968155
                },
                {
                    "displayName": "tc",
                    "percentile": 0.47245889,
                    "value": 0.02297871
                },
                {
                    "displayName": "v2_corr20",
                    "percentile": 0.8195410292072323,
                    "value": -0.005985406281769445
                }
            ],
            "latestUserScores": [
                {
                    "displayName": "apcwnm",
                    "rank": 10230,
                    "reputation": -0.04190112752783623
                },
                {
                    "displayName": "bmc",
                    "rank": 157,
                    "reputation": 0.010225136451947066
                },
                {
                    "displayName": "canon_bmc",
                    "rank": 153,
                    "reputation": 0.010255893772717139
                },
                {
                    "displayName": "canon_corj60",
                    "rank": 3339,
                    "reputation": 0.016885045748267415
                },
                {
                    "displayName": "canon_corr",
                    "rank": 4274,
                    "reputation": 0.009879032819174637
                },
                {
                    "displayName": "canon_corr60",
                    "rank": 5869,
                    "reputation": 0.008095113222276122
                },
                {
                    "displayName": "canon_cort20",
                    "rank": 4481,
                    "reputation": 0.007867595529283488
                },
                {
                    "displayName": "canon_fnc_v3",
                    "rank": 4804,
                    "reputation": 0.008265662445192942
                },
                {
                    "displayName": "canon_mmc",
                    "rank": 1,
                    "reputation": 0.009091994592438375
                },
                {
                    "displayName": "canon_mmc60",
                    "rank": 179,
                    "reputation": 0.008103201393141642
                },
                {
                    "displayName": "corj60",
                    "rank": 4738,
                    "reputation": 0.010403256403719648
                },
                {
                    "displayName": "corr60",
                    "rank": 5138,
                    "reputation": 0.010817390344728485
                },
                {
                    "displayName": "corr_w_meta_model",
                    "rank": 10210,
                    "reputation": -0.06555234046853978
                },
                {
                    "displayName": "cort20",
                    "rank": 4232,
                    "reputation": 0.00814224493839445
                },
                {
                    "displayName": "fnc_v3",
                    "rank": 5457,
                    "reputation": 0.006406301339572889
                },
                {
                    "displayName": "mcwnm",
                    "rank": 6136,
                    "reputation": 0.3865522685651708
                },
                {
                    "displayName": "mmc",
                    "rank": 2,
                    "reputation": 0.00895760316358292
                },
                {
                    "displayName": "mmc60",
                    "rank": 37,
                    "reputation": 0.011409527604117408
                },
                {
                    "displayName": "season_score",
                    "rank": 85,
                    "reputation": 0.023123505598495672
                },
                {
                    "displayName": "v2_corr20",
                    "rank": 4449,
                    "reputation": 0.009223072227773797
                }
            ],
            "linkText": null,
            "linkUrl": null,
            "profileUrl": null,
            "stakeInfo": {
                "corrMultiplier": 0.5,
                "mmcMultiplier": 2.0,
                "tcMultiplier": null
            },
            "stakeValue": null,
            "startDate": "2023-12-13T07:00:21Z",
            "team": false,
            "username": "mdel0017"
        }
    }
}


### Get User models 
this query will get all the user's models:

Request Payload:

{"query":"\n    query getAccount_20231012 {\n      account {\n        email\n        username\n        mfaEnabled\n        insertedAt\n        isBeta\n        walletAddress\n        availableNmr\n        availableStakeCredit\n        heldForPendingWithdrawals\n        heldForScheduledStakeIncreases\n        discordLinkToken\n        profileUrl\n        defaultCurrency\n        defaultCurrencySymbol\n        emailPreferences {\n          compute\n          deposit\n          diagnostics\n          modelUploadReceipt\n          pickleRoundOpen\n          pickleRoundStatus\n          roundOpen\n          roundSummary\n          signalsRoundOpen\n          signalsRoundSummary\n          signalsSubmission\n          cryptoRoundOpen\n          cryptoRoundSummary\n          cryptoSubmission\n          stakeChange\n          submission\n          submissionSuccess\n          submissionsStatus\n          withdrawal\n        }\n        models {\n          id\n          name\n          description\n          profileUrl\n          earliestReleaseDate\n          computePickleUpload {\n            id\n          }\n          returns{\n            oneDay\n            threeMonths\n            oneYear\n            allTime\n          }\n          currentPayoutSelection {\n            corrMultiplier\n            mmcMultiplier\n            takeProfit\n            updatedAt\n          }\n          tournament\n          submissionWebhook\n          computeEnabled\n          isComputeWeekdayEnabled\n          latestSubmissions(latestNRounds: 60) {\n            id\n            roundNumber\n            roundOpen\n            roundCloseStaking\n            status\n            filename\n            timestamp\n          }\n          v2Stake {\n            latestValue\n            latestValueSettled\n            stakeValue\n            status\n            pendingV2ChangeStakeRequest {\n              requestedAmount\n              status\n              type\n              dueDate\n              drain\n            }\n          }\n          latestUserScores {\n            displayName\n            reputation\n          }\n        }\n        apiTokens {\n          name\n          publicId\n          scopes\n        }\n        reports {\n          id\n          name\n          key\n          insertedAt\n        }\n      }\n    }\n  "}

Response
{
    "data": {
        "account": {
            "apiTokens": [
                {
                    "name": "ModelCompare",
                    "publicId": "2KTQCZEN777PIN6JKI2IJAB6BSZWBYVF",
                    "scopes": [
                        "read_submission_info",
                        "read_user_info"
                    ]
                },
                {
                    "name": "email@ling-li.com",
                    "publicId": "BS4HD6BKGR23NAG3P5Q4GPVCRTAUA3NJ",
                    "scopes": [
                        "upload_submission"
                    ]
                },
                {
                    "name": "crypto",
                    "publicId": "LKVQMHXLTD3M7JE352OA7ESVSA6WDJJG",
                    "scopes": [
                        "upload_submission"
                    ]
                },
                {
                    "name": "email@ling-li.com",
                    "publicId": "NARALHL4HHGQVDN6GTYYQZLXCM3WC4QU",
                    "scopes": [
                        "upload_submission",
                        "download_submission",
                        "read_submission_info"
                    ]
                },
                {
                    "name": "Model Viewer",
                    "publicId": "RCQFDE2W75533T3CHCDGGQU3UYLGH3QU",
                    "scopes": [
                        "read_submission_info",
                        "read_user_info"
                    ]
                }
            ],
            "availableNmr": "5.746875150000000000",
            "availableStakeCredit": "0.000000000000000000",
            "defaultCurrency": "USD",
            "defaultCurrencySymbol": "$",
            "discordLinkToken": "9hJqz8gkwTg3KmgYAIyC",
            "email": "email@ling-li.com",
            "emailPreferences": {
                "compute": true,
                "cryptoRoundOpen": true,
                "cryptoRoundSummary": true,
                "cryptoSubmission": true,
                "deposit": true,
                "diagnostics": true,
                "modelUploadReceipt": true,
                "pickleRoundOpen": true,
                "pickleRoundStatus": true,
                "roundOpen": true,
                "roundSummary": true,
                "signalsRoundOpen": true,
                "signalsRoundSummary": true,
                "signalsSubmission": true,
                "stakeChange": true,
                "submission": true,
                "submissionSuccess": true,
                "submissionsStatus": true,
                "withdrawal": true
            },
            "heldForPendingWithdrawals": "0.0",
            "heldForScheduledStakeIncreases": "0",
            "insertedAt": "2025-05-28T12:36:40Z",
            "isBeta": true,
            "mfaEnabled": true,
            "models": [
                {
                    "computeEnabled": false,
                    "computePickleUpload": {
                        "id": "e3f5d03d-2cf4-4e63-8306-6cfc0c08b3ec"
                    },
                    "currentPayoutSelection": {
                        "corrMultiplier": 0.5,
                        "mmcMultiplier": 2.0,
                        "takeProfit": false,
                        "updatedAt": null
                    },
                    "description": null,
                    "earliestReleaseDate": "2025-09-24T00:00:00Z",
                    "id": "70395d0d-0c25-4188-a82b-010cb750271b",
                    "isComputeWeekdayEnabled": true,
                    "latestSubmissions": [
                        {
                            "filename": "predictions-TqMFjDcNB8CX.csv",
                            "id": "99d00950-e9d1-4454-8937-c4a50adbf9a8",
                            "roundCloseStaking": "2025-09-23",
                            "roundNumber": 1100,
                            "roundOpen": "2025-09-23",
                            "status": "on-time",
                            "timestamp": "2025-09-23T13:35:36Z"
                        },
                        {
                            "filename": "predictions-3FaJEfFUHMg0.csv",
                            "id": "90f8d3be-f7fd-48a7-8228-30b4b5f8fc0f",
                            "roundCloseStaking": "2025-09-22",
                            "roundNumber": 1099,
                            "roundOpen": "2025-09-20",
                            "status": "on-time",
                            "timestamp": "2025-09-20T13:28:01Z"
                        },
                        {
                            "filename": "predictions-W6cZztMDTtV3.csv",
                            "id": "c7c3aed7-b77a-46a5-a054-fbb98645108a",
                            "roundCloseStaking": "2025-09-19",
                            "roundNumber": 1098,
                            "roundOpen": "2025-09-19",
                            "status": "on-time",
                            "timestamp": "2025-09-19T13:23:53Z"
                        },
                        {
                            "filename": "predictions-DUnIJTshd4Tb.csv",
                            "id": "32db3c94-b2a8-4410-bcf9-b9be039b763d",
                            "roundCloseStaking": "2025-09-18",
                            "roundNumber": 1097,
                            "roundOpen": "2025-09-18",
                            "status": "on-time",
                            "timestamp": "2025-09-18T13:22:20Z"
                        },
                        {
                            "filename": "predictions-2FPLnhHRxgJ7.csv",
                            "id": "ae33edff-1118-4112-80bf-c131b5eea870",
                            "roundCloseStaking": "2025-09-17",
                            "roundNumber": 1096,
                            "roundOpen": "2025-09-17",
                            "status": "on-time",
                            "timestamp": "2025-09-17T13:25:38Z"
                        },
                        {
                            "filename": "predictions-8sicuJRgJdHk.csv",
                            "id": "36f0adf9-9718-4425-ba9d-9920b8b00bf9",
                            "roundCloseStaking": "2025-09-16",
                            "roundNumber": 1095,
                            "roundOpen": "2025-09-16",
                            "status": "on-time",
                            "timestamp": "2025-09-16T13:31:16Z"
                        },
                        {
                            "filename": "predictions-tsPDe6AlgogQ.csv",
                            "id": "670a5394-99b1-4a79-ab6c-3fec543b1751",
                            "roundCloseStaking": "2025-09-15",
                            "roundNumber": 1094,
                            "roundOpen": "2025-09-13",
                            "status": "on-time",
                            "timestamp": "2025-09-13T13:28:52Z"
                        },
                        {
                            "filename": "predictions-XZM9rJ8OWirS.csv",
                            "id": "b2e5c64b-6a97-4b24-b1e1-7d0f89914952",
                            "roundCloseStaking": "2025-09-12",
                            "roundNumber": 1093,
                            "roundOpen": "2025-09-12",
                            "status": "on-time",
                            "timestamp": "2025-09-12T13:24:34Z"
                        },
                        {
                            "filename": "predictions-4N9pF1W0KYN6.csv",
                            "id": "de8a8574-b4fe-47e2-9ed3-6d0722f07693",
                            "roundCloseStaking": "2025-09-11",
                            "roundNumber": 1092,
                            "roundOpen": "2025-09-11",
                            "status": "on-time",
                            "timestamp": "2025-09-11T13:32:12Z"
                        },
                        {
                            "filename": "predictions-MG2u4YBhm0j2.csv",
                            "id": "19a4c537-d8d7-44f8-8aef-d52bbd45c6dc",
                            "roundCloseStaking": "2025-09-10",
                            "roundNumber": 1091,
                            "roundOpen": "2025-09-10",
                            "status": "on-time",
                            "timestamp": "2025-09-10T13:33:40Z"
                        },
                        {
                            "filename": "predictions-99z4EMdMOJqS.csv",
                            "id": "0514ef66-fe1b-4bce-9d91-b240aac71954",
                            "roundCloseStaking": "2025-09-09",
                            "roundNumber": 1090,
                            "roundOpen": "2025-09-09",
                            "status": "on-time",
                            "timestamp": "2025-09-09T13:27:54Z"
                        },
                        {
                            "filename": "predictions-2ZlOLP1SiPws.csv",
                            "id": "398dad89-b7c6-4e0a-8c57-abd375bd8f68",
                            "roundCloseStaking": "2025-09-08",
                            "roundNumber": 1089,
                            "roundOpen": "2025-09-06",
                            "status": "on-time",
                            "timestamp": "2025-09-06T13:19:31Z"
                        },
                        {
                            "filename": "predictions-zxynzqoCpfo5.csv",
                            "id": "b39de3ea-311d-42a8-81ce-6e7ba380cfa4",
                            "roundCloseStaking": "2025-09-05",
                            "roundNumber": 1088,
                            "roundOpen": "2025-09-05",
                            "status": "on-time",
                            "timestamp": "2025-09-05T13:32:11Z"
                        },
                        {
                            "filename": "predictions-JezRnTpRIcnT.csv",
                            "id": "fcbbd2de-5c93-48d5-b246-dcfeb63215e8",
                            "roundCloseStaking": "2025-09-04",
                            "roundNumber": 1087,
                            "roundOpen": "2025-09-04",
                            "status": "on-time",
                            "timestamp": "2025-09-04T13:28:07Z"
                        },
                        {
                            "filename": "predictions-tNDO1dsDC2g5.csv",
                            "id": "daa06a87-58e0-46fa-a9a9-845fb45de459",
                            "roundCloseStaking": "2025-09-03",
                            "roundNumber": 1086,
                            "roundOpen": "2025-09-03",
                            "status": "on-time",
                            "timestamp": "2025-09-03T13:27:41Z"
                        },
                        {
                            "filename": "predictions-VAK0uwFEn8o3.csv",
                            "id": "817314ee-9747-4e36-b6b8-eb40b9d97693",
                            "roundCloseStaking": "2025-09-02",
                            "roundNumber": 1085,
                            "roundOpen": "2025-09-02",
                            "status": "on-time",
                            "timestamp": "2025-09-02T13:36:12Z"
                        },
                        {
                            "filename": "predictions-3p7RcKGrFTyI.csv",
                            "id": "04f987e4-9a5f-4b34-a548-3d0303be9bb9",
                            "roundCloseStaking": "2025-09-01",
                            "roundNumber": 1084,
                            "roundOpen": "2025-08-30",
                            "status": "on-time",
                            "timestamp": "2025-08-30T13:33:16Z"
                        },
                        {
                            "filename": "predictions-M2MvDIecEEYc.csv",
                            "id": "16c45abb-8a9e-4f43-bc1f-0f36471526b4",
                            "roundCloseStaking": "2025-08-29",
                            "roundNumber": 1083,
                            "roundOpen": "2025-08-29",
                            "status": "on-time",
                            "timestamp": "2025-08-29T13:28:31Z"
                        },
                        {
                            "filename": "predictions-2GDLUjySpCZ4.csv",
                            "id": "8ac6aad5-e2c6-4c0e-b9f6-c6574885710a",
                            "roundCloseStaking": "2025-08-28",
                            "roundNumber": 1082,
                            "roundOpen": "2025-08-28",
                            "status": "on-time",
                            "timestamp": "2025-08-28T13:25:12Z"
                        },
                        {
                            "filename": "predictions-dkTtm3KTxsPa.csv",
                            "id": "b0580ffb-a64a-4f2d-8c1b-a254d95d7e65",
                            "roundCloseStaking": "2025-08-27",
                            "roundNumber": 1081,
                            "roundOpen": "2025-08-27",
                            "status": "on-time",
                            "timestamp": "2025-08-27T13:33:07Z"
                        },
                        {
                            "filename": "predictions-oS8Fp9iBkLrz.csv",
                            "id": "80b9d5da-1664-47a3-9681-181c1ec4f975",
                            "roundCloseStaking": "2025-08-26",
                            "roundNumber": 1080,
                            "roundOpen": "2025-08-26",
                            "status": "on-time",
                            "timestamp": "2025-08-26T13:25:45Z"
                        },
                        {
                            "filename": "predictions-0BRHoFtkj3fo.csv",
                            "id": "bb08c6c3-e356-4b75-aaad-063b9dc38cd5",
                            "roundCloseStaking": "2025-08-25",
                            "roundNumber": 1079,
                            "roundOpen": "2025-08-23",
                            "status": "on-time",
                            "timestamp": "2025-08-23T13:32:03Z"
                        },
                        {
                            "filename": "predictions-JeWDzgAag0LE.csv",
                            "id": "c02b2a6e-d05a-48ea-b82e-c708a2c5ecf5",
                            "roundCloseStaking": "2025-08-22",
                            "roundNumber": 1078,
                            "roundOpen": "2025-08-22",
                            "status": "on-time",
                            "timestamp": "2025-08-22T13:21:38Z"
                        },
                        {
                            "filename": "predictions-8uvACFBFMnfw.csv",
                            "id": "52a655ac-0de2-44e5-afd9-c63e95c08143",
                            "roundCloseStaking": "2025-08-21",
                            "roundNumber": 1077,
                            "roundOpen": "2025-08-21",
                            "status": "on-time",
                            "timestamp": "2025-08-21T13:30:36Z"
                        },
                        {
                            "filename": "predictions-hSoWckCD6hbZ.csv",
                            "id": "26c6d1ac-dbc0-4a02-9d2f-f520387bba5e",
                            "roundCloseStaking": "2025-08-20",
                            "roundNumber": 1076,
                            "roundOpen": "2025-08-20",
                            "status": "on-time",
                            "timestamp": "2025-08-20T13:31:45Z"
                        },
                        {
                            "filename": "predictions-zBIKBRA9akS7.csv",
                            "id": "27293204-5724-4c78-9a59-4c99a74e9536",
                            "roundCloseStaking": "2025-08-19",
                            "roundNumber": 1075,
                            "roundOpen": "2025-08-19",
                            "status": "on-time",
                            "timestamp": "2025-08-19T13:31:08Z"
                        },
                        {
                            "filename": "predictions-rFugwnYg1Tx6.csv",
                            "id": "95ef5d6c-02ae-4f97-86c6-6e4b20a23fc9",
                            "roundCloseStaking": "2025-08-18",
                            "roundNumber": 1074,
                            "roundOpen": "2025-08-16",
                            "status": "on-time",
                            "timestamp": "2025-08-16T13:28:23Z"
                        },
                        {
                            "filename": "predictions-bSYb8Y1AD6xD.csv",
                            "id": "d30a5098-08bd-4b70-87f3-dd349250cd63",
                            "roundCloseStaking": "2025-08-15",
                            "roundNumber": 1073,
                            "roundOpen": "2025-08-15",
                            "status": "on-time",
                            "timestamp": "2025-08-15T13:25:40Z"
                        },
                        {
                            "filename": "predictions-P4FeZXye9TZa.csv",
                            "id": "ded945be-8c54-4e51-9b55-4ac6d8e6880c",
                            "roundCloseStaking": "2025-08-14",
                            "roundNumber": 1072,
                            "roundOpen": "2025-08-14",
                            "status": "on-time",
                            "timestamp": "2025-08-14T13:27:40Z"
                        },
                        {
                            "filename": "predictions-rGN2gtGdEMNh.csv",
                            "id": "d45c2344-c66f-4e7e-bfeb-6458c417eeb1",
                            "roundCloseStaking": "2025-08-13",
                            "roundNumber": 1071,
                            "roundOpen": "2025-08-13",
                            "status": "on-time",
                            "timestamp": "2025-08-13T13:25:59Z"
                        },
                        {
                            "filename": "predictions-iwC426IK2hrD.csv",
                            "id": "9cd5e8f5-5cf4-41f6-bf31-1ecbab8fdfcf",
                            "roundCloseStaking": "2025-08-12",
                            "roundNumber": 1070,
                            "roundOpen": "2025-08-12",
                            "status": "on-time",
                            "timestamp": "2025-08-12T13:24:37Z"
                        },
                        {
                            "filename": "predictions-lWS0vGEqCdq1.csv",
                            "id": "864aef3c-badb-4e46-9d44-7ec5df469f38",
                            "roundCloseStaking": "2025-08-11",
                            "roundNumber": 1069,
                            "roundOpen": "2025-08-09",
                            "status": "on-time",
                            "timestamp": "2025-08-09T13:20:39Z"
                        },
                        {
                            "filename": "predictions-BrkvxgYn6ARF.csv",
                            "id": "ac65bdb2-140e-403f-ac21-8e5b01066a7d",
                            "roundCloseStaking": "2025-08-08",
                            "roundNumber": 1068,
                            "roundOpen": "2025-08-08",
                            "status": "on-time",
                            "timestamp": "2025-08-08T13:24:15Z"
                        },
                        {
                            "filename": "predictions-cxPjXNV6hMIQ.csv",
                            "id": "ddbaa39f-0e3b-49e8-93f2-e57ecaf6e571",
                            "roundCloseStaking": "2025-08-07",
                            "roundNumber": 1067,
                            "roundOpen": "2025-08-07",
                            "status": "on-time",
                            "timestamp": "2025-08-07T13:31:52Z"
                        },
                        {
                            "filename": "predictions-E5X3O2kTW1E7.csv",
                            "id": "8ddcd9fc-7256-4d82-8f07-a49f315e5a34",
                            "roundCloseStaking": "2025-08-06",
                            "roundNumber": 1066,
                            "roundOpen": "2025-08-06",
                            "status": "on-time",
                            "timestamp": "2025-08-06T13:29:17Z"
                        },
                        {
                            "filename": "predictions-uMO9clXbV1gk.csv",
                            "id": "49f93c91-fee4-4714-8502-b0f7717c31ed",
                            "roundCloseStaking": "2025-08-05",
                            "roundNumber": 1065,
                            "roundOpen": "2025-08-05",
                            "status": "on-time",
                            "timestamp": "2025-08-05T13:37:27Z"
                        },
                        {
                            "filename": "predictions-3HYoDNvoX8dl.csv",
                            "id": "1f6a94c2-c69d-4ef6-a025-0827ce178c42",
                            "roundCloseStaking": "2025-08-04",
                            "roundNumber": 1064,
                            "roundOpen": "2025-08-02",
                            "status": "on-time",
                            "timestamp": "2025-08-02T13:34:17Z"
                        },
                        {
                            "filename": "predictions-7HYFM3UArYCS.csv",
                            "id": "8c7e17ea-48e5-48c1-9156-a88515c2e54b",
                            "roundCloseStaking": "2025-08-01",
                            "roundNumber": 1063,
                            "roundOpen": "2025-08-01",
                            "status": "on-time",
                            "timestamp": "2025-08-01T13:22:01Z"
                        },
                        {
                            "filename": "predictions-78tAkFYB0c4Z.csv",
                            "id": "f129fae8-837a-465c-8345-c42ed630bcd6",
                            "roundCloseStaking": "2025-07-31",
                            "roundNumber": 1062,
                            "roundOpen": "2025-07-31",
                            "status": "on-time",
                            "timestamp": "2025-07-31T13:20:21Z"
                        },
                        {
                            "filename": "predictions-2FiyqNI6JyqH.csv",
                            "id": "467dc149-047c-4422-806c-565ad88ccbdd",
                            "roundCloseStaking": "2025-07-30",
                            "roundNumber": 1061,
                            "roundOpen": "2025-07-30",
                            "status": "on-time",
                            "timestamp": "2025-07-30T13:26:08Z"
                        },
                        {
                            "filename": "predictions-MLYBj96p4CpP.csv",
                            "id": "9b110532-606e-4727-a44b-eb61b521c7af",
                            "roundCloseStaking": "2025-07-29",
                            "roundNumber": 1060,
                            "roundOpen": "2025-07-29",
                            "status": "on-time",
                            "timestamp": "2025-07-29T13:25:20Z"
                        },
                        {
                            "filename": "predictions-xjFtnvbVjd9Q.csv",
                            "id": "18d9be14-341d-4293-9f53-0f2747f1b4eb",
                            "roundCloseStaking": "2025-07-28",
                            "roundNumber": 1059,
                            "roundOpen": "2025-07-26",
                            "status": "on-time",
                            "timestamp": "2025-07-26T13:22:34Z"
                        },
                        {
                            "filename": "predictions-sGStr5rMfilT.csv",
                            "id": "04432f30-a93a-4649-aea9-75be968beba9",
                            "roundCloseStaking": "2025-07-25",
                            "roundNumber": 1058,
                            "roundOpen": "2025-07-25",
                            "status": "on-time",
                            "timestamp": "2025-07-25T13:17:46Z"
                        },
                        {
                            "filename": "predictions-Ef5zKNXfnR7U.csv",
                            "id": "d2174bdd-b0d8-4e73-adaf-e0b226068831",
                            "roundCloseStaking": "2025-07-24",
                            "roundNumber": 1057,
                            "roundOpen": "2025-07-24",
                            "status": "on-time",
                            "timestamp": "2025-07-24T13:23:50Z"
                        },
                        {
                            "filename": "predictions-37huWYm8TeXY.csv",
                            "id": "e86a4d3b-e1bd-4c3b-bc1c-e44beb6947eb",
                            "roundCloseStaking": "2025-07-23",
                            "roundNumber": 1056,
                            "roundOpen": "2025-07-23",
                            "status": "on-time",
                            "timestamp": "2025-07-23T13:25:29Z"
                        },
                        {
                            "filename": "predictions-ZpJKiTzL4Qvf.csv",
                            "id": "341d0492-eba7-434b-9bd5-a4dbe0cf3b14",
                            "roundCloseStaking": "2025-07-22",
                            "roundNumber": 1055,
                            "roundOpen": "2025-07-22",
                            "status": "on-time",
                            "timestamp": "2025-07-22T13:26:44Z"
                        },
                        {
                            "filename": "predictions-Fq33m1m7LhWr.csv",
                            "id": "36443d0b-e304-48f9-bb0e-0e15c4785e91",
                            "roundCloseStaking": "2025-07-21",
                            "roundNumber": 1054,
                            "roundOpen": "2025-07-19",
                            "status": "on-time",
                            "timestamp": "2025-07-19T13:25:26Z"
                        },
                        {
                            "filename": "predictions-xzlEs1bnxfLy.csv",
                            "id": "78bcde19-03ca-4be4-a4f7-207f0a6f384b",
                            "roundCloseStaking": "2025-07-18",
                            "roundNumber": 1053,
                            "roundOpen": "2025-07-18",
                            "status": "on-time",
                            "timestamp": "2025-07-18T13:26:09Z"
                        },
                        {
                            "filename": "predictions-tRcgTHgPTCP2.csv",
                            "id": "4df81912-bf09-42c4-b76a-49da50dfed0b",
                            "roundCloseStaking": "2025-07-17",
                            "roundNumber": 1052,
                            "roundOpen": "2025-07-17",
                            "status": "on-time",
                            "timestamp": "2025-07-17T13:32:55Z"
                        },
                        {
                            "filename": "predictions-xWYonL9PYwCf.csv",
                            "id": "172e6ed3-fd74-4d44-a798-b6c35b65d303",
                            "roundCloseStaking": "2025-07-16",
                            "roundNumber": 1051,
                            "roundOpen": "2025-07-16",
                            "status": "on-time",
                            "timestamp": "2025-07-16T13:28:35Z"
                        },
                        {
                            "filename": "predictions-C3SGQEpPQW6q.csv",
                            "id": "b4f2a599-4b5d-4c4b-b881-45243f2312cb",
                            "roundCloseStaking": "2025-07-15",
                            "roundNumber": 1050,
                            "roundOpen": "2025-07-15",
                            "status": "on-time",
                            "timestamp": "2025-07-15T13:23:08Z"
                        },
                        {
                            "filename": "predictions-kFVRkrx9UFRf.csv",
                            "id": "ec04c4d2-87ae-4639-ac89-33277720e6c0",
                            "roundCloseStaking": "2025-07-14",
                            "roundNumber": 1049,
                            "roundOpen": "2025-07-12",
                            "status": "on-time",
                            "timestamp": "2025-07-12T13:32:12Z"
                        },
                        {
                            "filename": "predictions-Hh3pGZdfWRYk.csv",
                            "id": "4ed29beb-9d2e-4c40-a527-4c4b46c75721",
                            "roundCloseStaking": "2025-07-11",
                            "roundNumber": 1048,
                            "roundOpen": "2025-07-11",
                            "status": "on-time",
                            "timestamp": "2025-07-11T13:24:13Z"
                        },
                        {
                            "filename": "predictions-F90q1AoPBMzl.csv",
                            "id": "d29aa3b1-4196-462b-8175-5c5d671642da",
                            "roundCloseStaking": "2025-07-10",
                            "roundNumber": 1047,
                            "roundOpen": "2025-07-10",
                            "status": "on-time",
                            "timestamp": "2025-07-10T13:24:53Z"
                        },
                        {
                            "filename": "predictions-yRjNtmBAIxK0.csv",
                            "id": "5b7f3cf9-c2d2-4b22-be61-fc5ee41de7c1",
                            "roundCloseStaking": "2025-07-09",
                            "roundNumber": 1046,
                            "roundOpen": "2025-07-09",
                            "status": "on-time",
                            "timestamp": "2025-07-09T13:25:26Z"
                        },
                        {
                            "filename": "predictions-O4cOZfUb8OYg.csv",
                            "id": "8cbf7f9c-855f-4930-bb05-dd0e7f3e5e51",
                            "roundCloseStaking": "2025-07-08",
                            "roundNumber": 1045,
                            "roundOpen": "2025-07-08",
                            "status": "on-time",
                            "timestamp": "2025-07-08T14:08:36Z"
                        },
                        {
                            "filename": "predictions-5GyXLO9c4Hgj.csv",
                            "id": "1b1dcff7-6ebf-4768-bce2-48656688d143",
                            "roundCloseStaking": "2025-07-07",
                            "roundNumber": 1044,
                            "roundOpen": "2025-07-05",
                            "status": "on-time",
                            "timestamp": "2025-07-05T14:15:20Z"
                        },
                        {
                            "filename": "predictions-tREbZ9mnc2EW.csv",
                            "id": "6f09630d-1883-4e7b-985c-d54586ef2f3a",
                            "roundCloseStaking": "2025-07-04",
                            "roundNumber": 1043,
                            "roundOpen": "2025-07-04",
                            "status": "on-time",
                            "timestamp": "2025-07-04T13:35:27Z"
                        },
                        {
                            "filename": "predictions-rx8TlufBwi0b.csv",
                            "id": "ac76cf48-5a78-4d03-96b9-0ca7f98d8510",
                            "roundCloseStaking": "2025-07-03",
                            "roundNumber": 1042,
                            "roundOpen": "2025-07-03",
                            "status": "on-time",
                            "timestamp": "2025-07-03T13:52:46Z"
                        },
                        {
                            "filename": "predictions-sZdsB4Lu9xlc.csv",
                            "id": "63d56dd0-c798-4456-9bec-f543fd486dd0",
                            "roundCloseStaking": "2025-07-02",
                            "roundNumber": 1041,
                            "roundOpen": "2025-07-02",
                            "status": "on-time",
                            "timestamp": "2025-07-02T13:48:05Z"
                        },
                        {
                            "filename": "predictions-pKD61pkOx7Hq.csv",
                            "id": "1f98dd84-ef99-4b29-89ec-1ebac1b48be0",
                            "roundCloseStaking": "2025-07-01",
                            "roundNumber": 1040,
                            "roundOpen": "2025-07-01",
                            "status": "on-time",
                            "timestamp": "2025-07-01T14:00:26Z"
                        }
                    ],
                    "latestUserScores": [
                        {
                            "displayName": "apcwnm",
                            "reputation": 0.06846830632339053
                        },
                        {
                            "displayName": "bmc",
                            "reputation": -0.0019322876208172166
                        },
                        {
                            "displayName": "canon_bmc",
                            "reputation": -0.001806429806434486
                        },
                        {
                            "displayName": "canon_corj60",
                            "reputation": -0.0013758054230892662
                        },
                        {
                            "displayName": "canon_corr",
                            "reputation": -9.02768071575543e-4
                        },
                        {
                            "displayName": "canon_corr60",
                            "reputation": -0.001005726233131054
                        },
                        {
                            "displayName": "canon_cort20",
                            "reputation": 5.111746895533716e-4
                        },
                        {
                            "displayName": "canon_fnc_v3",
                            "reputation": -9.192928965367211e-5
                        },
                        {
                            "displayName": "canon_mmc",
                            "reputation": -0.0021469712905061345
                        },
                        {
                            "displayName": "canon_mmc60",
                            "reputation": -0.001492096893318995
                        },
                        {
                            "displayName": "corj60",
                            "reputation": -0.0013386214927355023
                        },
                        {
                            "displayName": "corr60",
                            "reputation": -0.0012742453730446848
                        },
                        {
                            "displayName": "corr_w_meta_model",
                            "reputation": 0.37707390928959345
                        },
                        {
                            "displayName": "cort20",
                            "reputation": 5.445575264221633e-4
                        },
                        {
                            "displayName": "fnc_v3",
                            "reputation": -9.793283510044253e-5
                        },
                        {
                            "displayName": "mcwnm",
                            "reputation": 0.24759796931065603
                        },
                        {
                            "displayName": "mmc",
                            "reputation": -0.002287181660498372
                        },
                        {
                            "displayName": "mmc60",
                            "reputation": -0.0018996940934451595
                        },
                        {
                            "displayName": "season_score",
                            "reputation": -0.004745326674271305
                        },
                        {
                            "displayName": "v2_corr20",
                            "reputation": -9.617243538008846e-4
                        }
                    ],
                    "name": "fnc_nai",
                    "profileUrl": "https://numerai-public-images.s3-us-west-2.amazonaws.com/profile_images/fish_n_chips-2XyFtQZIzBeu.jpg",
                    "returns": null,
                    "submissionWebhook": null,
                    "tournament": 8,
                    "v2Stake": {
                        "latestValue": "0.000000000000000000",
                        "latestValueSettled": "0.000000000000000000",
                        "pendingV2ChangeStakeRequest": null,
                        "stakeValue": null,
                        "status": null
                    }
                },
                {
                    "computeEnabled": false,
                    "computePickleUpload": {
                        "id": "48543fd7-9333-453d-9e70-b3236e4d2901"
                    },
                    "currentPayoutSelection": {
                        "corrMultiplier": 0.5,
                        "mmcMultiplier": 2.0,
                        "takeProfit": false,
                        "updatedAt": null
                    },
                    "description": null,
                    "earliestReleaseDate": "2025-09-24T00:00:00Z",
                    "id": "0c8aee74-4d69-4cf5-b181-59c3cbbc8ea1",
                    "isComputeWeekdayEnabled": true,
                    "latestSubmissions": [
                        {
                            "filename": "predictions-0HTnrHfJrLtj.csv",
                            "id": "e5edb887-4897-49ba-af07-c0d0ce4e9c76",
                            "roundCloseStaking": "2025-09-23",
                            "roundNumber": 1100,
                            "roundOpen": "2025-09-23",
                            "status": "on-time",
                            "timestamp": "2025-09-23T13:27:48Z"
                        },
                        {
                            "filename": "predictions-kIqtp2QuvDgw.csv",
                            "id": "d56c7f5b-68ac-4044-b954-f2e27f50d732",
                            "roundCloseStaking": "2025-09-22",
                            "roundNumber": 1099,
                            "roundOpen": "2025-09-20",
                            "status": "on-time",
                            "timestamp": "2025-09-20T13:28:23Z"
                        },
                        {
                            "filename": "predictions-y9NincPIZQIt.csv",
                            "id": "8a1c638b-4f7b-42fa-b8fb-9e1fe50ceb13",
                            "roundCloseStaking": "2025-09-19",
                            "roundNumber": 1098,
                            "roundOpen": "2025-09-19",
                            "status": "on-time",
                            "timestamp": "2025-09-19T13:27:13Z"
                        },
                        {
                            "filename": "predictions-kAu1Su1YyaGY.csv",
                            "id": "2ad5f18b-0691-4100-8024-cb13d9b9f436",
                            "roundCloseStaking": "2025-09-18",
                            "roundNumber": 1097,
                            "roundOpen": "2025-09-18",
                            "status": "on-time",
                            "timestamp": "2025-09-18T13:27:14Z"
                        },
                        {
                            "filename": "predictions-b7in5hTIntdf.csv",
                            "id": "86c320b8-859e-4ab2-9a37-66d64876c625",
                            "roundCloseStaking": "2025-09-17",
                            "roundNumber": 1096,
                            "roundOpen": "2025-09-17",
                            "status": "on-time",
                            "timestamp": "2025-09-17T13:32:17Z"
                        },
                        {
                            "filename": "predictions-CUlSpm88gllf.csv",
                            "id": "170feabc-be04-4a6e-b8dc-6adf635dc9b3",
                            "roundCloseStaking": "2025-09-16",
                            "roundNumber": 1095,
                            "roundOpen": "2025-09-16",
                            "status": "on-time",
                            "timestamp": "2025-09-16T13:23:32Z"
                        },
                        {
                            "filename": "predictions-SUJKsWpUO9La.csv",
                            "id": "eed3a787-0b80-4e0b-a46e-337d728efaa6",
                            "roundCloseStaking": "2025-09-15",
                            "roundNumber": 1094,
                            "roundOpen": "2025-09-13",
                            "status": "on-time",
                            "timestamp": "2025-09-13T13:30:12Z"
                        },
                        {
                            "filename": "predictions-AD4cvJCVubEV.csv",
                            "id": "7a64c7e0-10f2-4c7a-9f4f-15cf7f5bc9af",
                            "roundCloseStaking": "2025-09-12",
                            "roundNumber": 1093,
                            "roundOpen": "2025-09-12",
                            "status": "on-time",
                            "timestamp": "2025-09-12T13:28:56Z"
                        },
                        {
                            "filename": "predictions-uiCH9Ka25xK2.csv",
                            "id": "4c8516d8-1855-47ba-aa0b-3ba489b4c1ea",
                            "roundCloseStaking": "2025-09-11",
                            "roundNumber": 1092,
                            "roundOpen": "2025-09-11",
                            "status": "on-time",
                            "timestamp": "2025-09-11T13:25:38Z"
                        },
                        {
                            "filename": "predictions-CmAsd9jbRNiK.csv",
                            "id": "ea57e839-6fc1-4a56-a68f-cce749c1403b",
                            "roundCloseStaking": "2025-09-10",
                            "roundNumber": 1091,
                            "roundOpen": "2025-09-10",
                            "status": "on-time",
                            "timestamp": "2025-09-10T13:27:25Z"
                        },
                        {
                            "filename": "predictions-vS7jqpNSxNVX.csv",
                            "id": "9b9232af-9ee4-4371-9a0e-b2a9e58a9ce7",
                            "roundCloseStaking": "2025-09-09",
                            "roundNumber": 1090,
                            "roundOpen": "2025-09-09",
                            "status": "on-time",
                            "timestamp": "2025-09-09T13:26:47Z"
                        },
                        {
                            "filename": "predictions-AUYjnUhzEr1u.csv",
                            "id": "744b5e98-81fe-49f0-8dec-8c55147200b5",
                            "roundCloseStaking": "2025-09-08",
                            "roundNumber": 1089,
                            "roundOpen": "2025-09-06",
                            "status": "on-time",
                            "timestamp": "2025-09-06T13:22:34Z"
                        },
                        {
                            "filename": "predictions-EyjfC7MgeJ8F.csv",
                            "id": "9e33e8a1-2a9a-459a-948c-21484b2a2b0e",
                            "roundCloseStaking": "2025-09-05",
                            "roundNumber": 1088,
                            "roundOpen": "2025-09-05",
                            "status": "on-time",
                            "timestamp": "2025-09-05T13:26:35Z"
                        },
                        {
                            "filename": "predictions-BXsy2gcF45QH.csv",
                            "id": "7e5d7e7c-5a62-4a71-87e3-40dbe8a5d148",
                            "roundCloseStaking": "2025-09-04",
                            "roundNumber": 1087,
                            "roundOpen": "2025-09-04",
                            "status": "on-time",
                            "timestamp": "2025-09-04T13:25:29Z"
                        },
                        {
                            "filename": "predictions-O4SH1HvecWyv.csv",
                            "id": "4896fcf6-0ff5-4771-aa9e-512248651d63",
                            "roundCloseStaking": "2025-09-03",
                            "roundNumber": 1086,
                            "roundOpen": "2025-09-03",
                            "status": "on-time",
                            "timestamp": "2025-09-03T13:28:07Z"
                        },
                        {
                            "filename": "predictions-TfQimzRgCcez.csv",
                            "id": "e5e5909d-bfac-456a-8dfc-b674e3397d51",
                            "roundCloseStaking": "2025-09-02",
                            "roundNumber": 1085,
                            "roundOpen": "2025-09-02",
                            "status": "on-time",
                            "timestamp": "2025-09-02T13:34:09Z"
                        },
                        {
                            "filename": "predictions-R44OqGkSxm1m.csv",
                            "id": "fffd3278-be58-4ee1-b0ba-8a1f2cae142a",
                            "roundCloseStaking": "2025-09-01",
                            "roundNumber": 1084,
                            "roundOpen": "2025-08-30",
                            "status": "on-time",
                            "timestamp": "2025-08-30T13:22:55Z"
                        },
                        {
                            "filename": "predictions-FXX1C3XrS7GZ.csv",
                            "id": "beead028-005b-4802-9953-8cb0ae802b2a",
                            "roundCloseStaking": "2025-08-29",
                            "roundNumber": 1083,
                            "roundOpen": "2025-08-29",
                            "status": "on-time",
                            "timestamp": "2025-08-29T13:28:47Z"
                        },
                        {
                            "filename": "predictions-c7BGhaKTCkic.csv",
                            "id": "27836b00-4a8e-4c65-8f29-6378acf328dc",
                            "roundCloseStaking": "2025-08-28",
                            "roundNumber": 1082,
                            "roundOpen": "2025-08-28",
                            "status": "on-time",
                            "timestamp": "2025-08-28T13:32:45Z"
                        },
                        {
                            "filename": "predictions-uxhzPheoref5.csv",
                            "id": "bd04e82f-748e-4b85-bf29-edd525737a88",
                            "roundCloseStaking": "2025-08-27",
                            "roundNumber": 1081,
                            "roundOpen": "2025-08-27",
                            "status": "on-time",
                            "timestamp": "2025-08-27T13:23:39Z"
                        },
                        {
                            "filename": "predictions-7mZDKxvYttF1.csv",
                            "id": "207e766d-8ed6-483f-9838-7a473db9ac1b",
                            "roundCloseStaking": "2025-08-26",
                            "roundNumber": 1080,
                            "roundOpen": "2025-08-26",
                            "status": "on-time",
                            "timestamp": "2025-08-26T13:24:26Z"
                        },
                        {
                            "filename": "predictions-fma94ip65hzq.csv",
                            "id": "6f8495db-3c26-48f9-8187-25861917656c",
                            "roundCloseStaking": "2025-08-25",
                            "roundNumber": 1079,
                            "roundOpen": "2025-08-23",
                            "status": "on-time",
                            "timestamp": "2025-08-23T13:24:46Z"
                        },
                        {
                            "filename": "predictions-oenCndAbgD5O.csv",
                            "id": "98365fb8-10da-4173-9a81-048b7843df16",
                            "roundCloseStaking": "2025-08-22",
                            "roundNumber": 1078,
                            "roundOpen": "2025-08-22",
                            "status": "on-time",
                            "timestamp": "2025-08-22T13:24:49Z"
                        },
                        {
                            "filename": "predictions-uZqmCECBiYCr.csv",
                            "id": "8854c457-d359-4ba6-af67-fd0a039aa1f8",
                            "roundCloseStaking": "2025-08-21",
                            "roundNumber": 1077,
                            "roundOpen": "2025-08-21",
                            "status": "on-time",
                            "timestamp": "2025-08-21T13:26:28Z"
                        },
                        {
                            "filename": "predictions-JxhODlrwClTB.csv",
                            "id": "20ed0483-cf61-4b50-af8b-28835e24478e",
                            "roundCloseStaking": "2025-08-20",
                            "roundNumber": 1076,
                            "roundOpen": "2025-08-20",
                            "status": "on-time",
                            "timestamp": "2025-08-20T13:26:17Z"
                        },
                        {
                            "filename": "predictions-wzjbi43TJnAa.csv",
                            "id": "d2237e7b-0a0d-4481-a4db-e2efa5fe350e",
                            "roundCloseStaking": "2025-08-19",
                            "roundNumber": 1075,
                            "roundOpen": "2025-08-19",
                            "status": "on-time",
                            "timestamp": "2025-08-19T13:23:22Z"
                        },
                        {
                            "filename": "predictions-iSY2dK3LdMpP.csv",
                            "id": "407155a1-2aef-44b6-a822-bd26f7527238",
                            "roundCloseStaking": "2025-08-18",
                            "roundNumber": 1074,
                            "roundOpen": "2025-08-16",
                            "status": "on-time",
                            "timestamp": "2025-08-16T13:18:33Z"
                        },
                        {
                            "filename": "predictions-mIz3OYkPvbdU.csv",
                            "id": "c2d889cb-ca61-4e87-b824-61996ecc6223",
                            "roundCloseStaking": "2025-08-15",
                            "roundNumber": 1073,
                            "roundOpen": "2025-08-15",
                            "status": "on-time",
                            "timestamp": "2025-08-15T13:24:00Z"
                        },
                        {
                            "filename": "predictions-LaX0EoalwBtL.csv",
                            "id": "62474c9d-3bdd-4334-a06b-89276eebd3c6",
                            "roundCloseStaking": "2025-08-14",
                            "roundNumber": 1072,
                            "roundOpen": "2025-08-14",
                            "status": "on-time",
                            "timestamp": "2025-08-14T13:30:43Z"
                        },
                        {
                            "filename": "predictions-m7E4dlXZWIcD.csv",
                            "id": "1f657721-05ed-4b8c-8232-76173e6b06fb",
                            "roundCloseStaking": "2025-08-13",
                            "roundNumber": 1071,
                            "roundOpen": "2025-08-13",
                            "status": "on-time",
                            "timestamp": "2025-08-13T13:23:30Z"
                        },
                        {
                            "filename": "predictions-6kp7uHtX0okv.csv",
                            "id": "b07ce7f0-5273-4251-9911-26547104f4de",
                            "roundCloseStaking": "2025-08-12",
                            "roundNumber": 1070,
                            "roundOpen": "2025-08-12",
                            "status": "on-time",
                            "timestamp": "2025-08-12T13:23:16Z"
                        },
                        {
                            "filename": "predictions-KL3Q4cJAEdxa.csv",
                            "id": "0f113c33-4045-4d0e-afae-1a5e24c74b85",
                            "roundCloseStaking": "2025-08-11",
                            "roundNumber": 1069,
                            "roundOpen": "2025-08-09",
                            "status": "on-time",
                            "timestamp": "2025-08-09T13:20:38Z"
                        },
                        {
                            "filename": "predictions-HkSZYJTMVjZc.csv",
                            "id": "cc96774a-c7be-46e4-9d20-25e34db214ff",
                            "roundCloseStaking": "2025-08-08",
                            "roundNumber": 1068,
                            "roundOpen": "2025-08-08",
                            "status": "on-time",
                            "timestamp": "2025-08-08T13:31:52Z"
                        },
                        {
                            "filename": "predictions-InpUQesEBUPv.csv",
                            "id": "cccd7e50-8787-4167-ae9f-d48a4c13412b",
                            "roundCloseStaking": "2025-08-07",
                            "roundNumber": 1067,
                            "roundOpen": "2025-08-07",
                            "status": "on-time",
                            "timestamp": "2025-08-07T13:25:18Z"
                        },
                        {
                            "filename": "predictions-gvQwEm0JKGXS.csv",
                            "id": "995942a1-867d-4584-9966-231fb1143814",
                            "roundCloseStaking": "2025-08-06",
                            "roundNumber": 1066,
                            "roundOpen": "2025-08-06",
                            "status": "on-time",
                            "timestamp": "2025-08-06T13:25:08Z"
                        },
                        {
                            "filename": "predictions-AJCjrZyGw38M.csv",
                            "id": "29582bb0-e36c-4c93-848f-7d5f75187c7e",
                            "roundCloseStaking": "2025-08-05",
                            "roundNumber": 1065,
                            "roundOpen": "2025-08-05",
                            "status": "on-time",
                            "timestamp": "2025-08-05T13:34:20Z"
                        },
                        {
                            "filename": "predictions-R7817x83XZuy.csv",
                            "id": "d3d7d790-9962-4508-8f32-fd1b8601d29e",
                            "roundCloseStaking": "2025-08-04",
                            "roundNumber": 1064,
                            "roundOpen": "2025-08-02",
                            "status": "on-time",
                            "timestamp": "2025-08-02T13:38:29Z"
                        },
                        {
                            "filename": "predictions-mMZalBEFlDV0.csv",
                            "id": "fb08b3b6-c317-4e4e-9399-cd53bc7405cd",
                            "roundCloseStaking": "2025-08-01",
                            "roundNumber": 1063,
                            "roundOpen": "2025-08-01",
                            "status": "on-time",
                            "timestamp": "2025-08-01T13:23:05Z"
                        },
                        {
                            "filename": "predictions-EH9qAM1vzUTQ.csv",
                            "id": "aec35820-9bb3-45b2-b6c8-d6f867abab83",
                            "roundCloseStaking": "2025-07-31",
                            "roundNumber": 1062,
                            "roundOpen": "2025-07-31",
                            "status": "on-time",
                            "timestamp": "2025-07-31T13:19:47Z"
                        },
                        {
                            "filename": "predictions-cZBgtf5BXmCW.csv",
                            "id": "2ef25d8d-4abf-4d6f-80a8-e54be64ca2a4",
                            "roundCloseStaking": "2025-07-30",
                            "roundNumber": 1061,
                            "roundOpen": "2025-07-30",
                            "status": "on-time",
                            "timestamp": "2025-07-30T13:17:27Z"
                        },
                        {
                            "filename": "predictions-xjG5NEPamaZO.csv",
                            "id": "4cff1dfe-f61c-4232-ae28-0ae1ff46b896",
                            "roundCloseStaking": "2025-07-29",
                            "roundNumber": 1060,
                            "roundOpen": "2025-07-29",
                            "status": "on-time",
                            "timestamp": "2025-07-29T13:19:11Z"
                        },
                        {
                            "filename": "predictions-jrSOTWeSNJqj.csv",
                            "id": "49423b43-c46d-4917-82ce-339c2c5f9f45",
                            "roundCloseStaking": "2025-07-28",
                            "roundNumber": 1059,
                            "roundOpen": "2025-07-26",
                            "status": "on-time",
                            "timestamp": "2025-07-26T13:19:30Z"
                        },
                        {
                            "filename": "predictions-udltNS5AwXgI.csv",
                            "id": "27899edc-d93f-4805-b64e-59a29a91dc40",
                            "roundCloseStaking": "2025-07-25",
                            "roundNumber": 1058,
                            "roundOpen": "2025-07-25",
                            "status": "on-time",
                            "timestamp": "2025-07-25T13:18:38Z"
                        },
                        {
                            "filename": "predictions-0n6Wu56yqCSU.csv",
                            "id": "df8724c1-1a0c-4c17-aff2-8eebb24295b4",
                            "roundCloseStaking": "2025-07-24",
                            "roundNumber": 1057,
                            "roundOpen": "2025-07-24",
                            "status": "on-time",
                            "timestamp": "2025-07-24T13:21:46Z"
                        },
                        {
                            "filename": "predictions-dJT6i1G0PcPt.csv",
                            "id": "3da21221-34d1-4b2d-aed9-55015bbe85f3",
                            "roundCloseStaking": "2025-07-23",
                            "roundNumber": 1056,
                            "roundOpen": "2025-07-23",
                            "status": "on-time",
                            "timestamp": "2025-07-23T13:21:51Z"
                        },
                        {
                            "filename": "predictions-aUdWJ7krXrLG.csv",
                            "id": "1b5fd454-c115-46aa-a898-c1318dc66056",
                            "roundCloseStaking": "2025-07-22",
                            "roundNumber": 1055,
                            "roundOpen": "2025-07-22",
                            "status": "on-time",
                            "timestamp": "2025-07-22T13:20:29Z"
                        },
                        {
                            "filename": "predictions-YsYfAx76hMOZ.csv",
                            "id": "24ae55e0-46bd-46b9-9b05-6f6dbb5e5f48",
                            "roundCloseStaking": "2025-07-21",
                            "roundNumber": 1054,
                            "roundOpen": "2025-07-19",
                            "status": "on-time",
                            "timestamp": "2025-07-19T13:18:25Z"
                        },
                        {
                            "filename": "predictions-pCfiSmmYXYRH.csv",
                            "id": "4dc46608-b4c7-46f7-b312-3cebab08b09e",
                            "roundCloseStaking": "2025-07-18",
                            "roundNumber": 1053,
                            "roundOpen": "2025-07-18",
                            "status": "on-time",
                            "timestamp": "2025-07-18T13:22:31Z"
                        },
                        {
                            "filename": "predictions-HaNj9Vp1gO1R.csv",
                            "id": "7c607501-d0d9-4b94-bf35-41bb84693aa6",
                            "roundCloseStaking": "2025-07-17",
                            "roundNumber": 1052,
                            "roundOpen": "2025-07-17",
                            "status": "on-time",
                            "timestamp": "2025-07-17T13:31:17Z"
                        },
                        {
                            "filename": "predictions-SL7vkrWFoCzV.csv",
                            "id": "45e08a03-d372-4b88-9217-8c67e4f954f4",
                            "roundCloseStaking": "2025-07-16",
                            "roundNumber": 1051,
                            "roundOpen": "2025-07-16",
                            "status": "on-time",
                            "timestamp": "2025-07-16T13:22:02Z"
                        },
                        {
                            "filename": "predictions-0PxgnZMlJ0LQ.csv",
                            "id": "7a682ea3-bd33-47e1-bb2d-f9bc6ba22470",
                            "roundCloseStaking": "2025-07-15",
                            "roundNumber": 1050,
                            "roundOpen": "2025-07-15",
                            "status": "on-time",
                            "timestamp": "2025-07-15T13:21:37Z"
                        },
                        {
                            "filename": "predictions-7X95Fol9qJKv.csv",
                            "id": "0762584f-5892-42ec-8922-e71cb1913344",
                            "roundCloseStaking": "2025-07-14",
                            "roundNumber": 1049,
                            "roundOpen": "2025-07-12",
                            "status": "on-time",
                            "timestamp": "2025-07-12T13:28:51Z"
                        },
                        {
                            "filename": "predictions-fVMTGi9FTERM.csv",
                            "id": "6335dc88-7379-4d97-a939-a82283caaefc",
                            "roundCloseStaking": "2025-07-11",
                            "roundNumber": 1048,
                            "roundOpen": "2025-07-11",
                            "status": "on-time",
                            "timestamp": "2025-07-11T13:20:15Z"
                        },
                        {
                            "filename": "predictions-xBrBBmyBpoA4.csv",
                            "id": "fb89484f-e135-404d-afb5-322e08a9fbd5",
                            "roundCloseStaking": "2025-07-10",
                            "roundNumber": 1047,
                            "roundOpen": "2025-07-10",
                            "status": "on-time",
                            "timestamp": "2025-07-10T13:20:27Z"
                        },
                        {
                            "filename": "predictions-a1O80EcrH2Hp.csv",
                            "id": "719ff78c-3166-4087-9a52-c4aba6836abd",
                            "roundCloseStaking": "2025-07-09",
                            "roundNumber": 1046,
                            "roundOpen": "2025-07-09",
                            "status": "on-time",
                            "timestamp": "2025-07-09T13:22:18Z"
                        },
                        {
                            "filename": "predictions-6IarqNmVMCDF.csv",
                            "id": "f7d4bce5-251e-4f43-80a6-a7494f555403",
                            "roundCloseStaking": "2025-07-08",
                            "roundNumber": 1045,
                            "roundOpen": "2025-07-08",
                            "status": "on-time",
                            "timestamp": "2025-07-08T14:08:19Z"
                        },
                        {
                            "filename": "predictions-eeP7jEdwUAQV.csv",
                            "id": "1b42b9e4-e8ce-4e4f-9458-9e354bd17062",
                            "roundCloseStaking": "2025-07-07",
                            "roundNumber": 1044,
                            "roundOpen": "2025-07-05",
                            "status": "on-time",
                            "timestamp": "2025-07-05T14:09:42Z"
                        },
                        {
                            "filename": "predictions-XSaaZ6DBsRvV.csv",
                            "id": "d5226fbd-0aa7-42d6-9957-1b1c7c3388c8",
                            "roundCloseStaking": "2025-07-04",
                            "roundNumber": 1043,
                            "roundOpen": "2025-07-04",
                            "status": "on-time",
                            "timestamp": "2025-07-04T13:32:09Z"
                        },
                        {
                            "filename": "predictions-HE4AC61xOKiK.csv",
                            "id": "dca1da1b-1282-4bbd-8081-5f6a2abd6ff7",
                            "roundCloseStaking": "2025-07-03",
                            "roundNumber": 1042,
                            "roundOpen": "2025-07-03",
                            "status": "on-time",
                            "timestamp": "2025-07-03T13:52:24Z"
                        },
                        {
                            "filename": "predictions-aagI4SLkVDJ6.csv",
                            "id": "1efa7a18-f33e-40a2-98bd-f06794692bbc",
                            "roundCloseStaking": "2025-07-02",
                            "roundNumber": 1041,
                            "roundOpen": "2025-07-02",
                            "status": "on-time",
                            "timestamp": "2025-07-02T13:41:26Z"
                        },
                        {
                            "filename": "predictions-DjgXekOTwyJO.csv",
                            "id": "22c86952-7fb4-45cf-b492-c3a1a6ed0931",
                            "roundCloseStaking": "2025-07-01",
                            "roundNumber": 1040,
                            "roundOpen": "2025-07-01",
                            "status": "on-time",
                            "timestamp": "2025-07-01T13:52:22Z"
                        }
                    ],
                    "latestUserScores": [
                        {
                            "displayName": "apcwnm",
                            "reputation": 0.10271863345921806
                        },
                        {
                            "displayName": "bmc",
                            "reputation": -0.0019505329530032144
                        },
                        {
                            "displayName": "canon_bmc",
                            "reputation": -0.0018234867453363385
                        },
                        {
                            "displayName": "canon_corj60",
                            "reputation": -8.609504815612713e-4
                        },
                        {
                            "displayName": "canon_corr",
                            "reputation": -3.1546801551301216e-4
                        },
                        {
                            "displayName": "canon_corr60",
                            "reputation": -8.844877887101668e-5
                        },
                        {
                            "displayName": "canon_cort20",
                            "reputation": 7.116906908434937e-4
                        },
                        {
                            "displayName": "canon_fnc_v3",
                            "reputation": -8.999663042777736e-4
                        },
                        {
                            "displayName": "canon_mmc",
                            "reputation": -0.0025902920161547842
                        },
                        {
                            "displayName": "canon_mmc60",
                            "reputation": -0.0013444422673000301
                        },
                        {
                            "displayName": "corj60",
                            "reputation": -8.376815496271829e-4
                        },
                        {
                            "displayName": "corr60",
                            "reputation": -1.1206374410356968e-4
                        },
                        {
                            "displayName": "corr_w_meta_model",
                            "reputation": 0.5629458073579748
                        },
                        {
                            "displayName": "cort20",
                            "reputation": 7.581684502455178e-4
                        },
                        {
                            "displayName": "fnc_v3",
                            "reputation": -9.587396139448935e-4
                        },
                        {
                            "displayName": "mcwnm",
                            "reputation": 0.2523330006926107
                        },
                        {
                            "displayName": "mmc",
                            "reputation": -0.002759453943740403
                        },
                        {
                            "displayName": "mmc60",
                            "reputation": -0.0017117045451966236
                        },
                        {
                            "displayName": "season_score",
                            "reputation": -0.005338318020908986
                        },
                        {
                            "displayName": "v2_corr20",
                            "reputation": -3.360700083628415e-4
                        }
                    ],
                    "name": "fnc_nai_fn",
                    "profileUrl": "https://numerai-public-images.s3-us-west-2.amazonaws.com/profile_images/fish_n_chips-gVl4x52eivQY.jpg",
                    "returns": null,
                    "submissionWebhook": null,
                    "tournament": 8,
                    "v2Stake": {
                        "latestValue": "0.000000000000000000",
                        "latestValueSettled": "0.000000000000000000",
                        "pendingV2ChangeStakeRequest": null,
                        "stakeValue": null,
                        "status": null
                    }
                },
                {
                    "computeEnabled": false,
                    "computePickleUpload": {
                        "id": "388b35b6-632b-4014-8ada-d20e8cc08c48"
                    },
                    "currentPayoutSelection": {
                        "corrMultiplier": 0.5,
                        "mmcMultiplier": 2.0,
                        "takeProfit": false,
                        "updatedAt": null
                    },
                    "description": null,
                    "earliestReleaseDate": "2025-09-24T00:00:00Z",
                    "id": "d0148af9-8723-4868-b4ab-b389dbec0042",
                    "isComputeWeekdayEnabled": true,
                    "latestSubmissions": [
                        {
                            "filename": "predictions-CLb2jXObNyco.csv",
                            "id": "4977b80d-4aaf-4f71-bba2-98f3c173ead4",
                            "roundCloseStaking": "2025-09-23",
                            "roundNumber": 1100,
                            "roundOpen": "2025-09-23",
                            "status": "on-time",
                            "timestamp": "2025-09-23T13:36:02Z"
                        },
                        {
                            "filename": "predictions-ivgGoKRZted7.csv",
                            "id": "eab3d4f5-c4ea-43fc-8f06-885a8aebae1d",
                            "roundCloseStaking": "2025-09-22",
                            "roundNumber": 1099,
                            "roundOpen": "2025-09-20",
                            "status": "on-time",
                            "timestamp": "2025-09-20T13:33:13Z"
                        },
                        {
                            "filename": "predictions-guvYocBLVZwg.csv",
                            "id": "5c26a52e-f7d2-4638-b6b5-c9f1909c2fe4",
                            "roundCloseStaking": "2025-09-19",
                            "roundNumber": 1098,
                            "roundOpen": "2025-09-19",
                            "status": "on-time",
                            "timestamp": "2025-09-19T13:23:53Z"
                        },
                        {
                            "filename": "predictions-fkgTYQpldSRN.csv",
                            "id": "5061ec1a-ec04-4593-a12e-8c6d5935a3bb",
                            "roundCloseStaking": "2025-09-18",
                            "roundNumber": 1097,
                            "roundOpen": "2025-09-18",
                            "status": "on-time",
                            "timestamp": "2025-09-18T13:34:17Z"
                        },
                        {
                            "filename": "predictions-O2Sn7ecLn6hF.csv",
                            "id": "ebe0c248-fa09-40b2-b44a-e4e15952be94",
                            "roundCloseStaking": "2025-09-17",
                            "roundNumber": 1096,
                            "roundOpen": "2025-09-17",
                            "status": "on-time",
                            "timestamp": "2025-09-17T13:35:58Z"
                        },
                        {
                            "filename": "predictions-rbNt2v5Uclip.csv",
                            "id": "6fb3739d-22f2-4bc1-b406-fec39f398bb0",
                            "roundCloseStaking": "2025-09-16",
                            "roundNumber": 1095,
                            "roundOpen": "2025-09-16",
                            "status": "on-time",
                            "timestamp": "2025-09-16T13:29:13Z"
                        },
                        {
                            "filename": "predictions-FeBYj2FOLk0J.csv",
                            "id": "4a381e81-5bc3-4891-9d40-4451c1acea68",
                            "roundCloseStaking": "2025-09-15",
                            "roundNumber": 1094,
                            "roundOpen": "2025-09-13",
                            "status": "on-time",
                            "timestamp": "2025-09-13T13:26:41Z"
                        },
                        {
                            "filename": "predictions-sqsdXdNqGMBL.csv",
                            "id": "c2727332-9336-40a5-b49a-d01b36c81b62",
                            "roundCloseStaking": "2025-09-12",
                            "roundNumber": 1093,
                            "roundOpen": "2025-09-12",
                            "status": "on-time",
                            "timestamp": "2025-09-12T13:31:32Z"
                        },
                        {
                            "filename": "predictions-NNHBExhBWRIi.csv",
                            "id": "44964666-d33a-4793-86c7-3e26fe29d375",
                            "roundCloseStaking": "2025-09-11",
                            "roundNumber": 1092,
                            "roundOpen": "2025-09-11",
                            "status": "on-time",
                            "timestamp": "2025-09-11T13:27:17Z"
                        },
                        {
                            "filename": "predictions-Wai1cEzHDsx7.csv",
                            "id": "868a32a3-2797-43ed-91df-3e19caa1ccc0",
                            "roundCloseStaking": "2025-09-10",
                            "roundNumber": 1091,
                            "roundOpen": "2025-09-10",
                            "status": "on-time",
                            "timestamp": "2025-09-10T13:31:50Z"
                        },
                        {
                            "filename": "predictions-okk5US0slDky.csv",
                            "id": "3cd8560d-8c30-47d9-bc89-d4c878250533",
                            "roundCloseStaking": "2025-09-09",
                            "roundNumber": 1090,
                            "roundOpen": "2025-09-09",
                            "status": "on-time",
                            "timestamp": "2025-09-09T13:31:22Z"
                        },
                        {
                            "filename": "predictions-DFtYKfyP9ovN.csv",
                            "id": "3d5c8c45-a799-43da-a9e5-267ed62df5bb",
                            "roundCloseStaking": "2025-09-08",
                            "roundNumber": 1089,
                            "roundOpen": "2025-09-06",
                            "status": "on-time",
                            "timestamp": "2025-09-06T13:27:44Z"
                        },
                        {
                            "filename": "predictions-iD7OiCkhaGHa.csv",
                            "id": "c29b668f-6295-4fc7-8c47-44331e352ed2",
                            "roundCloseStaking": "2025-09-05",
                            "roundNumber": 1088,
                            "roundOpen": "2025-09-05",
                            "status": "on-time",
                            "timestamp": "2025-09-05T13:30:09Z"
                        },
                        {
                            "filename": "predictions-ENP4r1t0OWgY.csv",
                            "id": "317b1459-5e21-47fa-9ef8-120f0548782d",
                            "roundCloseStaking": "2025-09-04",
                            "roundNumber": 1087,
                            "roundOpen": "2025-09-04",
                            "status": "on-time",
                            "timestamp": "2025-09-04T13:27:33Z"
                        },
                        {
                            "filename": "predictions-vcMXzzo5gijl.csv",
                            "id": "52ed95f8-2bcb-47a2-ae3a-0dd782e560be",
                            "roundCloseStaking": "2025-09-03",
                            "roundNumber": 1086,
                            "roundOpen": "2025-09-03",
                            "status": "on-time",
                            "timestamp": "2025-09-03T13:29:20Z"
                        },
                        {
                            "filename": "predictions-H4tp7RXjgDSL.csv",
                            "id": "cdff14c7-2d5f-4911-b8e3-e2ef1803936f",
                            "roundCloseStaking": "2025-09-02",
                            "roundNumber": 1085,
                            "roundOpen": "2025-09-02",
                            "status": "on-time",
                            "timestamp": "2025-09-02T13:41:01Z"
                        },
                        {
                            "filename": "predictions-Jb8yvozVDWpH.csv",
                            "id": "8d24cc83-4277-46f3-9086-204fdeebf13e",
                            "roundCloseStaking": "2025-09-01",
                            "roundNumber": 1084,
                            "roundOpen": "2025-08-30",
                            "status": "on-time",
                            "timestamp": "2025-08-30T13:29:11Z"
                        },
                        {
                            "filename": "predictions-n2a1nMHWBn15.csv",
                            "id": "575039ec-63ec-4b9d-ad91-168055e13381",
                            "roundCloseStaking": "2025-08-29",
                            "roundNumber": 1083,
                            "roundOpen": "2025-08-29",
                            "status": "on-time",
                            "timestamp": "2025-08-29T13:30:14Z"
                        },
                        {
                            "filename": "predictions-O4b2F0aJTOEx.csv",
                            "id": "770bc2bc-6d75-4ec7-ae15-e3764af3e4e2",
                            "roundCloseStaking": "2025-08-28",
                            "roundNumber": 1082,
                            "roundOpen": "2025-08-28",
                            "status": "on-time",
                            "timestamp": "2025-08-28T13:29:37Z"
                        },
                        {
                            "filename": "predictions-0ruQ0V5Oicnq.csv",
                            "id": "f51d9bcb-6c53-476c-88de-9fc3b43ca252",
                            "roundCloseStaking": "2025-08-27",
                            "roundNumber": 1081,
                            "roundOpen": "2025-08-27",
                            "status": "on-time",
                            "timestamp": "2025-08-27T13:30:01Z"
                        },
                        {
                            "filename": "predictions-hmPwTDlN6p9m.csv",
                            "id": "59f0772c-c953-4168-bf55-217ff13360c7",
                            "roundCloseStaking": "2025-08-26",
                            "roundNumber": 1080,
                            "roundOpen": "2025-08-26",
                            "status": "on-time",
                            "timestamp": "2025-08-26T13:32:18Z"
                        },
                        {
                            "filename": "predictions-J6oeUL19EvWL.csv",
                            "id": "88f1ef67-517b-4df8-9c9b-705ae615b6f0",
                            "roundCloseStaking": "2025-08-25",
                            "roundNumber": 1079,
                            "roundOpen": "2025-08-23",
                            "status": "on-time",
                            "timestamp": "2025-08-23T13:28:30Z"
                        },
                        {
                            "filename": "predictions-G8o1DyxuaaZv.csv",
                            "id": "6f24863e-0b57-4cab-a01e-eaa11df6e13d",
                            "roundCloseStaking": "2025-08-22",
                            "roundNumber": 1078,
                            "roundOpen": "2025-08-22",
                            "status": "on-time",
                            "timestamp": "2025-08-22T13:29:33Z"
                        },
                        {
                            "filename": "predictions-4H002TFdDJeq.csv",
                            "id": "047f6b8b-0e23-4e3e-b15b-5b8c6db0fe43",
                            "roundCloseStaking": "2025-08-21",
                            "roundNumber": 1077,
                            "roundOpen": "2025-08-21",
                            "status": "on-time",
                            "timestamp": "2025-08-21T13:28:19Z"
                        },
                        {
                            "filename": "predictions-KDa7Urr875BS.csv",
                            "id": "2aa2b947-0888-4247-a7a3-fb60952aaf43",
                            "roundCloseStaking": "2025-08-20",
                            "roundNumber": 1076,
                            "roundOpen": "2025-08-20",
                            "status": "on-time",
                            "timestamp": "2025-08-20T13:29:49Z"
                        },
                        {
                            "filename": "predictions-DQnejZDnNeAs.csv",
                            "id": "1ad568d1-50f2-4728-9b34-92a9aa1522ab",
                            "roundCloseStaking": "2025-08-19",
                            "roundNumber": 1075,
                            "roundOpen": "2025-08-19",
                            "status": "on-time",
                            "timestamp": "2025-08-19T13:28:23Z"
                        },
                        {
                            "filename": "predictions-nalP5peu9N2G.csv",
                            "id": "d8b2cdcc-ef00-4bd0-b8e8-cf496a46c3e4",
                            "roundCloseStaking": "2025-08-18",
                            "roundNumber": 1074,
                            "roundOpen": "2025-08-16",
                            "status": "on-time",
                            "timestamp": "2025-08-16T13:25:01Z"
                        },
                        {
                            "filename": "predictions-fBAMTsRF1N2E.csv",
                            "id": "59bc0203-6880-44af-813f-772777dc901b",
                            "roundCloseStaking": "2025-08-15",
                            "roundNumber": 1073,
                            "roundOpen": "2025-08-15",
                            "status": "on-time",
                            "timestamp": "2025-08-15T13:21:46Z"
                        },
                        {
                            "filename": "predictions-FLn5aDKUJ60u.csv",
                            "id": "b45da4f0-a7cf-4e9f-b60d-0990654cc5ac",
                            "roundCloseStaking": "2025-08-14",
                            "roundNumber": 1072,
                            "roundOpen": "2025-08-14",
                            "status": "on-time",
                            "timestamp": "2025-08-14T13:28:14Z"
                        },
                        {
                            "filename": "predictions-U2XXV2QZOiPc.csv",
                            "id": "ae24d6fd-a748-4fba-9683-3c5663936888",
                            "roundCloseStaking": "2025-08-13",
                            "roundNumber": 1071,
                            "roundOpen": "2025-08-13",
                            "status": "on-time",
                            "timestamp": "2025-08-13T13:28:32Z"
                        },
                        {
                            "filename": "predictions-YUkEvdkVzF8O.csv",
                            "id": "aec7a44e-3cec-4270-a19a-2f8476f59337",
                            "roundCloseStaking": "2025-08-12",
                            "roundNumber": 1070,
                            "roundOpen": "2025-08-12",
                            "status": "on-time",
                            "timestamp": "2025-08-12T13:31:12Z"
                        },
                        {
                            "filename": "predictions-GMMk7qO79Wg4.csv",
                            "id": "3e613494-2cf3-4fcd-b6de-2c94ead5a7ca",
                            "roundCloseStaking": "2025-08-11",
                            "roundNumber": 1069,
                            "roundOpen": "2025-08-09",
                            "status": "on-time",
                            "timestamp": "2025-08-09T13:28:19Z"
                        },
                        {
                            "filename": "predictions-BIBb1bpvE5pm.csv",
                            "id": "55204540-ace7-48ed-adc9-631d4f839d83",
                            "roundCloseStaking": "2025-08-08",
                            "roundNumber": 1068,
                            "roundOpen": "2025-08-08",
                            "status": "on-time",
                            "timestamp": "2025-08-08T13:31:56Z"
                        },
                        {
                            "filename": "predictions-Lpu6ax05Tfcf.csv",
                            "id": "6e62db59-fb4b-4b72-9a7e-c567766d1614",
                            "roundCloseStaking": "2025-08-07",
                            "roundNumber": 1067,
                            "roundOpen": "2025-08-07",
                            "status": "on-time",
                            "timestamp": "2025-08-07T13:32:35Z"
                        },
                        {
                            "filename": "predictions-KMSJeTwJnAMh.csv",
                            "id": "f9066883-ba7f-49d0-bf35-3c11f90e35c9",
                            "roundCloseStaking": "2025-08-06",
                            "roundNumber": 1066,
                            "roundOpen": "2025-08-06",
                            "status": "on-time",
                            "timestamp": "2025-08-06T13:36:01Z"
                        },
                        {
                            "filename": "predictions-zMJMZ1LSJV5q.csv",
                            "id": "f2250137-202b-4ccc-8d6d-812e68f1724f",
                            "roundCloseStaking": "2025-08-05",
                            "roundNumber": 1065,
                            "roundOpen": "2025-08-05",
                            "status": "on-time",
                            "timestamp": "2025-08-05T13:31:35Z"
                        },
                        {
                            "filename": "predictions-amATlnISTgbc.csv",
                            "id": "7040fda7-b454-4397-9d8c-a3d069168d43",
                            "roundCloseStaking": "2025-08-04",
                            "roundNumber": 1064,
                            "roundOpen": "2025-08-02",
                            "status": "on-time",
                            "timestamp": "2025-08-02T13:43:43Z"
                        },
                        {
                            "filename": "predictions-iKBOscqvABWP.csv",
                            "id": "8a2b5a5e-7384-4431-9233-64b0d6a5471c",
                            "roundCloseStaking": "2025-08-01",
                            "roundNumber": 1063,
                            "roundOpen": "2025-08-01",
                            "status": "on-time",
                            "timestamp": "2025-08-01T13:24:28Z"
                        },
                        {
                            "filename": "predictions-CVpcje1mcAXg.csv",
                            "id": "1ed4919f-47b9-44dc-aa33-72db56bdb5fe",
                            "roundCloseStaking": "2025-07-31",
                            "roundNumber": 1062,
                            "roundOpen": "2025-07-31",
                            "status": "on-time",
                            "timestamp": "2025-07-31T13:20:52Z"
                        },
                        {
                            "filename": "predictions-Zi1FHNHCxiMO.csv",
                            "id": "9d98473f-05c7-454a-abef-5c10b94074e7",
                            "roundCloseStaking": "2025-07-30",
                            "roundNumber": 1061,
                            "roundOpen": "2025-07-30",
                            "status": "on-time",
                            "timestamp": "2025-07-30T13:27:01Z"
                        },
                        {
                            "filename": "predictions-SwHZb0XX8XOi.csv",
                            "id": "9acc9338-532c-413e-9843-4c2a87545a86",
                            "roundCloseStaking": "2025-07-29",
                            "roundNumber": 1060,
                            "roundOpen": "2025-07-29",
                            "status": "on-time",
                            "timestamp": "2025-07-29T13:24:54Z"
                        },
                        {
                            "filename": "predictions-GQ4QPixROfgk.csv",
                            "id": "daf7ff73-0861-464d-8128-9bd0e9956e80",
                            "roundCloseStaking": "2025-07-28",
                            "roundNumber": 1059,
                            "roundOpen": "2025-07-26",
                            "status": "on-time",
                            "timestamp": "2025-07-26T13:27:42Z"
                        },
                        {
                            "filename": "predictions-DNttH5uqiCtn.csv",
                            "id": "5d0bf992-f3cd-432d-8ef9-f9f0098b7f81",
                            "roundCloseStaking": "2025-07-25",
                            "roundNumber": 1058,
                            "roundOpen": "2025-07-25",
                            "status": "on-time",
                            "timestamp": "2025-07-25T13:27:48Z"
                        },
                        {
                            "filename": "predictions-vHNKs45rMpPI.csv",
                            "id": "168269c3-02ed-414b-8b58-5894f4ebab32",
                            "roundCloseStaking": "2025-07-24",
                            "roundNumber": 1057,
                            "roundOpen": "2025-07-24",
                            "status": "on-time",
                            "timestamp": "2025-07-24T13:26:17Z"
                        },
                        {
                            "filename": "predictions-zZ8YSHOLmvVt.csv",
                            "id": "e3b2d4bd-2767-49fc-bd27-9661b72c18f8",
                            "roundCloseStaking": "2025-07-23",
                            "roundNumber": 1056,
                            "roundOpen": "2025-07-23",
                            "status": "on-time",
                            "timestamp": "2025-07-23T13:25:52Z"
                        },
                        {
                            "filename": "predictions-3FmMttwKz2wi.csv",
                            "id": "b250a8d2-534b-4b68-a9df-9f402465edc0",
                            "roundCloseStaking": "2025-07-22",
                            "roundNumber": 1055,
                            "roundOpen": "2025-07-22",
                            "status": "on-time",
                            "timestamp": "2025-07-22T13:27:10Z"
                        },
                        {
                            "filename": "predictions-jyNeEO5KaNSj.csv",
                            "id": "bde9ad6c-767a-46ea-8290-3ba7b303b9c6",
                            "roundCloseStaking": "2025-07-21",
                            "roundNumber": 1054,
                            "roundOpen": "2025-07-19",
                            "status": "on-time",
                            "timestamp": "2025-07-19T13:23:13Z"
                        },
                        {
                            "filename": "predictions-3K5CfP6yuk7Q.csv",
                            "id": "8347e21b-e982-4ec5-bd75-3aceabeda9b6",
                            "roundCloseStaking": "2025-07-18",
                            "roundNumber": 1053,
                            "roundOpen": "2025-07-18",
                            "status": "on-time",
                            "timestamp": "2025-07-18T13:28:00Z"
                        },
                        {
                            "filename": "predictions-JbwjBnhlbpmy.csv",
                            "id": "873c2c51-22f2-4f3c-be46-6ac810afb9cb",
                            "roundCloseStaking": "2025-07-17",
                            "roundNumber": 1052,
                            "roundOpen": "2025-07-17",
                            "status": "on-time",
                            "timestamp": "2025-07-17T13:28:32Z"
                        },
                        {
                            "filename": "predictions-DVoQg4aYmFhj.csv",
                            "id": "186e68e6-3022-4353-97b5-9059713ad672",
                            "roundCloseStaking": "2025-07-16",
                            "roundNumber": 1051,
                            "roundOpen": "2025-07-16",
                            "status": "on-time",
                            "timestamp": "2025-07-16T13:27:05Z"
                        },
                        {
                            "filename": "predictions-XEYRsxbEnP7Q.csv",
                            "id": "7c68b225-d7b0-4a55-8131-d3b809f5a49f",
                            "roundCloseStaking": "2025-07-15",
                            "roundNumber": 1050,
                            "roundOpen": "2025-07-15",
                            "status": "on-time",
                            "timestamp": "2025-07-15T13:27:34Z"
                        },
                        {
                            "filename": "predictions-usZ4UC6rxWMh.csv",
                            "id": "a251245b-181f-48b0-9390-de1ce55e9142",
                            "roundCloseStaking": "2025-07-14",
                            "roundNumber": 1049,
                            "roundOpen": "2025-07-12",
                            "status": "on-time",
                            "timestamp": "2025-07-12T13:32:40Z"
                        },
                        {
                            "filename": "predictions-GpG9CbDIoAeW.csv",
                            "id": "822707a8-e8cd-4e0f-a319-1f0fe1cbb8ee",
                            "roundCloseStaking": "2025-07-11",
                            "roundNumber": 1048,
                            "roundOpen": "2025-07-11",
                            "status": "on-time",
                            "timestamp": "2025-07-11T13:23:20Z"
                        },
                        {
                            "filename": "predictions-aydgnkNtdB4H.csv",
                            "id": "e68778ee-2980-46dd-bd0b-7dbad4d7a76d",
                            "roundCloseStaking": "2025-07-10",
                            "roundNumber": 1047,
                            "roundOpen": "2025-07-10",
                            "status": "on-time",
                            "timestamp": "2025-07-10T13:26:01Z"
                        },
                        {
                            "filename": "predictions-mWyIftdZmjWQ.csv",
                            "id": "209da159-4ee2-4faf-997f-b2a9d4ac070f",
                            "roundCloseStaking": "2025-07-09",
                            "roundNumber": 1046,
                            "roundOpen": "2025-07-09",
                            "status": "on-time",
                            "timestamp": "2025-07-09T13:25:50Z"
                        },
                        {
                            "filename": "predictions-s5GEVShvOWyN.csv",
                            "id": "9c77d2c5-4806-4058-a6e0-d7dd5d28267c",
                            "roundCloseStaking": "2025-07-08",
                            "roundNumber": 1045,
                            "roundOpen": "2025-07-08",
                            "status": "on-time",
                            "timestamp": "2025-07-08T14:13:42Z"
                        },
                        {
                            "filename": "predictions-Uuly9Jx5NZYF.csv",
                            "id": "63d48861-a039-4f05-84c4-6a2b76a098af",
                            "roundCloseStaking": "2025-07-07",
                            "roundNumber": 1044,
                            "roundOpen": "2025-07-05",
                            "status": "on-time",
                            "timestamp": "2025-07-05T14:15:20Z"
                        },
                        {
                            "filename": "predictions-dqbeNkV13tPu.csv",
                            "id": "25118910-9226-4419-8705-ce8eb90a6b51",
                            "roundCloseStaking": "2025-07-04",
                            "roundNumber": 1043,
                            "roundOpen": "2025-07-04",
                            "status": "on-time",
                            "timestamp": "2025-07-04T13:33:49Z"
                        },
                        {
                            "filename": "predictions-Qu7z1NVD2B0a.csv",
                            "id": "618ac1b6-1b12-499e-aaa9-6c18edaaa126",
                            "roundCloseStaking": "2025-07-03",
                            "roundNumber": 1042,
                            "roundOpen": "2025-07-03",
                            "status": "on-time",
                            "timestamp": "2025-07-03T13:55:16Z"
                        },
                        {
                            "filename": "predictions-bWniqu0ZsPaq.csv",
                            "id": "21db04c1-48e9-4f94-add7-ba09af9217d3",
                            "roundCloseStaking": "2025-07-02",
                            "roundNumber": 1041,
                            "roundOpen": "2025-07-02",
                            "status": "on-time",
                            "timestamp": "2025-07-02T13:49:02Z"
                        },
                        {
                            "filename": "predictions-ptPfskv6wVdF.csv",
                            "id": "bae60b38-21b4-4cbc-8169-f75cab206fa2",
                            "roundCloseStaking": "2025-07-01",
                            "roundNumber": 1040,
                            "roundOpen": "2025-07-01",
                            "status": "on-time",
                            "timestamp": "2025-07-01T13:59:57Z"
                        }
                    ],
                    "latestUserScores": [
                        {
                            "displayName": "apcwnm",
                            "reputation": 0.06611841319935305
                        },
                        {
                            "displayName": "bmc",
                            "reputation": -0.0019172994862348418
                        },
                        {
                            "displayName": "canon_bmc",
                            "reputation": -0.0017924179105030704
                        },
                        {
                            "displayName": "canon_corj60",
                            "reputation": -9.133279150163482e-4
                        },
                        {
                            "displayName": "canon_corr",
                            "reputation": -8.272038626209611e-4
                        },
                        {
                            "displayName": "canon_corr60",
                            "reputation": -7.276800602157264e-4
                        },
                        {
                            "displayName": "canon_cort20",
                            "reputation": 5.349911049585548e-4
                        },
                        {
                            "displayName": "canon_fnc_v3",
                            "reputation": -4.6052368225060227e-4
                        },
                        {
                            "displayName": "canon_mmc",
                            "reputation": -0.0020674931245773854
                        },
                        {
                            "displayName": "canon_mmc60",
                            "reputation": -0.0012945550202451118
                        },
                        {
                            "displayName": "corj60",
                            "reputation": -8.886433767726631e-4
                        },
                        {
                            "displayName": "corr60",
                            "reputation": -9.219635714383717e-4
                        },
                        {
                            "displayName": "corr_w_meta_model",
                            "reputation": 0.3676222551110385
                        },
                        {
                            "displayName": "cort20",
                            "reputation": 5.69929299568093e-4
                        },
                        {
                            "displayName": "fnc_v3",
                            "reputation": -4.905986982343151e-4
                        },
                        {
                            "displayName": "mcwnm",
                            "reputation": 0.23478828451103867
                        },
                        {
                            "displayName": "mmc",
                            "reputation": -0.0022025130837334595
                        },
                        {
                            "displayName": "mmc60",
                            "reputation": -0.0016481895623608497
                        },
                        {
                            "displayName": "season_score",
                            "reputation": -0.004548588218779428
                        },
                        {
                            "displayName": "v2_corr20",
                            "reputation": -8.812253393635545e-4
                        }
                    ],
                    "name": "fnc_nai_te",
                    "profileUrl": "https://numerai-public-images.s3-us-west-2.amazonaws.com/profile_images/fish_n_chips-fhP1yo6VgABa.jpg",
                    "returns": null,
                    "submissionWebhook": null,
                    "tournament": 8,
                    "v2Stake": {
                        "latestValue": "0.000000000000000000",
                        "latestValueSettled": "0.000000000000000000",
                        "pendingV2ChangeStakeRequest": null,
                        "stakeValue": null,
                        "status": null
                    }
                },
                {
                    "computeEnabled": false,
                    "computePickleUpload": null,
                    "currentPayoutSelection": {
                        "corrMultiplier": 0.0,
                        "mmcMultiplier": 1.0,
                        "takeProfit": false,
                        "updatedAt": null
                    },
                    "description": null,
                    "earliestReleaseDate": "2025-10-24T00:00:00Z",
                    "id": "c37f58b4-eacc-44f5-9220-ad2b3b00b429",
                    "isComputeWeekdayEnabled": true,
                    "latestSubmissions": [
                        {
                            "filename": "lightgbm_submission-isGYvEpnBrUM.parquet",
                            "id": "6c27f1ba-20a9-425e-bcf0-b72b8bf18741",
                            "roundCloseStaking": "2025-09-23",
                            "roundNumber": 1100,
                            "roundOpen": "2025-09-23",
                            "status": "on-time",
                            "timestamp": "2025-09-23T13:02:27Z"
                        },
                        {
                            "filename": "lightgbm_submission-isGYvEpnBrUM.parquet",
                            "id": "3d0cafba-165e-4e85-9b7b-6a892b182aba",
                            "roundCloseStaking": "2025-09-22",
                            "roundNumber": 1099,
                            "roundOpen": "2025-09-20",
                            "status": "late",
                            "timestamp": "2025-09-23T07:22:37Z"
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-19",
                            "roundNumber": 1098,
                            "roundOpen": "2025-09-19",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-18",
                            "roundNumber": 1097,
                            "roundOpen": "2025-09-18",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-17",
                            "roundNumber": 1096,
                            "roundOpen": "2025-09-17",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-16",
                            "roundNumber": 1095,
                            "roundOpen": "2025-09-16",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-15",
                            "roundNumber": 1094,
                            "roundOpen": "2025-09-13",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-12",
                            "roundNumber": 1093,
                            "roundOpen": "2025-09-12",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-11",
                            "roundNumber": 1092,
                            "roundOpen": "2025-09-11",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-10",
                            "roundNumber": 1091,
                            "roundOpen": "2025-09-10",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-09",
                            "roundNumber": 1090,
                            "roundOpen": "2025-09-09",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-08",
                            "roundNumber": 1089,
                            "roundOpen": "2025-09-06",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-05",
                            "roundNumber": 1088,
                            "roundOpen": "2025-09-05",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-04",
                            "roundNumber": 1087,
                            "roundOpen": "2025-09-04",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-03",
                            "roundNumber": 1086,
                            "roundOpen": "2025-09-03",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-02",
                            "roundNumber": 1085,
                            "roundOpen": "2025-09-02",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-01",
                            "roundNumber": 1084,
                            "roundOpen": "2025-08-30",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-29",
                            "roundNumber": 1083,
                            "roundOpen": "2025-08-29",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-28",
                            "roundNumber": 1082,
                            "roundOpen": "2025-08-28",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-27",
                            "roundNumber": 1081,
                            "roundOpen": "2025-08-27",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-26",
                            "roundNumber": 1080,
                            "roundOpen": "2025-08-26",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-25",
                            "roundNumber": 1079,
                            "roundOpen": "2025-08-23",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-22",
                            "roundNumber": 1078,
                            "roundOpen": "2025-08-22",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-21",
                            "roundNumber": 1077,
                            "roundOpen": "2025-08-21",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-20",
                            "roundNumber": 1076,
                            "roundOpen": "2025-08-20",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-19",
                            "roundNumber": 1075,
                            "roundOpen": "2025-08-19",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-18",
                            "roundNumber": 1074,
                            "roundOpen": "2025-08-16",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-15",
                            "roundNumber": 1073,
                            "roundOpen": "2025-08-15",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-14",
                            "roundNumber": 1072,
                            "roundOpen": "2025-08-14",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-13",
                            "roundNumber": 1071,
                            "roundOpen": "2025-08-13",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-12",
                            "roundNumber": 1070,
                            "roundOpen": "2025-08-12",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-11",
                            "roundNumber": 1069,
                            "roundOpen": "2025-08-09",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-08",
                            "roundNumber": 1068,
                            "roundOpen": "2025-08-08",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-07",
                            "roundNumber": 1067,
                            "roundOpen": "2025-08-07",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-06",
                            "roundNumber": 1066,
                            "roundOpen": "2025-08-06",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-05",
                            "roundNumber": 1065,
                            "roundOpen": "2025-08-05",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-04",
                            "roundNumber": 1064,
                            "roundOpen": "2025-08-02",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-01",
                            "roundNumber": 1063,
                            "roundOpen": "2025-08-01",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-31",
                            "roundNumber": 1062,
                            "roundOpen": "2025-07-31",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-30",
                            "roundNumber": 1061,
                            "roundOpen": "2025-07-30",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-29",
                            "roundNumber": 1060,
                            "roundOpen": "2025-07-29",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-28",
                            "roundNumber": 1059,
                            "roundOpen": "2025-07-26",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-25",
                            "roundNumber": 1058,
                            "roundOpen": "2025-07-25",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-24",
                            "roundNumber": 1057,
                            "roundOpen": "2025-07-24",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-23",
                            "roundNumber": 1056,
                            "roundOpen": "2025-07-23",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-22",
                            "roundNumber": 1055,
                            "roundOpen": "2025-07-22",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-21",
                            "roundNumber": 1054,
                            "roundOpen": "2025-07-19",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-18",
                            "roundNumber": 1053,
                            "roundOpen": "2025-07-18",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-17",
                            "roundNumber": 1052,
                            "roundOpen": "2025-07-17",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-16",
                            "roundNumber": 1051,
                            "roundOpen": "2025-07-16",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-15",
                            "roundNumber": 1050,
                            "roundOpen": "2025-07-15",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-14",
                            "roundNumber": 1049,
                            "roundOpen": "2025-07-12",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-11",
                            "roundNumber": 1048,
                            "roundOpen": "2025-07-11",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-10",
                            "roundNumber": 1047,
                            "roundOpen": "2025-07-10",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-09",
                            "roundNumber": 1046,
                            "roundOpen": "2025-07-09",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-08",
                            "roundNumber": 1045,
                            "roundOpen": "2025-07-08",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-07",
                            "roundNumber": 1044,
                            "roundOpen": "2025-07-05",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-04",
                            "roundNumber": 1043,
                            "roundOpen": "2025-07-04",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-03",
                            "roundNumber": 1042,
                            "roundOpen": "2025-07-03",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-02",
                            "roundNumber": 1041,
                            "roundOpen": "2025-07-02",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-01",
                            "roundNumber": 1040,
                            "roundOpen": "2025-07-01",
                            "status": "none",
                            "timestamp": null
                        }
                    ],
                    "latestUserScores": null,
                    "name": "fncc_lightgbm",
                    "profileUrl": null,
                    "returns": null,
                    "submissionWebhook": null,
                    "tournament": 12,
                    "v2Stake": {
                        "latestValue": "1.000000000000000000",
                        "latestValueSettled": "1.000000000000000000",
                        "pendingV2ChangeStakeRequest": null,
                        "stakeValue": "1.000000000000000000",
                        "status": null
                    }
                },
                {
                    "computeEnabled": false,
                    "computePickleUpload": {
                        "id": "74a3b572-462c-4ec8-98d8-c3fdde0e8550"
                    },
                    "currentPayoutSelection": {
                        "corrMultiplier": 0.5,
                        "mmcMultiplier": 2.0,
                        "takeProfit": false,
                        "updatedAt": null
                    },
                    "description": null,
                    "earliestReleaseDate": "2025-10-24T00:00:00Z",
                    "id": "54e6acad-6a1d-4c9e-9acc-c0336f239a0b",
                    "isComputeWeekdayEnabled": true,
                    "latestSubmissions": [
                        {
                            "filename": "predictions-xoWAX6kftBfI.csv",
                            "id": "f042d7a8-3594-499b-a797-b455b98f1ada",
                            "roundCloseStaking": "2025-09-23",
                            "roundNumber": 1100,
                            "roundOpen": "2025-09-23",
                            "status": "on-time",
                            "timestamp": "2025-09-23T13:31:52Z"
                        },
                        {
                            "filename": "predictions-EshmKotECPFy.csv",
                            "id": "eb5da26f-0da6-4a51-aa26-d286f38169d2",
                            "roundCloseStaking": "2025-09-22",
                            "roundNumber": 1099,
                            "roundOpen": "2025-09-20",
                            "status": "on-time",
                            "timestamp": "2025-09-20T13:31:09Z"
                        },
                        {
                            "filename": "predictions-Z227zQ7lKDLU.csv",
                            "id": "a51a2d9b-03c3-4b6a-9b9b-761092af0134",
                            "roundCloseStaking": "2025-09-19",
                            "roundNumber": 1098,
                            "roundOpen": "2025-09-19",
                            "status": "on-time",
                            "timestamp": "2025-09-19T13:28:36Z"
                        },
                        {
                            "filename": "predictions-X1WsSazcbk60.csv",
                            "id": "b021317d-1345-47ff-b7c4-a1ffa9410717",
                            "roundCloseStaking": "2025-09-18",
                            "roundNumber": 1097,
                            "roundOpen": "2025-09-18",
                            "status": "on-time",
                            "timestamp": "2025-09-18T13:27:09Z"
                        },
                        {
                            "filename": "predictions-fsGxTS7uPlNy.csv",
                            "id": "9e7eae63-2a71-41b5-95eb-fc4c6992ccc1",
                            "roundCloseStaking": "2025-09-17",
                            "roundNumber": 1096,
                            "roundOpen": "2025-09-17",
                            "status": "on-time",
                            "timestamp": "2025-09-17T13:28:05Z"
                        },
                        {
                            "filename": "predictions-JaeuAj8YEGn3.csv",
                            "id": "859ec7a9-bc61-406d-ac05-258d02516778",
                            "roundCloseStaking": "2025-09-16",
                            "roundNumber": 1095,
                            "roundOpen": "2025-09-16",
                            "status": "on-time",
                            "timestamp": "2025-09-16T13:28:00Z"
                        },
                        {
                            "filename": "predictions-82bUEj5OHKtJ.csv",
                            "id": "67328a82-526e-46a4-bd75-c63f1bc12b2f",
                            "roundCloseStaking": "2025-09-15",
                            "roundNumber": 1094,
                            "roundOpen": "2025-09-13",
                            "status": "on-time",
                            "timestamp": "2025-09-13T13:34:30Z"
                        },
                        {
                            "filename": "predictions-UAAzIVNUOp5F.csv",
                            "id": "0642c664-6dbf-469f-a1c1-c4e6d7b9b510",
                            "roundCloseStaking": "2025-09-12",
                            "roundNumber": 1093,
                            "roundOpen": "2025-09-12",
                            "status": "on-time",
                            "timestamp": "2025-09-12T13:35:51Z"
                        },
                        {
                            "filename": "predictions-JQMe1Azogi2u.csv",
                            "id": "1919f738-2887-4d83-b832-e25e1971bdde",
                            "roundCloseStaking": "2025-09-11",
                            "roundNumber": 1092,
                            "roundOpen": "2025-09-11",
                            "status": "on-time",
                            "timestamp": "2025-09-11T13:28:06Z"
                        },
                        {
                            "filename": "predictions-8AW4kmSpUIFe.csv",
                            "id": "092956aa-0718-445e-b0cb-d00111262276",
                            "roundCloseStaking": "2025-09-10",
                            "roundNumber": 1091,
                            "roundOpen": "2025-09-10",
                            "status": "on-time",
                            "timestamp": "2025-09-10T13:29:18Z"
                        },
                        {
                            "filename": "predictions-3rLgbTs6IXSj.csv",
                            "id": "ded6a5b3-02dc-4427-a32e-9b5221198033",
                            "roundCloseStaking": "2025-09-09",
                            "roundNumber": 1090,
                            "roundOpen": "2025-09-09",
                            "status": "on-time",
                            "timestamp": "2025-09-09T13:29:52Z"
                        },
                        {
                            "filename": "predictions-fUhHt58vLEcz.csv",
                            "id": "665ec3d3-473c-440e-800e-382082385ed1",
                            "roundCloseStaking": "2025-09-08",
                            "roundNumber": 1089,
                            "roundOpen": "2025-09-06",
                            "status": "on-time",
                            "timestamp": "2025-09-06T13:24:11Z"
                        },
                        {
                            "filename": "predictions-PDbxZ7mxi39k.csv",
                            "id": "9d9ecd8b-c0ae-4655-afd8-92c52b60d2c7",
                            "roundCloseStaking": "2025-09-05",
                            "roundNumber": 1088,
                            "roundOpen": "2025-09-05",
                            "status": "on-time",
                            "timestamp": "2025-09-05T13:34:25Z"
                        },
                        {
                            "filename": "predictions-32jOeqQ5e3C4.csv",
                            "id": "f60a39d0-7ed5-4974-90bf-d2488c5636dc",
                            "roundCloseStaking": "2025-09-04",
                            "roundNumber": 1087,
                            "roundOpen": "2025-09-04",
                            "status": "on-time",
                            "timestamp": "2025-09-04T13:27:25Z"
                        },
                        {
                            "filename": "predictions-GUJzItO00HLf.csv",
                            "id": "d03844bf-e26e-49a6-b1a9-65ddd9c60cca",
                            "roundCloseStaking": "2025-09-03",
                            "roundNumber": 1086,
                            "roundOpen": "2025-09-03",
                            "status": "on-time",
                            "timestamp": "2025-09-03T13:29:06Z"
                        },
                        {
                            "filename": "predictions-h87cwvZYITYH.csv",
                            "id": "73f6018e-4b69-4d80-865c-d24024394504",
                            "roundCloseStaking": "2025-09-02",
                            "roundNumber": 1085,
                            "roundOpen": "2025-09-02",
                            "status": "on-time",
                            "timestamp": "2025-09-02T13:35:30Z"
                        },
                        {
                            "filename": "predictions-NUz3VPQ4zyJL.csv",
                            "id": "0397a9f6-e88d-4a8b-9c59-3dc7ee7f3f30",
                            "roundCloseStaking": "2025-09-01",
                            "roundNumber": 1084,
                            "roundOpen": "2025-08-30",
                            "status": "on-time",
                            "timestamp": "2025-08-30T13:31:26Z"
                        },
                        {
                            "filename": "predictions-KsBMNLONWtQV.csv",
                            "id": "8d68f777-e841-4e9f-b1b2-6be3abccb5c5",
                            "roundCloseStaking": "2025-08-29",
                            "roundNumber": 1083,
                            "roundOpen": "2025-08-29",
                            "status": "on-time",
                            "timestamp": "2025-08-29T13:25:32Z"
                        },
                        {
                            "filename": "predictions-6T3KYVdfyGol.csv",
                            "id": "5f7a0e15-46bc-4ae3-980d-ba2666fb4067",
                            "roundCloseStaking": "2025-08-28",
                            "roundNumber": 1082,
                            "roundOpen": "2025-08-28",
                            "status": "on-time",
                            "timestamp": "2025-08-28T13:27:27Z"
                        },
                        {
                            "filename": "predictions-vtpSp3c9kUdA.csv",
                            "id": "7f9c5b0f-3d9d-4345-a223-d8c324af75d2",
                            "roundCloseStaking": "2025-08-27",
                            "roundNumber": 1081,
                            "roundOpen": "2025-08-27",
                            "status": "on-time",
                            "timestamp": "2025-08-27T13:25:22Z"
                        },
                        {
                            "filename": "predictions-rDV1xTbi47YT.csv",
                            "id": "56910eb4-3d31-4e94-af4a-4da231d7e225",
                            "roundCloseStaking": "2025-08-26",
                            "roundNumber": 1080,
                            "roundOpen": "2025-08-26",
                            "status": "on-time",
                            "timestamp": "2025-08-26T13:27:27Z"
                        },
                        {
                            "filename": "predictions-PMHVU3pMMNjj.csv",
                            "id": "1b71974f-3c46-4196-b3cc-dc2f54c99c68",
                            "roundCloseStaking": "2025-08-25",
                            "roundNumber": 1079,
                            "roundOpen": "2025-08-23",
                            "status": "on-time",
                            "timestamp": "2025-08-23T13:24:58Z"
                        },
                        {
                            "filename": "predictions-bKYE46svCqNK.csv",
                            "id": "6b6a4e64-a7be-458b-84e7-58353baca1eb",
                            "roundCloseStaking": "2025-08-22",
                            "roundNumber": 1078,
                            "roundOpen": "2025-08-22",
                            "status": "on-time",
                            "timestamp": "2025-08-22T13:29:41Z"
                        },
                        {
                            "filename": "predictions-ERwFT34BNc2t.csv",
                            "id": "3946ad1a-4107-46e3-a76b-e820bc5173f7",
                            "roundCloseStaking": "2025-08-21",
                            "roundNumber": 1077,
                            "roundOpen": "2025-08-21",
                            "status": "on-time",
                            "timestamp": "2025-08-21T13:26:50Z"
                        },
                        {
                            "filename": "predictions-9mGYK3eLC5I3.csv",
                            "id": "d704dd32-9989-4f4a-8a52-1c61cd06d80a",
                            "roundCloseStaking": "2025-08-20",
                            "roundNumber": 1076,
                            "roundOpen": "2025-08-20",
                            "status": "on-time",
                            "timestamp": "2025-08-20T13:26:08Z"
                        },
                        {
                            "filename": "predictions-KxrAScdPg3TL.csv",
                            "id": "b19a8e39-26e9-4519-849d-dfe09328ef38",
                            "roundCloseStaking": "2025-08-19",
                            "roundNumber": 1075,
                            "roundOpen": "2025-08-19",
                            "status": "on-time",
                            "timestamp": "2025-08-19T13:26:35Z"
                        },
                        {
                            "filename": "predictions-gDkhVnO6CIBf.csv",
                            "id": "afb8e141-abd8-402d-9342-ed9772fd370e",
                            "roundCloseStaking": "2025-08-18",
                            "roundNumber": 1074,
                            "roundOpen": "2025-08-16",
                            "status": "on-time",
                            "timestamp": "2025-08-16T13:23:21Z"
                        },
                        {
                            "filename": "predictions-CC7PNtT2c2a6.csv",
                            "id": "6c736d1d-7bc0-40b4-abb5-a632d469a620",
                            "roundCloseStaking": "2025-08-15",
                            "roundNumber": 1073,
                            "roundOpen": "2025-08-15",
                            "status": "on-time",
                            "timestamp": "2025-08-15T13:26:23Z"
                        },
                        {
                            "filename": "predictions-BrgisGmaceZ3.csv",
                            "id": "e83ed813-fe37-4c0e-84fd-ea6dc2c0402b",
                            "roundCloseStaking": "2025-08-14",
                            "roundNumber": 1072,
                            "roundOpen": "2025-08-14",
                            "status": "on-time",
                            "timestamp": "2025-08-14T13:27:43Z"
                        },
                        {
                            "filename": "predictions-HCRh4cA796o0.csv",
                            "id": "cd116e18-df9d-491c-827a-212dde4307d1",
                            "roundCloseStaking": "2025-08-13",
                            "roundNumber": 1071,
                            "roundOpen": "2025-08-13",
                            "status": "on-time",
                            "timestamp": "2025-08-13T13:28:46Z"
                        },
                        {
                            "filename": "predictions-F4lasLgQNlTr.csv",
                            "id": "1b03ab81-0182-4e5f-91d9-3523289725f8",
                            "roundCloseStaking": "2025-08-12",
                            "roundNumber": 1070,
                            "roundOpen": "2025-08-12",
                            "status": "on-time",
                            "timestamp": "2025-08-12T13:32:31Z"
                        },
                        {
                            "filename": "predictions-k4MUelGhhD5G.csv",
                            "id": "4f685214-bd03-47dd-beb0-a2ea94d8f964",
                            "roundCloseStaking": "2025-08-11",
                            "roundNumber": 1069,
                            "roundOpen": "2025-08-09",
                            "status": "on-time",
                            "timestamp": "2025-08-09T13:26:44Z"
                        },
                        {
                            "filename": "predictions-ByqrnDpMydTi.csv",
                            "id": "1a923e7a-3b0a-449d-a974-493ee809d371",
                            "roundCloseStaking": "2025-08-08",
                            "roundNumber": 1068,
                            "roundOpen": "2025-08-08",
                            "status": "on-time",
                            "timestamp": "2025-08-08T13:26:35Z"
                        },
                        {
                            "filename": "predictions-6zQs6DDoTf8C.csv",
                            "id": "a18d00d8-9ba7-49bf-87b6-e8710e4f078d",
                            "roundCloseStaking": "2025-08-07",
                            "roundNumber": 1067,
                            "roundOpen": "2025-08-07",
                            "status": "on-time",
                            "timestamp": "2025-08-07T13:28:49Z"
                        },
                        {
                            "filename": "predictions-Y4OnCKZY17qt.csv",
                            "id": "83daf3ac-2bac-4558-9431-dcf46ebe1bc7",
                            "roundCloseStaking": "2025-08-06",
                            "roundNumber": 1066,
                            "roundOpen": "2025-08-06",
                            "status": "on-time",
                            "timestamp": "2025-08-06T13:28:58Z"
                        },
                        {
                            "filename": "predictions-ijYHv83yssWb.csv",
                            "id": "77521f41-3365-4bc4-9f39-ebbf149e75cc",
                            "roundCloseStaking": "2025-08-05",
                            "roundNumber": 1065,
                            "roundOpen": "2025-08-05",
                            "status": "on-time",
                            "timestamp": "2025-08-05T13:22:06Z"
                        },
                        {
                            "filename": "predictions-JV8zIdTMrUSw.csv",
                            "id": "68bff969-8a3c-4c66-b755-79ce11cddf59",
                            "roundCloseStaking": "2025-08-04",
                            "roundNumber": 1064,
                            "roundOpen": "2025-08-02",
                            "status": "on-time",
                            "timestamp": "2025-08-02T13:33:27Z"
                        },
                        {
                            "filename": "predictions-7VAelDOyYiem.csv",
                            "id": "841dab54-f43d-454a-9b15-1d9f0795a6ce",
                            "roundCloseStaking": "2025-08-01",
                            "roundNumber": 1063,
                            "roundOpen": "2025-08-01",
                            "status": "on-time",
                            "timestamp": "2025-08-01T13:25:11Z"
                        },
                        {
                            "filename": "predictions-X8rAIo9NuipX.csv",
                            "id": "f30db3df-68b1-4982-a5f2-7a14c49faf66",
                            "roundCloseStaking": "2025-07-31",
                            "roundNumber": 1062,
                            "roundOpen": "2025-07-31",
                            "status": "on-time",
                            "timestamp": "2025-07-31T13:25:05Z"
                        },
                        {
                            "filename": "predictions-gTpntxkbstpi.csv",
                            "id": "bea40f23-f7c4-4d66-86a2-207483079c62",
                            "roundCloseStaking": "2025-07-30",
                            "roundNumber": 1061,
                            "roundOpen": "2025-07-30",
                            "status": "on-time",
                            "timestamp": "2025-07-30T13:24:44Z"
                        },
                        {
                            "filename": "predictions-ns4fjvolwa1n.csv",
                            "id": "9aab7c6f-7fd1-4552-8cce-237f93c4dfe0",
                            "roundCloseStaking": "2025-07-29",
                            "roundNumber": 1060,
                            "roundOpen": "2025-07-29",
                            "status": "on-time",
                            "timestamp": "2025-07-29T13:23:34Z"
                        },
                        {
                            "filename": "predictions-rqBxsQS4Gvq4.csv",
                            "id": "2ffb5dde-1ecc-458a-b848-6afe3b562b19",
                            "roundCloseStaking": "2025-07-28",
                            "roundNumber": 1059,
                            "roundOpen": "2025-07-26",
                            "status": "on-time",
                            "timestamp": "2025-07-26T13:25:01Z"
                        },
                        {
                            "filename": "predictions-v1Up37u9mDy5.csv",
                            "id": "b06efe66-063d-4010-82dc-7a07cdb3847c",
                            "roundCloseStaking": "2025-07-25",
                            "roundNumber": 1058,
                            "roundOpen": "2025-07-25",
                            "status": "on-time",
                            "timestamp": "2025-07-25T13:26:05Z"
                        },
                        {
                            "filename": "predictions-AFm9pPwIOLQc.csv",
                            "id": "432e5aa5-b49b-4abd-8301-086273d2923f",
                            "roundCloseStaking": "2025-07-24",
                            "roundNumber": 1057,
                            "roundOpen": "2025-07-24",
                            "status": "on-time",
                            "timestamp": "2025-07-24T13:22:47Z"
                        },
                        {
                            "filename": "predictions-JJWFBpqgHU0z.csv",
                            "id": "65fa5e73-2e6a-4354-b35e-92d02d75cb54",
                            "roundCloseStaking": "2025-07-23",
                            "roundNumber": 1056,
                            "roundOpen": "2025-07-23",
                            "status": "on-time",
                            "timestamp": "2025-07-23T13:17:17Z"
                        },
                        {
                            "filename": "predictions-uHk59uvF7w7N.csv",
                            "id": "11db10bc-2a09-4127-82da-a060fe597d8c",
                            "roundCloseStaking": "2025-07-22",
                            "roundNumber": 1055,
                            "roundOpen": "2025-07-22",
                            "status": "on-time",
                            "timestamp": "2025-07-22T13:24:41Z"
                        },
                        {
                            "filename": "predictions-5aTV8HG8LRyn.csv",
                            "id": "b4a2f424-11f5-46cb-afac-f0ebfc00a0a5",
                            "roundCloseStaking": "2025-07-21",
                            "roundNumber": 1054,
                            "roundOpen": "2025-07-19",
                            "status": "on-time",
                            "timestamp": "2025-07-19T13:21:43Z"
                        },
                        {
                            "filename": "predictions-ZYTkjGlZZOLS.csv",
                            "id": "1d13a6c2-3635-477a-ab40-c68537264dd3",
                            "roundCloseStaking": "2025-07-18",
                            "roundNumber": 1053,
                            "roundOpen": "2025-07-18",
                            "status": "on-time",
                            "timestamp": "2025-07-18T13:23:18Z"
                        },
                        {
                            "filename": "predictions-mhufr9xUYuBU.csv",
                            "id": "c393d377-3c6d-43b1-9609-03b2c88008fa",
                            "roundCloseStaking": "2025-07-17",
                            "roundNumber": 1052,
                            "roundOpen": "2025-07-17",
                            "status": "on-time",
                            "timestamp": "2025-07-17T13:29:59Z"
                        },
                        {
                            "filename": "predictions-mT6uuBfGT4nS.csv",
                            "id": "fdbe8b01-00ce-4e34-8bca-a9161b2d8592",
                            "roundCloseStaking": "2025-07-16",
                            "roundNumber": 1051,
                            "roundOpen": "2025-07-16",
                            "status": "on-time",
                            "timestamp": "2025-07-16T13:22:28Z"
                        },
                        {
                            "filename": "predictions-Q22Ky9bCajND.csv",
                            "id": "5d2e34a9-f3dd-49e8-b309-95529ceb81d7",
                            "roundCloseStaking": "2025-07-15",
                            "roundNumber": 1050,
                            "roundOpen": "2025-07-15",
                            "status": "on-time",
                            "timestamp": "2025-07-15T13:22:22Z"
                        },
                        {
                            "filename": "predictions-gPrOUnQBMhKr.csv",
                            "id": "5fbb7cb1-b9dc-496e-b671-e301ad403b7a",
                            "roundCloseStaking": "2025-07-14",
                            "roundNumber": 1049,
                            "roundOpen": "2025-07-12",
                            "status": "on-time",
                            "timestamp": "2025-07-12T13:34:46Z"
                        },
                        {
                            "filename": "predictions-XZkuhxhcEPwC.csv",
                            "id": "0d13a43b-7864-47dd-895d-54c634011826",
                            "roundCloseStaking": "2025-07-11",
                            "roundNumber": 1048,
                            "roundOpen": "2025-07-11",
                            "status": "on-time",
                            "timestamp": "2025-07-11T13:23:22Z"
                        },
                        {
                            "filename": "predictions-ALGX2bA0kiqa.csv",
                            "id": "f61e1599-377d-4918-843a-380940d042b3",
                            "roundCloseStaking": "2025-07-10",
                            "roundNumber": 1047,
                            "roundOpen": "2025-07-10",
                            "status": "on-time",
                            "timestamp": "2025-07-10T13:19:44Z"
                        },
                        {
                            "filename": "predictions-L4HqselITKm8.csv",
                            "id": "96136996-79dc-439e-b290-45685f1a5d52",
                            "roundCloseStaking": "2025-07-09",
                            "roundNumber": 1046,
                            "roundOpen": "2025-07-09",
                            "status": "on-time",
                            "timestamp": "2025-07-09T13:25:20Z"
                        },
                        {
                            "filename": "predictions-1Oecn43rFE0J.csv",
                            "id": "2617987f-f9f4-4431-9585-08bd12d59fd9",
                            "roundCloseStaking": "2025-07-08",
                            "roundNumber": 1045,
                            "roundOpen": "2025-07-08",
                            "status": "on-time",
                            "timestamp": "2025-07-08T14:12:20Z"
                        },
                        {
                            "filename": "predictions-YnjSzwfQBiE6.csv",
                            "id": "e069a325-f5b2-4d5b-957a-6bad98deac04",
                            "roundCloseStaking": "2025-07-07",
                            "roundNumber": 1044,
                            "roundOpen": "2025-07-05",
                            "status": "on-time",
                            "timestamp": "2025-07-05T14:15:23Z"
                        },
                        {
                            "filename": "predictions-fHTz1iCxKMwJ.csv",
                            "id": "9c8382c2-c078-46d5-9079-408e41b7b6ec",
                            "roundCloseStaking": "2025-07-04",
                            "roundNumber": 1043,
                            "roundOpen": "2025-07-04",
                            "status": "on-time",
                            "timestamp": "2025-07-04T13:31:42Z"
                        },
                        {
                            "filename": "predictions-uYNELP2vPIjJ.csv",
                            "id": "7a7aeec4-bcb5-455a-802a-d3fb7f9983ee",
                            "roundCloseStaking": "2025-07-03",
                            "roundNumber": 1042,
                            "roundOpen": "2025-07-03",
                            "status": "on-time",
                            "timestamp": "2025-07-03T13:48:45Z"
                        },
                        {
                            "filename": "predictions-7RxWr9gqIRkv.csv",
                            "id": "d0369a69-da0f-4aef-a44a-18ff2e26ce7a",
                            "roundCloseStaking": "2025-07-02",
                            "roundNumber": 1041,
                            "roundOpen": "2025-07-02",
                            "status": "on-time",
                            "timestamp": "2025-07-02T13:46:34Z"
                        },
                        {
                            "filename": "predictions-xGVhOf2pvbjS.csv",
                            "id": "20d47f01-ffed-4e5a-b0fa-69e22360220f",
                            "roundCloseStaking": "2025-07-01",
                            "roundNumber": 1040,
                            "roundOpen": "2025-07-01",
                            "status": "on-time",
                            "timestamp": "2025-07-01T13:55:32Z"
                        }
                    ],
                    "latestUserScores": [
                        {
                            "displayName": "apcwnm",
                            "reputation": 0.11552360924685026
                        },
                        {
                            "displayName": "bmc",
                            "reputation": -3.1351987106427144e-4
                        },
                        {
                            "displayName": "canon_bmc",
                            "reputation": -2.9309903655050666e-4
                        },
                        {
                            "displayName": "canon_corj60",
                            "reputation": 4.083340603788757e-4
                        },
                        {
                            "displayName": "canon_corr",
                            "reputation": 0.0014680500769631128
                        },
                        {
                            "displayName": "canon_corr60",
                            "reputation": 4.478318340429912e-4
                        },
                        {
                            "displayName": "canon_cort20",
                            "reputation": 0.00174749623899977
                        },
                        {
                            "displayName": "canon_fnc_v3",
                            "reputation": 0.0015991269079456728
                        },
                        {
                            "displayName": "canon_mmc",
                            "reputation": -0.0011358141641706616
                        },
                        {
                            "displayName": "canon_mmc60",
                            "reputation": -9.534555686615722e-4
                        },
                        {
                            "displayName": "corj60",
                            "reputation": 3.972980046929602e-4
                        },
                        {
                            "displayName": "corr60",
                            "reputation": 5.673985858505859e-4
                        },
                        {
                            "displayName": "corr_w_meta_model",
                            "reputation": 0.6725259508416114
                        },
                        {
                            "displayName": "cort20",
                            "reputation": 0.0018616184423630201
                        },
                        {
                            "displayName": "fnc_v3",
                            "reputation": 0.001703559685607431
                        },
                        {
                            "displayName": "mcwnm",
                            "reputation": 0.22795538138950605
                        },
                        {
                            "displayName": "mmc",
                            "reputation": -0.001209989783055276
                        },
                        {
                            "displayName": "mmc60",
                            "reputation": -0.00121391172400327
                        },
                        {
                            "displayName": "season_score",
                            "reputation": -0.0015376032980902263
                        },
                        {
                            "displayName": "v2_corr20",
                            "reputation": 0.0015639227350504998
                        }
                    ],
                    "name": "fnc_efficient",
                    "profileUrl": "https://numerai-public-images.s3-us-west-2.amazonaws.com/profile_images/lemmings1-OYgu8QUNS4Lz.jpg",
                    "returns": {
                        "allTime": -3.9783870453510004,
                        "oneDay": 0.10680094158448965,
                        "oneYear": null,
                        "threeMonths": null
                    },
                    "submissionWebhook": null,
                    "tournament": 8,
                    "v2Stake": {
                        "latestValue": "0.415993419090347700",
                        "latestValueSettled": "0.415993419090347700",
                        "pendingV2ChangeStakeRequest": null,
                        "stakeValue": "0.415601286869832309",
                        "status": null
                    }
                },
                {
                    "computeEnabled": true,
                    "computePickleUpload": null,
                    "currentPayoutSelection": {
                        "corrMultiplier": 0.5,
                        "mmcMultiplier": 2.0,
                        "takeProfit": false,
                        "updatedAt": null
                    },
                    "description": null,
                    "earliestReleaseDate": "2025-09-24T00:00:00Z",
                    "id": "994bab73-959b-4f63-8307-a6b74a020a9c",
                    "isComputeWeekdayEnabled": true,
                    "latestSubmissions": [
                        {
                            "filename": "deep_learning_predictions2-QezwyphQYcOq.csv",
                            "id": "b529fb7c-ec07-4d97-b9c7-eb9b97d1d211",
                            "roundCloseStaking": "2025-09-23",
                            "roundNumber": 1100,
                            "roundOpen": "2025-09-23",
                            "status": "on-time",
                            "timestamp": "2025-09-23T13:11:36Z"
                        },
                        {
                            "filename": "deep_learning_predictions2-h7pj0wgk743o.csv",
                            "id": "1a67a95d-8353-401c-9dff-dc31f4fe97ae",
                            "roundCloseStaking": "2025-09-22",
                            "roundNumber": 1099,
                            "roundOpen": "2025-09-20",
                            "status": "on-time",
                            "timestamp": "2025-09-21T11:44:17Z"
                        },
                        {
                            "filename": "deep_learning_predictions2-rHq2NMZodpaj.csv",
                            "id": "f86c6f3f-b707-4143-bb52-07b7a6b203d7",
                            "roundCloseStaking": "2025-09-19",
                            "roundNumber": 1098,
                            "roundOpen": "2025-09-19",
                            "status": "on-time",
                            "timestamp": "2025-09-19T13:07:08Z"
                        },
                        {
                            "filename": "deep_learning_predictions2-ycltoIYBBdT8.csv",
                            "id": "45357343-a356-4017-aa3a-709d244d897a",
                            "roundCloseStaking": "2025-09-18",
                            "roundNumber": 1097,
                            "roundOpen": "2025-09-18",
                            "status": "on-time",
                            "timestamp": "2025-09-18T13:07:25Z"
                        },
                        {
                            "filename": "deep_learning_predictions2-QEayOYooFiCi.csv",
                            "id": "2c756371-6fec-4d59-9f75-57d5e341285b",
                            "roundCloseStaking": "2025-09-17",
                            "roundNumber": 1096,
                            "roundOpen": "2025-09-17",
                            "status": "on-time",
                            "timestamp": "2025-09-17T13:09:21Z"
                        },
                        {
                            "filename": "deep_learning_predictions2-63DtdU6SFI0o.csv",
                            "id": "f4ade587-d69f-41ff-b6bd-109126de39ce",
                            "roundCloseStaking": "2025-09-16",
                            "roundNumber": 1095,
                            "roundOpen": "2025-09-16",
                            "status": "on-time",
                            "timestamp": "2025-09-16T13:07:12Z"
                        },
                        {
                            "filename": "deep_learning_predictions2-4eFllG0pb4WB.csv",
                            "id": "2ebbc874-9a5b-4815-ac4e-69a48fe34612",
                            "roundCloseStaking": "2025-09-15",
                            "roundNumber": 1094,
                            "roundOpen": "2025-09-13",
                            "status": "on-time",
                            "timestamp": "2025-09-13T13:07:43Z"
                        },
                        {
                            "filename": "deep_learning_predictions2-SvhCGjZAqF4V.csv",
                            "id": "9a57a15f-d0d3-4519-a1e1-0bc27a04f362",
                            "roundCloseStaking": "2025-09-12",
                            "roundNumber": 1093,
                            "roundOpen": "2025-09-12",
                            "status": "on-time",
                            "timestamp": "2025-09-12T13:07:18Z"
                        },
                        {
                            "filename": "deep_learning_predictions2-vqbis5sTs9ml.csv",
                            "id": "6d3c7d75-7486-401c-a4a6-bd47fc2a5330",
                            "roundCloseStaking": "2025-09-11",
                            "roundNumber": 1092,
                            "roundOpen": "2025-09-11",
                            "status": "on-time",
                            "timestamp": "2025-09-11T13:07:05Z"
                        },
                        {
                            "filename": "deep_learning_predictions2-eFLyCndz8Add.csv",
                            "id": "8c30f7da-cf21-4fac-a8e2-3af2028071b1",
                            "roundCloseStaking": "2025-09-10",
                            "roundNumber": 1091,
                            "roundOpen": "2025-09-10",
                            "status": "on-time",
                            "timestamp": "2025-09-10T13:07:19Z"
                        },
                        {
                            "filename": "deep_learning_predictions2-B4CwUeYl4D8l.csv",
                            "id": "81ae6ae1-a314-4b06-868e-c7580ff7c093",
                            "roundCloseStaking": "2025-09-09",
                            "roundNumber": 1090,
                            "roundOpen": "2025-09-09",
                            "status": "on-time",
                            "timestamp": "2025-09-09T13:08:03Z"
                        },
                        {
                            "filename": "deep_learning_predictions2-kyLwqGUz7k2Q.csv",
                            "id": "3ab346d1-bc98-4dfa-894b-8520072f2569",
                            "roundCloseStaking": "2025-09-08",
                            "roundNumber": 1089,
                            "roundOpen": "2025-09-06",
                            "status": "on-time",
                            "timestamp": "2025-09-06T13:05:04Z"
                        },
                        {
                            "filename": "deep_learning_predictions2-YGJnX10z2JJ1.csv",
                            "id": "c8e3f69d-8467-4e59-9f4f-6f60658c359b",
                            "roundCloseStaking": "2025-09-05",
                            "roundNumber": 1088,
                            "roundOpen": "2025-09-05",
                            "status": "on-time",
                            "timestamp": "2025-09-05T13:07:05Z"
                        },
                        {
                            "filename": "deep_learning_predictions2-8mXK3m8cSDAJ.csv",
                            "id": "0c3638d6-00d6-4ec0-9616-bc0fd6a6480a",
                            "roundCloseStaking": "2025-09-04",
                            "roundNumber": 1087,
                            "roundOpen": "2025-09-04",
                            "status": "on-time",
                            "timestamp": "2025-09-04T13:07:00Z"
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-03",
                            "roundNumber": 1086,
                            "roundOpen": "2025-09-03",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": "deep_learning_predictions2-ySRpXYesyWf7.csv",
                            "id": "c967f4be-54a2-49d8-9ac7-6804e84b2329",
                            "roundCloseStaking": "2025-09-02",
                            "roundNumber": 1085,
                            "roundOpen": "2025-09-02",
                            "status": "on-time",
                            "timestamp": "2025-09-02T13:17:54Z"
                        },
                        {
                            "filename": "deep_learning_predictions2-4zv8oNLcwbkV.csv",
                            "id": "e54a97bc-085b-4c36-a5c9-dad321b6cc14",
                            "roundCloseStaking": "2025-09-01",
                            "roundNumber": 1084,
                            "roundOpen": "2025-08-30",
                            "status": "on-time",
                            "timestamp": "2025-08-30T13:07:43Z"
                        },
                        {
                            "filename": "deep_learning_predictions2-itR05tsitFU4.csv",
                            "id": "a9f9f063-4af7-458c-858d-c7c0f9be37dc",
                            "roundCloseStaking": "2025-08-29",
                            "roundNumber": 1083,
                            "roundOpen": "2025-08-29",
                            "status": "on-time",
                            "timestamp": "2025-08-29T13:07:26Z"
                        },
                        {
                            "filename": "deep_learning_predictions2-Xu17wq1PrN2Z.csv",
                            "id": "0d06b077-30d2-4d1f-b921-bc3365c4b7f2",
                            "roundCloseStaking": "2025-08-28",
                            "roundNumber": 1082,
                            "roundOpen": "2025-08-28",
                            "status": "on-time",
                            "timestamp": "2025-08-28T13:09:30Z"
                        },
                        {
                            "filename": "deep_learning_predictions2-Tk9A9om9ZjRM.csv",
                            "id": "197f3c9e-7453-48e3-90ec-8db5ac9064fa",
                            "roundCloseStaking": "2025-08-27",
                            "roundNumber": 1081,
                            "roundOpen": "2025-08-27",
                            "status": "on-time",
                            "timestamp": "2025-08-27T13:07:50Z"
                        },
                        {
                            "filename": "deep_learning_predictions2-LEH3luT45TCB.csv",
                            "id": "48caaae3-a964-4696-9ab9-122ac4c2ee38",
                            "roundCloseStaking": "2025-08-26",
                            "roundNumber": 1080,
                            "roundOpen": "2025-08-26",
                            "status": "on-time",
                            "timestamp": "2025-08-26T13:08:03Z"
                        },
                        {
                            "filename": "deep_learning_predictions2-UpzhPbKN1CHp.csv",
                            "id": "41369292-6074-4a31-b12a-09a33cd22997",
                            "roundCloseStaking": "2025-08-25",
                            "roundNumber": 1079,
                            "roundOpen": "2025-08-23",
                            "status": "on-time",
                            "timestamp": "2025-08-23T13:07:02Z"
                        },
                        {
                            "filename": "deep_learning_predictions2-x0c9NOK7NBog.csv",
                            "id": "4306200f-4a2e-4fc8-91c9-4c32d1941123",
                            "roundCloseStaking": "2025-08-22",
                            "roundNumber": 1078,
                            "roundOpen": "2025-08-22",
                            "status": "on-time",
                            "timestamp": "2025-08-22T13:07:53Z"
                        },
                        {
                            "filename": "deep_learning_predictions2-Pi2izZ0gCyfi.csv",
                            "id": "221279c4-94a3-4868-b725-4f6fbbc87bf6",
                            "roundCloseStaking": "2025-08-21",
                            "roundNumber": 1077,
                            "roundOpen": "2025-08-21",
                            "status": "on-time",
                            "timestamp": "2025-08-21T13:07:28Z"
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-20",
                            "roundNumber": 1076,
                            "roundOpen": "2025-08-20",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": "deep_learning_predictions2-HF7PYl9lxGBp.csv",
                            "id": "15179a0d-448c-4cee-8798-fe530da1de94",
                            "roundCloseStaking": "2025-08-19",
                            "roundNumber": 1075,
                            "roundOpen": "2025-08-19",
                            "status": "on-time",
                            "timestamp": "2025-08-19T13:07:03Z"
                        },
                        {
                            "filename": "deep_learning_predictions2-VIOjJn8PLnt3.csv",
                            "id": "5d7ad013-f117-41af-b874-e8002e50a923",
                            "roundCloseStaking": "2025-08-18",
                            "roundNumber": 1074,
                            "roundOpen": "2025-08-16",
                            "status": "on-time",
                            "timestamp": "2025-08-16T13:05:46Z"
                        },
                        {
                            "filename": "deep_learning_predictions2-COmw5LH4zdlv.csv",
                            "id": "5a3300ca-2223-4f5c-8f39-aa5b3fac6324",
                            "roundCloseStaking": "2025-08-15",
                            "roundNumber": 1073,
                            "roundOpen": "2025-08-15",
                            "status": "on-time",
                            "timestamp": "2025-08-15T13:07:37Z"
                        },
                        {
                            "filename": "deep_learning_predictions2-KrR1wuWy3LVo.csv",
                            "id": "2a45c83f-eb01-4963-b0c1-8f07d5ad57cb",
                            "roundCloseStaking": "2025-08-14",
                            "roundNumber": 1072,
                            "roundOpen": "2025-08-14",
                            "status": "on-time",
                            "timestamp": "2025-08-14T13:08:04Z"
                        },
                        {
                            "filename": "deep_learning_predictions2-gS7xaBipQhQZ.csv",
                            "id": "0ae2215b-fc4c-4548-af50-b3ea30fc683e",
                            "roundCloseStaking": "2025-08-13",
                            "roundNumber": 1071,
                            "roundOpen": "2025-08-13",
                            "status": "on-time",
                            "timestamp": "2025-08-13T13:07:34Z"
                        },
                        {
                            "filename": "deep_learning_predictions2-b7VAgoWRgsfU.csv",
                            "id": "c9597ff7-c607-4780-b60f-e7cbf803b880",
                            "roundCloseStaking": "2025-08-12",
                            "roundNumber": 1070,
                            "roundOpen": "2025-08-12",
                            "status": "on-time",
                            "timestamp": "2025-08-12T13:07:26Z"
                        },
                        {
                            "filename": "deep_learning_predictions2-yuApLIWpKr0Q.csv",
                            "id": "456e002a-95cf-4863-b868-91e1076a6c89",
                            "roundCloseStaking": "2025-08-11",
                            "roundNumber": 1069,
                            "roundOpen": "2025-08-09",
                            "status": "on-time",
                            "timestamp": "2025-08-09T13:07:30Z"
                        },
                        {
                            "filename": "deep_learning_predictions2-yhArTvGBgFPn.csv",
                            "id": "1514cabd-daa1-457e-a438-7fefc09c19a3",
                            "roundCloseStaking": "2025-08-08",
                            "roundNumber": 1068,
                            "roundOpen": "2025-08-08",
                            "status": "on-time",
                            "timestamp": "2025-08-08T13:07:32Z"
                        },
                        {
                            "filename": "deep_learning_predictions2-Bto7HLQ3BanX.csv",
                            "id": "4e38384d-c58b-4240-ba61-ec211deb6bc6",
                            "roundCloseStaking": "2025-08-07",
                            "roundNumber": 1067,
                            "roundOpen": "2025-08-07",
                            "status": "on-time",
                            "timestamp": "2025-08-07T13:11:23Z"
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-06",
                            "roundNumber": 1066,
                            "roundOpen": "2025-08-06",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": "deep_learning_predictions2-eMBVas8IA72x.csv",
                            "id": "21cc1827-ae35-4f90-88ce-db2696564824",
                            "roundCloseStaking": "2025-08-05",
                            "roundNumber": 1065,
                            "roundOpen": "2025-08-05",
                            "status": "on-time",
                            "timestamp": "2025-08-05T13:07:08Z"
                        },
                        {
                            "filename": "deep_learning_predictions2-7gkCCqn48vII.csv",
                            "id": "6758f413-fa6b-4ce8-a539-723a354e7461",
                            "roundCloseStaking": "2025-08-04",
                            "roundNumber": 1064,
                            "roundOpen": "2025-08-02",
                            "status": "on-time",
                            "timestamp": "2025-08-02T13:18:20Z"
                        },
                        {
                            "filename": "deep_learning_predictions2-RDJM1UALwqQO.csv",
                            "id": "11aaadb0-3a67-49f5-97ae-5d31d9196252",
                            "roundCloseStaking": "2025-08-01",
                            "roundNumber": 1063,
                            "roundOpen": "2025-08-01",
                            "status": "on-time",
                            "timestamp": "2025-08-01T13:07:44Z"
                        },
                        {
                            "filename": "deep_learning_predictions2-rCn7Hl8wnpIe.csv",
                            "id": "d9098932-4d8c-4045-a8c9-07def426a5a9",
                            "roundCloseStaking": "2025-07-31",
                            "roundNumber": 1062,
                            "roundOpen": "2025-07-31",
                            "status": "on-time",
                            "timestamp": "2025-07-31T13:07:21Z"
                        },
                        {
                            "filename": "deep_learning_predictions2-aiCJuT2mnZhf.csv",
                            "id": "193f252b-bcab-4e5a-af4c-ae9ce10052fb",
                            "roundCloseStaking": "2025-07-30",
                            "roundNumber": 1061,
                            "roundOpen": "2025-07-30",
                            "status": "on-time",
                            "timestamp": "2025-07-30T13:08:03Z"
                        },
                        {
                            "filename": "deep_learning_predictions2-KLturTxYq8ef.csv",
                            "id": "95793538-3b9f-40e3-b12b-4996e674b9ae",
                            "roundCloseStaking": "2025-07-29",
                            "roundNumber": 1060,
                            "roundOpen": "2025-07-29",
                            "status": "on-time",
                            "timestamp": "2025-07-29T13:07:48Z"
                        },
                        {
                            "filename": "deep_learning_predictions2-kKRmdLhzf9Mk.csv",
                            "id": "0851c638-bb29-4215-bd67-1c58fff392b7",
                            "roundCloseStaking": "2025-07-28",
                            "roundNumber": 1059,
                            "roundOpen": "2025-07-26",
                            "status": "on-time",
                            "timestamp": "2025-07-26T13:07:58Z"
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-25",
                            "roundNumber": 1058,
                            "roundOpen": "2025-07-25",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": "deep_learning_predictions2-MLL4n3bqb9YN.csv",
                            "id": "3a0a1d6b-49d3-4886-914c-04f1fc72146b",
                            "roundCloseStaking": "2025-07-24",
                            "roundNumber": 1057,
                            "roundOpen": "2025-07-24",
                            "status": "on-time",
                            "timestamp": "2025-07-24T13:07:18Z"
                        },
                        {
                            "filename": "deep_learning_predictions2-0KCqrU00Q1bl.csv",
                            "id": "81fa88de-02ec-4f0f-8cb4-ce4b2d4462aa",
                            "roundCloseStaking": "2025-07-23",
                            "roundNumber": 1056,
                            "roundOpen": "2025-07-23",
                            "status": "on-time",
                            "timestamp": "2025-07-23T13:08:05Z"
                        },
                        {
                            "filename": "deep_learning_predictions2-2T4lpexfYRj1.csv",
                            "id": "0cb38ee1-0aff-4212-b5a9-59992edd41be",
                            "roundCloseStaking": "2025-07-22",
                            "roundNumber": 1055,
                            "roundOpen": "2025-07-22",
                            "status": "on-time",
                            "timestamp": "2025-07-22T13:10:35Z"
                        },
                        {
                            "filename": "deep_learning_predictions2-OfO2DhZlmpaG.csv",
                            "id": "8ddbab05-727c-49b9-aedc-b84f9992d44e",
                            "roundCloseStaking": "2025-07-21",
                            "roundNumber": 1054,
                            "roundOpen": "2025-07-19",
                            "status": "on-time",
                            "timestamp": "2025-07-19T13:07:18Z"
                        },
                        {
                            "filename": "deep_learning_predictions2-Ll23gfqrybfS.csv",
                            "id": "a788f48a-972e-43d1-b9fb-2eb33dcb0edd",
                            "roundCloseStaking": "2025-07-18",
                            "roundNumber": 1053,
                            "roundOpen": "2025-07-18",
                            "status": "on-time",
                            "timestamp": "2025-07-18T13:07:25Z"
                        },
                        {
                            "filename": "deep_learning_predictions2-RAgr8uqCFyd7.csv",
                            "id": "32a6e3af-ff26-48a2-94ad-489c9362d78a",
                            "roundCloseStaking": "2025-07-17",
                            "roundNumber": 1052,
                            "roundOpen": "2025-07-17",
                            "status": "on-time",
                            "timestamp": "2025-07-17T13:14:32Z"
                        },
                        {
                            "filename": "deep_learning_predictions2-9MHkb34upbJE.csv",
                            "id": "774703b4-e150-489e-85f4-169d3bc66974",
                            "roundCloseStaking": "2025-07-16",
                            "roundNumber": 1051,
                            "roundOpen": "2025-07-16",
                            "status": "late",
                            "timestamp": "2025-07-17T11:19:31Z"
                        },
                        {
                            "filename": "deep_learning_predictions2-2jCGT2Kr5w8x.csv",
                            "id": "fefc8718-f690-4c58-903f-4ee798627e41",
                            "roundCloseStaking": "2025-07-15",
                            "roundNumber": 1050,
                            "roundOpen": "2025-07-15",
                            "status": "on-time",
                            "timestamp": "2025-07-15T13:05:11Z"
                        },
                        {
                            "filename": "deep_learning_predictions2-ra0VbxxOI3Lg.csv",
                            "id": "473df4c8-8396-4245-aad3-5caedae788c1",
                            "roundCloseStaking": "2025-07-14",
                            "roundNumber": 1049,
                            "roundOpen": "2025-07-12",
                            "status": "on-time",
                            "timestamp": "2025-07-13T07:10:11Z"
                        },
                        {
                            "filename": "deep_learning_predictions2-9gzBdWToHrjn.csv",
                            "id": "7b3b19c7-3e53-4c18-86b5-8a5d3ecda65d",
                            "roundCloseStaking": "2025-07-11",
                            "roundNumber": 1048,
                            "roundOpen": "2025-07-11",
                            "status": "on-time",
                            "timestamp": "2025-07-11T13:05:27Z"
                        },
                        {
                            "filename": "deep_learning_predictions2-vnPK1awuqPJS.csv",
                            "id": "cd7f94eb-3519-4088-b812-0758c7e003b9",
                            "roundCloseStaking": "2025-07-10",
                            "roundNumber": 1047,
                            "roundOpen": "2025-07-10",
                            "status": "late",
                            "timestamp": "2025-07-10T18:57:31Z"
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-09",
                            "roundNumber": 1046,
                            "roundOpen": "2025-07-09",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-08",
                            "roundNumber": 1045,
                            "roundOpen": "2025-07-08",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": "deep_learning_predictions2-1UFlyl7i6Gf3.csv",
                            "id": "bf8c62b0-cfc9-4d72-9a77-551d49137ea8",
                            "roundCloseStaking": "2025-07-07",
                            "roundNumber": 1044,
                            "roundOpen": "2025-07-05",
                            "status": "on-time",
                            "timestamp": "2025-07-05T13:52:36Z"
                        },
                        {
                            "filename": "deep_learning_predictions2-1UFlyl7i6Gf3.csv",
                            "id": "95a8f39f-f9c9-4816-b383-eec292b8cf41",
                            "roundCloseStaking": "2025-07-04",
                            "roundNumber": 1043,
                            "roundOpen": "2025-07-04",
                            "status": "late",
                            "timestamp": "2025-07-05T12:52:29Z"
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-03",
                            "roundNumber": 1042,
                            "roundOpen": "2025-07-03",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-02",
                            "roundNumber": 1041,
                            "roundOpen": "2025-07-02",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-01",
                            "roundNumber": 1040,
                            "roundOpen": "2025-07-01",
                            "status": "none",
                            "timestamp": null
                        }
                    ],
                    "latestUserScores": [
                        {
                            "displayName": "apcwnm",
                            "reputation": -0.003288294716852916
                        },
                        {
                            "displayName": "bmc",
                            "reputation": -0.0015375674753847425
                        },
                        {
                            "displayName": "canon_bmc",
                            "reputation": -0.0014374194022753915
                        },
                        {
                            "displayName": "canon_corr",
                            "reputation": -0.0019156735537826917
                        },
                        {
                            "displayName": "canon_cort20",
                            "reputation": -5.366241160861624e-4
                        },
                        {
                            "displayName": "canon_fnc_v3",
                            "reputation": -3.5289410960759673e-4
                        },
                        {
                            "displayName": "canon_mmc",
                            "reputation": -0.0014309613296875378
                        },
                        {
                            "displayName": "corr_w_meta_model",
                            "reputation": -0.03867162153187554
                        },
                        {
                            "displayName": "cort20",
                            "reputation": -5.716689563203607e-4
                        },
                        {
                            "displayName": "fnc_v3",
                            "reputation": -3.7594025554115406e-4
                        },
                        {
                            "displayName": "mcwnm",
                            "reputation": 0.036923525965191384
                        },
                        {
                            "displayName": "mmc",
                            "reputation": -0.001524411865503867
                        },
                        {
                            "displayName": "season_score",
                            "reputation": -0.0038197594362664217
                        },
                        {
                            "displayName": "v2_corr20",
                            "reputation": -0.002040778765458296
                        }
                    ],
                    "name": "fnc_dl2_994b",
                    "profileUrl": "https://numerai-public-images.s3-us-west-2.amazonaws.com/profile_images/lemmings2-ImRmaP4Hnrzr.jpg",
                    "returns": null,
                    "submissionWebhook": "https://numerai.imperialai.ai/numerai-994bab73-959b-4f63-8307-a6b74a020a9c/",
                    "tournament": 8,
                    "v2Stake": {
                        "latestValue": "0.000000000000000000",
                        "latestValueSettled": "0.000000000000000000",
                        "pendingV2ChangeStakeRequest": null,
                        "stakeValue": null,
                        "status": null
                    }
                },
                {
                    "computeEnabled": false,
                    "computePickleUpload": {
                        "id": "f9393bb8-9dce-44d1-be87-362231b240c4"
                    },
                    "currentPayoutSelection": {
                        "corrMultiplier": 0.5,
                        "mmcMultiplier": 2.0,
                        "takeProfit": false,
                        "updatedAt": null
                    },
                    "description": null,
                    "earliestReleaseDate": "2025-10-24T00:00:00Z",
                    "id": "d43fcf06-e036-4f71-93e4-04a973846ba8",
                    "isComputeWeekdayEnabled": true,
                    "latestSubmissions": [
                        {
                            "filename": "predictions-TJr31a8gdhRo.csv",
                            "id": "5201bb0c-5c0f-400f-8591-0cbec6358de1",
                            "roundCloseStaking": "2025-09-23",
                            "roundNumber": 1100,
                            "roundOpen": "2025-09-23",
                            "status": "on-time",
                            "timestamp": "2025-09-23T13:34:08Z"
                        },
                        {
                            "filename": "predictions-jTMl4FSC4Jyr.csv",
                            "id": "2aac01d3-ea24-4be1-a843-268cf547210a",
                            "roundCloseStaking": "2025-09-22",
                            "roundNumber": 1099,
                            "roundOpen": "2025-09-20",
                            "status": "on-time",
                            "timestamp": "2025-09-20T13:32:40Z"
                        },
                        {
                            "filename": "predictions-eQcPf6rbnfQK.csv",
                            "id": "2d9471c9-dde4-410b-b05c-0394bca77d5c",
                            "roundCloseStaking": "2025-09-19",
                            "roundNumber": 1098,
                            "roundOpen": "2025-09-19",
                            "status": "on-time",
                            "timestamp": "2025-09-19T13:31:10Z"
                        },
                        {
                            "filename": "predictions-EW9taxfw25sy.csv",
                            "id": "d690b154-53b5-4612-baef-18ba82150993",
                            "roundCloseStaking": "2025-09-18",
                            "roundNumber": 1097,
                            "roundOpen": "2025-09-18",
                            "status": "on-time",
                            "timestamp": "2025-09-18T13:32:06Z"
                        },
                        {
                            "filename": "predictions-tTWfoQvI4Lq6.csv",
                            "id": "a16ca260-82c7-4e6e-8df4-df34c1332ed9",
                            "roundCloseStaking": "2025-09-17",
                            "roundNumber": 1096,
                            "roundOpen": "2025-09-17",
                            "status": "on-time",
                            "timestamp": "2025-09-17T13:30:36Z"
                        },
                        {
                            "filename": "predictions-tk4DdKb2MUc5.csv",
                            "id": "70af429e-b95f-4cd4-9138-e822fd12bab2",
                            "roundCloseStaking": "2025-09-16",
                            "roundNumber": 1095,
                            "roundOpen": "2025-09-16",
                            "status": "on-time",
                            "timestamp": "2025-09-16T13:29:10Z"
                        },
                        {
                            "filename": "predictions-nGLcNStRFhp9.csv",
                            "id": "d22afa0b-54fa-4592-908f-37b94e03b6f0",
                            "roundCloseStaking": "2025-09-15",
                            "roundNumber": 1094,
                            "roundOpen": "2025-09-13",
                            "status": "on-time",
                            "timestamp": "2025-09-13T13:29:17Z"
                        },
                        {
                            "filename": "predictions-6YF6i42C6qW8.csv",
                            "id": "0e1c2dcd-0fc4-4aa8-bf42-35e8ef2c0e38",
                            "roundCloseStaking": "2025-09-12",
                            "roundNumber": 1093,
                            "roundOpen": "2025-09-12",
                            "status": "on-time",
                            "timestamp": "2025-09-12T13:26:28Z"
                        },
                        {
                            "filename": "predictions-l3sC0Ab1JVwm.csv",
                            "id": "5a6750c7-f726-4f72-a793-810399f517b4",
                            "roundCloseStaking": "2025-09-11",
                            "roundNumber": 1092,
                            "roundOpen": "2025-09-11",
                            "status": "on-time",
                            "timestamp": "2025-09-11T13:27:54Z"
                        },
                        {
                            "filename": "predictions-9d56nextDnyk.csv",
                            "id": "0570c1a8-cf46-4e53-b4d3-d8f0198164f8",
                            "roundCloseStaking": "2025-09-10",
                            "roundNumber": 1091,
                            "roundOpen": "2025-09-10",
                            "status": "on-time",
                            "timestamp": "2025-09-10T13:30:54Z"
                        },
                        {
                            "filename": "predictions-P8SX66aPn3Fm.csv",
                            "id": "6fd3028b-b69a-4f4a-a10f-d90aa45364f5",
                            "roundCloseStaking": "2025-09-09",
                            "roundNumber": 1090,
                            "roundOpen": "2025-09-09",
                            "status": "on-time",
                            "timestamp": "2025-09-09T13:33:17Z"
                        },
                        {
                            "filename": "predictions-6BUgCiH8BZAf.csv",
                            "id": "3a326984-f454-40ec-b4c0-65c8907e8d89",
                            "roundCloseStaking": "2025-09-08",
                            "roundNumber": 1089,
                            "roundOpen": "2025-09-06",
                            "status": "on-time",
                            "timestamp": "2025-09-06T13:28:14Z"
                        },
                        {
                            "filename": "predictions-iQMZN1mCzbxR.csv",
                            "id": "58b3fd35-7a25-4b4f-93ec-8a5e0be9157b",
                            "roundCloseStaking": "2025-09-05",
                            "roundNumber": 1088,
                            "roundOpen": "2025-09-05",
                            "status": "on-time",
                            "timestamp": "2025-09-05T13:28:59Z"
                        },
                        {
                            "filename": "predictions-YRaD3mK3bzjL.csv",
                            "id": "ad6bd38e-f0bd-450e-a00c-77f3c4b7f443",
                            "roundCloseStaking": "2025-09-04",
                            "roundNumber": 1087,
                            "roundOpen": "2025-09-04",
                            "status": "on-time",
                            "timestamp": "2025-09-04T13:22:58Z"
                        },
                        {
                            "filename": "predictions-rY9n60e7LGJL.csv",
                            "id": "76c6d104-6d4c-4297-80e2-ccd83fcb401d",
                            "roundCloseStaking": "2025-09-03",
                            "roundNumber": 1086,
                            "roundOpen": "2025-09-03",
                            "status": "on-time",
                            "timestamp": "2025-09-03T13:32:48Z"
                        },
                        {
                            "filename": "predictions-cIBjvV7lhozN.csv",
                            "id": "a93c6c3c-061e-4dd2-a9b8-8240005a560a",
                            "roundCloseStaking": "2025-09-02",
                            "roundNumber": 1085,
                            "roundOpen": "2025-09-02",
                            "status": "on-time",
                            "timestamp": "2025-09-02T13:43:40Z"
                        },
                        {
                            "filename": "predictions-CXXArRmkLSHF.csv",
                            "id": "7a276a4a-9d0d-4af3-9060-72881def3ba2",
                            "roundCloseStaking": "2025-09-01",
                            "roundNumber": 1084,
                            "roundOpen": "2025-08-30",
                            "status": "on-time",
                            "timestamp": "2025-08-30T13:29:08Z"
                        },
                        {
                            "filename": "predictions-6UqbK1qPfuQM.csv",
                            "id": "06611a3f-333d-4cf3-8d04-ff0cb3e67bcb",
                            "roundCloseStaking": "2025-08-29",
                            "roundNumber": 1083,
                            "roundOpen": "2025-08-29",
                            "status": "on-time",
                            "timestamp": "2025-08-29T13:28:55Z"
                        },
                        {
                            "filename": "predictions-qwEWu8ppjrGL.csv",
                            "id": "22f20aff-1e7d-4a61-9f77-26a1fd89a7c6",
                            "roundCloseStaking": "2025-08-28",
                            "roundNumber": 1082,
                            "roundOpen": "2025-08-28",
                            "status": "on-time",
                            "timestamp": "2025-08-28T13:34:06Z"
                        },
                        {
                            "filename": "predictions-PTxIKoQ5ehB6.csv",
                            "id": "f8c77a19-2e2f-4299-90ff-4b5496495a7c",
                            "roundCloseStaking": "2025-08-27",
                            "roundNumber": 1081,
                            "roundOpen": "2025-08-27",
                            "status": "on-time",
                            "timestamp": "2025-08-27T13:30:28Z"
                        },
                        {
                            "filename": "predictions-5enuJiokUj7d.csv",
                            "id": "e953908b-df82-468d-a770-cee56b93d961",
                            "roundCloseStaking": "2025-08-26",
                            "roundNumber": 1080,
                            "roundOpen": "2025-08-26",
                            "status": "on-time",
                            "timestamp": "2025-08-26T13:30:13Z"
                        },
                        {
                            "filename": "predictions-XtfkahGOTCBo.csv",
                            "id": "bbb30789-353e-4d58-b0da-0efc6167836a",
                            "roundCloseStaking": "2025-08-25",
                            "roundNumber": 1079,
                            "roundOpen": "2025-08-23",
                            "status": "on-time",
                            "timestamp": "2025-08-23T13:34:00Z"
                        },
                        {
                            "filename": "predictions-VYI6Wt3dCBBF.csv",
                            "id": "e4d41399-23ee-4c0d-9411-a3e8fb681b7a",
                            "roundCloseStaking": "2025-08-22",
                            "roundNumber": 1078,
                            "roundOpen": "2025-08-22",
                            "status": "on-time",
                            "timestamp": "2025-08-22T13:27:10Z"
                        },
                        {
                            "filename": "predictions-Vdzq4QtDcQcE.csv",
                            "id": "7ee339db-4d4a-4dea-a537-f24d59ac3b84",
                            "roundCloseStaking": "2025-08-21",
                            "roundNumber": 1077,
                            "roundOpen": "2025-08-21",
                            "status": "on-time",
                            "timestamp": "2025-08-21T13:28:13Z"
                        },
                        {
                            "filename": "predictions-LP4EwyhdMLky.csv",
                            "id": "fbb390ac-02ba-4569-89ed-d1c88266145a",
                            "roundCloseStaking": "2025-08-20",
                            "roundNumber": 1076,
                            "roundOpen": "2025-08-20",
                            "status": "on-time",
                            "timestamp": "2025-08-20T13:29:13Z"
                        },
                        {
                            "filename": "predictions-Kpj9uOIt2tqt.csv",
                            "id": "d47c4b9a-1f39-4130-abca-104c7190e1a7",
                            "roundCloseStaking": "2025-08-19",
                            "roundNumber": 1075,
                            "roundOpen": "2025-08-19",
                            "status": "on-time",
                            "timestamp": "2025-08-19T13:30:58Z"
                        },
                        {
                            "filename": "predictions-OUTFC0OYHXfD.csv",
                            "id": "1dde339b-709c-4b06-adb9-9d7492c181d9",
                            "roundCloseStaking": "2025-08-18",
                            "roundNumber": 1074,
                            "roundOpen": "2025-08-16",
                            "status": "on-time",
                            "timestamp": "2025-08-16T13:28:45Z"
                        },
                        {
                            "filename": "predictions-C0Doos80pTOH.csv",
                            "id": "5c9a2ea4-3661-4197-821f-1602d035daf2",
                            "roundCloseStaking": "2025-08-15",
                            "roundNumber": 1073,
                            "roundOpen": "2025-08-15",
                            "status": "on-time",
                            "timestamp": "2025-08-15T13:36:45Z"
                        },
                        {
                            "filename": "predictions-b6Zgs0rO8Xih.csv",
                            "id": "e79003a9-4bb4-4b3f-8f4e-140f407a03b1",
                            "roundCloseStaking": "2025-08-14",
                            "roundNumber": 1072,
                            "roundOpen": "2025-08-14",
                            "status": "on-time",
                            "timestamp": "2025-08-14T13:25:55Z"
                        },
                        {
                            "filename": "predictions-XW23sbWg8oLR.csv",
                            "id": "438a461a-0d35-44d9-9b14-4f9d667f51c4",
                            "roundCloseStaking": "2025-08-13",
                            "roundNumber": 1071,
                            "roundOpen": "2025-08-13",
                            "status": "on-time",
                            "timestamp": "2025-08-13T13:29:53Z"
                        },
                        {
                            "filename": "predictions-5p0qZLZ7MLyU.csv",
                            "id": "fa42d2da-d606-4b26-bff5-3f2c4dcfc465",
                            "roundCloseStaking": "2025-08-12",
                            "roundNumber": 1070,
                            "roundOpen": "2025-08-12",
                            "status": "on-time",
                            "timestamp": "2025-08-12T13:27:44Z"
                        },
                        {
                            "filename": "predictions-4aXjiYYK5YNL.csv",
                            "id": "fb878b41-26b1-4599-bebe-502bc9d06709",
                            "roundCloseStaking": "2025-08-11",
                            "roundNumber": 1069,
                            "roundOpen": "2025-08-09",
                            "status": "on-time",
                            "timestamp": "2025-08-09T13:33:44Z"
                        },
                        {
                            "filename": "predictions-JvuN0Hd8HtfR.csv",
                            "id": "fc221bff-a15d-4b7d-9f9d-7f5cba9e258f",
                            "roundCloseStaking": "2025-08-08",
                            "roundNumber": 1068,
                            "roundOpen": "2025-08-08",
                            "status": "on-time",
                            "timestamp": "2025-08-08T13:32:04Z"
                        },
                        {
                            "filename": "predictions-5w3dMCt7Z3n1.csv",
                            "id": "a6b43c42-99d0-4bf5-a589-93a9c14f6c90",
                            "roundCloseStaking": "2025-08-07",
                            "roundNumber": 1067,
                            "roundOpen": "2025-08-07",
                            "status": "on-time",
                            "timestamp": "2025-08-07T13:35:19Z"
                        },
                        {
                            "filename": "predictions-AkuhpLrNUgfX.csv",
                            "id": "6a2d8a92-af22-470b-9c10-75612c44f6ec",
                            "roundCloseStaking": "2025-08-06",
                            "roundNumber": 1066,
                            "roundOpen": "2025-08-06",
                            "status": "on-time",
                            "timestamp": "2025-08-06T13:30:04Z"
                        },
                        {
                            "filename": "predictions-H9TbSoiQW3CA.csv",
                            "id": "2d1def63-32cf-4539-8c07-37a5c8f7c62d",
                            "roundCloseStaking": "2025-08-05",
                            "roundNumber": 1065,
                            "roundOpen": "2025-08-05",
                            "status": "on-time",
                            "timestamp": "2025-08-05T13:31:17Z"
                        },
                        {
                            "filename": "predictions-yVhA7bwVXxL2.csv",
                            "id": "fb295b52-5304-4065-bcef-2c5b4efd21dc",
                            "roundCloseStaking": "2025-08-04",
                            "roundNumber": 1064,
                            "roundOpen": "2025-08-02",
                            "status": "on-time",
                            "timestamp": "2025-08-02T13:37:31Z"
                        },
                        {
                            "filename": "predictions-ldaTzScPYxUP.csv",
                            "id": "d47fa365-0b30-4aaa-b4c8-81fbc90b5e4b",
                            "roundCloseStaking": "2025-08-01",
                            "roundNumber": 1063,
                            "roundOpen": "2025-08-01",
                            "status": "on-time",
                            "timestamp": "2025-08-01T13:27:01Z"
                        },
                        {
                            "filename": "predictions-OtEDD1ehxeSE.csv",
                            "id": "f113d7e9-2649-4725-8e34-40e8f08e10ab",
                            "roundCloseStaking": "2025-07-31",
                            "roundNumber": 1062,
                            "roundOpen": "2025-07-31",
                            "status": "on-time",
                            "timestamp": "2025-07-31T13:24:16Z"
                        },
                        {
                            "filename": "predictions-ELmLt0j1D3dW.csv",
                            "id": "5e8adc71-cff6-4428-8503-06afeeba8d04",
                            "roundCloseStaking": "2025-07-30",
                            "roundNumber": 1061,
                            "roundOpen": "2025-07-30",
                            "status": "on-time",
                            "timestamp": "2025-07-30T13:28:02Z"
                        },
                        {
                            "filename": "predictions-7l0HDhKCxSwf.csv",
                            "id": "7645818e-4ddb-4653-ac40-4715dcb12f52",
                            "roundCloseStaking": "2025-07-29",
                            "roundNumber": 1060,
                            "roundOpen": "2025-07-29",
                            "status": "on-time",
                            "timestamp": "2025-07-29T13:22:58Z"
                        },
                        {
                            "filename": "predictions-eepdEpRIlqSV.csv",
                            "id": "b771c49f-778d-4b51-800e-7b9ebbc6a890",
                            "roundCloseStaking": "2025-07-28",
                            "roundNumber": 1059,
                            "roundOpen": "2025-07-26",
                            "status": "on-time",
                            "timestamp": "2025-07-26T13:23:35Z"
                        },
                        {
                            "filename": "predictions-rdXL6B9qcNmm.csv",
                            "id": "4e836399-a4e3-44ce-8c95-79cbe2294941",
                            "roundCloseStaking": "2025-07-25",
                            "roundNumber": 1058,
                            "roundOpen": "2025-07-25",
                            "status": "on-time",
                            "timestamp": "2025-07-25T13:26:34Z"
                        },
                        {
                            "filename": "predictions-cdnsXQypRuoA.csv",
                            "id": "03f434b9-b654-4156-acd8-6b3648447636",
                            "roundCloseStaking": "2025-07-24",
                            "roundNumber": 1057,
                            "roundOpen": "2025-07-24",
                            "status": "on-time",
                            "timestamp": "2025-07-24T13:26:11Z"
                        },
                        {
                            "filename": "predictions-IaH7N6n3mb2r.csv",
                            "id": "17a281c5-676a-4ea3-acec-d52181f1db24",
                            "roundCloseStaking": "2025-07-23",
                            "roundNumber": 1056,
                            "roundOpen": "2025-07-23",
                            "status": "on-time",
                            "timestamp": "2025-07-23T13:26:25Z"
                        },
                        {
                            "filename": "predictions-olRXHzrgBMLi.csv",
                            "id": "b364ffff-08fb-4c2c-874b-f4ac427505b0",
                            "roundCloseStaking": "2025-07-22",
                            "roundNumber": 1055,
                            "roundOpen": "2025-07-22",
                            "status": "on-time",
                            "timestamp": "2025-07-22T13:28:48Z"
                        },
                        {
                            "filename": "predictions-eUEibAX004xf.csv",
                            "id": "d7d5697e-dc20-4f2d-8850-cfcbcff72ad8",
                            "roundCloseStaking": "2025-07-21",
                            "roundNumber": 1054,
                            "roundOpen": "2025-07-19",
                            "status": "on-time",
                            "timestamp": "2025-07-19T13:24:59Z"
                        },
                        {
                            "filename": "predictions-2wSFzzTF1YAN.csv",
                            "id": "ba590cd2-da2e-4ded-977f-86b0ebb5644f",
                            "roundCloseStaking": "2025-07-18",
                            "roundNumber": 1053,
                            "roundOpen": "2025-07-18",
                            "status": "on-time",
                            "timestamp": "2025-07-18T13:28:17Z"
                        },
                        {
                            "filename": "predictions-SVaLQkjWwVNp.csv",
                            "id": "195c83a2-00e2-4543-99f5-51ff4c2db939",
                            "roundCloseStaking": "2025-07-17",
                            "roundNumber": 1052,
                            "roundOpen": "2025-07-17",
                            "status": "on-time",
                            "timestamp": "2025-07-17T13:33:46Z"
                        },
                        {
                            "filename": "predictions-plOw60zT2dxS.csv",
                            "id": "9539fe90-cb6b-47b4-8f24-6641f6a0480b",
                            "roundCloseStaking": "2025-07-16",
                            "roundNumber": 1051,
                            "roundOpen": "2025-07-16",
                            "status": "on-time",
                            "timestamp": "2025-07-16T13:30:07Z"
                        },
                        {
                            "filename": "predictions-hpZ2tY953zLT.csv",
                            "id": "66aa166f-b293-4550-90d2-99a3c8a4ad1a",
                            "roundCloseStaking": "2025-07-15",
                            "roundNumber": 1050,
                            "roundOpen": "2025-07-15",
                            "status": "on-time",
                            "timestamp": "2025-07-15T13:27:34Z"
                        },
                        {
                            "filename": "predictions-e4nv9nG9bV8w.csv",
                            "id": "ad381b51-f98a-433a-9cd3-f29aa7410a39",
                            "roundCloseStaking": "2025-07-14",
                            "roundNumber": 1049,
                            "roundOpen": "2025-07-12",
                            "status": "on-time",
                            "timestamp": "2025-07-12T13:35:37Z"
                        },
                        {
                            "filename": "predictions-YQqUXJJvrSnc.csv",
                            "id": "eb3aa925-c409-42b9-acd5-04cee5c97e02",
                            "roundCloseStaking": "2025-07-11",
                            "roundNumber": 1048,
                            "roundOpen": "2025-07-11",
                            "status": "on-time",
                            "timestamp": "2025-07-11T13:26:42Z"
                        },
                        {
                            "filename": "predictions-I8HfMaZgbvr5.csv",
                            "id": "bb673700-2f1e-45eb-acc3-897bd20e8700",
                            "roundCloseStaking": "2025-07-10",
                            "roundNumber": 1047,
                            "roundOpen": "2025-07-10",
                            "status": "on-time",
                            "timestamp": "2025-07-10T13:27:18Z"
                        },
                        {
                            "filename": "predictions-sA2hZP4DSZam.csv",
                            "id": "e96674c7-c6e1-4a45-af79-6120d2f836f2",
                            "roundCloseStaking": "2025-07-09",
                            "roundNumber": 1046,
                            "roundOpen": "2025-07-09",
                            "status": "on-time",
                            "timestamp": "2025-07-09T13:21:30Z"
                        },
                        {
                            "filename": "predictions-rWzeUhjOvbVa.csv",
                            "id": "241ac1f4-0bec-47cf-b53b-2fed88d33cb1",
                            "roundCloseStaking": "2025-07-08",
                            "roundNumber": 1045,
                            "roundOpen": "2025-07-08",
                            "status": "late",
                            "timestamp": "2025-07-08T20:26:15Z"
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-07",
                            "roundNumber": 1044,
                            "roundOpen": "2025-07-05",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-04",
                            "roundNumber": 1043,
                            "roundOpen": "2025-07-04",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": "gpu_enhanced_predictions-g6KfpXtUiHUm.csv",
                            "id": "4a2f22b7-fcab-4493-8aa3-6fe2c9c996f7",
                            "roundCloseStaking": "2025-07-03",
                            "roundNumber": 1042,
                            "roundOpen": "2025-07-03",
                            "status": "on-time",
                            "timestamp": "2025-07-03T13:36:35Z"
                        },
                        {
                            "filename": "gpu_enhanced_predictions-jW41l02FwuKd.csv",
                            "id": "16faff2b-f821-488e-aebf-abe02695aa58",
                            "roundCloseStaking": "2025-07-02",
                            "roundNumber": 1041,
                            "roundOpen": "2025-07-02",
                            "status": "on-time",
                            "timestamp": "2025-07-02T13:29:15Z"
                        },
                        {
                            "filename": "gpu_enhanced_predictions-4gtq7pdBnWdy.csv",
                            "id": "38cc01e8-2253-42c2-95b8-0505814b01b2",
                            "roundCloseStaking": "2025-07-01",
                            "roundNumber": 1040,
                            "roundOpen": "2025-07-01",
                            "status": "late",
                            "timestamp": "2025-07-01T21:30:50Z"
                        }
                    ],
                    "latestUserScores": [
                        {
                            "displayName": "apcwnm",
                            "reputation": 0.05264514963439993
                        },
                        {
                            "displayName": "bmc",
                            "reputation": 0.0019081526530939992
                        },
                        {
                            "displayName": "canon_bmc",
                            "reputation": 0.0017838668481032023
                        },
                        {
                            "displayName": "canon_corj60",
                            "reputation": -1.0093638303931118e-4
                        },
                        {
                            "displayName": "canon_corr",
                            "reputation": 0.0024634533799596414
                        },
                        {
                            "displayName": "canon_corr60",
                            "reputation": 9.042351552714196e-5
                        },
                        {
                            "displayName": "canon_cort20",
                            "reputation": 0.002277578252468051
                        },
                        {
                            "displayName": "canon_fnc_v3",
                            "reputation": 0.001916292879283429
                        },
                        {
                            "displayName": "canon_mmc",
                            "reputation": 0.0013103430824052923
                        },
                        {
                            "displayName": "canon_mmc60",
                            "reputation": -2.7924792436146903e-4
                        },
                        {
                            "displayName": "corj60",
                            "reputation": -9.820837268689735e-5
                        },
                        {
                            "displayName": "corr60",
                            "reputation": 1.1456571627467985e-4
                        },
                        {
                            "displayName": "corr_w_meta_model",
                            "reputation": 0.44022048492838317
                        },
                        {
                            "displayName": "cort20",
                            "reputation": 0.002426318056710863
                        },
                        {
                            "displayName": "fnc_v3",
                            "reputation": 0.0020414385367060204
                        },
                        {
                            "displayName": "mcwnm",
                            "reputation": 0.12183596667194749
                        },
                        {
                            "displayName": "mmc",
                            "reputation": 0.0013959165081950256
                        },
                        {
                            "displayName": "mmc60",
                            "reputation": -3.555302841870411e-4
                        },
                        {
                            "displayName": "season_score",
                            "reputation": 0.0038524128931045815
                        },
                        {
                            "displayName": "v2_corr20",
                            "reputation": 0.002624331968038638
                        }
                    ],
                    "name": "fnc_imp_01",
                    "profileUrl": "https://numerai-public-images.s3-us-west-2.amazonaws.com/profile_images/evolve2-iVbWPtqVP6eJ.png",
                    "returns": {
                        "allTime": 0.2547271725118586,
                        "oneDay": 0.902564952599325,
                        "oneYear": null,
                        "threeMonths": null
                    },
                    "submissionWebhook": null,
                    "tournament": 8,
                    "v2Stake": {
                        "latestValue": "10.000000000000000000",
                        "latestValueSettled": "10.000000000000000000",
                        "pendingV2ChangeStakeRequest": null,
                        "stakeValue": "10.002547271725118586",
                        "status": null
                    }
                },
                {
                    "computeEnabled": true,
                    "computePickleUpload": null,
                    "currentPayoutSelection": {
                        "corrMultiplier": 0.5,
                        "mmcMultiplier": 2.0,
                        "takeProfit": false,
                        "updatedAt": null
                    },
                    "description": null,
                    "earliestReleaseDate": "2025-10-07T00:00:00Z",
                    "id": "876d79d5-0942-46f6-946f-b2c09e451f6a",
                    "isComputeWeekdayEnabled": true,
                    "latestSubmissions": [
                        {
                            "filename": "deep_learning_predictions-THbXzlgccCeC.csv",
                            "id": "1c4a8994-ba96-4f3d-b30e-20b0f8332bca",
                            "roundCloseStaking": "2025-09-24",
                            "roundNumber": 1101,
                            "roundOpen": "2025-09-24",
                            "status": "queued",
                            "timestamp": "2025-09-23T14:36:06Z"
                        },
                        {
                            "filename": "deep_learning_predictions-THbXzlgccCeC.csv",
                            "id": "1c4a8994-ba96-4f3d-b30e-20b0f8332bca",
                            "roundCloseStaking": "2025-09-23",
                            "roundNumber": 1100,
                            "roundOpen": "2025-09-23",
                            "status": "late",
                            "timestamp": "2025-09-23T14:36:06Z"
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-22",
                            "roundNumber": 1099,
                            "roundOpen": "2025-09-20",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-19",
                            "roundNumber": 1098,
                            "roundOpen": "2025-09-19",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-18",
                            "roundNumber": 1097,
                            "roundOpen": "2025-09-18",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-17",
                            "roundNumber": 1096,
                            "roundOpen": "2025-09-17",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-16",
                            "roundNumber": 1095,
                            "roundOpen": "2025-09-16",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-15",
                            "roundNumber": 1094,
                            "roundOpen": "2025-09-13",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-12",
                            "roundNumber": 1093,
                            "roundOpen": "2025-09-12",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-11",
                            "roundNumber": 1092,
                            "roundOpen": "2025-09-11",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-10",
                            "roundNumber": 1091,
                            "roundOpen": "2025-09-10",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-09",
                            "roundNumber": 1090,
                            "roundOpen": "2025-09-09",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-08",
                            "roundNumber": 1089,
                            "roundOpen": "2025-09-06",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-05",
                            "roundNumber": 1088,
                            "roundOpen": "2025-09-05",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": "deep_learning_predictions-5STCMHF9WYdW.csv",
                            "id": "e773da0f-9f8f-4dd1-9796-c32785d05e16",
                            "roundCloseStaking": "2025-09-04",
                            "roundNumber": 1087,
                            "roundOpen": "2025-09-04",
                            "status": "on-time",
                            "timestamp": "2025-09-04T13:09:00Z"
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-03",
                            "roundNumber": 1086,
                            "roundOpen": "2025-09-03",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-02",
                            "roundNumber": 1085,
                            "roundOpen": "2025-09-02",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": "deep_learning_predictions-o6q72L9mmXij.csv",
                            "id": "522360bd-e4ae-4d11-95e7-a567304c0072",
                            "roundCloseStaking": "2025-09-01",
                            "roundNumber": 1084,
                            "roundOpen": "2025-08-30",
                            "status": "on-time",
                            "timestamp": "2025-08-30T13:09:51Z"
                        },
                        {
                            "filename": "deep_learning_predictions-3Y1vjdm07W9H.csv",
                            "id": "860d636a-a075-48b4-85bb-397beab88584",
                            "roundCloseStaking": "2025-08-29",
                            "roundNumber": 1083,
                            "roundOpen": "2025-08-29",
                            "status": "on-time",
                            "timestamp": "2025-08-29T13:08:52Z"
                        },
                        {
                            "filename": "deep_learning_predictions-KiT51f3yBfED.csv",
                            "id": "94785f17-bf89-4852-a991-066639e9e04e",
                            "roundCloseStaking": "2025-08-28",
                            "roundNumber": 1082,
                            "roundOpen": "2025-08-28",
                            "status": "on-time",
                            "timestamp": "2025-08-28T13:11:10Z"
                        },
                        {
                            "filename": "deep_learning_predictions-sJdwg9ErdBfq.csv",
                            "id": "eb5b6b3c-9971-4197-8ef8-b92bd2c5f00c",
                            "roundCloseStaking": "2025-08-27",
                            "roundNumber": 1081,
                            "roundOpen": "2025-08-27",
                            "status": "on-time",
                            "timestamp": "2025-08-27T13:09:24Z"
                        },
                        {
                            "filename": "deep_learning_predictions-zlclfufZoBCq.csv",
                            "id": "bf698315-9c86-40f3-97f6-902b057bb2b3",
                            "roundCloseStaking": "2025-08-26",
                            "roundNumber": 1080,
                            "roundOpen": "2025-08-26",
                            "status": "on-time",
                            "timestamp": "2025-08-26T13:08:46Z"
                        },
                        {
                            "filename": "deep_learning_predictions-QYjEt5tFHFgu.csv",
                            "id": "74a63e29-19ee-40d5-8b45-8ce4189b7d83",
                            "roundCloseStaking": "2025-08-25",
                            "roundNumber": 1079,
                            "roundOpen": "2025-08-23",
                            "status": "on-time",
                            "timestamp": "2025-08-23T13:10:01Z"
                        },
                        {
                            "filename": "deep_learning_predictions-58WpLvCgdzEn.csv",
                            "id": "af645b34-4523-4b58-95d9-0749797f28ef",
                            "roundCloseStaking": "2025-08-22",
                            "roundNumber": 1078,
                            "roundOpen": "2025-08-22",
                            "status": "on-time",
                            "timestamp": "2025-08-22T13:10:44Z"
                        },
                        {
                            "filename": "deep_learning_predictions-W7epEq8fRnFu.csv",
                            "id": "8bd44eca-0d65-485b-96c9-d87110134509",
                            "roundCloseStaking": "2025-08-21",
                            "roundNumber": 1077,
                            "roundOpen": "2025-08-21",
                            "status": "on-time",
                            "timestamp": "2025-08-21T13:10:29Z"
                        },
                        {
                            "filename": "deep_learning_predictions-Z8WQAlAzP8Pk.csv",
                            "id": "f970d42f-848f-4f8d-a81c-700a02e1fc72",
                            "roundCloseStaking": "2025-08-20",
                            "roundNumber": 1076,
                            "roundOpen": "2025-08-20",
                            "status": "on-time",
                            "timestamp": "2025-08-20T13:09:26Z"
                        },
                        {
                            "filename": "deep_learning_predictions-V5XwsVxlDPAU.csv",
                            "id": "c8bd3f58-f272-4afb-acb2-f995a167ce04",
                            "roundCloseStaking": "2025-08-19",
                            "roundNumber": 1075,
                            "roundOpen": "2025-08-19",
                            "status": "on-time",
                            "timestamp": "2025-08-19T13:09:19Z"
                        },
                        {
                            "filename": "deep_learning_predictions-BSjDIdH4ebZr.csv",
                            "id": "1a65241d-bcfe-4eb5-9e5b-59d343b49f46",
                            "roundCloseStaking": "2025-08-18",
                            "roundNumber": 1074,
                            "roundOpen": "2025-08-16",
                            "status": "on-time",
                            "timestamp": "2025-08-16T13:09:32Z"
                        },
                        {
                            "filename": "deep_learning_predictions-pmkdgfz1JxpP.csv",
                            "id": "2c1298b7-a3ab-4801-8036-03525ed0f65a",
                            "roundCloseStaking": "2025-08-15",
                            "roundNumber": 1073,
                            "roundOpen": "2025-08-15",
                            "status": "on-time",
                            "timestamp": "2025-08-15T13:11:11Z"
                        },
                        {
                            "filename": "deep_learning_predictions-ZIEEpIiG056G.csv",
                            "id": "f16bafeb-5db1-420d-a3f4-586d8e85a9ed",
                            "roundCloseStaking": "2025-08-14",
                            "roundNumber": 1072,
                            "roundOpen": "2025-08-14",
                            "status": "on-time",
                            "timestamp": "2025-08-14T13:11:15Z"
                        },
                        {
                            "filename": "deep_learning_predictions-SWykMeZPrGUt.csv",
                            "id": "d61ab577-484f-41de-b8c4-2da8119b053d",
                            "roundCloseStaking": "2025-08-13",
                            "roundNumber": 1071,
                            "roundOpen": "2025-08-13",
                            "status": "on-time",
                            "timestamp": "2025-08-13T13:10:07Z"
                        },
                        {
                            "filename": "deep_learning_predictions-zuv1JNalvbWP.csv",
                            "id": "b7a30c3a-1805-4405-b86c-a4a14841a7d5",
                            "roundCloseStaking": "2025-08-12",
                            "roundNumber": 1070,
                            "roundOpen": "2025-08-12",
                            "status": "on-time",
                            "timestamp": "2025-08-12T13:09:55Z"
                        },
                        {
                            "filename": "deep_learning_predictions-4aZuJCHGAamz.csv",
                            "id": "afe304b0-6551-4ea9-88a1-364e19366871",
                            "roundCloseStaking": "2025-08-11",
                            "roundNumber": 1069,
                            "roundOpen": "2025-08-09",
                            "status": "on-time",
                            "timestamp": "2025-08-09T13:10:04Z"
                        },
                        {
                            "filename": "deep_learning_predictions-r33xdIZUR68F.csv",
                            "id": "c1f631dc-ca8a-4ba2-8ded-b8fcf1de4bd8",
                            "roundCloseStaking": "2025-08-08",
                            "roundNumber": 1068,
                            "roundOpen": "2025-08-08",
                            "status": "on-time",
                            "timestamp": "2025-08-08T13:09:35Z"
                        },
                        {
                            "filename": "deep_learning_predictions-lzIt3HwRI8f9.csv",
                            "id": "3daa2565-c29e-4fa9-81d4-66d813663b26",
                            "roundCloseStaking": "2025-08-07",
                            "roundNumber": 1067,
                            "roundOpen": "2025-08-07",
                            "status": "on-time",
                            "timestamp": "2025-08-07T13:11:19Z"
                        },
                        {
                            "filename": "deep_learning_predictions-lKzo0abHHMTX.csv",
                            "id": "e08dd5f5-a7d3-4e24-9991-94a0d4b1abec",
                            "roundCloseStaking": "2025-08-06",
                            "roundNumber": 1066,
                            "roundOpen": "2025-08-06",
                            "status": "late",
                            "timestamp": "2025-08-06T14:15:13Z"
                        },
                        {
                            "filename": "deep_learning_predictions-3ZTQRCS81ZUU.csv",
                            "id": "9cf6a3b7-92a3-45b2-8dbb-d366a584a99f",
                            "roundCloseStaking": "2025-08-05",
                            "roundNumber": 1065,
                            "roundOpen": "2025-08-05",
                            "status": "on-time",
                            "timestamp": "2025-08-05T13:08:52Z"
                        },
                        {
                            "filename": "deep_learning_predictions-axcfgotQR3Tp.csv",
                            "id": "4ae06ff2-a58d-4fed-b677-ef139b18dffe",
                            "roundCloseStaking": "2025-08-04",
                            "roundNumber": 1064,
                            "roundOpen": "2025-08-02",
                            "status": "on-time",
                            "timestamp": "2025-08-02T13:20:34Z"
                        },
                        {
                            "filename": "deep_learning_predictions-Go952HB6o3cv.csv",
                            "id": "d1a17151-4c2e-443e-a4e7-55354f896ee0",
                            "roundCloseStaking": "2025-08-01",
                            "roundNumber": 1063,
                            "roundOpen": "2025-08-01",
                            "status": "on-time",
                            "timestamp": "2025-08-01T13:08:27Z"
                        },
                        {
                            "filename": "deep_learning_predictions-KH9UxUv91Vuu.csv",
                            "id": "d431cb26-9443-45b3-bf1b-bd942595d01d",
                            "roundCloseStaking": "2025-07-31",
                            "roundNumber": 1062,
                            "roundOpen": "2025-07-31",
                            "status": "on-time",
                            "timestamp": "2025-07-31T13:08:34Z"
                        },
                        {
                            "filename": "deep_learning_predictions-zxuV90aqzbv1.csv",
                            "id": "1fcd4683-7445-4433-9e1f-f6e6463277f9",
                            "roundCloseStaking": "2025-07-30",
                            "roundNumber": 1061,
                            "roundOpen": "2025-07-30",
                            "status": "on-time",
                            "timestamp": "2025-07-30T13:08:34Z"
                        },
                        {
                            "filename": "deep_learning_predictions-306GqpNjwUr6.csv",
                            "id": "763c5d52-b435-47b8-a019-d84ffdeac037",
                            "roundCloseStaking": "2025-07-29",
                            "roundNumber": 1060,
                            "roundOpen": "2025-07-29",
                            "status": "on-time",
                            "timestamp": "2025-07-29T13:08:49Z"
                        },
                        {
                            "filename": "deep_learning_predictions-8l9d7V1rUXh4.csv",
                            "id": "b65c8ae3-637a-4a01-84d9-1fa9811a4542",
                            "roundCloseStaking": "2025-07-28",
                            "roundNumber": 1059,
                            "roundOpen": "2025-07-26",
                            "status": "on-time",
                            "timestamp": "2025-07-26T13:09:47Z"
                        },
                        {
                            "filename": "deep_learning_predictions-ATfwOzX3tBZC.csv",
                            "id": "272ed724-3b3b-42fb-afd2-dbb9708008a6",
                            "roundCloseStaking": "2025-07-25",
                            "roundNumber": 1058,
                            "roundOpen": "2025-07-25",
                            "status": "on-time",
                            "timestamp": "2025-07-25T13:09:22Z"
                        },
                        {
                            "filename": "deep_learning_predictions-emDT05ULnRIA.csv",
                            "id": "6154a83e-061b-4c48-88c8-0cd15d0c92c1",
                            "roundCloseStaking": "2025-07-24",
                            "roundNumber": 1057,
                            "roundOpen": "2025-07-24",
                            "status": "on-time",
                            "timestamp": "2025-07-24T13:09:30Z"
                        },
                        {
                            "filename": "deep_learning_predictions-gcX6saOlEyBZ.csv",
                            "id": "c3c35daf-0416-4ab8-a991-790a3433f4fd",
                            "roundCloseStaking": "2025-07-23",
                            "roundNumber": 1056,
                            "roundOpen": "2025-07-23",
                            "status": "on-time",
                            "timestamp": "2025-07-23T13:09:12Z"
                        },
                        {
                            "filename": "deep_learning_predictions-ehH1vm3P4BSH.csv",
                            "id": "d3a5a134-4aa4-443f-895a-ee3ffc5bf611",
                            "roundCloseStaking": "2025-07-22",
                            "roundNumber": 1055,
                            "roundOpen": "2025-07-22",
                            "status": "on-time",
                            "timestamp": "2025-07-22T13:12:33Z"
                        },
                        {
                            "filename": "deep_learning_predictions-BRYQoUYKZOni.csv",
                            "id": "7c2671e1-c0a8-4695-a700-e8be4ef169b4",
                            "roundCloseStaking": "2025-07-21",
                            "roundNumber": 1054,
                            "roundOpen": "2025-07-19",
                            "status": "on-time",
                            "timestamp": "2025-07-19T13:09:32Z"
                        },
                        {
                            "filename": "deep_learning_predictions-tnZgp3VCy2Rx.csv",
                            "id": "519631f1-c995-454b-8592-3ddc49d4b009",
                            "roundCloseStaking": "2025-07-18",
                            "roundNumber": 1053,
                            "roundOpen": "2025-07-18",
                            "status": "on-time",
                            "timestamp": "2025-07-18T13:09:22Z"
                        },
                        {
                            "filename": "deep_learning_predictions-1Pm53F3yQ6Db.csv",
                            "id": "aebbdf82-bd50-4a93-9919-317d35375b6b",
                            "roundCloseStaking": "2025-07-17",
                            "roundNumber": 1052,
                            "roundOpen": "2025-07-17",
                            "status": "on-time",
                            "timestamp": "2025-07-17T13:15:37Z"
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-16",
                            "roundNumber": 1051,
                            "roundOpen": "2025-07-16",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": "deep_learning_predictions-GZtBnLPMHHWJ.csv",
                            "id": "1eb340f4-032a-4f89-bdfc-262a5a509249",
                            "roundCloseStaking": "2025-07-15",
                            "roundNumber": 1050,
                            "roundOpen": "2025-07-15",
                            "status": "on-time",
                            "timestamp": "2025-07-15T13:07:05Z"
                        },
                        {
                            "filename": "deep_learning_predictions-E6VEN3OffoCa.csv",
                            "id": "557c7267-0ab8-4797-983c-b9e823f28d88",
                            "roundCloseStaking": "2025-07-14",
                            "roundNumber": 1049,
                            "roundOpen": "2025-07-12",
                            "status": "on-time",
                            "timestamp": "2025-07-12T13:55:34Z"
                        },
                        {
                            "filename": "deep_learning_predictions-Dnw4P1LtToon.csv",
                            "id": "fe8413e2-5f20-4312-bf96-16d9b7e042a1",
                            "roundCloseStaking": "2025-07-11",
                            "roundNumber": 1048,
                            "roundOpen": "2025-07-11",
                            "status": "on-time",
                            "timestamp": "2025-07-11T13:07:14Z"
                        },
                        {
                            "filename": "deep_learning_predictions-OJqiyHqbm5bQ.csv",
                            "id": "967268f8-dcda-4f56-934a-17bbee9bc2f3",
                            "roundCloseStaking": "2025-07-10",
                            "roundNumber": 1047,
                            "roundOpen": "2025-07-10",
                            "status": "on-time",
                            "timestamp": "2025-07-10T13:08:06Z"
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-09",
                            "roundNumber": 1046,
                            "roundOpen": "2025-07-09",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": "deep_learning_predictions-OXNzXUXR0B51.csv",
                            "id": "c40e1a81-0cf0-4325-94ef-d23f394e686d",
                            "roundCloseStaking": "2025-07-08",
                            "roundNumber": 1045,
                            "roundOpen": "2025-07-08",
                            "status": "on-time",
                            "timestamp": "2025-07-08T13:56:27Z"
                        },
                        {
                            "filename": "deep_learning_predictions-7zYrsAIxW3FQ.csv",
                            "id": "f76b5fbb-b4d1-4195-92e4-d410b930ad17",
                            "roundCloseStaking": "2025-07-07",
                            "roundNumber": 1044,
                            "roundOpen": "2025-07-05",
                            "status": "on-time",
                            "timestamp": "2025-07-05T13:59:17Z"
                        },
                        {
                            "filename": "deep_learning_predictions-QK7X37vlz6pb.csv",
                            "id": "708a5f21-5e9b-49ef-b853-c09dcf8133c5",
                            "roundCloseStaking": "2025-07-04",
                            "roundNumber": 1043,
                            "roundOpen": "2025-07-04",
                            "status": "on-time",
                            "timestamp": "2025-07-04T13:11:37Z"
                        },
                        {
                            "filename": "deep_learning_predictions-QK7X37vlz6pb.csv",
                            "id": "c8ef60f7-0a9a-460d-bcaf-cc1b617b8451",
                            "roundCloseStaking": "2025-07-03",
                            "roundNumber": 1042,
                            "roundOpen": "2025-07-03",
                            "status": "late",
                            "timestamp": "2025-07-04T12:03:01Z"
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-02",
                            "roundNumber": 1041,
                            "roundOpen": "2025-07-02",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-01",
                            "roundNumber": 1040,
                            "roundOpen": "2025-07-01",
                            "status": "none",
                            "timestamp": null
                        }
                    ],
                    "latestUserScores": [
                        {
                            "displayName": "apcwnm",
                            "reputation": 0.0051130731008480175
                        },
                        {
                            "displayName": "bmc",
                            "reputation": -0.0015354443825091367
                        },
                        {
                            "displayName": "canon_bmc",
                            "reputation": -0.0014354345951426413
                        },
                        {
                            "displayName": "canon_corj60",
                            "reputation": 2.290795767560117e-6
                        },
                        {
                            "displayName": "canon_corr",
                            "reputation": -0.0018641695698373795
                        },
                        {
                            "displayName": "canon_corr60",
                            "reputation": -7.972140569379863e-5
                        },
                        {
                            "displayName": "canon_cort20",
                            "reputation": -4.3884284119320027e-4
                        },
                        {
                            "displayName": "canon_fnc_v3",
                            "reputation": -0.002051365462875525
                        },
                        {
                            "displayName": "canon_mmc",
                            "reputation": -0.0014683571024143155
                        },
                        {
                            "displayName": "canon_mmc60",
                            "reputation": -7.950066138337859e-5
                        },
                        {
                            "displayName": "corj60",
                            "reputation": 2.2288823684368707e-6
                        },
                        {
                            "displayName": "corr60",
                            "reputation": -1.0100624701981282e-4
                        },
                        {
                            "displayName": "corr_w_meta_model",
                            "reputation": 0.03408481558998299
                        },
                        {
                            "displayName": "cort20",
                            "reputation": -4.6750196551602157e-4
                        },
                        {
                            "displayName": "fnc_v3",
                            "reputation": -0.0021853321869816818
                        },
                        {
                            "displayName": "mcwnm",
                            "reputation": 0.0631229157207764
                        },
                        {
                            "displayName": "mmc",
                            "reputation": -0.0015642498111434137
                        },
                        {
                            "displayName": "mmc60",
                            "reputation": -1.0121791522469176e-4
                        },
                        {
                            "displayName": "season_score",
                            "reputation": -0.0038687989705902333
                        },
                        {
                            "displayName": "v2_corr20",
                            "reputation": -0.001985911256030841
                        }
                    ],
                    "name": "fnc_dl_c1d8",
                    "profileUrl": "https://numerai-public-images.s3-us-west-2.amazonaws.com/profile_images_originals/wile-y0fAk4UssbGz.jpg",
                    "returns": {
                        "allTime": -9.81450062849314,
                        "oneDay": 0.4464424829724736,
                        "oneYear": null,
                        "threeMonths": null
                    },
                    "submissionWebhook": "https://numerai.imperialai.ai/numerai-c1d82ec4-23c7-41b4-b2ea-c1239034bc19/",
                    "tournament": 8,
                    "v2Stake": {
                        "latestValue": "0.456424609159957400",
                        "latestValueSettled": "9.456424609159958000",
                        "pendingV2ChangeStakeRequest": {
                            "drain": false,
                            "dueDate": "2025-09-26T00:00:00Z",
                            "requestedAmount": "9.000000000000000000",
                            "status": "pending",
                            "type": "decrease"
                        },
                        "stakeValue": "9.436750498649829194",
                        "status": null
                    }
                },
                {
                    "computeEnabled": true,
                    "computePickleUpload": null,
                    "currentPayoutSelection": {
                        "corrMultiplier": 0.5,
                        "mmcMultiplier": 2.0,
                        "takeProfit": false,
                        "updatedAt": null
                    },
                    "description": null,
                    "earliestReleaseDate": "2025-10-24T00:00:00Z",
                    "id": "6afb711e-0b81-4f0b-9003-85fb88aa081c",
                    "isComputeWeekdayEnabled": true,
                    "latestSubmissions": [
                        {
                            "filename": "predictions_20250923_131336-fERzZrsNmNMp.csv",
                            "id": "68fc4fb5-6238-4ca7-ace0-b60c9cf96207",
                            "roundCloseStaking": "2025-09-23",
                            "roundNumber": 1100,
                            "roundOpen": "2025-09-23",
                            "status": "on-time",
                            "timestamp": "2025-09-23T13:13:42Z"
                        },
                        {
                            "filename": "predictions_20250920_130935-z2OtmChCv7uU.csv",
                            "id": "fa14fcfb-1a9b-45ce-a137-656d7f1ad554",
                            "roundCloseStaking": "2025-09-22",
                            "roundNumber": 1099,
                            "roundOpen": "2025-09-20",
                            "status": "on-time",
                            "timestamp": "2025-09-20T13:09:41Z"
                        },
                        {
                            "filename": "predictions_20250919_130856-v6HL9q5ZuOWp.csv",
                            "id": "18896ecd-2acd-4b1f-9a8f-13926a2b6a1c",
                            "roundCloseStaking": "2025-09-19",
                            "roundNumber": 1098,
                            "roundOpen": "2025-09-19",
                            "status": "on-time",
                            "timestamp": "2025-09-19T13:09:02Z"
                        },
                        {
                            "filename": "predictions_20250918_130906-UdH1p1bbT1yH.csv",
                            "id": "4d4593d5-fc8f-41b2-9b99-7eb54576769a",
                            "roundCloseStaking": "2025-09-18",
                            "roundNumber": 1097,
                            "roundOpen": "2025-09-18",
                            "status": "on-time",
                            "timestamp": "2025-09-18T13:09:11Z"
                        },
                        {
                            "filename": "predictions_20250917_131045-L7ND6E7iVhzq.csv",
                            "id": "706ecf6c-1d6d-4e03-8aac-a902b0035dc0",
                            "roundCloseStaking": "2025-09-17",
                            "roundNumber": 1096,
                            "roundOpen": "2025-09-17",
                            "status": "on-time",
                            "timestamp": "2025-09-17T13:10:50Z"
                        },
                        {
                            "filename": "predictions_20250916_130709-ZUJyurqWxbha.csv",
                            "id": "d6999b58-8884-411d-ad06-1e5c77e34b51",
                            "roundCloseStaking": "2025-09-16",
                            "roundNumber": 1095,
                            "roundOpen": "2025-09-16",
                            "status": "on-time",
                            "timestamp": "2025-09-16T13:07:14Z"
                        },
                        {
                            "filename": "predictions_20250913_130938-GfGaXhndvcNs.csv",
                            "id": "9eaa9939-6f15-4ec6-a286-895891b6ee43",
                            "roundCloseStaking": "2025-09-15",
                            "roundNumber": 1094,
                            "roundOpen": "2025-09-13",
                            "status": "on-time",
                            "timestamp": "2025-09-13T13:09:43Z"
                        },
                        {
                            "filename": "predictions_20250912_130906-4RXQ3zyLuMtF.csv",
                            "id": "f2d8c68f-3446-4f0a-95e3-e767d77fc00a",
                            "roundCloseStaking": "2025-09-12",
                            "roundNumber": 1093,
                            "roundOpen": "2025-09-12",
                            "status": "on-time",
                            "timestamp": "2025-09-12T13:09:11Z"
                        },
                        {
                            "filename": "predictions_20250911_130900-jtFmmbwg06hf.csv",
                            "id": "45e73a38-4ebc-4308-97bd-f6f7431ed05b",
                            "roundCloseStaking": "2025-09-11",
                            "roundNumber": 1092,
                            "roundOpen": "2025-09-11",
                            "status": "on-time",
                            "timestamp": "2025-09-11T13:09:05Z"
                        },
                        {
                            "filename": "predictions_20250910_130925-BAXJF1en3Hca.csv",
                            "id": "e47cf3ac-ffea-4073-8923-48f1bd0fb942",
                            "roundCloseStaking": "2025-09-10",
                            "roundNumber": 1091,
                            "roundOpen": "2025-09-10",
                            "status": "on-time",
                            "timestamp": "2025-09-10T13:09:30Z"
                        },
                        {
                            "filename": "predictions_20250909_130828-V4fwi7m9QeVt.csv",
                            "id": "dbabae43-897f-4044-859d-8475a30bb50d",
                            "roundCloseStaking": "2025-09-09",
                            "roundNumber": 1090,
                            "roundOpen": "2025-09-09",
                            "status": "on-time",
                            "timestamp": "2025-09-09T13:08:35Z"
                        },
                        {
                            "filename": "predictions_20250906_130643-ZJIUJKnFUH66.csv",
                            "id": "3d83de2b-3560-4c70-835c-83128c4ceef2",
                            "roundCloseStaking": "2025-09-08",
                            "roundNumber": 1089,
                            "roundOpen": "2025-09-06",
                            "status": "on-time",
                            "timestamp": "2025-09-06T13:06:48Z"
                        },
                        {
                            "filename": "predictions_20250905_130810-w7Y7BT0qpczG.csv",
                            "id": "6637bad0-c403-42a3-8ebe-1e1cf475d4c6",
                            "roundCloseStaking": "2025-09-05",
                            "roundNumber": 1088,
                            "roundOpen": "2025-09-05",
                            "status": "on-time",
                            "timestamp": "2025-09-05T13:08:16Z"
                        },
                        {
                            "filename": "predictions_20250904_130830-rUTX2qWtG3BJ.csv",
                            "id": "aae8fde9-b2a0-4425-9b5e-995f1caa0559",
                            "roundCloseStaking": "2025-09-04",
                            "roundNumber": 1087,
                            "roundOpen": "2025-09-04",
                            "status": "on-time",
                            "timestamp": "2025-09-04T13:08:36Z"
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-03",
                            "roundNumber": 1086,
                            "roundOpen": "2025-09-03",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": "predictions_20250902_131844-t64YcFLRgcXZ.csv",
                            "id": "d563ab03-8cb0-4c5e-8881-5626eee2bb0c",
                            "roundCloseStaking": "2025-09-02",
                            "roundNumber": 1085,
                            "roundOpen": "2025-09-02",
                            "status": "on-time",
                            "timestamp": "2025-09-02T13:18:49Z"
                        },
                        {
                            "filename": "predictions_20250830_130906-8Kag1ejykQmV.csv",
                            "id": "cbd30e14-078e-4c70-83e0-f3aa29892664",
                            "roundCloseStaking": "2025-09-01",
                            "roundNumber": 1084,
                            "roundOpen": "2025-08-30",
                            "status": "on-time",
                            "timestamp": "2025-08-30T13:09:11Z"
                        },
                        {
                            "filename": "predictions_20250829_131037-7O36nCA1Hbtz.csv",
                            "id": "ac414fdc-8160-4cd9-9238-a50bfc408006",
                            "roundCloseStaking": "2025-08-29",
                            "roundNumber": 1083,
                            "roundOpen": "2025-08-29",
                            "status": "on-time",
                            "timestamp": "2025-08-29T13:10:43Z"
                        },
                        {
                            "filename": "predictions_20250828_131132-ksLDiwnBmSoC.csv",
                            "id": "00c4017f-93ef-4138-bbfa-e0ad1a034d67",
                            "roundCloseStaking": "2025-08-28",
                            "roundNumber": 1082,
                            "roundOpen": "2025-08-28",
                            "status": "on-time",
                            "timestamp": "2025-08-28T13:11:37Z"
                        },
                        {
                            "filename": "predictions_20250827_131032-MQHMsFQWk9RW.csv",
                            "id": "abb137fd-97a5-4220-b02d-7c00e64e51e6",
                            "roundCloseStaking": "2025-08-27",
                            "roundNumber": 1081,
                            "roundOpen": "2025-08-27",
                            "status": "on-time",
                            "timestamp": "2025-08-27T13:10:37Z"
                        },
                        {
                            "filename": "predictions_20250826_130917-wYBxrXyfGAjS.csv",
                            "id": "a7bc74a8-bc70-4528-aa8c-d8258aefe884",
                            "roundCloseStaking": "2025-08-26",
                            "roundNumber": 1080,
                            "roundOpen": "2025-08-26",
                            "status": "on-time",
                            "timestamp": "2025-08-26T13:09:22Z"
                        },
                        {
                            "filename": "predictions_20250823_130937-vlTCStWC6MLV.csv",
                            "id": "5d648749-186f-4f03-b5cd-12aa35905caf",
                            "roundCloseStaking": "2025-08-25",
                            "roundNumber": 1079,
                            "roundOpen": "2025-08-23",
                            "status": "on-time",
                            "timestamp": "2025-08-23T13:09:42Z"
                        },
                        {
                            "filename": "predictions_20250822_130900-uY4eZaTOLFrK.csv",
                            "id": "615a35d6-4dc3-4734-8e92-bd9b46edfb90",
                            "roundCloseStaking": "2025-08-22",
                            "roundNumber": 1078,
                            "roundOpen": "2025-08-22",
                            "status": "on-time",
                            "timestamp": "2025-08-22T13:09:06Z"
                        },
                        {
                            "filename": "predictions_20250821_130855-KIo7DxgxqTSN.csv",
                            "id": "e99481cc-9144-484c-8825-465408c1ddb4",
                            "roundCloseStaking": "2025-08-21",
                            "roundNumber": 1077,
                            "roundOpen": "2025-08-21",
                            "status": "on-time",
                            "timestamp": "2025-08-21T13:09:00Z"
                        },
                        {
                            "filename": "predictions_20250820_130904-pMqbbCpJ8JV9.csv",
                            "id": "18811e2e-1b8b-423b-841d-d9353a23d104",
                            "roundCloseStaking": "2025-08-20",
                            "roundNumber": 1076,
                            "roundOpen": "2025-08-20",
                            "status": "on-time",
                            "timestamp": "2025-08-20T13:09:11Z"
                        },
                        {
                            "filename": "predictions_20250819_130850-HXsYIppoVlI4.csv",
                            "id": "d6343503-a50f-45fd-bf6f-7edf3e102053",
                            "roundCloseStaking": "2025-08-19",
                            "roundNumber": 1075,
                            "roundOpen": "2025-08-19",
                            "status": "on-time",
                            "timestamp": "2025-08-19T13:08:56Z"
                        },
                        {
                            "filename": "predictions_20250816_130756-VQzm0PsUREbA.csv",
                            "id": "53ca7887-b136-4aca-ae87-3481cc5d90e0",
                            "roundCloseStaking": "2025-08-18",
                            "roundNumber": 1074,
                            "roundOpen": "2025-08-16",
                            "status": "on-time",
                            "timestamp": "2025-08-16T13:08:02Z"
                        },
                        {
                            "filename": "predictions_20250815_130919-wADNeqaeTLf4.csv",
                            "id": "7b17bbb5-c2de-4c00-aac7-026433922503",
                            "roundCloseStaking": "2025-08-15",
                            "roundNumber": 1073,
                            "roundOpen": "2025-08-15",
                            "status": "on-time",
                            "timestamp": "2025-08-15T13:09:25Z"
                        },
                        {
                            "filename": "predictions_20250814_130921-PaPsdChIuQzL.csv",
                            "id": "8f5c428f-42bb-4671-a354-9a317e435373",
                            "roundCloseStaking": "2025-08-14",
                            "roundNumber": 1072,
                            "roundOpen": "2025-08-14",
                            "status": "on-time",
                            "timestamp": "2025-08-14T13:09:27Z"
                        },
                        {
                            "filename": "predictions_20250813_130931-Ig79gQbC9xFd.csv",
                            "id": "5bcdfcaa-3532-4d3c-b6aa-18d5d0c4408d",
                            "roundCloseStaking": "2025-08-13",
                            "roundNumber": 1071,
                            "roundOpen": "2025-08-13",
                            "status": "on-time",
                            "timestamp": "2025-08-13T13:09:36Z"
                        },
                        {
                            "filename": "predictions_20250812_130910-pLw5vodgBUSK.csv",
                            "id": "54998f38-dc69-414b-8b5b-22bd5b052c74",
                            "roundCloseStaking": "2025-08-12",
                            "roundNumber": 1070,
                            "roundOpen": "2025-08-12",
                            "status": "on-time",
                            "timestamp": "2025-08-12T13:09:16Z"
                        },
                        {
                            "filename": "predictions_20250809_130927-oMzWiFQuGBCg.csv",
                            "id": "f7fced6d-ced4-4fd6-ad6e-b94d8a778c87",
                            "roundCloseStaking": "2025-08-11",
                            "roundNumber": 1069,
                            "roundOpen": "2025-08-09",
                            "status": "on-time",
                            "timestamp": "2025-08-09T13:09:33Z"
                        },
                        {
                            "filename": "predictions_20250808_130905-OMcxVyR8JuEb.csv",
                            "id": "f2b355ac-520f-47ed-ba62-80e01e591322",
                            "roundCloseStaking": "2025-08-08",
                            "roundNumber": 1068,
                            "roundOpen": "2025-08-08",
                            "status": "on-time",
                            "timestamp": "2025-08-08T13:09:11Z"
                        },
                        {
                            "filename": "predictions_20250807_131055-FJUfKNqHzNc7.csv",
                            "id": "b5be2726-7e1d-41dd-a6e2-165eea58c767",
                            "roundCloseStaking": "2025-08-07",
                            "roundNumber": 1067,
                            "roundOpen": "2025-08-07",
                            "status": "on-time",
                            "timestamp": "2025-08-07T13:11:31Z"
                        },
                        {
                            "filename": "predictions_20250806_141459-K9crYpMfKh9U.csv",
                            "id": "269b547c-2438-4e90-ae76-2b61d0a169de",
                            "roundCloseStaking": "2025-08-06",
                            "roundNumber": 1066,
                            "roundOpen": "2025-08-06",
                            "status": "late",
                            "timestamp": "2025-08-06T14:15:04Z"
                        },
                        {
                            "filename": "predictions_20250805_130830-3lWAoWf6RdZl.csv",
                            "id": "9b74e067-d219-4533-8099-0f8992a657ab",
                            "roundCloseStaking": "2025-08-05",
                            "roundNumber": 1065,
                            "roundOpen": "2025-08-05",
                            "status": "on-time",
                            "timestamp": "2025-08-05T13:08:36Z"
                        },
                        {
                            "filename": "predictions_20250802_132000-fYSEE0uIHs5O.csv",
                            "id": "332e97ed-921b-4bc0-8281-d16c29addda5",
                            "roundCloseStaking": "2025-08-04",
                            "roundNumber": 1064,
                            "roundOpen": "2025-08-02",
                            "status": "on-time",
                            "timestamp": "2025-08-02T13:20:06Z"
                        },
                        {
                            "filename": "predictions_20250801_130805-4hPe9D15Mtt5.csv",
                            "id": "4b25759f-3ecc-4924-aea0-f5b480535d7f",
                            "roundCloseStaking": "2025-08-01",
                            "roundNumber": 1063,
                            "roundOpen": "2025-08-01",
                            "status": "on-time",
                            "timestamp": "2025-08-01T13:08:12Z"
                        },
                        {
                            "filename": "predictions_20250731_130804-3wcnbZC3udzx.csv",
                            "id": "7216f325-1951-4f80-afcf-2c93a4916c22",
                            "roundCloseStaking": "2025-07-31",
                            "roundNumber": 1062,
                            "roundOpen": "2025-07-31",
                            "status": "on-time",
                            "timestamp": "2025-07-31T13:08:11Z"
                        },
                        {
                            "filename": "predictions_20250730_130818-rYtIL6ZTUHRu.csv",
                            "id": "99028b01-9284-41cc-ba29-2e1de1b0f6b9",
                            "roundCloseStaking": "2025-07-30",
                            "roundNumber": 1061,
                            "roundOpen": "2025-07-30",
                            "status": "on-time",
                            "timestamp": "2025-07-30T13:08:24Z"
                        },
                        {
                            "filename": "predictions_20250729_130831-b9qfwsb5qPxH.csv",
                            "id": "918c3ea5-3b35-4e5c-ae9d-370f3ed5f2e9",
                            "roundCloseStaking": "2025-07-29",
                            "roundNumber": 1060,
                            "roundOpen": "2025-07-29",
                            "status": "on-time",
                            "timestamp": "2025-07-29T13:08:37Z"
                        },
                        {
                            "filename": "predictions_20250726_130925-OGRFEsRGP0Ao.csv",
                            "id": "b821453d-f0d7-47ed-aa60-50270c689f99",
                            "roundCloseStaking": "2025-07-28",
                            "roundNumber": 1059,
                            "roundOpen": "2025-07-26",
                            "status": "on-time",
                            "timestamp": "2025-07-26T13:09:30Z"
                        },
                        {
                            "filename": "predictions_20250725_130855-zOyUDOX3l4Df.csv",
                            "id": "320140ae-069d-429a-a297-7aab809293b2",
                            "roundCloseStaking": "2025-07-25",
                            "roundNumber": 1058,
                            "roundOpen": "2025-07-25",
                            "status": "on-time",
                            "timestamp": "2025-07-25T13:09:01Z"
                        },
                        {
                            "filename": "predictions_20250724_130912-T6Sj7kEIO5i8.csv",
                            "id": "27c3da61-fd4b-4e0c-8a37-4bd4db58d498",
                            "roundCloseStaking": "2025-07-24",
                            "roundNumber": 1057,
                            "roundOpen": "2025-07-24",
                            "status": "on-time",
                            "timestamp": "2025-07-24T13:09:18Z"
                        },
                        {
                            "filename": "predictions_20250723_130854-aKkyLdntPw6I.csv",
                            "id": "c38f0c71-f60b-436f-9608-97b7a45ee9f8",
                            "roundCloseStaking": "2025-07-23",
                            "roundNumber": 1056,
                            "roundOpen": "2025-07-23",
                            "status": "on-time",
                            "timestamp": "2025-07-23T13:09:00Z"
                        },
                        {
                            "filename": "predictions_20250722_131209-P4atxa4QU1e4.csv",
                            "id": "34ceea36-fdd5-409c-a0e8-7f730bd307f1",
                            "roundCloseStaking": "2025-07-22",
                            "roundNumber": 1055,
                            "roundOpen": "2025-07-22",
                            "status": "on-time",
                            "timestamp": "2025-07-22T13:12:16Z"
                        },
                        {
                            "filename": "predictions_20250719_130909-sU7NxXHiyT7Z.csv",
                            "id": "c1fc3ac8-80a5-4523-a148-b858d2f19022",
                            "roundCloseStaking": "2025-07-21",
                            "roundNumber": 1054,
                            "roundOpen": "2025-07-19",
                            "status": "on-time",
                            "timestamp": "2025-07-19T13:09:15Z"
                        },
                        {
                            "filename": "predictions_20250718_130856-WkC2myK70yMa.csv",
                            "id": "9d394b19-7364-4ebf-9aa1-b855f3aa68b5",
                            "roundCloseStaking": "2025-07-18",
                            "roundNumber": 1053,
                            "roundOpen": "2025-07-18",
                            "status": "on-time",
                            "timestamp": "2025-07-18T13:09:01Z"
                        },
                        {
                            "filename": "predictions_20250717_131514-netVYdMBp2sv.csv",
                            "id": "fe7d3a1f-68d7-46d7-9a86-091d2ea7fa88",
                            "roundCloseStaking": "2025-07-17",
                            "roundNumber": 1052,
                            "roundOpen": "2025-07-17",
                            "status": "on-time",
                            "timestamp": "2025-07-17T13:15:20Z"
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-16",
                            "roundNumber": 1051,
                            "roundOpen": "2025-07-16",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": "predictions_20250715_130642-j1l5XDSztVRM.csv",
                            "id": "8a5f944b-885e-408c-9d9c-e2e080c56698",
                            "roundCloseStaking": "2025-07-15",
                            "roundNumber": 1050,
                            "roundOpen": "2025-07-15",
                            "status": "on-time",
                            "timestamp": "2025-07-15T13:06:47Z"
                        },
                        {
                            "filename": "predictions_20250712_135530-4zowEiKwjOW1.csv",
                            "id": "92269d9e-fce0-4f35-9e1e-10a3b6279d44",
                            "roundCloseStaking": "2025-07-14",
                            "roundNumber": 1049,
                            "roundOpen": "2025-07-12",
                            "status": "on-time",
                            "timestamp": "2025-07-12T13:55:40Z"
                        },
                        {
                            "filename": "predictions_20250711_130622-Hn6iAA47OPa8.csv",
                            "id": "1c982cb4-80f1-41c6-89b2-7a016cff389e",
                            "roundCloseStaking": "2025-07-11",
                            "roundNumber": 1048,
                            "roundOpen": "2025-07-11",
                            "status": "on-time",
                            "timestamp": "2025-07-11T13:06:31Z"
                        },
                        {
                            "filename": "predictions_20250710_130756-mfUh3rm59VC3.csv",
                            "id": "946d5c6a-51e9-48d2-9965-884dae267a69",
                            "roundCloseStaking": "2025-07-10",
                            "roundNumber": 1047,
                            "roundOpen": "2025-07-10",
                            "status": "on-time",
                            "timestamp": "2025-07-10T13:08:01Z"
                        },
                        {
                            "filename": "predictions_20250709_130820-hZzDy6z7d6rM.csv",
                            "id": "cccc5bb8-3fe1-4fb7-b475-06f8c370e7ed",
                            "roundCloseStaking": "2025-07-09",
                            "roundNumber": 1046,
                            "roundOpen": "2025-07-09",
                            "status": "on-time",
                            "timestamp": "2025-07-09T13:08:25Z"
                        },
                        {
                            "filename": "predictions_20250708_135604-VZTEQ5NTe0dk.csv",
                            "id": "ab97e640-c673-481c-93dd-6069dd62684c",
                            "roundCloseStaking": "2025-07-08",
                            "roundNumber": 1045,
                            "roundOpen": "2025-07-08",
                            "status": "on-time",
                            "timestamp": "2025-07-08T13:56:10Z"
                        },
                        {
                            "filename": "predictions_20250705_135747-gbi6agyD7JdZ.csv",
                            "id": "0106a95f-3365-48fc-9d69-bd429d9a60fc",
                            "roundCloseStaking": "2025-07-07",
                            "roundNumber": 1044,
                            "roundOpen": "2025-07-05",
                            "status": "on-time",
                            "timestamp": "2025-07-05T13:57:52Z"
                        },
                        {
                            "filename": "predictions_20250705_111320-kJwXRwkBRmuS.csv",
                            "id": "300f4760-f242-4bb7-97b7-3f4644425480",
                            "roundCloseStaking": "2025-07-04",
                            "roundNumber": 1043,
                            "roundOpen": "2025-07-04",
                            "status": "late",
                            "timestamp": "2025-07-05T11:13:28Z"
                        },
                        {
                            "filename": "predictions_20250703_133701-iI7PN3TT2EE6.csv",
                            "id": "fb565e0f-496c-4b12-94be-bf64af1b1280",
                            "roundCloseStaking": "2025-07-03",
                            "roundNumber": 1042,
                            "roundOpen": "2025-07-03",
                            "status": "on-time",
                            "timestamp": "2025-07-03T13:37:36Z"
                        },
                        {
                            "filename": "predictions_20250702_132902-C3Hv4dmmBmTv.csv",
                            "id": "a762ee38-c8f4-44a4-abb8-b3a9f341be6a",
                            "roundCloseStaking": "2025-07-02",
                            "roundNumber": 1041,
                            "roundOpen": "2025-07-02",
                            "status": "on-time",
                            "timestamp": "2025-07-02T13:29:07Z"
                        },
                        {
                            "filename": "predictions_20250701_112551-ctZWmMlqPsSP.csv",
                            "id": "cc33cff2-9de6-415c-9784-dd1c8f411263",
                            "roundCloseStaking": "2025-07-01",
                            "roundNumber": 1040,
                            "roundOpen": "2025-07-01",
                            "status": "on-time",
                            "timestamp": "2025-07-01T13:35:41Z"
                        }
                    ],
                    "latestUserScores": [
                        {
                            "displayName": "apcwnm",
                            "reputation": 0.06341335580822817
                        },
                        {
                            "displayName": "bmc",
                            "reputation": -7.326103427367857e-6
                        },
                        {
                            "displayName": "canon_bmc",
                            "reputation": -6.848924276926272e-6
                        },
                        {
                            "displayName": "canon_corr",
                            "reputation": 0.0014427529961299178
                        },
                        {
                            "displayName": "canon_cort20",
                            "reputation": 0.0015596870905649502
                        },
                        {
                            "displayName": "canon_fnc_v3",
                            "reputation": 7.977565566029909e-4
                        },
                        {
                            "displayName": "canon_mmc",
                            "reputation": -5.197636489487317e-4
                        },
                        {
                            "displayName": "corr_w_meta_model",
                            "reputation": 0.5618297892508224
                        },
                        {
                            "displayName": "cort20",
                            "reputation": 0.0016615442066834777
                        },
                        {
                            "displayName": "fnc_v3",
                            "reputation": 8.498549439729821e-4
                        },
                        {
                            "displayName": "mcwnm",
                            "reputation": 0.14960966373152348
                        },
                        {
                            "displayName": "mmc",
                            "reputation": -5.537073974515059e-4
                        },
                        {
                            "displayName": "season_score",
                            "reputation": -3.1815079983250444e-4
                        },
                        {
                            "displayName": "v2_corr20",
                            "reputation": 0.0015369735999588104
                        }
                    ],
                    "name": "fnc_xgboost",
                    "profileUrl": "https://numerai-public-images.s3-us-west-2.amazonaws.com/profile_images/booster-FQNylBqQGUr1.jpg",
                    "returns": {
                        "allTime": -0.2544295439327256,
                        "oneDay": 0.4441876506397775,
                        "oneYear": null,
                        "threeMonths": null
                    },
                    "submissionWebhook": "https://numerai.imperialai.ai/numerai-6afb711e-0b81-4f0b-9003-85fb88aa081c/",
                    "tournament": 8,
                    "v2Stake": {
                        "latestValue": "0.998708676440228300",
                        "latestValueSettled": "0.998708676440228300",
                        "pendingV2ChangeStakeRequest": null,
                        "stakeValue": "0.997455704560672747",
                        "status": null
                    }
                },
                {
                    "computeEnabled": true,
                    "computePickleUpload": null,
                    "currentPayoutSelection": {
                        "corrMultiplier": 0.5,
                        "mmcMultiplier": 2.0,
                        "takeProfit": false,
                        "updatedAt": null
                    },
                    "description": null,
                    "earliestReleaseDate": "2025-10-24T00:00:00Z",
                    "id": "eb9fa1ab-0d67-4970-b477-c9c0e7bcac5e",
                    "isComputeWeekdayEnabled": true,
                    "latestSubmissions": [
                        {
                            "filename": "tabnet_predictions-SD1T7rlgEzwz.csv",
                            "id": "21a3ac22-633a-487f-bf3c-f22d63465d86",
                            "roundCloseStaking": "2025-09-23",
                            "roundNumber": 1100,
                            "roundOpen": "2025-09-23",
                            "status": "on-time",
                            "timestamp": "2025-09-23T13:15:29Z"
                        },
                        {
                            "filename": "tabnet_predictions-Ep3yTKtqNCbV.csv",
                            "id": "1e092712-d3c5-4677-afc4-e5f084daa9ab",
                            "roundCloseStaking": "2025-09-22",
                            "roundNumber": 1099,
                            "roundOpen": "2025-09-20",
                            "status": "on-time",
                            "timestamp": "2025-09-21T11:04:23Z"
                        },
                        {
                            "filename": "tabnet_predictions-wqeW2qJKOqmS.csv",
                            "id": "30b30e5b-2ddd-4657-b6be-61b26048961e",
                            "roundCloseStaking": "2025-09-19",
                            "roundNumber": 1098,
                            "roundOpen": "2025-09-19",
                            "status": "on-time",
                            "timestamp": "2025-09-19T13:10:44Z"
                        },
                        {
                            "filename": "tabnet_predictions-Jx3zh2QyXjXe.csv",
                            "id": "8f55e1ae-83df-463f-8589-44c405778261",
                            "roundCloseStaking": "2025-09-18",
                            "roundNumber": 1097,
                            "roundOpen": "2025-09-18",
                            "status": "on-time",
                            "timestamp": "2025-09-18T13:10:39Z"
                        },
                        {
                            "filename": "tabnet_predictions-Dnhh8t2nVzEh.csv",
                            "id": "ed17544e-8c41-4b50-aafa-022b78749125",
                            "roundCloseStaking": "2025-09-17",
                            "roundNumber": 1096,
                            "roundOpen": "2025-09-17",
                            "status": "on-time",
                            "timestamp": "2025-09-17T13:12:38Z"
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-16",
                            "roundNumber": 1095,
                            "roundOpen": "2025-09-16",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": "tabnet_predictions-aasmtP7p7pQY.csv",
                            "id": "0cdc9db7-5f55-4d5c-a4d5-74e8aac0c852",
                            "roundCloseStaking": "2025-09-15",
                            "roundNumber": 1094,
                            "roundOpen": "2025-09-13",
                            "status": "on-time",
                            "timestamp": "2025-09-13T13:09:06Z"
                        },
                        {
                            "filename": "tabnet_predictions-FIjdgxsga83y.csv",
                            "id": "b8b69204-914c-4b91-a790-0a452310de8d",
                            "roundCloseStaking": "2025-09-12",
                            "roundNumber": 1093,
                            "roundOpen": "2025-09-12",
                            "status": "on-time",
                            "timestamp": "2025-09-12T13:08:30Z"
                        },
                        {
                            "filename": "tabnet_predictions-nhowjYr8ZdJo.csv",
                            "id": "4f9f89ad-f08e-4499-8507-b06eb171bb9e",
                            "roundCloseStaking": "2025-09-11",
                            "roundNumber": 1092,
                            "roundOpen": "2025-09-11",
                            "status": "on-time",
                            "timestamp": "2025-09-11T13:10:34Z"
                        },
                        {
                            "filename": "tabnet_predictions-74eG6InLVlwb.csv",
                            "id": "b1b52f9f-b467-441f-af12-6af9f34581a9",
                            "roundCloseStaking": "2025-09-10",
                            "roundNumber": 1091,
                            "roundOpen": "2025-09-10",
                            "status": "on-time",
                            "timestamp": "2025-09-10T13:08:21Z"
                        },
                        {
                            "filename": "tabnet_predictions-sS9INu0PujWS.csv",
                            "id": "e8e38fc7-0853-4c07-8d2b-6e30c2f8930f",
                            "roundCloseStaking": "2025-09-09",
                            "roundNumber": 1090,
                            "roundOpen": "2025-09-09",
                            "status": "on-time",
                            "timestamp": "2025-09-09T13:10:40Z"
                        },
                        {
                            "filename": "tabnet_predictions-iqFrOeeEgEvZ.csv",
                            "id": "a99f817e-70fe-4120-b7e9-3b5e2bf9d35f",
                            "roundCloseStaking": "2025-09-08",
                            "roundNumber": 1089,
                            "roundOpen": "2025-09-06",
                            "status": "on-time",
                            "timestamp": "2025-09-06T13:09:00Z"
                        },
                        {
                            "filename": "tabnet_predictions-21spcvGTpZ7F.csv",
                            "id": "11f8f385-2168-4131-8cdb-0b8592cc5285",
                            "roundCloseStaking": "2025-09-05",
                            "roundNumber": 1088,
                            "roundOpen": "2025-09-05",
                            "status": "on-time",
                            "timestamp": "2025-09-05T13:10:33Z"
                        },
                        {
                            "filename": "tabnet_predictions-yPPQ31Nu49jc.csv",
                            "id": "6d8462e9-d780-40fc-b24d-07ac0f824819",
                            "roundCloseStaking": "2025-09-04",
                            "roundNumber": 1087,
                            "roundOpen": "2025-09-04",
                            "status": "on-time",
                            "timestamp": "2025-09-04T13:10:37Z"
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-03",
                            "roundNumber": 1086,
                            "roundOpen": "2025-09-03",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": "tabnet_predictions-YhTOSIE3BDIt.csv",
                            "id": "746fc71b-1b8f-4773-a250-36b8cb141077",
                            "roundCloseStaking": "2025-09-02",
                            "roundNumber": 1085,
                            "roundOpen": "2025-09-02",
                            "status": "on-time",
                            "timestamp": "2025-09-02T13:20:10Z"
                        },
                        {
                            "filename": "tabnet_predictions-hz7nqVr1ZTeh.csv",
                            "id": "7516c124-cf6f-42be-ab3e-04b41a0ad8c6",
                            "roundCloseStaking": "2025-09-01",
                            "roundNumber": 1084,
                            "roundOpen": "2025-08-30",
                            "status": "on-time",
                            "timestamp": "2025-08-30T13:10:58Z"
                        },
                        {
                            "filename": "tabnet_predictions-OI5vWv4We3tq.csv",
                            "id": "85c17ef1-72f4-4f68-9be4-6cc27ad604bf",
                            "roundCloseStaking": "2025-08-29",
                            "roundNumber": 1083,
                            "roundOpen": "2025-08-29",
                            "status": "on-time",
                            "timestamp": "2025-08-29T13:09:58Z"
                        },
                        {
                            "filename": "tabnet_predictions-2eA0XXojOO5Q.csv",
                            "id": "144c61c1-a2d8-4da8-a975-3589ed96b19b",
                            "roundCloseStaking": "2025-08-28",
                            "roundNumber": 1082,
                            "roundOpen": "2025-08-28",
                            "status": "on-time",
                            "timestamp": "2025-08-28T13:12:34Z"
                        },
                        {
                            "filename": "tabnet_predictions-YkJ6JOgFBZIQ.csv",
                            "id": "90800247-be6f-40de-a922-f3a26cbe188d",
                            "roundCloseStaking": "2025-08-27",
                            "roundNumber": 1081,
                            "roundOpen": "2025-08-27",
                            "status": "on-time",
                            "timestamp": "2025-08-27T13:10:28Z"
                        },
                        {
                            "filename": "tabnet_predictions-H6JGMwYbDcYm.csv",
                            "id": "2b8deb1e-9d3a-415b-b15f-fa5abbd41424",
                            "roundCloseStaking": "2025-08-26",
                            "roundNumber": 1080,
                            "roundOpen": "2025-08-26",
                            "status": "on-time",
                            "timestamp": "2025-08-26T13:10:30Z"
                        },
                        {
                            "filename": "tabnet_predictions-bX9AcN3FrfJZ.csv",
                            "id": "b2749786-712c-4f0c-952c-3ad4f910291e",
                            "roundCloseStaking": "2025-08-25",
                            "roundNumber": 1079,
                            "roundOpen": "2025-08-23",
                            "status": "on-time",
                            "timestamp": "2025-08-23T13:10:46Z"
                        },
                        {
                            "filename": "tabnet_predictions-TMbDsyNuHlen.csv",
                            "id": "56ab86a3-969d-4fd6-8289-00d35d1be964",
                            "roundCloseStaking": "2025-08-22",
                            "roundNumber": 1078,
                            "roundOpen": "2025-08-22",
                            "status": "on-time",
                            "timestamp": "2025-08-22T13:10:44Z"
                        },
                        {
                            "filename": "tabnet_predictions-xnHE4oCCl90k.csv",
                            "id": "097605f0-6dcf-48a7-89cb-59a913a0ef34",
                            "roundCloseStaking": "2025-08-21",
                            "roundNumber": 1077,
                            "roundOpen": "2025-08-21",
                            "status": "on-time",
                            "timestamp": "2025-08-21T13:07:28Z"
                        },
                        {
                            "filename": "tabnet_predictions-5q3rOo4bXsL4.csv",
                            "id": "ba937c51-be6d-42b0-95a1-739f8654fc5d",
                            "roundCloseStaking": "2025-08-20",
                            "roundNumber": 1076,
                            "roundOpen": "2025-08-20",
                            "status": "on-time",
                            "timestamp": "2025-08-20T13:07:50Z"
                        },
                        {
                            "filename": "tabnet_predictions-LChnkLkTVIrO.csv",
                            "id": "953d51e6-6c88-4cfb-a9c3-593b52f572ff",
                            "roundCloseStaking": "2025-08-19",
                            "roundNumber": 1075,
                            "roundOpen": "2025-08-19",
                            "status": "on-time",
                            "timestamp": "2025-08-19T13:07:35Z"
                        },
                        {
                            "filename": "tabnet_predictions-BZjbWcWkbydX.csv",
                            "id": "217e2150-f991-449c-8e59-b38b81b92a4a",
                            "roundCloseStaking": "2025-08-18",
                            "roundNumber": 1074,
                            "roundOpen": "2025-08-16",
                            "status": "on-time",
                            "timestamp": "2025-08-16T13:05:07Z"
                        },
                        {
                            "filename": "tabnet_predictions-c0lBao6n3kOq.csv",
                            "id": "c87ed291-3baf-40d7-8f7f-634557b16dbb",
                            "roundCloseStaking": "2025-08-15",
                            "roundNumber": 1073,
                            "roundOpen": "2025-08-15",
                            "status": "on-time",
                            "timestamp": "2025-08-15T13:07:16Z"
                        },
                        {
                            "filename": "tabnet_predictions-5p7QrkYru0ij.csv",
                            "id": "aec4d324-5f20-41a4-bd9b-4787ab3da6ed",
                            "roundCloseStaking": "2025-08-14",
                            "roundNumber": 1072,
                            "roundOpen": "2025-08-14",
                            "status": "on-time",
                            "timestamp": "2025-08-14T13:07:34Z"
                        },
                        {
                            "filename": "tabnet_predictions-am6Hu1Q3br6x.csv",
                            "id": "405a18c8-398f-4cc1-84ea-30d72844012f",
                            "roundCloseStaking": "2025-08-13",
                            "roundNumber": 1071,
                            "roundOpen": "2025-08-13",
                            "status": "on-time",
                            "timestamp": "2025-08-13T13:07:39Z"
                        },
                        {
                            "filename": "tabnet_predictions-6NUalewZQvul.csv",
                            "id": "b992334c-2531-4b47-8c4f-c71a88694039",
                            "roundCloseStaking": "2025-08-12",
                            "roundNumber": 1070,
                            "roundOpen": "2025-08-12",
                            "status": "on-time",
                            "timestamp": "2025-08-12T13:07:41Z"
                        },
                        {
                            "filename": "tabnet_predictions-lnxGgNCxvS0a.csv",
                            "id": "1fce1c08-b726-4938-82b8-8a9d146e08c3",
                            "roundCloseStaking": "2025-08-11",
                            "roundNumber": 1069,
                            "roundOpen": "2025-08-09",
                            "status": "on-time",
                            "timestamp": "2025-08-09T13:07:07Z"
                        },
                        {
                            "filename": "tabnet_predictions-OFmRcigg6Pu4.csv",
                            "id": "6c695ddb-64d6-4dfc-934f-6ffe18ae2842",
                            "roundCloseStaking": "2025-08-08",
                            "roundNumber": 1068,
                            "roundOpen": "2025-08-08",
                            "status": "on-time",
                            "timestamp": "2025-08-08T13:07:38Z"
                        },
                        {
                            "filename": "tabnet_predictions-luGp8L27aS4R.csv",
                            "id": "e96e1f6d-6cca-4a07-a97a-9d282f6673fd",
                            "roundCloseStaking": "2025-08-07",
                            "roundNumber": 1067,
                            "roundOpen": "2025-08-07",
                            "status": "on-time",
                            "timestamp": "2025-08-07T13:11:29Z"
                        },
                        {
                            "filename": "tabnet_predictions-BwYeHMIcldmq.csv",
                            "id": "c06c50d0-acb1-4f3c-82a3-efd2f036edf3",
                            "roundCloseStaking": "2025-08-06",
                            "roundNumber": 1066,
                            "roundOpen": "2025-08-06",
                            "status": "late",
                            "timestamp": "2025-08-06T14:16:24Z"
                        },
                        {
                            "filename": "tabnet_predictions-aNTa3QZ68QGf.csv",
                            "id": "0bd74922-18bc-4cfe-9b11-5847f0e57c50",
                            "roundCloseStaking": "2025-08-05",
                            "roundNumber": 1065,
                            "roundOpen": "2025-08-05",
                            "status": "on-time",
                            "timestamp": "2025-08-05T13:07:46Z"
                        },
                        {
                            "filename": "tabnet_predictions-8f8J7SAXLlKk.csv",
                            "id": "c984996c-84e9-489c-8c05-22b12efd23c1",
                            "roundCloseStaking": "2025-08-04",
                            "roundNumber": 1064,
                            "roundOpen": "2025-08-02",
                            "status": "on-time",
                            "timestamp": "2025-08-02T13:19:47Z"
                        },
                        {
                            "filename": "tabnet_predictions-kGZy07O3rkDk.csv",
                            "id": "cabfb7d6-1bc8-4aea-b15d-4ebb55436ff9",
                            "roundCloseStaking": "2025-08-01",
                            "roundNumber": 1063,
                            "roundOpen": "2025-08-01",
                            "status": "on-time",
                            "timestamp": "2025-08-01T13:08:45Z"
                        },
                        {
                            "filename": "tabnet_predictions-TcACaDrB5J0l.csv",
                            "id": "81e4325d-5a23-421f-b301-2bda9bc1f53e",
                            "roundCloseStaking": "2025-07-31",
                            "roundNumber": 1062,
                            "roundOpen": "2025-07-31",
                            "status": "on-time",
                            "timestamp": "2025-07-31T13:08:48Z"
                        },
                        {
                            "filename": "tabnet_predictions-HTRKPG90pYP9.csv",
                            "id": "aa292dd3-3570-4690-99a7-42de8cd17370",
                            "roundCloseStaking": "2025-07-30",
                            "roundNumber": 1061,
                            "roundOpen": "2025-07-30",
                            "status": "on-time",
                            "timestamp": "2025-07-30T13:07:56Z"
                        },
                        {
                            "filename": "tabnet_predictions-E4bkcXbo4J2c.csv",
                            "id": "82d679a5-d965-409a-92c2-9b59f47f97c3",
                            "roundCloseStaking": "2025-07-29",
                            "roundNumber": 1060,
                            "roundOpen": "2025-07-29",
                            "status": "on-time",
                            "timestamp": "2025-07-29T13:09:40Z"
                        },
                        {
                            "filename": "tabnet_predictions-nXjxQVQBRD1g.csv",
                            "id": "56875172-5d76-489c-8c85-25352f4811bb",
                            "roundCloseStaking": "2025-07-28",
                            "roundNumber": 1059,
                            "roundOpen": "2025-07-26",
                            "status": "on-time",
                            "timestamp": "2025-07-26T13:07:52Z"
                        },
                        {
                            "filename": "tabnet_predictions-U0mhd39jJGWe.csv",
                            "id": "85005ac6-143a-4366-9f2a-b60564dab667",
                            "roundCloseStaking": "2025-07-25",
                            "roundNumber": 1058,
                            "roundOpen": "2025-07-25",
                            "status": "on-time",
                            "timestamp": "2025-07-25T13:07:57Z"
                        },
                        {
                            "filename": "tabnet_predictions-CO2SifD5c7iH.csv",
                            "id": "3a282312-c0b7-43fa-bfb2-672b63fa8fd3",
                            "roundCloseStaking": "2025-07-24",
                            "roundNumber": 1057,
                            "roundOpen": "2025-07-24",
                            "status": "on-time",
                            "timestamp": "2025-07-24T13:07:24Z"
                        },
                        {
                            "filename": "tabnet_predictions-BXx8kS8OMo9q.csv",
                            "id": "5b1a7bb1-87f0-481a-8b2c-f53183e24422",
                            "roundCloseStaking": "2025-07-23",
                            "roundNumber": 1056,
                            "roundOpen": "2025-07-23",
                            "status": "on-time",
                            "timestamp": "2025-07-23T13:07:59Z"
                        },
                        {
                            "filename": "tabnet_predictions-siunnCAhKX4V.csv",
                            "id": "b1d05a49-7bd2-47f2-94a7-948d8e5d15e5",
                            "roundCloseStaking": "2025-07-22",
                            "roundNumber": 1055,
                            "roundOpen": "2025-07-22",
                            "status": "on-time",
                            "timestamp": "2025-07-22T13:10:28Z"
                        },
                        {
                            "filename": "tabnet_predictions-WHQOM2CkfgPW.csv",
                            "id": "a5cb0e09-8024-458a-a304-dcce7e3dc6c5",
                            "roundCloseStaking": "2025-07-21",
                            "roundNumber": 1054,
                            "roundOpen": "2025-07-19",
                            "status": "on-time",
                            "timestamp": "2025-07-19T13:07:36Z"
                        },
                        {
                            "filename": "tabnet_predictions-c1V6OOsWk024.csv",
                            "id": "af6b323f-aedd-4d3a-b5a7-baf6fd36b85d",
                            "roundCloseStaking": "2025-07-18",
                            "roundNumber": 1053,
                            "roundOpen": "2025-07-18",
                            "status": "on-time",
                            "timestamp": "2025-07-18T13:07:31Z"
                        },
                        {
                            "filename": "tabnet_predictions-5i7aVEhbAsPW.csv",
                            "id": "f56389c2-8b5c-4fd3-9a86-73ca4fc3577a",
                            "roundCloseStaking": "2025-07-17",
                            "roundNumber": 1052,
                            "roundOpen": "2025-07-17",
                            "status": "on-time",
                            "timestamp": "2025-07-17T13:14:32Z"
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-16",
                            "roundNumber": 1051,
                            "roundOpen": "2025-07-16",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": "tabnet_predictions-sCOHMW1Siov5.csv",
                            "id": "71b5041e-ef19-4cfd-a917-8a92f8c96c98",
                            "roundCloseStaking": "2025-07-15",
                            "roundNumber": 1050,
                            "roundOpen": "2025-07-15",
                            "status": "on-time",
                            "timestamp": "2025-07-15T13:05:29Z"
                        },
                        {
                            "filename": "tabnet_predictions-Nq70S76copMs.csv",
                            "id": "cb29c338-6785-48ce-a76b-a2269eb74afd",
                            "roundCloseStaking": "2025-07-14",
                            "roundNumber": 1049,
                            "roundOpen": "2025-07-12",
                            "status": "on-time",
                            "timestamp": "2025-07-12T13:55:40Z"
                        },
                        {
                            "filename": "tabnet_predictions-893SuDiXx0fx.csv",
                            "id": "83b9a316-5230-421b-bd49-3faa3ad774bc",
                            "roundCloseStaking": "2025-07-11",
                            "roundNumber": 1048,
                            "roundOpen": "2025-07-11",
                            "status": "on-time",
                            "timestamp": "2025-07-11T13:00:34Z"
                        },
                        {
                            "filename": "tabnet_predictions-511Uq2oSg6PS.csv",
                            "id": "bc788ed5-2089-4134-be87-a1bc39d2ec13",
                            "roundCloseStaking": "2025-07-10",
                            "roundNumber": 1047,
                            "roundOpen": "2025-07-10",
                            "status": "on-time",
                            "timestamp": "2025-07-10T13:07:27Z"
                        },
                        {
                            "filename": "tabnet_predictions-nJvS0PnnF5jd.csv",
                            "id": "3d6456a2-6c01-4d84-8d22-bf302e2a5d76",
                            "roundCloseStaking": "2025-07-09",
                            "roundNumber": 1046,
                            "roundOpen": "2025-07-09",
                            "status": "on-time",
                            "timestamp": "2025-07-09T13:07:31Z"
                        },
                        {
                            "filename": "tabnet_predictions-kzJlhg5VGrkQ.csv",
                            "id": "5f480429-b123-4331-958d-8ae0ae5fd6cd",
                            "roundCloseStaking": "2025-07-08",
                            "roundNumber": 1045,
                            "roundOpen": "2025-07-08",
                            "status": "on-time",
                            "timestamp": "2025-07-08T13:54:47Z"
                        },
                        {
                            "filename": "tabnet_predictions-FVWhFhoZAliM.csv",
                            "id": "be3d8bc4-8bcb-47be-a61c-be18d66398fc",
                            "roundCloseStaking": "2025-07-07",
                            "roundNumber": 1044,
                            "roundOpen": "2025-07-05",
                            "status": "late",
                            "timestamp": "2025-07-07T20:32:51Z"
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-04",
                            "roundNumber": 1043,
                            "roundOpen": "2025-07-04",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-03",
                            "roundNumber": 1042,
                            "roundOpen": "2025-07-03",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-02",
                            "roundNumber": 1041,
                            "roundOpen": "2025-07-02",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-01",
                            "roundNumber": 1040,
                            "roundOpen": "2025-07-01",
                            "status": "none",
                            "timestamp": null
                        }
                    ],
                    "latestUserScores": [
                        {
                            "displayName": "apcwnm",
                            "reputation": 0.019263588842195496
                        },
                        {
                            "displayName": "bmc",
                            "reputation": 0.0014293661637691602
                        },
                        {
                            "displayName": "canon_bmc",
                            "reputation": 0.001336265685669253
                        },
                        {
                            "displayName": "canon_corr",
                            "reputation": 0.0011841663150864664
                        },
                        {
                            "displayName": "canon_cort20",
                            "reputation": 1.9129533174306083e-4
                        },
                        {
                            "displayName": "canon_fnc_v3",
                            "reputation": 2.947894388159064e-4
                        },
                        {
                            "displayName": "canon_mmc",
                            "reputation": 0.0012130720847669469
                        },
                        {
                            "displayName": "corr_w_meta_model",
                            "reputation": 0.18303316023562394
                        },
                        {
                            "displayName": "cort20",
                            "reputation": 2.0378808810179132e-4
                        },
                        {
                            "displayName": "fnc_v3",
                            "reputation": 3.14040994003884e-4
                        },
                        {
                            "displayName": "mcwnm",
                            "reputation": 0.08376612059814176
                        },
                        {
                            "displayName": "mmc",
                            "reputation": 0.001292293118874176
                        },
                        {
                            "displayName": "season_score",
                            "reputation": 0.0030182273270771267
                        },
                        {
                            "displayName": "v2_corr20",
                            "reputation": 0.0012614996254594602
                        }
                    ],
                    "name": "fnc_t1_eb91",
                    "profileUrl": "https://numerai-public-images.s3-us-west-2.amazonaws.com/profile_images_originals/terminator4-YYtIh3pCWGpv.jpg",
                    "returns": {
                        "allTime": 0.097277890377826,
                        "oneDay": 1.5599331441504585,
                        "oneYear": null,
                        "threeMonths": null
                    },
                    "submissionWebhook": "https://numerai.imperialai.ai/numerai-eb9fa1ab-0d67-4970-b477-c9c0e7bcac5e/",
                    "tournament": 8,
                    "v2Stake": {
                        "latestValue": "10.000000000000000000",
                        "latestValueSettled": "10.000000000000000000",
                        "pendingV2ChangeStakeRequest": null,
                        "stakeValue": "10.000972778903778260",
                        "status": null
                    }
                },
                {
                    "computeEnabled": false,
                    "computePickleUpload": {
                        "id": "075ebb57-6f12-4364-aab9-8204b2028525"
                    },
                    "currentPayoutSelection": {
                        "corrMultiplier": 0.5,
                        "mmcMultiplier": 2.0,
                        "takeProfit": false,
                        "updatedAt": null
                    },
                    "description": null,
                    "earliestReleaseDate": "2025-10-24T00:00:00Z",
                    "id": "5067acd8-df58-410d-bbc2-00152b836dd6",
                    "isComputeWeekdayEnabled": true,
                    "latestSubmissions": [
                        {
                            "filename": "predictions-LjrQNrB7Bzln.csv",
                            "id": "d34bb384-51e1-40b3-bba4-26881f2b5ef6",
                            "roundCloseStaking": "2025-09-23",
                            "roundNumber": 1100,
                            "roundOpen": "2025-09-23",
                            "status": "on-time",
                            "timestamp": "2025-09-23T13:33:29Z"
                        },
                        {
                            "filename": "predictions-NmwK6gZPkorW.csv",
                            "id": "acbbc58e-d205-420a-843a-c87f38bfc131",
                            "roundCloseStaking": "2025-09-22",
                            "roundNumber": 1099,
                            "roundOpen": "2025-09-20",
                            "status": "on-time",
                            "timestamp": "2025-09-20T13:27:48Z"
                        },
                        {
                            "filename": "predictions-QQfc9KKLJyCp.csv",
                            "id": "60abb1a5-9d80-427c-8eae-2019be217ad9",
                            "roundCloseStaking": "2025-09-19",
                            "roundNumber": 1098,
                            "roundOpen": "2025-09-19",
                            "status": "on-time",
                            "timestamp": "2025-09-19T13:27:48Z"
                        },
                        {
                            "filename": "predictions-AXfJcCz6ubZd.csv",
                            "id": "d409a8e5-722b-4314-94e6-426cb8a1f69e",
                            "roundCloseStaking": "2025-09-18",
                            "roundNumber": 1097,
                            "roundOpen": "2025-09-18",
                            "status": "on-time",
                            "timestamp": "2025-09-18T13:23:43Z"
                        },
                        {
                            "filename": "predictions-GsCWQ43rS9vP.csv",
                            "id": "c52d0f93-2a03-4f66-81ff-3b004561091d",
                            "roundCloseStaking": "2025-09-17",
                            "roundNumber": 1096,
                            "roundOpen": "2025-09-17",
                            "status": "on-time",
                            "timestamp": "2025-09-17T13:28:18Z"
                        },
                        {
                            "filename": "predictions-MlSdoZmxV3wh.csv",
                            "id": "88674e46-1a33-461e-9cb5-c0e8640306b9",
                            "roundCloseStaking": "2025-09-16",
                            "roundNumber": 1095,
                            "roundOpen": "2025-09-16",
                            "status": "on-time",
                            "timestamp": "2025-09-16T13:28:09Z"
                        },
                        {
                            "filename": "predictions-3OCOgOdYTkkd.csv",
                            "id": "091c0dac-f934-4ba1-b126-65b4a6699b58",
                            "roundCloseStaking": "2025-09-15",
                            "roundNumber": 1094,
                            "roundOpen": "2025-09-13",
                            "status": "on-time",
                            "timestamp": "2025-09-13T13:34:37Z"
                        },
                        {
                            "filename": "predictions-7zwP8WFZFwBn.csv",
                            "id": "c0f8e65b-f587-41e9-9250-35171ee34825",
                            "roundCloseStaking": "2025-09-12",
                            "roundNumber": 1093,
                            "roundOpen": "2025-09-12",
                            "status": "on-time",
                            "timestamp": "2025-09-12T13:26:02Z"
                        },
                        {
                            "filename": "predictions-y1qoAR9AbLBK.csv",
                            "id": "2b99f8e3-9212-4823-ac00-3ffc9fd9c2bb",
                            "roundCloseStaking": "2025-09-11",
                            "roundNumber": 1092,
                            "roundOpen": "2025-09-11",
                            "status": "on-time",
                            "timestamp": "2025-09-11T13:28:44Z"
                        },
                        {
                            "filename": "predictions-fY7gk9kN92qr.csv",
                            "id": "cd56d2f9-1aaf-494b-8c65-153dfbc5b679",
                            "roundCloseStaking": "2025-09-10",
                            "roundNumber": 1091,
                            "roundOpen": "2025-09-10",
                            "status": "on-time",
                            "timestamp": "2025-09-10T13:27:32Z"
                        },
                        {
                            "filename": "predictions-M2OwgIlg460c.csv",
                            "id": "857f42ad-eba4-4a05-ae46-7a1b65dcc2a7",
                            "roundCloseStaking": "2025-09-09",
                            "roundNumber": 1090,
                            "roundOpen": "2025-09-09",
                            "status": "on-time",
                            "timestamp": "2025-09-09T13:29:23Z"
                        },
                        {
                            "filename": "predictions-RhNu3hThoaVe.csv",
                            "id": "5ad2c2c0-f612-4087-b50b-2a7ee53afd95",
                            "roundCloseStaking": "2025-09-08",
                            "roundNumber": 1089,
                            "roundOpen": "2025-09-06",
                            "status": "on-time",
                            "timestamp": "2025-09-06T13:32:30Z"
                        },
                        {
                            "filename": "predictions-S3uSHTHUne3Q.csv",
                            "id": "e960a47d-3eb3-4409-b65d-bee6e9ebd5b1",
                            "roundCloseStaking": "2025-09-05",
                            "roundNumber": 1088,
                            "roundOpen": "2025-09-05",
                            "status": "on-time",
                            "timestamp": "2025-09-05T13:25:43Z"
                        },
                        {
                            "filename": "predictions-rlghYt3ewVXs.csv",
                            "id": "57c0e5f7-3f1f-48e3-b0f2-68ad1dd34e0c",
                            "roundCloseStaking": "2025-09-04",
                            "roundNumber": 1087,
                            "roundOpen": "2025-09-04",
                            "status": "on-time",
                            "timestamp": "2025-09-04T13:26:07Z"
                        },
                        {
                            "filename": "predictions-lqQ7BBYAmAc4.csv",
                            "id": "68dbfdef-d83a-48d4-838c-617650dd9be9",
                            "roundCloseStaking": "2025-09-03",
                            "roundNumber": 1086,
                            "roundOpen": "2025-09-03",
                            "status": "on-time",
                            "timestamp": "2025-09-03T13:33:06Z"
                        },
                        {
                            "filename": "predictions-7XTcM3sbCixD.csv",
                            "id": "6f423dd5-ca6a-49c1-a475-35192df0c83d",
                            "roundCloseStaking": "2025-09-02",
                            "roundNumber": 1085,
                            "roundOpen": "2025-09-02",
                            "status": "on-time",
                            "timestamp": "2025-09-02T13:35:47Z"
                        },
                        {
                            "filename": "predictions-sMCZvSK51RvX.csv",
                            "id": "53c5d14d-3fd6-442b-9f81-c3f555f45055",
                            "roundCloseStaking": "2025-09-01",
                            "roundNumber": 1084,
                            "roundOpen": "2025-08-30",
                            "status": "on-time",
                            "timestamp": "2025-08-30T13:29:11Z"
                        },
                        {
                            "filename": "predictions-QwAQLJYEyPHg.csv",
                            "id": "257ae94f-c203-4553-b038-7dc2c8ebe9a1",
                            "roundCloseStaking": "2025-08-29",
                            "roundNumber": 1083,
                            "roundOpen": "2025-08-29",
                            "status": "on-time",
                            "timestamp": "2025-08-29T13:34:56Z"
                        },
                        {
                            "filename": "predictions-yR8s9EVJusgA.csv",
                            "id": "0d70dc7c-808d-4194-9198-0c072cffe6e8",
                            "roundCloseStaking": "2025-08-28",
                            "roundNumber": 1082,
                            "roundOpen": "2025-08-28",
                            "status": "on-time",
                            "timestamp": "2025-08-28T13:30:44Z"
                        },
                        {
                            "filename": "predictions-7H7thiBT3vnk.csv",
                            "id": "55340fd9-38fe-4754-a19d-c490be6b6272",
                            "roundCloseStaking": "2025-08-27",
                            "roundNumber": 1081,
                            "roundOpen": "2025-08-27",
                            "status": "on-time",
                            "timestamp": "2025-08-27T13:25:22Z"
                        },
                        {
                            "filename": "predictions-FJ3wUTnOWzUE.csv",
                            "id": "93c17d2a-fe59-4667-ad9c-4def3e7c680f",
                            "roundCloseStaking": "2025-08-26",
                            "roundNumber": 1080,
                            "roundOpen": "2025-08-26",
                            "status": "on-time",
                            "timestamp": "2025-08-26T13:29:30Z"
                        },
                        {
                            "filename": "predictions-0mfhHmozFyGN.csv",
                            "id": "47deccb6-8b2e-4390-9fb1-f99126e400a9",
                            "roundCloseStaking": "2025-08-25",
                            "roundNumber": 1079,
                            "roundOpen": "2025-08-23",
                            "status": "on-time",
                            "timestamp": "2025-08-23T13:25:48Z"
                        },
                        {
                            "filename": "predictions-9MPdDhIYowWb.csv",
                            "id": "254d801f-ac3c-43b4-847f-3727305e1eb8",
                            "roundCloseStaking": "2025-08-22",
                            "roundNumber": 1078,
                            "roundOpen": "2025-08-22",
                            "status": "on-time",
                            "timestamp": "2025-08-22T13:20:10Z"
                        },
                        {
                            "filename": "predictions-G32hn0aExlyV.csv",
                            "id": "0b8d7a6d-893b-4e6e-93fd-7793ee2aff18",
                            "roundCloseStaking": "2025-08-21",
                            "roundNumber": 1077,
                            "roundOpen": "2025-08-21",
                            "status": "on-time",
                            "timestamp": "2025-08-21T13:26:37Z"
                        },
                        {
                            "filename": "predictions-QAEVQhou3eaa.csv",
                            "id": "2461bf8b-f674-4d94-b16f-2a6bd7938dbc",
                            "roundCloseStaking": "2025-08-20",
                            "roundNumber": 1076,
                            "roundOpen": "2025-08-20",
                            "status": "on-time",
                            "timestamp": "2025-08-20T13:31:46Z"
                        },
                        {
                            "filename": "predictions-ZBWqXUERiWDn.csv",
                            "id": "eaece709-a69c-4ffd-8c0c-9768c0352e1e",
                            "roundCloseStaking": "2025-08-19",
                            "roundNumber": 1075,
                            "roundOpen": "2025-08-19",
                            "status": "on-time",
                            "timestamp": "2025-08-19T13:27:26Z"
                        },
                        {
                            "filename": "predictions-aQVwzVFnTTPd.csv",
                            "id": "419fdf0c-d3f2-4a65-a053-fbca79ffd556",
                            "roundCloseStaking": "2025-08-18",
                            "roundNumber": 1074,
                            "roundOpen": "2025-08-16",
                            "status": "on-time",
                            "timestamp": "2025-08-16T13:25:50Z"
                        },
                        {
                            "filename": "predictions-K1ILHZTevtXv.csv",
                            "id": "47d8a575-82e0-4840-9a2c-514ef78b5acf",
                            "roundCloseStaking": "2025-08-15",
                            "roundNumber": 1073,
                            "roundOpen": "2025-08-15",
                            "status": "on-time",
                            "timestamp": "2025-08-15T13:29:24Z"
                        },
                        {
                            "filename": "predictions-16Danlg3Rn80.csv",
                            "id": "1946ec82-b032-4dd8-81d0-b58dcb1428f2",
                            "roundCloseStaking": "2025-08-14",
                            "roundNumber": 1072,
                            "roundOpen": "2025-08-14",
                            "status": "on-time",
                            "timestamp": "2025-08-14T13:27:03Z"
                        },
                        {
                            "filename": "predictions-ZCHewhHKrMbX.csv",
                            "id": "914bb23b-44f3-4668-b1a9-e35e9368a2f5",
                            "roundCloseStaking": "2025-08-13",
                            "roundNumber": 1071,
                            "roundOpen": "2025-08-13",
                            "status": "on-time",
                            "timestamp": "2025-08-13T13:28:55Z"
                        },
                        {
                            "filename": "predictions-CcVyKeWdX61j.csv",
                            "id": "6d4b5663-c752-4579-80e8-5d3b91c02a5c",
                            "roundCloseStaking": "2025-08-12",
                            "roundNumber": 1070,
                            "roundOpen": "2025-08-12",
                            "status": "on-time",
                            "timestamp": "2025-08-12T13:27:56Z"
                        },
                        {
                            "filename": "predictions-uA1QpyDXjVga.csv",
                            "id": "25506453-6539-45d4-ab11-35d0b51dd90c",
                            "roundCloseStaking": "2025-08-11",
                            "roundNumber": 1069,
                            "roundOpen": "2025-08-09",
                            "status": "on-time",
                            "timestamp": "2025-08-09T13:25:58Z"
                        },
                        {
                            "filename": "predictions-0DxEu6dWGdIk.csv",
                            "id": "b94242fb-90e4-4557-8413-6d29438c3147",
                            "roundCloseStaking": "2025-08-08",
                            "roundNumber": 1068,
                            "roundOpen": "2025-08-08",
                            "status": "on-time",
                            "timestamp": "2025-08-08T13:20:51Z"
                        },
                        {
                            "filename": "predictions-SUgSIho9j2VB.csv",
                            "id": "e3b75a6f-3867-4cc4-bb51-c1f190835972",
                            "roundCloseStaking": "2025-08-07",
                            "roundNumber": 1067,
                            "roundOpen": "2025-08-07",
                            "status": "on-time",
                            "timestamp": "2025-08-07T13:29:46Z"
                        },
                        {
                            "filename": "predictions-FzzalnqZZ0iO.csv",
                            "id": "9402a0f9-a057-4cbb-9695-d672c7cd19c5",
                            "roundCloseStaking": "2025-08-06",
                            "roundNumber": 1066,
                            "roundOpen": "2025-08-06",
                            "status": "on-time",
                            "timestamp": "2025-08-06T13:26:40Z"
                        },
                        {
                            "filename": "predictions-RGe6W6Tem22k.csv",
                            "id": "3cc42554-2118-4948-b31a-150b4206c5ac",
                            "roundCloseStaking": "2025-08-05",
                            "roundNumber": 1065,
                            "roundOpen": "2025-08-05",
                            "status": "on-time",
                            "timestamp": "2025-08-05T13:30:08Z"
                        },
                        {
                            "filename": "predictions-WoLRsolzbNxo.csv",
                            "id": "7b8856d7-424d-43f0-9ac3-37c882e531a7",
                            "roundCloseStaking": "2025-08-04",
                            "roundNumber": 1064,
                            "roundOpen": "2025-08-02",
                            "status": "on-time",
                            "timestamp": "2025-08-02T13:37:26Z"
                        },
                        {
                            "filename": "predictions-bP5vX0ee7LiM.csv",
                            "id": "008cf601-54a1-4297-a66c-6626a4508476",
                            "roundCloseStaking": "2025-08-01",
                            "roundNumber": 1063,
                            "roundOpen": "2025-08-01",
                            "status": "on-time",
                            "timestamp": "2025-08-01T13:23:38Z"
                        },
                        {
                            "filename": "predictions-YK4XBziiRIjr.csv",
                            "id": "61b32971-108c-4302-a7bb-0c58e6170499",
                            "roundCloseStaking": "2025-07-31",
                            "roundNumber": 1062,
                            "roundOpen": "2025-07-31",
                            "status": "on-time",
                            "timestamp": "2025-07-31T13:25:04Z"
                        },
                        {
                            "filename": "predictions-1HUtOSHFw7Hs.csv",
                            "id": "ff211262-4c9e-4fce-b4c0-cf91823d3353",
                            "roundCloseStaking": "2025-07-30",
                            "roundNumber": 1061,
                            "roundOpen": "2025-07-30",
                            "status": "on-time",
                            "timestamp": "2025-07-30T13:22:21Z"
                        },
                        {
                            "filename": "predictions-xFYXhYHBesau.csv",
                            "id": "39dcec2c-a1ec-4f2e-bb27-d351c05378b5",
                            "roundCloseStaking": "2025-07-29",
                            "roundNumber": 1060,
                            "roundOpen": "2025-07-29",
                            "status": "on-time",
                            "timestamp": "2025-07-29T13:24:53Z"
                        },
                        {
                            "filename": "predictions-tO1Tsq7KecCC.csv",
                            "id": "319369bf-bd05-41bd-8ca7-e38f84e53f2a",
                            "roundCloseStaking": "2025-07-28",
                            "roundNumber": 1059,
                            "roundOpen": "2025-07-26",
                            "status": "on-time",
                            "timestamp": "2025-07-26T13:19:55Z"
                        },
                        {
                            "filename": "predictions-Kq1R9Ynfes9Z.csv",
                            "id": "e712e706-fb5b-468d-ba10-992b689927f4",
                            "roundCloseStaking": "2025-07-25",
                            "roundNumber": 1058,
                            "roundOpen": "2025-07-25",
                            "status": "on-time",
                            "timestamp": "2025-07-25T13:23:53Z"
                        },
                        {
                            "filename": "predictions-KGdC4RMJZvVT.csv",
                            "id": "3dfb8319-c8b7-4e93-b3b4-109f46d3e73e",
                            "roundCloseStaking": "2025-07-24",
                            "roundNumber": 1057,
                            "roundOpen": "2025-07-24",
                            "status": "on-time",
                            "timestamp": "2025-07-24T13:22:16Z"
                        },
                        {
                            "filename": "predictions-rMrmbQFlU7cI.csv",
                            "id": "41254257-be9e-44ff-9429-705615f89334",
                            "roundCloseStaking": "2025-07-23",
                            "roundNumber": 1056,
                            "roundOpen": "2025-07-23",
                            "status": "on-time",
                            "timestamp": "2025-07-23T13:24:36Z"
                        },
                        {
                            "filename": "predictions-YYuyxRqBuoCW.csv",
                            "id": "896201f6-8906-460f-9e6a-40c93e7fedff",
                            "roundCloseStaking": "2025-07-22",
                            "roundNumber": 1055,
                            "roundOpen": "2025-07-22",
                            "status": "on-time",
                            "timestamp": "2025-07-22T13:29:30Z"
                        },
                        {
                            "filename": "predictions-5wwiEmqhzBpW.csv",
                            "id": "5eec1393-da24-48ca-bf57-42c4da53aaed",
                            "roundCloseStaking": "2025-07-21",
                            "roundNumber": 1054,
                            "roundOpen": "2025-07-19",
                            "status": "on-time",
                            "timestamp": "2025-07-19T13:23:54Z"
                        },
                        {
                            "filename": "predictions-S0WIpPXUn2xK.csv",
                            "id": "4773a9b5-7742-467f-91d2-271e57896974",
                            "roundCloseStaking": "2025-07-18",
                            "roundNumber": 1053,
                            "roundOpen": "2025-07-18",
                            "status": "on-time",
                            "timestamp": "2025-07-18T13:24:02Z"
                        },
                        {
                            "filename": "predictions-kRRQ5ykO7EhM.csv",
                            "id": "89abc408-679c-4164-992c-7f3b9c1fcf1b",
                            "roundCloseStaking": "2025-07-17",
                            "roundNumber": 1052,
                            "roundOpen": "2025-07-17",
                            "status": "on-time",
                            "timestamp": "2025-07-17T13:24:20Z"
                        },
                        {
                            "filename": "predictions-Bgp4GfVn47iq.csv",
                            "id": "2301af16-a5c4-49c5-90fb-e61520261a3c",
                            "roundCloseStaking": "2025-07-16",
                            "roundNumber": 1051,
                            "roundOpen": "2025-07-16",
                            "status": "on-time",
                            "timestamp": "2025-07-16T13:25:34Z"
                        },
                        {
                            "filename": "predictions-k7SdtocwIByq.csv",
                            "id": "da796e02-19e5-4482-81ac-efd931860f2d",
                            "roundCloseStaking": "2025-07-15",
                            "roundNumber": 1050,
                            "roundOpen": "2025-07-15",
                            "status": "on-time",
                            "timestamp": "2025-07-15T13:21:22Z"
                        },
                        {
                            "filename": "predictions-VobFJDEMRMli.csv",
                            "id": "158ce3a0-12ba-44f3-8bfe-6078409cb682",
                            "roundCloseStaking": "2025-07-14",
                            "roundNumber": 1049,
                            "roundOpen": "2025-07-12",
                            "status": "on-time",
                            "timestamp": "2025-07-12T13:33:25Z"
                        },
                        {
                            "filename": "predictions-uivRQ7FdSpTX.csv",
                            "id": "9f790be5-0b85-43c4-95d1-392cf5798832",
                            "roundCloseStaking": "2025-07-11",
                            "roundNumber": 1048,
                            "roundOpen": "2025-07-11",
                            "status": "on-time",
                            "timestamp": "2025-07-11T13:27:32Z"
                        },
                        {
                            "filename": "predictions-9KqPubl76lkM.csv",
                            "id": "62c07faf-afff-486c-a583-6f7c581298a5",
                            "roundCloseStaking": "2025-07-10",
                            "roundNumber": 1047,
                            "roundOpen": "2025-07-10",
                            "status": "on-time",
                            "timestamp": "2025-07-10T13:23:59Z"
                        },
                        {
                            "filename": "predictions-EwvEgL58nLS8.csv",
                            "id": "ed9359c4-e1e7-476e-aacf-adf043be8779",
                            "roundCloseStaking": "2025-07-09",
                            "roundNumber": 1046,
                            "roundOpen": "2025-07-09",
                            "status": "on-time",
                            "timestamp": "2025-07-09T13:26:14Z"
                        },
                        {
                            "filename": "predictions-BMsL9T7n3tvz.csv",
                            "id": "5e4c0e04-b6db-4f4c-b745-6c163079e5f1",
                            "roundCloseStaking": "2025-07-08",
                            "roundNumber": 1045,
                            "roundOpen": "2025-07-08",
                            "status": "late",
                            "timestamp": "2025-07-08T21:16:31Z"
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-07",
                            "roundNumber": 1044,
                            "roundOpen": "2025-07-05",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-04",
                            "roundNumber": 1043,
                            "roundOpen": "2025-07-04",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-03",
                            "roundNumber": 1042,
                            "roundOpen": "2025-07-03",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-02",
                            "roundNumber": 1041,
                            "roundOpen": "2025-07-02",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-01",
                            "roundNumber": 1040,
                            "roundOpen": "2025-07-01",
                            "status": "none",
                            "timestamp": null
                        }
                    ],
                    "latestUserScores": [
                        {
                            "displayName": "apcwnm",
                            "reputation": 0.05629098032249405
                        },
                        {
                            "displayName": "bmc",
                            "reputation": 2.491500069090409e-4
                        },
                        {
                            "displayName": "canon_bmc",
                            "reputation": 2.3292184553948652e-4
                        },
                        {
                            "displayName": "canon_corr",
                            "reputation": 0.0015359734424022426
                        },
                        {
                            "displayName": "canon_cort20",
                            "reputation": 0.0011898615393790214
                        },
                        {
                            "displayName": "canon_fnc_v3",
                            "reputation": 7.326491712571561e-4
                        },
                        {
                            "displayName": "canon_mmc",
                            "reputation": -2.7758662113407985e-4
                        },
                        {
                            "displayName": "corr_w_meta_model",
                            "reputation": 0.5810418040906729
                        },
                        {
                            "displayName": "cort20",
                            "reputation": 0.0012675667827670393
                        },
                        {
                            "displayName": "fnc_v3",
                            "reputation": 7.804956477474193e-4
                        },
                        {
                            "displayName": "mcwnm",
                            "reputation": 0.1276048529554032
                        },
                        {
                            "displayName": "mmc",
                            "reputation": -2.9571472700406056e-4
                        },
                        {
                            "displayName": "season_score",
                            "reputation": 2.1281347893296158e-4
                        },
                        {
                            "displayName": "v2_corr20",
                            "reputation": 0.001636281912110144
                        }
                    ],
                    "name": "fnc_imp_e",
                    "profileUrl": "https://numerai-public-images.s3-us-west-2.amazonaws.com/profile_images/rock-WRHoX5TIDBu9.jpg",
                    "returns": {
                        "allTime": -0.1654127229749694,
                        "oneDay": 0.20371706985612845,
                        "oneYear": null,
                        "threeMonths": null
                    },
                    "submissionWebhook": null,
                    "tournament": 8,
                    "v2Stake": {
                        "latestValue": "1.000000000000000000",
                        "latestValueSettled": "1.000000000000000000",
                        "pendingV2ChangeStakeRequest": null,
                        "stakeValue": "0.998345872770250306",
                        "status": null
                    }
                },
                {
                    "computeEnabled": true,
                    "computePickleUpload": null,
                    "currentPayoutSelection": {
                        "corrMultiplier": 0.5,
                        "mmcMultiplier": 2.0,
                        "takeProfit": false,
                        "updatedAt": null
                    },
                    "description": null,
                    "earliestReleaseDate": "2025-10-16T00:00:00Z",
                    "id": "d6769cb7-f13a-45c9-a105-23048973d64c",
                    "isComputeWeekdayEnabled": true,
                    "latestSubmissions": [
                        {
                            "filename": "mmoe_ensemble_predictions_20250923_143007-n0vB8iZCVAsc.csv",
                            "id": "2d92f225-0a36-41e5-8066-2536725812bb",
                            "roundCloseStaking": "2025-09-24",
                            "roundNumber": 1101,
                            "roundOpen": "2025-09-24",
                            "status": "queued",
                            "timestamp": "2025-09-23T14:30:19Z"
                        },
                        {
                            "filename": "mmoe_ensemble_predictions_20250923_143007-n0vB8iZCVAsc.csv",
                            "id": "2d92f225-0a36-41e5-8066-2536725812bb",
                            "roundCloseStaking": "2025-09-23",
                            "roundNumber": 1100,
                            "roundOpen": "2025-09-23",
                            "status": "late",
                            "timestamp": "2025-09-23T14:30:19Z"
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-22",
                            "roundNumber": 1099,
                            "roundOpen": "2025-09-20",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-19",
                            "roundNumber": 1098,
                            "roundOpen": "2025-09-19",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-18",
                            "roundNumber": 1097,
                            "roundOpen": "2025-09-18",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-17",
                            "roundNumber": 1096,
                            "roundOpen": "2025-09-17",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-16",
                            "roundNumber": 1095,
                            "roundOpen": "2025-09-16",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": "mmoe_ensemble_predictions_20250913_130824-TKNNsM8xxda1.csv",
                            "id": "602fba88-b05e-4673-9bae-3461ecffb8d7",
                            "roundCloseStaking": "2025-09-15",
                            "roundNumber": 1094,
                            "roundOpen": "2025-09-13",
                            "status": "on-time",
                            "timestamp": "2025-09-13T13:08:58Z"
                        },
                        {
                            "filename": "mmoe_ensemble_predictions_20250912_130751-dcTmj5M7vNOe.csv",
                            "id": "6e1a23dd-8e46-45ba-9246-eaa8a0c73c88",
                            "roundCloseStaking": "2025-09-12",
                            "roundNumber": 1093,
                            "roundOpen": "2025-09-12",
                            "status": "on-time",
                            "timestamp": "2025-09-12T13:08:21Z"
                        },
                        {
                            "filename": "mmoe_ensemble_predictions_20250911_131006-7EaNM3Slpjq2.csv",
                            "id": "ac121147-51c1-4bb7-9835-faacbc4b5176",
                            "roundCloseStaking": "2025-09-11",
                            "roundNumber": 1092,
                            "roundOpen": "2025-09-11",
                            "status": "on-time",
                            "timestamp": "2025-09-11T13:10:26Z"
                        },
                        {
                            "filename": "mmoe_ensemble_predictions_20250910_130750-RzbUtC1n6BzR.csv",
                            "id": "07590a92-3a83-4a83-8c2d-ab8fc1ad037a",
                            "roundCloseStaking": "2025-09-10",
                            "roundNumber": 1091,
                            "roundOpen": "2025-09-10",
                            "status": "on-time",
                            "timestamp": "2025-09-10T13:08:20Z"
                        },
                        {
                            "filename": "mmoe_ensemble_predictions_20250909_131001-fkrUm4wAxNn7.csv",
                            "id": "fbbca1a8-164c-4668-baa8-65c5877ce425",
                            "roundCloseStaking": "2025-09-09",
                            "roundNumber": 1090,
                            "roundOpen": "2025-09-09",
                            "status": "on-time",
                            "timestamp": "2025-09-09T13:10:22Z"
                        },
                        {
                            "filename": "mmoe_ensemble_predictions_20250906_130820-oGmmfoLie3mb.csv",
                            "id": "4d43ce06-0f80-4411-a722-483918259bb1",
                            "roundCloseStaking": "2025-09-08",
                            "roundNumber": 1089,
                            "roundOpen": "2025-09-06",
                            "status": "on-time",
                            "timestamp": "2025-09-06T13:08:34Z"
                        },
                        {
                            "filename": "mmoe_ensemble_predictions_20250905_130953-Va8e5aeyXOTg.csv",
                            "id": "74e60ac9-a614-4d4c-acb6-394f7348e032",
                            "roundCloseStaking": "2025-09-05",
                            "roundNumber": 1088,
                            "roundOpen": "2025-09-05",
                            "status": "on-time",
                            "timestamp": "2025-09-05T13:10:04Z"
                        },
                        {
                            "filename": "mmoe_ensemble_predictions_20250904_131018-mOjii9pl4PZB.csv",
                            "id": "3757fc72-363d-4a8a-b872-67e1f67d50c2",
                            "roundCloseStaking": "2025-09-04",
                            "roundNumber": 1087,
                            "roundOpen": "2025-09-04",
                            "status": "on-time",
                            "timestamp": "2025-09-04T13:10:32Z"
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-03",
                            "roundNumber": 1086,
                            "roundOpen": "2025-09-03",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": "mmoe_ensemble_predictions_20250902_131737-y7g8Y3MxdUcp.csv",
                            "id": "ada400ae-b913-4701-abf0-040a97dac28e",
                            "roundCloseStaking": "2025-09-02",
                            "roundNumber": 1085,
                            "roundOpen": "2025-09-02",
                            "status": "on-time",
                            "timestamp": "2025-09-02T13:17:48Z"
                        },
                        {
                            "filename": "mmoe_ensemble_predictions_20250830_131034-PWxIOiUhLFpJ.csv",
                            "id": "fd9b9513-e541-40f6-895c-89a0e39587b7",
                            "roundCloseStaking": "2025-09-01",
                            "roundNumber": 1084,
                            "roundOpen": "2025-08-30",
                            "status": "on-time",
                            "timestamp": "2025-08-30T13:10:45Z"
                        },
                        {
                            "filename": "mmoe_ensemble_predictions_20250829_130927-ZYQDwZWg2zyD.csv",
                            "id": "f671fc55-aed0-4dbb-958a-c2e231c5025d",
                            "roundCloseStaking": "2025-08-29",
                            "roundNumber": 1083,
                            "roundOpen": "2025-08-29",
                            "status": "on-time",
                            "timestamp": "2025-08-29T13:09:39Z"
                        },
                        {
                            "filename": "mmoe_ensemble_predictions_20250828_131207-8C1L4GPyw1R4.csv",
                            "id": "1928e320-fa8d-4e95-aee5-d9441de57dfe",
                            "roundCloseStaking": "2025-08-28",
                            "roundNumber": 1082,
                            "roundOpen": "2025-08-28",
                            "status": "on-time",
                            "timestamp": "2025-08-28T13:12:18Z"
                        },
                        {
                            "filename": "mmoe_ensemble_predictions_20250827_131001-PDOnOmXesTwL.csv",
                            "id": "244dd781-1e0e-4e68-b9ad-7ae9798da0f2",
                            "roundCloseStaking": "2025-08-27",
                            "roundNumber": 1081,
                            "roundOpen": "2025-08-27",
                            "status": "on-time",
                            "timestamp": "2025-08-27T13:10:16Z"
                        },
                        {
                            "filename": "mmoe_ensemble_predictions_20250826_131002-cIFDflXMI2KO.csv",
                            "id": "44c8778b-ed29-4ed4-b6e4-2d0ae625f62b",
                            "roundCloseStaking": "2025-08-26",
                            "roundNumber": 1080,
                            "roundOpen": "2025-08-26",
                            "status": "on-time",
                            "timestamp": "2025-08-26T13:10:14Z"
                        },
                        {
                            "filename": "mmoe_ensemble_predictions_20250823_131014-AQYGRVDoSIKd.csv",
                            "id": "2cdd1ffa-af2a-4aa9-87c4-6a24be2b64a9",
                            "roundCloseStaking": "2025-08-25",
                            "roundNumber": 1079,
                            "roundOpen": "2025-08-23",
                            "status": "on-time",
                            "timestamp": "2025-08-23T13:10:25Z"
                        },
                        {
                            "filename": "mmoe_ensemble_predictions_20250822_130957-EmJMnwz0Yuj4.csv",
                            "id": "83b02ab7-3fc9-4de6-ac84-4cb11a914230",
                            "roundCloseStaking": "2025-08-22",
                            "roundNumber": 1078,
                            "roundOpen": "2025-08-22",
                            "status": "on-time",
                            "timestamp": "2025-08-22T13:10:17Z"
                        },
                        {
                            "filename": "mmoe_ensemble_predictions_20250821_130939-2GPooYTjF1I5.csv",
                            "id": "0d99e57d-982a-40da-a81b-56ca07d24729",
                            "roundCloseStaking": "2025-08-21",
                            "roundNumber": 1077,
                            "roundOpen": "2025-08-21",
                            "status": "on-time",
                            "timestamp": "2025-08-21T13:10:00Z"
                        },
                        {
                            "filename": "mmoe_ensemble_predictions_20250820_131015-up0bjKoTwDVk.csv",
                            "id": "eb274428-77ef-4af8-be84-a9c2282e9d56",
                            "roundCloseStaking": "2025-08-20",
                            "roundNumber": 1076,
                            "roundOpen": "2025-08-20",
                            "status": "on-time",
                            "timestamp": "2025-08-20T13:10:36Z"
                        },
                        {
                            "filename": "mmoe_ensemble_predictions_20250819_131020-3je2TlChpTX0.csv",
                            "id": "89157fe4-1598-4fbb-bb3a-3a4d8428aa7e",
                            "roundCloseStaking": "2025-08-19",
                            "roundNumber": 1075,
                            "roundOpen": "2025-08-19",
                            "status": "on-time",
                            "timestamp": "2025-08-19T13:10:42Z"
                        },
                        {
                            "filename": "mmoe_ensemble_predictions_20250816_130838-gL4dzghTjs0l.csv",
                            "id": "071109a2-5331-4a84-9fdb-dfd323ed2e93",
                            "roundCloseStaking": "2025-08-18",
                            "roundNumber": 1074,
                            "roundOpen": "2025-08-16",
                            "status": "on-time",
                            "timestamp": "2025-08-16T13:08:55Z"
                        },
                        {
                            "filename": "mmoe_ensemble_predictions_20250815_130952-w7x1L4Jcw0tG.csv",
                            "id": "ba4e9502-9049-4632-91f8-ea1d0e620bea",
                            "roundCloseStaking": "2025-08-15",
                            "roundNumber": 1073,
                            "roundOpen": "2025-08-15",
                            "status": "on-time",
                            "timestamp": "2025-08-15T13:10:17Z"
                        },
                        {
                            "filename": "mmoe_ensemble_predictions_20250814_131021-WxsJSTPSQ4iG.csv",
                            "id": "6d3a48e4-172b-4d97-a08a-a2f159c0db36",
                            "roundCloseStaking": "2025-08-14",
                            "roundNumber": 1072,
                            "roundOpen": "2025-08-14",
                            "status": "on-time",
                            "timestamp": "2025-08-14T13:10:37Z"
                        },
                        {
                            "filename": "mmoe_ensemble_predictions_20250813_131039-JpnDsHb3H7MJ.csv",
                            "id": "fa39d811-cf11-4b36-a436-9758cfc824f7",
                            "roundCloseStaking": "2025-08-13",
                            "roundNumber": 1071,
                            "roundOpen": "2025-08-13",
                            "status": "on-time",
                            "timestamp": "2025-08-13T13:10:53Z"
                        },
                        {
                            "filename": "mmoe_ensemble_predictions_20250812_131032-HXTKlht2rY4i.csv",
                            "id": "1247cfb6-e14d-4c03-adbb-e05099e0d6a5",
                            "roundCloseStaking": "2025-08-12",
                            "roundNumber": 1070,
                            "roundOpen": "2025-08-12",
                            "status": "on-time",
                            "timestamp": "2025-08-12T13:10:43Z"
                        },
                        {
                            "filename": "mmoe_ensemble_predictions_20250809_131032-mcznwg5dojhC.csv",
                            "id": "42702bac-5796-4545-a076-34cbb35b80c3",
                            "roundCloseStaking": "2025-08-11",
                            "roundNumber": 1069,
                            "roundOpen": "2025-08-09",
                            "status": "on-time",
                            "timestamp": "2025-08-09T13:10:45Z"
                        },
                        {
                            "filename": "mmoe_ensemble_predictions_20250808_130959-BSn01gBsI0gx.csv",
                            "id": "6818bed4-aea5-4069-a845-3b77dfd79c63",
                            "roundCloseStaking": "2025-08-08",
                            "roundNumber": 1068,
                            "roundOpen": "2025-08-08",
                            "status": "on-time",
                            "timestamp": "2025-08-08T13:10:11Z"
                        },
                        {
                            "filename": "mmoe_ensemble_predictions_20250807_131154-2hTpWY5Flan8.csv",
                            "id": "1b3a3a10-b016-439b-990f-a871a7979de1",
                            "roundCloseStaking": "2025-08-07",
                            "roundNumber": 1067,
                            "roundOpen": "2025-08-07",
                            "status": "on-time",
                            "timestamp": "2025-08-07T13:12:11Z"
                        },
                        {
                            "filename": "mmoe_ensemble_predictions_20250806_141508-3E9RHCYeq9Zq.csv",
                            "id": "5e148716-0a32-4fc8-9798-f061f92867e4",
                            "roundCloseStaking": "2025-08-06",
                            "roundNumber": 1066,
                            "roundOpen": "2025-08-06",
                            "status": "late",
                            "timestamp": "2025-08-06T14:16:11Z"
                        },
                        {
                            "filename": "mmoe_ensemble_predictions_20250805_130907-G5cNIFSa0JmR.csv",
                            "id": "5512e43d-345a-4e43-9105-caa1a16c8d3d",
                            "roundCloseStaking": "2025-08-05",
                            "roundNumber": 1065,
                            "roundOpen": "2025-08-05",
                            "status": "on-time",
                            "timestamp": "2025-08-05T13:09:30Z"
                        },
                        {
                            "filename": "mmoe_ensemble_predictions_20250802_132046-XdEfU3Y8xyA4.csv",
                            "id": "da605fa7-f1b6-4682-a058-e94bbcae75a9",
                            "roundCloseStaking": "2025-08-04",
                            "roundNumber": 1064,
                            "roundOpen": "2025-08-02",
                            "status": "on-time",
                            "timestamp": "2025-08-02T13:21:51Z"
                        },
                        {
                            "filename": "mmoe_ensemble_predictions_20250801_130946-JxLyLiLfm2em.csv",
                            "id": "893dc057-bdbb-428b-8b1d-40c4b8acd4a3",
                            "roundCloseStaking": "2025-08-01",
                            "roundNumber": 1063,
                            "roundOpen": "2025-08-01",
                            "status": "on-time",
                            "timestamp": "2025-08-01T13:10:57Z"
                        },
                        {
                            "filename": "mmoe_ensemble_predictions_20250731_130838-nRJSGtw3zQJb.csv",
                            "id": "42ad8285-e114-42ea-ad65-8580aa21ef2c",
                            "roundCloseStaking": "2025-07-31",
                            "roundNumber": 1062,
                            "roundOpen": "2025-07-31",
                            "status": "on-time",
                            "timestamp": "2025-07-31T13:09:49Z"
                        },
                        {
                            "filename": "mmoe_ensemble_predictions_20250730_130939-fHuWefVk6CVP.csv",
                            "id": "26420bfa-aabf-4fab-97ba-680b72279ea4",
                            "roundCloseStaking": "2025-07-30",
                            "roundNumber": 1061,
                            "roundOpen": "2025-07-30",
                            "status": "on-time",
                            "timestamp": "2025-07-30T13:09:51Z"
                        },
                        {
                            "filename": "mmoe_ensemble_predictions_20250729_130655-82fDp32ZKW5l.csv",
                            "id": "f30ff3b5-d8e2-4ac5-8e86-1dabd20fec80",
                            "roundCloseStaking": "2025-07-29",
                            "roundNumber": 1060,
                            "roundOpen": "2025-07-29",
                            "status": "on-time",
                            "timestamp": "2025-07-29T13:07:15Z"
                        },
                        {
                            "filename": "mmoe_ensemble_predictions_20250728_093657-VTLikHYnx5Ni.csv",
                            "id": "1bbe4321-67d9-4fd7-a62c-61eb147e128c",
                            "roundCloseStaking": "2025-07-28",
                            "roundNumber": 1059,
                            "roundOpen": "2025-07-26",
                            "status": "on-time",
                            "timestamp": "2025-07-28T09:37:15Z"
                        },
                        {
                            "filename": "mmoe_ensemble_predictions_20250725_130731-j246e72nqbTv.csv",
                            "id": "11c949eb-bf8a-473e-b1f8-92e94cfa23d0",
                            "roundCloseStaking": "2025-07-25",
                            "roundNumber": 1058,
                            "roundOpen": "2025-07-25",
                            "status": "on-time",
                            "timestamp": "2025-07-25T13:07:52Z"
                        },
                        {
                            "filename": "mmoe_ensemble_predictions_20250724_130717-Au493rJgpc4t.csv",
                            "id": "0717aa15-1cbc-4921-8696-b443f10caef5",
                            "roundCloseStaking": "2025-07-24",
                            "roundNumber": 1057,
                            "roundOpen": "2025-07-24",
                            "status": "on-time",
                            "timestamp": "2025-07-24T13:07:33Z"
                        },
                        {
                            "filename": "mmoe_ensemble_predictions_20250723_130713-u1R7CTpSjkho.csv",
                            "id": "3fed2426-f175-4e8f-8c16-3cdd567eabc1",
                            "roundCloseStaking": "2025-07-23",
                            "roundNumber": 1056,
                            "roundOpen": "2025-07-23",
                            "status": "on-time",
                            "timestamp": "2025-07-23T13:07:33Z"
                        },
                        {
                            "filename": "mmoe_ensemble_predictions_20250722_131035-Dq6pE86fdIJ5.csv",
                            "id": "61810851-e36d-4a0d-8fd3-bcff2f96e22c",
                            "roundCloseStaking": "2025-07-22",
                            "roundNumber": 1055,
                            "roundOpen": "2025-07-22",
                            "status": "on-time",
                            "timestamp": "2025-07-22T13:10:48Z"
                        },
                        {
                            "filename": "mmoe_ensemble_predictions_20250719_130659-Las8Jhy8SYEi.csv",
                            "id": "09d09c49-9a22-49ee-95c4-a13758080488",
                            "roundCloseStaking": "2025-07-21",
                            "roundNumber": 1054,
                            "roundOpen": "2025-07-19",
                            "status": "on-time",
                            "timestamp": "2025-07-19T13:07:21Z"
                        },
                        {
                            "filename": "mmoe_ensemble_predictions_20250718_130714-Jhv4JHaCosvm.csv",
                            "id": "546bec48-0f26-4467-aa97-b963e0f3a774",
                            "roundCloseStaking": "2025-07-18",
                            "roundNumber": 1053,
                            "roundOpen": "2025-07-18",
                            "status": "on-time",
                            "timestamp": "2025-07-18T13:07:33Z"
                        },
                        {
                            "filename": "mmoe_ensemble_predictions_20250717_131403-eDEOnAiOd6jt.csv",
                            "id": "11b724d2-f470-4daa-a8d1-a3a43132a6ba",
                            "roundCloseStaking": "2025-07-17",
                            "roundNumber": 1052,
                            "roundOpen": "2025-07-17",
                            "status": "on-time",
                            "timestamp": "2025-07-17T13:14:28Z"
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-16",
                            "roundNumber": 1051,
                            "roundOpen": "2025-07-16",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": "mmoe_ensemble_predictions_20250715_130522-FsEVkRTmLKZ0.csv",
                            "id": "ec2a4c1a-87d0-4df6-ac9f-c17f5924ae3d",
                            "roundCloseStaking": "2025-07-15",
                            "roundNumber": 1050,
                            "roundOpen": "2025-07-15",
                            "status": "on-time",
                            "timestamp": "2025-07-15T13:05:38Z"
                        },
                        {
                            "filename": "mmoe_ensemble_predictions_20250712_135530-otuWqezrhknF.csv",
                            "id": "6291ec73-a6f2-44ab-ba97-053334244b6a",
                            "roundCloseStaking": "2025-07-14",
                            "roundNumber": 1049,
                            "roundOpen": "2025-07-12",
                            "status": "on-time",
                            "timestamp": "2025-07-12T13:55:47Z"
                        },
                        {
                            "filename": "mmoe_ensemble_predictions_20250711_130507-mCuVVwIVVvQT.csv",
                            "id": "3462368e-ecef-4d31-9dc6-0bee59881fe4",
                            "roundCloseStaking": "2025-07-11",
                            "roundNumber": 1048,
                            "roundOpen": "2025-07-11",
                            "status": "on-time",
                            "timestamp": "2025-07-11T13:05:21Z"
                        },
                        {
                            "filename": "mmoe_ensemble_predictions_20250710_185559-yDMQ8gQQ0aIx.csv",
                            "id": "210a7009-2ff5-405b-96a6-f22f49d82f5b",
                            "roundCloseStaking": "2025-07-10",
                            "roundNumber": 1047,
                            "roundOpen": "2025-07-10",
                            "status": "late",
                            "timestamp": "2025-07-10T18:56:14Z"
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-09",
                            "roundNumber": 1046,
                            "roundOpen": "2025-07-09",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-08",
                            "roundNumber": 1045,
                            "roundOpen": "2025-07-08",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-07",
                            "roundNumber": 1044,
                            "roundOpen": "2025-07-05",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-04",
                            "roundNumber": 1043,
                            "roundOpen": "2025-07-04",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-03",
                            "roundNumber": 1042,
                            "roundOpen": "2025-07-03",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-02",
                            "roundNumber": 1041,
                            "roundOpen": "2025-07-02",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-01",
                            "roundNumber": 1040,
                            "roundOpen": "2025-07-01",
                            "status": "none",
                            "timestamp": null
                        }
                    ],
                    "latestUserScores": [
                        {
                            "displayName": "apcwnm",
                            "reputation": 0.03199409648913681
                        },
                        {
                            "displayName": "bmc",
                            "reputation": 2.7346620374154413e-4
                        },
                        {
                            "displayName": "canon_bmc",
                            "reputation": 2.556542287851983e-4
                        },
                        {
                            "displayName": "canon_corr",
                            "reputation": 0.0013642406905608536
                        },
                        {
                            "displayName": "canon_cort20",
                            "reputation": 0.0011727018380834893
                        },
                        {
                            "displayName": "canon_fnc_v3",
                            "reputation": 6.367675993781125e-4
                        },
                        {
                            "displayName": "canon_mmc",
                            "reputation": -8.532831357665381e-5
                        },
                        {
                            "displayName": "corr_w_meta_model",
                            "reputation": 0.3714516890297066
                        },
                        {
                            "displayName": "cort20",
                            "reputation": 0.001249286447917513
                        },
                        {
                            "displayName": "fnc_v3",
                            "reputation": 6.783524221946422e-4
                        },
                        {
                            "displayName": "mcwnm",
                            "reputation": 0.06154167546041351
                        },
                        {
                            "displayName": "mmc",
                            "reputation": -9.09007748714557e-5
                        },
                        {
                            "displayName": "season_score",
                            "reputation": 5.114637181271192e-4
                        },
                        {
                            "displayName": "v2_corr20",
                            "reputation": 0.0014533339601485013
                        }
                    ],
                    "name": "fnc_me_e_d676",
                    "profileUrl": "https://numerai-public-images.s3-us-west-2.amazonaws.com/profile_images/fish_n_chips-c0zdPvYNpMRY.jpg",
                    "returns": {
                        "allTime": 1.2048086027587515,
                        "oneDay": -3.1402795803308203,
                        "oneYear": null,
                        "threeMonths": null
                    },
                    "submissionWebhook": "https://numerai.imperialai.ai/numerai-d6769cb7-f13a-45c9-a105-23048973d64c/",
                    "tournament": 8,
                    "v2Stake": {
                        "latestValue": "1.013754905760929000",
                        "latestValueSettled": "1.013754905760929000",
                        "pendingV2ChangeStakeRequest": null,
                        "stakeValue": "1.012048086027587514",
                        "status": null
                    }
                },
                {
                    "computeEnabled": false,
                    "computePickleUpload": {
                        "id": "4dac2370-3738-4d5e-a63b-13288efb00f8"
                    },
                    "currentPayoutSelection": {
                        "corrMultiplier": 0.5,
                        "mmcMultiplier": 2.0,
                        "takeProfit": false,
                        "updatedAt": null
                    },
                    "description": null,
                    "earliestReleaseDate": "2025-10-24T00:00:00Z",
                    "id": "1f5a33fe-92d6-43c6-8973-f1cc4e1824e2",
                    "isComputeWeekdayEnabled": true,
                    "latestSubmissions": [
                        {
                            "filename": "predictions-8tdh7bTEHuKW.csv",
                            "id": "3370993d-f722-4f43-8929-43b44733356c",
                            "roundCloseStaking": "2025-09-23",
                            "roundNumber": 1100,
                            "roundOpen": "2025-09-23",
                            "status": "on-time",
                            "timestamp": "2025-09-23T13:35:02Z"
                        },
                        {
                            "filename": "predictions-jNhor13zmYcM.csv",
                            "id": "44d0a7cb-641a-4d26-ba22-ddfb4711df7e",
                            "roundCloseStaking": "2025-09-22",
                            "roundNumber": 1099,
                            "roundOpen": "2025-09-20",
                            "status": "on-time",
                            "timestamp": "2025-09-20T13:25:41Z"
                        },
                        {
                            "filename": "predictions-DY9y46kkvKOC.csv",
                            "id": "d43ac69b-a272-473b-baba-88a5b08819bc",
                            "roundCloseStaking": "2025-09-19",
                            "roundNumber": 1098,
                            "roundOpen": "2025-09-19",
                            "status": "on-time",
                            "timestamp": "2025-09-19T13:25:56Z"
                        },
                        {
                            "filename": "predictions-fbI51XYoQmUc.csv",
                            "id": "ac8bc8a4-091f-4da0-83f0-85326acd965b",
                            "roundCloseStaking": "2025-09-18",
                            "roundNumber": 1097,
                            "roundOpen": "2025-09-18",
                            "status": "on-time",
                            "timestamp": "2025-09-18T13:26:47Z"
                        },
                        {
                            "filename": "predictions-esH2xCXsr342.csv",
                            "id": "f35c631e-617f-48f2-8a7a-8da3fc7d81a9",
                            "roundCloseStaking": "2025-09-17",
                            "roundNumber": 1096,
                            "roundOpen": "2025-09-17",
                            "status": "on-time",
                            "timestamp": "2025-09-17T13:26:24Z"
                        },
                        {
                            "filename": "predictions-GCLoNniNhQeu.csv",
                            "id": "19138b20-e2ac-4846-987f-2217985d7229",
                            "roundCloseStaking": "2025-09-16",
                            "roundNumber": 1095,
                            "roundOpen": "2025-09-16",
                            "status": "on-time",
                            "timestamp": "2025-09-16T13:28:36Z"
                        },
                        {
                            "filename": "predictions-HzutZHKL0BRv.csv",
                            "id": "9649f27f-bc5c-45cd-b6c4-a1400b6bca40",
                            "roundCloseStaking": "2025-09-15",
                            "roundNumber": 1094,
                            "roundOpen": "2025-09-13",
                            "status": "late",
                            "timestamp": "2025-09-16T07:20:36Z"
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-12",
                            "roundNumber": 1093,
                            "roundOpen": "2025-09-12",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-11",
                            "roundNumber": 1092,
                            "roundOpen": "2025-09-11",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-10",
                            "roundNumber": 1091,
                            "roundOpen": "2025-09-10",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-09",
                            "roundNumber": 1090,
                            "roundOpen": "2025-09-09",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-08",
                            "roundNumber": 1089,
                            "roundOpen": "2025-09-06",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-05",
                            "roundNumber": 1088,
                            "roundOpen": "2025-09-05",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-04",
                            "roundNumber": 1087,
                            "roundOpen": "2025-09-04",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-03",
                            "roundNumber": 1086,
                            "roundOpen": "2025-09-03",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-02",
                            "roundNumber": 1085,
                            "roundOpen": "2025-09-02",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-01",
                            "roundNumber": 1084,
                            "roundOpen": "2025-08-30",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-29",
                            "roundNumber": 1083,
                            "roundOpen": "2025-08-29",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-28",
                            "roundNumber": 1082,
                            "roundOpen": "2025-08-28",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-27",
                            "roundNumber": 1081,
                            "roundOpen": "2025-08-27",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-26",
                            "roundNumber": 1080,
                            "roundOpen": "2025-08-26",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-25",
                            "roundNumber": 1079,
                            "roundOpen": "2025-08-23",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-22",
                            "roundNumber": 1078,
                            "roundOpen": "2025-08-22",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-21",
                            "roundNumber": 1077,
                            "roundOpen": "2025-08-21",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-20",
                            "roundNumber": 1076,
                            "roundOpen": "2025-08-20",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-19",
                            "roundNumber": 1075,
                            "roundOpen": "2025-08-19",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-18",
                            "roundNumber": 1074,
                            "roundOpen": "2025-08-16",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-15",
                            "roundNumber": 1073,
                            "roundOpen": "2025-08-15",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-14",
                            "roundNumber": 1072,
                            "roundOpen": "2025-08-14",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-13",
                            "roundNumber": 1071,
                            "roundOpen": "2025-08-13",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-12",
                            "roundNumber": 1070,
                            "roundOpen": "2025-08-12",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-11",
                            "roundNumber": 1069,
                            "roundOpen": "2025-08-09",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-08",
                            "roundNumber": 1068,
                            "roundOpen": "2025-08-08",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-07",
                            "roundNumber": 1067,
                            "roundOpen": "2025-08-07",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-06",
                            "roundNumber": 1066,
                            "roundOpen": "2025-08-06",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-05",
                            "roundNumber": 1065,
                            "roundOpen": "2025-08-05",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-04",
                            "roundNumber": 1064,
                            "roundOpen": "2025-08-02",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-01",
                            "roundNumber": 1063,
                            "roundOpen": "2025-08-01",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-31",
                            "roundNumber": 1062,
                            "roundOpen": "2025-07-31",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-30",
                            "roundNumber": 1061,
                            "roundOpen": "2025-07-30",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-29",
                            "roundNumber": 1060,
                            "roundOpen": "2025-07-29",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-28",
                            "roundNumber": 1059,
                            "roundOpen": "2025-07-26",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-25",
                            "roundNumber": 1058,
                            "roundOpen": "2025-07-25",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-24",
                            "roundNumber": 1057,
                            "roundOpen": "2025-07-24",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-23",
                            "roundNumber": 1056,
                            "roundOpen": "2025-07-23",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-22",
                            "roundNumber": 1055,
                            "roundOpen": "2025-07-22",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-21",
                            "roundNumber": 1054,
                            "roundOpen": "2025-07-19",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-18",
                            "roundNumber": 1053,
                            "roundOpen": "2025-07-18",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-17",
                            "roundNumber": 1052,
                            "roundOpen": "2025-07-17",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-16",
                            "roundNumber": 1051,
                            "roundOpen": "2025-07-16",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-15",
                            "roundNumber": 1050,
                            "roundOpen": "2025-07-15",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-14",
                            "roundNumber": 1049,
                            "roundOpen": "2025-07-12",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-11",
                            "roundNumber": 1048,
                            "roundOpen": "2025-07-11",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-10",
                            "roundNumber": 1047,
                            "roundOpen": "2025-07-10",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-09",
                            "roundNumber": 1046,
                            "roundOpen": "2025-07-09",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-08",
                            "roundNumber": 1045,
                            "roundOpen": "2025-07-08",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-07",
                            "roundNumber": 1044,
                            "roundOpen": "2025-07-05",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-04",
                            "roundNumber": 1043,
                            "roundOpen": "2025-07-04",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-03",
                            "roundNumber": 1042,
                            "roundOpen": "2025-07-03",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-02",
                            "roundNumber": 1041,
                            "roundOpen": "2025-07-02",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-01",
                            "roundNumber": 1040,
                            "roundOpen": "2025-07-01",
                            "status": "none",
                            "timestamp": null
                        }
                    ],
                    "latestUserScores": null,
                    "name": "fnc_imp_03",
                    "profileUrl": "https://numerai-public-images.s3-us-west-2.amazonaws.com/profile_images/bart-sled-eTe3xE1sLwFY.jpg",
                    "returns": {
                        "allTime": null,
                        "oneDay": -0.34615085371251,
                        "oneYear": null,
                        "threeMonths": null
                    },
                    "submissionWebhook": null,
                    "tournament": 8,
                    "v2Stake": {
                        "latestValue": "1.000000000000000000",
                        "latestValueSettled": "1.000000000000000000",
                        "pendingV2ChangeStakeRequest": null,
                        "stakeValue": "1.000000000000000000",
                        "status": null
                    }
                },
                {
                    "computeEnabled": true,
                    "computePickleUpload": null,
                    "currentPayoutSelection": {
                        "corrMultiplier": 0.5,
                        "mmcMultiplier": 2.0,
                        "takeProfit": false,
                        "updatedAt": null
                    },
                    "description": null,
                    "earliestReleaseDate": "2025-10-24T00:00:00Z",
                    "id": "61e0dc85-55dc-461c-b40f-41bc65929fe5",
                    "isComputeWeekdayEnabled": true,
                    "latestSubmissions": [
                        {
                            "filename": "tabnet_predictions_2-9xDuySCqE3v7.csv",
                            "id": "b4af94cb-67ae-4e83-9142-2317ced74427",
                            "roundCloseStaking": "2025-09-23",
                            "roundNumber": 1100,
                            "roundOpen": "2025-09-23",
                            "status": "on-time",
                            "timestamp": "2025-09-23T13:14:02Z"
                        },
                        {
                            "filename": "tabnet_predictions_2-AeQVgWTbiExV.csv",
                            "id": "487628a0-baeb-44af-b8d9-f9e31f544cff",
                            "roundCloseStaking": "2025-09-22",
                            "roundNumber": 1099,
                            "roundOpen": "2025-09-20",
                            "status": "on-time",
                            "timestamp": "2025-09-20T13:10:00Z"
                        },
                        {
                            "filename": "tabnet_predictions_2-vMVjnyV77gvd.csv",
                            "id": "a989f4ff-4bc9-46ab-9df8-701e1a073b6f",
                            "roundCloseStaking": "2025-09-19",
                            "roundNumber": 1098,
                            "roundOpen": "2025-09-19",
                            "status": "on-time",
                            "timestamp": "2025-09-19T13:09:30Z"
                        },
                        {
                            "filename": "tabnet_predictions_2-V1lAXAmEOhmz.csv",
                            "id": "1b435cde-86b1-44e4-ada4-dd0622ed761e",
                            "roundCloseStaking": "2025-09-18",
                            "roundNumber": 1097,
                            "roundOpen": "2025-09-18",
                            "status": "on-time",
                            "timestamp": "2025-09-18T13:09:10Z"
                        },
                        {
                            "filename": "tabnet_predictions_2-mDq61SLBkjb5.csv",
                            "id": "7a7a8c1d-654f-46c1-bf06-0532375a93f0",
                            "roundCloseStaking": "2025-09-17",
                            "roundNumber": 1096,
                            "roundOpen": "2025-09-17",
                            "status": "on-time",
                            "timestamp": "2025-09-17T13:10:49Z"
                        },
                        {
                            "filename": "tabnet_predictions_2-MHyCcZPYeE7D.csv",
                            "id": "00b964f6-f76e-4b44-9a2c-38a69278bde2",
                            "roundCloseStaking": "2025-09-16",
                            "roundNumber": 1095,
                            "roundOpen": "2025-09-16",
                            "status": "on-time",
                            "timestamp": "2025-09-16T13:02:31Z"
                        },
                        {
                            "filename": "tabnet_predictions_2-MHyCcZPYeE7D.csv",
                            "id": "39931820-fda7-434e-8c45-b0f6dc661adc",
                            "roundCloseStaking": "2025-09-15",
                            "roundNumber": 1094,
                            "roundOpen": "2025-09-13",
                            "status": "late",
                            "timestamp": "2025-09-15T22:31:08Z"
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-12",
                            "roundNumber": 1093,
                            "roundOpen": "2025-09-12",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-11",
                            "roundNumber": 1092,
                            "roundOpen": "2025-09-11",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-10",
                            "roundNumber": 1091,
                            "roundOpen": "2025-09-10",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-09",
                            "roundNumber": 1090,
                            "roundOpen": "2025-09-09",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-08",
                            "roundNumber": 1089,
                            "roundOpen": "2025-09-06",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-05",
                            "roundNumber": 1088,
                            "roundOpen": "2025-09-05",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-04",
                            "roundNumber": 1087,
                            "roundOpen": "2025-09-04",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-03",
                            "roundNumber": 1086,
                            "roundOpen": "2025-09-03",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-02",
                            "roundNumber": 1085,
                            "roundOpen": "2025-09-02",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-01",
                            "roundNumber": 1084,
                            "roundOpen": "2025-08-30",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-29",
                            "roundNumber": 1083,
                            "roundOpen": "2025-08-29",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-28",
                            "roundNumber": 1082,
                            "roundOpen": "2025-08-28",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-27",
                            "roundNumber": 1081,
                            "roundOpen": "2025-08-27",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-26",
                            "roundNumber": 1080,
                            "roundOpen": "2025-08-26",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-25",
                            "roundNumber": 1079,
                            "roundOpen": "2025-08-23",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-22",
                            "roundNumber": 1078,
                            "roundOpen": "2025-08-22",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-21",
                            "roundNumber": 1077,
                            "roundOpen": "2025-08-21",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-20",
                            "roundNumber": 1076,
                            "roundOpen": "2025-08-20",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-19",
                            "roundNumber": 1075,
                            "roundOpen": "2025-08-19",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-18",
                            "roundNumber": 1074,
                            "roundOpen": "2025-08-16",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-15",
                            "roundNumber": 1073,
                            "roundOpen": "2025-08-15",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-14",
                            "roundNumber": 1072,
                            "roundOpen": "2025-08-14",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-13",
                            "roundNumber": 1071,
                            "roundOpen": "2025-08-13",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-12",
                            "roundNumber": 1070,
                            "roundOpen": "2025-08-12",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-11",
                            "roundNumber": 1069,
                            "roundOpen": "2025-08-09",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-08",
                            "roundNumber": 1068,
                            "roundOpen": "2025-08-08",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-07",
                            "roundNumber": 1067,
                            "roundOpen": "2025-08-07",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-06",
                            "roundNumber": 1066,
                            "roundOpen": "2025-08-06",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-05",
                            "roundNumber": 1065,
                            "roundOpen": "2025-08-05",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-04",
                            "roundNumber": 1064,
                            "roundOpen": "2025-08-02",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-01",
                            "roundNumber": 1063,
                            "roundOpen": "2025-08-01",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-31",
                            "roundNumber": 1062,
                            "roundOpen": "2025-07-31",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-30",
                            "roundNumber": 1061,
                            "roundOpen": "2025-07-30",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-29",
                            "roundNumber": 1060,
                            "roundOpen": "2025-07-29",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-28",
                            "roundNumber": 1059,
                            "roundOpen": "2025-07-26",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-25",
                            "roundNumber": 1058,
                            "roundOpen": "2025-07-25",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-24",
                            "roundNumber": 1057,
                            "roundOpen": "2025-07-24",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-23",
                            "roundNumber": 1056,
                            "roundOpen": "2025-07-23",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-22",
                            "roundNumber": 1055,
                            "roundOpen": "2025-07-22",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-21",
                            "roundNumber": 1054,
                            "roundOpen": "2025-07-19",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-18",
                            "roundNumber": 1053,
                            "roundOpen": "2025-07-18",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-17",
                            "roundNumber": 1052,
                            "roundOpen": "2025-07-17",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-16",
                            "roundNumber": 1051,
                            "roundOpen": "2025-07-16",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-15",
                            "roundNumber": 1050,
                            "roundOpen": "2025-07-15",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-14",
                            "roundNumber": 1049,
                            "roundOpen": "2025-07-12",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-11",
                            "roundNumber": 1048,
                            "roundOpen": "2025-07-11",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-10",
                            "roundNumber": 1047,
                            "roundOpen": "2025-07-10",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-09",
                            "roundNumber": 1046,
                            "roundOpen": "2025-07-09",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-08",
                            "roundNumber": 1045,
                            "roundOpen": "2025-07-08",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-07",
                            "roundNumber": 1044,
                            "roundOpen": "2025-07-05",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-04",
                            "roundNumber": 1043,
                            "roundOpen": "2025-07-04",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-03",
                            "roundNumber": 1042,
                            "roundOpen": "2025-07-03",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-02",
                            "roundNumber": 1041,
                            "roundOpen": "2025-07-02",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-01",
                            "roundNumber": 1040,
                            "roundOpen": "2025-07-01",
                            "status": "none",
                            "timestamp": null
                        }
                    ],
                    "latestUserScores": null,
                    "name": "fnc_t2_61e0",
                    "profileUrl": "https://numerai-public-images.s3-us-west-2.amazonaws.com/profile_images/teminator2-qTxSCR69eEQF.jpg",
                    "returns": {
                        "allTime": null,
                        "oneDay": 0.13710627036126133,
                        "oneYear": null,
                        "threeMonths": null
                    },
                    "submissionWebhook": "https://numerai.imperialai.ai/numerai-61e0dc85-55dc-461c-b40f-41bc65929fe5/",
                    "tournament": 8,
                    "v2Stake": {
                        "latestValue": "1.000000000000000000",
                        "latestValueSettled": "1.000000000000000000",
                        "pendingV2ChangeStakeRequest": null,
                        "stakeValue": "1.000000000000000000",
                        "status": null
                    }
                },
                {
                    "computeEnabled": false,
                    "computePickleUpload": {
                        "id": "8acc1454-7f09-4a0f-8642-f94c5b50e7ad"
                    },
                    "currentPayoutSelection": {
                        "corrMultiplier": 0.5,
                        "mmcMultiplier": 2.0,
                        "takeProfit": false,
                        "updatedAt": null
                    },
                    "description": null,
                    "earliestReleaseDate": "2025-10-24T00:00:00Z",
                    "id": "82c38772-a474-46a8-8168-aa2bb7d72a7c",
                    "isComputeWeekdayEnabled": true,
                    "latestSubmissions": [
                        {
                            "filename": "predictions-qqzvDWlOuen1.csv",
                            "id": "99aa33a2-2667-484d-b4d8-8db93682fd68",
                            "roundCloseStaking": "2025-09-23",
                            "roundNumber": 1100,
                            "roundOpen": "2025-09-23",
                            "status": "on-time",
                            "timestamp": "2025-09-23T13:31:55Z"
                        },
                        {
                            "filename": "predictions-DgkedcynXHCL.csv",
                            "id": "716c7702-f288-4558-a9c7-e66dd4a68da9",
                            "roundCloseStaking": "2025-09-22",
                            "roundNumber": 1099,
                            "roundOpen": "2025-09-20",
                            "status": "on-time",
                            "timestamp": "2025-09-20T13:29:38Z"
                        },
                        {
                            "filename": "predictions-o2zpqbsga8F9.csv",
                            "id": "b89e52b3-7dab-445b-878d-8e557b8e33d7",
                            "roundCloseStaking": "2025-09-19",
                            "roundNumber": 1098,
                            "roundOpen": "2025-09-19",
                            "status": "on-time",
                            "timestamp": "2025-09-19T13:26:42Z"
                        },
                        {
                            "filename": "predictions-UuDCWB9b61dn.csv",
                            "id": "2b679165-754b-436f-ba81-723a17bb50db",
                            "roundCloseStaking": "2025-09-18",
                            "roundNumber": 1097,
                            "roundOpen": "2025-09-18",
                            "status": "on-time",
                            "timestamp": "2025-09-18T13:26:48Z"
                        },
                        {
                            "filename": "predictions-MyEEKO6mJHT2.csv",
                            "id": "215dd593-18c9-4e18-9e8f-e385512da0e0",
                            "roundCloseStaking": "2025-09-17",
                            "roundNumber": 1096,
                            "roundOpen": "2025-09-17",
                            "status": "on-time",
                            "timestamp": "2025-09-17T13:28:10Z"
                        },
                        {
                            "filename": "predictions-pvUzcUtLmEr4.csv",
                            "id": "5b88cc4a-38ca-4308-9032-2c544fdd853b",
                            "roundCloseStaking": "2025-09-16",
                            "roundNumber": 1095,
                            "roundOpen": "2025-09-16",
                            "status": "on-time",
                            "timestamp": "2025-09-16T13:26:44Z"
                        },
                        {
                            "filename": "predictions-KE6JBb4RzvXg.csv",
                            "id": "e038a7f6-eeca-4452-bd33-e9af4dd7dc3b",
                            "roundCloseStaking": "2025-09-15",
                            "roundNumber": 1094,
                            "roundOpen": "2025-09-13",
                            "status": "late",
                            "timestamp": "2025-09-16T05:23:56Z"
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-12",
                            "roundNumber": 1093,
                            "roundOpen": "2025-09-12",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-11",
                            "roundNumber": 1092,
                            "roundOpen": "2025-09-11",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-10",
                            "roundNumber": 1091,
                            "roundOpen": "2025-09-10",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-09",
                            "roundNumber": 1090,
                            "roundOpen": "2025-09-09",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-08",
                            "roundNumber": 1089,
                            "roundOpen": "2025-09-06",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-05",
                            "roundNumber": 1088,
                            "roundOpen": "2025-09-05",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-04",
                            "roundNumber": 1087,
                            "roundOpen": "2025-09-04",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-03",
                            "roundNumber": 1086,
                            "roundOpen": "2025-09-03",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-02",
                            "roundNumber": 1085,
                            "roundOpen": "2025-09-02",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-01",
                            "roundNumber": 1084,
                            "roundOpen": "2025-08-30",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-29",
                            "roundNumber": 1083,
                            "roundOpen": "2025-08-29",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-28",
                            "roundNumber": 1082,
                            "roundOpen": "2025-08-28",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-27",
                            "roundNumber": 1081,
                            "roundOpen": "2025-08-27",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-26",
                            "roundNumber": 1080,
                            "roundOpen": "2025-08-26",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-25",
                            "roundNumber": 1079,
                            "roundOpen": "2025-08-23",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-22",
                            "roundNumber": 1078,
                            "roundOpen": "2025-08-22",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-21",
                            "roundNumber": 1077,
                            "roundOpen": "2025-08-21",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-20",
                            "roundNumber": 1076,
                            "roundOpen": "2025-08-20",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-19",
                            "roundNumber": 1075,
                            "roundOpen": "2025-08-19",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-18",
                            "roundNumber": 1074,
                            "roundOpen": "2025-08-16",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-15",
                            "roundNumber": 1073,
                            "roundOpen": "2025-08-15",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-14",
                            "roundNumber": 1072,
                            "roundOpen": "2025-08-14",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-13",
                            "roundNumber": 1071,
                            "roundOpen": "2025-08-13",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-12",
                            "roundNumber": 1070,
                            "roundOpen": "2025-08-12",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-11",
                            "roundNumber": 1069,
                            "roundOpen": "2025-08-09",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-08",
                            "roundNumber": 1068,
                            "roundOpen": "2025-08-08",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-07",
                            "roundNumber": 1067,
                            "roundOpen": "2025-08-07",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-06",
                            "roundNumber": 1066,
                            "roundOpen": "2025-08-06",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-05",
                            "roundNumber": 1065,
                            "roundOpen": "2025-08-05",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-04",
                            "roundNumber": 1064,
                            "roundOpen": "2025-08-02",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-01",
                            "roundNumber": 1063,
                            "roundOpen": "2025-08-01",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-31",
                            "roundNumber": 1062,
                            "roundOpen": "2025-07-31",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-30",
                            "roundNumber": 1061,
                            "roundOpen": "2025-07-30",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-29",
                            "roundNumber": 1060,
                            "roundOpen": "2025-07-29",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-28",
                            "roundNumber": 1059,
                            "roundOpen": "2025-07-26",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-25",
                            "roundNumber": 1058,
                            "roundOpen": "2025-07-25",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-24",
                            "roundNumber": 1057,
                            "roundOpen": "2025-07-24",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-23",
                            "roundNumber": 1056,
                            "roundOpen": "2025-07-23",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-22",
                            "roundNumber": 1055,
                            "roundOpen": "2025-07-22",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-21",
                            "roundNumber": 1054,
                            "roundOpen": "2025-07-19",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-18",
                            "roundNumber": 1053,
                            "roundOpen": "2025-07-18",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-17",
                            "roundNumber": 1052,
                            "roundOpen": "2025-07-17",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-16",
                            "roundNumber": 1051,
                            "roundOpen": "2025-07-16",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-15",
                            "roundNumber": 1050,
                            "roundOpen": "2025-07-15",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-14",
                            "roundNumber": 1049,
                            "roundOpen": "2025-07-12",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-11",
                            "roundNumber": 1048,
                            "roundOpen": "2025-07-11",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-10",
                            "roundNumber": 1047,
                            "roundOpen": "2025-07-10",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-09",
                            "roundNumber": 1046,
                            "roundOpen": "2025-07-09",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-08",
                            "roundNumber": 1045,
                            "roundOpen": "2025-07-08",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-07",
                            "roundNumber": 1044,
                            "roundOpen": "2025-07-05",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-04",
                            "roundNumber": 1043,
                            "roundOpen": "2025-07-04",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-03",
                            "roundNumber": 1042,
                            "roundOpen": "2025-07-03",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-02",
                            "roundNumber": 1041,
                            "roundOpen": "2025-07-02",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-01",
                            "roundNumber": 1040,
                            "roundOpen": "2025-07-01",
                            "status": "none",
                            "timestamp": null
                        }
                    ],
                    "latestUserScores": null,
                    "name": "fnc_imp_02",
                    "profileUrl": "https://numerai-public-images.s3-us-west-2.amazonaws.com/profile_images/evolve2-KSEjT0MPGNGt.png",
                    "returns": {
                        "allTime": null,
                        "oneDay": -0.42942799303864,
                        "oneYear": null,
                        "threeMonths": null
                    },
                    "submissionWebhook": null,
                    "tournament": 8,
                    "v2Stake": {
                        "latestValue": "1.000000000000000000",
                        "latestValueSettled": "1.000000000000000000",
                        "pendingV2ChangeStakeRequest": null,
                        "stakeValue": "1.000000000000000000",
                        "status": null
                    }
                },
                {
                    "computeEnabled": true,
                    "computePickleUpload": null,
                    "currentPayoutSelection": {
                        "corrMultiplier": 0.5,
                        "mmcMultiplier": 2.0,
                        "takeProfit": false,
                        "updatedAt": null
                    },
                    "description": null,
                    "earliestReleaseDate": "2025-10-24T00:00:00Z",
                    "id": "3f608ba4-565b-49be-acd9-3ca8331c3837",
                    "isComputeWeekdayEnabled": true,
                    "latestSubmissions": [
                        {
                            "filename": "tabnet_predictions_wf-7PjAjhrfXzhi.csv",
                            "id": "6099c98e-0c02-44e6-84f1-e3649e9145c3",
                            "roundCloseStaking": "2025-09-23",
                            "roundNumber": 1100,
                            "roundOpen": "2025-09-23",
                            "status": "on-time",
                            "timestamp": "2025-09-23T13:13:30Z"
                        },
                        {
                            "filename": "tabnet_predictions_wf-LsL2BM4ryTVD.csv",
                            "id": "3b928fe4-3117-4f2d-b7e7-b44c45995a74",
                            "roundCloseStaking": "2025-09-22",
                            "roundNumber": 1099,
                            "roundOpen": "2025-09-20",
                            "status": "on-time",
                            "timestamp": "2025-09-20T13:09:38Z"
                        },
                        {
                            "filename": "tabnet_predictions_wf-HEFbN3wwLihP.csv",
                            "id": "d96b63a3-140b-4964-9c2e-2e5dbf8c1e74",
                            "roundCloseStaking": "2025-09-19",
                            "roundNumber": 1098,
                            "roundOpen": "2025-09-19",
                            "status": "on-time",
                            "timestamp": "2025-09-19T13:09:17Z"
                        },
                        {
                            "filename": "tabnet_predictions_wf-ZAgQErs8wIlJ.csv",
                            "id": "35af6e17-fcc7-46f2-9b10-8c5ab626ff44",
                            "roundCloseStaking": "2025-09-18",
                            "roundNumber": 1097,
                            "roundOpen": "2025-09-18",
                            "status": "on-time",
                            "timestamp": "2025-09-18T13:09:00Z"
                        },
                        {
                            "filename": "tabnet_predictions_wf-63f9jKPRJj9v.csv",
                            "id": "5fec0435-8f3a-4b5f-82e2-fa8ff68ec05c",
                            "roundCloseStaking": "2025-09-17",
                            "roundNumber": 1096,
                            "roundOpen": "2025-09-17",
                            "status": "on-time",
                            "timestamp": "2025-09-17T13:10:37Z"
                        },
                        {
                            "filename": "tabnet_predictions_wf-DKwZnHrwO0YF.csv",
                            "id": "500f30cb-1b90-4c88-91e3-4210ef86179d",
                            "roundCloseStaking": "2025-09-16",
                            "roundNumber": 1095,
                            "roundOpen": "2025-09-16",
                            "status": "on-time",
                            "timestamp": "2025-09-16T13:07:09Z"
                        },
                        {
                            "filename": "tabnet_predictions_wf-Ilab0faLjAOs.csv",
                            "id": "be079fd6-2d57-414e-8383-45fb01f80161",
                            "roundCloseStaking": "2025-09-15",
                            "roundNumber": 1094,
                            "roundOpen": "2025-09-13",
                            "status": "late",
                            "timestamp": "2025-09-15T22:30:34Z"
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-12",
                            "roundNumber": 1093,
                            "roundOpen": "2025-09-12",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-11",
                            "roundNumber": 1092,
                            "roundOpen": "2025-09-11",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-10",
                            "roundNumber": 1091,
                            "roundOpen": "2025-09-10",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-09",
                            "roundNumber": 1090,
                            "roundOpen": "2025-09-09",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-08",
                            "roundNumber": 1089,
                            "roundOpen": "2025-09-06",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-05",
                            "roundNumber": 1088,
                            "roundOpen": "2025-09-05",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-04",
                            "roundNumber": 1087,
                            "roundOpen": "2025-09-04",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-03",
                            "roundNumber": 1086,
                            "roundOpen": "2025-09-03",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-02",
                            "roundNumber": 1085,
                            "roundOpen": "2025-09-02",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-01",
                            "roundNumber": 1084,
                            "roundOpen": "2025-08-30",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-29",
                            "roundNumber": 1083,
                            "roundOpen": "2025-08-29",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-28",
                            "roundNumber": 1082,
                            "roundOpen": "2025-08-28",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-27",
                            "roundNumber": 1081,
                            "roundOpen": "2025-08-27",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-26",
                            "roundNumber": 1080,
                            "roundOpen": "2025-08-26",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-25",
                            "roundNumber": 1079,
                            "roundOpen": "2025-08-23",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-22",
                            "roundNumber": 1078,
                            "roundOpen": "2025-08-22",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-21",
                            "roundNumber": 1077,
                            "roundOpen": "2025-08-21",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-20",
                            "roundNumber": 1076,
                            "roundOpen": "2025-08-20",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-19",
                            "roundNumber": 1075,
                            "roundOpen": "2025-08-19",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-18",
                            "roundNumber": 1074,
                            "roundOpen": "2025-08-16",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-15",
                            "roundNumber": 1073,
                            "roundOpen": "2025-08-15",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-14",
                            "roundNumber": 1072,
                            "roundOpen": "2025-08-14",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-13",
                            "roundNumber": 1071,
                            "roundOpen": "2025-08-13",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-12",
                            "roundNumber": 1070,
                            "roundOpen": "2025-08-12",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-11",
                            "roundNumber": 1069,
                            "roundOpen": "2025-08-09",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-08",
                            "roundNumber": 1068,
                            "roundOpen": "2025-08-08",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-07",
                            "roundNumber": 1067,
                            "roundOpen": "2025-08-07",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-06",
                            "roundNumber": 1066,
                            "roundOpen": "2025-08-06",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-05",
                            "roundNumber": 1065,
                            "roundOpen": "2025-08-05",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-04",
                            "roundNumber": 1064,
                            "roundOpen": "2025-08-02",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-01",
                            "roundNumber": 1063,
                            "roundOpen": "2025-08-01",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-31",
                            "roundNumber": 1062,
                            "roundOpen": "2025-07-31",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-30",
                            "roundNumber": 1061,
                            "roundOpen": "2025-07-30",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-29",
                            "roundNumber": 1060,
                            "roundOpen": "2025-07-29",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-28",
                            "roundNumber": 1059,
                            "roundOpen": "2025-07-26",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-25",
                            "roundNumber": 1058,
                            "roundOpen": "2025-07-25",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-24",
                            "roundNumber": 1057,
                            "roundOpen": "2025-07-24",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-23",
                            "roundNumber": 1056,
                            "roundOpen": "2025-07-23",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-22",
                            "roundNumber": 1055,
                            "roundOpen": "2025-07-22",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-21",
                            "roundNumber": 1054,
                            "roundOpen": "2025-07-19",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-18",
                            "roundNumber": 1053,
                            "roundOpen": "2025-07-18",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-17",
                            "roundNumber": 1052,
                            "roundOpen": "2025-07-17",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-16",
                            "roundNumber": 1051,
                            "roundOpen": "2025-07-16",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-15",
                            "roundNumber": 1050,
                            "roundOpen": "2025-07-15",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-14",
                            "roundNumber": 1049,
                            "roundOpen": "2025-07-12",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-11",
                            "roundNumber": 1048,
                            "roundOpen": "2025-07-11",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-10",
                            "roundNumber": 1047,
                            "roundOpen": "2025-07-10",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-09",
                            "roundNumber": 1046,
                            "roundOpen": "2025-07-09",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-08",
                            "roundNumber": 1045,
                            "roundOpen": "2025-07-08",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-07",
                            "roundNumber": 1044,
                            "roundOpen": "2025-07-05",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-04",
                            "roundNumber": 1043,
                            "roundOpen": "2025-07-04",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-03",
                            "roundNumber": 1042,
                            "roundOpen": "2025-07-03",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-02",
                            "roundNumber": 1041,
                            "roundOpen": "2025-07-02",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-01",
                            "roundNumber": 1040,
                            "roundOpen": "2025-07-01",
                            "status": "none",
                            "timestamp": null
                        }
                    ],
                    "latestUserScores": null,
                    "name": "fnc_t3_3f60",
                    "profileUrl": "https://numerai-public-images.s3-us-west-2.amazonaws.com/profile_images/terminator3-N9xLEmu2r27P.jpg",
                    "returns": {
                        "allTime": null,
                        "oneDay": -0.36902105514553685,
                        "oneYear": null,
                        "threeMonths": null
                    },
                    "submissionWebhook": "https://numerai.imperialai.ai/numerai-3f608ba4-565b-49be-acd9-3ca8331c3837/",
                    "tournament": 8,
                    "v2Stake": {
                        "latestValue": "1.000000000000000000",
                        "latestValueSettled": "1.000000000000000000",
                        "pendingV2ChangeStakeRequest": null,
                        "stakeValue": "1.000000000000000000",
                        "status": null
                    }
                },
                {
                    "computeEnabled": true,
                    "computePickleUpload": null,
                    "currentPayoutSelection": {
                        "corrMultiplier": 0.5,
                        "mmcMultiplier": 2.0,
                        "takeProfit": false,
                        "updatedAt": null
                    },
                    "description": null,
                    "earliestReleaseDate": "2025-09-24T00:00:00Z",
                    "id": "3ef49b09-d917-480c-900e-19cd53b07757",
                    "isComputeWeekdayEnabled": true,
                    "latestSubmissions": [
                        {
                            "filename": "ensemble_target-UnwyE0JpV8yl.csv",
                            "id": "15e31947-ba80-4676-90a4-03a493c13ed2",
                            "roundCloseStaking": "2025-09-24",
                            "roundNumber": 1101,
                            "roundOpen": "2025-09-24",
                            "status": "queued",
                            "timestamp": "2025-09-23T14:11:26Z"
                        },
                        {
                            "filename": "ensemble_target-UnwyE0JpV8yl.csv",
                            "id": "15e31947-ba80-4676-90a4-03a493c13ed2",
                            "roundCloseStaking": "2025-09-23",
                            "roundNumber": 1100,
                            "roundOpen": "2025-09-23",
                            "status": "late",
                            "timestamp": "2025-09-23T14:11:26Z"
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-22",
                            "roundNumber": 1099,
                            "roundOpen": "2025-09-20",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-19",
                            "roundNumber": 1098,
                            "roundOpen": "2025-09-19",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-18",
                            "roundNumber": 1097,
                            "roundOpen": "2025-09-18",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-17",
                            "roundNumber": 1096,
                            "roundOpen": "2025-09-17",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-16",
                            "roundNumber": 1095,
                            "roundOpen": "2025-09-16",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-15",
                            "roundNumber": 1094,
                            "roundOpen": "2025-09-13",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-12",
                            "roundNumber": 1093,
                            "roundOpen": "2025-09-12",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-11",
                            "roundNumber": 1092,
                            "roundOpen": "2025-09-11",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-10",
                            "roundNumber": 1091,
                            "roundOpen": "2025-09-10",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-09",
                            "roundNumber": 1090,
                            "roundOpen": "2025-09-09",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-08",
                            "roundNumber": 1089,
                            "roundOpen": "2025-09-06",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-05",
                            "roundNumber": 1088,
                            "roundOpen": "2025-09-05",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-04",
                            "roundNumber": 1087,
                            "roundOpen": "2025-09-04",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-03",
                            "roundNumber": 1086,
                            "roundOpen": "2025-09-03",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-02",
                            "roundNumber": 1085,
                            "roundOpen": "2025-09-02",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-01",
                            "roundNumber": 1084,
                            "roundOpen": "2025-08-30",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-29",
                            "roundNumber": 1083,
                            "roundOpen": "2025-08-29",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-28",
                            "roundNumber": 1082,
                            "roundOpen": "2025-08-28",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-27",
                            "roundNumber": 1081,
                            "roundOpen": "2025-08-27",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-26",
                            "roundNumber": 1080,
                            "roundOpen": "2025-08-26",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-25",
                            "roundNumber": 1079,
                            "roundOpen": "2025-08-23",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-22",
                            "roundNumber": 1078,
                            "roundOpen": "2025-08-22",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-21",
                            "roundNumber": 1077,
                            "roundOpen": "2025-08-21",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-20",
                            "roundNumber": 1076,
                            "roundOpen": "2025-08-20",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-19",
                            "roundNumber": 1075,
                            "roundOpen": "2025-08-19",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-18",
                            "roundNumber": 1074,
                            "roundOpen": "2025-08-16",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-15",
                            "roundNumber": 1073,
                            "roundOpen": "2025-08-15",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-14",
                            "roundNumber": 1072,
                            "roundOpen": "2025-08-14",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-13",
                            "roundNumber": 1071,
                            "roundOpen": "2025-08-13",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-12",
                            "roundNumber": 1070,
                            "roundOpen": "2025-08-12",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-11",
                            "roundNumber": 1069,
                            "roundOpen": "2025-08-09",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-08",
                            "roundNumber": 1068,
                            "roundOpen": "2025-08-08",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-07",
                            "roundNumber": 1067,
                            "roundOpen": "2025-08-07",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-06",
                            "roundNumber": 1066,
                            "roundOpen": "2025-08-06",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-05",
                            "roundNumber": 1065,
                            "roundOpen": "2025-08-05",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-04",
                            "roundNumber": 1064,
                            "roundOpen": "2025-08-02",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-01",
                            "roundNumber": 1063,
                            "roundOpen": "2025-08-01",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-31",
                            "roundNumber": 1062,
                            "roundOpen": "2025-07-31",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-30",
                            "roundNumber": 1061,
                            "roundOpen": "2025-07-30",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-29",
                            "roundNumber": 1060,
                            "roundOpen": "2025-07-29",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-28",
                            "roundNumber": 1059,
                            "roundOpen": "2025-07-26",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-25",
                            "roundNumber": 1058,
                            "roundOpen": "2025-07-25",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-24",
                            "roundNumber": 1057,
                            "roundOpen": "2025-07-24",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-23",
                            "roundNumber": 1056,
                            "roundOpen": "2025-07-23",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-22",
                            "roundNumber": 1055,
                            "roundOpen": "2025-07-22",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-21",
                            "roundNumber": 1054,
                            "roundOpen": "2025-07-19",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-18",
                            "roundNumber": 1053,
                            "roundOpen": "2025-07-18",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-17",
                            "roundNumber": 1052,
                            "roundOpen": "2025-07-17",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-16",
                            "roundNumber": 1051,
                            "roundOpen": "2025-07-16",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-15",
                            "roundNumber": 1050,
                            "roundOpen": "2025-07-15",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-14",
                            "roundNumber": 1049,
                            "roundOpen": "2025-07-12",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-11",
                            "roundNumber": 1048,
                            "roundOpen": "2025-07-11",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-10",
                            "roundNumber": 1047,
                            "roundOpen": "2025-07-10",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-09",
                            "roundNumber": 1046,
                            "roundOpen": "2025-07-09",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-08",
                            "roundNumber": 1045,
                            "roundOpen": "2025-07-08",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-07",
                            "roundNumber": 1044,
                            "roundOpen": "2025-07-05",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-04",
                            "roundNumber": 1043,
                            "roundOpen": "2025-07-04",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-03",
                            "roundNumber": 1042,
                            "roundOpen": "2025-07-03",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-02",
                            "roundNumber": 1041,
                            "roundOpen": "2025-07-02",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-01",
                            "roundNumber": 1040,
                            "roundOpen": "2025-07-01",
                            "status": "none",
                            "timestamp": null
                        }
                    ],
                    "latestUserScores": null,
                    "name": "fnc_t4_wf42",
                    "profileUrl": null,
                    "returns": null,
                    "submissionWebhook": "https://numerai.imperialai.ai/numerai-3ef49b09-d917-480c-900e-19cd53b07757/",
                    "tournament": 8,
                    "v2Stake": {
                        "latestValue": "0.000000000000000000",
                        "latestValueSettled": "0.000000000000000000",
                        "pendingV2ChangeStakeRequest": null,
                        "stakeValue": null,
                        "status": null
                    }
                },
                {
                    "computeEnabled": false,
                    "computePickleUpload": null,
                    "currentPayoutSelection": {
                        "corrMultiplier": 0.0,
                        "mmcMultiplier": 1.0,
                        "takeProfit": false,
                        "updatedAt": null
                    },
                    "description": null,
                    "earliestReleaseDate": "2025-09-24T00:00:00Z",
                    "id": "ae800569-0185-4f10-9bb0-5c093ac9d386",
                    "isComputeWeekdayEnabled": true,
                    "latestSubmissions": [
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-23",
                            "roundNumber": 1100,
                            "roundOpen": "2025-09-23",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-22",
                            "roundNumber": 1099,
                            "roundOpen": "2025-09-20",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-19",
                            "roundNumber": 1098,
                            "roundOpen": "2025-09-19",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-18",
                            "roundNumber": 1097,
                            "roundOpen": "2025-09-18",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-17",
                            "roundNumber": 1096,
                            "roundOpen": "2025-09-17",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-16",
                            "roundNumber": 1095,
                            "roundOpen": "2025-09-16",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-15",
                            "roundNumber": 1094,
                            "roundOpen": "2025-09-13",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-12",
                            "roundNumber": 1093,
                            "roundOpen": "2025-09-12",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-11",
                            "roundNumber": 1092,
                            "roundOpen": "2025-09-11",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-10",
                            "roundNumber": 1091,
                            "roundOpen": "2025-09-10",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-09",
                            "roundNumber": 1090,
                            "roundOpen": "2025-09-09",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-08",
                            "roundNumber": 1089,
                            "roundOpen": "2025-09-06",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-05",
                            "roundNumber": 1088,
                            "roundOpen": "2025-09-05",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-04",
                            "roundNumber": 1087,
                            "roundOpen": "2025-09-04",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-03",
                            "roundNumber": 1086,
                            "roundOpen": "2025-09-03",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-02",
                            "roundNumber": 1085,
                            "roundOpen": "2025-09-02",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-01",
                            "roundNumber": 1084,
                            "roundOpen": "2025-08-30",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-29",
                            "roundNumber": 1083,
                            "roundOpen": "2025-08-29",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-28",
                            "roundNumber": 1082,
                            "roundOpen": "2025-08-28",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-27",
                            "roundNumber": 1081,
                            "roundOpen": "2025-08-27",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-26",
                            "roundNumber": 1080,
                            "roundOpen": "2025-08-26",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-25",
                            "roundNumber": 1079,
                            "roundOpen": "2025-08-23",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-22",
                            "roundNumber": 1078,
                            "roundOpen": "2025-08-22",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-21",
                            "roundNumber": 1077,
                            "roundOpen": "2025-08-21",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-20",
                            "roundNumber": 1076,
                            "roundOpen": "2025-08-20",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-19",
                            "roundNumber": 1075,
                            "roundOpen": "2025-08-19",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-18",
                            "roundNumber": 1074,
                            "roundOpen": "2025-08-16",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-15",
                            "roundNumber": 1073,
                            "roundOpen": "2025-08-15",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-14",
                            "roundNumber": 1072,
                            "roundOpen": "2025-08-14",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-13",
                            "roundNumber": 1071,
                            "roundOpen": "2025-08-13",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-12",
                            "roundNumber": 1070,
                            "roundOpen": "2025-08-12",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-11",
                            "roundNumber": 1069,
                            "roundOpen": "2025-08-09",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-08",
                            "roundNumber": 1068,
                            "roundOpen": "2025-08-08",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-07",
                            "roundNumber": 1067,
                            "roundOpen": "2025-08-07",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-06",
                            "roundNumber": 1066,
                            "roundOpen": "2025-08-06",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-05",
                            "roundNumber": 1065,
                            "roundOpen": "2025-08-05",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-04",
                            "roundNumber": 1064,
                            "roundOpen": "2025-08-02",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-01",
                            "roundNumber": 1063,
                            "roundOpen": "2025-08-01",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-31",
                            "roundNumber": 1062,
                            "roundOpen": "2025-07-31",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-30",
                            "roundNumber": 1061,
                            "roundOpen": "2025-07-30",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-29",
                            "roundNumber": 1060,
                            "roundOpen": "2025-07-29",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-28",
                            "roundNumber": 1059,
                            "roundOpen": "2025-07-26",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-25",
                            "roundNumber": 1058,
                            "roundOpen": "2025-07-25",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-24",
                            "roundNumber": 1057,
                            "roundOpen": "2025-07-24",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-23",
                            "roundNumber": 1056,
                            "roundOpen": "2025-07-23",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-22",
                            "roundNumber": 1055,
                            "roundOpen": "2025-07-22",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-21",
                            "roundNumber": 1054,
                            "roundOpen": "2025-07-19",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-18",
                            "roundNumber": 1053,
                            "roundOpen": "2025-07-18",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-17",
                            "roundNumber": 1052,
                            "roundOpen": "2025-07-17",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-16",
                            "roundNumber": 1051,
                            "roundOpen": "2025-07-16",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-15",
                            "roundNumber": 1050,
                            "roundOpen": "2025-07-15",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-14",
                            "roundNumber": 1049,
                            "roundOpen": "2025-07-12",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-11",
                            "roundNumber": 1048,
                            "roundOpen": "2025-07-11",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-10",
                            "roundNumber": 1047,
                            "roundOpen": "2025-07-10",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-09",
                            "roundNumber": 1046,
                            "roundOpen": "2025-07-09",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-08",
                            "roundNumber": 1045,
                            "roundOpen": "2025-07-08",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-07",
                            "roundNumber": 1044,
                            "roundOpen": "2025-07-05",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-04",
                            "roundNumber": 1043,
                            "roundOpen": "2025-07-04",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-03",
                            "roundNumber": 1042,
                            "roundOpen": "2025-07-03",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-02",
                            "roundNumber": 1041,
                            "roundOpen": "2025-07-02",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-01",
                            "roundNumber": 1040,
                            "roundOpen": "2025-07-01",
                            "status": "none",
                            "timestamp": null
                        }
                    ],
                    "latestUserScores": null,
                    "name": "fncc_xgboost",
                    "profileUrl": null,
                    "returns": null,
                    "submissionWebhook": null,
                    "tournament": 12,
                    "v2Stake": {
                        "latestValue": "1.000000000000000000",
                        "latestValueSettled": "1.000000000000000000",
                        "pendingV2ChangeStakeRequest": null,
                        "stakeValue": "1.000000000000000000",
                        "status": null
                    }
                },
                {
                    "computeEnabled": true,
                    "computePickleUpload": null,
                    "currentPayoutSelection": {
                        "corrMultiplier": 0.5,
                        "mmcMultiplier": 2.0,
                        "takeProfit": false,
                        "updatedAt": null
                    },
                    "description": null,
                    "earliestReleaseDate": "2025-09-24T00:00:00Z",
                    "id": "70605aee-c62c-4826-9367-cf0c7fca73bc",
                    "isComputeWeekdayEnabled": true,
                    "latestSubmissions": [
                        {
                            "filename": "hybrid_ft_predictions_20250924_045133-S0UUkxR8auee.csv",
                            "id": "e61d2880-12b0-42ba-9137-f2f647fb6a46",
                            "roundCloseStaking": "2025-09-24",
                            "roundNumber": 1101,
                            "roundOpen": "2025-09-24",
                            "status": "queued",
                            "timestamp": "2025-09-24T04:53:16Z"
                        },
                        {
                            "filename": "hybrid_ft_predictions_20250924_045133-S0UUkxR8auee.csv",
                            "id": "e61d2880-12b0-42ba-9137-f2f647fb6a46",
                            "roundCloseStaking": "2025-09-23",
                            "roundNumber": 1100,
                            "roundOpen": "2025-09-23",
                            "status": "late",
                            "timestamp": "2025-09-24T04:53:16Z"
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-22",
                            "roundNumber": 1099,
                            "roundOpen": "2025-09-20",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-19",
                            "roundNumber": 1098,
                            "roundOpen": "2025-09-19",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-18",
                            "roundNumber": 1097,
                            "roundOpen": "2025-09-18",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-17",
                            "roundNumber": 1096,
                            "roundOpen": "2025-09-17",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-16",
                            "roundNumber": 1095,
                            "roundOpen": "2025-09-16",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-15",
                            "roundNumber": 1094,
                            "roundOpen": "2025-09-13",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-12",
                            "roundNumber": 1093,
                            "roundOpen": "2025-09-12",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-11",
                            "roundNumber": 1092,
                            "roundOpen": "2025-09-11",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-10",
                            "roundNumber": 1091,
                            "roundOpen": "2025-09-10",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-09",
                            "roundNumber": 1090,
                            "roundOpen": "2025-09-09",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-08",
                            "roundNumber": 1089,
                            "roundOpen": "2025-09-06",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-05",
                            "roundNumber": 1088,
                            "roundOpen": "2025-09-05",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-04",
                            "roundNumber": 1087,
                            "roundOpen": "2025-09-04",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-03",
                            "roundNumber": 1086,
                            "roundOpen": "2025-09-03",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-02",
                            "roundNumber": 1085,
                            "roundOpen": "2025-09-02",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-09-01",
                            "roundNumber": 1084,
                            "roundOpen": "2025-08-30",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-29",
                            "roundNumber": 1083,
                            "roundOpen": "2025-08-29",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-28",
                            "roundNumber": 1082,
                            "roundOpen": "2025-08-28",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-27",
                            "roundNumber": 1081,
                            "roundOpen": "2025-08-27",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-26",
                            "roundNumber": 1080,
                            "roundOpen": "2025-08-26",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-25",
                            "roundNumber": 1079,
                            "roundOpen": "2025-08-23",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-22",
                            "roundNumber": 1078,
                            "roundOpen": "2025-08-22",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-21",
                            "roundNumber": 1077,
                            "roundOpen": "2025-08-21",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-20",
                            "roundNumber": 1076,
                            "roundOpen": "2025-08-20",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-19",
                            "roundNumber": 1075,
                            "roundOpen": "2025-08-19",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-18",
                            "roundNumber": 1074,
                            "roundOpen": "2025-08-16",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-15",
                            "roundNumber": 1073,
                            "roundOpen": "2025-08-15",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-14",
                            "roundNumber": 1072,
                            "roundOpen": "2025-08-14",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-13",
                            "roundNumber": 1071,
                            "roundOpen": "2025-08-13",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-12",
                            "roundNumber": 1070,
                            "roundOpen": "2025-08-12",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-11",
                            "roundNumber": 1069,
                            "roundOpen": "2025-08-09",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-08",
                            "roundNumber": 1068,
                            "roundOpen": "2025-08-08",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-07",
                            "roundNumber": 1067,
                            "roundOpen": "2025-08-07",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-06",
                            "roundNumber": 1066,
                            "roundOpen": "2025-08-06",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-05",
                            "roundNumber": 1065,
                            "roundOpen": "2025-08-05",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-04",
                            "roundNumber": 1064,
                            "roundOpen": "2025-08-02",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-08-01",
                            "roundNumber": 1063,
                            "roundOpen": "2025-08-01",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-31",
                            "roundNumber": 1062,
                            "roundOpen": "2025-07-31",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-30",
                            "roundNumber": 1061,
                            "roundOpen": "2025-07-30",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-29",
                            "roundNumber": 1060,
                            "roundOpen": "2025-07-29",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-28",
                            "roundNumber": 1059,
                            "roundOpen": "2025-07-26",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-25",
                            "roundNumber": 1058,
                            "roundOpen": "2025-07-25",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-24",
                            "roundNumber": 1057,
                            "roundOpen": "2025-07-24",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-23",
                            "roundNumber": 1056,
                            "roundOpen": "2025-07-23",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-22",
                            "roundNumber": 1055,
                            "roundOpen": "2025-07-22",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-21",
                            "roundNumber": 1054,
                            "roundOpen": "2025-07-19",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-18",
                            "roundNumber": 1053,
                            "roundOpen": "2025-07-18",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-17",
                            "roundNumber": 1052,
                            "roundOpen": "2025-07-17",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-16",
                            "roundNumber": 1051,
                            "roundOpen": "2025-07-16",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-15",
                            "roundNumber": 1050,
                            "roundOpen": "2025-07-15",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-14",
                            "roundNumber": 1049,
                            "roundOpen": "2025-07-12",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-11",
                            "roundNumber": 1048,
                            "roundOpen": "2025-07-11",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-10",
                            "roundNumber": 1047,
                            "roundOpen": "2025-07-10",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-09",
                            "roundNumber": 1046,
                            "roundOpen": "2025-07-09",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-08",
                            "roundNumber": 1045,
                            "roundOpen": "2025-07-08",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-07",
                            "roundNumber": 1044,
                            "roundOpen": "2025-07-05",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-04",
                            "roundNumber": 1043,
                            "roundOpen": "2025-07-04",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-03",
                            "roundNumber": 1042,
                            "roundOpen": "2025-07-03",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-02",
                            "roundNumber": 1041,
                            "roundOpen": "2025-07-02",
                            "status": "none",
                            "timestamp": null
                        },
                        {
                            "filename": null,
                            "id": null,
                            "roundCloseStaking": "2025-07-01",
                            "roundNumber": 1040,
                            "roundOpen": "2025-07-01",
                            "status": "none",
                            "timestamp": null
                        }
                    ],
                    "latestUserScores": null,
                    "name": "fnc_ft",
                    "profileUrl": null,
                    "returns": null,
                    "submissionWebhook": "https://numerai.imperialai.ai/numerai-70605aee-c62c-4826-9367-cf0c7fca73bc/",
                    "tournament": 8,
                    "v2Stake": {
                        "latestValue": null,
                        "latestValueSettled": null,
                        "pendingV2ChangeStakeRequest": null,
                        "stakeValue": null,
                        "status": null
                    }
                }
            ],
            "profileUrl": "https://numerai-public-images.s3-us-west-2.amazonaws.com/profile_images/fish_n_chips-55snn4z8Qafh.jpg",
            "reports": [],
            "username": "fish_n_chips",
            "walletAddress": "0x000000000000000000000000000000000002fe61"
        }
    }
}


### Account Profile (accountProfile)
The following query will get the user's account details:



Request Payload:
{"query":"\n    query accountProfile($username: String!, $tournament: Int) {\n      accountProfile(username: $username, tournament: $tournament) {\n          id\n          username\n          title\n          achievements {\n            date\n            rank\n            type\n            season\n            tier\n          }\n          tournament\n          displayName\n          bio\n          github\n          kaggle\n          linkedin\n          twitter\n          discord {\n            userId\n            username\n          }\n          profileUrl\n          location\n          website\n          startDate\n          team\n          scores {\n            tcLtmRank\n            v2Corr20LtmRank\n            fncV4LtmRank\n            mmcLtmRank\n            corrLtmRank\n            seasonRank\n            corr60LtmRank\n            mmc60LtmRank\n            alphaLtmRank\n            mpcLtmRank\n          }\n          scoresTs {\n            date\n            tc\n            tcLtm\n            v2Corr20\n            v2Corr20Ltm\n            fncV4\n            fncV4Ltm\n            mmc\n            mmcLtm\n            corr\n            corrLtm\n            corr60\n            corr60Ltm\n            mmc60\n            mmc60Ltm\n            alpha\n            alphaLtm\n            mpc\n            mpcLtm\n          }\n          returns {\n            allTime\n            allTimeNmr\n            oneYear\n            oneYearNmr\n          }\n          returnsTs {\n            allTime\n            date\n            oneYear\n          }\n          totalStake\n          totalStakeTs {\n            delta\n            date\n            value\n          }\n          models {\n            displayName\n            stake\n            profileUrl\n            return1y\n            tcRep\n            corr20V2Rep\n            fncV4Rep\n            mmcRep\n            corrRep\n            mmc60Rep\n            corr60Rep\n            alphaRep\n            mpcRep\n          }\n        }\n      }\n    ","variables":{"username":"benchmark_models","tournament":8}}



Response:
{
    "data": {
        "accountProfile": {
            "achievements": [
                {
                    "date": "2024-02-01",
                    "rank": 177,
                    "season": "2023",
                    "tier": "Researcher",
                    "type": "canon_tc"
                },
                {
                    "date": "2024-02-01",
                    "rank": 38,
                    "season": "2023",
                    "tier": "Expert",
                    "type": "canon_corr"
                },
                {
                    "date": "2023-10-30",
                    "rank": 21,
                    "season": "2022",
                    "tier": "Expert",
                    "type": "canon_tc"
                },
                {
                    "date": "2023-10-30",
                    "rank": 65,
                    "season": "2022",
                    "tier": "Expert",
                    "type": "canon_corr"
                }
            ],
            "bio": "Submits example scripts and benchmark models developed by Numerai.",
            "discord": {
                "userId": null,
                "username": null
            },
            "displayName": "Numerai Benchmark Models",
            "github": "numerai",
            "id": "59de8728-38e5-45bd-a3d5-9d4ad649dd3f",
            "kaggle": null,
            "linkedin": null,
            "location": "San Francisco, CA",
            "models": [
                {
                    "alphaRep": null,
                    "corr20V2Rep": 0.01556131518512944,
                    "corr60Rep": 0.02479582372544827,
                    "corrRep": null,
                    "displayName": "nb_example_model",
                    "fncV4Rep": null,
                    "mmc60Rep": -5.490772884181891e-4,
                    "mmcRep": -0.0015410222225609239,
                    "mpcRep": null,
                    "profileUrl": "https://numerai-public-images.s3.amazonaws.com/profile_images/1h7VM_cL_400x400-bMm0lvKCjiCj (1)-AFhMiRNB4zYK.jpg",
                    "return1y": 20.93925715390792,
                    "stake": "7.088561343807214000",
                    "tcRep": 0.0
                },
                {
                    "alphaRep": null,
                    "corr20V2Rep": 0.015658998556776948,
                    "corr60Rep": 0.024915427441923366,
                    "corrRep": null,
                    "displayName": "nb_hello_numerai",
                    "fncV4Rep": null,
                    "mmc60Rep": -6.926548746250855e-4,
                    "mmcRep": -0.0015560084677716521,
                    "mpcRep": null,
                    "profileUrl": "https://numerai-public-images.s3.amazonaws.com/profile_images/black_sigil.-6sFyeVA28kk8.jpg",
                    "return1y": 20.51452543611835,
                    "stake": "7.104201391159314000",
                    "tcRep": 0.0
                },
                {
                    "alphaRep": null,
                    "corr20V2Rep": 0.013795698039002855,
                    "corr60Rep": 0.021867839969211395,
                    "corrRep": null,
                    "displayName": "nb_feat_neutral",
                    "fncV4Rep": null,
                    "mmc60Rep": -0.003337764888690361,
                    "mmcRep": -0.004000775261983734,
                    "mpcRep": null,
                    "profileUrl": "https://numerai-public-images.s3.amazonaws.com/profile_images/1h7VM_cL_400x400-bMm0lvKCjiCj (1)-qGneZXXvKMyC.jpg",
                    "return1y": 1.6420394972064458,
                    "stake": "5.405591059731945000",
                    "tcRep": 0.0
                },
                {
                    "alphaRep": null,
                    "corr20V2Rep": 0.015587617133547619,
                    "corr60Rep": 0.02466322193775615,
                    "corrRep": null,
                    "displayName": "nb_target_ensemble",
                    "fncV4Rep": null,
                    "mmc60Rep": -0.0010551154950109887,
                    "mmcRep": -0.0011159826648072697,
                    "mpcRep": null,
                    "profileUrl": "https://numerai-public-images.s3.amazonaws.com/profile_images/1h7VM_cL_400x400-bMm0lvKCjiCj (1)-Cmn59yc3Fm7t.jpg",
                    "return1y": 23.679098679770092,
                    "stake": "6.985527379794029000",
                    "tcRep": 0.0
                },
                {
                    "alphaRep": null,
                    "corr20V2Rep": 5.298702912494329e-5,
                    "corr60Rep": 0.0,
                    "corrRep": null,
                    "displayName": "deprecated_6",
                    "fncV4Rep": null,
                    "mmc60Rep": 0.0,
                    "mmcRep": -1.9023045116686756e-4,
                    "mpcRep": null,
                    "profileUrl": "https://numerai-public-images.s3.amazonaws.com/profile_images/1h7VM_cL_400x400-bMm0lvKCjiCj-FCJmL7v2dwKR.jpg",
                    "return1y": 0.0,
                    "stake": "0.000000000000000000",
                    "tcRep": 0.0
                },
                {
                    "alphaRep": null,
                    "corr20V2Rep": 1.0972209820121308e-4,
                    "corr60Rep": 0.0,
                    "corrRep": null,
                    "displayName": "deprecated_7",
                    "fncV4Rep": null,
                    "mmc60Rep": 0.0,
                    "mmcRep": -1.0237055544366723e-4,
                    "mpcRep": null,
                    "profileUrl": "https://numerai-public-images.s3.amazonaws.com/profile_images/1h7VM_cL_400x400-bMm0lvKCjiCj-9x3hpxnc7QOJ.jpg",
                    "return1y": 0.0,
                    "stake": "0.000000000000000000",
                    "tcRep": 0.0
                },
                {
                    "alphaRep": null,
                    "corr20V2Rep": 0.019223454861337433,
                    "corr60Rep": 0.0274770336268195,
                    "corrRep": null,
                    "displayName": "old_data_datestamp",
                    "fncV4Rep": null,
                    "mmc60Rep": -0.00667669398858158,
                    "mmcRep": -0.004858809088379544,
                    "mpcRep": null,
                    "profileUrl": "https://numerai-public-images.s3.amazonaws.com/profile_images/1h7VM_cL_400x400-IuD6b6cLPkaY.jpg",
                    "return1y": 0.0,
                    "stake": "0.000000000000000000",
                    "tcRep": 0.0
                },
                {
                    "alphaRep": null,
                    "corr20V2Rep": 0.0,
                    "corr60Rep": 0.0,
                    "corrRep": null,
                    "displayName": "benchmark_models_te",
                    "fncV4Rep": null,
                    "mmc60Rep": 0.0,
                    "mmcRep": 0.0,
                    "mpcRep": null,
                    "profileUrl": null,
                    "return1y": 0.0,
                    "stake": "0",
                    "tcRep": 0.0
                },
                {
                    "alphaRep": null,
                    "corr20V2Rep": 0.0,
                    "corr60Rep": 0.0,
                    "corrRep": null,
                    "displayName": "benchmark_models_fn",
                    "fncV4Rep": null,
                    "mmc60Rep": 0.0,
                    "mmcRep": 0.0,
                    "mpcRep": null,
                    "profileUrl": null,
                    "return1y": 0.0,
                    "stake": "0",
                    "tcRep": 0.0
                },
                {
                    "alphaRep": null,
                    "corr20V2Rep": 0.0013511575862068968,
                    "corr60Rep": 0.003612670153256705,
                    "corrRep": null,
                    "displayName": "v4_lgbm_waldo20",
                    "fncV4Rep": null,
                    "mmc60Rep": -0.0024842640613026816,
                    "mmcRep": -0.001111669731800766,
                    "mpcRep": null,
                    "profileUrl": "https://numerai-public-images.s3.amazonaws.com/profile_images/Screen Shot 2023-09-06 at 2.57.18 PM-5kp0AlvyuWYu.jpg",
                    "return1y": -5.685018633405272,
                    "stake": "0.000000000000000000",
                    "tcRep": 0.0
                },
                {
                    "alphaRep": null,
                    "corr20V2Rep": 0.001660589037416132,
                    "corr60Rep": 0.004118213180076629,
                    "corrRep": null,
                    "displayName": "v41_lgbm_caroline20",
                    "fncV4Rep": null,
                    "mmc60Rep": -0.0019260757471264366,
                    "mmcRep": -0.0011386147184273532,
                    "mpcRep": null,
                    "profileUrl": "https://numerai-public-images.s3.amazonaws.com/profile_images/sunshine.-yg304e5eNlEF.jpg",
                    "return1y": -4.578794826495449,
                    "stake": "0.000000000000000000",
                    "tcRep": 0.0
                },
                {
                    "alphaRep": null,
                    "corr20V2Rep": 0.0010679748275862068,
                    "corr60Rep": 0.004130651800766283,
                    "corrRep": null,
                    "displayName": "v41_lgbm_xerxes60",
                    "fncV4Rep": null,
                    "mmc60Rep": -0.0022032317241379314,
                    "mmcRep": -0.0016215197701149424,
                    "mpcRep": null,
                    "profileUrl": "https://numerai-public-images.s3.amazonaws.com/profile_images/sunshine.-yg304e5eNlEF.jpg",
                    "return1y": -9.40687471993259,
                    "stake": "0.000000000000000000",
                    "tcRep": 0.0
                },
                {
                    "alphaRep": null,
                    "corr20V2Rep": 0.001143556087224561,
                    "corr60Rep": 0.0028767292720306512,
                    "corrRep": null,
                    "displayName": "deprecated_3",
                    "fncV4Rep": null,
                    "mmc60Rep": 7.017907662835249e-4,
                    "mmcRep": 2.5768093762168866e-4,
                    "mpcRep": null,
                    "profileUrl": "https://numerai-public-images.s3.amazonaws.com/profile_images/1h7VM_cL_400x400-bMm0lvKCjiCj-gKpoBrlc5vcZ.jpg",
                    "return1y": 0.0,
                    "stake": "0.000000000000000000",
                    "tcRep": 0.0
                },
                {
                    "alphaRep": null,
                    "corr20V2Rep": 0.004314356245210728,
                    "corr60Rep": 0.008440320498084289,
                    "corrRep": null,
                    "displayName": "v43_lgbm_teager60",
                    "fncV4Rep": null,
                    "mmc60Rep": 0.0014503989146708812,
                    "mmcRep": 0.0011719634482758622,
                    "mpcRep": null,
                    "profileUrl": "https://numerai-public-images.s3.amazonaws.com/profile_images/midnight_art-A2wt7z4AIUe3.jpg",
                    "return1y": 15.222897796177648,
                    "stake": "0.000000000000000000",
                    "tcRep": 0.0
                },
                {
                    "alphaRep": null,
                    "corr20V2Rep": 1.9518214449905122e-4,
                    "corr60Rep": 0.002248785747126437,
                    "corrRep": null,
                    "displayName": "v4_example_preds",
                    "fncV4Rep": null,
                    "mmc60Rep": -0.0018402199616858233,
                    "mmcRep": -0.0017860379316022392,
                    "mpcRep": null,
                    "profileUrl": "https://numerai-public-images.s3.amazonaws.com/profile_images/Screen Shot 2023-09-06 at 2.57.18 PM-5kp0AlvyuWYu.jpg",
                    "return1y": -12.071983872364388,
                    "stake": "0.000000000000000000",
                    "tcRep": 0.0
                },
                {
                    "alphaRep": null,
                    "corr20V2Rep": 0.0010145435621235722,
                    "corr60Rep": 0.004375525478927203,
                    "corrRep": null,
                    "displayName": "v3_example_preds",
                    "fncV4Rep": null,
                    "mmc60Rep": -0.0012011326436781608,
                    "mmcRep": -0.0015748309967363388,
                    "mpcRep": null,
                    "profileUrl": "https://numerai-public-images.s3.amazonaws.com/profile_images/1h7VM_cL_400x400-FYwE2D7U9Cs3.jpg",
                    "return1y": -8.598687646369072,
                    "stake": "0.000000000000000000",
                    "tcRep": 0.0
                },
                {
                    "alphaRep": null,
                    "corr20V2Rep": 0.001815600847537314,
                    "corr60Rep": 0.0026879875065789266,
                    "corrRep": null,
                    "displayName": "v41_example_preds",
                    "fncV4Rep": null,
                    "mmc60Rep": -0.0033548018121977016,
                    "mmcRep": -0.0012742472780188099,
                    "mpcRep": null,
                    "profileUrl": "https://numerai-public-images.s3.amazonaws.com/profile_images/sunshine.-yg304e5eNlEF.jpg",
                    "return1y": -4.717905689267808,
                    "stake": "0.000000000000000000",
                    "tcRep": 0.0
                },
                {
                    "alphaRep": null,
                    "corr20V2Rep": 0.001630335359255212,
                    "corr60Rep": 0.004108522720306513,
                    "corrRep": null,
                    "displayName": "v4_lgbm_jerome60",
                    "fncV4Rep": null,
                    "mmc60Rep": -0.0013138431800766284,
                    "mmcRep": -8.741499436043651e-4,
                    "mpcRep": null,
                    "profileUrl": "https://numerai-public-images.s3.amazonaws.com/profile_images/Screen Shot 2023-09-06 at 2.57.18 PM-5kp0AlvyuWYu.jpg",
                    "return1y": -3.3667014383166345,
                    "stake": "0.000000000000000000",
                    "tcRep": 0.0
                },
                {
                    "alphaRep": null,
                    "corr20V2Rep": 0.003102526321839081,
                    "corr60Rep": 0.004323003103448275,
                    "corrRep": null,
                    "displayName": "v42_rain_ensemble2",
                    "fncV4Rep": null,
                    "mmc60Rep": -0.0025887313026819914,
                    "mmcRep": -1.5649754789272033e-4,
                    "mpcRep": null,
                    "profileUrl": "https://numerai-public-images.s3.amazonaws.com/profile_images/Screen Shot 2023-10-11 at 9.57.11 AM-ZRpoa2Nu8l0X.jpg",
                    "return1y": 4.7313202041579965,
                    "stake": "0.000000000000000000",
                    "tcRep": 0.0
                },
                {
                    "alphaRep": null,
                    "corr20V2Rep": 0.0016459106849257105,
                    "corr60Rep": 0.004123094674329503,
                    "corrRep": null,
                    "displayName": "v4_lgbm_ralph20",
                    "fncV4Rep": null,
                    "mmc60Rep": -0.0020629632950191577,
                    "mmcRep": -9.661627788534071e-4,
                    "mpcRep": null,
                    "profileUrl": "https://numerai-public-images.s3.amazonaws.com/profile_images/Screen Shot 2023-09-06 at 2.57.18 PM-5kp0AlvyuWYu.jpg",
                    "return1y": -3.9853341114321768,
                    "stake": "0.000000000000000000",
                    "tcRep": 0.0
                },
                {
                    "alphaRep": null,
                    "corr20V2Rep": 0.0013810386590038313,
                    "corr60Rep": 0.004735781187739464,
                    "corrRep": null,
                    "displayName": "v4_lgbm_tyler60",
                    "fncV4Rep": null,
                    "mmc60Rep": -8.428416091954023e-4,
                    "mmcRep": -9.172519540229884e-4,
                    "mpcRep": null,
                    "profileUrl": "https://numerai-public-images.s3.amazonaws.com/profile_images/Screen Shot 2023-09-06 at 2.57.18 PM-5kp0AlvyuWYu.jpg",
                    "return1y": -4.306084804948457,
                    "stake": "0.000000000000000000",
                    "tcRep": 0.0
                },
                {
                    "alphaRep": null,
                    "corr20V2Rep": 0.00354070908045977,
                    "corr60Rep": 0.004134208275862069,
                    "corrRep": null,
                    "displayName": "v42_lgbm_claudia20",
                    "fncV4Rep": null,
                    "mmc60Rep": -0.0020782043678160915,
                    "mmcRep": 4.34525785440613e-4,
                    "mpcRep": null,
                    "profileUrl": "https://numerai-public-images.s3.amazonaws.com/profile_images/rain_image.-kWXAGgZJDYtF.jpg",
                    "return1y": 9.995723018400275,
                    "stake": "0.000000000000000000",
                    "tcRep": 0.0
                },
                {
                    "alphaRep": null,
                    "corr20V2Rep": 0.001599999842013833,
                    "corr60Rep": 0.002494690788663219,
                    "corrRep": null,
                    "displayName": "numerai_cli_test",
                    "fncV4Rep": null,
                    "mmc60Rep": -6.820181226053639e-4,
                    "mmcRep": 4.7161857161918556e-5,
                    "mpcRep": null,
                    "profileUrl": "https://numerai-public-images.s3.amazonaws.com/profile_images/1h7VM_cL_400x400-bMm0lvKCjiCj (1)-d5Ljtu9Ct4cn.jpg",
                    "return1y": 0.0,
                    "stake": "0.000000000000000000",
                    "tcRep": 0.0
                },
                {
                    "alphaRep": null,
                    "corr20V2Rep": 0.0011927772796934866,
                    "corr60Rep": 0.004148395670498083,
                    "corrRep": null,
                    "displayName": "v41_lgbm_sam60",
                    "fncV4Rep": null,
                    "mmc60Rep": -0.0021056794636015322,
                    "mmcRep": -0.0014682273946360154,
                    "mpcRep": null,
                    "profileUrl": "https://numerai-public-images.s3.amazonaws.com/profile_images/sunshine.-yg304e5eNlEF.jpg",
                    "return1y": -7.82559258267635,
                    "stake": "0.000000000000000000",
                    "tcRep": 0.0
                },
                {
                    "alphaRep": null,
                    "corr20V2Rep": 0.003872582835249042,
                    "corr60Rep": 0.006875012298850575,
                    "corrRep": null,
                    "displayName": "v43_lgbm_teager20",
                    "fncV4Rep": null,
                    "mmc60Rep": -3.1172823754789275e-4,
                    "mmcRep": 4.691673563218391e-4,
                    "mpcRep": null,
                    "profileUrl": "https://numerai-public-images.s3.amazonaws.com/profile_images/midnight_art-4EDUpBFRbQ23.jpg",
                    "return1y": 10.488817259797216,
                    "stake": "0.000000000000000000",
                    "tcRep": 0.0
                },
                {
                    "alphaRep": null,
                    "corr20V2Rep": 0.003480520727969349,
                    "corr60Rep": 0.004484681264367817,
                    "corrRep": null,
                    "displayName": "v42_lgbm_ct_blend",
                    "fncV4Rep": null,
                    "mmc60Rep": -0.002840668812260537,
                    "mmcRep": -6.798799467432884e-7,
                    "mpcRep": null,
                    "profileUrl": "https://numerai-public-images.s3.amazonaws.com/profile_images/rain_image.-lm3uBCeBWY05.jpg",
                    "return1y": 6.6015922205892235,
                    "stake": "0.000000000000000000",
                    "tcRep": 0.0
                },
                {
                    "alphaRep": null,
                    "corr20V2Rep": 8.269738650023388e-4,
                    "corr60Rep": 0.0038388172413793106,
                    "corrRep": null,
                    "displayName": "v4_lgbm_ralph60",
                    "fncV4Rep": null,
                    "mmc60Rep": -0.0014283582457628352,
                    "mmcRep": -0.0015547969167844415,
                    "mpcRep": null,
                    "profileUrl": "https://numerai-public-images.s3.amazonaws.com/profile_images/Screen Shot 2023-09-06 at 2.57.18 PM-5kp0AlvyuWYu.jpg",
                    "return1y": -9.828149735843825,
                    "stake": "0.000000000000000000",
                    "tcRep": 0.0
                },
                {
                    "alphaRep": null,
                    "corr20V2Rep": 0.001087239995270538,
                    "corr60Rep": 0.001586634942528736,
                    "corrRep": null,
                    "displayName": "v4_lgbm_victor20",
                    "fncV4Rep": null,
                    "mmc60Rep": -0.00349026429118774,
                    "mmcRep": -0.0012075580662097292,
                    "mpcRep": null,
                    "profileUrl": "https://numerai-public-images.s3.amazonaws.com/profile_images/Screen Shot 2023-09-06 at 2.57.18 PM-5kp0AlvyuWYu.jpg",
                    "return1y": -6.627057100012493,
                    "stake": "0.000000000000000000",
                    "tcRep": 0.0
                },
                {
                    "alphaRep": null,
                    "corr20V2Rep": 5.986113641180076e-4,
                    "corr60Rep": 0.0026071590804597707,
                    "corrRep": null,
                    "displayName": "v4_lgbm_victor60",
                    "fncV4Rep": null,
                    "mmc60Rep": -0.0024139716475095785,
                    "mmcRep": -0.001446643754789272,
                    "mpcRep": null,
                    "profileUrl": "https://numerai-public-images.s3.amazonaws.com/profile_images/Screen Shot 2023-09-06 at 2.57.18 PM-5kp0AlvyuWYu.jpg",
                    "return1y": -9.152246201969685,
                    "stake": "0.000000000000000000",
                    "tcRep": 0.0
                },
                {
                    "alphaRep": null,
                    "corr20V2Rep": 0.0037198240613026817,
                    "corr60Rep": 0.007081402222222222,
                    "corrRep": null,
                    "displayName": "v43_lgbm_ct_blend",
                    "fncV4Rep": null,
                    "mmc60Rep": -8.897891978360151e-4,
                    "mmcRep": 5.242996307241368e-6,
                    "mpcRep": null,
                    "profileUrl": "https://numerai-public-images.s3.amazonaws.com/profile_images/midnight_art-eT16gX3Z2H5s.jpg",
                    "return1y": 6.789256090658123,
                    "stake": "0.000000000000000000",
                    "tcRep": 0.0
                },
                {
                    "alphaRep": null,
                    "corr20V2Rep": 0.003708885325670498,
                    "corr60Rep": 0.005798451915708811,
                    "corrRep": null,
                    "displayName": "v42_lgbm_teager60",
                    "fncV4Rep": null,
                    "mmc60Rep": -5.030719540229885e-4,
                    "mmcRep": 9.240005747126437e-4,
                    "mpcRep": null,
                    "profileUrl": "https://numerai-public-images.s3.amazonaws.com/profile_images/rain_image.-4EkdIzlKyvzJ.jpg",
                    "return1y": 12.608421371220725,
                    "stake": "0.000000000000000000",
                    "tcRep": 0.0
                },
                {
                    "alphaRep": null,
                    "corr20V2Rep": 0.0015252205699831818,
                    "corr60Rep": 0.004019811570881227,
                    "corrRep": null,
                    "displayName": "v41_lgbm_caroline60",
                    "fncV4Rep": null,
                    "mmc60Rep": -0.002205601072796935,
                    "mmcRep": -0.0013389602501177752,
                    "mpcRep": null,
                    "profileUrl": "https://numerai-public-images.s3.amazonaws.com/profile_images/sunshine.-yg304e5eNlEF.jpg",
                    "return1y": -6.633864695952846,
                    "stake": "0.000000000000000000",
                    "tcRep": 0.0
                },
                {
                    "alphaRep": null,
                    "corr20V2Rep": 8.023235201747525e-4,
                    "corr60Rep": 0.0034607865690739455,
                    "corrRep": null,
                    "displayName": "v4_lgbm_nomi60",
                    "fncV4Rep": null,
                    "mmc60Rep": -0.0019514257854406128,
                    "mmcRep": -0.0015200967635277366,
                    "mpcRep": null,
                    "profileUrl": "https://numerai-public-images.s3.amazonaws.com/profile_images/Screen Shot 2023-09-06 at 2.57.18 PM-5kp0AlvyuWYu.jpg",
                    "return1y": -9.487115297414313,
                    "stake": "0.000000000000000000",
                    "tcRep": 0.0
                },
                {
                    "alphaRep": null,
                    "corr20V2Rep": 0.0029604120689655173,
                    "corr60Rep": 0.00634658724137931,
                    "corrRep": null,
                    "displayName": "v43_lgbm_cyrus20",
                    "fncV4Rep": null,
                    "mmc60Rep": -0.001332664827586207,
                    "mmcRep": -4.471230268199234e-4,
                    "mpcRep": null,
                    "profileUrl": "https://numerai-public-images.s3.amazonaws.com/profile_images/midnight_art-oIWZRna9bKuk.jpg",
                    "return1y": 2.0942052097978285,
                    "stake": "0.000000000000000000",
                    "tcRep": 0.0
                },
                {
                    "alphaRep": null,
                    "corr20V2Rep": 5.614990850852069e-4,
                    "corr60Rep": 0.0021271938314176247,
                    "corrRep": null,
                    "displayName": "v2_example_preds",
                    "fncV4Rep": null,
                    "mmc60Rep": -0.002742343295019157,
                    "mmcRep": -0.0017820214159498446,
                    "mpcRep": null,
                    "profileUrl": "https://numerai-public-images.s3.amazonaws.com/profile_images/1h7VM_cL_400x400-sdQHqDEufBEe.jpg",
                    "return1y": -11.151225947336002,
                    "stake": "0.000000000000000000",
                    "tcRep": 0.0
                },
                {
                    "alphaRep": null,
                    "corr20V2Rep": 0.0016398080459770117,
                    "corr60Rep": 0.004082238467432949,
                    "corrRep": null,
                    "displayName": "v41_lgbm_cyrus20",
                    "fncV4Rep": null,
                    "mmc60Rep": -0.002228700536398468,
                    "mmcRep": -0.0011659290421455939,
                    "mpcRep": null,
                    "profileUrl": "https://numerai-public-images.s3.amazonaws.com/profile_images/sunshine.-yg304e5eNlEF.jpg",
                    "return1y": -4.873461004394259,
                    "stake": "0.000000000000000000",
                    "tcRep": 0.0
                },
                {
                    "alphaRep": null,
                    "corr20V2Rep": 0.0032837689272030655,
                    "corr60Rep": 0.0033543550191570876,
                    "corrRep": null,
                    "displayName": "v42_lgbm_rowan20",
                    "fncV4Rep": null,
                    "mmc60Rep": -0.0027284715708812256,
                    "mmcRep": 3.393030651340996e-4,
                    "mpcRep": null,
                    "profileUrl": "https://numerai-public-images.s3.amazonaws.com/profile_images/rain_image.-uZyGxtciYAJc.jpg",
                    "return1y": 8.47849950712248,
                    "stake": "0.000000000000000000",
                    "tcRep": 0.0
                },
                {
                    "alphaRep": null,
                    "corr20V2Rep": 0.0011653754069242874,
                    "corr60Rep": 0.003089220957854406,
                    "corrRep": null,
                    "displayName": "v4_lgbm_nomi20",
                    "fncV4Rep": null,
                    "mmc60Rep": -0.002793729157088122,
                    "mmcRep": -0.0013645180443023351,
                    "mpcRep": null,
                    "profileUrl": "https://numerai-public-images.s3.amazonaws.com/profile_images/Screen Shot 2023-09-06 at 2.57.18 PM-5kp0AlvyuWYu.jpg",
                    "return1y": -7.319641962819381,
                    "stake": "0.000000000000000000",
                    "tcRep": 0.0
                },
                {
                    "alphaRep": null,
                    "corr20V2Rep": 7.749137821552633e-5,
                    "corr60Rep": 0.0,
                    "corrRep": null,
                    "displayName": "deprecated_4",
                    "fncV4Rep": null,
                    "mmc60Rep": 0.0,
                    "mmcRep": -1.86040077196109e-4,
                    "mpcRep": null,
                    "profileUrl": "https://numerai-public-images.s3.amazonaws.com/profile_images/1h7VM_cL_400x400-OtQR9OznJ62k.jpg",
                    "return1y": 0.0,
                    "stake": "0.000000000000000000",
                    "tcRep": 0.0
                },
                {
                    "alphaRep": null,
                    "corr20V2Rep": 7.749137821552633e-5,
                    "corr60Rep": 0.0,
                    "corrRep": null,
                    "displayName": "deprecated_5",
                    "fncV4Rep": null,
                    "mmc60Rep": 0.0,
                    "mmcRep": -1.86040077196109e-4,
                    "mpcRep": null,
                    "profileUrl": "https://numerai-public-images.s3.amazonaws.com/profile_images/1h7VM_cL_400x400-SlK9U75vdEo8.jpg",
                    "return1y": 0.0,
                    "stake": "0.000000000000000000",
                    "tcRep": 0.0
                },
                {
                    "alphaRep": null,
                    "corr20V2Rep": 0.0034444201532567048,
                    "corr60Rep": 0.004861638544061302,
                    "corrRep": null,
                    "displayName": "v42_teager_ensemble",
                    "fncV4Rep": null,
                    "mmc60Rep": -0.0026119155172413793,
                    "mmcRep": -4.52175478927203e-5,
                    "mpcRep": null,
                    "profileUrl": "https://numerai-public-images.s3.amazonaws.com/profile_images/rain_image.-fpdgen8otTca.jpg",
                    "return1y": 5.904646925584823,
                    "stake": "0.000000000000000000",
                    "tcRep": 0.0
                },
                {
                    "alphaRep": null,
                    "corr20V2Rep": 0.0011235013409961686,
                    "corr60Rep": 0.0032887507662835254,
                    "corrRep": null,
                    "displayName": "v4_lgbm_tyler20",
                    "fncV4Rep": null,
                    "mmc60Rep": -0.0025881348659003833,
                    "mmcRep": -0.0012831880459770115,
                    "mpcRep": null,
                    "profileUrl": "https://numerai-public-images.s3.amazonaws.com/profile_images/Screen Shot 2023-09-06 at 2.57.18 PM-5kp0AlvyuWYu.jpg",
                    "return1y": -7.41409240563372,
                    "stake": "0.000000000000000000",
                    "tcRep": 0.0
                },
                {
                    "alphaRep": null,
                    "corr20V2Rep": 0.003384924334127352,
                    "corr60Rep": 0.004649442893245594,
                    "corrRep": null,
                    "displayName": "v42_example_preds",
                    "fncV4Rep": null,
                    "mmc60Rep": -0.0025461824904214557,
                    "mmcRep": -2.2429045809543827e-4,
                    "mpcRep": null,
                    "profileUrl": "https://numerai-public-images.s3.amazonaws.com/profile_images/screenshot_2023-09-04_at_7.48.28_pm-HUu5qSHm7g3O.jpg",
                    "return1y": 5.115768853210556,
                    "stake": "0.000000000000000000",
                    "tcRep": 0.0
                },
                {
                    "alphaRep": null,
                    "corr20V2Rep": 0.0031727934099616863,
                    "corr60Rep": 0.0037417288122605368,
                    "corrRep": null,
                    "displayName": "v42_lgbm_teager20",
                    "fncV4Rep": null,
                    "mmc60Rep": -0.0026779758237547896,
                    "mmcRep": 1.2265812260536395e-4,
                    "mpcRep": null,
                    "profileUrl": "https://numerai-public-images.s3.amazonaws.com/profile_images/rain_image.-vqLX8hddyAwE.jpg",
                    "return1y": 6.988032564955703,
                    "stake": "0.000000000000000000",
                    "tcRep": 0.0
                },
                {
                    "alphaRep": null,
                    "corr20V2Rep": 0.0017537697318007661,
                    "corr60Rep": 0.004326535287356323,
                    "corrRep": null,
                    "displayName": "v41_lgbm_sam20",
                    "fncV4Rep": null,
                    "mmc60Rep": -0.0018158678927203066,
                    "mmcRep": -9.723160153256706e-4,
                    "mpcRep": null,
                    "profileUrl": "https://numerai-public-images.s3.amazonaws.com/profile_images/sunshine.-yg304e5eNlEF.jpg",
                    "return1y": -3.1665045709478985,
                    "stake": "0.000000000000000000",
                    "tcRep": 0.0
                },
                {
                    "alphaRep": null,
                    "corr20V2Rep": 0.0031826963218390806,
                    "corr60Rep": 0.007543084099616858,
                    "corrRep": null,
                    "displayName": "v43_lgbm_cyrus60",
                    "fncV4Rep": null,
                    "mmc60Rep": -1.9059079384482758e-4,
                    "mmcRep": -1.4830616858237548e-4,
                    "mpcRep": null,
                    "profileUrl": "https://numerai-public-images.s3.amazonaws.com/profile_images/midnight_art-v6Ld8U9qRW1d.jpg",
                    "return1y": 3.9001999535351404,
                    "stake": "0.000000000000000000",
                    "tcRep": 0.0
                },
                {
                    "alphaRep": null,
                    "corr20V2Rep": 0.001610957701149425,
                    "corr60Rep": 0.002484032835249042,
                    "corrRep": null,
                    "displayName": "v42_lgbm_agnes20",
                    "fncV4Rep": null,
                    "mmc60Rep": -0.003182980153256705,
                    "mmcRep": -0.0010102261302681991,
                    "mpcRep": null,
                    "profileUrl": "https://numerai-public-images.s3.amazonaws.com/profile_images/rain_image.-VRuZhbJLJ0ve.jpg",
                    "return1y": -4.348366595674717,
                    "stake": "0.000000000000000000",
                    "tcRep": 0.0
                },
                {
                    "alphaRep": null,
                    "corr20V2Rep": 0.001356585440613027,
                    "corr60Rep": 0.004356522596329118,
                    "corrRep": null,
                    "displayName": "v41_lgbm_cyrus60",
                    "fncV4Rep": null,
                    "mmc60Rep": -0.0021466790804597702,
                    "mmcRep": -0.0013969975095785437,
                    "mpcRep": null,
                    "profileUrl": "https://numerai-public-images.s3.amazonaws.com/profile_images/sunshine.-yg304e5eNlEF.jpg",
                    "return1y": -7.3320652261999255,
                    "stake": "0.000000000000000000",
                    "tcRep": 0.0
                },
                {
                    "alphaRep": null,
                    "corr20V2Rep": 0.002067816015325671,
                    "corr60Rep": 0.004402799042145594,
                    "corrRep": null,
                    "displayName": "v41_lgbm_xerxes20",
                    "fncV4Rep": null,
                    "mmc60Rep": -0.0019829961949398467,
                    "mmcRep": -8.048319540229884e-4,
                    "mpcRep": null,
                    "profileUrl": "https://numerai-public-images.s3.amazonaws.com/profile_images/sunshine.-yg304e5eNlEF.jpg",
                    "return1y": -1.6250287807816297,
                    "stake": "0.000000000000000000",
                    "tcRep": 0.0
                },
                {
                    "alphaRep": null,
                    "corr20V2Rep": 0.0011762021072796935,
                    "corr60Rep": 0.0043360267049808434,
                    "corrRep": null,
                    "displayName": "v4_lgbm_waldo60",
                    "fncV4Rep": null,
                    "mmc60Rep": -0.0012186118007662837,
                    "mmcRep": -0.0012094549042145593,
                    "mpcRep": null,
                    "profileUrl": "https://numerai-public-images.s3.amazonaws.com/profile_images/Screen Shot 2023-09-06 at 2.57.18 PM-5kp0AlvyuWYu.jpg",
                    "return1y": -6.720148351259739,
                    "stake": "0.000000000000000000",
                    "tcRep": 0.0
                },
                {
                    "alphaRep": null,
                    "corr20V2Rep": 0.0028810780076628352,
                    "corr60Rep": 0.00466059398467433,
                    "corrRep": null,
                    "displayName": "v42_rain_ensemble",
                    "fncV4Rep": null,
                    "mmc60Rep": -0.00275419724137931,
                    "mmcRep": -4.306501915708812e-4,
                    "mpcRep": null,
                    "profileUrl": "https://numerai-public-images.s3.amazonaws.com/profile_images/screenshot_2023-09-04_at_7.48.28_pm-HUu5qSHm7g3O-08x077jsRYdR.jpg",
                    "return1y": 2.134166346301017,
                    "stake": "0.000000000000000000",
                    "tcRep": 0.0
                },
                {
                    "alphaRep": null,
                    "corr20V2Rep": 0.0014503968151939096,
                    "corr60Rep": 0.003458772260536399,
                    "corrRep": null,
                    "displayName": "v4_lgbm_jerome20",
                    "fncV4Rep": null,
                    "mmc60Rep": -0.00255476913887433,
                    "mmcRep": -0.0011252455757882732,
                    "mpcRep": null,
                    "profileUrl": "https://numerai-public-images.s3.amazonaws.com/profile_images/Screen Shot 2023-09-06 at 2.57.18 PM-5kp0AlvyuWYu.jpg",
                    "return1y": -5.689527609221686,
                    "stake": "0.000000000000000000",
                    "tcRep": 0.0
                },
                {
                    "alphaRep": null,
                    "corr20V2Rep": 0.017247193160523457,
                    "corr60Rep": 0.02337691304114739,
                    "corrRep": null,
                    "displayName": "v5_lgbm_teager2b",
                    "fncV4Rep": null,
                    "mmc60Rep": -0.002908348797862541,
                    "mmcRep": -0.0025445913422372105,
                    "mpcRep": null,
                    "profileUrl": "https://numerai-public-images.s3-us-west-2.amazonaws.com/profile_images/GXXkoR6bkAAxLMJ-yQSzeuJ7bMUW.jpeg",
                    "return1y": 0.0,
                    "stake": "48.376452071608620000",
                    "tcRep": 0.0
                },
                {
                    "alphaRep": null,
                    "corr20V2Rep": 0.019753466380970877,
                    "corr60Rep": 0.026936241271050723,
                    "corrRep": null,
                    "displayName": "v5_lgbm_cyrusd",
                    "fncV4Rep": null,
                    "mmc60Rep": -0.0043842769723955255,
                    "mmcRep": -0.004027106477853769,
                    "mpcRep": null,
                    "profileUrl": "https://numerai-public-images.s3-us-west-2.amazonaws.com/profile_images/GXXkoR6bkAAxLMJ-X5vUQfZGb0zR.jpeg",
                    "return1y": 0.0,
                    "stake": "43.706794983021750000",
                    "tcRep": 0.0
                },
                {
                    "alphaRep": null,
                    "corr20V2Rep": 0.019297465546609154,
                    "corr60Rep": 0.026652427054413154,
                    "corrRep": null,
                    "displayName": "v5_example_preds",
                    "fncV4Rep": null,
                    "mmc60Rep": -0.0037268216358883875,
                    "mmcRep": -0.0034496364032431857,
                    "mpcRep": null,
                    "profileUrl": "https://numerai-public-images.s3-us-west-2.amazonaws.com/profile_images/GXXkoR6bkAAxLMJ-eJjsNFzzZUMY.jpeg",
                    "return1y": 0.0,
                    "stake": "45.677191513982635000",
                    "tcRep": 0.0
                },
                {
                    "alphaRep": null,
                    "corr20V2Rep": 0.022931124128984633,
                    "corr60Rep": 0.03185876398927906,
                    "corrRep": null,
                    "displayName": "integration_test",
                    "fncV4Rep": null,
                    "mmc60Rep": -0.004831951868207161,
                    "mmcRep": -0.003412396625326748,
                    "mpcRep": null,
                    "profileUrl": "https://numerai-public-images.s3.amazonaws.com/profile_images/weekend-Qzl7KmFRcrH6.jpg",
                    "return1y": 16.041751824530394,
                    "stake": "34.075703442890860000",
                    "tcRep": 0.0
                },
                {
                    "alphaRep": null,
                    "corr20V2Rep": 0.01929730445309092,
                    "corr60Rep": 0.02634490989061147,
                    "corrRep": null,
                    "displayName": "v5_lgbm_ct_blend",
                    "fncV4Rep": null,
                    "mmc60Rep": -0.003823690084095341,
                    "mmcRep": -0.0034496989812487517,
                    "mpcRep": null,
                    "profileUrl": "https://numerai-public-images.s3-us-west-2.amazonaws.com/profile_images/GXXkoR6bkAAxLMJ-g2GyWA3ZrKH8.jpeg",
                    "return1y": 0.0,
                    "stake": "136.763033423589040000",
                    "tcRep": 0.0
                }
            ],
            "profileUrl": "https://numerai-public-images.s3.amazonaws.com/profile_images/black_sigil.-a9rgQsDDV5XS.jpg",
            "returns": {
                "allTime": 941.1323858641507,
                "allTimeNmr": "255.139486418690520000",
                "oneYear": 15.503511099440548,
                "oneYearNmr": "18.220791836491514000"
            },
            "returnsTs": [
                {
                    "allTime": 941.1323858641507,
                    "date": "2025-09-23",
                    "oneYear": 15.503511099440548
                },
                {
                    "allTime": 941.1567080410881,
                    "date": "2025-09-20",
                    "oneYear": 15.476369133226623
                },
                {
                    "allTime": 941.2865138170183,
                    "date": "2025-09-19",
                    "oneYear": 15.467742499775683
                },
                {
                    "allTime": 941.2264320288446,
                    "date": "2025-09-18",
                    "oneYear": 15.200366985051662
                },
                {
                    "allTime": 940.9771555303373,
                    "date": "2025-09-17",
                    "oneYear": 14.975519208784588
                },
                {
                    "allTime": 940.8197828851372,
                    "date": "2025-09-16",
                    "oneYear": 14.983510996731418
                },
                {
                    "allTime": 940.7282518512579,
                    "date": "2025-09-13",
                    "oneYear": 15.100254843799858
                },
                {
                    "allTime": 940.4537443363505,
                    "date": "2025-09-12",
                    "oneYear": 15.004301384983588
                },
                {
                    "allTime": 940.29919651925,
                    "date": "2025-09-11",
                    "oneYear": 14.997842464453901
                },
                {
                    "allTime": 940.2150011731392,
                    "date": "2025-09-10",
                    "oneYear": 14.890958875020942
                },
                {
                    "allTime": 940.2627691984384,
                    "date": "2025-09-09",
                    "oneYear": 15.119417345682217
                },
                {
                    "allTime": 940.4832501462118,
                    "date": "2025-09-06",
                    "oneYear": 15.294588595942676
                },
                {
                    "allTime": 940.7233113968011,
                    "date": "2025-09-05",
                    "oneYear": 15.25007096867738
                },
                {
                    "allTime": 941.0211556999856,
                    "date": "2025-09-04",
                    "oneYear": 15.14100726389973
                },
                {
                    "allTime": 941.2106841445859,
                    "date": "2025-09-03",
                    "oneYear": 14.976893961671436
                },
                {
                    "allTime": 941.0786378442275,
                    "date": "2025-09-02",
                    "oneYear": 14.944887042188011
                },
                {
                    "allTime": 941.0278154858604,
                    "date": "2025-08-30",
                    "oneYear": 15.07096370503599
                },
                {
                    "allTime": 941.2765744824504,
                    "date": "2025-08-29",
                    "oneYear": 15.24845559223427
                },
                {
                    "allTime": 941.2997737523934,
                    "date": "2025-08-28",
                    "oneYear": 15.43651312564917
                },
                {
                    "allTime": 941.3815880653221,
                    "date": "2025-08-27",
                    "oneYear": 15.683017638778278
                },
                {
                    "allTime": 941.4487105697592,
                    "date": "2025-08-26",
                    "oneYear": 15.938614679842734
                },
                {
                    "allTime": 941.3498604109043,
                    "date": "2025-08-23",
                    "oneYear": 16.09164220234656
                },
                {
                    "allTime": 941.4087965920656,
                    "date": "2025-08-22",
                    "oneYear": 16.22190037440718
                },
                {
                    "allTime": 941.301805534118,
                    "date": "2025-08-21",
                    "oneYear": 16.147992038223645
                },
                {
                    "allTime": 941.1013392170825,
                    "date": "2025-08-20",
                    "oneYear": 16.08259246621088
                },
                {
                    "allTime": 941.3158045830148,
                    "date": "2025-08-19",
                    "oneYear": 16.080717797148214
                },
                {
                    "allTime": 941.268394045626,
                    "date": "2025-08-16",
                    "oneYear": 15.93288421240497
                },
                {
                    "allTime": 941.1976097861707,
                    "date": "2025-08-15",
                    "oneYear": 15.877249649394734
                },
                {
                    "allTime": 941.1492219770952,
                    "date": "2025-08-14",
                    "oneYear": 16.047219234584336
                },
                {
                    "allTime": 941.0696681543925,
                    "date": "2025-08-13",
                    "oneYear": 16.257186693991194
                },
                {
                    "allTime": 940.937061856069,
                    "date": "2025-08-12",
                    "oneYear": 16.496833417450546
                },
                {
                    "allTime": 940.7608544756068,
                    "date": "2025-08-09",
                    "oneYear": 16.6155169197286
                },
                {
                    "allTime": 940.7429569247404,
                    "date": "2025-08-08",
                    "oneYear": 16.896538329406773
                },
                {
                    "allTime": 940.5351803222642,
                    "date": "2025-08-07",
                    "oneYear": 17.438924510738477
                },
                {
                    "allTime": 940.1897870328878,
                    "date": "2025-08-06",
                    "oneYear": 17.83760595731759
                },
                {
                    "allTime": 939.8010051958555,
                    "date": "2025-08-05",
                    "oneYear": 18.238665285261966
                },
                {
                    "allTime": 939.6322411938659,
                    "date": "2025-08-02",
                    "oneYear": 18.44412015456098
                },
                {
                    "allTime": 939.4959381198005,
                    "date": "2025-08-01",
                    "oneYear": 18.829254060835108
                },
                {
                    "allTime": 939.6049602324747,
                    "date": "2025-07-31",
                    "oneYear": 19.33773419970368
                },
                {
                    "allTime": 939.4695609979068,
                    "date": "2025-07-30",
                    "oneYear": 19.784685093386727
                },
                {
                    "allTime": 939.6840503052177,
                    "date": "2025-07-29",
                    "oneYear": 20.572342649015294
                },
                {
                    "allTime": 940.046210052607,
                    "date": "2025-07-26",
                    "oneYear": 21.367655520194035
                },
                {
                    "allTime": 940.3121101484359,
                    "date": "2025-07-25",
                    "oneYear": 22.181192073168358
                },
                {
                    "allTime": 940.3170791995791,
                    "date": "2025-07-24",
                    "oneYear": 22.756069454029877
                },
                {
                    "allTime": 940.5467982415641,
                    "date": "2025-07-23",
                    "oneYear": 23.470188226933068
                },
                {
                    "allTime": 940.7957821721764,
                    "date": "2025-07-22",
                    "oneYear": 23.891448882126717
                },
                {
                    "allTime": 940.8832033378076,
                    "date": "2025-07-19",
                    "oneYear": 24.327462974766323
                },
                {
                    "allTime": 940.9123931461394,
                    "date": "2025-07-18",
                    "oneYear": 24.81638388325944
                },
                {
                    "allTime": 941.2187260339999,
                    "date": "2025-07-17",
                    "oneYear": 25.292385497406197
                },
                {
                    "allTime": 941.4019620750607,
                    "date": "2025-07-16",
                    "oneYear": 25.593531618755755
                },
                {
                    "allTime": 941.5871706602791,
                    "date": "2025-07-15",
                    "oneYear": 25.918710456978285
                },
                {
                    "allTime": 941.8125803351295,
                    "date": "2025-07-12",
                    "oneYear": 26.43927901716826
                },
                {
                    "allTime": 942.2395573635642,
                    "date": "2025-07-11",
                    "oneYear": 26.988280146084122
                },
                {
                    "allTime": 942.5450211025865,
                    "date": "2025-07-10",
                    "oneYear": 27.42918377213144
                },
                {
                    "allTime": 942.6695730976305,
                    "date": "2025-07-09",
                    "oneYear": 27.896010456422538
                },
                {
                    "allTime": 942.8268440158639,
                    "date": "2025-07-08",
                    "oneYear": 28.505701057034535
                },
                {
                    "allTime": 943.036368693581,
                    "date": "2025-07-05",
                    "oneYear": 29.257507679929823
                },
                {
                    "allTime": 943.0926341986799,
                    "date": "2025-07-04",
                    "oneYear": 29.90294661080635
                },
                {
                    "allTime": 942.9583517507152,
                    "date": "2025-07-03",
                    "oneYear": 30.515623134620643
                },
                {
                    "allTime": 943.0130427424408,
                    "date": "2025-07-02",
                    "oneYear": 31.105423230815568
                },
                {
                    "allTime": 943.0225333102034,
                    "date": "2025-07-01",
                    "oneYear": 31.738144876817348
                },
                {
                    "allTime": 943.2496190712236,
                    "date": "2025-06-28",
                    "oneYear": 32.429969282559426
                },
                {
                    "allTime": 943.430238613735,
                    "date": "2025-06-27",
                    "oneYear": 33.12624054753905
                },
                {
                    "allTime": 943.712050726157,
                    "date": "2025-06-26",
                    "oneYear": 33.869927358206965
                },
                {
                    "allTime": 943.8005182518577,
                    "date": "2025-06-25",
                    "oneYear": 34.29973214299502
                },
                {
                    "allTime": 943.8822725088697,
                    "date": "2025-06-24",
                    "oneYear": 34.679365364856835
                },
                {
                    "allTime": 944.2650501722712,
                    "date": "2025-06-21",
                    "oneYear": 35.162949347971264
                },
                {
                    "allTime": 944.840388722197,
                    "date": "2025-06-20",
                    "oneYear": 36.002288371060025
                },
                {
                    "allTime": 945.1377837266992,
                    "date": "2025-06-19",
                    "oneYear": 36.31836840392048
                },
                {
                    "allTime": 945.3252743230396,
                    "date": "2025-06-18",
                    "oneYear": 36.659093436825415
                },
                {
                    "allTime": 945.5981199250245,
                    "date": "2025-06-17",
                    "oneYear": 36.90879636774182
                },
                {
                    "allTime": 945.8693037384755,
                    "date": "2025-06-14",
                    "oneYear": 36.9992843699064
                },
                {
                    "allTime": 945.8149693633745,
                    "date": "2025-06-13",
                    "oneYear": 36.91115009257253
                },
                {
                    "allTime": 945.9748195717673,
                    "date": "2025-06-12",
                    "oneYear": 36.82111929299143
                },
                {
                    "allTime": 946.2289771183148,
                    "date": "2025-06-11",
                    "oneYear": 36.677339657023126
                },
                {
                    "allTime": 946.6785769700805,
                    "date": "2025-06-10",
                    "oneYear": 36.738104390074426
                },
                {
                    "allTime": 946.4697431347513,
                    "date": "2025-06-07",
                    "oneYear": 36.46063091410934
                },
                {
                    "allTime": 946.2880588726617,
                    "date": "2025-06-06",
                    "oneYear": 36.38072038065893
                },
                {
                    "allTime": 946.2436269843654,
                    "date": "2025-06-05",
                    "oneYear": 36.33756540675305
                },
                {
                    "allTime": 945.8712807217463,
                    "date": "2025-06-04",
                    "oneYear": 36.006643406982874
                },
                {
                    "allTime": 945.7934598175922,
                    "date": "2025-06-03",
                    "oneYear": 35.795174397974016
                },
                {
                    "allTime": 945.4145759540876,
                    "date": "2025-05-31",
                    "oneYear": 35.32365751475751
                },
                {
                    "allTime": 944.7890926373447,
                    "date": "2025-05-30",
                    "oneYear": 34.97131843242175
                },
                {
                    "allTime": 944.2356631200969,
                    "date": "2025-05-29",
                    "oneYear": 34.51030850928143
                },
                {
                    "allTime": 943.7300577064274,
                    "date": "2025-05-28",
                    "oneYear": 34.11919820513757
                },
                {
                    "allTime": 943.2590959154783,
                    "date": "2025-05-27",
                    "oneYear": 34.1317562075472
                },
                {
                    "allTime": 942.6081863559687,
                    "date": "2025-05-24",
                    "oneYear": 34.040949647244695
                },
                {
                    "allTime": 942.2194871138744,
                    "date": "2025-05-23",
                    "oneYear": 33.90825955175292
                },
                {
                    "allTime": 941.3467974013413,
                    "date": "2025-05-22",
                    "oneYear": 33.75894084180577
                },
                {
                    "allTime": 940.5146997586869,
                    "date": "2025-05-21",
                    "oneYear": 33.544923998905944
                },
                {
                    "allTime": 939.5330733375673,
                    "date": "2025-05-20",
                    "oneYear": 33.310292589744684
                },
                {
                    "allTime": 938.7295431179869,
                    "date": "2025-05-17",
                    "oneYear": 33.34876678627607
                },
                {
                    "allTime": 937.9149157458597,
                    "date": "2025-05-16",
                    "oneYear": 33.12833213133611
                },
                {
                    "allTime": 937.0672655524509,
                    "date": "2025-05-15",
                    "oneYear": 32.975756642276686
                },
                {
                    "allTime": 936.3132075724864,
                    "date": "2025-05-14",
                    "oneYear": 32.73618560328958
                },
                {
                    "allTime": 935.4598891939133,
                    "date": "2025-05-13",
                    "oneYear": 32.59118425433249
                },
                {
                    "allTime": 934.8751107340273,
                    "date": "2025-05-10",
                    "oneYear": 32.46254381502981
                },
                {
                    "allTime": 934.4965729232811,
                    "date": "2025-05-09",
                    "oneYear": 32.7053666820889
                },
                {
                    "allTime": 934.4489929155058,
                    "date": "2025-05-08",
                    "oneYear": 32.88986805001833
                },
                {
                    "allTime": 934.0172049666617,
                    "date": "2025-05-07",
                    "oneYear": 32.9465027519605
                },
                {
                    "allTime": 933.5403509141875,
                    "date": "2025-05-06",
                    "oneYear": 33.09854435768207
                },
                {
                    "allTime": 933.2585744624519,
                    "date": "2025-05-03",
                    "oneYear": 33.24619615589131
                },
                {
                    "allTime": 932.6778581870051,
                    "date": "2025-05-02",
                    "oneYear": 33.373532488543354
                },
                {
                    "allTime": 932.3744104482302,
                    "date": "2025-05-01",
                    "oneYear": 33.424606306416486
                },
                {
                    "allTime": 932.0301901952319,
                    "date": "2025-04-30",
                    "oneYear": 33.64465521584903
                },
                {
                    "allTime": 931.6062118080469,
                    "date": "2025-04-29",
                    "oneYear": 33.87841097013692
                },
                {
                    "allTime": 931.2802807400672,
                    "date": "2025-04-26",
                    "oneYear": 34.37500421100551
                },
                {
                    "allTime": 931.0234121228817,
                    "date": "2025-04-25",
                    "oneYear": 34.79657607194624
                },
                {
                    "allTime": 931.1089127294507,
                    "date": "2025-04-24",
                    "oneYear": 35.11597881516349
                },
                {
                    "allTime": 931.1692493083171,
                    "date": "2025-04-23",
                    "oneYear": 35.566262870572494
                },
                {
                    "allTime": 931.1056432147128,
                    "date": "2025-04-22",
                    "oneYear": 35.99400659597242
                },
                {
                    "allTime": 931.2468473848974,
                    "date": "2025-04-19",
                    "oneYear": 36.628021333126306
                },
                {
                    "allTime": 931.1533408811259,
                    "date": "2025-04-18",
                    "oneYear": 37.16488417615494
                },
                {
                    "allTime": 930.9539323128695,
                    "date": "2025-04-17",
                    "oneYear": 37.4922271455631
                },
                {
                    "allTime": 930.6651699917398,
                    "date": "2025-04-16",
                    "oneYear": 38.000388496414615
                },
                {
                    "allTime": 930.2142648819187,
                    "date": "2025-04-15",
                    "oneYear": 38.086480725624085
                },
                {
                    "allTime": 929.8527879384526,
                    "date": "2025-04-12",
                    "oneYear": 38.47533892348841
                },
                {
                    "allTime": 929.6747762617613,
                    "date": "2025-04-11",
                    "oneYear": 39.02237064754424
                },
                {
                    "allTime": 929.26977804469,
                    "date": "2025-04-10",
                    "oneYear": 39.54740653430656
                },
                {
                    "allTime": 929.1933601627676,
                    "date": "2025-04-09",
                    "oneYear": 39.98508652425108
                },
                {
                    "allTime": 929.1362587363071,
                    "date": "2025-04-08",
                    "oneYear": 40.85544427768643
                },
                {
                    "allTime": 928.9426485209065,
                    "date": "2025-04-05",
                    "oneYear": 41.72025933683255
                },
                {
                    "allTime": 929.2089260088248,
                    "date": "2025-04-04",
                    "oneYear": 42.39776474629803
                },
                {
                    "allTime": 929.1020860187808,
                    "date": "2025-04-03",
                    "oneYear": 43.19882493028612
                },
                {
                    "allTime": 929.0669341077386,
                    "date": "2025-04-02",
                    "oneYear": 43.95429422091273
                },
                {
                    "allTime": 929.1629689574852,
                    "date": "2025-04-01",
                    "oneYear": 44.55932814115165
                },
                {
                    "allTime": 929.1626286679186,
                    "date": "2025-03-29",
                    "oneYear": 44.8820304865079
                },
                {
                    "allTime": 929.3687851886774,
                    "date": "2025-03-28",
                    "oneYear": 45.34085112214394
                },
                {
                    "allTime": 929.6360919546098,
                    "date": "2025-03-27",
                    "oneYear": 45.800828091267306
                },
                {
                    "allTime": 929.7269533894275,
                    "date": "2025-03-26",
                    "oneYear": 45.89914397297282
                },
                {
                    "allTime": 929.6391579920086,
                    "date": "2025-03-25",
                    "oneYear": 46.00752601618629
                },
                {
                    "allTime": 929.8176101563128,
                    "date": "2025-03-22",
                    "oneYear": 46.302317097035804
                },
                {
                    "allTime": 929.5474284046176,
                    "date": "2025-03-21",
                    "oneYear": 46.35202629276721
                },
                {
                    "allTime": 929.4446109833153,
                    "date": "2025-03-20",
                    "oneYear": 46.46681597528877
                },
                {
                    "allTime": 928.7635966620927,
                    "date": "2025-03-19",
                    "oneYear": 46.31914347023763
                },
                {
                    "allTime": 928.5525652022603,
                    "date": "2025-03-18",
                    "oneYear": 46.324963503499085
                },
                {
                    "allTime": 928.0770361444135,
                    "date": "2025-03-15",
                    "oneYear": 46.15692744848131
                },
                {
                    "allTime": 927.5069613012685,
                    "date": "2025-03-14",
                    "oneYear": 45.861244354337565
                },
                {
                    "allTime": 927.2260203635608,
                    "date": "2025-03-13",
                    "oneYear": 45.689369668653235
                },
                {
                    "allTime": 926.7483008088745,
                    "date": "2025-03-12",
                    "oneYear": 45.48004809131992
                },
                {
                    "allTime": 926.2044429908232,
                    "date": "2025-03-11",
                    "oneYear": 44.958658195247715
                },
                {
                    "allTime": 925.9874042853454,
                    "date": "2025-03-08",
                    "oneYear": 44.71631567275127
                },
                {
                    "allTime": 925.458236943593,
                    "date": "2025-03-07",
                    "oneYear": 44.252191905067036
                },
                {
                    "allTime": 925.1811735688134,
                    "date": "2025-03-06",
                    "oneYear": 44.065914929828466
                },
                {
                    "allTime": 925.1649122885392,
                    "date": "2025-03-05",
                    "oneYear": 44.057494979827105
                },
                {
                    "allTime": 924.8926640797829,
                    "date": "2025-03-04",
                    "oneYear": 43.87921879383009
                },
                {
                    "allTime": 924.6242347808069,
                    "date": "2025-03-01",
                    "oneYear": 43.88363098074461
                },
                {
                    "allTime": 924.5516631584906,
                    "date": "2025-02-28",
                    "oneYear": 44.20096278403633
                },
                {
                    "allTime": 924.0576078590282,
                    "date": "2025-02-27",
                    "oneYear": 43.914766240474385
                },
                {
                    "allTime": 923.8039043736663,
                    "date": "2025-02-26",
                    "oneYear": 43.97657108844216
                },
                {
                    "allTime": 923.5155099703073,
                    "date": "2025-02-25",
                    "oneYear": 44.015458898021436
                },
                {
                    "allTime": 923.074773498428,
                    "date": "2025-02-22",
                    "oneYear": 43.80404015315308
                },
                {
                    "allTime": 923.1188949224298,
                    "date": "2025-02-21",
                    "oneYear": 44.12315401107517
                },
                {
                    "allTime": 923.5002521800195,
                    "date": "2025-02-20",
                    "oneYear": 44.30863617016284
                },
                {
                    "allTime": 923.6343313743624,
                    "date": "2025-02-19",
                    "oneYear": 44.312891710781436
                },
                {
                    "allTime": 924.1516945009304,
                    "date": "2025-02-18",
                    "oneYear": 44.824877722338755
                },
                {
                    "allTime": 924.2693094684845,
                    "date": "2025-02-15",
                    "oneYear": 45.14061935458548
                },
                {
                    "allTime": 924.3564883082073,
                    "date": "2025-02-14",
                    "oneYear": 45.36608125508505
                },
                {
                    "allTime": 924.651032992976,
                    "date": "2025-02-13",
                    "oneYear": 45.8892173545333
                },
                {
                    "allTime": 924.8872355179265,
                    "date": "2025-02-12",
                    "oneYear": 46.51747216440871
                },
                {
                    "allTime": 924.8362584041065,
                    "date": "2025-02-11",
                    "oneYear": 46.60847188525895
                },
                {
                    "allTime": 924.7121883228014,
                    "date": "2025-02-08",
                    "oneYear": 46.434034557234696
                },
                {
                    "allTime": 924.5633731145826,
                    "date": "2025-02-07",
                    "oneYear": 46.64271691702529
                },
                {
                    "allTime": 924.203323047138,
                    "date": "2025-02-06",
                    "oneYear": 46.83157498165757
                },
                {
                    "allTime": 923.9722757780925,
                    "date": "2025-02-05",
                    "oneYear": 47.121202788968766
                },
                {
                    "allTime": 924.0388134375438,
                    "date": "2025-02-04",
                    "oneYear": 47.62084334796199
                },
                {
                    "allTime": 923.6117818775429,
                    "date": "2025-02-01",
                    "oneYear": 47.90927416744923
                },
                {
                    "allTime": 923.2370843694913,
                    "date": "2025-01-31",
                    "oneYear": 48.232552735091566
                },
                {
                    "allTime": 922.733708430297,
                    "date": "2025-01-30",
                    "oneYear": 48.34916174936931
                },
                {
                    "allTime": 922.1664785311859,
                    "date": "2025-01-29",
                    "oneYear": 48.75311256265788
                },
                {
                    "allTime": 921.9874793103845,
                    "date": "2025-01-28",
                    "oneYear": 38.42571481131092
                },
                {
                    "allTime": 922.0993730635133,
                    "date": "2025-01-25",
                    "oneYear": 39.213916912844624
                },
                {
                    "allTime": 921.954898902346,
                    "date": "2025-01-24",
                    "oneYear": 40.16286393468872
                },
                {
                    "allTime": 921.7378630585583,
                    "date": "2025-01-23",
                    "oneYear": 40.885799865389885
                },
                {
                    "allTime": 921.4150080856789,
                    "date": "2025-01-22",
                    "oneYear": 42.224637509169206
                },
                {
                    "allTime": 921.0178515135606,
                    "date": "2025-01-21",
                    "oneYear": 42.90707868267522
                },
                {
                    "allTime": 920.6423301013483,
                    "date": "2025-01-18",
                    "oneYear": 43.312208865654064
                },
                {
                    "allTime": 920.5462979183577,
                    "date": "2025-01-17",
                    "oneYear": 43.70120224240061
                },
                {
                    "allTime": 920.1124867286862,
                    "date": "2025-01-16",
                    "oneYear": 44.15423253966623
                },
                {
                    "allTime": 920.021638740349,
                    "date": "2025-01-15",
                    "oneYear": 44.63439612277441
                },
                {
                    "allTime": 920.0959808942586,
                    "date": "2025-01-14",
                    "oneYear": 45.13327413873443
                },
                {
                    "allTime": 920.4114727408062,
                    "date": "2025-01-11",
                    "oneYear": 45.757653726593425
                },
                {
                    "allTime": 920.7653981595817,
                    "date": "2025-01-10",
                    "oneYear": 46.89769939626236
                },
                {
                    "allTime": 921.1727204152974,
                    "date": "2025-01-09",
                    "oneYear": 47.304331132638815
                },
                {
                    "allTime": 921.3774449902774,
                    "date": "2025-01-08",
                    "oneYear": 47.31137207189219
                },
                {
                    "allTime": 921.2025852661585,
                    "date": "2025-01-07",
                    "oneYear": 47.490484635066686
                },
                {
                    "allTime": 920.8044102961743,
                    "date": "2025-01-04",
                    "oneYear": 47.38123528429129
                },
                {
                    "allTime": 920.4387429631848,
                    "date": "2025-01-03",
                    "oneYear": 47.35185123565027
                },
                {
                    "allTime": 919.8840161632882,
                    "date": "2025-01-02",
                    "oneYear": 46.74449985886727
                },
                {
                    "allTime": 919.5981680514132,
                    "date": "2025-01-01",
                    "oneYear": 46.015432662104686
                },
                {
                    "allTime": 919.1592122084716,
                    "date": "2024-12-31",
                    "oneYear": 45.62988400643755
                },
                {
                    "allTime": 918.796521464258,
                    "date": "2024-12-28",
                    "oneYear": 45.539845858161726
                },
                {
                    "allTime": 918.5907991882655,
                    "date": "2024-12-27",
                    "oneYear": 44.18719955517004
                },
                {
                    "allTime": 918.3070094557322,
                    "date": "2024-12-26",
                    "oneYear": 43.7432195911626
                },
                {
                    "allTime": 918.2854901925859,
                    "date": "2024-12-25",
                    "oneYear": 43.730950242827255
                },
                {
                    "allTime": 918.2432712693543,
                    "date": "2024-12-24",
                    "oneYear": 43.71716084856083
                },
                {
                    "allTime": 918.0419108010022,
                    "date": "2024-12-21",
                    "oneYear": 43.37384528928692
                },
                {
                    "allTime": 917.9470407968886,
                    "date": "2024-12-20",
                    "oneYear": 42.60867772724023
                },
                {
                    "allTime": 917.8161070719449,
                    "date": "2024-12-19",
                    "oneYear": 42.11282953153264
                },
                {
                    "allTime": 917.6650960486668,
                    "date": "2024-12-18",
                    "oneYear": 41.59443561699951
                },
                {
                    "allTime": 917.7759757796451,
                    "date": "2024-12-17",
                    "oneYear": 41.83334068535639
                },
                {
                    "allTime": 917.6873687618653,
                    "date": "2024-12-14",
                    "oneYear": 41.49412422681655
                },
                {
                    "allTime": 917.5289029158635,
                    "date": "2024-12-13",
                    "oneYear": 41.32489069624072
                },
                {
                    "allTime": 916.9450832180104,
                    "date": "2024-12-12",
                    "oneYear": 40.92443050642459
                },
                {
                    "allTime": 916.2298111173125,
                    "date": "2024-12-11",
                    "oneYear": 40.74416208789933
                },
                {
                    "allTime": 915.6153907377992,
                    "date": "2024-12-10",
                    "oneYear": 40.428261999438874
                },
                {
                    "allTime": 915.5605613948366,
                    "date": "2024-12-07",
                    "oneYear": 40.81073946538566
                },
                {
                    "allTime": 915.6329013415901,
                    "date": "2024-12-06",
                    "oneYear": 40.762804082647236
                },
                {
                    "allTime": 915.5964837885783,
                    "date": "2024-12-05",
                    "oneYear": 40.329665161115756
                },
                {
                    "allTime": 916.1241658715669,
                    "date": "2024-12-04",
                    "oneYear": 41.35896476134639
                },
                {
                    "allTime": 916.6860292226156,
                    "date": "2024-12-03",
                    "oneYear": 42.300009352773515
                },
                {
                    "allTime": 917.0155603759381,
                    "date": "2024-11-30",
                    "oneYear": 43.64156374526831
                },
                {
                    "allTime": 917.0633310683749,
                    "date": "2024-11-29",
                    "oneYear": 44.881146942415654
                },
                {
                    "allTime": 916.9313071506459,
                    "date": "2024-11-28",
                    "oneYear": 45.955208873960125
                },
                {
                    "allTime": 917.6725824928338,
                    "date": "2024-11-27",
                    "oneYear": 47.16786927473631
                },
                {
                    "allTime": 917.8617006461112,
                    "date": "2024-11-26",
                    "oneYear": 48.25397836341053
                },
                {
                    "allTime": 918.2431644016826,
                    "date": "2024-11-23",
                    "oneYear": 49.272837062449106
                },
                {
                    "allTime": 918.6187223400968,
                    "date": "2024-11-22",
                    "oneYear": 48.3285645763935
                },
                {
                    "allTime": 919.2700832014195,
                    "date": "2024-11-21",
                    "oneYear": 49.612284538335324
                },
                {
                    "allTime": 919.6853080622085,
                    "date": "2024-11-20",
                    "oneYear": 50.74898423731216
                },
                {
                    "allTime": 920.3018292787739,
                    "date": "2024-11-19",
                    "oneYear": 51.90487372183156
                },
                {
                    "allTime": 920.8516650241644,
                    "date": "2024-11-16",
                    "oneYear": 53.27987803903416
                },
                {
                    "allTime": 921.5884140922936,
                    "date": "2024-11-15",
                    "oneYear": 55.074953353919575
                },
                {
                    "allTime": 921.6797319461773,
                    "date": "2024-11-14",
                    "oneYear": 56.73806605464538
                },
                {
                    "allTime": 922.1552053325327,
                    "date": "2024-11-13",
                    "oneYear": 58.358182263087485
                },
                {
                    "allTime": 922.8426217410861,
                    "date": "2024-11-12",
                    "oneYear": 59.57213437531396
                },
                {
                    "allTime": 923.5595901881383,
                    "date": "2024-11-09",
                    "oneYear": 59.06581767459841
                },
                {
                    "allTime": 924.1818947104807,
                    "date": "2024-11-08",
                    "oneYear": 59.678074819489474
                },
                {
                    "allTime": 924.7519154783076,
                    "date": "2024-11-07",
                    "oneYear": 60.04508747413185
                },
                {
                    "allTime": 925.3565518244317,
                    "date": "2024-11-06",
                    "oneYear": 60.405615981522246
                },
                {
                    "allTime": 925.9758678313582,
                    "date": "2024-11-05",
                    "oneYear": 60.6666453773892
                },
                {
                    "allTime": 926.382699251079,
                    "date": "2024-11-02",
                    "oneYear": 61.11291883629101
                },
                {
                    "allTime": 927.0551606079805,
                    "date": "2024-11-01",
                    "oneYear": 61.661270564376714
                },
                {
                    "allTime": 927.6604011460602,
                    "date": "2024-10-31",
                    "oneYear": 62.647719196176055
                },
                {
                    "allTime": 928.0020265414515,
                    "date": "2024-10-30",
                    "oneYear": 62.37735325396953
                },
                {
                    "allTime": 928.1533497820309,
                    "date": "2024-10-29",
                    "oneYear": 62.50927168951971
                },
                {
                    "allTime": 927.6846913285839,
                    "date": "2024-10-26",
                    "oneYear": 63.03714282617989
                },
                {
                    "allTime": 927.4424956577556,
                    "date": "2024-10-25",
                    "oneYear": 63.38912704038726
                },
                {
                    "allTime": 927.1519938377571,
                    "date": "2024-10-24",
                    "oneYear": 64.24882838412731
                },
                {
                    "allTime": 927.0845171592202,
                    "date": "2024-10-23",
                    "oneYear": 65.49227143798366
                },
                {
                    "allTime": 926.8249297035436,
                    "date": "2024-10-22",
                    "oneYear": 66.89906452469887
                },
                {
                    "allTime": 926.4293825347567,
                    "date": "2024-10-19",
                    "oneYear": 68.48630251912832
                },
                {
                    "allTime": 926.0674614841645,
                    "date": "2024-10-18",
                    "oneYear": 69.61200532923094
                },
                {
                    "allTime": 925.8031769101947,
                    "date": "2024-10-17",
                    "oneYear": 70.53448546020586
                },
                {
                    "allTime": 925.4634870570486,
                    "date": "2024-10-16",
                    "oneYear": 71.72659163876507
                },
                {
                    "allTime": 925.3386697854017,
                    "date": "2024-10-15",
                    "oneYear": 72.36002215618048
                },
                {
                    "allTime": 925.1502133662311,
                    "date": "2024-10-12",
                    "oneYear": 73.64855591833395
                },
                {
                    "allTime": 924.9460964573134,
                    "date": "2024-10-11",
                    "oneYear": 74.41050560782824
                },
                {
                    "allTime": 924.5337013562826,
                    "date": "2024-10-10",
                    "oneYear": 75.07756132491038
                },
                {
                    "allTime": 924.0374670267288,
                    "date": "2024-10-09",
                    "oneYear": 75.75078749861669
                },
                {
                    "allTime": 923.4925817319362,
                    "date": "2024-10-08",
                    "oneYear": 76.9502336462897
                },
                {
                    "allTime": 923.043042975187,
                    "date": "2024-10-05",
                    "oneYear": 77.58177352539612
                },
                {
                    "allTime": 922.4933932916312,
                    "date": "2024-10-04",
                    "oneYear": 77.87318714978178
                },
                {
                    "allTime": 922.318526450736,
                    "date": "2024-10-03",
                    "oneYear": 78.4617193525048
                },
                {
                    "allTime": 921.8526850752108,
                    "date": "2024-10-02",
                    "oneYear": 78.86702277719968
                },
                {
                    "allTime": 921.4614143001153,
                    "date": "2024-10-01",
                    "oneYear": 79.0844928507712
                },
                {
                    "allTime": 921.3235684292813,
                    "date": "2024-09-28",
                    "oneYear": 79.22948811156247
                },
                {
                    "allTime": 921.1923784931383,
                    "date": "2024-09-27",
                    "oneYear": 79.62410208615788
                },
                {
                    "allTime": 921.2112620998222,
                    "date": "2024-09-26",
                    "oneYear": 80.28613563332611
                },
                {
                    "allTime": 921.3014017559192,
                    "date": "2024-09-25",
                    "oneYear": 80.85108917562083
                }
            ],
            "scores": {
                "alphaLtmRank": null,
                "corr60LtmRank": 46,
                "corrLtmRank": null,
                "fncV4LtmRank": null,
                "mmc60LtmRank": 2386,
                "mmcLtmRank": 2341,
                "mpcLtmRank": null,
                "seasonRank": 141,
                "tcLtmRank": null,
                "v2Corr20LtmRank": 43
            },
            "scoresTs": [
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.012324052531033452,
                    "corr60Ltm": 0.02912481855022284,
                    "corrLtm": null,
                    "date": "2025-09-23",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": 0.0032943027428846148,
                    "mmc60": -0.004228803999759944,
                    "mmc60Ltm": -0.005331940997599534,
                    "mmcLtm": -0.003457143745411944,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": -0.015525329187649864,
                    "v2Corr20Ltm": 0.019889466954696837
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.01382136797539074,
                    "corr60Ltm": 0.029194091988801255,
                    "corrLtm": null,
                    "date": "2025-09-20",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": 4.8742868314226436e-4,
                    "mmc60": -0.007724378210309311,
                    "mmc60Ltm": -0.005313213740895472,
                    "mmcLtm": -0.003490739924503456,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": -0.014857841470823694,
                    "v2Corr20Ltm": 0.020034609561837603
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.020626897301904652,
                    "corr60Ltm": 0.029223120234106274,
                    "corrLtm": null,
                    "date": "2025-09-19",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": 0.001677824460941241,
                    "mmc60": -0.0030677547306464867,
                    "mmc60Ltm": -0.005293825318633752,
                    "mmcLtm": -0.0035189915286534265,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": -0.001159000217285212,
                    "v2Corr20Ltm": 0.02017819989530534
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.024809795148171956,
                    "corr60Ltm": 0.029225595148658363,
                    "corrLtm": null,
                    "date": "2025-09-18",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": 0.004767429136439181,
                    "mmc60": -0.002861863071452211,
                    "mmc60Ltm": -0.005288212541887979,
                    "mmcLtm": -0.0035394050706493703,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.006041100162200733,
                    "v2Corr20Ltm": 0.020266370143704474
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.019882344828704917,
                    "corr60Ltm": 0.029219276699814792,
                    "corrLtm": null,
                    "date": "2025-09-17",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": 0.001713224799876785,
                    "mmc60": -0.001525782115409017,
                    "mmc60Ltm": -0.005279370461154446,
                    "mmcLtm": -0.0035674500098694436,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.008821991305797847,
                    "v2Corr20Ltm": 0.02032539616022524
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.014865397870991531,
                    "corr60Ltm": 0.029213610474417454,
                    "corrLtm": null,
                    "date": "2025-09-16",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.0033951662458233255,
                    "mmc60": -0.0022322937945274055,
                    "mmc60Ltm": -0.005273917119716098,
                    "mmcLtm": -0.0035866688405203125,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.022570800686358604,
                    "v2Corr20Ltm": 0.02037332701378535
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.017510930098115406,
                    "corr60Ltm": 0.029233877570697182,
                    "corrLtm": null,
                    "date": "2025-09-13",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.0014788224199321185,
                    "mmc60": -0.005102025262608943,
                    "mmc60Ltm": -0.00525975411667193,
                    "mmcLtm": -0.003593384602030568,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.03205601508844923,
                    "v2Corr20Ltm": 0.020364132563272495
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.01323994366990855,
                    "corr60Ltm": 0.029278182704420876,
                    "corrLtm": null,
                    "date": "2025-09-12",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.0016327063225840903,
                    "mmc60": -0.006487752672984857,
                    "mmc60Ltm": -0.0052349863187309,
                    "mmcLtm": -0.003616716585095962,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.021694165355578877,
                    "v2Corr20Ltm": 0.02031500700644402
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.019105943936896182,
                    "corr60Ltm": 0.029310225755494024,
                    "corrLtm": null,
                    "date": "2025-09-11",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.002973455491933791,
                    "mmc60": -0.0034818525613548837,
                    "mmc60Ltm": -0.005217106346803755,
                    "mmcLtm": -0.00364334525818951,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.020428216034622543,
                    "v2Corr20Ltm": 0.020309187772903366
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.02259445625153367,
                    "corr60Ltm": 0.02934946267527603,
                    "corrLtm": null,
                    "date": "2025-09-10",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.006984741348843214,
                    "mmc60": -0.002901068643749335,
                    "mmc60Ltm": -0.005208329670323469,
                    "mmcLtm": -0.00365718776588325,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.0234239044992064,
                    "v2Corr20Ltm": 0.020308683415862186
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.016109154216646285,
                    "corr60Ltm": 0.029366882957837202,
                    "corrLtm": null,
                    "date": "2025-09-09",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.009988143740069245,
                    "mmc60": -0.005969039741364405,
                    "mmc60Ltm": -0.005187966150615617,
                    "mmcLtm": -0.003662852473358946,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.017872862111127617,
                    "v2Corr20Ltm": 0.02029542715593306
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.013223027314542979,
                    "corr60Ltm": 0.029444343018309827,
                    "corrLtm": null,
                    "date": "2025-09-06",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.009861591903874534,
                    "mmc60": -0.007270663804777807,
                    "mmc60Ltm": -0.005155359255054833,
                    "mmcLtm": -0.003652438665925731,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.015252601557096375,
                    "v2Corr20Ltm": 0.020305779998004876
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.012642963110784841,
                    "corr60Ltm": 0.029560337932813492,
                    "corrLtm": null,
                    "date": "2025-09-05",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.009433595852044525,
                    "mmc60": -0.003718294020190304,
                    "mmc60Ltm": -0.0051062196236189026,
                    "mmcLtm": -0.0036519633712748705,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.0076637188300157965,
                    "v2Corr20Ltm": 0.020327467459124657
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.019153674865936735,
                    "corr60Ltm": 0.02963463776763807,
                    "corrLtm": null,
                    "date": "2025-09-04",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00790212558851148,
                    "mmc60": -0.005220983769643863,
                    "mmc60Ltm": -0.005082101102468749,
                    "mmcLtm": -0.0036516921611137805,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.012256508947396069,
                    "v2Corr20Ltm": 0.020382052582525987
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.02236596484275834,
                    "corr60Ltm": 0.029698821618726435,
                    "corrLtm": null,
                    "date": "2025-09-03",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.0024077409402781906,
                    "mmc60": -0.0021177785375982206,
                    "mmc60Ltm": -0.005046767793006511,
                    "mmcLtm": -0.0036353661243761887,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.023239310983747815,
                    "v2Corr20Ltm": 0.02041722809609798
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.014105717454769863,
                    "corr60Ltm": 0.02977692244308368,
                    "corrLtm": null,
                    "date": "2025-09-02",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.0037193697772951095,
                    "mmc60": -0.0030787690503451207,
                    "mmc60Ltm": -0.005014201553398856,
                    "mmcLtm": -0.003620778342995812,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.020918816708084105,
                    "v2Corr20Ltm": 0.0204049581704995
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.02161018860535833,
                    "corr60Ltm": 0.029890777625249314,
                    "corrLtm": null,
                    "date": "2025-08-30",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.008313289743566852,
                    "mmc60": -0.002483778760014777,
                    "mmc60Ltm": -0.004986353779259602,
                    "mmcLtm": -0.0036126536312054095,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.009819283762387568,
                    "v2Corr20Ltm": 0.02040271424675459
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.027087076810307163,
                    "corr60Ltm": 0.02995975671105254,
                    "corrLtm": null,
                    "date": "2025-08-29",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.005041823965721115,
                    "mmc60": -0.0023759421342578724,
                    "mmc60Ltm": -0.00496427596791855,
                    "mmcLtm": -0.003571942214563391,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.018640344148257406,
                    "v2Corr20Ltm": 0.020449132801510585
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.026232671741024477,
                    "corr60Ltm": 0.02998294787269887,
                    "corrLtm": null,
                    "date": "2025-08-28",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.0059454737498333445,
                    "mmc60": -0.0018155344252390197,
                    "mmc60Ltm": -0.004947669714530588,
                    "mmcLtm": -0.003550214996303923,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.016068454297199955,
                    "v2Corr20Ltm": 0.020457101033463244
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.019197056957227808,
                    "corr60Ltm": 0.030025691697445907,
                    "corrLtm": null,
                    "date": "2025-08-27",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.0063877962815725164,
                    "mmc60": -0.005152644377283354,
                    "mmc60Ltm": -0.004920241076885994,
                    "mmcLtm": -0.0035195908056915347,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.019343121981821813,
                    "v2Corr20Ltm": 0.020476519824331664
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.026954870006671613,
                    "corr60Ltm": 0.03011805247538756,
                    "corrLtm": null,
                    "date": "2025-08-26",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.006930681270376155,
                    "mmc60": -0.006141376940267107,
                    "mmc60Ltm": -0.004878840447087973,
                    "mmcLtm": -0.0034956122375629046,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.03730326428025788,
                    "v2Corr20Ltm": 0.020481557148076153
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.026943469156364017,
                    "corr60Ltm": 0.03017981354815893,
                    "corrLtm": null,
                    "date": "2025-08-23",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00914094026687932,
                    "mmc60": -0.003546080117806296,
                    "mmc60Ltm": -0.004841091569922199,
                    "mmcLtm": -0.003475991926182153,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.03158943482117742,
                    "v2Corr20Ltm": 0.020406460241236053
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.02567126300940573,
                    "corr60Ltm": 0.030264604164418077,
                    "corrLtm": null,
                    "date": "2025-08-22",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.004782239210872765,
                    "mmc60": -0.010219373383408045,
                    "mmc60Ltm": -0.0047979412246432485,
                    "mmcLtm": -0.003451819434738171,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.029360707880307865,
                    "v2Corr20Ltm": 0.02035631237316457
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.02557105402610109,
                    "corr60Ltm": 0.030333723003462498,
                    "corrLtm": null,
                    "date": "2025-08-21",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.0047589053343839675,
                    "mmc60": -0.011050596769323387,
                    "mmc60Ltm": -0.0047410023611052865,
                    "mmcLtm": -0.003441407023968544,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.03779685458364828,
                    "v2Corr20Ltm": 0.020315752033042304
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.02082423406297127,
                    "corr60Ltm": 0.030387868735163262,
                    "corrLtm": null,
                    "date": "2025-08-20",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.010165054215483605,
                    "mmc60": -0.009654577274578016,
                    "mmc60Ltm": -0.0046767398830619014,
                    "mmcLtm": -0.0034438602602352717,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.019618999024929803,
                    "v2Corr20Ltm": 0.0202366520215011
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.01243026276016752,
                    "corr60Ltm": 0.030463989255994788,
                    "corrLtm": null,
                    "date": "2025-08-19",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.005278990037309976,
                    "mmc60": -0.012107495015272878,
                    "mmc60Ltm": -0.00461750215404053,
                    "mmcLtm": -0.0034266326578770968,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.02479753835107034,
                    "v2Corr20Ltm": 0.02023945953512188
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.004792511582200868,
                    "corr60Ltm": 0.030571882310553536,
                    "corrLtm": null,
                    "date": "2025-08-16",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00257720156103706,
                    "mmc60": -0.011053372990769882,
                    "mmc60Ltm": -0.004548888494978182,
                    "mmcLtm": -0.0034254574470061775,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.01629370216705179,
                    "v2Corr20Ltm": 0.020218646389843574
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.011154276138899936,
                    "corr60Ltm": 0.03068963222786311,
                    "corrLtm": null,
                    "date": "2025-08-15",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.004670590090298032,
                    "mmc60": -0.009429026684700572,
                    "mmc60Ltm": -0.004479710207657224,
                    "mmcLtm": -0.003408743647921744,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.022200937961900716,
                    "v2Corr20Ltm": 0.020236650721140784
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.01937987816882693,
                    "corr60Ltm": 0.03075650806641138,
                    "corrLtm": null,
                    "date": "2025-08-14",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.0032850054969319653,
                    "mmc60": -0.00383046207394113,
                    "mmc60Ltm": -0.004420008457907414,
                    "mmcLtm": -0.003377276061368878,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.019669842108797776,
                    "v2Corr20Ltm": 0.020227598706206405
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.008644008548479496,
                    "corr60Ltm": 0.03080401466346569,
                    "corrLtm": null,
                    "date": "2025-08-13",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.0018463314317327094,
                    "mmc60": -0.007674235144543636,
                    "mmc60Ltm": -0.004385109024673923,
                    "mmcLtm": -0.0033520363851354223,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.019246347897699998,
                    "v2Corr20Ltm": 0.020230180912675894
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.01393452448108924,
                    "corr60Ltm": 0.03087578677630676,
                    "corrLtm": null,
                    "date": "2025-08-12",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": 2.916767295730323e-4,
                    "mmc60": -0.00963319330384303,
                    "mmc60Ltm": -0.00434058846856456,
                    "mmcLtm": -0.0033363417819487072,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.014879260921946384,
                    "v2Corr20Ltm": 0.02023475688018741
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.010225617584660588,
                    "corr60Ltm": 0.030916715954540135,
                    "corrLtm": null,
                    "date": "2025-08-09",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -7.580139846246352e-4,
                    "mmc60": -0.007774808349661227,
                    "mmc60Ltm": -0.004294073513377422,
                    "mmcLtm": -0.0033322724207593317,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.0046238413758707434,
                    "v2Corr20Ltm": 0.020259782562235262
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.0052253000225104505,
                    "corr60Ltm": 0.03095447538908167,
                    "corrLtm": null,
                    "date": "2025-08-08",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": 0.001530147265910821,
                    "mmc60": -0.009102046931177363,
                    "mmc60Ltm": -0.004255457925830827,
                    "mmcLtm": -0.003309894397829735,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.013362798841941227,
                    "v2Corr20Ltm": 0.020333190736819134
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.006686515081489347,
                    "corr60Ltm": 0.030985660638037565,
                    "corrLtm": null,
                    "date": "2025-08-07",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": 0.00507375815619473,
                    "mmc60": -0.007789073918479862,
                    "mmc60Ltm": -0.004208643339887619,
                    "mmcLtm": -0.003301943927584183,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.012739242101699362,
                    "v2Corr20Ltm": 0.020366069943870444
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.00680060819845465,
                    "corr60Ltm": 0.03106312406684412,
                    "corrLtm": null,
                    "date": "2025-08-06",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": 0.004937398842119172,
                    "mmc60": -0.012393678350860101,
                    "mmc60Ltm": -0.0041680071562919105,
                    "mmcLtm": -0.00331336131515581,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.016163335876535217,
                    "v2Corr20Ltm": 0.020402216047387844
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.0014099185938623556,
                    "corr60Ltm": 0.031117834686773413,
                    "corrLtm": null,
                    "date": "2025-08-05",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": 5.733136060189774e-4,
                    "mmc60": -0.005779744792528714,
                    "mmc60Ltm": -0.004123392909736891,
                    "mmcLtm": -0.003344893647884236,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.012953899673086633,
                    "v2Corr20Ltm": 0.02042240119105857
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.004281781442704321,
                    "corr60Ltm": 0.03120476860020689,
                    "corrLtm": null,
                    "date": "2025-08-02",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": 0.001896541888477859,
                    "mmc60": -0.0025879289477214384,
                    "mmc60Ltm": -0.004100183657658237,
                    "mmcLtm": -0.0033422655390950365,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.004842230071190755,
                    "v2Corr20Ltm": 0.02045813564808236
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.019847644862029456,
                    "corr60Ltm": 0.03124634035713139,
                    "corrLtm": null,
                    "date": "2025-08-01",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.002735646686619272,
                    "mmc60": -0.001187309519959864,
                    "mmc60Ltm": -0.004096871439467733,
                    "mmcLtm": -0.003346106925640929,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.00196049129114296,
                    "v2Corr20Ltm": 0.02053321211720203
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.007370175463850007,
                    "corr60Ltm": 0.03125524547260255,
                    "corrLtm": null,
                    "date": "2025-07-31",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": 4.9608762156159626e-5,
                    "mmc60": 0.0014226459768373896,
                    "mmc60Ltm": -0.0040862294489698026,
                    "mmcLtm": -0.0033305995820140355,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.014291485185191256,
                    "v2Corr20Ltm": 0.02062293540621681
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.010195059348116127,
                    "corr60Ltm": 0.031309818440174005,
                    "corrLtm": null,
                    "date": "2025-07-30",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.003935886614693167,
                    "mmc60": 0.0018785795065232394,
                    "mmc60Ltm": -0.004088207862674161,
                    "mmcLtm": -0.0033277408799533307,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": -0.002000348307787887,
                    "v2Corr20Ltm": 0.020653670601464502
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.016514253694266626,
                    "corr60Ltm": 0.03136036150780574,
                    "corrLtm": null,
                    "date": "2025-07-29",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.006085882149152724,
                    "mmc60": 0.0022241936115371327,
                    "mmc60Ltm": -0.004095479157404518,
                    "mmcLtm": -0.0033150165634219394,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": -0.008167533157654063,
                    "v2Corr20Ltm": 0.020764178010777932
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.014675000176836055,
                    "corr60Ltm": 0.031374102949590164,
                    "corrLtm": null,
                    "date": "2025-07-26",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.006658566936826219,
                    "mmc60": 6.74295381871689e-4,
                    "mmc60Ltm": -0.004085226642506192,
                    "mmcLtm": -0.0033001413061454926,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.003943091994543366,
                    "v2Corr20Ltm": 0.020906000124348675
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.011566208809290041,
                    "corr60Ltm": 0.031403834060023735,
                    "corrLtm": null,
                    "date": "2025-07-25",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.003255534332465252,
                    "mmc60": 3.3129277000472856e-4,
                    "mmc60Ltm": -0.004059750647800721,
                    "mmcLtm": -0.0032765132335906026,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.014319056016409685,
                    "v2Corr20Ltm": 0.02098956124814082
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.0127627361126854,
                    "corr60Ltm": 0.03144546134427933,
                    "corrLtm": null,
                    "date": "2025-07-24",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.0054344269930472755,
                    "mmc60": 0.0013401002595389976,
                    "mmc60Ltm": -0.0040341991258467155,
                    "mmcLtm": -0.0032643384795520386,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.0017603099771321279,
                    "v2Corr20Ltm": 0.021022583551268202
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.02051456864520248,
                    "corr60Ltm": 0.03150944212545678,
                    "corrLtm": null,
                    "date": "2025-07-23",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.003999290166427008,
                    "mmc60": 0.0035899081896449245,
                    "mmc60Ltm": -0.004018641157492459,
                    "mmcLtm": -0.0032576950044828916,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": -0.005875724848971328,
                    "v2Corr20Ltm": 0.021118415758104702
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.019043416099017864,
                    "corr60Ltm": 0.03154047960191195,
                    "corrLtm": null,
                    "date": "2025-07-22",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.0017009962956077167,
                    "mmc60": 0.004678823153823316,
                    "mmc60Ltm": -0.004014968353621366,
                    "mmcLtm": -0.0032397397548030948,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": -8.847677719838033e-4,
                    "v2Corr20Ltm": 0.021253386461140084
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.02146759,
                    "corr60Ltm": 0.03156827,
                    "corrLtm": null,
                    "date": "2025-07-19",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00256213,
                    "mmc60": 0.00272876,
                    "mmc60Ltm": -0.00401923,
                    "mmcLtm": -0.00323194,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.00805002,
                    "v2Corr20Ltm": 0.02136463
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.02626142,
                    "corr60Ltm": 0.03161066,
                    "corrLtm": null,
                    "date": "2025-07-18",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00735516,
                    "mmc60": 0.00474643,
                    "mmc60Ltm": -0.00402082,
                    "mmcLtm": -0.00323022,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 8.3354e-4,
                    "v2Corr20Ltm": 0.02143188
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.02979454,
                    "corr60Ltm": 0.0316283,
                    "corrLtm": null,
                    "date": "2025-07-17",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00718161,
                    "mmc60": 0.00638717,
                    "mmc60Ltm": -0.0040265,
                    "mmcLtm": -0.00321811,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.01198298,
                    "v2Corr20Ltm": 0.02153644
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.03078849,
                    "corr60Ltm": 0.03168269,
                    "corrLtm": null,
                    "date": "2025-07-16",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00621725,
                    "mmc60": 0.00617982,
                    "mmc60Ltm": -0.00402649,
                    "mmcLtm": -0.00319807,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.00736664,
                    "v2Corr20Ltm": 0.02158518
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.03036545,
                    "corr60Ltm": 0.03172156,
                    "corrLtm": null,
                    "date": "2025-07-15",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00710506,
                    "mmc60": 0.00172628,
                    "mmc60Ltm": -0.00405452,
                    "mmcLtm": -0.00316925,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.00763361,
                    "v2Corr20Ltm": 0.0216581
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.02259795,
                    "corr60Ltm": 0.03173904,
                    "corrLtm": null,
                    "date": "2025-07-12",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00831456,
                    "mmc60": -5.0489e-4,
                    "mmc60Ltm": -0.00406836,
                    "mmcLtm": -0.0031439,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": -0.00616476,
                    "v2Corr20Ltm": 0.02173039
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.02596101,
                    "corr60Ltm": 0.03173279,
                    "corrLtm": null,
                    "date": "2025-07-11",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00635772,
                    "mmc60": -0.00221051,
                    "mmc60Ltm": -0.00407842,
                    "mmcLtm": -0.00310237,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": -0.00250881,
                    "v2Corr20Ltm": 0.02187492
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.01899524,
                    "corr60Ltm": 0.03170195,
                    "corrLtm": null,
                    "date": "2025-07-10",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00411277,
                    "mmc60": -0.00197069,
                    "mmc60Ltm": -0.00409067,
                    "mmcLtm": -0.00305731,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.00466778,
                    "v2Corr20Ltm": 0.02200192
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.01992216,
                    "corr60Ltm": 0.03171135,
                    "corrLtm": null,
                    "date": "2025-07-09",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00278919,
                    "mmc60": -0.00246973,
                    "mmc60Ltm": -0.0040991,
                    "mmcLtm": -0.00301975,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": -0.00331372,
                    "v2Corr20Ltm": 0.02209268
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.01605799,
                    "corr60Ltm": 0.03169124,
                    "corrLtm": null,
                    "date": "2025-07-08",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00420714,
                    "mmc60": -0.00387687,
                    "mmc60Ltm": -0.00410444,
                    "mmcLtm": -0.00300906,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": -0.0022016,
                    "v2Corr20Ltm": 0.02222639
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.01910048,
                    "corr60Ltm": 0.03169946,
                    "corrLtm": null,
                    "date": "2025-07-05",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -1.6029e-4,
                    "mmc60": -0.00328151,
                    "mmc60Ltm": -0.00409879,
                    "mmcLtm": -0.0029711,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": -0.00444997,
                    "v2Corr20Ltm": 0.02235564
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.01093115,
                    "corr60Ltm": 0.03168582,
                    "corrLtm": null,
                    "date": "2025-07-04",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": 0.00394884,
                    "mmc60": -0.00235613,
                    "mmc60Ltm": -0.00409685,
                    "mmcLtm": -0.0029565,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": -0.00260595,
                    "v2Corr20Ltm": 0.02249823
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.01876481,
                    "corr60Ltm": 0.03171659,
                    "corrLtm": null,
                    "date": "2025-07-03",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -3.6836e-4,
                    "mmc60": -0.00312037,
                    "mmc60Ltm": -0.00409293,
                    "mmcLtm": -0.00296255,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": -0.00327082,
                    "v2Corr20Ltm": 0.02263247
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.02200092,
                    "corr60Ltm": 0.03172847,
                    "corrLtm": null,
                    "date": "2025-07-02",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -7.406e-4,
                    "mmc60": -0.00106781,
                    "mmc60Ltm": -0.00409209,
                    "mmcLtm": -0.00293657,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.00230402,
                    "v2Corr20Ltm": 0.02277174
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.01589222,
                    "corr60Ltm": 0.03171956,
                    "corrLtm": null,
                    "date": "2025-07-01",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00499187,
                    "mmc60": -0.001431,
                    "mmc60Ltm": -0.00408736,
                    "mmcLtm": -0.00290465,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": -7.375e-4,
                    "v2Corr20Ltm": 0.02288237
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.02502391,
                    "corr60Ltm": 0.03178554,
                    "corrLtm": null,
                    "date": "2025-06-28",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00311245,
                    "mmc60": 8.96119976e-5,
                    "mmc60Ltm": -0.00407753,
                    "mmcLtm": -0.00286751,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": -0.00383672,
                    "v2Corr20Ltm": 0.02301074
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.01683026,
                    "corr60Ltm": 0.03177846,
                    "corrLtm": null,
                    "date": "2025-06-27",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00722976,
                    "mmc60": -0.00478205,
                    "mmc60Ltm": -0.0040696,
                    "mmcLtm": -0.00282883,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.00363016,
                    "v2Corr20Ltm": 0.02315745
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.02315415,
                    "corr60Ltm": 0.03176273,
                    "corrLtm": null,
                    "date": "2025-06-26",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00282528,
                    "mmc60": -0.00513626,
                    "mmc60Ltm": -0.00404209,
                    "mmcLtm": -0.00277828,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.0027046,
                    "v2Corr20Ltm": 0.02326474
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.02305235,
                    "corr60Ltm": 0.0317345,
                    "corrLtm": null,
                    "date": "2025-06-25",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00261477,
                    "mmc60": -0.00584425,
                    "mmc60Ltm": -0.00400796,
                    "mmcLtm": -0.00274741,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.00269621,
                    "v2Corr20Ltm": 0.02337833
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.02047585,
                    "corr60Ltm": 0.03174078,
                    "corrLtm": null,
                    "date": "2025-06-24",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00778283,
                    "mmc60": -0.00306749,
                    "mmc60Ltm": -0.00397709,
                    "mmcLtm": -0.00273014,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": -0.00361351,
                    "v2Corr20Ltm": 0.02349324
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.02342365,
                    "corr60Ltm": 0.03179053,
                    "corrLtm": null,
                    "date": "2025-06-21",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.01086173,
                    "mmc60": -0.00326812,
                    "mmc60Ltm": -0.00394203,
                    "mmcLtm": -0.00268268,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": -0.00815219,
                    "v2Corr20Ltm": 0.02364467
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.03167107,
                    "corr60Ltm": 0.03180758,
                    "corrLtm": null,
                    "date": "2025-06-20",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00741251,
                    "mmc60": -0.00273771,
                    "mmc60Ltm": -0.00391999,
                    "mmcLtm": -0.00263496,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.00344566,
                    "v2Corr20Ltm": 0.0238233
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.01917143,
                    "corr60Ltm": 0.03177933,
                    "corrLtm": null,
                    "date": "2025-06-19",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00452808,
                    "mmc60": -0.00612683,
                    "mmc60Ltm": -0.00389961,
                    "mmcLtm": -0.00259899,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.00100696,
                    "v2Corr20Ltm": 0.02393843
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.01974266,
                    "corr60Ltm": 0.03180343,
                    "corrLtm": null,
                    "date": "2025-06-18",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00504542,
                    "mmc60": -0.0083626,
                    "mmc60Ltm": -0.00385757,
                    "mmcLtm": -0.00257395,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": -0.00493414,
                    "v2Corr20Ltm": 0.02406872
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.0162559,
                    "corr60Ltm": 0.03180265,
                    "corrLtm": null,
                    "date": "2025-06-17",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00793196,
                    "mmc60": -0.00852,
                    "mmc60Ltm": -0.0038057,
                    "mmcLtm": -0.00255683,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.00669744,
                    "v2Corr20Ltm": 0.02423445
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.030346,
                    "corr60Ltm": 0.03181762,
                    "corrLtm": null,
                    "date": "2025-06-14",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00266887,
                    "mmc60": -0.00680089,
                    "mmc60Ltm": -0.00376079,
                    "mmcLtm": -0.00253715,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.01474747,
                    "v2Corr20Ltm": 0.02433524
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.0374417,
                    "corr60Ltm": 0.03180235,
                    "corrLtm": null,
                    "date": "2025-06-13",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00615409,
                    "mmc60": -0.0074167,
                    "mmc60Ltm": -0.00371725,
                    "mmcLtm": -0.00254434,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.00932966,
                    "v2Corr20Ltm": 0.02439066
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.03192314,
                    "corr60Ltm": 0.03175135,
                    "corrLtm": null,
                    "date": "2025-06-12",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00830762,
                    "mmc60": -0.00862349,
                    "mmc60Ltm": -0.00367262,
                    "mmcLtm": -0.00254171,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.00905968,
                    "v2Corr20Ltm": 0.02447823
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.02382963,
                    "corr60Ltm": 0.03170237,
                    "corrLtm": null,
                    "date": "2025-06-11",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.01111475,
                    "mmc60": -0.01121596,
                    "mmc60Ltm": -0.00364303,
                    "mmcLtm": -0.00251895,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.0032064,
                    "v2Corr20Ltm": 0.02456839
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.02856263,
                    "corr60Ltm": 0.03170979,
                    "corrLtm": null,
                    "date": "2025-06-10",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -1.651e-4,
                    "mmc60": -0.01148068,
                    "mmc60Ltm": -0.00359543,
                    "mmcLtm": -0.00249352,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.01825573,
                    "v2Corr20Ltm": 0.02469405
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.02995461,
                    "corr60Ltm": 0.03171362,
                    "corrLtm": null,
                    "date": "2025-06-07",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": 0.00127861,
                    "mmc60": -0.01436605,
                    "mmc60Ltm": -0.00354599,
                    "mmcLtm": -0.00250344,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.01025407,
                    "v2Corr20Ltm": 0.02473215
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.03877212,
                    "corr60Ltm": 0.03174399,
                    "corrLtm": null,
                    "date": "2025-06-06",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -9.1274e-4,
                    "mmc60": -0.01194829,
                    "mmc60Ltm": -0.00348324,
                    "mmcLtm": -0.00251833,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.00765804,
                    "v2Corr20Ltm": 0.02481833
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.04201164,
                    "corr60Ltm": 0.03171015,
                    "corrLtm": null,
                    "date": "2025-06-05",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": 0.00636691,
                    "mmc60": -0.00921111,
                    "mmc60Ltm": -0.00343286,
                    "mmcLtm": -0.00252243,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.00756842,
                    "v2Corr20Ltm": 0.02492108
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.04542215,
                    "corr60Ltm": 0.03167569,
                    "corrLtm": null,
                    "date": "2025-06-04",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": 0.00201545,
                    "mmc60": -0.0097282,
                    "mmc60Ltm": -0.003379,
                    "mmcLtm": -0.0025522,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": -0.00153446,
                    "v2Corr20Ltm": 0.02502562
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.05122406,
                    "corr60Ltm": 0.03164933,
                    "corrLtm": null,
                    "date": "2025-06-03",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": 0.00545019,
                    "mmc60": -0.00805516,
                    "mmc60Ltm": -0.00333527,
                    "mmcLtm": -0.00256363,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.01082851,
                    "v2Corr20Ltm": 0.02518659
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.05000023,
                    "corr60Ltm": 0.03160643,
                    "corrLtm": null,
                    "date": "2025-05-31",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": 0.0085479,
                    "mmc60": -0.00941255,
                    "mmc60Ltm": -0.00329704,
                    "mmcLtm": -0.00256464,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.02162695,
                    "v2Corr20Ltm": 0.02527414
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.04564231,
                    "corr60Ltm": 0.03157883,
                    "corrLtm": null,
                    "date": "2025-05-30",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": 0.00664702,
                    "mmc60": -0.01066623,
                    "mmc60Ltm": -0.00324016,
                    "mmcLtm": -0.00257471,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.02087116,
                    "v2Corr20Ltm": 0.02529651
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.04500874,
                    "corr60Ltm": 0.03157674,
                    "corrLtm": null,
                    "date": "2025-05-29",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": 0.00580686,
                    "mmc60": -0.00919093,
                    "mmc60Ltm": -0.00316407,
                    "mmcLtm": -0.00257884,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.02091126,
                    "v2Corr20Ltm": 0.02532383
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.04844366,
                    "corr60Ltm": 0.03160914,
                    "corrLtm": null,
                    "date": "2025-05-28",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": 0.00493061,
                    "mmc60": -0.00993377,
                    "mmc60Ltm": -0.00310223,
                    "mmcLtm": -0.00257756,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.02266982,
                    "v2Corr20Ltm": 0.02535124
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.03823175,
                    "corr60Ltm": 0.03161096,
                    "corrLtm": null,
                    "date": "2025-05-27",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": 0.00702292,
                    "mmc60": -0.01291716,
                    "mmc60Ltm": -0.00303495,
                    "mmcLtm": -0.00257251,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.03049251,
                    "v2Corr20Ltm": 0.025368
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.03831211,
                    "corr60Ltm": 0.0316188,
                    "corrLtm": null,
                    "date": "2025-05-24",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": 0.00259302,
                    "mmc60": -0.0121583,
                    "mmc60Ltm": -0.00296016,
                    "mmcLtm": -0.00259092,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.02352904,
                    "v2Corr20Ltm": 0.02533577
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.03615417,
                    "corr60Ltm": 0.03167252,
                    "corrLtm": null,
                    "date": "2025-05-23",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": 0.00918034,
                    "mmc60": -0.01173542,
                    "mmc60Ltm": -0.0028873,
                    "mmcLtm": -0.00258251,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.04191618,
                    "v2Corr20Ltm": 0.0253472
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.0287644,
                    "corr60Ltm": 0.03167198,
                    "corrLtm": null,
                    "date": "2025-05-22",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": 0.00797327,
                    "mmc60": -0.00821049,
                    "mmc60Ltm": -0.00282669,
                    "mmcLtm": -0.0025971,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.04309275,
                    "v2Corr20Ltm": 0.02524167
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.03071896,
                    "corr60Ltm": 0.03169362,
                    "corrLtm": null,
                    "date": "2025-05-21",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": 0.01090131,
                    "mmc60": -0.00991999,
                    "mmc60Ltm": -0.00278551,
                    "mmcLtm": -0.00260969,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.0422065,
                    "v2Corr20Ltm": 0.02512724
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.03835987,
                    "corr60Ltm": 0.03171903,
                    "corrLtm": null,
                    "date": "2025-05-20",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": 0.006619,
                    "mmc60": -0.00892864,
                    "mmc60Ltm": -0.00272673,
                    "mmcLtm": -0.00262384,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.04509038,
                    "v2Corr20Ltm": 0.02501705
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.03466013,
                    "corr60Ltm": 0.03168652,
                    "corrLtm": null,
                    "date": "2025-05-17",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": 0.00633237,
                    "mmc60": -0.01089071,
                    "mmc60Ltm": -0.00266554,
                    "mmcLtm": -0.00263846,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.04630447,
                    "v2Corr20Ltm": 0.0248867
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.03871252,
                    "corr60Ltm": 0.03169064,
                    "corrLtm": null,
                    "date": "2025-05-16",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": 0.00807292,
                    "mmc60": -0.00459015,
                    "mmc60Ltm": -0.00260664,
                    "mmcLtm": -0.00264395,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.04095125,
                    "v2Corr20Ltm": 0.02474672
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.04263699,
                    "corr60Ltm": 0.03169656,
                    "corrLtm": null,
                    "date": "2025-05-15",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": 0.00546721,
                    "mmc60": -0.00471759,
                    "mmc60Ltm": -0.00257416,
                    "mmcLtm": -0.0026761,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.04459504,
                    "v2Corr20Ltm": 0.02464011
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.04560342,
                    "corr60Ltm": 0.03171012,
                    "corrLtm": null,
                    "date": "2025-05-14",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": 0.00646584,
                    "mmc60": -0.00947215,
                    "mmc60Ltm": -0.0025433,
                    "mmcLtm": -0.00268626,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.04650737,
                    "v2Corr20Ltm": 0.02450796
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.04754167,
                    "corr60Ltm": 0.03171361,
                    "corrLtm": null,
                    "date": "2025-05-13",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": 0.00392432,
                    "mmc60": -0.00318238,
                    "mmc60Ltm": -0.00249938,
                    "mmcLtm": -0.00269791,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.03459915,
                    "v2Corr20Ltm": 0.02436129
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.04997954,
                    "corr60Ltm": 0.0317029,
                    "corrLtm": null,
                    "date": "2025-05-10",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": 0.00307572,
                    "mmc60": -0.0014924,
                    "mmc60Ltm": -0.00248257,
                    "mmcLtm": -0.00268637,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.02073798,
                    "v2Corr20Ltm": 0.02429258
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.05147014,
                    "corr60Ltm": 0.03162813,
                    "corrLtm": null,
                    "date": "2025-05-09",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00187724,
                    "mmc60": -0.00455157,
                    "mmc60Ltm": -0.00247737,
                    "mmcLtm": -0.0026815,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.01097857,
                    "v2Corr20Ltm": 0.0243166
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.04606685,
                    "corr60Ltm": 0.03155154,
                    "corrLtm": null,
                    "date": "2025-05-08",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": 0.00272101,
                    "mmc60": -0.00567676,
                    "mmc60Ltm": -0.00246929,
                    "mmcLtm": -0.00265174,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.02616862,
                    "v2Corr20Ltm": 0.02440733
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.051429,
                    "corr60Ltm": 0.03148392,
                    "corrLtm": null,
                    "date": "2025-05-07",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": 0.00312514,
                    "mmc60": -0.00407328,
                    "mmc60Ltm": -0.00244774,
                    "mmcLtm": -0.0026402,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.02786438,
                    "v2Corr20Ltm": 0.02439527
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.0496361,
                    "corr60Ltm": 0.03141561,
                    "corrLtm": null,
                    "date": "2025-05-06",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": 4.2731e-4,
                    "mmc60": -0.00303021,
                    "mmc60Ltm": -0.00243594,
                    "mmcLtm": -0.00263412,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.02227663,
                    "v2Corr20Ltm": 0.02437135
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.04406837,
                    "corr60Ltm": 0.03133606,
                    "corrLtm": null,
                    "date": "2025-05-03",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": 0.00436647,
                    "mmc60": -0.00549388,
                    "mmc60Ltm": -0.00243133,
                    "mmcLtm": -0.00261929,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.03059294,
                    "v2Corr20Ltm": 0.02438589
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.03545992,
                    "corr60Ltm": 0.03131136,
                    "corrLtm": null,
                    "date": "2025-05-02",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.001024,
                    "mmc60": -0.00758413,
                    "mmc60Ltm": -0.0024169,
                    "mmcLtm": -0.00262612,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.02979504,
                    "v2Corr20Ltm": 0.02434249
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.04266126,
                    "corr60Ltm": 0.03117549,
                    "corrLtm": null,
                    "date": "2025-05-01",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": 0.00144389,
                    "mmc60": -0.00629712,
                    "mmc60Ltm": -0.0023662,
                    "mmcLtm": -0.00261259,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.02311064,
                    "v2Corr20Ltm": 0.02430409
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.03561603,
                    "corr60Ltm": 0.03101204,
                    "corrLtm": null,
                    "date": "2025-04-30",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": 0.00222776,
                    "mmc60": -0.00580008,
                    "mmc60Ltm": -0.00234207,
                    "mmcLtm": -0.00260714,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.0262437,
                    "v2Corr20Ltm": 0.02431255
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.03596102,
                    "corr60Ltm": 0.03087558,
                    "corrLtm": null,
                    "date": "2025-04-29",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": 7.3732e-4,
                    "mmc60": -0.00672088,
                    "mmc60Ltm": -0.00231985,
                    "mmcLtm": -0.00260587,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.02480806,
                    "v2Corr20Ltm": 0.02429876
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.03196964,
                    "corr60Ltm": 0.0307378,
                    "corrLtm": null,
                    "date": "2025-04-26",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -5.5784e-4,
                    "mmc60": -0.00512716,
                    "mmc60Ltm": -0.0022941,
                    "mmcLtm": -0.00259331,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.02377158,
                    "v2Corr20Ltm": 0.0242951
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.02861483,
                    "corr60Ltm": 0.03061531,
                    "corrLtm": null,
                    "date": "2025-04-25",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00493618,
                    "mmc60": -0.00343731,
                    "mmc60Ltm": -0.00227445,
                    "mmcLtm": -0.00259173,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.01376196,
                    "v2Corr20Ltm": 0.02429889
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.02571472,
                    "corr60Ltm": 0.03050567,
                    "corrLtm": null,
                    "date": "2025-04-24",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00496695,
                    "mmc60": -0.00678656,
                    "mmc60Ltm": -0.00226128,
                    "mmcLtm": -0.00256461,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.01557259,
                    "v2Corr20Ltm": 0.0243758
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.03759912,
                    "corr60Ltm": 0.03040715,
                    "corrLtm": null,
                    "date": "2025-04-23",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00266264,
                    "mmc60": -0.0049885,
                    "mmc60Ltm": -0.00216963,
                    "mmcLtm": -0.00254956,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.01647186,
                    "v2Corr20Ltm": 0.02444053
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.04172111,
                    "corr60Ltm": 0.03026309,
                    "corrLtm": null,
                    "date": "2025-04-22",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00534637,
                    "mmc60": -0.00259484,
                    "mmc60Ltm": -0.00215051,
                    "mmcLtm": -0.00254148,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.01110782,
                    "v2Corr20Ltm": 0.02449956
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.0370047,
                    "corr60Ltm": 0.03027666,
                    "corrLtm": null,
                    "date": "2025-04-19",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00295253,
                    "mmc60": -0.00404509,
                    "mmc60Ltm": -0.00214601,
                    "mmcLtm": -0.00252291,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.01964937,
                    "v2Corr20Ltm": 0.0245995
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.04703576,
                    "corr60Ltm": 0.03026703,
                    "corrLtm": null,
                    "date": "2025-04-18",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00480305,
                    "mmc60": -0.00364441,
                    "mmc60Ltm": -0.00214727,
                    "mmcLtm": -0.00251803,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.03575537,
                    "v2Corr20Ltm": 0.02463671
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.03482102,
                    "corr60Ltm": 0.03023246,
                    "corrLtm": null,
                    "date": "2025-04-17",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00153031,
                    "mmc60": -0.00509816,
                    "mmc60Ltm": -0.00212215,
                    "mmcLtm": -0.00249202,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.02909302,
                    "v2Corr20Ltm": 0.02455248
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.03558196,
                    "corr60Ltm": 0.03024848,
                    "corrLtm": null,
                    "date": "2025-04-16",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -6.0546e-4,
                    "mmc60": -0.00421909,
                    "mmc60Ltm": -0.00212939,
                    "mmcLtm": -0.00250111,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.0375622,
                    "v2Corr20Ltm": 0.02451782
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.03142202,
                    "corr60Ltm": 0.03027544,
                    "corrLtm": null,
                    "date": "2025-04-15",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00328059,
                    "mmc60": -0.00565084,
                    "mmc60Ltm": -0.00214206,
                    "mmcLtm": -0.00251479,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.0427501,
                    "v2Corr20Ltm": 0.02441748
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.03907105,
                    "corr60Ltm": 0.03033474,
                    "corrLtm": null,
                    "date": "2025-04-12",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00541505,
                    "mmc60": -0.00838013,
                    "mmc60Ltm": -0.0021618,
                    "mmcLtm": -0.0024811,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.03629205,
                    "v2Corr20Ltm": 0.02427537
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.04430256,
                    "corr60Ltm": 0.03032883,
                    "corrLtm": null,
                    "date": "2025-04-11",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00550033,
                    "mmc60": -0.00453599,
                    "mmc60Ltm": -0.00215975,
                    "mmcLtm": -0.00247362,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.05335826,
                    "v2Corr20Ltm": 0.02418149
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.03307641,
                    "corr60Ltm": 0.03030201,
                    "corrLtm": null,
                    "date": "2025-04-10",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00894817,
                    "mmc60": -0.00582267,
                    "mmc60Ltm": -0.00214847,
                    "mmcLtm": -0.00250812,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.04257493,
                    "v2Corr20Ltm": 0.02395175
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.03399055,
                    "corr60Ltm": 0.03032183,
                    "corrLtm": null,
                    "date": "2025-04-09",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00986668,
                    "mmc60": -0.00497671,
                    "mmc60Ltm": -0.00213261,
                    "mmcLtm": -0.00246074,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.04460359,
                    "v2Corr20Ltm": 0.02380395
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.04305744,
                    "corr60Ltm": 0.03029311,
                    "corrLtm": null,
                    "date": "2025-04-08",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00644035,
                    "mmc60": -0.00263461,
                    "mmc60Ltm": -0.00213081,
                    "mmcLtm": -0.00241134,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.0408031,
                    "v2Corr20Ltm": 0.02363755
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.05927094,
                    "corr60Ltm": 0.03024834,
                    "corrLtm": null,
                    "date": "2025-04-05",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.01398196,
                    "mmc60": 0.00246277,
                    "mmc60Ltm": -0.00213989,
                    "mmcLtm": -0.00239287,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.03547984,
                    "v2Corr20Ltm": 0.02349912
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.0537543,
                    "corr60Ltm": 0.03014896,
                    "corrLtm": null,
                    "date": "2025-04-04",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.01225329,
                    "mmc60": 0.00212785,
                    "mmc60Ltm": -0.00216464,
                    "mmcLtm": -0.00234788,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.05767842,
                    "v2Corr20Ltm": 0.02340171
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.05608294,
                    "corr60Ltm": 0.03005112,
                    "corrLtm": null,
                    "date": "2025-04-03",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.01065798,
                    "mmc60": 0.00206516,
                    "mmc60Ltm": -0.0021806,
                    "mmcLtm": -0.00230266,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.04636981,
                    "v2Corr20Ltm": 0.02312076
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.05272481,
                    "corr60Ltm": 0.02993342,
                    "corrLtm": null,
                    "date": "2025-04-02",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.01402961,
                    "mmc60": 0.00215985,
                    "mmc60Ltm": -0.00220333,
                    "mmcLtm": -0.00226495,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.04873908,
                    "v2Corr20Ltm": 0.02292861
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.04657163,
                    "corr60Ltm": 0.02984979,
                    "corrLtm": null,
                    "date": "2025-04-01",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.01126479,
                    "mmc60": -0.00324911,
                    "mmc60Ltm": -0.00222296,
                    "mmcLtm": -0.00220988,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.04403314,
                    "v2Corr20Ltm": 0.02271353
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.04558444,
                    "corr60Ltm": 0.02977749,
                    "corrLtm": null,
                    "date": "2025-03-29",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.01418134,
                    "mmc60": -0.00301517,
                    "mmc60Ltm": -0.00222066,
                    "mmcLtm": -0.00216756,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.04041396,
                    "v2Corr20Ltm": 0.02253437
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.04849354,
                    "corr60Ltm": 0.02969684,
                    "corrLtm": null,
                    "date": "2025-03-28",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.01430779,
                    "mmc60": -0.001172,
                    "mmc60Ltm": -0.00222514,
                    "mmcLtm": -0.00211741,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.03677648,
                    "v2Corr20Ltm": 0.02238285
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.05422865,
                    "corr60Ltm": 0.02962828,
                    "corrLtm": null,
                    "date": "2025-03-27",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00998278,
                    "mmc60": -0.00364723,
                    "mmc60Ltm": -0.00223463,
                    "mmcLtm": -0.00207619,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.03254468,
                    "v2Corr20Ltm": 0.02225983
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.04270346,
                    "corr60Ltm": 0.02951386,
                    "corrLtm": null,
                    "date": "2025-03-26",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00827981,
                    "mmc60": -0.00470738,
                    "mmc60Ltm": -0.00225717,
                    "mmcLtm": -0.00204474,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.03927873,
                    "v2Corr20Ltm": 0.02217116
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.04744011,
                    "corr60Ltm": 0.02946167,
                    "corrLtm": null,
                    "date": "2025-03-25",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.01362691,
                    "mmc60": -0.00517481,
                    "mmc60Ltm": -0.00226822,
                    "mmcLtm": -0.00201683,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.0419257,
                    "v2Corr20Ltm": 0.0220224
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.05207203,
                    "corr60Ltm": 0.02939739,
                    "corrLtm": null,
                    "date": "2025-03-22",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00600376,
                    "mmc60": -0.00340222,
                    "mmc60Ltm": -0.00227638,
                    "mmcLtm": -0.0019685,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.0427531,
                    "v2Corr20Ltm": 0.02184781
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.04740256,
                    "corr60Ltm": 0.02931529,
                    "corrLtm": null,
                    "date": "2025-03-21",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.006121,
                    "mmc60": -0.00425965,
                    "mmc60Ltm": -0.00229218,
                    "mmcLtm": -0.00195558,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.03153333,
                    "v2Corr20Ltm": 0.02166281
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.05301601,
                    "corr60Ltm": 0.02925998,
                    "corrLtm": null,
                    "date": "2025-03-20",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00208231,
                    "mmc60": -0.00240282,
                    "mmc60Ltm": -0.00229309,
                    "mmcLtm": -0.00194845,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.05689224,
                    "v2Corr20Ltm": 0.02157468
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.04779507,
                    "corr60Ltm": 0.02916721,
                    "corrLtm": null,
                    "date": "2025-03-19",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00853562,
                    "mmc60": 2.013e-4,
                    "mmc60Ltm": -0.00230508,
                    "mmcLtm": -0.00195736,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.04829459,
                    "v2Corr20Ltm": 0.0212565
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.03985888,
                    "corr60Ltm": 0.02910426,
                    "corrLtm": null,
                    "date": "2025-03-18",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00367217,
                    "mmc60": -0.00153508,
                    "mmc60Ltm": -0.00232352,
                    "mmcLtm": -0.00194676,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.04724979,
                    "v2Corr20Ltm": 0.0210107
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.03686958,
                    "corr60Ltm": 0.02905432,
                    "corrLtm": null,
                    "date": "2025-03-15",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00215814,
                    "mmc60": 0.00112405,
                    "mmc60Ltm": -0.00232971,
                    "mmcLtm": -0.00195075,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.04641485,
                    "v2Corr20Ltm": 0.02076998
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.04016439,
                    "corr60Ltm": 0.0290315,
                    "corrLtm": null,
                    "date": "2025-03-14",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00293719,
                    "mmc60": 0.00588881,
                    "mmc60Ltm": -0.002348,
                    "mmcLtm": -0.00196329,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.03029982,
                    "v2Corr20Ltm": 0.02053252
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.05281994,
                    "corr60Ltm": 0.02897881,
                    "corrLtm": null,
                    "date": "2025-03-13",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -8.944e-4,
                    "mmc60": 0.00507072,
                    "mmc60Ltm": -0.00238022,
                    "mmcLtm": -0.00197683,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.03850851,
                    "v2Corr20Ltm": 0.02044124
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.05606637,
                    "corr60Ltm": 0.02884905,
                    "corrLtm": null,
                    "date": "2025-03-12",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -3.22671273e-5,
                    "mmc60": 0.00348315,
                    "mmc60Ltm": -0.00241025,
                    "mmcLtm": -0.00200285,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.03919888,
                    "v2Corr20Ltm": 0.0202708
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.04674275,
                    "corr60Ltm": 0.02868242,
                    "corrLtm": null,
                    "date": "2025-03-11",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00279633,
                    "mmc60": 7.4895e-4,
                    "mmc60Ltm": -0.00243736,
                    "mmcLtm": -0.00202397,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.02642735,
                    "v2Corr20Ltm": 0.02009053
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.04557626,
                    "corr60Ltm": 0.02859516,
                    "corrLtm": null,
                    "date": "2025-03-08",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": 8.2845e-4,
                    "mmc60": -0.00288181,
                    "mmc60Ltm": -0.00244964,
                    "mmcLtm": -0.00202855,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.03384353,
                    "v2Corr20Ltm": 0.0200296
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.03933549,
                    "corr60Ltm": 0.02850253,
                    "corrLtm": null,
                    "date": "2025-03-07",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00141992,
                    "mmc60": -0.00272747,
                    "mmc60Ltm": -0.00244327,
                    "mmcLtm": -0.0020385,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.0254944,
                    "v2Corr20Ltm": 0.01989548
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.04463232,
                    "corr60Ltm": 0.02842384,
                    "corrLtm": null,
                    "date": "2025-03-06",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00346254,
                    "mmc60": 5.17129715e-5,
                    "mmc60Ltm": -0.00244362,
                    "mmcLtm": -0.00204869,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.01527589,
                    "v2Corr20Ltm": 0.01984059
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.03379214,
                    "corr60Ltm": 0.02833086,
                    "corrLtm": null,
                    "date": "2025-03-05",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": 0.00133908,
                    "mmc60": -0.00132262,
                    "mmc60Ltm": -0.00245414,
                    "mmcLtm": -0.00204453,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.01380471,
                    "v2Corr20Ltm": 0.01988579
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.04718006,
                    "corr60Ltm": 0.0282734,
                    "corrLtm": null,
                    "date": "2025-03-04",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -6.0523e-4,
                    "mmc60": -9.3188e-4,
                    "mmc60Ltm": -0.00246822,
                    "mmcLtm": -0.00205396,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.02184603,
                    "v2Corr20Ltm": 0.0199466
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.04834206,
                    "corr60Ltm": 0.02818113,
                    "corrLtm": null,
                    "date": "2025-03-01",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00383127,
                    "mmc60": -1.1441e-4,
                    "mmc60Ltm": -0.00248457,
                    "mmcLtm": -0.00204048,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.02071477,
                    "v2Corr20Ltm": 0.01992741
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.04938603,
                    "corr60Ltm": 0.02800034,
                    "corrLtm": null,
                    "date": "2025-02-28",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": 0.00133974,
                    "mmc60": 1.762e-4,
                    "mmc60Ltm": -0.00250668,
                    "mmcLtm": -0.00199253,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.02936422,
                    "v2Corr20Ltm": 0.01991938
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.05848589,
                    "corr60Ltm": 0.02788669,
                    "corrLtm": null,
                    "date": "2025-02-27",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00292536,
                    "mmc60": -0.00244984,
                    "mmc60Ltm": -0.00252702,
                    "mmcLtm": -0.00197682,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.02906285,
                    "v2Corr20Ltm": 0.01982201
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.0597859,
                    "corr60Ltm": 0.02776757,
                    "corrLtm": null,
                    "date": "2025-02-26",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -3.2618e-4,
                    "mmc60": -4.4362e-4,
                    "mmc60Ltm": -0.00253188,
                    "mmcLtm": -0.00195509,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.02150312,
                    "v2Corr20Ltm": 0.01972575
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.06106463,
                    "corr60Ltm": 0.0276449,
                    "corrLtm": null,
                    "date": "2025-02-25",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": 0.00196875,
                    "mmc60": -0.00229496,
                    "mmc60Ltm": -0.00253989,
                    "mmcLtm": -0.00196133,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.02339247,
                    "v2Corr20Ltm": 0.01970704
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.04109213,
                    "corr60Ltm": 0.02748112,
                    "corrLtm": null,
                    "date": "2025-02-22",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00316576,
                    "mmc60": -0.00401949,
                    "mmc60Ltm": -0.00254366,
                    "mmcLtm": -0.00194802,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.00943919,
                    "v2Corr20Ltm": 0.01966783
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.05416609,
                    "corr60Ltm": 0.02740408,
                    "corrLtm": null,
                    "date": "2025-02-21",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00810141,
                    "mmc60": -0.00317996,
                    "mmc60Ltm": -0.00254556,
                    "mmcLtm": -0.00193594,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.00520688,
                    "v2Corr20Ltm": 0.01977782
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.05575187,
                    "corr60Ltm": 0.0272698,
                    "corrLtm": null,
                    "date": "2025-02-20",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00521112,
                    "mmc60": -0.00596837,
                    "mmc60Ltm": -0.0025483,
                    "mmcLtm": -0.00188858,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.01065689,
                    "v2Corr20Ltm": 0.0199362
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.04246162,
                    "corr60Ltm": 0.02713832,
                    "corrLtm": null,
                    "date": "2025-02-19",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00778122,
                    "mmc60": -0.00655,
                    "mmc60Ltm": -0.00254,
                    "mmcLtm": -0.00185416,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": -0.00464841,
                    "v2Corr20Ltm": 0.02003817
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.04466309,
                    "corr60Ltm": 0.02707961,
                    "corrLtm": null,
                    "date": "2025-02-18",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.0037964,
                    "mmc60": -0.00554581,
                    "mmc60Ltm": -0.00252464,
                    "mmcLtm": -0.00183145,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.00743823,
                    "v2Corr20Ltm": 0.02031246
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.03643913,
                    "corr60Ltm": 0.02698942,
                    "corrLtm": null,
                    "date": "2025-02-15",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00471684,
                    "mmc60": -0.00294879,
                    "mmc60Ltm": -0.00251802,
                    "mmcLtm": -0.00178281,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.01273979,
                    "v2Corr20Ltm": 0.02045712
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.0440179,
                    "corr60Ltm": 0.0269223,
                    "corrLtm": null,
                    "date": "2025-02-14",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00689742,
                    "mmc60": -0.01060321,
                    "mmc60Ltm": -0.00251417,
                    "mmcLtm": -0.00174731,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.00754737,
                    "v2Corr20Ltm": 0.02054481
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.04753327,
                    "corr60Ltm": 0.02680887,
                    "corrLtm": null,
                    "date": "2025-02-13",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00813371,
                    "mmc60": -0.00742346,
                    "mmc60Ltm": -0.00248333,
                    "mmcLtm": -0.00171874,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.01681742,
                    "v2Corr20Ltm": 0.02069421
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.04494901,
                    "corr60Ltm": 0.02668716,
                    "corrLtm": null,
                    "date": "2025-02-12",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.0040606,
                    "mmc60": -0.00947639,
                    "mmc60Ltm": -0.00245367,
                    "mmcLtm": -0.00169199,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.01930938,
                    "v2Corr20Ltm": 0.02073929
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.04110403,
                    "corr60Ltm": 0.02661719,
                    "corrLtm": null,
                    "date": "2025-02-11",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00389475,
                    "mmc60": -0.00749121,
                    "mmc60Ltm": -0.00242676,
                    "mmcLtm": -0.00168292,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.02355375,
                    "v2Corr20Ltm": 0.02075611
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.05448629,
                    "corr60Ltm": 0.02635225,
                    "corrLtm": null,
                    "date": "2025-02-08",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00395483,
                    "mmc60": -0.0075856,
                    "mmc60Ltm": -0.00241142,
                    "mmcLtm": -0.00165243,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.02614143,
                    "v2Corr20Ltm": 0.02072281
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.04887803,
                    "corr60Ltm": 0.02613354,
                    "corrLtm": null,
                    "date": "2025-02-07",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00257074,
                    "mmc60": -0.00442985,
                    "mmc60Ltm": -0.00239848,
                    "mmcLtm": -0.00162587,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.03483447,
                    "v2Corr20Ltm": 0.02065752
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.04359896,
                    "corr60Ltm": 0.02596063,
                    "corrLtm": null,
                    "date": "2025-02-06",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00498161,
                    "mmc60": -0.00363422,
                    "mmc60Ltm": -0.00239955,
                    "mmcLtm": -0.00160552,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.03545086,
                    "v2Corr20Ltm": 0.02048463
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.04386562,
                    "corr60Ltm": 0.02585846,
                    "corrLtm": null,
                    "date": "2025-02-05",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00881544,
                    "mmc60": -0.00894542,
                    "mmc60Ltm": -0.00240447,
                    "mmcLtm": -0.00157099,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.03092849,
                    "v2Corr20Ltm": 0.02029986
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.04794279,
                    "corr60Ltm": 0.02578947,
                    "corrLtm": null,
                    "date": "2025-02-04",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00102096,
                    "mmc60": -0.00845407,
                    "mmc60Ltm": -0.00237941,
                    "mmcLtm": -0.00154323,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.0336143,
                    "v2Corr20Ltm": 0.020167
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.04132996,
                    "corr60Ltm": 0.02561828,
                    "corrLtm": null,
                    "date": "2025-02-01",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.0010504,
                    "mmc60": -0.00763446,
                    "mmc60Ltm": -0.00237423,
                    "mmcLtm": -0.00148956,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.02998795,
                    "v2Corr20Ltm": 0.01999679
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": null,
                    "corr60Ltm": null,
                    "corrLtm": null,
                    "date": "2025-01-31",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00122256,
                    "mmc60": -0.00356848,
                    "mmc60Ltm": -0.00235233,
                    "mmcLtm": -0.00147963,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.03881795,
                    "v2Corr20Ltm": 0.01986869
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.03805648,
                    "corr60Ltm": 0.02552166,
                    "corrLtm": null,
                    "date": "2025-01-30",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": 3.696e-4,
                    "mmc60": -0.00799557,
                    "mmc60Ltm": -0.00234705,
                    "mmcLtm": -0.00148873,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.03742827,
                    "v2Corr20Ltm": 0.0196226
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.03058732,
                    "corr60Ltm": 0.02546181,
                    "corrLtm": null,
                    "date": "2025-01-29",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00345243,
                    "mmc60": -0.01085561,
                    "mmc60Ltm": -0.00232871,
                    "mmcLtm": -0.00149583,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.02535389,
                    "v2Corr20Ltm": 0.01938831
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.02632392,
                    "corr60Ltm": 0.02544217,
                    "corrLtm": null,
                    "date": "2025-01-28",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00706718,
                    "mmc60": -0.00942404,
                    "mmc60Ltm": -0.00229604,
                    "mmcLtm": -0.00148833,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.02102169,
                    "v2Corr20Ltm": 0.01930877
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.02455368,
                    "corr60Ltm": 0.02548858,
                    "corrLtm": null,
                    "date": "2025-01-25",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00345474,
                    "mmc60": -0.00940399,
                    "mmc60Ltm": -0.00225073,
                    "mmcLtm": -0.00149887,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.02408183,
                    "v2Corr20Ltm": 0.01928563
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.03010544,
                    "corr60Ltm": 0.02550498,
                    "corrLtm": null,
                    "date": "2025-01-24",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00231092,
                    "mmc60": -0.00503876,
                    "mmc60Ltm": -0.0022134,
                    "mmcLtm": -0.00149356,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.0235971,
                    "v2Corr20Ltm": 0.01921992
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.02508062,
                    "corr60Ltm": 0.02547037,
                    "corrLtm": null,
                    "date": "2025-01-23",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -9.054e-4,
                    "mmc60": -0.00835934,
                    "mmc60Ltm": -0.00219664,
                    "mmcLtm": -0.0014968,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.02580822,
                    "v2Corr20Ltm": 0.01915913
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.02937956,
                    "corr60Ltm": 0.02546442,
                    "corrLtm": null,
                    "date": "2025-01-22",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": 8.4181e-4,
                    "mmc60": -0.00646533,
                    "mmc60Ltm": -0.00216165,
                    "mmcLtm": -0.00149906,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.02252344,
                    "v2Corr20Ltm": 0.01906548
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.02422858,
                    "corr60Ltm": 0.02544942,
                    "corrLtm": null,
                    "date": "2025-01-21",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -5.5762e-4,
                    "mmc60": -0.00753277,
                    "mmc60Ltm": -0.00214516,
                    "mmcLtm": -0.00150803,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.02750258,
                    "v2Corr20Ltm": 0.01901608
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.02833624,
                    "corr60Ltm": 0.02544247,
                    "corrLtm": null,
                    "date": "2025-01-18",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -4.4236e-4,
                    "mmc60": -0.00936608,
                    "mmc60Ltm": -0.00211047,
                    "mmcLtm": -0.00154289,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.00874336,
                    "v2Corr20Ltm": 0.01889309
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.02306441,
                    "corr60Ltm": 0.02541979,
                    "corrLtm": null,
                    "date": "2025-01-17",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": 0.00372227,
                    "mmc60": -0.00830867,
                    "mmc60Ltm": -0.00208406,
                    "mmcLtm": -0.00154313,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.01463624,
                    "v2Corr20Ltm": 0.01904235
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.02467709,
                    "corr60Ltm": 0.02539722,
                    "corrLtm": null,
                    "date": "2025-01-16",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.0036227,
                    "mmc60": -0.0108943,
                    "mmc60Ltm": -0.00204464,
                    "mmcLtm": -0.00155639,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.02066997,
                    "v2Corr20Ltm": 0.01910811
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.02982292,
                    "corr60Ltm": 0.02540958,
                    "corrLtm": null,
                    "date": "2025-01-15",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00691199,
                    "mmc60": -0.00781326,
                    "mmc60Ltm": -0.00199555,
                    "mmcLtm": -0.0015485,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.02278063,
                    "v2Corr20Ltm": 0.01908445
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.0297067,
                    "corr60Ltm": 0.02539267,
                    "corrLtm": null,
                    "date": "2025-01-14",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00958705,
                    "mmc60": -0.00806968,
                    "mmc60Ltm": -0.00197326,
                    "mmcLtm": -0.00152795,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.01732231,
                    "v2Corr20Ltm": 0.01902758
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.03316656,
                    "corr60Ltm": 0.02536498,
                    "corrLtm": null,
                    "date": "2025-01-11",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00890997,
                    "mmc60": -0.00856574,
                    "mmc60Ltm": -0.00195454,
                    "mmcLtm": -0.00150034,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.01155511,
                    "v2Corr20Ltm": 0.01905423
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.03395664,
                    "corr60Ltm": 0.02530811,
                    "corrLtm": null,
                    "date": "2025-01-10",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00945186,
                    "mmc60": -0.00641701,
                    "mmc60Ltm": -0.00193522,
                    "mmcLtm": -0.00146599,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.01018955,
                    "v2Corr20Ltm": 0.01917326
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.02676447,
                    "corr60Ltm": 0.02525755,
                    "corrLtm": null,
                    "date": "2025-01-09",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00811568,
                    "mmc60": -0.00547199,
                    "mmc60Ltm": -0.00191388,
                    "mmcLtm": -0.00144312,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.01859246,
                    "v2Corr20Ltm": 0.01931816
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.02575545,
                    "corr60Ltm": 0.02521669,
                    "corrLtm": null,
                    "date": "2025-01-08",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00248301,
                    "mmc60": -0.00850174,
                    "mmc60Ltm": -0.0018811,
                    "mmcLtm": -0.00141765,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.02168743,
                    "v2Corr20Ltm": 0.01933006
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.03326297,
                    "corr60Ltm": 0.02521462,
                    "corrLtm": null,
                    "date": "2025-01-07",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00245869,
                    "mmc60": -0.00750641,
                    "mmc60Ltm": -0.00185573,
                    "mmcLtm": -0.00141357,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.03759616,
                    "v2Corr20Ltm": 0.01929077
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.02292691,
                    "corr60Ltm": 0.02507627,
                    "corrLtm": null,
                    "date": "2025-01-04",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00240977,
                    "mmc60": -0.0092349,
                    "mmc60Ltm": -0.00182492,
                    "mmcLtm": -0.00142092,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.03513891,
                    "v2Corr20Ltm": 0.01898051
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.03225892,
                    "corr60Ltm": 0.02498876,
                    "corrLtm": null,
                    "date": "2025-01-03",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00105937,
                    "mmc60": -0.0084549,
                    "mmc60Ltm": -0.00178967,
                    "mmcLtm": -0.00141953,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.04327412,
                    "v2Corr20Ltm": 0.01870191
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.03003115,
                    "corr60Ltm": 0.02489749,
                    "corrLtm": null,
                    "date": "2025-01-02",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00663908,
                    "mmc60": -0.00914816,
                    "mmc60Ltm": -0.00174852,
                    "mmcLtm": -0.00141299,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.04693436,
                    "v2Corr20Ltm": 0.01827082
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.02986694,
                    "corr60Ltm": 0.02482139,
                    "corrLtm": null,
                    "date": "2025-01-01",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00509581,
                    "mmc60": -0.0088146,
                    "mmc60Ltm": -0.00171077,
                    "mmcLtm": -0.00139304,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.0514069,
                    "v2Corr20Ltm": 0.01775897
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.03493967,
                    "corr60Ltm": 0.02480206,
                    "corrLtm": null,
                    "date": "2024-12-31",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00584763,
                    "mmc60": -0.00612685,
                    "mmc60Ltm": -0.00168355,
                    "mmcLtm": -0.00137885,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.0488648,
                    "v2Corr20Ltm": 0.01714719
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.03346782,
                    "corr60Ltm": 0.02461853,
                    "corrLtm": null,
                    "date": "2024-12-28",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00568249,
                    "mmc60": -0.00549376,
                    "mmc60Ltm": -0.00166234,
                    "mmcLtm": -0.00131565,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.03759582,
                    "v2Corr20Ltm": 0.01655983
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.03630073,
                    "corr60Ltm": 0.02449079,
                    "corrLtm": null,
                    "date": "2024-12-27",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.004401,
                    "mmc60": -0.0080917,
                    "mmc60Ltm": -0.00164137,
                    "mmcLtm": -0.00129484,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.03716625,
                    "v2Corr20Ltm": 0.01616293
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.0331512,
                    "corr60Ltm": 0.0243788,
                    "corrLtm": null,
                    "date": "2024-12-26",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00677445,
                    "mmc60": -0.00833411,
                    "mmc60Ltm": -0.00160226,
                    "mmcLtm": -0.00127578,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.02937603,
                    "v2Corr20Ltm": 0.01575902
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.02899279,
                    "corr60Ltm": 0.0242482,
                    "corrLtm": null,
                    "date": "2024-12-25",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00615904,
                    "mmc60": -0.00781336,
                    "mmc60Ltm": -0.00156249,
                    "mmcLtm": -0.0012548,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.02845344,
                    "v2Corr20Ltm": 0.01549201
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.02707531,
                    "corr60Ltm": 0.02423002,
                    "corrLtm": null,
                    "date": "2024-12-24",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00604439,
                    "mmc60": -0.01020846,
                    "mmc60Ltm": -0.00153854,
                    "mmcLtm": -0.00123601,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.03802172,
                    "v2Corr20Ltm": 0.01523279
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.02470032,
                    "corr60Ltm": 0.0240709,
                    "corrLtm": null,
                    "date": "2024-12-21",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00595386,
                    "mmc60": -0.01225892,
                    "mmc60Ltm": -0.00148228,
                    "mmcLtm": -0.00122828,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.03098701,
                    "v2Corr20Ltm": 0.01476771
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.03049626,
                    "corr60Ltm": 0.02397663,
                    "corrLtm": null,
                    "date": "2024-12-20",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00734181,
                    "mmc60": -0.01242752,
                    "mmc60Ltm": -0.00143549,
                    "mmcLtm": -0.00120564,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.03908152,
                    "v2Corr20Ltm": 0.0144298
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.02189629,
                    "corr60Ltm": 0.02389221,
                    "corrLtm": null,
                    "date": "2024-12-19",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00459981,
                    "mmc60": -0.01230467,
                    "mmc60Ltm": -0.00137245,
                    "mmcLtm": -0.00118028,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.02948507,
                    "v2Corr20Ltm": 0.0139053
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.0260191,
                    "corr60Ltm": 0.02387953,
                    "corrLtm": null,
                    "date": "2024-12-18",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00676735,
                    "mmc60": -0.01236782,
                    "mmc60Ltm": -0.00131038,
                    "mmcLtm": -0.00116723,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.02022022,
                    "v2Corr20Ltm": 0.01356661
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.02830138,
                    "corr60Ltm": 0.02387134,
                    "corrLtm": null,
                    "date": "2024-12-17",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00317324,
                    "mmc60": -0.01289099,
                    "mmc60Ltm": -0.00126802,
                    "mmcLtm": -0.00114577,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.01984719,
                    "v2Corr20Ltm": 0.01341875
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.0342489,
                    "corr60Ltm": 0.02379191,
                    "corrLtm": null,
                    "date": "2024-12-14",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00583865,
                    "mmc60": -0.01351081,
                    "mmc60Ltm": -0.00118789,
                    "mmcLtm": -0.00111352,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.03515901,
                    "v2Corr20Ltm": 0.01327265
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.03599739,
                    "corr60Ltm": 0.02366119,
                    "corrLtm": null,
                    "date": "2024-12-13",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -3.7697e-4,
                    "mmc60": -0.01329416,
                    "mmc60Ltm": -0.00113632,
                    "mmcLtm": -0.00109477,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.04273668,
                    "v2Corr20Ltm": 0.01276366
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.03715465,
                    "corr60Ltm": 0.02357394,
                    "corrLtm": null,
                    "date": "2024-12-12",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": 0.0021225,
                    "mmc60": -0.01391176,
                    "mmc60Ltm": -0.00107717,
                    "mmcLtm": -0.00110492,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.04248233,
                    "v2Corr20Ltm": 0.01205002
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.03905834,
                    "corr60Ltm": 0.0234749,
                    "corrLtm": null,
                    "date": "2024-12-11",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00245138,
                    "mmc60": -0.01105133,
                    "mmc60Ltm": -0.0010227,
                    "mmcLtm": -0.00111723,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.05213737,
                    "v2Corr20Ltm": 0.01130777
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.03156242,
                    "corr60Ltm": 0.0234152,
                    "corrLtm": null,
                    "date": "2024-12-10",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00677959,
                    "mmc60": -0.00885801,
                    "mmc60Ltm": -9.8427e-4,
                    "mmcLtm": -0.00111212,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.03156415,
                    "v2Corr20Ltm": 0.01028703
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.02838419,
                    "corr60Ltm": 0.02325624,
                    "corrLtm": null,
                    "date": "2024-12-07",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00604648,
                    "mmc60": -0.01020107,
                    "mmc60Ltm": -9.3326e-4,
                    "mmcLtm": -0.00106089,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.02043178,
                    "v2Corr20Ltm": 0.00974146
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.027832,
                    "corr60Ltm": 0.0231479,
                    "corrLtm": null,
                    "date": "2024-12-06",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00378017,
                    "mmc60": -0.01128551,
                    "mmc60Ltm": -8.9432e-4,
                    "mmcLtm": -0.00101002,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.01888903,
                    "v2Corr20Ltm": 0.00946014
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.03010054,
                    "corr60Ltm": 0.02305558,
                    "corrLtm": null,
                    "date": "2024-12-05",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00424793,
                    "mmc60": -0.01299681,
                    "mmc60Ltm": -8.353e-4,
                    "mmcLtm": -9.7601e-4,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.00640247,
                    "v2Corr20Ltm": 0.0092053
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.01641552,
                    "corr60Ltm": 0.02293145,
                    "corrLtm": null,
                    "date": "2024-12-04",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.0065512,
                    "mmc60": -0.01434001,
                    "mmc60Ltm": -7.7546e-4,
                    "mmcLtm": -9.6352e-4,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.01186562,
                    "v2Corr20Ltm": 0.00928316
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.02206861,
                    "corr60Ltm": 0.02295642,
                    "corrLtm": null,
                    "date": "2024-12-03",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.005623,
                    "mmc60": -0.01202675,
                    "mmc60Ltm": -7.2349e-4,
                    "mmcLtm": -9.4211e-4,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.01497026,
                    "v2Corr20Ltm": 0.00920938
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.03056654,
                    "corr60Ltm": 0.02278086,
                    "corrLtm": null,
                    "date": "2024-11-30",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00436091,
                    "mmc60": -0.01134794,
                    "mmc60Ltm": -6.35e-4,
                    "mmcLtm": -8.026e-4,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.01957355,
                    "v2Corr20Ltm": 0.00903994
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.02866979,
                    "corr60Ltm": 0.02266419,
                    "corrLtm": null,
                    "date": "2024-11-29",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00444081,
                    "mmc60": -0.00818393,
                    "mmc60Ltm": -5.9169e-4,
                    "mmcLtm": -7.4975e-4,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.02650929,
                    "v2Corr20Ltm": 0.00872074
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.02078574,
                    "corr60Ltm": 0.02256712,
                    "corrLtm": null,
                    "date": "2024-11-28",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00739217,
                    "mmc60": -0.00802224,
                    "mmc60Ltm": -5.4492e-4,
                    "mmcLtm": -6.9597e-4,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.00617664,
                    "v2Corr20Ltm": 0.00816485
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.0254405,
                    "corr60Ltm": 0.02250009,
                    "corrLtm": null,
                    "date": "2024-11-27",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00594021,
                    "mmc60": -0.00881282,
                    "mmc60Ltm": -4.9597e-4,
                    "mmcLtm": -6.7041e-4,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.02110463,
                    "v2Corr20Ltm": 0.00822898
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.0226219,
                    "corr60Ltm": 0.02248882,
                    "corrLtm": null,
                    "date": "2024-11-26",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00642353,
                    "mmc60": -0.00950196,
                    "mmc60Ltm": -4.641e-4,
                    "mmcLtm": -6.5022e-4,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.01648899,
                    "v2Corr20Ltm": 0.00779979
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.01804761,
                    "corr60Ltm": 0.02231413,
                    "corrLtm": null,
                    "date": "2024-11-23",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00660335,
                    "mmc60": -0.01078348,
                    "mmc60Ltm": -4.1185e-4,
                    "mmcLtm": -5.341e-4,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.01727367,
                    "v2Corr20Ltm": 0.00750017
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.01583904,
                    "corr60Ltm": 0.02224525,
                    "corrLtm": null,
                    "date": "2024-11-22",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00729624,
                    "mmc60": -0.01090222,
                    "mmc60Ltm": -3.7069e-4,
                    "mmcLtm": -4.9005e-4,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.009029,
                    "v2Corr20Ltm": 0.00715111
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.02157184,
                    "corr60Ltm": 0.02221231,
                    "corrLtm": null,
                    "date": "2024-11-21",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00604539,
                    "mmc60": -0.00617356,
                    "mmc60Ltm": -3.3283e-4,
                    "mmcLtm": -4.3665e-4,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.01346687,
                    "v2Corr20Ltm": 0.00708156
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.01589299,
                    "corr60Ltm": 0.02212295,
                    "corrLtm": null,
                    "date": "2024-11-20",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00727486,
                    "mmc60": -0.00805175,
                    "mmc60Ltm": -2.9706e-4,
                    "mmcLtm": -4.1524e-4,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.01083836,
                    "v2Corr20Ltm": 0.00683597
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.01481537,
                    "corr60Ltm": 0.02214682,
                    "corrLtm": null,
                    "date": "2024-11-19",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00617982,
                    "mmc60": -0.00711247,
                    "mmc60Ltm": -2.6735e-4,
                    "mmcLtm": -3.8896e-4,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.00952735,
                    "v2Corr20Ltm": 0.00667588
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.01154143,
                    "corr60Ltm": 0.02207243,
                    "corrLtm": null,
                    "date": "2024-11-16",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00872917,
                    "mmc60": -0.00809306,
                    "mmc60Ltm": -2.1115e-4,
                    "mmcLtm": -3.1003e-4,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.00494581,
                    "v2Corr20Ltm": 0.00655706
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.01146841,
                    "corr60Ltm": 0.02202838,
                    "corrLtm": null,
                    "date": "2024-11-15",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00554281,
                    "mmc60": -0.00688035,
                    "mmc60Ltm": -1.8027e-4,
                    "mmcLtm": -2.5017e-4,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.02031992,
                    "v2Corr20Ltm": 0.00662712
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.01036764,
                    "corr60Ltm": 0.02198004,
                    "corrLtm": null,
                    "date": "2024-11-14",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00336559,
                    "mmc60": -0.00587762,
                    "mmc60Ltm": -1.3604e-4,
                    "mmcLtm": -2.0316e-4,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": -0.00446761,
                    "v2Corr20Ltm": 0.00600472
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.0080683,
                    "corr60Ltm": 0.02193904,
                    "corrLtm": null,
                    "date": "2024-11-13",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00774075,
                    "mmc60": -0.00253985,
                    "mmc60Ltm": -1.0211e-4,
                    "mmcLtm": -1.9109e-4,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.0016364,
                    "v2Corr20Ltm": 0.0065034
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.00474182,
                    "corr60Ltm": 0.02199218,
                    "corrLtm": null,
                    "date": "2024-11-12",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00809697,
                    "mmc60": -0.00448204,
                    "mmc60Ltm": -9.27703537e-5,
                    "mmcLtm": -1.6216e-4,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.00355724,
                    "v2Corr20Ltm": 0.00674675
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.01636348,
                    "corr60Ltm": 0.02186708,
                    "corrLtm": null,
                    "date": "2024-11-09",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00813929,
                    "mmc60": -0.007409,
                    "mmc60Ltm": -6.6357885e-5,
                    "mmcLtm": -2.3263e-4,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.00529448,
                    "v2Corr20Ltm": 0.00691462
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.02188432,
                    "corr60Ltm": 0.02178894,
                    "corrLtm": null,
                    "date": "2024-11-08",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00938333,
                    "mmc60": -0.01107742,
                    "mmc60Ltm": -3.80792433e-5,
                    "mmcLtm": -2.0857e-4,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.01509573,
                    "v2Corr20Ltm": 0.00700463
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.02684111,
                    "corr60Ltm": 0.02167223,
                    "corrLtm": null,
                    "date": "2024-11-07",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.0099591,
                    "mmc60": -0.00966992,
                    "mmc60Ltm": -1.24936499e-5,
                    "mmcLtm": -1.8937e-4,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.01357429,
                    "v2Corr20Ltm": 0.00652868
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.01780235,
                    "corr60Ltm": 0.02155342,
                    "corrLtm": null,
                    "date": "2024-11-06",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00973557,
                    "mmc60": -0.00710425,
                    "mmc60Ltm": -1.52187401e-6,
                    "mmcLtm": -1.5208e-4,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.01204521,
                    "v2Corr20Ltm": 0.00608833
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.02558558,
                    "corr60Ltm": 0.02156779,
                    "corrLtm": null,
                    "date": "2024-11-05",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00676643,
                    "mmc60": -0.00665603,
                    "mmc60Ltm": 2.56916189e-5,
                    "mmcLtm": -1.1536e-4,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.00983723,
                    "v2Corr20Ltm": 0.0056912
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.02726745,
                    "corr60Ltm": 0.02133985,
                    "corrLtm": null,
                    "date": "2024-11-02",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.01109819,
                    "mmc60": -0.00795373,
                    "mmc60Ltm": 3.00481647e-5,
                    "mmcLtm": -1.3046e-4,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.01477347,
                    "v2Corr20Ltm": 0.00539506
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.02626116,
                    "corr60Ltm": 0.02119808,
                    "corrLtm": null,
                    "date": "2024-11-01",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00963095,
                    "mmc60": -0.00919411,
                    "mmc60Ltm": 6.04058927e-5,
                    "mmcLtm": -1.0086e-4,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.01423368,
                    "v2Corr20Ltm": 0.00467364
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.02453671,
                    "corr60Ltm": 0.02109995,
                    "corrLtm": null,
                    "date": "2024-10-31",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00891168,
                    "mmc60": -0.00588815,
                    "mmc60Ltm": 8.05152765e-5,
                    "mmcLtm": -5.80840129e-5,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.02120126,
                    "v2Corr20Ltm": 0.00387697
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.01951319,
                    "corr60Ltm": 0.02101121,
                    "corrLtm": null,
                    "date": "2024-10-30",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00851084,
                    "mmc60": -0.00217522,
                    "mmc60Ltm": 8.17946532e-5,
                    "mmcLtm": -2.42916707e-5,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.02142481,
                    "v2Corr20Ltm": 0.00230204
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.0199352,
                    "corr60Ltm": 0.02101695,
                    "corrLtm": null,
                    "date": "2024-10-29",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": 7.46209477e-5,
                    "mmc60": -0.00204289,
                    "mmc60Ltm": 9.04422243e-5,
                    "mmcLtm": 8.22385679e-6,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.03030893,
                    "v2Corr20Ltm": 0.02017294
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.00720842,
                    "corr60Ltm": 0.0208933,
                    "corrLtm": null,
                    "date": "2024-10-26",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": 3.3468e-4,
                    "mmc60": -0.00341887,
                    "mmc60Ltm": 7.06076697e-5,
                    "mmcLtm": 7.16653879e-5,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.01510987,
                    "v2Corr20Ltm": 0.01998335
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.00382161,
                    "corr60Ltm": 0.0208901,
                    "corrLtm": null,
                    "date": "2024-10-25",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -1.2284e-4,
                    "mmc60": -0.00516788,
                    "mmc60Ltm": 8.3656775e-5,
                    "mmcLtm": 1.0513e-4,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.02038748,
                    "v2Corr20Ltm": 0.01996323
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.00904103,
                    "corr60Ltm": 0.02087247,
                    "corrLtm": null,
                    "date": "2024-10-24",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00233788,
                    "mmc60": -0.00153121,
                    "mmc60Ltm": 8.78432435e-5,
                    "mmcLtm": 1.497e-4,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.01289246,
                    "v2Corr20Ltm": 0.01995715
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.01816421,
                    "corr60Ltm": 0.02079983,
                    "corrLtm": null,
                    "date": "2024-10-23",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00111243,
                    "mmc60": -0.00211836,
                    "mmc60Ltm": 7.47717733e-5,
                    "mmcLtm": 1.592e-4,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.02041459,
                    "v2Corr20Ltm": 0.01998411
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.00784843,
                    "corr60Ltm": 0.02080993,
                    "corrLtm": null,
                    "date": "2024-10-22",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -5.81e-4,
                    "mmc60": -0.00307682,
                    "mmc60Ltm": 8.31745966e-5,
                    "mmcLtm": 1.6407e-4,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.02839365,
                    "v2Corr20Ltm": 0.01998246
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.00852336,
                    "corr60Ltm": 0.02070926,
                    "corrLtm": null,
                    "date": "2024-10-19",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00201238,
                    "mmc60": -0.0040721,
                    "mmc60Ltm": 1.008e-4,
                    "mmcLtm": 2.94e-4,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.03329975,
                    "v2Corr20Ltm": 0.01980942
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": -9.7149e-4,
                    "corr60Ltm": 0.02069638,
                    "corrLtm": null,
                    "date": "2024-10-18",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00300909,
                    "mmc60": -0.00713923,
                    "mmc60Ltm": 1.1635e-4,
                    "mmcLtm": 3.4373e-4,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.02923619,
                    "v2Corr20Ltm": 0.019702
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.00475159,
                    "corr60Ltm": 0.0206905,
                    "corrLtm": null,
                    "date": "2024-10-17",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00461973,
                    "mmc60": -0.00396778,
                    "mmc60Ltm": 1.3043e-4,
                    "mmcLtm": 3.7781e-4,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.04310002,
                    "v2Corr20Ltm": 0.01961659
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": -0.00257018,
                    "corr60Ltm": 0.02066662,
                    "corrLtm": null,
                    "date": "2024-10-16",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00384592,
                    "mmc60": -0.00918456,
                    "mmc60Ltm": 1.4033e-4,
                    "mmcLtm": 3.9689e-4,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.02409104,
                    "v2Corr20Ltm": 0.01952696
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.00651303,
                    "corr60Ltm": 0.02075565,
                    "corrLtm": null,
                    "date": "2024-10-15",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00259097,
                    "mmc60": -0.00700862,
                    "mmc60Ltm": 1.7606e-4,
                    "mmcLtm": 4.1314e-4,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.02252735,
                    "v2Corr20Ltm": 0.01950947
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.01724423,
                    "corr60Ltm": 0.02065913,
                    "corrLtm": null,
                    "date": "2024-10-12",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00409076,
                    "mmc60": -0.00727172,
                    "mmc60Ltm": 2.0797e-4,
                    "mmcLtm": 4.6852e-4,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.03062185,
                    "v2Corr20Ltm": 0.01925233
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.01469984,
                    "corr60Ltm": 0.02061675,
                    "corrLtm": null,
                    "date": "2024-10-11",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -9.9811e-4,
                    "mmc60": -0.00209705,
                    "mmc60Ltm": 2.3573e-4,
                    "mmcLtm": 4.9381e-4,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.0343696,
                    "v2Corr20Ltm": 0.01914003
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.01737145,
                    "corr60Ltm": 0.02060322,
                    "corrLtm": null,
                    "date": "2024-10-10",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00144984,
                    "mmc60": -3.543e-4,
                    "mmc60Ltm": 2.4504e-4,
                    "mmcLtm": 5.0291e-4,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.04021069,
                    "v2Corr20Ltm": 0.01900555
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.01884668,
                    "corr60Ltm": 0.02054367,
                    "corrLtm": null,
                    "date": "2024-10-09",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00106599,
                    "mmc60": -0.00309581,
                    "mmc60Ltm": 2.4493e-4,
                    "mmcLtm": 5.1036e-4,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.04301599,
                    "v2Corr20Ltm": 0.01892462
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.02467732,
                    "corr60Ltm": 0.02055017,
                    "corrLtm": null,
                    "date": "2024-10-08",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -3.8185e-4,
                    "mmc60": -0.00456943,
                    "mmc60Ltm": 2.5773e-4,
                    "mmcLtm": 5.164e-4,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.03737252,
                    "v2Corr20Ltm": 0.01883231
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.01976839,
                    "corr60Ltm": 0.02043851,
                    "corrLtm": null,
                    "date": "2024-10-05",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00155697,
                    "mmc60": -0.00274755,
                    "mmc60Ltm": 2.746e-4,
                    "mmcLtm": 5.0592e-4,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.05010622,
                    "v2Corr20Ltm": 0.01863901
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.02560713,
                    "corr60Ltm": 0.02038353,
                    "corrLtm": null,
                    "date": "2024-10-04",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00525923,
                    "mmc60": -0.00154229,
                    "mmc60Ltm": 2.8509e-4,
                    "mmcLtm": 5.0893e-4,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.03302544,
                    "v2Corr20Ltm": 0.01845367
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.02771186,
                    "corr60Ltm": 0.02032038,
                    "corrLtm": null,
                    "date": "2024-10-03",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00182646,
                    "mmc60": -0.00193389,
                    "mmc60Ltm": 2.88e-4,
                    "mmcLtm": 5.2233e-4,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.04438865,
                    "v2Corr20Ltm": 0.01831326
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.03145967,
                    "corr60Ltm": 0.02026301,
                    "corrLtm": null,
                    "date": "2024-10-02",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00119686,
                    "mmc60": 0.00162615,
                    "mmc60Ltm": 2.9981e-4,
                    "mmcLtm": 5.3129e-4,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.03678757,
                    "v2Corr20Ltm": 0.01821374
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.01935601,
                    "corr60Ltm": 0.02022011,
                    "corrLtm": null,
                    "date": "2024-10-01",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00483374,
                    "mmc60": 0.00103931,
                    "mmc60Ltm": 2.9473e-4,
                    "mmcLtm": 5.3791e-4,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.0286256,
                    "v2Corr20Ltm": 0.01814258
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.03022756,
                    "corr60Ltm": 0.02015618,
                    "corrLtm": null,
                    "date": "2024-09-28",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00350417,
                    "mmc60": 8.3874e-4,
                    "mmc60Ltm": 2.9648e-4,
                    "mmcLtm": 5.1219e-4,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.02212836,
                    "v2Corr20Ltm": 0.01788553
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.02646707,
                    "corr60Ltm": 0.02008019,
                    "corrLtm": null,
                    "date": "2024-09-27",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00594634,
                    "mmc60": 0.00179323,
                    "mmc60Ltm": 2.9328e-4,
                    "mmcLtm": 4.9978e-4,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.01942145,
                    "v2Corr20Ltm": 0.01774999
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.02663957,
                    "corr60Ltm": 0.01997835,
                    "corrLtm": null,
                    "date": "2024-09-26",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00535931,
                    "mmc60": 0.00190067,
                    "mmc60Ltm": 2.8838e-4,
                    "mmcLtm": 5.1588e-4,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.01162622,
                    "v2Corr20Ltm": 0.01762206
                },
                {
                    "alpha": null,
                    "alphaLtm": null,
                    "corr": null,
                    "corr60": 0.02667609,
                    "corr60Ltm": 0.01987939,
                    "corrLtm": null,
                    "date": "2024-09-25",
                    "fncV4": null,
                    "fncV4Ltm": null,
                    "mmc": -0.00561108,
                    "mmc60": 0.0046761,
                    "mmc60Ltm": 2.6413e-4,
                    "mmcLtm": 5.383e-4,
                    "mpc": null,
                    "mpcLtm": null,
                    "tc": null,
                    "tcLtm": null,
                    "v2Corr20": 0.01803802,
                    "v2Corr20Ltm": 0.01764494
                }
            ],
            "startDate": "2018-06-06T17:33:21Z",
            "team": true,
            "title": "Expert",
            "totalStake": "335.183056609585400721",
            "totalStakeTs": [
                {
                    "date": "2024-09-25",
                    "delta": "-0.090767830022449529",
                    "value": "318.521478926706421903"
                },
                {
                    "date": "2024-09-26",
                    "delta": "39.038226814462393735",
                    "value": "357.559705741168815638"
                },
                {
                    "date": "2024-09-27",
                    "delta": "-0.092312579018197905",
                    "value": "357.467393162150617733"
                },
                {
                    "date": "2024-09-28",
                    "delta": "0.169032483419370754",
                    "value": "357.636425645569988487"
                },
                {
                    "date": "2024-10-01",
                    "delta": "0.194352430868531012",
                    "value": "357.830778076438519499"
                },
                {
                    "date": "2024-10-02",
                    "delta": "0.673574215744543179",
                    "value": "358.504352292183062678"
                },
                {
                    "date": "2024-10-03",
                    "delta": "0.783718676177645879",
                    "value": "359.288070968360708557"
                },
                {
                    "date": "2024-10-04",
                    "delta": "0.261183468251997968",
                    "value": "359.549254436612706525"
                },
                {
                    "date": "2024-10-05",
                    "delta": "0.925201597373450364",
                    "value": "360.474456033986156889"
                },
                {
                    "date": "2024-10-08",
                    "delta": "0.755772843123276383",
                    "value": "361.230228877109433272"
                },
                {
                    "date": "2024-10-09",
                    "delta": "0.845154582965824178",
                    "value": "362.075383460075257450"
                },
                {
                    "date": "2024-10-10",
                    "delta": "0.742539798961436666",
                    "value": "362.817923259036694116"
                },
                {
                    "date": "2024-10-11",
                    "delta": "0.666374025581081987",
                    "value": "363.484297284617776103"
                },
                {
                    "date": "2024-10-12",
                    "delta": "0.311212299958188217",
                    "value": "363.795509584575964320"
                },
                {
                    "date": "2024-10-15",
                    "delta": "0.278867834411365419",
                    "value": "364.074377418987329739"
                },
                {
                    "date": "2024-10-16",
                    "delta": "6.304952636538880086",
                    "value": "370.379330055526209825"
                },
                {
                    "date": "2024-10-17",
                    "delta": "0.533336766255406638",
                    "value": "370.912666821781616463"
                },
                {
                    "date": "2024-10-18",
                    "delta": "0.391056088552058992",
                    "value": "371.303722910333675455"
                },
                {
                    "date": "2024-10-19",
                    "delta": "0.575884751413075269",
                    "value": "371.879607661746750724"
                },
                {
                    "date": "2024-10-22",
                    "delta": "0.643956066993117343",
                    "value": "372.523563728739868067"
                },
                {
                    "date": "2024-10-23",
                    "delta": "0.404785845724724456",
                    "value": "372.928349574464592523"
                },
                {
                    "date": "2024-10-24",
                    "delta": "0.084944701935618602",
                    "value": "373.013294276400211125"
                },
                {
                    "date": "2024-10-25",
                    "delta": "0.492211600892734734",
                    "value": "373.505505877292945859"
                },
                {
                    "date": "2024-10-26",
                    "delta": "0.410755038685884900",
                    "value": "373.916260915978830759"
                },
                {
                    "date": "2024-10-29",
                    "delta": "-309.494975646079582887",
                    "value": "64.421285269899247872"
                },
                {
                    "date": "2024-10-30",
                    "delta": "-0.057122427457512338",
                    "value": "64.364162842441735534"
                },
                {
                    "date": "2024-10-31",
                    "delta": "-0.069388227626155958",
                    "value": "64.294774614815579576"
                },
                {
                    "date": "2024-11-01",
                    "delta": "-0.114166066069130804",
                    "value": "64.180608548746448772"
                },
                {
                    "date": "2024-11-02",
                    "delta": "-0.134879495752413946",
                    "value": "64.045729052994034826"
                },
                {
                    "date": "2024-11-04",
                    "delta": "232.000000000000000000",
                    "value": "296.045729052994034826"
                },
                {
                    "date": "2024-11-05",
                    "delta": "-0.079200658799830265",
                    "value": "295.966528394194204561"
                },
                {
                    "date": "2024-11-06",
                    "delta": "-0.120069524792273138",
                    "value": "295.846458869401931423"
                },
                {
                    "date": "2024-11-07",
                    "delta": "-0.116018352444825309",
                    "value": "295.730440516957106114"
                },
                {
                    "date": "2024-11-08",
                    "delta": "-0.099601432036313238",
                    "value": "295.630839084920792876"
                },
                {
                    "date": "2024-11-09",
                    "delta": "-0.120494935333716691",
                    "value": "295.510344149587076185"
                },
                {
                    "date": "2024-11-12",
                    "delta": "-0.130472057914372443",
                    "value": "295.379872091672703742"
                },
                {
                    "date": "2024-11-13",
                    "delta": "-0.130620404894777571",
                    "value": "295.249251686777926171"
                },
                {
                    "date": "2024-11-14",
                    "delta": "-0.078457839329881523",
                    "value": "295.170793847448044648"
                },
                {
                    "date": "2024-11-15",
                    "delta": "-0.008175992542134363",
                    "value": "295.162617854905910285"
                },
                {
                    "date": "2024-11-16",
                    "delta": "-0.131884276694324512",
                    "value": "295.030733578211585773"
                },
                {
                    "date": "2024-11-19",
                    "delta": "-0.073608723011494927",
                    "value": "294.957124855200090846"
                },
                {
                    "date": "2024-11-20",
                    "delta": "-0.090966179665760239",
                    "value": "294.866158675534330607"
                },
                {
                    "date": "2024-11-21",
                    "delta": "-0.051423728395421370",
                    "value": "294.814734947138909237"
                },
                {
                    "date": "2024-11-22",
                    "delta": "-0.098266380490538479",
                    "value": "294.716468566648370758"
                },
                {
                    "date": "2024-11-23",
                    "delta": "-0.044174275896422316",
                    "value": "294.672294290751948442"
                },
                {
                    "date": "2024-11-26",
                    "delta": "-0.044305862806491514",
                    "value": "294.627988427945456928"
                },
                {
                    "date": "2024-11-27",
                    "delta": "-0.012751764026896973",
                    "value": "294.615236663918559955"
                },
                {
                    "date": "2024-11-28",
                    "delta": "-0.111439275709266713",
                    "value": "294.503797388209293242"
                },
                {
                    "date": "2024-11-29",
                    "delta": "0.041976603946342403",
                    "value": "294.545773992155635645"
                },
                {
                    "date": "2024-11-30",
                    "delta": "0.010223781506538404",
                    "value": "294.555997773662174049"
                },
                {
                    "date": "2024-12-03",
                    "delta": "-0.036465124889521706",
                    "value": "294.519532648772652343"
                },
                {
                    "date": "2024-12-04",
                    "delta": "-0.067706944660392874",
                    "value": "294.451825704112259469"
                },
                {
                    "date": "2024-12-05",
                    "delta": "-0.051182613369788172",
                    "value": "294.400643090742471297"
                },
                {
                    "date": "2024-12-06",
                    "delta": "0.086930148546004898",
                    "value": "294.487573239288476195"
                },
                {
                    "date": "2024-12-07",
                    "delta": "-0.083945713036259538",
                    "value": "294.403627526252216657"
                },
                {
                    "date": "2024-12-10",
                    "delta": "0.099236083456847058",
                    "value": "294.502863609709063715"
                },
                {
                    "date": "2024-12-11",
                    "delta": "0.959371322183573380",
                    "value": "295.462234931892637095"
                },
                {
                    "date": "2024-12-12",
                    "delta": "1.106103906297613311",
                    "value": "296.568338838190250406"
                },
                {
                    "date": "2024-12-13",
                    "delta": "0.904246338009195848",
                    "value": "297.472585176199446254"
                },
                {
                    "date": "2024-12-14",
                    "delta": "0.263432066454777253",
                    "value": "297.736017242654223507"
                },
                {
                    "date": "2024-12-17",
                    "delta": "0.157961042732426977",
                    "value": "297.893978285386650484"
                },
                {
                    "date": "2024-12-18",
                    "delta": "-0.150857605909802926",
                    "value": "297.743120679476847558"
                },
                {
                    "date": "2024-12-19",
                    "delta": "0.245432614631763754",
                    "value": "297.988553294108611312"
                },
                {
                    "date": "2024-12-20",
                    "delta": "0.216375532207893039",
                    "value": "298.204928826316504351"
                },
                {
                    "date": "2024-12-21",
                    "delta": "0.162886516910095412",
                    "value": "298.367815343226599763"
                },
                {
                    "date": "2024-12-24",
                    "delta": "0.326394493528981894",
                    "value": "298.694209836755581657"
                },
                {
                    "date": "2024-12-25",
                    "delta": "0.087308478507973440",
                    "value": "298.781518315263555097"
                },
                {
                    "date": "2024-12-26",
                    "delta": "0.051233403050087562",
                    "value": "298.832751718313642659"
                },
                {
                    "date": "2024-12-27",
                    "delta": "0.450452396247509850",
                    "value": "299.283204114561152509"
                },
                {
                    "date": "2024-12-28",
                    "delta": "0.330012970228535774",
                    "value": "299.613217084789688283"
                },
                {
                    "date": "2024-12-31",
                    "delta": "0.578674021438043244",
                    "value": "300.191891106227731527"
                },
                {
                    "date": "2025-01-01",
                    "delta": "0.700370689374334024",
                    "value": "300.892261795602065551"
                },
                {
                    "date": "2025-01-02",
                    "delta": "0.453668233945083886",
                    "value": "301.345930029547149437"
                },
                {
                    "date": "2025-01-03",
                    "delta": "0.874796457460406527",
                    "value": "302.220726487007555964"
                },
                {
                    "date": "2025-01-04",
                    "delta": "0.578235738231185722",
                    "value": "302.798962225238741686"
                },
                {
                    "date": "2025-01-07",
                    "delta": "0.628642215679595891",
                    "value": "303.427604440918337577"
                },
                {
                    "date": "2025-01-08",
                    "delta": "0.279849127854579071",
                    "value": "303.707453568772916648"
                },
                {
                    "date": "2025-01-09",
                    "delta": "-0.324464594112528363",
                    "value": "303.382988974660388285"
                },
                {
                    "date": "2025-01-10",
                    "delta": "-0.633903930890539699",
                    "value": "302.749085043769848586"
                },
                {
                    "date": "2025-01-11",
                    "delta": "-0.549790692762046227",
                    "value": "302.199294351007802359"
                },
                {
                    "date": "2025-01-14",
                    "delta": "-0.491215706949410917",
                    "value": "301.708078644058391442"
                },
                {
                    "date": "2025-01-15",
                    "delta": "-0.112928666396307442",
                    "value": "301.595149977662084000"
                },
                {
                    "date": "2025-01-16",
                    "delta": "0.143716473683463220",
                    "value": "301.738866451345547220"
                },
                {
                    "date": "2025-01-17",
                    "delta": "0.684096123850771907",
                    "value": "302.422962575196319127"
                },
                {
                    "date": "2025-01-18",
                    "delta": "0.161660044066929738",
                    "value": "302.584622619263248865"
                },
                {
                    "date": "2025-01-21",
                    "delta": "0.593720534744384879",
                    "value": "303.178343154007633744"
                },
                {
                    "date": "2025-01-22",
                    "delta": "0.629431996362124344",
                    "value": "303.807775150369758088"
                },
                {
                    "date": "2025-01-23",
                    "delta": "0.518151507744252477",
                    "value": "304.325926658114010565"
                },
                {
                    "date": "2025-01-24",
                    "delta": "0.347587356085934078",
                    "value": "304.673514014199944643"
                },
                {
                    "date": "2025-01-25",
                    "delta": "0.239575347397273961",
                    "value": "304.913089361597218604"
                },
                {
                    "date": "2025-01-28",
                    "delta": "-0.168879924664598553",
                    "value": "304.744209436932620051"
                },
                {
                    "date": "2025-01-29",
                    "delta": "0.287732268205326845",
                    "value": "305.031941705137946896"
                },
                {
                    "date": "2025-01-30",
                    "delta": "0.891941389875224216",
                    "value": "305.923883095013171112"
                },
                {
                    "date": "2025-01-31",
                    "delta": "0.789132467547343973",
                    "value": "306.713015562560515085"
                },
                {
                    "date": "2025-02-01",
                    "delta": "0.595066519094018329",
                    "value": "307.308082081654533414"
                },
                {
                    "date": "2025-02-04",
                    "delta": "0.680576191274926891",
                    "value": "307.988658272929460305"
                },
                {
                    "date": "2025-02-05",
                    "delta": "-0.099155808826645391",
                    "value": "307.889502464102814914"
                },
                {
                    "date": "2025-02-06",
                    "delta": "0.372790431153917273",
                    "value": "308.262292895256732187"
                },
                {
                    "date": "2025-02-07",
                    "delta": "0.572386633599503798",
                    "value": "308.834679528856235985"
                },
                {
                    "date": "2025-02-08",
                    "delta": "0.240563306950236256",
                    "value": "309.075242835806472241"
                },
                {
                    "date": "2025-02-11",
                    "delta": "0.183853138784542480",
                    "value": "309.259095974591014721"
                },
                {
                    "date": "2025-02-12",
                    "delta": "0.071614305325860954",
                    "value": "309.330710279916875675"
                },
                {
                    "date": "2025-02-13",
                    "delta": "-0.364551997585274589",
                    "value": "308.966158282331601086"
                },
                {
                    "date": "2025-02-14",
                    "delta": "-0.464201019641396801",
                    "value": "308.501957262690204285"
                },
                {
                    "date": "2025-02-15",
                    "delta": "-0.140880248134711750",
                    "value": "308.361077014555492535"
                },
                {
                    "date": "2025-02-18",
                    "delta": "-0.175601392805314687",
                    "value": "308.185475621750177848"
                },
                {
                    "date": "2025-02-19",
                    "delta": "-0.817531242469068413",
                    "value": "307.367944379281109435"
                },
                {
                    "date": "2025-02-20",
                    "delta": "-0.225836581889159824",
                    "value": "307.142107797391949611"
                },
                {
                    "date": "2025-02-21",
                    "delta": "-0.607044702788028844",
                    "value": "306.535063094603920767"
                },
                {
                    "date": "2025-02-22",
                    "delta": "-0.071505730128733925",
                    "value": "306.463557364475186842"
                },
                {
                    "date": "2025-02-25",
                    "delta": "0.690462119862697026",
                    "value": "307.154019484337883868"
                },
                {
                    "date": "2025-02-26",
                    "delta": "0.447691723479493428",
                    "value": "307.601711207817377296"
                },
                {
                    "date": "2025-02-27",
                    "delta": "0.387371596632988615",
                    "value": "307.989082804450365911"
                },
                {
                    "date": "2025-02-28",
                    "delta": "0.776552246225836390",
                    "value": "308.765635050676202301"
                },
                {
                    "date": "2025-03-01",
                    "delta": "0.118858225520236064",
                    "value": "308.884493276196438365"
                },
                {
                    "date": "2025-03-04",
                    "delta": "0.426402035873600397",
                    "value": "309.310895312070038762"
                },
                {
                    "date": "2025-03-05",
                    "delta": "0.428491005306671394",
                    "value": "309.739386317376710156"
                },
                {
                    "date": "2025-03-06",
                    "delta": "0.030783111209227228",
                    "value": "309.770169428585937384"
                },
                {
                    "date": "2025-03-07",
                    "delta": "0.425608258471048300",
                    "value": "310.195777687056985684"
                },
                {
                    "date": "2025-03-08",
                    "delta": "0.818543513479825442",
                    "value": "311.014321200536811126"
                },
                {
                    "date": "2025-03-11",
                    "delta": "0.333881003571158557",
                    "value": "311.348202204107969683"
                },
                {
                    "date": "2025-03-12",
                    "delta": "0.849104366737276328",
                    "value": "312.197306570845246011"
                },
                {
                    "date": "2025-03-13",
                    "delta": "0.747703086489006741",
                    "value": "312.945009657334252752"
                },
                {
                    "date": "2025-03-14",
                    "delta": "0.440263406886339602",
                    "value": "313.385273064220592354"
                },
                {
                    "date": "2025-03-15",
                    "delta": "0.885842027616689415",
                    "value": "314.271115091837281769"
                },
                {
                    "date": "2025-03-18",
                    "delta": "0.744571118219374749",
                    "value": "315.015686210056656518"
                },
                {
                    "date": "2025-03-19",
                    "delta": "0.321542990252304899",
                    "value": "315.337229200308961417"
                },
                {
                    "date": "2025-03-20",
                    "delta": "1.079339923967964053",
                    "value": "316.416569124276925470"
                },
                {
                    "date": "2025-03-21",
                    "delta": "0.158482965618715348",
                    "value": "316.575052089895640818"
                },
                {
                    "date": "2025-03-22",
                    "delta": "0.429498220674115966",
                    "value": "317.004550310569756784"
                },
                {
                    "date": "2025-03-25",
                    "delta": "-0.284433205055601601",
                    "value": "316.720117105514155183"
                },
                {
                    "date": "2025-03-26",
                    "delta": "0.143677700194531863",
                    "value": "316.863794805708687046"
                },
                {
                    "date": "2025-03-27",
                    "delta": "-0.154181838304141577",
                    "value": "316.709612967404545469"
                },
                {
                    "date": "2025-03-28",
                    "delta": "-0.429965362489608683",
                    "value": "316.279647604914936786"
                },
                {
                    "date": "2025-03-29",
                    "delta": "-0.341811816367961340",
                    "value": "315.937835788546975446"
                },
                {
                    "date": "2025-04-01",
                    "delta": "-0.021801463289057001",
                    "value": "315.916034325257918445"
                },
                {
                    "date": "2025-04-02",
                    "delta": "-0.151640445314250572",
                    "value": "315.764393879943667873"
                },
                {
                    "date": "2025-04-03",
                    "delta": "0.076835719946717686",
                    "value": "315.841229599890385559"
                },
                {
                    "date": "2025-04-04",
                    "delta": "0.186613316543404577",
                    "value": "316.027842916433790136"
                },
                {
                    "date": "2025-04-05",
                    "delta": "-0.423196644824365028",
                    "value": "315.604646271609425108"
                },
                {
                    "date": "2025-04-08",
                    "delta": "0.322257677324690904",
                    "value": "315.926903948934116012"
                },
                {
                    "date": "2025-04-09",
                    "delta": "0.105256200968328265",
                    "value": "316.032160149902444277"
                },
                {
                    "date": "2025-04-10",
                    "delta": "0.137007763595206395",
                    "value": "316.169167913497650672"
                },
                {
                    "date": "2025-04-11",
                    "delta": "0.660467298952718338",
                    "value": "316.829635212450369010"
                },
                {
                    "date": "2025-04-12",
                    "delta": "0.306744842667123895",
                    "value": "317.136380055117492905"
                },
                {
                    "date": "2025-04-15",
                    "delta": "0.600384785952945634",
                    "value": "317.736764841070438539"
                },
                {
                    "date": "2025-04-16",
                    "delta": "0.715711022684127171",
                    "value": "318.452475863754565710"
                },
                {
                    "date": "2025-04-17",
                    "delta": "0.469570715437897541",
                    "value": "318.922046579192463251"
                },
                {
                    "date": "2025-04-18",
                    "delta": "0.333925205222046214",
                    "value": "319.255971784414509465"
                },
                {
                    "date": "2025-04-19",
                    "delta": "0.157614495904489789",
                    "value": "319.413586280318999254"
                },
                {
                    "date": "2025-04-22",
                    "delta": "-0.205590210915080460",
                    "value": "319.207996069403918794"
                },
                {
                    "date": "2025-04-23",
                    "delta": "0.116023821596074885",
                    "value": "319.324019890999993679"
                },
                {
                    "date": "2025-04-24",
                    "delta": "-0.084232088772718358",
                    "value": "319.239787802227275321"
                },
                {
                    "date": "2025-04-25",
                    "delta": "-0.120114531963031163",
                    "value": "319.119673270264244158"
                },
                {
                    "date": "2025-04-26",
                    "delta": "0.420849431757873743",
                    "value": "319.540522702022117901"
                },
                {
                    "date": "2025-04-29",
                    "delta": "0.540499329999541542",
                    "value": "320.081022032021659443"
                },
                {
                    "date": "2025-04-30",
                    "delta": "0.683543732792566525",
                    "value": "320.764565764814225968"
                },
                {
                    "date": "2025-05-01",
                    "delta": "0.556863802176723625",
                    "value": "321.321429566990949593"
                },
                {
                    "date": "2025-05-02",
                    "delta": "0.484281630752871217",
                    "value": "321.805711197743820810"
                },
                {
                    "date": "2025-05-03",
                    "delta": "0.922769960829112434",
                    "value": "322.728481158572933244"
                },
                {
                    "date": "2025-05-06",
                    "delta": "0.444714047515562729",
                    "value": "323.173195206088495973"
                },
                {
                    "date": "2025-05-07",
                    "delta": "0.749381453085251553",
                    "value": "323.922576659173747526"
                },
                {
                    "date": "2025-05-08",
                    "delta": "0.680467010115372181",
                    "value": "324.603043669289119707"
                },
                {
                    "date": "2025-05-09",
                    "delta": "0.065805595035307296",
                    "value": "324.668849264324427003"
                },
                {
                    "date": "2025-05-10",
                    "delta": "0.599446071698984343",
                    "value": "325.268295336023411346"
                },
                {
                    "date": "2025-05-13",
                    "delta": "0.916557406649103612",
                    "value": "326.184852742672514958"
                },
                {
                    "date": "2025-05-14",
                    "delta": "1.354323878099363353",
                    "value": "327.539176620771878311"
                },
                {
                    "date": "2025-05-15",
                    "delta": "1.198331819561382014",
                    "value": "328.737508440333260325"
                },
                {
                    "date": "2025-05-16",
                    "delta": "1.338701843387595757",
                    "value": "330.076210283720856082"
                },
                {
                    "date": "2025-05-17",
                    "delta": "1.288407682665587949",
                    "value": "331.364617966386444031"
                },
                {
                    "date": "2025-05-20",
                    "delta": "1.267213518780770488",
                    "value": "332.631831485167214519"
                },
                {
                    "date": "2025-05-21",
                    "delta": "1.536929903083045134",
                    "value": "334.168761388250259653"
                },
                {
                    "date": "2025-05-22",
                    "delta": "1.294541758430649943",
                    "value": "335.463303146680909596"
                },
                {
                    "date": "2025-05-23",
                    "delta": "1.368311430551238823",
                    "value": "336.831614577232148419"
                },
                {
                    "date": "2025-05-24",
                    "delta": "0.599585324757743604",
                    "value": "337.431199901989892023"
                },
                {
                    "date": "2025-05-27",
                    "delta": "1.012427803808597132",
                    "value": "338.443627705798489155"
                },
                {
                    "date": "2025-05-28",
                    "delta": "0.741441149138157635",
                    "value": "339.185068854936646790"
                },
                {
                    "date": "2025-05-29",
                    "delta": "0.758578816466694932",
                    "value": "339.943647671403341722"
                },
                {
                    "date": "2025-05-30",
                    "delta": "0.842128589140438993",
                    "value": "340.785776260543780715"
                },
                {
                    "date": "2025-05-31",
                    "delta": "0.963881466674261092",
                    "value": "341.749657727218041807"
                },
                {
                    "date": "2025-06-03",
                    "delta": "0.579712138405594350",
                    "value": "342.329369865623636157"
                },
                {
                    "date": "2025-06-04",
                    "delta": "0.114360603229984960",
                    "value": "342.443730468853621117"
                },
                {
                    "date": "2025-06-05",
                    "delta": "0.575841025732792094",
                    "value": "343.019571494586413211"
                },
                {
                    "date": "2025-06-06",
                    "delta": "0.070731854733988154",
                    "value": "343.090303349320401365"
                },
                {
                    "date": "2025-06-07",
                    "delta": "0.272644468846158465",
                    "value": "343.362947818166559830"
                },
                {
                    "date": "2025-06-10",
                    "delta": "0.313371510840388692",
                    "value": "343.676319329006948522"
                },
                {
                    "date": "2025-06-11",
                    "delta": "-0.727827937836271950",
                    "value": "342.948491391170676572"
                },
                {
                    "date": "2025-06-12",
                    "delta": "-0.412252994836118349",
                    "value": "342.536238396334558223"
                },
                {
                    "date": "2025-06-13",
                    "delta": "-0.262370355801064465",
                    "value": "342.273868040533493758"
                },
                {
                    "date": "2025-06-14",
                    "delta": "0.071126439302743320",
                    "value": "342.344994479836237078"
                },
                {
                    "date": "2025-06-17",
                    "delta": "-0.434279784422428317",
                    "value": "341.910714695413808761"
                },
                {
                    "date": "2025-06-18",
                    "delta": "-0.439182401682008843",
                    "value": "341.471532293731799918"
                },
                {
                    "date": "2025-06-19",
                    "delta": "-0.297099057090700893",
                    "value": "341.174433236641099025"
                },
                {
                    "date": "2025-06-20",
                    "delta": "-0.470577801404067039",
                    "value": "340.703855435237031986"
                },
                {
                    "date": "2025-06-21",
                    "delta": "-0.899081868081612866",
                    "value": "339.804773567155419120"
                },
                {
                    "date": "2025-06-24",
                    "delta": "-0.609424163559281862",
                    "value": "339.195349403596137258"
                },
                {
                    "date": "2025-06-25",
                    "delta": "-0.138403986908885119",
                    "value": "339.056945416687252139"
                },
                {
                    "date": "2025-06-26",
                    "delta": "-0.151279137910713602",
                    "value": "338.905666278776538537"
                },
                {
                    "date": "2025-06-27",
                    "delta": "-0.447827749335243996",
                    "value": "338.457838529441294541"
                },
                {
                    "date": "2025-06-28",
                    "delta": "-0.283672513484867897",
                    "value": "338.174166015956426644"
                },
                {
                    "date": "2025-07-01",
                    "delta": "-0.361074617043840619",
                    "value": "337.813091398912586025"
                },
                {
                    "date": "2025-07-02",
                    "delta": "-0.011821555899249238",
                    "value": "337.801269843013336787"
                },
                {
                    "date": "2025-07-03",
                    "delta": "-0.079986894583031298",
                    "value": "337.721282948430305489"
                },
                {
                    "date": "2025-07-04",
                    "delta": "0.227299696379432885",
                    "value": "337.948582644809738374"
                },
                {
                    "date": "2025-07-05",
                    "delta": "-0.085399269413875083",
                    "value": "337.863183375395863291"
                },
                {
                    "date": "2025-07-08",
                    "delta": "-0.322154256229676043",
                    "value": "337.541029119166187248"
                },
                {
                    "date": "2025-07-09",
                    "delta": "-0.242368296353832401",
                    "value": "337.298660822812354847"
                },
                {
                    "date": "2025-07-10",
                    "delta": "-0.191480656830026778",
                    "value": "337.107180165982328069"
                },
                {
                    "date": "2025-07-11",
                    "delta": "-0.470166342657929586",
                    "value": "336.637013823324398483"
                },
                {
                    "date": "2025-07-12",
                    "delta": "-0.654663323438890088",
                    "value": "335.982350499885508395"
                },
                {
                    "date": "2025-07-15",
                    "delta": "-0.345936286955398100",
                    "value": "335.636414212930110295"
                },
                {
                    "date": "2025-07-16",
                    "delta": "-0.289635086471365575",
                    "value": "335.346779126458744720"
                },
                {
                    "date": "2025-07-17",
                    "delta": "-0.274179740987266061",
                    "value": "335.072599385471478659"
                },
                {
                    "date": "2025-07-18",
                    "delta": "-0.472170506526998719",
                    "value": "334.600428878944479940"
                },
                {
                    "date": "2025-07-19",
                    "delta": "-0.036246640455971668",
                    "value": "334.564182238488508272"
                },
                {
                    "date": "2025-07-22",
                    "delta": "-0.128549261909901537",
                    "value": "334.435632976578606735"
                },
                {
                    "date": "2025-07-23",
                    "delta": "-0.369907066578243671",
                    "value": "334.065725910000363064"
                },
                {
                    "date": "2025-07-24",
                    "delta": "-0.330451814379306408",
                    "value": "333.735274095621056656"
                },
                {
                    "date": "2025-07-25",
                    "delta": "0.022122777344106530",
                    "value": "333.757396872965163186"
                },
                {
                    "date": "2025-07-26",
                    "delta": "-0.375168088711101374",
                    "value": "333.382228784254061812"
                },
                {
                    "date": "2025-07-29",
                    "delta": "-0.531806506614608091",
                    "value": "332.850422277639453721"
                },
                {
                    "date": "2025-07-30",
                    "delta": "-0.297465487809568016",
                    "value": "332.552956789829885705"
                },
                {
                    "date": "2025-07-31",
                    "delta": "0.240657780015133950",
                    "value": "332.793614569845019655"
                },
                {
                    "date": "2025-08-01",
                    "delta": "-0.153719333322597702",
                    "value": "332.639895236522421953"
                },
                {
                    "date": "2025-08-02",
                    "delta": "0.222980881515713281",
                    "value": "332.862876118038135234"
                },
                {
                    "date": "2025-08-05",
                    "delta": "0.267292815027219423",
                    "value": "333.130168933065354657"
                },
                {
                    "date": "2025-08-06",
                    "delta": "0.620039388995715720",
                    "value": "333.750208322061070377"
                },
                {
                    "date": "2025-08-07",
                    "delta": "0.546191969384899290",
                    "value": "334.296400291445969667"
                },
                {
                    "date": "2025-08-08",
                    "delta": "0.330739202701255345",
                    "value": "334.627139494147225012"
                },
                {
                    "date": "2025-08-09",
                    "delta": "0.026577266360385805",
                    "value": "334.653716760507610817"
                },
                {
                    "date": "2025-08-12",
                    "delta": "0.263525734394432802",
                    "value": "334.917242494902043619"
                },
                {
                    "date": "2025-08-13",
                    "delta": "0.193136584387595307",
                    "value": "335.110379079289638926"
                },
                {
                    "date": "2025-08-14",
                    "delta": "0.106369824596398124",
                    "value": "335.216748903886037050"
                },
                {
                    "date": "2025-08-15",
                    "delta": "0.057897620819272120",
                    "value": "335.274646524705309170"
                },
                {
                    "date": "2025-08-16",
                    "delta": "0.099043345202115552",
                    "value": "335.373689869907424722"
                },
                {
                    "date": "2025-08-19",
                    "delta": "0.060571307300518984",
                    "value": "335.434261177207943706"
                },
                {
                    "date": "2025-08-20",
                    "delta": "-0.342060164031955237",
                    "value": "335.092201013175988469"
                },
                {
                    "date": "2025-08-21",
                    "delta": "0.305623575142495354",
                    "value": "335.397824588318483823"
                },
                {
                    "date": "2025-08-22",
                    "delta": "0.165735187874298131",
                    "value": "335.563559776192781954"
                },
                {
                    "date": "2025-08-23",
                    "delta": "-0.080455609423438123",
                    "value": "335.483104166769343831"
                },
                {
                    "date": "2025-08-26",
                    "delta": "0.156452587392251075",
                    "value": "335.639556754161594906"
                },
                {
                    "date": "2025-08-27",
                    "delta": "-0.100470461718294017",
                    "value": "335.539086292443300889"
                },
                {
                    "date": "2025-08-28",
                    "delta": "-0.125353274484699427",
                    "value": "335.413733017958601462"
                },
                {
                    "date": "2025-08-29",
                    "delta": "-0.026860934012222399",
                    "value": "335.386872083946379063"
                },
                {
                    "date": "2025-08-30",
                    "delta": "-0.378897178815932223",
                    "value": "335.007974905130446840"
                },
                {
                    "date": "2025-09-02",
                    "delta": "0.094586098495925923",
                    "value": "335.102561003626372763"
                },
                {
                    "date": "2025-09-03",
                    "delta": "0.214353379037515444",
                    "value": "335.316914382663888207"
                },
                {
                    "date": "2025-09-04",
                    "delta": "-0.296550140193360645",
                    "value": "335.020364242470527562"
                },
                {
                    "date": "2025-09-05",
                    "delta": "-0.465077256931782955",
                    "value": "334.555286985538744607"
                },
                {
                    "date": "2025-09-06",
                    "delta": "-0.376725342466904729",
                    "value": "334.178561643071839878"
                },
                {
                    "date": "2025-09-09",
                    "delta": "-0.341411262996596325",
                    "value": "333.837150380075243553"
                },
                {
                    "date": "2025-09-10",
                    "delta": "-0.071315989111331964",
                    "value": "333.765834390963911589"
                },
                {
                    "date": "2025-09-11",
                    "delta": "0.130718691093363306",
                    "value": "333.896553082057274895"
                },
                {
                    "date": "2025-09-12",
                    "delta": "0.238239010837853735",
                    "value": "334.134792092895128630"
                },
                {
                    "date": "2025-09-13",
                    "delta": "0.422880791008829597",
                    "value": "334.557672883903958227"
                },
                {
                    "date": "2025-09-16",
                    "delta": "0.141272823691343390",
                    "value": "334.698945707595301617"
                },
                {
                    "date": "2025-09-17",
                    "delta": "0.246580028112029751",
                    "value": "334.945525735707331368"
                },
                {
                    "date": "2025-09-18",
                    "delta": "0.387218562764989585",
                    "value": "335.332744298472320953"
                },
                {
                    "date": "2025-09-19",
                    "delta": "0.092229626844893953",
                    "value": "335.424973925317214906"
                },
                {
                    "date": "2025-09-20",
                    "delta": "-0.204009057038170359",
                    "value": "335.220964868279044547"
                },
                {
                    "date": "2025-09-23",
                    "delta": "-0.037908258693643826",
                    "value": "335.183056609585400721"
                }
            ],
            "tournament": 8,
            "twitter": "numerai",
            "username": "benchmark_models",
            "website": null
        }
    }
}

