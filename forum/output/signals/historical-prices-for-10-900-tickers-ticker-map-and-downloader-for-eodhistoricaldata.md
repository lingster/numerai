---
title: "Historical prices for 10,900 tickers - ticker map and downloader for eodhistoricaldata"
category: Signals
url: https://forum.numer.ai/t/historical-prices-for-10-900-tickers-ticker-map-and-downloader-for-eodhistoricaldata/4321
created_at: 2021-10-11T20:51:46.008000+00:00
last_posted_at: 2023-06-02T07:56:45.066000+00:00
posts_count: 9
views: 3459
tags: []
---

# Historical prices for 10,900 tickers - ticker map and downloader for eodhistoricaldata

---

### Post #1 — **degerhan** | 2021-10-11 20:51 UTC

First thank you [@restrading](</u/restrading>) for pointing me to [eodhistoricaldata](<https://eodhistoricaldata.com/>). They seem to be a fully [legit](<https://eodhistoricaldata.com/financial-apis/our-data-sources-and-data-partners/>) operation, and not to be confused with [eoddata.com](<http://eoddata.com>).

## What I like

  * Excellent coverage of the signals universe (all except Japan, New Zealand, Czech Republic); in contrast with Tiingo which only has US.
  * Historical data for a majority of the de-listed stocks; in contrast with yahoo, which only covers live tickers.
  * Split and dividend adjusted prices; in contrast with iqfeed or refinitiv consumer, which have excellent data but no adjustments.
  * Practically limitless API quota; in contrast with IEX cloud, which counts each ticker x day as an API usage.
  * $20/mo price is hard to beat.



## What makes it challenging

As usual, ticker mapping. Well, it’s a good thing I worked on it – your welcome ![:slight_smile:](https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=15)

Within the [GitHub - degerhan/dsignals: Utilities and information for the signals.numer.ai tournament](<https://github.com/degerhan/dsignals>) repository:

  * `build_eodhd_map.py` will attempt to map the 13,400 live and historical tickers with rules, replacements, and manual overrides. While some tickers are speculative, most are good.
  * `download_quotes.py` is the universal downloader, that will use either eodhd or yahoo, saving each ticker history in a separate pickle file.



While it is possible to invest some time in a number of Korean and Taiwanese exchange codes, and possibly a look at the delisted Singapore tickers, as of October 2021, the net result is 10,900+ ticker histories.

Good hunting !

---

### Post #2 — **aventurine** | 2021-10-12 05:38 UTC

Nice job! That ticker map looks amazing and really shows how many holes are in the yahoo data. Seems like this needs a retroactive bounty! ![:man_dancing:](//forum.numer.ai/images/emoji/twitter/man_dancing.png?v=9)

---

### Post #3 — **objectscience** | 2021-10-12 12:36 UTC _(reply to #2)_

[@aventurine](</u/aventurine>) [@degerhan](</u/degerhan>) I’ve pinged the CoE in their RC channel on a potential bounty.  
Really nice work here!

---

### Post #4 — **degerhan** | 2022-02-20 03:11 UTC

I pushed an update to github – the mapper and downloader now retrieve price data for 11,200 tickers in the live and historical Signals universe. Data source is automatically selected as eodhistoricaldata for its supported exchanges, and yahoo for Japan, Czech Republic and New Zealand.

---

### Post #5 — **olivepossum** | 2022-07-31 21:39 UTC

Wouldn’t it make sense to push this to the official Numerai Github repo?

---

### Post #6 — **quantverse** | 2022-11-04 15:13 UTC

For those who don’t know yet - JP data is already supported (the TSE exchange), but you must ask the support to enable it for you…

In the map builder script use this line:
    
    
    "JP": ConverterItem(MAP_EODHD, _BBG, MAP_EODHD, ".TSE"),

---

### Post #7 — **guillem** | 2022-12-18 12:42 UTC

Hi,

Not sure if it’s the expected result or I’m doing something wrong, but when I merge eodhd-map.csv with the train csv (<https://numerai-signals-public-data.s3-us-west-2.amazonaws.com/signals_train_val.csv>) I’m only getting 4906 coincident tickers/bloomber_tickers ![:confused:](http://forum.numer.ai/images/emoji/twitter/confused.png?v=12)

Thanks for the work!

---

### Post #8 — **guillem** | 2022-12-18 12:51 UTC _(reply to #7)_

sorry! never mind, was using old target file instead of this one <https://numerai-signals-public-data.s3-us-west-2.amazonaws.com/signals_train_val_bbg.csv>

---

### Post #9 — **k1111** | 2023-06-02 07:56 UTC _(reply to #6)_

Could you tell me more about how to get Japanese stock data from EOD?
