---
title: "Selling Predictions via NumerBay"
category: Tournament
url: https://forum.numer.ai/t/selling-predictions-via-numerbay/5344
created_at: 2022-05-01T21:04:48.114000+00:00
last_posted_at: 2022-09-30T06:10:21.832000+00:00
posts_count: 12
views: 1168
tags: []
---

# Selling Predictions via NumerBay

---

### Post #1 — **dzheng1887** | 2022-05-01 21:04 UTC

Can someone help me understand how NumerBay works? I see others here who are selling their predictions for 1 NMR, but I do not feel that is enough to make selling on that platform worthwhile.

I am thinking of putting my main model for the regular tournament for sale, but I don’t really understand the ramifications. For the past 13 weeks (include unresolved weeks) since I have started, it averages 0.0320 corr, 0.0156 MMC and 0.0432 TC.

I also have another one that averages 0.0311 corr, 0.0087 mmc and 0.0274 TC over the past 15 weeks. I also have some other NN models that I just developed, but will still need time to evaluate for TC.

Thanks for any help.

---

### Post #2 — **restrading** | 2022-05-02 01:21 UTC

Hi [@dzheng1887](</u/dzheng1887>) you can list at any price you are comfortable with, and you can also set different price levels for different options (e.g. 3 NMR for stake only submission without files, 5 NMR for getting the files, etc.)

You can follow the steps here to get your models listed: [Sell a Product | NumerBay](<https://docs.numerbay.ai/docs/tutorial-basics/sell-a-product>)

---

### Post #3 — **johnnywhippet** | 2022-05-02 21:34 UTC

it costs nothing apart from 5 minutes of your time to sell on numerbay. as you’ve already created predictions for the main tournament its a no-brainer to get them on numberbay - if they’re any good. what’s your ranking? don’t want to sound like I’m boasting but I’ve earned a decent return from numberbay - for not much effort.

JW

---

### Post #4 — **dzheng1887** | 2022-05-02 22:18 UTC _(reply to #3)_

Thank you for your advice and sharing your experience. The rankings are not that great because I’ve only been running the models for 15 weeks.

One thing I wasn’t sure about is if the TC Would change much if others stake on it too

---

### Post #5 — **johnnywhippet** | 2022-05-02 22:23 UTC _(reply to #4)_

sounds like TC is significantly impacted only on very high stakes… there was a post by mdo saying just that i think.

if your model is good or highly rankedthough , get it on numberbay and make some loot! what’s the model name you’re thinking of selling preds for ?

JW.

---

### Post #6 — **dzheng1887** | 2022-05-02 23:11 UTC _(reply to #5)_

Thanks for that, I’ll take a look. I can offer on these two, but their tournament experience is limited. The validation diagnostics also looked good though.

<https://numer.ai/dz_model0>  
<https://numer.ai/dz_model1>

---

### Post #7 — **johnnywhippet** | 2022-05-03 13:47 UTC

They look thoroughly decent! Nowt to lose by trying to sell them. Nothing at all.

---

### Post #8 — **dzheng1887** | 2022-05-03 14:46 UTC _(reply to #7)_

Thank you! these were made on v3 data. Haven’t really had a chance to look at v4 yet. Wanted to pivot to signals as well.

---

### Post #9 — **nyuton** | 2022-09-29 08:41 UTC

Do buyers automatically get my predictions, when they buy it, or do I have to send the the files manually?  
How does it work?

---

### Post #10 — **restrading** | 2022-09-29 10:24 UTC _(reply to #9)_

[@nyuton](</u/nyuton>) You need to upload through the UI or the numerbay Python client. You can set up automation so you don’t have to do manually. [Automate Submissions (seller) | NumerBay](<https://docs.numerbay.ai/docs/tutorial-extras/api-automation>)

---

### Post #11 — **themicon** | 2022-09-30 06:07 UTC _(reply to #9)_

Also remember that you cannot upload the predictions before someone actually bought the predictions. I’ve automated the upload process, but sometimes my pipeline finishes before a sale and I have to then manually upload that sale using the UI.

---

### Post #12 — **restrading** | 2022-09-30 06:10 UTC _(reply to #11)_

[@themicon](</u/themicon>) that’s the case for encrypted listings. If a listing is not using encryption then it can be uploaded anytime.

For encrypted listings you can either automate via webhook ([docs here](<https://docs.numerbay.ai/docs/tutorial-extras/api-automation#webhook-trigger>)) or do the NumerBay submission close to the deadline to cover all existing orders (but make sure to do it at least 30 minutes before round deadline)
