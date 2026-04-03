---
title: "Crypto Factor model - Prediction the return of Bitcoin and Crypto with High Trading Volume"
category: Data Science
url: https://forum.numer.ai/t/crypto-factor-model-prediction-the-return-of-bitcoin-and-crypto-with-high-trading-volume/7672
created_at: 2024-08-25T17:15:27.470000+00:00
last_posted_at: 2024-08-27T11:46:42.180000+00:00
posts_count: 7
views: 732
tags: []
---

# Crypto Factor model - Prediction the return of Bitcoin and Crypto with High Trading Volume

---

### Post #1 — **nishimoto** | 2024-08-25 17:15 UTC

This is my entry for the Numerai/Ocean competition.

All pdf: [Crypto Factor model - Prediction the return of Bitcoin and Crypto with High Trading Volume.pdf - Google Drive](<https://drive.google.com/file/d/1_zfJunbaH8KoZ_ewQFWokYeYyvpdrmMh/view?usp=sharing>)  
Notebook: [desights-ai-crypto-factor-model.ipynb - Google Drive](<https://drive.google.com/file/d/1kvv7ol3AH3e-WxDNDb1nWVaWb9o43aQX/view?usp=sharing>)

Unlike the Numerai crypto tournament, I conducted a factor analysis of the relative monthly return values.  
I also analyzed various factors such as gold and stocks. As a result, the momentum factor seemed to be the most effective. It was also interesting to see something like a small-cap effect.

---

### Post #2 — **accountnumber1** | 2024-08-26 14:54 UTC

Hey, if I leave a comment on your entry, and you leave a comment on mine, then we both get points for engaging with the community!

Ummm… I like your graphs!

Also, interestingly I also got a negative momentum correlation for 20-day timeframe, but positive for 200 day intervals! Still, I was following a different methodology, using Numerai’s binned data rather than raw returns, so it doesn’t necessarily mean that our results are in disagreement.

---

### Post #3 — **yunusgumussoy** | 2024-08-26 20:34 UTC

I like the way you’ve categorized the factors. The Crypto Fear & Greed Index from [alternative.me](<http://alternative.me>) is an excellent choice. However, I’d prefer to use it as a Sentiment Index rather than as an Integrated Index factor. Additionally, I’d like to use Wikipedia “Bitcoin” page views as a Public Interest Index instead of a Social Media factor. Aside from these points, I enjoyed reviewing your work and found it very informative.

---

### Post #5 — **nishimoto** | 2024-08-27 04:46 UTC _(reply to #3)_

Thanks for your comment!

As you pointed out, the Crypto Fear & Greed Index is a sentiment index for users, but the Momentum factor is also used in the actual calculation of the index, so we used the name Integrated Index factor.

---

### Post #6 — **nishimoto** | 2024-08-27 04:48 UTC _(reply to #2)_

Thanks for your comment.  
The inverse result of Momentum Factor is interesting, as we should always be prepared for the possibility of the opposite happening, as during the crypto asset bubble in 2021, the price of crypto assets went up despite being well above their 200-day moving average.

---

### Post #7 — **accountnumber1** | 2024-08-27 10:54 UTC _(reply to #6)_

Indeed, there can be specific unusual market conditions, where behaviour which is abnormal or even the opposite to normal can be exhibited, and momentum could switch from being anti-inductive to inductive for example, and identifying such conditions is important for managing risk from extrordinary circumstances such as bubbles!

---

### Post #8 — **okpo** | 2024-08-27 11:46 UTC

good job. It’s a tough one
