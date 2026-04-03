---
title: "Understanding Bloomberg Tickers"
category: Signals
url: https://forum.numer.ai/t/understanding-bloomberg-tickers/1905
created_at: 2021-02-19T20:07:48.922000+00:00
last_posted_at: 2021-04-20T21:00:05.866000+00:00
posts_count: 9
views: 6888
tags: []
---

# Understanding Bloomberg Tickers

---

### Post #1 — **arbitrage** | 2021-02-19 20:07 UTC

You may be confused about the ticker provided by Numerai in the ‘ticker universe’ provided every week; I certainly was! I have found some resources to explain the two characters following the ticker. Allow me to assist:

Bloomberg requires an ‘Exchange Code’ or a ‘Composite Code’ following a ticker in order to retrieve the relevant information about said ticker. Bloomberg’s Composite Code is a blanket suffix that accesses all exchanges in a country.

For instance, the United States has 8+ different exchanges (NYSE American, CBOE BATS, NYSE, NYSE Arca, NASDAQ Global Market, NASDAQ Capital Market, OTC markets, NASDAQ Global Select) which have their own exchange code. Having to remember which exchange AAPL trades on in order to retrieve quotes is problematic, so Bloomberg also uses a Composite Code which aggregates all of the US exchanges into a single end-point. “AAPL US” automatically routes to the correct US exchange.

Not all countries have a Bloomberg Composite Code. For instance, Turkey has a single exchange, the Istanbul Stock Exchange. Bloomberg’s Exchange Code for the ISE is “TI” and Turkey does not have a composite code. Therefore, the ticker provided by Numerai for a company traded in Turkey is followed by " TI"

Without further explanation from the team, we have to assume that we are given the Composite Code where such a code is available, otherwise the exchange code is provided.

From my Alpha Vantage mapping, I further discovered that Bloomberg represents different classes of shares using “/”. For instance, Berkshire Hathaway has Class “A” and Class “B” shares, and are passed to us from Numerai as “BRK/A US” and “BRK/B US”. This holds for the US, but a “/” also occurs in Canada. Simply replacing “/” with “-” fixes the issue. However, if “/” is followed by an empty space, dropping the “/” seems to fix mapping issues.

Numerai passes us some tickers that include an asterisk, however those companies only come from Mexico. Unfortunately, Alpha Vantage does not appear to cover Mexico at this time.

Mapping tickers from Bloomberg to the provider of your choice should not be a complicated affair now that you know what the Bloomberg ticker represents. I hope you are able to create mapping scripts incorporating this information. I encourage you to share those maps here.

I contributed to this script as a reference: [numerai-signals-tickermap/alpha_vantage_tickers.py at main · hellno/numerai-signals-tickermap · GitHub](<https://github.com/hellno/numerai-signals-tickermap/blob/main/scripts/alpha_vantage_tickers.py>)

---

### Post #2 — **lgs** | 2021-02-20 03:20 UTC

I have not yet tried any Signals predictions. BTW, I thought it would be easier to use CUSIP numbers and CINS numbers, instead of the Bloomberg Tickers. I think CUSIP is more official/formal and Bloomberg ticker is just for Bloomberg. I am not saying it is better way to do it, just throwing thoughts. Thanks arbitrage for sharing the info.

---

### Post #3 — **arbitrage** | 2021-02-20 14:33 UTC _(reply to #2)_

CUSIP is not international. ISIN or SEDOL would work better for the entire universe. We simply have to work with what we have at the moment ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=9)

---

### Post #4 — **lgs** | 2021-02-20 14:51 UTC _(reply to #3)_

Sure, we work with what we have ![:slightly_smiling_face:](http://forum.numer.ai/images/emoji/twitter/slightly_smiling_face.png?v=9)  
I meant CINS would work for international securities. Yes, CUSIP is only for the US and Canada.

---

### Post #5 — **stacktrace** | 2021-03-11 19:00 UTC

CUSIP, ISIN, SEDOL are proprietary identifiers which have very high licensing costs (>$100k for you to use these).

However, there is OpenFIGI. OpenFIGI is a Bloomberg funded effort to create a free and public permanent identifier. You can hit the API for free (with rate limitations) and get, for example, from the exchange ticker, the FIGI.

It would be very helpful if Numerai would provide the OpenFIGI identifier in Signals data. The Bloomberg exchange symbol is not permanent and cannot be used to ensure point-in-time accuracy of mapping to price series. OpenFIGI identifiers would allow for easier mapping across datasets and ensuring identifier consistency over time.

![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/3/37e8b4b205167cde08a545f53053bb1cd24043ce.png) [openfigi.com](<https://www.openfigi.com/api/overview>)

### [Overview | OpenFIGI](<https://www.openfigi.com/api/overview>)

---

### Post #6 — **datacryptoanalytics** | 2021-03-11 20:39 UTC

Very useful information, thanks for sharing friend. ![:smiley:](http://forum.numer.ai/images/emoji/twitter/smiley.png?v=9)

Now I’m starting to develop models for numbers and trying to understand more and more how it works.

---

### Post #7 — **gammarat** | 2021-04-20 13:21 UTC

Thanks [@arbitrage](</u/arbitrage>) ; I’m just starting with developing a Signals project, and your script is a big help (even if I do have to translate it to MatLab and adapt it to Yahoo ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=12)  
One possible issue; in your script you have

> elif ticker.endswith(**’ CA’**):  
>  return ‘.TRT’

Shouldn’t that be

> elif ticker.endswith(**’ CN’**)

[bold added by me]  
I was just looking over the most recent list (_latest.csv_), and those ending with “CN” all seem to be Canadian. Like these:

> ABX CN  
>  BCE CN  
>  BAM/A CN  
>  T CN  
>  CAE CN  
>  MFI CN  
>  CNR CN  
>  CP CN  
>  CTC/A CN  
>  RUS CN  
>  FTT CN  
>  IMO CN  
>  ENB CN  
>  L CN  
>  MG CN  
>  K CN

FWIW, in Yahooland. the **CN** ones map to **.TO** usually; I haven’t gotten far enough to to see if the list contains any Vancouver exchange listings.

---

### Post #8 — **arbitrage** | 2021-04-20 18:54 UTC _(reply to #7)_

at the time of my mapping, CA was indeed the correct exchange code. Liam has since updated a lot of the mapping in the ‘official’ mapping file, though.

---

### Post #9 — **gammarat** | 2021-04-20 21:00 UTC _(reply to #8)_

I saw that and figured there was probably some Bloomberg quirkiness going on. I always associated “CN” mentally with China, and it struck me as odd as I scrolled through the “latest” file to see all these stocks I’ve enjoyed losing money for years on as being Chinese. ![:grinning_face_with_smiling_eyes:](http://forum.numer.ai/images/emoji/twitter/grinning_face_with_smiling_eyes.png?v=9)
