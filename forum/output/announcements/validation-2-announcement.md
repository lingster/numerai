---
title: "Validation 2 Announcement"
category: Announcements
url: https://forum.numer.ai/t/validation-2-announcement/166
created_at: 2020-04-14T23:04:31.110000+00:00
last_posted_at: 2020-04-14T23:04:31.190000+00:00
posts_count: 1
views: 4819
tags: []
---

# Validation 2 Announcement

---

### Post #1 — **master_key** | 2020-04-14 23:04 UTC

# Validation 2

[**New Tournament Data File**](<https://drive.google.com/file/d/1Wkp8hidVNn2nF0Xe-RaFShi_PgjdIQVd/view?usp=sharing>)

[**Compressed Download**](<https://drive.google.com/file/d/1vApYt6rqFg4gGRhMYWtdLHW6M-NfsACz/view?usp=sharing>)

[**Example Predictions**](<https://drive.google.com/file/d/1ZHy_FkA27vm51Kt6Rz9uFHNOTyrVehMm/view?usp=sharing>)

This is a file that shows what the tournament file would look like for the most recent round (207).  
Feel free to download and double-check that it doesn’t affect your pipeline.

## Summary

We will be giving out 10 additional eras of validation data (features + targets).

[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/0ce37d35c2282775af4e99ed6ef6f626eec09a0a_2_624x445.png)1386×990 19.4 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/0ce37d35c2282775af4e99ed6ef6f626eec09a0a.png>)

## Objective

The current validation data is known to be “easy”. Models trained on the training data tend to perform very well on the validation data - often unrealistically so. An important part of developing a model for a stock prediction problem is understanding how your model will perform out of sample.

By providing users with an extra year of validation data, we enable users to test their theories and models on a very different regime than any data they’ve seen so far. We want this to give users a better understanding of the problem by seeing how their models perform well into the future, leading to better model selection and creation.

(and yes, you can train on it if you want)

## Notes

  * These validation eras will be replacing the most recent few test eras. This is the time period since round 168.
  * The data_type label is still “validation”
  * The validation data is monthly, like the training data, while test data remains weekly.
  * Test data will continue to grow weekly, and will be placed after the new validaton segment, indicating ordering.
  * You will notice that the era numbers themselves are now out of order - this is because the validation era numbers indicate months, while test era numbers indicate weeks. So weekly eras 854-899 are now replaced by monthly eras 197-206
  * Since this data is years removed from the training data, it is well-suited as a hold-out set to verify your model’s performance.
  * We have posted a file containing the new test data at the top of this post.



## Rollout

We are designing this rollout to minimize impact to user pipelines.

Still, we’d like to give lots of time for users to double check their pipelines with any change to the data file, and provide feedback if it breaks pipelines in ways that we didn’t expect

April 17 - File released as a separate download

May 2 - Rolled into the Tournament Data
