---
title: "R Download and Submit Super Massive Data"
category: Tournament
url: https://forum.numer.ai/t/r-download-and-submit-super-massive-data/4099
created_at: 2021-09-12T14:05:17.338000+00:00
last_posted_at: 2021-09-20T22:44:32.831000+00:00
posts_count: 9
views: 1698
tags: []
---

# R Download and Submit Super Massive Data

---

### Post #1 — **of_s** | 2021-09-12 14:05 UTC

For any R users not on the #cran channel in RocketChat, I have posted updated functionality to the Rnumerai routines for downloading and submitting both the legacy and new datasets.

The data downloading updates can be found here:  
<https://github.com/Omni-Analytics-Group/Rnumerai/issues/35>

The submission updates can be found here:  
<https://github.com/Omni-Analytics-Group/Rnumerai/issues/36>

Please suggest any improvements or report any issues, thanks!

**EDIT:`diagnostics` upload now available**  
**EDIT (9/29):`old_data_new_val.parquet` download added and `source` added to submissions**

---

### Post #2 — **jrb** | 2021-09-15 19:47 UTC

[@of_s](</u/of_s>) Thanks for unblocking all our fellow R users in the community, on being able to use the new super massive dataset. The Council of Elders has awarded you a 10 NMR discretionary retroactive [bounty](<https://etherscan.io/tx/0xc0c3495bd833d77c10bc83bc3d45bbc43fbf3db1e06c3d9440149a13d49c7045>) for your work on this. Keep it coming!

---

### Post #3 — **of_s** | 2021-09-15 19:58 UTC _(reply to #2)_

Thanks CoE, I hope more R users participate!

The popularity of this post made me realize that I should post the fast R yahoo finance data download routine as well as the transformation from long to wide for Signals, which I did here (previously tucked away in the #cran channel in RC):

![](http://forum.numer.ai/user_avatar/forum.numer.ai/of_s/48/2627_2.png) [R yahoo! Finance Download for Signals Universe](<http://forum.numer.ai/t/r-yahoo-finance-download-for-signals-universe/4126>) [Signals](</c/signals/10>)

> I had shared this download routine in RocketChat but figured it should be shared here as well. The resulting Signals_data list is in long format, so depending on your preferences, you can convert it to a data.frame of returns (and volumes). Whole process takes < 10 min on 7 cores. library(BatchGetSymbols) first.date <\- Sys.Date()-365 last.date <\- Sys.Date() map <\- read.csv('https://numerai-signals-public-data.s3-us-west-2.amazonaws.com/signals_ticker_map_w_bbg.csv') # Used to have missing sy…

---

### Post #4 — **javibear** | 2021-09-20 04:39 UTC

Hi thanks for doing this. I’m still getting the error: “Error in handle_url(handle, url, …) : Must specify at least one of url or handle”. don’t know what’s going on…

---

### Post #5 — **of_s** | 2021-09-20 10:49 UTC _(reply to #4)_

Hi [@javibear](</u/javibear>), there’s a couple of possibilities: libraries **`httr`** and **`lubridate`** need to be installed, and the correct **`model_id`** parameter needs to be used in **`submit_predictions()`**.

You can view your **`model_id`** from the **`get_models()`** call or alternatively view each ID via <https://numer.ai/models> .

LMK if any of these solutions work! Also, you can follow the discussions on the #cran channel in RC [here](<https://community.numer.ai/channel/cran>).

---

### Post #6 — **javibear** | 2021-09-20 16:03 UTC _(reply to #5)_

[@of_s](</u/of_s>) no luck. re-installed httr,lubridate. Still getting the error. by the way, I’m getting this message on download_data(). This started to happen just all of a sudden about 4 weeks ago, even before the super massive data intro.

---

### Post #7 — **of_s** | 2021-09-20 16:08 UTC _(reply to #6)_

[@javibear](</u/javibear>) And you are using this **`download_data()`** version (<https://github.com/Omni-Analytics-Group/Rnumerai/issues/35>) saved locally **after** loading **`Rnumerai`**?

---

### Post #8 — **javibear** | 2021-09-20 21:35 UTC _(reply to #7)_

[@of_s](</u/of_s>) my reply in rc:  
javibear  
2:29 PM  
yes, did all those. tried writing the function directly onto the main script but no luck as well. from the error, it seems to functionally working and then it hits a walll or something. `Downloading Data...numerai_live_data_int8.parquet Error in handle_url(handle, url, ...) : Must specify at least one of url or handle`

---

### Post #9 — **of_s** | 2021-09-20 22:44 UTC _(reply to #8)_

Just in case someone else runs into similar issue, having the latest version of `Rnumerai (>=2.1.3)` installed resolved this as noted in RC:

![](https://community.numer.ai/channel/cran/assets/favicon_16.png) [community.numer.ai](<https://community.numer.ai/channel/cran?msg=PAaWt67k6teCwYgvu>) ![](https://community.numer.ai/channel/cran/assets/favicon_512.png)

### [Numerai Community](<https://community.numer.ai/channel/cran?msg=PAaWt67k6teCwYgvu>)

Thanks!
