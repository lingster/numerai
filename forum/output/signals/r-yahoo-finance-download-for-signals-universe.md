---
title: "R yahoo! Finance Download for Signals Universe"
category: Signals
url: https://forum.numer.ai/t/r-yahoo-finance-download-for-signals-universe/4126
created_at: 2021-09-15T17:46:58.348000+00:00
last_posted_at: 2021-10-05T23:49:43.153000+00:00
posts_count: 8
views: 1273
tags: []
---

# R yahoo! Finance Download for Signals Universe

---

### Post #1 — **of_s** | 2021-09-15 17:46 UTC

I had shared this download routine in RocketChat but figured it should be shared here as well. The resulting `Signals_data` list is in long format, so depending on your preferences, you can convert it to a data.frame of returns (and volumes).

Whole process takes < 10 min on 7 cores.
    
    
    library(BatchGetSymbols)
    first.date <- Sys.Date()-365
    last.date <- Sys.Date()
    
    map <- read.csv('https://numerai-signals-public-data.s3-us-west-2.amazonaws.com/signals_ticker_map_w_bbg.csv')
    # Used to have missing symbols in the yahoo map
    map <- map[-which(map$yahoo==""),]
    
    start.time <- Sys.time()
    
    future::plan(future::multisession, workers = floor(parallel::detectCores()-1))
    
    Signals_data <- BatchGetSymbols(tickers = map$yahoo,
                                    first.date = first.date,
                                    last.date = last.date, 
                                    do.parallel = TRUE)
    
    print(Sys.time() - start.time)
    
    # Reshape returns from long to wide
    Returns <- reshape2::dcast(data.frame(Signals_data$df.tickers[,7:9]), ref.date~ticker , value.var = "ret.adjusted.prices",fun.aggregate = sum)
    rownames(Returns) <- Returns[,1]
    Returns <- Returns[,-1]
    
    
    # Reshape volume from long to wide
    Volume <- reshape2::dcast(Signals_data$df.tickers[,c(5,7,8)], ref.date~ticker , value.var = "volume",fun.aggregate = sum)
    rownames(Volume) <- Volume[,1]
    Volume <- Volume[,-1]
    colnames(Volume) <- colnames(Returns)

---

### Post #2 — **aqsmith08** | 2021-10-04 22:52 UTC

Hey - I might be doing something wrong but I can’t get `BackGetSymbols` to be assigned to Signals_data. I think it’s due to this error: `Error: Can't combine `…1$price.open`<double> and`…1910$price.open` <character>.`

Here’s what I’m doing:
    
    
    Signals_data <- BatchGetSymbols(tickers = map$yahoo,
                                    first.date = first.date,
                                    last.date = last.date, 
                                    do.parallel = TRUE)
    

It results in this:
    
    
    < get a ton of 'looking good' messages >
    TNK | yahoo (5197|5197) | Found cache file - Got 100% of valid prices | Nice!Error: Can't combine `..1$price.open` <double> and `..1910$price.open` <character>.
    Run `rlang::last_error()` to see where the error occurred.
    

Then I run the two error commands to get more details and I see:
    
    
    > rlang::last_error()
    <error/vctrs_error_incompatible_type>
    Can't combine `..1$price.open` <double> and `..1910$price.open` <character>.
    Backtrace:
     1. BatchGetSymbols::BatchGetSymbols(...)
     2. dplyr::bind_rows(purrr::map(my.l, 1))
     3. vctrs::vec_rbind(!!!dots, .names_to = .id)
     5. vctrs::vec_default_ptype2(...)
     6. vctrs::stop_incompatible_type(...)
     7. vctrs:::stop_incompatible(...)
     8. vctrs:::stop_vctrs(...)
    Run `rlang::last_trace()` to see the full context.
    > rlang::last_trace()
    <error/vctrs_error_incompatible_type>
    Can't combine `..1$price.open` <double> and `..1910$price.open` <character>.
    Backtrace:
        █
     1. └─BatchGetSymbols::BatchGetSymbols(...)
     2.   └─dplyr::bind_rows(purrr::map(my.l, 1))
     3.     └─vctrs::vec_rbind(!!!dots, .names_to = .id)
     4.       └─(function () ...
     5.         └─vctrs::vec_default_ptype2(...)
     6.           └─vctrs::stop_incompatible_type(...)
     7.             └─vctrs:::stop_incompatible(...)
     8.               └─vctrs:::stop_vctrs(...)
    

Have you hit this error before where it seems like `price.open` is being returned as a `double` and a `character`? Any idea how to avoid this error?

Thanks! ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=9)

---

### Post #3 — **of_s** | 2021-10-04 23:32 UTC _(reply to #2)_

Thanks for the feedback! I just ran it without error and my number of symbols was 5288, ultimately resulting in 5176 complete returns. I’m not sure where the discrepancy lies except for the `map <-` download from Numer.ai…

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/6/674701b9ad366878374556d6434da178fd6606cb_2_690x258.png)image1689×632 33.5 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/6/674701b9ad366878374556d6434da178fd6606cb.png> "image")

Downloading messages I received:

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/2/2a64fd27f081db70a78a312905c8c962b8eda9a3_2_690x317.png)image1884×866 82.3 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/2/2a64fd27f081db70a78a312905c8c962b8eda9a3.png> "image")

Resulting `Returns` and `Volume` data.frames:

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/7/763c0bb6f4ec1a8cffa707d180e229762b74d47e.png)image1893×433 31.6 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/7/763c0bb6f4ec1a8cffa707d180e229762b74d47e.png> "image")

---

### Post #4 — **aqsmith08** | 2021-10-05 14:15 UTC _(reply to #3)_

Hey - Thanks for your response! Let me poke around on my side and I’ll see if I can 1) figure it out or 2) come up with a reproducible example. Thanks for creating the package as I hope to use it once I get it working! ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=9)

---

### Post #5 — **of_s** | 2021-10-05 14:20 UTC _(reply to #4)_

YW! Also, I typically break down the downloads into US and Foreign tickers so it’s easier to spot issues.

---

### Post #6 — **aqsmith08** | 2021-10-05 22:47 UTC

Good news! After I updated all of my R packages, the error went away, and I now have it working. ![:+1:](http://forum.numer.ai/images/emoji/twitter/+1.png?v=9)

My only “nit” is that the file runs every time that I save it. I suspect that the `source` function gets called because of the:

`future::plan(future::multisession, workers = floor(parallel::detectCores()-1))`

line but I was too lazy to poke into it. I figured that once my script was good (aka working and scheduled with cron), I wouldn’t need to worry about saving it and having it run. Thanks again for posting this in the forum!

---

### Post #7 — **of_s** | 2021-10-05 23:02 UTC _(reply to #6)_

That’s great news!

BTW, you may have “Source on Save” enabled  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/1/1e2e9dffd58e009e34a56993cc0c01c8414ea41c.png)image414×236 24.8 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/1/1e2e9dffd58e009e34a56993cc0c01c8414ea41c.png> "image")

---

### Post #8 — **aqsmith08** | 2021-10-05 23:49 UTC

I’m not worthy! I’m not worthy! ![:wink:](http://forum.numer.ai/images/emoji/twitter/wink.png?v=9) That fixed it. Thanks again!
