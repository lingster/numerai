---
title: "Signals: Plugging in the data from Alpha Vantage"
category: Signals
url: https://forum.numer.ai/t/signals-plugging-in-the-data-from-alpha-vantage/3295
created_at: 2021-05-14T04:54:39.377000+00:00
last_posted_at: 2021-07-03T18:43:04.422000+00:00
posts_count: 3
views: 1744
tags: []
---

# Signals: Plugging in the data from Alpha Vantage

---

### Post #1 — **surajp** | 2021-05-14 04:54 UTC

[This script](<https://github.com/numerai/example-scripts/tree/master/signals/alphavantage>) uses data from [AlphaVantage](<https://www.alphavantage.co/>) using raw queries which do not require any extra library.
    
    
    pip install numerapi tqdm
    

`numerapi` and `tqdm` (to check progress of downloads) are needed.

`key = "<ALPHAVANTAGE API KEY>"` **this needs to be set before running the script.**

AlphaVantage has a free key with a limit of 5 API calls per minute. For a limit of 75 calls per minute, you can pay $50 USD per month for a [premium key](<https://www.alphavantage.co/premium/>). This script was created for use with the 75 calls per minute plan so it would work. This takes around 13 mins to load all US stocks.

Alpha Vantage offers various types of data including stocks, cryptocurrencies, and technical indicators. [Documentation](<https://www.alphavantage.co/documentation/>).

### Data Loading

Since the API has a rate limit of calls per minute, this script provides two functions for loading the data.

  * Sequential

    * This may take over an hour to load all available tickers.
    * Safe and loading function can be stopped.
    * `full_data = load_data(tickers, "full_data.csv", threads=False)`
  * Parallel

    * uses threads from Python’s `concurrent` module.
    * much faster loading (~13 mins for all US tckers)
    * execution is not stoppable.
    * `full_data = load_data(tickers, "full_data.csv", threads=True)`
    * Thanks to **[Jordi Villar](<https://twitter.com/jrdi>)** for **supercharging the parallel execution** and bringing it to ~13 mins.



### Feature Generation

  * Since Alpha vantage has different types of data resolutions, this script uses **weekly data** (OHLC) to generate features.
  * Some features are `simple moveing average` and `exponential moving average` of periods `[2, 5, 21, 50, 200]`.



I’d like to thank [@_liamhz](</u/_liamhz>) for the encouragement and feedback ![:slightly_smiling_face:](https://emoji.discourse-cdn.com/twitter/slightly_smiling_face.png?v=15). All errors remain mine.

[![Diagnostics](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/2c5cc565100ad0703d9e8cb52f8b25b28a5c302f_2_201x500.png)Diagnostics304×755 12.3 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/2c5cc565100ad0703d9e8cb52f8b25b28a5c302f.png> "Diagnostics")

---

### Post #2 — **ihab** | 2021-07-02 22:59 UTC

Thank you very much [@surajp](</u/surajp>) and [@_liamhz](</u/_liamhz>) for this. Question, please:  
Have you tried this with the entire universe? if so, I am assuming that 75 API calls per minute were sufficient? And most importantly, were all tickers submitted valid by NumeraiSignals? Looking forward to hearing from you. Once again, a BIG THANK YOU!

---

### Post #3 — **surajp** | 2021-07-03 18:43 UTC _(reply to #2)_

Thank you [@ihab](</u/ihab>) .

I tested on the intersection of the tickers that Numerai wants and the tickers that AV provides, It was ~3.2k ish common tickers (US is fully covered).

Since the common tickers are in Bloomberg format, they were accepted when I ran this script few weeks ago.
