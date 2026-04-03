---
title: "Open Source Datasets for Numerai Signals"
category: Signals
url: https://forum.numer.ai/t/open-source-datasets-for-numerai-signals/5011
created_at: 2022-03-03T16:12:31.934000+00:00
last_posted_at: 2022-03-08T14:04:23.923000+00:00
posts_count: 6
views: 1695
tags: []
---

# Open Source Datasets for Numerai Signals

---

### Post #1 — **thomasxthomas** | 2022-03-03 16:12 UTC

2022-03-03: version 1.0

Preparing data sources is the biggest challenge for Numerai Signals as it is extremely time-consuming. In view of this, I want to start a community project to share and document open-source datasets for Numerai Signals.

The current goal is to maintain high-quality training and validation datasets for Numerai Signals and provide benchmark performance on these datasets. This benchmark can be used to decide whether a new data source or features can improve model performance.

I have created a historical stock metadata mapping of US stocks in the Numerai universe, covering the time period from 2003 to 2020. The stock metadata is mapped with academic research quality databases so that it does not have survivor bias. I also created a very simple dataset of normalised price and financials features using data sources from CRSP, Compustat and OptionMetrics, obtained through WRDS.

The data can be found in the following GitHub

[numerai-signals/data at main · ThomasWong2022/numerai-signals (github.com)](<https://github.com/ThomasWong2022/numerai-signals/tree/main/data>)

This is a work in progress. Please open an issue on GitHub for data sources and feature engineering suggestions.

---

### Post #2 — **maxchu** | 2022-03-04 00:01 UTC

Thanks for the great work! Is it possible that this project can be integrated into <https://github.com/councilofelders/opensignals> ?

---

### Post #3 — **thomasxthomas** | 2022-03-04 10:35 UTC _(reply to #2)_

As I am using data from academic research (which is not available in real-time), the dataset cannot be used to submit the live predictions for Numerai Signals. It can be integrated into the opensignals repo once I finish the draft of my paper on this dataset.

---

### Post #4 — **maxchu** | 2022-03-05 00:43 UTC _(reply to #3)_

oh yes, it cannot be used in live predictions. But it is still a very good resource for ppl who can test their ideas on the dataset, if it turns out good then ppl can buy similar data from data companies.

I am not sure if numeral can help to expand/improve this type of free historical data to lower the entry barrier.

---

### Post #5 — **thomasxthomas** | 2022-03-05 12:16 UTC _(reply to #4)_

The purpose of this dataset and benchmark is to encourage the community to maintain open-source/low-cost data feeds by sharing the time and costs of preparing data feeds.

While most data license terms do not allow sharing of the raw data itself, it is usually allowed to share processed data as in Open Source Asset Pricing.

[Data – Open Source Asset Pricing (openassetpricing.com)](<https://www.openassetpricing.com/data/>)

The Numerai features are created in a conceptually similar process with better data sources and different factors to neutralise features and targets against, such as sector and country. The big difference is that the data generation process will be open-source for my dataset.

---

### Post #6 — **thomasxthomas** | 2022-03-08 14:04 UTC

2022-03-08: version 2.0  
Added sentiment data from Ravenpack
