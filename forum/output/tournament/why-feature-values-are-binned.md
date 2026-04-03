---
title: "Why feature values are binned?"
category: Tournament
url: https://forum.numer.ai/t/why-feature-values-are-binned/5700
created_at: 2022-09-19T03:39:34.220000+00:00
last_posted_at: 2022-09-19T14:01:42.356000+00:00
posts_count: 3
views: 757
tags: []
---

# Why feature values are binned?

---

### Post #1 — **ryo_matsuzaka** | 2022-09-19 03:39 UTC

Hello. I am a newbie of Numerai.  
I started yesterday.  
I have a question about training data.  
Why feature values are binned like 0, 0.25, 0.5, 0.75 and 1.0?  
What these values do mean?  
These data are already feature engineered?

---

### Post #2 — **bor1** | 2022-09-19 13:53 UTC

The main reason the features are as they are is that numer.ai isn’t allowed to give out the financial datasets that they are subscribed to.

By hiding the name of the stock, and by anonymizing the features, they can still share the data with us.

The plus side is that you have little (if any!) data cleaning to do. All features are ~ normal distributions centered at 0.5. So maybe you want to substract 0.5 from them when you feed them to a neural network, but that is about it.

---

### Post #3 — **wigglemuse** | 2022-09-19 14:01 UTC

That’s the main reason they are obfuscated/normalized, but the binning itself I think they just did because they thought it worked better… or something. (I forget exactly what they said about this when asked, but it was more like “we considered that, but didn’t do it for whatever reason”, not “because secrecy”.) It does potentially lower the computing resource level needed to deal with the data as it can be cast to integers, and likely doesn’t affect results (in most cases) as much as one might think. Still, I wouldn’t be surprised to see them go to true real-valued features at some point.
