---
title: "Signals V2 “Cosmic” Data"
category: Announcements
url: https://forum.numer.ai/t/signals-v2-cosmic-data/7866
created_at: 2024-11-27T19:02:12.624000+00:00
last_posted_at: 2024-12-08T10:48:06.261000+00:00
posts_count: 5
views: 1811
tags: []
---

# Signals V2 “Cosmic” Data

---

### Post #1 — **ark** | 2024-11-27 19:02 UTC

The Signals V2 “Cosmic” dataset is officially released. Download it [here](<http://signals.numer.ai/data>).

[![cosmic_art](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/3/38f52531475822a1b382f7565dc90f798702ac91_2_500x500.jpeg)cosmic_art1600×1600 509 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/3/38f52531475822a1b382f7565dc90f798702ac91.jpeg> "cosmic_art")

Similar to the [V5 Atlas](<http://forum.numer.ai/t/v5-atlas-data-release/7576>) dataset for the Numerai tournament, the Cosmic release focuses on universe expansion - including even more stocks than the Atlas dataset. We also substantially improved our numerai_ticker and the country feature column.

In the Atlas forum post, we showed v5 models perform much better than v4 models solely due to the larger universe. The case is similar for Signals V2 data. Here are the diagnostics for V1 example validation predictions scored against the V1 dataset:

[![v1_diagnostics](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/9/96cca2bc9e69b45331fcbd66b7f20e915d08d7f6_2_504x500.png)v1_diagnostics1494×1482 181 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/9/96cca2bc9e69b45331fcbd66b7f20e915d08d7f6.png> "v1_diagnostics")

And here are the diagnostics for V2 example predictions scored against the V2 dataset:

[![v2_diagnostics](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/5/5d41d1a8281ec857e65a82a183d8b0623de31729_2_502x499.png)v2_diagnostics1494×1486 182 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/5/5d41d1a8281ec857e65a82a183d8b0623de31729.png> "v2_diagnostics")

You can see that there is an increase in the mean and Sharpe for 3 of the primary metrics. No change to the model or training parameters, just a larger universe. Note: while churn of our example model does increase, we believe this is negligible and we know that churn is relatively easy to control.

Below, you can see that the ticker universe has greatly expanded from around 5000 stocks in recent years to well over 6000. This is at least a 20% increase for all eras in the last decade:

[![cosmic_universe](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/2/26bec36596b7a9de03cc3272ef55663b1ff9d473_2_690x409.png)cosmic_universe984×584 68.7 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/2/26bec36596b7a9de03cc3272ef55663b1ff9d473.png> "cosmic_universe")

We’ve added several new countries to the dataset including Chile, China, Colombia, Egypt, India, Morocco, Peru, Qatar, Russia, and UAE. We also fixed several consistency issues with our ticker and country columns. Countries now have consistent codes throughout the entire dataset, and notations such as shareclass are either made consistent or removed altogether if unnecessary.

Signals V2 data will be used for Signals submissions starting Dec 3, 2024. Our records indicate this would not significantly affect the community since we do not require full coverage of the Signals universe.

Signals V2 data will be used for Signals scores in rounds starting on or after Jan 1, 2025.

Furthermore, with this release we are officially deprecating Signals V0, V1, and the ticker map files. These files have been de-listed from the website, but we will allow users to continue downloading these files via the API until Jan 1, 2025. On this date, these files will be removed and will no longer be available for download. They will not be updated each round and the historical files will be deleted. We are unable to provide alternatives.

---

### Post #2 — **mlinux** | 2024-12-02 02:50 UTC

What is the process for switching over the below CSV files to this new V2 dataset? Will the v2 version be a different S3 path or the same?

AWS_BASE_URL = ‘<https://numerai-signals-public-data.s3-us-west-2.amazonaws.com>’  
SIGNALS_UNIVERSE = f’{AWS_BASE_URL}/latest_universe.csv’  
SIGNALS_TICKER_MAP = f’{AWS_BASE_URL}/signals_ticker_map_w_bbg.csv’  
SIGNALS_TARGETS = f’{AWS_BASE_URL}/signals_train_val_bbg.csv’

---

### Post #3 — **yantime** | 2024-12-03 21:26 UTC

Dear Numer.ai,

I am writing to suggest the creation of an ETF (Exchange-Traded Fund) based on your hedge fund. This would allow smaller investors, including the Numer.ai community, to invest in your fund and potentially benefit from its success.

I believe this would be a mutually beneficial opportunity, providing greater access to your fund while also expanding your investor base.

Thank you for considering this suggestion. I look forward to hearing your thoughts.

Sincerely,  
Yan

---

### Post #4 — **ark** | 2024-12-03 21:53 UTC _(reply to #2)_

You can get the universe from the live.parquet file. We are unable to provide equivalents for the ticker map files.

---

### Post #5 — **mlinux** | 2024-12-08 10:48 UTC _(reply to #4)_

I am currently using the opensignals to pull data from Yahoo. Is anyone working to update this package to work with v2 data? I am looking at the new live.parquet file and without a yahoo column, I am unsure how to correctly pull data from Yahoo.

[github.com](<https://github.com/councilofelders/opensignals>)

![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/e/e4baf16a46616615bb92db8e7a5937334ad92c9f_2_690x344.png)

### [GitHub - councilofelders/opensignals](<https://github.com/councilofelders/opensignals>)

Contribute to councilofelders/opensignals development by creating an account on GitHub.
