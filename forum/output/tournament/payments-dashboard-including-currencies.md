---
title: "Payments dashboard including currencies"
category: Tournament
url: https://forum.numer.ai/t/payments-dashboard-including-currencies/5157
created_at: 2022-03-28T12:05:47.346000+00:00
last_posted_at: 2022-12-23T12:57:12.714000+00:00
posts_count: 20
views: 2011
tags: []
---

# Payments dashboard including currencies

---

### Post #1 — **quantized** | 2022-03-28 12:05 UTC

Hey folks, I’ve made a dashboard showing payouts by round with a few popular currencies. You can select model(s), currency and a date range. Any feedback much appreciated. Currently supports classic tournament only.

<http://numerai-payouts.herokuapp.com/>

Note: this is currently running on a free Heroku plan so may take a few seconds to load.

---

### Post #2 — **by256** | 2022-03-28 12:19 UTC

Thanks! This is great for tracking payouts in fiat currencies. FYI, the ‘Download CSV’ button doesn’t download the data for the model I’m currently viewing though.

---

### Post #3 — **quantized** | 2022-03-28 12:22 UTC

[@by256](</u/by256>) thanks for the feedback, can you let me know the model, currency and date range so I can try to reproduce?

---

### Post #4 — **by256** | 2022-03-28 12:24 UTC _(reply to #3)_

by1024, GBP, 26/10/21 → 31/03/22

---

### Post #5 — **quantized** | 2022-03-28 12:44 UTC _(reply to #4)_

Thanks, I think this an issue with using limited resources on free Heroku. I’ve disabled downloads for the time being.

---

### Post #6 — **aventurine** | 2022-03-28 19:22 UTC

Great work on this! How long did this take to build? Maybe I can take this back to the CoE for a possible retro bounty if interested?

---

### Post #7 — **quantized** | 2022-03-28 19:59 UTC _(reply to #6)_

Thank you, it took 2 days. Yes, happy to be considered for a retro bounty ![:+1:](http://forum.numer.ai/images/emoji/twitter/+1.png?v=10)

---

### Post #8 — **aventurine** | 2022-03-28 20:13 UTC _(reply to #7)_

Are you able to break it down into hours working on it?

---

### Post #9 — **quantized** | 2022-03-28 20:15 UTC _(reply to #8)_

5 hours yesterday, 5 today, so 10 total.

---

### Post #10 — **quantized** | 2022-03-31 13:22 UTC

The issue with CSV downloading has been fixed and re-enabled.  
Coming soon: Support for signals models.

---

### Post #11 — **quantized** | 2022-04-02 08:34 UTC

Renamed to Numerai Earnings so as not to cause confusion with the existing payouts app.  
<https://numerai-earnings.herokuapp.com/>

---

### Post #12 — **aventurine** | 2022-04-04 17:56 UTC _(reply to #11)_

Please DM me on rocketchat a wallet address. Retro bounty will be queued up ![:man_dancing:](http://forum.numer.ai/images/emoji/twitter/man_dancing.png?v=10)

---

### Post #14 — **quantized** | 2022-09-27 21:15 UTC

Signals models now added on <https://numerai-earnings.herokuapp.com/>  
Any issues with using this dashboard, please let me know.

---

### Post #15 — **noobdev** | 2022-09-27 21:20 UTC _(reply to #14)_

The link in your initial post doesn’t work anymore ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=12)

---

### Post #16 — **quantized** | 2022-09-29 20:15 UTC

New location at <https://nmrearn.com/>

---

### Post #17 — **quantized** | 2022-11-15 11:45 UTC

Update: added BTC, CNY, ETH, INR, JPY, KRW, RUB.

---

### Post #18 — **rareprecious** | 2022-12-15 19:31 UTC _(reply to #17)_

[@quantized](</u/quantized>) thanks for the app. I have been trying to generate a report but it is not responding at all. It seems something is broken. For a single model for only Dec 22 but no data for the past hour.

Please, can you also add this feature… a “processing bar” signal or hour glass or something… to inform the user that the report is being generated.

Thanks.

---

### Post #19 — **quantized** | 2022-12-21 14:04 UTC _(reply to #18)_

Thanks for the feedback. The error is now fixed, and I’ve added a loading element which should appear when the dashboard is retrieving the data. Please let me know if you have any further issues. You can also raise github issues here: [Issues · mikedbjones/numerai-earnings · GitHub](<https://github.com/mikedbjones/numerai-earnings/issues>)

---

### Post #20 — **rareprecious** | 2022-12-23 12:31 UTC _(reply to #19)_

Thanks, it seems like Numerai queries work but Signals queries do not work. Sorry mate, still some bugs hanging in there.

---

### Post #21 — **quantized** | 2022-12-23 12:57 UTC _(reply to #20)_

Ok, I volunteer my time on this so don’t expect a fix imminently.
