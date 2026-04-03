---
title: "Do really model diagnostics makes sense?"
category: Tournament
url: https://forum.numer.ai/t/do-really-model-diagnostics-makes-sense/3842
created_at: 2021-07-25T22:42:58.441000+00:00
last_posted_at: 2021-07-27T15:27:53.589000+00:00
posts_count: 11
views: 852
tags: []
---

# Do really model diagnostics makes sense?

---

### Post #1 — **eleven_sigma** | 2021-07-25 22:42 UTC

Model diagnostics uses the validation eras, so the results depends if you use them for training or not.  
If you use validation eras, then diagnostics are too much optimistics, as they are overfitted, but if you don’t use validation eras then the diagnostics aren’t real because for real models a lot of people use validation for sure.  
The percentiles returned are biased with models that uses validation.  
Diagnostics should use a blind part of test, not validation.

---

### Post #2 — **wigglemuse** | 2021-07-25 23:16 UTC

Well, that’s the definition of a validation set – a hold-out set that you “validate” on by checking the stats on it. If you train on it, of course it doesn’t mean anything. The problem is that even if you don’t train on it, it doesn’t seem to mean much. What eras are “representative” of the larger population and indicate a good generalized model? Well, probably none of them. We need a validation set with years worth of data in it. Sounds like that’s what we’ll actually get soon if the rumblings about releasing the targets for the test set happen.

---

### Post #3 — **rigrog** | 2021-07-26 05:53 UTC _(reply to #2)_

If they’d just give us the targets, for 1/4 of the test eras… I believe that would improve the metamodel a whole lot more than throwing 3,000 columns at us. And they wouldn’t need to buy any more data!

---

### Post #4 — **sirmobius** | 2021-07-26 11:28 UTC _(reply to #3)_

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/r/dec6dc/48.png) rigrog:

> If they’d just give us the targets, for 1/4 of the test eras… I believe that would improve the metamodel a whole lot more than throwing 3,000 columns at us. And they wouldn’t need to buy any more data!

I assume they use this data to train and validate the meta-model and back-test their trading strategy. They have probably decided they need these examples more than we do at the modelling stage.

---

### Post #5 — **wigglemuse** | 2021-07-26 15:32 UTC

That’s what they said before – they had to have it for backtests. But in the most recent fireside chat Richard said they didn’t really anymore for whatever reason and will probably be releasing those targets, and maybe even releasing targets weekly for live eras that have recently resolved. We’ll see…sounds like we’ll get something anyway.

---

### Post #6 — **eleven_sigma** | 2021-07-26 15:40 UTC

I think the conversation is going to other site… The problem isn’t if we have data enough for modelling (We may open other thread for that). The problem is that if they use a part of data labelled for diagnostics, they will be useless at the moment some people train the models using these labelled data.  
The only way diagnostics makes sense is computing them with a part of unlabelled data.

---

### Post #7 — **rigrog** | 2021-07-26 17:20 UTC _(reply to #4)_

According to Numerai-guy Anson Chu, they do indeed use it for back testing & stuff. So I’m suggesting that they continue using _three fourths_ of it just that way.

---

### Post #8 — **rigrog** | 2021-07-26 17:55 UTC _(reply to #6)_

“I think the conversation is going to other site…”

Is “chat” the other site, to which you refer? Please help me find the discussion of this topic, if it’s there.

Thx,  
Rigrog

---

### Post #9 — **wigglemuse** | 2021-07-26 18:46 UTC _(reply to #6)_

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/e/8797f3/48.png) eleven_sigma:

> The problem is that if they use a part of data labelled for diagnostics, they will be useless at the moment some people train the models using these labelled data.  
>  The only way diagnostics makes sense is computing them with a part of unlabelled data.

The diagnostics are just for you and for your models (and you can calculate them yourself), so it doesn’t really matter what other people are doing. (Numerai doesn’t care what your diagnostics are and do not use them to evaluate your model internally.) Obviously you will know if you’ve trained your own models using the validation set or not.

---

### Post #10 — **eleven_sigma** | 2021-07-27 07:14 UTC _(reply to #9)_

I know if I train using validation or not, but don’t know how many people did, so the percentile diagnostics gives, is useless for me. I think diagnostics is a very good idea but needs to use an unlabelled part of data for compute them.

---

### Post #11 — **wigglemuse** | 2021-07-27 15:27 UTC

Those percentages I believe are hard-coded thresholds and based on the assumption you are not training on the validation set.
