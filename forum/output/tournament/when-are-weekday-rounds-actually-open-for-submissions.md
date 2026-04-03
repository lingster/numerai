---
title: "When are weekday rounds actually open for submissions?"
category: Tournament
url: https://forum.numer.ai/t/when-are-weekday-rounds-actually-open-for-submissions/5905
created_at: 2022-12-02T13:10:16.553000+00:00
last_posted_at: 2023-01-12T15:58:15.468000+00:00
posts_count: 19
views: 1706
tags: []
---

# When are weekday rounds actually open for submissions?

---

### Post #1 — **sentientai** | 2022-12-02 13:10 UTC

The [tournament overview page](<https://docs.numer.ai/tournament/learn#submissions>) says weekday tournaments should open at UTC 13:00 and close in 1 hour, but it doesn’t seem like that was the case yesterday or today. It’s 13:08 and trying to download the latest tournament data returns the error `ERROR numerapi.base_api: Current round not open for submissions`. Yesterday (Thursday, Dec 1) it seemed like it was open until 14:50 UTC. Have the submission/round times changed for weekday tournaments?

---

### Post #2 — **autratec** | 2022-12-02 13:16 UTC

Facing same issue. The daily round open now based upon email trigger, not fixed schedule.

---

### Post #3 — **kayeffnumeraitor** | 2022-12-02 14:47 UTC _(reply to #2)_

Unfortunately, the numerai docs are misleading and should make it clear that the daily rounds opens **no earlier than** UTC 13:00. The round opens when the Numerai data vendors submitted their data and Numerai itself has finished the data preprocessing. If any of them are late for whatever reason, the round opens later.

This leaves you with 4 options:

  * Keep polling for a new round after 13:00 UTC and start your prediction pipeline once it is open (Currently there seems to be a bug with the round open check function though)
  * Use Numerai Compute (gets triggered via webhook)
  * Find your own way to trigger your prediction pipeline via the webhook
  * Submit only weekly predictions which are easily schedulable

---

### Post #4 — **sunkay** | 2022-12-02 20:45 UTC _(reply to #3)_

Will numerai provide round start listener API?

---

### Post #5 — **kayeffnumeraitor** | 2022-12-03 08:07 UTC _(reply to #4)_

I’m not sure what you mean by “listener api”. What you can do is to select one of your models on the model overview page, select “compute” and enter your desired webhook address. Whenever a new round starts, Numerai will send a JSON similar to the following:
    
    
    {
        "roundNumber": 368,
        "dataVersion": 1,
        "triggerId": "01234567-89ab-cdef-0123-4567890abcde"
    }

---

### Post #6 — **autratec** | 2022-12-07 00:20 UTC _(reply to #5)_

Any one tried to connect this message with any messaging tool, like telegram or WhatsApp?

---

### Post #7 — **degerhan** | 2022-12-07 02:11 UTC _(reply to #6)_

That’s an interesting idea [@autratec](</u/autratec>) – haven’t tried it but this looks promising: [Webhooks works better with IFTTT](<https://ifttt.com/maker_webhooks>) \+ <https://ifttt.com/telegram> (looks like ifttt free tier should be sufficient).

---

### Post #8 — **autratec** | 2022-12-07 03:58 UTC _(reply to #7)_

hi, thanks for the positive response. i am still trying to connect dot. some further thoughts, will be:

  1. create a chatbot in telegram. and get token.
  2. setup a url with token and message and setup in Numerai compute



every time, when numerai call that url for new round submission, i will get a new message from my chatbot under telegram.

And here are some new thoughts of using IFTTT and webhook:

![](https://web-assets.ifttt.com/packs/media/shared/favicon-52685f5f6a9fa84b597b.svg) [IFTTT](<https://ifttt.com/maker_webhooks/details>) ![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/8/84d12ad7f1ddbf92adaf9ce7686287792a610989.webp)

### [Webhooks's triggers, queries, and actions - IFTTT](<https://ifttt.com/maker_webhooks/details>)

Learn the building blocks for how Webhooks can connect to hundreds of other services. Learn to use webhooks and integrate other services on IFTTT with you...

Using trigger from IFTTT based on webhooks from numerai, and connect with telegram message.

---

### Post #9 — **autratec** | 2022-12-07 04:36 UTC

More sharing from chatGPT:

[![Screenshot_20221207_123345_Chrome](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/7/78fb1be19e169f84b09ec570c3275ea1f44146c8_2_236x500.jpeg)Screenshot_20221207_123345_Chrome1080×2280 235 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/7/78fb1be19e169f84b09ec570c3275ea1f44146c8.jpeg> "Screenshot_20221207_123345_Chrome")

  


[![Screenshot_20221207_123338_Chrome](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/a/aedd6fb05e4bd46af6bf5900c54fad0d4bb6194e_2_236x500.jpeg)Screenshot_20221207_123338_Chrome1080×2280 254 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/a/aedd6fb05e4bd46af6bf5900c54fad0d4bb6194e.jpeg> "Screenshot_20221207_123338_Chrome")

  


[![Screenshot_20221207_123327_Chrome](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/c/ce8037ed83a0f71beb822d1d499f0e33e0440801_2_236x500.jpeg)Screenshot_20221207_123327_Chrome1080×2280 256 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/c/ce8037ed83a0f71beb822d1d499f0e33e0440801.jpeg> "Screenshot_20221207_123327_Chrome")

---

### Post #10 — **autratec** | 2022-12-07 10:16 UTC

i have done some setup with IFTTT and looks work well between Numerai and Telegram. Here are the steps:

  1. apply telgram account.
  2. apply IFTTT account. using free service tier with 5 connections.
  3. using object - webhook: If received and web request with JSON payload. Then send Telegram message
  4. Received url below: <https://maker.ifttt.com/trigger/EVENTNAME/with/key/TOKENID>
  5. setup url in model/compute



test it and working fine. now after the message being received from numerai in telegram, i can manually click the notebook running, which is better than before.

---

### Post #11 — **kayeffnumeraitor** | 2022-12-07 13:06 UTC _(reply to #10)_

If you are doing this just to get notified so that you can upload manually then you could have just waited for the numerai round open mail though.

---

### Post #12 — **autratec** | 2022-12-07 13:19 UTC _(reply to #11)_

I don’t proactively check email. Messaging tool is more real time. Might explore API trigger notebook execution as next step.

---

### Post #13 — **taori** | 2022-12-07 14:19 UTC _(reply to #5)_

[@kayeffnumeraitor](</u/kayeffnumeraitor>) thanks for sharing. I was looking for the webhook API details so that I can configure a webhook server on my machine, but I couldn’t find the documentation. Do you know if there is one? Or did you find out about the API call by checking on your registered webhook machine how the data passed by numerai?

---

### Post #14 — **kayeffnumeraitor** | 2022-12-07 15:52 UTC _(reply to #13)_

Back then I was also looking for documentation, but havent found one and in the end I don’t actually care what is sent in the JSON file, I just want to reliably be informed when a new round opened.

I followed the same steps regarding IFTTT that [@autratec](</u/autratec>) mentioned

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/a/6bbea6/48.png) autratec:

>   * apply IFTTT account. using free service tier with 5 connections.
>   * using object - webhook: If received and web request with JSON payload.
> 


The action I registered on IFTTT is “send me an email” with the JSON payload attached. The JSON I posted above is one of these mails with an obfuscated triggerId (don’t know if this Id is sensitive or not).

---

### Post #16 — **autratec** | 2022-12-08 04:57 UTC _(reply to #15)_

hi all, i have creates a telegram channel to publish and receive notification of daily submission.

![](https://telegram.org/img/website_icon.svg?4) [Telegram](<https://t.me/numeraidaily>) ![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/f/f1be713231a12acdfae4d71909ac80c166f67896.jpeg)

### [Numerai Daily](<https://t.me/numeraidaily>)

Provide open notification of NUMERAI daily prediction submission window.

---

### Post #17 — **markdamon90** | 2023-01-08 17:56 UTC _(reply to #9)_

Dude this chatgpt is great and works like charm

---

### Post #18 — **mundan** | 2023-01-12 01:46 UTC _(reply to #3)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/kayeffnumeraitor/48/991_2.png) kayeffnumeraitor:

>   * Keep polling for a new round after 13:00 UTC and start your prediction pipeline once it is open (Currently there seems to be a bug with the round open check function though)
> 


Does this work nicely?

---

### Post #19 — **kayeffnumeraitor** | 2023-01-12 14:37 UTC _(reply to #18)_

As I am not doing it, I can’t tell, but, as always with api requests, they eventually will fail (network overload, server error, internet connection lost, etc… ), so you should implement a try / except / retry mechanism around it if you want it to be robust.

---

### Post #20 — **gammarat** | 2023-01-12 15:58 UTC _(reply to #18)_

![](https://avatars.discourse-cdn.com/v4/letter/m/7993a0/48.png) mundan:

> Does this work nicely?

Yes, it does. There’s a useful example in Python if you need it, at this post:

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/forum.numer.ai/svendaj/48/3285_2.png) [Server Errors on Friday](<http://forum.numer.ai/t/server-errors-on-friday/5883/5>) [Tournament](</c/tournament/7>)

> Piece of code I have added to my script on Friday (while waiting for round openning): from numerapi import NumerAPI from time import sleep from datetime import datetime napi = NumerAPI(public_id="your_public_id", secret_key="your_secret_key") # wait until current round is open and get current_round number current_round = 0 while current_round == 0: print("Waiting for openning of current round at", datetime.now()) try: if napi.check_round_open(): current_round = nap…
