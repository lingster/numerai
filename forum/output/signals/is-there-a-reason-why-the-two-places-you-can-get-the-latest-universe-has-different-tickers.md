---
title: "Is there a reason why the two places you can get the latest universe has different tickers?"
category: Signals
url: https://forum.numer.ai/t/is-there-a-reason-why-the-two-places-you-can-get-the-latest-universe-has-different-tickers/3218
created_at: 2021-05-05T05:28:45.605000+00:00
last_posted_at: 2021-06-04T20:06:19.326000+00:00
posts_count: 9
views: 966
tags: []
---

# Is there a reason why the two places you can get the latest universe has different tickers?

---

### Post #1 — **asteeber** | 2021-05-05 05:28 UTC

If you go to the [Numerai Signals Tournament page](<https://signals.numer.ai/tournament>) you can click “Download Latest Universe” which has the AWS endpoint:

`https://numerai-signals-public-data.s3-us-west-2.amazonaws.com/example_predictions/latest.csv`

But if you go to the [Numerai Signals Overview page](<https://docs.numer.ai/numerai-signals/signals-overview>) and click “latest universe file” it has a different endpoint:

`https://numerai-signals-public-data.s3-us-west-2.amazonaws.com/universe/latest.csv`

I loaded both csv’s in R and I got the following results:
    
    
    > tickers_from_tournament <- c(unique(universe_from_tournament$bloomberg_ticker))
    > tickers_from_overview <- c(unique(universe_from_overview$bloomberg_ticker))
    > length(tickers_from_tournament)
    [1] 4764
    > length(tickers_from_overview)
    [1] 5433
    

It looks like the universe from the docs page is correct and the one from the tournament page is not correct. I understand that the tournament page endpoint is an example signal submission but shouldn’t that example include _all_ of the tickers in the current universe?

---

### Post #2 — **chaotician** | 2021-05-31 09:33 UTC

Yes, this is confusing. They also change from bloomberg_ticker to numerai_ticker, prediction to signal recently on submission example. This really messes up proper mapping most specially if we are incorporating from different data sources. I know it is still a big work in progress but I hope they have better revision management/messaging and up to date consistent links to its universe / targets.

---

### Post #3 — **joakim** | 2021-06-01 09:39 UTC

Can this be fixed please LiamHz or EasyMikeP aka [@master_key](</u/master_key>) ? ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=9)

---

### Post #4 — **_liamhz** | 2021-06-04 17:30 UTC

Thanks for reporting this! The link on the tournament page pointed to a no longer updated universe file, this has been corrected to point to the same universe linked to in the docs.

---

### Post #5 — **_liamhz** | 2021-06-04 17:30 UTC _(reply to #2)_

> They also change from bloomberg_ticker to numerai_ticker, prediction to signal recently on submission example. This really messes up proper mapping

The example may have changed, but you should still be able to make Signals submissions with the columns bloomberg_ticker and prediction (or just rename the new columns to what they were previously)

---

### Post #6 — **asteeber** | 2021-06-04 17:46 UTC _(reply to #4)_

Awesome thanks! Is this perhaps worthy of a bounty? ![:eyes:](http://forum.numer.ai/images/emoji/twitter/eyes.png?v=9)

0x0000000000000000000000000000000000022041

---

### Post #7 — **_liamhz** | 2021-06-04 17:57 UTC _(reply to #6)_

Yep! I’ll send a small bounty in NMR stake credits to your account. Is asteeber the account you’d like me to send it to?

---

### Post #8 — **asteeber** | 2021-06-04 18:29 UTC _(reply to #7)_

Yes, thank you so much! NumerAI is awesome!

---

### Post #9 — **chaotician** | 2021-06-04 20:06 UTC _(reply to #7)_

What about me? ![:pray:](http://forum.numer.ai/images/emoji/twitter/pray.png?v=9) ![:pray:](http://forum.numer.ai/images/emoji/twitter/pray.png?v=9) ![:pray:](http://forum.numer.ai/images/emoji/twitter/pray.png?v=9)Hahaha!
