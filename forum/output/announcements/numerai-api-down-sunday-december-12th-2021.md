---
title: "Numerai API down Sunday December 12th, 2021"
category: Announcements
url: https://forum.numer.ai/t/numerai-api-down-sunday-december-12th-2021/4613
created_at: 2021-12-12T15:32:05.200000+00:00
last_posted_at: 2021-12-12T15:32:05.334000+00:00
posts_count: 1
views: 919
tags: []
---

# Numerai API down Sunday December 12th, 2021

---

### Post #1 — **zizek** | 2021-12-12 15:32 UTC

**Numerai’s backend API server was down from 11:38 - 14:12 UTC on Sunday December 12th, 2021.**

During this time, all backend features such as _login_ , _signup_ , _data download_ , _diagnostics_ , _submissions_ , _staking_ , and _withdrawals_ were unavailable.  
Our websites [api-tournament.numer.ai](<https://api-tournament.numer.ai>), <https://numer.ai>, <https://signals.numer.ai> and <https://numerai.fund> were also partially degraded due to the inability to load data from the API.

The root cause of this outage was due to an expired SSL certificate of the API server which blocked all incoming web traffic. A new certificate was issued and the API is now available again. There are no security concerns.

We have put measures in place to prevent this from happening again, and we sincerely apologize for any inconvenience caused.

What to do if you are an active tournament participant:

  * If you have successfully uploaded your submissions for this round, there is nothing you need to do.
  * If you received an error uploading your submissions, please try again now. 
  * If your Numerai Compute instance received an error uploading your submissions, please re-trigger your instance manually. 


For further technical support, please reach out at the [#support channel](<https://community.numer.ai/channel/support>), or at [support@numer.ai](<mailto:support@numer.ai>).
