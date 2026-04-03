---
title: "Daily tournament"
category: Tournament
url: https://forum.numer.ai/t/daily-tournament/5772
created_at: 2022-10-22T09:07:28.662000+00:00
last_posted_at: 2022-10-26T21:08:44.554000+00:00
posts_count: 17
views: 1481
tags: []
---

# Daily tournament

---

### Post #1 — **stochastic_geometry_1** | 2022-10-22 09:07 UTC

Opening time is approximately 13.0 UTC? What time should we submit? With a 1 hour window we need to know exactly

---

### Post #2 — **nasdaqjockey** | 2022-10-22 13:34 UTC

Slyfox — I’m not sure I understand the “70/30”. Does that mean the payout threshold for Saturday will eventually be ~210K NMR and all the week days will be ~ 90K NMR combined (22.5K NMR/day)?

---

### Post #3 — **dzheng1887** | 2022-10-22 16:31 UTC

I feel the comment that the payouts/burns will come faster because of continuous compounding to be a bit disingenuous. It is already compounding on a weekly level. I do not think daily compounding will provide sufficient benefits to offset numeraire price risk and numerai tournament return risk much less the work required for daily submissions.

2% return per week for 52 weeks compounds to 1.02^52 = 2.800  
2% return per week for 260 days compounds to (1+.02/5)^(52*5) = 2.823

You get about 1 extra week of payments if compounding daily over a year. Yes, perhaps over 10 years it’ll be much different though. Also didn’t consider if the return varies much each week and very roughly ignored the 70/30 split.

---

### Post #4 — **jay1100** | 2022-10-24 09:04 UTC _(reply to #3)_

I thought the same: Daily rounds will not significantly increase compounding compared to weekly rounds. This seems indeed a bit disingenuous.

---

### Post #5 — **kayeffnumeraitor** | 2022-10-24 13:06 UTC

![](http://forum.numer.ai/user_avatar/forum.numer.ai/stochastic_geometry_1/48/3013_2.png) stochastic_geometry_1:

> Opening time is approximately 13.0 UTC? What time should we submit? With a 1 hour window we need to know exactly

At first I didn’t get the question, but this is a valid one. Somewhere on rocketchat it was stated that because the data generating pipeline obviously depends on data providers it might happen that they are late with their data. The idea is to get away from scheduled “cron-like” submission and be more like submission on demand. So once numerai has their data, which is (as I understood it) no earlier than 13:00 UTC, you have a one hour time window to submit. That is why they want the webhook trigger mechanism, because at another day it may happen that data is ready at 13:20 UTC, so they will trigger the webhook at 13:20 and then you have time until 14:20. You can still have a cronjob starting a script that polls for new round starting at 13:00 UTC if a webhook mechanism is too much of a hassle.

---

### Post #6 — **stochastic_geometry_1** | 2022-10-24 18:32 UTC _(reply to #5)_

Thanks. So I really do have to master numerai compute. I will give it another go.

---

### Post #7 — **aqsmith08** | 2022-10-24 18:34 UTC _(reply to #2)_

I asked the same thing on Rocketchat. Here’s the response from Slyfox:

_so for classic, right now its 300K threshold for Saturday and 0 for weekdays. the target would be about 210K for Saturday and 90/4 for each weekday. Something like that. Basically we are aiming for the outcome “if someone wants to continue only submitting once a week, they would get about 70% of what they would have if they submitted daily”_

You can find more Q&A on the #General channel on Rocketchat.

---

### Post #8 — **kayeffnumeraitor** | 2022-10-25 08:39 UTC _(reply to #6)_

So you don’t actually have to, I have exchanged my cron job with a very ugly coded “stolen from the internet” imap listener running on a raspberry pi waiting for the numerai “round open” mail and starting my main computer to run the predictions if said mail arrives.  
In the end the only thing you care about is that you find a way to automatically handle a “round open” signal. If the numerai mail is not reliable there a ways to “translate” webhook trigger to mail (like with [IFTTT](<https://ifttt.com/explore>) for example).

If you ask why so much hassle the reason is cloud compute power can be expensive if your models are more power hungry than your standard LGBM/XGBoost predictor, especially if you want to retrain on the fly. With my current numerai earnings those bills would probably be not covered, and my risk tolerance is not high enough to stake a years worth of savings on my models, at least not for now.

---

### Post #9 — **mlinux** | 2022-10-25 14:22 UTC

My old pipeline is using the numerai_tournament_data.parquet for live predictions and the md5sum for today’s daily data was identical to what was released this past weekend. Should I be switching to the live dataset?

$ md5sum 2022-10-22/numerai_tournament_data.parquet  
6a6eccb8d316bb4b244fb06d68f44adb 2022-10-22/numerai_tournament_data.parquet

$ md5sum 2022-10-25/numerai_tournament_data.parquet  
6a6eccb8d316bb4b244fb06d68f44adb 2022-10-25/numerai_tournament_data.parquet

---

### Post #10 — **slyfox** | 2022-10-25 14:33 UTC _(reply to #9)_

[@mlinux](</u/mlinux>) yeah you should switch to downloading the `live_data` files which is much smaller.

the `tournament_data` file is sort of a legacy file since that still includes the test_eras which we already gave out as training data.

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/8/8ea63aa34aab1e1f914cc24b44f3b92df9a19552_2_537x500.png)image1028×956 120 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/8/8ea63aa34aab1e1f914cc24b44f3b92df9a19552.png> "image")

---

### Post #11 — **anonai** | 2022-10-25 19:06 UTC

So if I’m understanding correctly, the daily tournaments will cause less payout for the weekly tournaments eventually? For those who only want to participate on Saturday can we please not be affected by this? It is almost impossible for some people to particiapte with a one hour window during the week with full time jobs etc. I care about my stake in the weekly tournment and don’t think the payout should be affected by the addition of daily tournaments.

---

### Post #14 — **autratec** | 2022-10-26 01:59 UTC _(reply to #3)_

assuming we are still trying to predict the market performance 4 weeks later, so the new annual shouldn’t be:

1.02^(52*5) ?

---

### Post #15 — **dzheng1887** | 2022-10-26 02:34 UTC _(reply to #14)_

I think the payout factor is adjusted so the additive weekly return is still 0.02. If they didn’t, then yes I think the returns would 5x which would be cool (or suck if you had burns)

---

### Post #16 — **autratec** | 2022-10-26 03:20 UTC _(reply to #15)_

as long as we are building a model with winning ratio little higher than losing, and prediction period is still 4 weeks, which normally leads to higher return or lose, get minor positive daily compound will be a good business model to most of us ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=12)

---

### Post #17 — **liborty** | 2022-10-26 04:15 UTC _(reply to #12)_

I am getting some uploads going now via Python3 script. Pity it does not work from numerapi CLI.

---

### Post #18 — **mlinux** | 2022-10-26 13:37 UTC

I started doing this daily rounds thinking that “If you do want to participate in the new rounds, then you can use the same data and submissions API to run your daily model pipeline. And if you are already automated with Numerai Compute, then you can simply enable daily triggers on the models page of the website.” However, for the signals competition I found that I did need to make one code change when using the opensignals data provider. Specifically, I found that the get_ticker_missing function (github link below) assumes that you will be running this code only for weekend uploads. Luckily, the function does have an optional argument where you can pass in today’s date to get the correct functionality for during the week. Furthermore, if you are using the download_data function, it does not currently have this optional argument to pass in so I had to code a bit around this in order to to get the correct date to get_ticker_missing.

[github.com](<https://github.com/councilofelders/opensignals/blob/master/src/opensignals/data/provider.py#L58>)

#### [councilofelders/opensignals/blob/master/src/opensignals/data/provider.py#L58](<https://github.com/councilofelders/opensignals/blob/master/src/opensignals/data/provider.py#L58>)
    
    
          
    
    
              
        48.     })
    
              
        49.     if len(list(db_dir.rglob('*.parquet'))) > 0:
    
              
        50.         ticker_data = pd.read_parquet(db_dir)
    
              
        51. 
                   
    
    
        52.     num = ticker_data.bloomberg_ticker.unique().shape[0]
    
              
        53.     logger.info(f'Retrieving data for {num} tickers from the database')
    
              
        54. 
                   
    
    
        55.     return ticker_data
    
              
        56. 
                   
    
    
        57. @staticmethod
    
              
        58. def get_ticker_missing(ticker_data: pd.DataFrame,
    
              
        59.                        ticker_map: pd.DataFrame,
    
              
        60.                        last_friday: Optional[dt.datetime] = None) -> pd.DataFrame:
    
              
        61.     if last_friday is None:
    
              
        62.         last_friday = dt.datetime.today() - relativedelta(weekday=FR(-1))
    
              
        63.     tickers_available_data = ticker_data.groupby('bloomberg_ticker').agg({'date': [max, min]})
    
              
        64.     tickers_available_data.columns = ['date_max', 'date_min']
    
              
        65. 
                   
    
    
        66.     eligible_tickers_available_data = ticker_map.merge(
    
              
        67.         tickers_available_data.reset_index(),
    
              
        68.         on='bloomberg_ticker',

---

### Post #19 — **dzheng1887** | 2022-10-26 21:08 UTC _(reply to #16)_

For sure it does ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=12) I guess I was just complaining about having to set up something to monitor for daily data releases or just always be ready for that 1 hour window and the benefit of a slightly more continuous compounding doesn’t really seem to be that exciting when I have to put my attention elsewhere too.

I understand why they need to do it though, of course, they have business needs to survive and thrive, but it doesn’t seem like we would really benefit as much from this change as perhaps the hedge fund thinks they would.
