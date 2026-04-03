---
title: "Signals: Plugging in the data from Quandl"
category: Signals
url: https://forum.numer.ai/t/signals-plugging-in-the-data-from-quandl/2431
created_at: 2021-03-18T14:51:53.883000+00:00
last_posted_at: 2021-03-20T04:52:40.255000+00:00
posts_count: 3
views: 1806
tags: []
---

# Signals: Plugging in the data from Quandl

---

### Post #1 — **surajp** | 2021-03-18 14:51 UTC

Quandl example model: [`example_model_quandl.py`](<https://github.com/numerai/example-scripts/tree/master/signals/quandl>)

Google Colab notebook: [Signals_Quandl_EOD_baseline.ipynb](<https://github.com/parmarsuraj99/numerai-guides/blob/master/Signals_Quandl/Signals_Quandl_EOD_baseline.ipynb>)

[Quandl](<https://www.quandl.com>) is a financial, economic, alternative data marketplace which provides premium and free data.

One such data source is [End of Day US Stock Prices by QuoteMedia](<https://www.quandl.com/data/EOD-End-of-Day-US-Stock-Prices>) (premium, so need to set `API_KEY` in `example_model_quandl.py`).

> Updated daily, this data feed offers end of day **prices, dividends, adjustments and splits** for **US publicly traded stocks** with **history to 1996**. Prices are provided both adjusted and unadjusted.

This example downloads the whole ‘Time-series’ data in a .zip file and loads Adj_Open and Adj_Close columns from it. However, specific tickers for specific time span can also be loaded iteratively using API(much slower). [Getting started with the API](<https://www.quandl.com/data/EOD-End-of-Day-US-Stock-Prices/usage/quickstart/api>).

While the feature extraction and modeling part are very similar to the main `example_model.py`, the focus here is to make the data loading flexible so different data sources can be easily ‘plugged’.

**Steps to re-arrange the data as in Signals’ main`example_script.py`**

  1. Find common tickers between [EOD data source ticker list](<https://s3.amazonaws.com/quandl-production-static/end_of_day_us_stocks/ticker_list.csv>) and Numerai Signals Universe’s yahoo tickers.
  2. Specify the columns in `download_full_and_load` with common tickers and rename columns as required by feature extraction setup.


    
    
        # column names in the csv file without headers
        cols = [
            "ticker", "date", "Open", "High", "Low", "Close", "Volume", "Dividend",
            "Split", "Adj_Open", "Adj_High", "Adj_Low", "Adj_Close", "Adj_Volume",
        ]
    
        # usecols refers to the column in the csv.
        # using only [ticker, date, adj_open, adj_close]
        # Loading only needed columns as FP32
        print("loading from csv...")
        full_data = pd.read_csv(
            f_name,
            usecols=[0, 1, 9, 12],
            compression="zip",
            dtype={0: str, 1: str, 9: np.float32, 12: np.float32},
            header=None,
        )
    
        # renaming the columns
        filter_columns = ["ticker", "date", "Adj_Open", "Adj_Close"]
        full_data.columns = filter_columns
        full_data.set_index("date", inplace=True)
        full_data.index = pd.to_datetime(full_data.index)
    

  3. Map ticker names to Bloomberg tickers using [Numerai’s Bloomberg ticker map](<https://numerai-signals-public-data.s3-us-west-2.amazonaws.com/signals_ticker_map_w_bbg.csv>).


    
    
        full_data = full_data[full_data.ticker.isin(common_tickers)]
        full_data["bloomberg_ticker"] = full_data.ticker.map(
            dict(zip(ticker_map["yahoo"], ticker_map["bloomberg_ticker"]))
         )
    

After creating a `day_chg` column and applying RSI and SMA on them, features are quintiled and lags are calculated as in main `example_model.py`.

**Validation results:**  


[![quandl_signals_scores_ttransparent_](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/6b81a5ffef59f67612b72621f466606f2f917758_2_517x292.jpeg)quandl_signals_scores_ttransparent_2368×1341 160 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/6b81a5ffef59f67612b72621f466606f2f917758.jpeg> "quandl_signals_scores_ttransparent_")

Thanks [@_liamhz](</u/_liamhz>) for the feedback ![:slight_smile:](https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=13)

---

### Post #2 — **richai** | 2021-03-19 18:36 UTC

nice! not a bad result for such simple data.

you say this is premium, how much does this data cost you per month?

(also did you train on validation for this great cumsum graph?)

---

### Post #3 — **surajp** | 2021-03-20 04:52 UTC _(reply to #2)_

This one costs me USD $49/mo. but I guess some organizational licensing is there.

This wasn’t trained on validation data. However, this has some extra features compared to default yfinance example_model.py:

  * a day_change column
  * RSI: (14, 21)
  * SMA: (14, 21)
  * quintilation factor to 100 from 5



we get 72 features after computing lags.
