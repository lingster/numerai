---
title: "Basic question of data"
category: Tournament
url: https://forum.numer.ai/t/basic-question-of-data/3587
created_at: 2021-06-12T06:04:01.790000+00:00
last_posted_at: 2021-06-13T11:23:06.835000+00:00
posts_count: 12
views: 1147
tags: []
---

# Basic question of data

---

### Post #1 — **autratec** | 2021-06-12 06:04 UTC

Hi all , i am very new in this domain. and sorry for those basic question.

I check the data set being provided, which includes id (unique index data, no duplication), era 1 to era 120, features, and target.

Here my confusion:

" Each id corresponds to a stock at a specific time era " Lets assume there is APPLE data in the data set, data frequency is daily, and cover last 120 days, then there will be 120 lines of data related to APPLE. How i can identify those 120 line of data related to APPLE ?

Id is a unique index number. so what’s the business reason to predict the target, related to a stock with specific time era ? Should that be a prediction to stock A with next 4 weeks performance ?

Are we looking for a model to predict future without knowing which data elements are linking back to the same stock ?

Are we looking for the prediction for whole market ? can we focus on couple selected stocks ?

sorry, i am really confused.

hope will get some inputs from you guys.

thx.

---

### Post #2 — **sneaky** | 2021-06-12 08:52 UTC

Hi, you cannot link them together. It is designed that way. If you would be able to link them, then you would be able to determine which stock is which.

Some features are likely composed of temporal data like: lagging indicators, look back, etc.

Also, I recommend you to read all forum before you start implement any model. This is quite repeated question. For example [here](<http://forum.numer.ai/t/taking-advantage-of-eras/3269>)

---

### Post #3 — **ml_is_lyf** | 2021-06-12 09:00 UTC

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/a/6bbea6/48.png) autratec:

> data frequency is daily

From my memory, the dataset is not weekly, each era is a 4 week period (without overlap).

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/a/6bbea6/48.png) autratec:

> so what’s the business reason to predict the target

Individual targets don’t really tells us much, what we’re really interested in is the order of the targets in a given era, as this tells us the rank of the models with respect to the target, which can be used to make portfolio allocation decisions.

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/a/6bbea6/48.png) autratec:

> Are we looking for a model to predict future without knowing which data elements are linking back to the same stock ?

Yes exactly. The purpose of the tournament is you don’t know which exact stock is which, we’re just trying to rank them with no knowledge other than the features provided. If you’re interested in the problem where you know which stock your predicting, take a look at the sister tournament Signals, but the downside is you have to bring your own data (as that’s the point of it).

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/a/6bbea6/48.png) autratec:

> Are we looking for the prediction for whole market ? can we focus on couple selected stocks ?

Nope, each era consists of a subset of stocks, the fund aims to be sector and country invariant, so the stocks are very diverse. Our job is to predict the order for the given stocks.

And yeah as sneaky said, a lot of stuff isn’t written down, so it’s good to have a read through the forum. My recommendation is try to watch all the YouTube videos on the Numerai channel (or as many as you can), and most importantly watch Arbitrage’s introduction series, as it covers all the basic questions like these

---

### Post #4 — **autratec** | 2021-06-12 09:10 UTC _(reply to #3)_

hi all. thanks for the patient and reply. I am new in this area. After spend couple hours and trying different tools, i am able to make some progress, and submitted my first prediction file.

But here is the error i got:

_Invalid submission size. You submitted 5389 targets, but number of tournament data targets is 1736405. The live universe changes each week, make sure you are using the latest tournament data._

What i did is:

Download: numerai_tournament_data , which is a 2.5G file. I realized in that huge file, including lots of test, validation data. and there are about 5389 lines is live data without target value. I assume this the prediction we need. After push those 5389 data lines through my model, i got a result csv file with id and target results.

Please help suggest where are those 1736405 lines ? do i need to resend whole tournament, include live entry with prediction and those test/validation lines back to numer.ai ?

thanks again for your patient.

---

### Post #5 — **ml_is_lyf** | 2021-06-12 09:32 UTC _(reply to #4)_

If you want to do this, you probably need to load in the IDs for validation and test at least too, and put random values in the CSV file.

---

### Post #6 — **autratec** | 2021-06-12 09:54 UTC _(reply to #4)_

Thanks for the suggestion. I am doing the modeling and prediction using some low end tools , even Excel. Handling 2.5G is very painful.

---

### Post #7 — **ml_is_lyf** | 2021-06-12 10:40 UTC _(reply to #6)_

Everything you can do in Excel you should be able to do in Python. If you’re using Python then you can use Google Colab, which gives you very powerful machines for free. So that’s probably the best way to go

<https://research.google.com/colaboratory/>

---

### Post #8 — **autratec** | 2021-06-12 10:54 UTC _(reply to #7)_

thanks. but i am not using python (looks like need to learn it now ) ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=9) i am using all those microsoft products to link dots together: Azure ML studio, PowerBI desktop, Excel, etc

---

### Post #9 — **ml_is_lyf** | 2021-06-12 11:29 UTC _(reply to #8)_

Ah right, I’m assuming the bit where you’re having problems is Excel then? As I know it has a size limit for files. Whereas I’m pretty sure those two other tools should be able to handle that kinda size of data? So you probably just need to replace your Excel workflow with Python. Take a look at the Pandas and Numpy packages in Python, they are basically the Excel of the Python world.

---

### Post #10 — **autratec** | 2021-06-12 11:45 UTC _(reply to #9)_

yes. i am using PowerBI to replace excel for the data preparation. . but still need Macro in Excel to connect with AZ ML studio web service to handle the prediction in a batch file mode. looks like it is the right time for me to learn python.

---

### Post #11 — **sneaky** | 2021-06-12 20:03 UTC _(reply to #10)_

Learn pandas and numpy (python modules). That is the way. They are optimized to do matrix calculations which is the core of machine learning.

---

### Post #12 — **autratec** | 2021-06-13 11:23 UTC _(reply to #11)_

All, thanks for all the guidance. At the end, I realized all the data processing can be done though Azure ml studio: from loading training and tournament data, untill export final prediction.

Two module was submitted today. Let’s see how these prediction going.
