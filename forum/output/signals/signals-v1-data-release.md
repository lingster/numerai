---
title: "Signals V1 Data Release"
category: Signals
url: https://forum.numer.ai/t/signals-v1-data-release/7050
created_at: 2024-02-21T17:02:09.513000+00:00
last_posted_at: 2025-02-23T08:59:00.462000+00:00
posts_count: 5
views: 2889
tags: []
---

# Signals V1 Data Release

---

### Post #1 — **chanes** | 2024-02-21 17:02 UTC

[![signals_data](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/6/6c9a43818c9e4622bd82a6ec6f3f8b330f4908a2_2_500x500.jpeg)signals_data1024×1024 101 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/6/6c9a43818c9e4622bd82a6ec6f3f8b330f4908a2.jpeg> "signals_data")

# Overview

Signals V1 data is out now and includes 24 features and updated tickers.

This dataset contains:

  1. Factors, which are similar to the factors which the target is neutral to. Use these to determine if your model is sufficiently unique, use them to neutralize your predictions, or use them as additional features in your dataset.
  2. Some starter features, which are relatively simple classic quant features constructed from returns series.



There is a new column called `numerai_ticker` which is the stock’s ticker, and country of execution (as a two-letter ISO code). We also include [composite FIGI tickers](<https://www.openfigi.com/about>) when available.

Legacy Signals data has been a mess of different sources, but V1 data has been built with our modern data pipelines and is now available via the [data API](<https://docs.numer.ai/numerai-signals/signals-data#data-api>).
    
    
    import pandas as pd
    from numerapi import NumerAPI
    napi = NumerAPI()
    napi.download_dataset("signals/v1.0/live.parquet", "live.parquet")
    pd.read_parquet("live.parquet")
    

This dataset comes with a [new example model](<https://signals.numer.ai/v1_lgbm_ffn>), a small LGBM trained on the 24 features in this dataset.

## Breaking Changes

There are breaking changes from the legacy dataset:

  * Removed old ticker columns
  * Renamed `friday_date` to `date`
  * Renamed targets
  * Default target change



If you have Bloomberg tickers, you can replace the exchange code with the ISO country code to map to `numerai_ticker`. See the updated [example notebook](<https://colab.research.google.com/github/numerai/signals-example-scripts/blob/master/example_model.ipynb#scrollTo=c60a1d87-0cbd-4a4b-be6b-66a882fc7895>) for an example.

The targets have slight name changes to match the conventions of our other datasets. For example, `target_20d_factor_feat_neutral` is now `target_factor_feat_neutral_20`.

The default target is now `target_factor_feat_neutral_20`. The legacy default targets (target_4d and target_20d) have been renamed to `target_eleven_{length}`.

### What do you need to do?

To prepare for this update, at minimum you will need to make the following changes:

**Live submissions**

  1. Update your pipeline to use data from the [data API](<https://docs.numer.ai/numerai-signals/signals-data#data-api>).

  2. The live.parquet file contains the latest universe with `numerai_ticker` and `composite_figi` tickers (along with v1 features)




**Model training**

  1. Update your pipeline to map `numerai_ticker` to the ticker of your choosing for historical data.
  2. Update your pipeline to read the `date` column instead of `friday_date`
  3. If your pipeline uses any of the auxiliary targets, update the target names to the new convention.
  4. If your pipeline uses the old default target, be aware that the default target has changed.



You can refer to our new [example notebook](<https://colab.research.google.com/github/numerai/signals-example-scripts/blob/master/example_model.ipynb>) to see what this looks like now.

## V1 Features

The new features are:
    
    
    feature_adv_20d_factor
    feature_beta_factor
    feature_book_to_price_factor
    feature_country
    feature_dividend_yield_factor
    feature_earnings_yield_factor
    feature_exchange_code
    feature_growth_factor
    feature_impact_cost_factor
    feature_market_cap_factor
    feature_momentum_12w_factor
    feature_momentum_26w_factor
    feature_momentum_52w_factor
    feature_momentum_52w_less_4w_factor
    feature_ppo_60d_130d_country_ranknorm
    feature_ppo_60d_90d_country_ranknorm
    feature_price_factor
    feature_rsi_130d_country_ranknorm
    feature_rsi_60d_country_ranknorm
    feature_rsi_90d_country_ranknorm
    feature_trix_130d_country_ranknorm
    feature_trix_60d_country_ranknorm
    feature_value_factor
    feature_volatility_factor
    

Features with `{n}(d|w)` in the name (for example, `feature_adv_20d_factor`) are time-series features that are computed over `n` days or `n` weeks.

Features with `country_ranknorm` in the name are grouped by country, then ranked, then gaussianized.

Features with `factor` in the name refer to risk factors that most of the targets are neutral to.

PPO, RSI and TRIX are examples of technical indicators.

PPO is a percentage price oscillator that compares shorter and longer moving averages in a ratio

RSI is the relative strength index usually used as an overbought/oversold indicator

TRIX is a triple exponential moving average indicator usually used as momentum or reversal feature

`momentum_52w_less_4w` refers to one year return of a stock excluding the last 4 weeks.

## Minor Target Updates

There are now 20 and 60-day versions of all targets.

## Ticker Updates

The new data has two tickers: `numerai_ticker` and `composite_figi`.

You can still submit any of the currently accepted tickers. So we now accept all of the following:

  * cusip
  * sedol
  * bloomberg_ticker
  * composite_figi
  * numerai_ticker



You’ll see that we only have composite FIGI tickers going back to September 2022. If anyone knows where to find historic FIGI tickers, please reach out. This also means that we cannot accept `composite_figi` for diagnostics.

## Legacy Data Deprecation and New Submission Formats

All Signals legacy data is now deprecated and will no longer be available as of **March 30, 2024**. Anything that does not have the `signals/v1.0` prefix in the data API will be discontinued.

Anything not in the data API will also be discontinued. For example, any hardcoded S3 URLs like <https://numerai-signals-public-data.s3-us-west-2.amazonaws.com/universe/latest.csv> will not be available.

Along with this deprecation, please note the updates to submissions and diagnostics formats. The legacy formats will still be accepted, so updating your submission format is not required.

Live Submissions

  * The current live submission header format is: `[(cusip|sedol|bloomberg_ticker|ticker), data_type, friday_date, signal]`: 
    * [![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/1/13320b63d9f2fb34022b08a21e5b518d7c90d4ed.png)680×334 16.4 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/1/13320b63d9f2fb34022b08a21e5b518d7c90d4ed.png>)

  * Submissions have been updated to only require two columns: `[(cusip|sedol|bloomberg_ticker|composite_figi|numerai_ticker), signal]`
    * [![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/6/69fb3f81610bb04492359e7309761d3ea3996f2f.png)378×344 11 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/6/69fb3f81610bb04492359e7309761d3ea3996f2f.png>)




Diagnostics

  * The current diagnostics header format is: `[(cusip|sedol|bloomberg_ticker|ticker), data_type, friday_date, signal]`: 
    * [![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/5/5ebc3f2d452f227c1869391df098b55f1b0654da.png)686×332 20.1 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/5/5ebc3f2d452f227c1869391df098b55f1b0654da.png>)

  * Diagnostics have been updated to only require three columns: `[(cusip|sedol|bloomberg_ticker|numerai_ticker), date, signal]`: 
    * [![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/6/6aa03dc1123fda7e4af40abca285a18c45a00777.png)552×340 14.8 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/6/6aa03dc1123fda7e4af40abca285a18c45a00777.png>)

---

### Post #2 — **jrb** | 2024-02-23 20:19 UTC

Nice! Three more features, compared to the 2016 v1 numerai classic dataset. ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=12)

---

### Post #5 — **wrcx** | 2024-03-09 00:48 UTC

Thanks for the post. A few questions that I couldn’t find answer elsewhere:

  * What time during the day does the live data update?

  * It looks like the latest ticker universal now resides in ‘signals/v1.0/live.parquet’. Since it changes daily, is there any reference file that maps numerai_ticker to other major tickers (e.g., Bloomberg, Yahoo) and updates daily?

---

### Post #6 — **katsu1110** | 2024-03-29 03:16 UTC

Thanks for the update.

This

`napi = NumerAPI()`

should be

`napi = SignalsAPI()`

correct? The same applies in the docs as well:

![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/9/90e8adeb4f6f03ac5b052087372c6555fb93d298_2_500x500.png) [docs.numer.ai](<https://docs.numer.ai/numerai-signals/data#files>)

![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/7/7469d06d5a34327e8bd1c3fc001f341b2ee835d7.png)

### [Data | Numerai Docs](<https://docs.numer.ai/numerai-signals/data#files>)

---

### Post #7 — **joakim** | 2025-02-23 08:59 UTC

Is the **feature_beta_factor** column measured against some **global index** , or the **main index of each respective country** (or something else)? I’m curious whether having a **beta feature** for all tickers in the universe relative to the **main index in each country** within the universe could be useful? E.g. 26 beta factors (one per market), so one beta feature (for all stocks) against the US market, another against Japan, etc. Possibly sector betas as well, if you can’t provide sectors themselves? I’m thinking this would be something Numerai could possibly do directly, without having to rely on and pay data vendors?
