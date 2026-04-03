---
title: "Free or cheap data and tools for Numerai Signals"
category: Signals
url: https://forum.numer.ai/t/free-or-cheap-data-and-tools-for-numerai-signals/350
created_at: 2020-05-07T04:48:42.722000+00:00
last_posted_at: 2021-07-23T12:12:06.843000+00:00
posts_count: 19
views: 11128
tags: []
---

# Free or cheap data and tools for Numerai Signals

---

### Post #1 — **player1** | 2020-05-07 04:48 UTC

Please feel free to add any others that you know of. I’m not associate with any of these and I’m also not vouching for the quality of any of them. ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=9)

  * [Google Finance](<https://support.google.com/docs/answer/3093281?hl=en>) \- Free
  * [Yahoo Finance](<https://github.com/ranaroussi/yfinance>) \- Free
  * [TenQuant](<https://www.tenquant.io/>) \- Free
  * [EDGAR](<https://www.sec.gov/edgar/searchedgar/accessing-edgar-data.htm>) \- Free
  * [IEXCloud](<https://iexcloud.io/pricing/>) \- Cheap
  * [AlphaVantage](<https://www.alphavantage.co/>) \- Free/Cheap
  * [WorldTradingData](<https://www.worldtradingdata.com/>) \- Free/Cheap
  * [Tiingo](<https://www.tiingo.com/account/billing/pricing>) \- Free/Cheap
  * [Quandl](<https://www.quandl.com/>) \- Some Free
  * [Norgate Data](<https://norgatedata.com/>) \- Free Trial / Moderately priced
  * [Intrinio](<https://intrinio.com/prices>) \- Moderately priced
  * [Polygon](<https://polygon.io/pricing>) \- Expensive
  * [Xignite](<https://www.xignite.com/>) \- Free Trial / Might be expensive
  * [BarChart](<https://www.barchart.com/ondemand>) \- Might be expensive

---

### Post #2 — **kainsama** | 2020-05-07 06:15 UTC

[FMP](<https://financialmodelingprep.com/>) \- Free

---

### Post #3 — **joakim** | 2020-05-07 22:49 UTC

Alternative data (sentiment)

  * [StockTwits](<https://api.stocktwits.com/developers/docs/start>) \- Free?
  * [Sentdex](<http://www.sentdex.com/>) \- API pricing unknown

---

### Post #4 — **joakim_arvidsson** | 2020-06-05 20:42 UTC

* [Zipline](<https://github.com/quantopian/zipline/blob/master/README.rst>) \- OSS backtester.

---

### Post #5 — **joakim** | 2020-06-07 23:02 UTC

* [Borsdata](<https://borsdata.se/en/pricetable>) \- Free/Cheap. Focus on Nordic markets. API access requires Pro membership.



I also found a [tutorial on how to analyze financial data](<https://towardsdatascience.com/pull-and-analyze-financial-data-using-a-simple-python-package-83e47759c4a7>) using the FMP API.

---

### Post #6 — **ia_ai** | 2020-06-08 00:59 UTC

For R users, the [tidyquant](<https://cran.r-project.org/web/packages/tidyquant/vignettes/TQ00-introduction-to-tidyquant.html>) package has quite a few handy [functions](<https://business-science.github.io/tidyquant/articles/TQ01-core-functions-in-tidyquant.html>) to download data from different sources.

---

### Post #7 — **sturlese** | 2020-06-08 08:33 UTC

[Sharadar](<https://www.sharadar.com/>) has prices and fundamentals.

---

### Post #8 — **slyfox** | 2020-10-07 04:34 UTC

Anyone have any experience with these?

![](https://cdn-ildbolb.nitrocdn.com/UezRGMkmQsEFWqGJixAgmLduluxMTcEV/assets/images/optimized/rev-270a884/www.koyfin.com/wp-content/uploads/2023/05/favicon.svg) [Koyfin](<https://www.koyfin.com/>)

![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/1/196744fd86cca6a87bc0fde0a9b11b6095316bd7_2_690x362.png)

### [Comprehensive financial data analysis - Koyfin](<https://www.koyfin.com/>)

Koyfin provides tools for investors to research stocks & other asset classes. Koyfin covers equities, ETFs, mutual funds, forex, bonds, etc.

![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/138f79d3852d42866bf8cc4609427689b2754a45.png) [Canalyst](<https://canalyst.com/>)

### [Canalyst - Clean data. Fundamental models.](<https://canalyst.com/>)

4,000+ financial models with every KPI that matters, built and updated by our team of analysts.

---

### Post #9 — **degerhan** | 2021-02-17 17:33 UTC

**ISIN codes**  
Signals ticker mapping challenges have taken a good part of the zoom and twitch sessions recently. Just came across this package, another arrow in our quiver:
    
    
    # https://pypi.org/project/investpy/
    # Financial Data Extraction from Investing.com with Python
    !pip install investpy
    
    import investpy
    import pandas as pd
    
    pd.DataFrame(
        investpy.stocks.get_stocks_dict(
            country=None,
            columns=["symbol", "country", "name", "full_name", "isin", "currency"],
            as_json=False,
        )
    )
    

voilà, you have name, country, and isin codes for 40,000 stocks

| symbol | country | name | full_name | isin | currency  
---|---|---|---|---|---|---  
0 | TS | argentina | Tenaris | Tenaris | LU0156801721 | ARS  
1 | APBR | argentina | PETROBRAS ON | Petroleo Brasileiro - Petrobras | BRPETRACNOR9 | ARS  
2 | GGAL | argentina | Grupo Financiero Galicia | Grupo Financiero Galicia B | ARP495251018 | ARS  
3 | TXAR | argentina | Ternium Argentina | Ternium Argentina SA | ARSIDE010029 | ARS  
4 | PAMP | argentina | Pampa Energia | Pampa Energia SA | ARP432631215 | ARS  
… | … | … | … | … | … | …

---

### Post #10 — **sirbradflies** | 2021-02-25 16:35 UTC _(reply to #9)_

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/forum.numer.ai/degerhan/48/3449_2.png) degerhan:

> 
>     import investpy
>     import pandas as pd
>     
>     pd.DataFrame(
>         investpy.stocks.get_stocks_dict(
>             country=None,
>             columns=["symbol", "country", "name", "full_name", "isin", "currency"],
>             as_json=False,
>         )
>     )
>     

Hi Degerhan,

That is very helpful as I’m just now approaching Signals and figuring out how to use the bloomberg tickers. Did you go one step further and match them to the investpy list? How did you match them?

---

### Post #11 — **degerhan** | 2021-02-25 23:03 UTC _(reply to #10)_

[@sirbradflies](</u/sirbradflies>), I did not pursue this further.

In real life I only trade commodity futures spreads, where the symbols are exact and data is extremely clean. I was trying to gather a similar quality dataset for Signals until I realized I was trying to boil the data ocean instead of building useful things.

[@arbitrage](</u/arbitrage>) recently advised in rocketchat that he is working only with US stocks for now (and he is getting solid results). If you remove the US suffix from bloomberg_ticker, what remains will be the Yahoo ticker for all except about 10 symbols, and historical data coverage is quite good. I’ve decided to just focus on the US stock universe until I get my act together on the modeling side; and expand the dataset at a later phase.

(actually to speed up iterations, I am only working with the largest cap 900 US stocks for now, list here: [SP900](<https://gist.github.com/degerhan/e85e9eb407406a406c58c3686ec3c789>) )

---

### Post #12 — **sirbradflies** | 2021-02-26 09:01 UTC _(reply to #11)_

hi [@degerhan](</u/degerhan>),

Thanks for the tips. I had actually already started focused on US stocks when I realized most of them were easily downloadable (except for Berkshire and a few others ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=9) ).

I’ll share an update if I come up with a robust way to match all the bloomberg tickers on Yahoo Finance.

---

### Post #13 — **fisagol** | 2021-02-26 19:55 UTC

For those who want to get data directly from [FINVIZ](<https://finviz.com/>) there is a code implemented which helps to get specific data from each of the companies we want.

Attached code:
    
    
    # Data that we want to extract from Finviz Table
    metric = ['Price', 'EPS next 5Y', 'Beta', 'Shs Outstand']
    
    def fundamental_metric(soup, metric):
        # the table which stores the data in Finviz has html table attribute class of 'snapshot-td2'
        return soup.find(text = metric).find_next(class_='snapshot-td2').text
       
    def get_finviz_data(ticker):
        try:
            url = ("http://finviz.com/quote.ashx?t=" + ticker.lower())
            soup = bs(requests.get(url,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0'}).content)
            dict_finviz = {}        
            for m in metric:   
                dict_finviz[m] = fundamental_metric(soup,m)
            for key, value in dict_finviz.items():
                # replace percentages
                if (value[-1]=='%'):
                    dict_finviz[key] = value[:-1]
                    dict_finviz[key] = float(dict_finviz[key])
                # billion
                if (value[-1]=='B'):
                    dict_finviz[key] = value[:-1]
                    dict_finviz[key] = float(dict_finviz[key])*1000000000  
                # million
                if (value[-1]=='M'):
                    dict_finviz[key] = value[:-1]
                    dict_finviz[key] = float(dict_finviz[key])*1000000
                try:
                    dict_finviz[key] = float(dict_finviz[key])
                except:
                    pass 
        except Exception as e:
            print (e)
            print ('Not successful parsing ' + ticker + ' data.')        
        return dict_finviz
    
    finviz_data = get_finviz_data(ticker)
    
    finviz_data

---

### Post #14 — **whaleblotter** | 2021-02-27 02:38 UTC

Any thoughts on Alpaca API v2

![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/c/c852d20018b11a81452fb98389b96179b13b3fb1.png) [Alpaca API Docs](<https://docs.alpaca.markets/reference/stockauctions-1>)

![](https://files.readme.io/2a85a89-black-alpaca-logo.svg)

### [Historical auctions](<https://docs.alpaca.markets/reference/stockauctions-1>)

The historical auctions endpoint provides auction prices for a list of stock symbols between the specified dates.

curl -X GET -H “APCA-API-KEY-ID: …” -H “APCA-API-SECRET-KEY: …” “<https://data.alpaca.markets/v2/stocks/AAPL/trades?start=2021-02-2> 4T00:57:47.317087Z&end=2021-02-25T00:57:47.317087Z”

Free account max end time seems to be utcnow - 15min

---

### Post #15 — **sirbradflies** | 2021-04-23 06:54 UTC _(reply to #14)_

Did anybody find a free data source for order book data?

Thanks

---

### Post #16 — **crispy_holiday** | 2021-06-15 06:05 UTC

Does anyone have experience with <https://eodhistoricaldata.com>?

---

### Post #17 — **mugamma** | 2021-06-15 12:46 UTC _(reply to #16)_

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/c/87869e/48.png) crispy_holiday:

> Does anyone have experience with [https://eodhistoricaldata.com ](<https://eodhistoricaldata.com>)?

This might be an important detail from their disclaimer -

> All CFDs (stocks, indices, futures, mutual funds, ETFs), and Forex are not provided by exchanges but rather by market makers, and so prices may not be accurate and may differ from the actual market price, meaning prices are indicative and not appropriate for trading purposes.

---

### Post #18 — **autratec** | 2021-06-30 12:38 UTC

Hi, I want to fetch last 48 days close price by every trick. Is there any free api resource can be suggested ?

---

### Post #19 — **gammarat** | 2021-07-23 12:12 UTC _(reply to #16)_

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/c/87869e/48.png) crispy_holiday:

> Does anyone have experience with [https://eodhistoricaldata.com ](<https://eodhistoricaldata.com>)?

I’ve just started using them, along with Altman’s [UndocumentedMatLab](<https://undocumentedmatlab.com/EODML>) software. So far, so good, we’ll see how it goes. EOD seems to have a lot of info available, which should take a lot of the more tedious programming tasks off the table.

EOD [provides support for other languages](<https://eodhistoricaldata.com/financial-apis/category/excel-python-php-laravel-java-matlab-examples/>), and the [data prices](<https://eodhistoricaldata.com/pricing>) aren’t outrageous. It would be great if Numerai could work a deal though them (though I can understand why they might not want to do so); perhaps interested individuals could figure out a way to access the data via some sort of group account. IDK, I’m just throwing spaghetti at the walls now…
