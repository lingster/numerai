---
title: "Using the SWMM for MMC"
category: Announcements
url: https://forum.numer.ai/t/using-the-swmm-for-mmc/7931
created_at: 2025-02-04T19:11:11.519000+00:00
last_posted_at: 2025-02-04T19:11:11.594000+00:00
posts_count: 1
views: 812
tags: []
---

# Using the SWMM for MMC

---

### Post #1 — **ark** | 2025-02-04 19:11 UTC

Currently, Signals and Crypto use their Naive-Weighted Meta Models (NWMM) to calculate MMC. We know that this is incorrect because the Stake-Weighted Meta Model (SWMM) fundamentally outperforms the Naive-Weighted variant on CORR. This is true of all tournaments we host. Thus, we must ensure that all tournaments are paying for contribution to the Stake-Weighted Meta Model.

For rounds starting on or after Feb. 18, 2025, payouts will begin paying on MMC with respect to the SWMM for both Signals and Crypto.

Here is what that change looks like for Signals and Crypto in terms of average MMC per round, as you can see the cumulative expected value of MMC for Signals is slightly lower while the cumulative expected value of MMC in Crypto is slightly higher:

[![Screenshot 2025-02-04 at 11.09.27](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/8/8939826d8a1650186e58b942072c1fa5dc69d1fc_2_273x250.jpeg)Screenshot 2025-02-04 at 11.09.271078×986 73 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/8/8939826d8a1650186e58b942072c1fa5dc69d1fc.jpeg> "Screenshot 2025-02-04 at 11.09.27")

[![Screenshot 2025-02-04 at 11.09.32](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/2/2bb9eed78d6aa0fc98f5aad78d7600905763fd7f_2_271x250.jpeg)Screenshot 2025-02-04 at 11.09.321082×996 78.6 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/2/2bb9eed78d6aa0fc98f5aad78d7600905763fd7f.jpeg> "Screenshot 2025-02-04 at 11.09.32")

Correlation between the 2 scores is high across both tournaments over 2024, so most data scientists should not see any significant change in payouts going forward:

[![Screenshot 2025-02-04 at 11.05.29](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/8/88bb8494110f8116b229d9f91eb656360258d688_2_256x250.png)Screenshot 2025-02-04 at 11.05.291102×1072 72.9 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/8/88bb8494110f8116b229d9f91eb656360258d688.png> "Screenshot 2025-02-04 at 11.05.29")

[![Screenshot 2025-02-04 at 11.05.35](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/4/4fdeef72dc11d1d6036ad2e6756ca492fc727fa4_2_258x250.png)Screenshot 2025-02-04 at 11.05.351092×1058 70.9 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/4/4fdeef72dc11d1d6036ad2e6756ca492fc727fa4.png> "Screenshot 2025-02-04 at 11.05.35")
