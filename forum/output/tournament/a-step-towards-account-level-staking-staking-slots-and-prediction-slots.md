---
title: "A Step Towards Account Level Staking: Staking Slots and Prediction Slots"
category: Tournament
url: https://forum.numer.ai/t/a-step-towards-account-level-staking-staking-slots-and-prediction-slots/6211
created_at: 2023-03-07T17:14:07.148000+00:00
last_posted_at: 2023-03-07T17:14:07.250000+00:00
posts_count: 1
views: 549
tags: []
---

# A Step Towards Account Level Staking: Staking Slots and Prediction Slots

---

### Post #1 — **gbrecht** | 2023-03-07 17:14 UTC

## Idea & Definition

Model slots are split in two kinds: Staking Slots and Prediction Slots.  
**Prediction Slots** cannot be staked on. Users can upload predictions to prediction slots. Metrics will be calculated for predictions slots.  
**Staking Slots** can be staked on. Staking slots cannot receive predictions. A Staking slot can be linked to a prediction slot. The staking slot will use the predictions from the linked prediction slot. Metrics will be calculated for staking slots

## Cons

**Increased Complexity** \- It is another concept that needs to be understood, explained etc.  
**UI Effort** \- The UI needs to incorporate a way to set the slot type and link prediction slots to stake slots.  
No complete fix for stake management, the problem of a stake being locked up until round resultion still persists.

## Benefits

**Fast prediction switching** between models. Users can already achieve this by implementing basically the same thing. A user does not need to wait to stake on different predictions, just use the UI to switch to a different prediction slot  
**Relaxing computation schedule** as the predictions of the prediction slots are not relevant to the trading pipeline, those metrics can be calculated off the critical path  
**More features** can be realized on the numerai side and be made available to the users per staking slot: Ensembling of multiple prediction slots, post prediction neutralization  
**Gather more data** As now there is no need to switch models of prediction nodes any more, numerai and users can gather data on prediction node performance and also on staking node links
