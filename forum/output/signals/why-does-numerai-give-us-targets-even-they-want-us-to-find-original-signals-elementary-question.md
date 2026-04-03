---
title: "Why does Numerai give us targets even they want us to find original signals? (elementary question)"
category: Signals
url: https://forum.numer.ai/t/why-does-numerai-give-us-targets-even-they-want-us-to-find-original-signals-elementary-question/5022
created_at: 2022-03-06T13:08:36.182000+00:00
last_posted_at: 2022-03-07T19:02:11.119000+00:00
posts_count: 4
views: 1303
tags: []
---

# Why does Numerai give us targets even they want us to find original signals? (elementary question)

---

### Post #1 — **mikamiyusuke** | 2022-03-06 13:08 UTC

Hi, these days I’ve just started working on Numerai Signals and have a few points I completely cannot understand about signal targets given by Numerai.

The questions are belows

#### 1\. Why does Numerai give us targets even they want us to create original signals?

  * In [this notebook](<https://colab.research.google.com/drive/1ECh69C0LDCUnuyvEmNFZ51l_276nkQqo#scrollTo=Pod7d3YFHqIB>), target is downloaded by following code,


    
    
    numerai_targets = 'https://numerai-signals-public-data.s3-us-west-2.amazonaws.com/signals_train_val.csv'
    targets = pd.read_csv(numerai_targets)
    

  * However, in this Numerai Signals, is it most important to pursue originality? Why targets are given?



#### 2\. If I train a ML model using given targets as targets, the model can output targets that have originality?

#### 3\. How can I define the meaning of the original signals I create?

  * Here is an example way to get original signals using alternative data.  
[Getting Started with Numerai Signals: Sentiment Analysis](<https://wandb.ai/carlolepelaars/finbert-stocknewsapi-numerai-signals/reports/Getting-Started-with-Numerai-Signals-Sentiment-Analysis--Vmlldzo0OTg2MDU>)
  * In this sample, this data scientist use sentiment as signals without given targets. Thus, the signal has a meaning of sentiments. However, is this ok to define the meaning of targets by ourselves? If it’s ok, are there any precise steps to define meanings? Because I think we cannot handle signals if we cannot understand the meanings of the signals.



#### 4\. What’s the difference between a trained model using given targets and a model trained model without given targets.

  * Considering the above questions, What are the precise differences between them?
  * Should I use targets when I want to train a model using alternative data like news text, satellite image, and of course stock price to extract super original signals?



Thank you for reading.  
If you think this question is not suitable for this forum(because this is so elementary question), sorry for that.

---

### Post #2 — **autratec** | 2022-03-07 10:54 UTC

I am also interested to know how the target was calculated.

---

### Post #3 — **autratec** | 2022-03-07 11:53 UTC

Realized there’s a post here: [Decoding the signals target](<http://forum.numer.ai/t/decoding-the-signals-target/2501>)

---

### Post #4 — **robo_boi** | 2022-03-07 19:02 UTC

I’m certainly not an expert but I’ll do my best to help.

  1. Targets can be used to train a model or to test whatever alternative data you have. For example, say you have sentiment data, is that correlated with the target at least in the past? No guarantee it will be in the future or that it won’t get neutralized away but it will give you an idea



You certainly don’t have to use the targets and can just submit an original signal between 0 and 1 from whatever data you have

I don’t know if I would say pursuing originality is the most important thing. It’s certainly very important because if you are un-original your signal or model most likely won’t do well because they will neutralize it. In other words, they have something similar and it wont help so they don’t want it. It’s also important though to have a good signal for obvious reasons which is where the targets come in. So good and different is what you’re looking for

  2. I believe so, especially if you use unique modeling techniques but you would have to try. Originality is a tough thing to define IMO and you want original and good

  3. Yes you can. As stated before you can just submit a number between 0 and 1. There really are no steps except that it’s a ranking problem so what you submit should be a ranking that’s normalized between 0 and 1

  4. Can’t answer these. You should really just try all those things you mentioned. You have up to 50 model spots and you don’t have to stake any NMR on them to just try things out




Signals is a little more guarded than the main tournament in terms of what people share that works well, so you will have to just try different things but it sounds like you are on the right track. Good luck.
