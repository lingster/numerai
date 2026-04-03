---
title: "Stock Data Transform Example Notebook"
category: Signals
url: https://forum.numer.ai/t/stock-data-transform-example-notebook/3146
created_at: 2021-05-01T11:40:33.244000+00:00
last_posted_at: 2021-09-08T14:51:21.336000+00:00
posts_count: 2
views: 1160
tags: []
---

# Stock Data Transform Example Notebook

---

### Post #1 — **robo_boi** | 2021-05-01 11:40 UTC

Hi. [Here](<https://colab.research.google.com/drive/1aLIz_yQELGXuPXMWGZNuOTbIpplKsEBa?usp=sharing>) is a colab notebook with some examples of different transforms you can do with stock data.

They are mostly technical indicators using open, high, low. close, volume (OHLCV). I’m using [ta-lib](<https://mrjbq7.github.io/ta-lib/doc_index.html>)  
to calculate the indicators wherever I can. I also added some graphs where I thought they would be helpful.

Now for the disclaimers. In no way is this list exhaustive. I am not claiming everything here is 100% correct. Trust but verify. There is no explanation of the different indicators, that’s up to you. Will these build a good model, maybe but maybe not. As always, start with good clean data. Garbage in, garbage out.

I want to send a huge thank you to [@jrai](</u/jrai>) and [@jrb](</u/jrb>) for their weekly signals clubhouse/twitch chats as well as [@arbitrage](</u/arbitrage>) for daily scores and chill/office hours. I’ve learned a tremendous amount from those talks. Signals crew for life.

---

### Post #2 — **mwangbq** | 2021-09-08 14:51 UTC

Hi, thanks very much for your sharing, I noticed one point, ‘adj_close’ is not the same scale as open, high, low because open,high,low,close columns are not adjusted, so be careful if you want to make features which are calculated by close & OHL;  
By the way, is there any link that I can find '**their weekly signals clubhouse/twitch chats**? thanks in advance!
