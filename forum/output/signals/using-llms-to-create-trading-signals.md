---
title: "Using LLMs to Create Trading Signals"
category: Signals
url: https://forum.numer.ai/t/using-llms-to-create-trading-signals/6374
created_at: 2023-05-18T00:46:08.288000+00:00
last_posted_at: 2024-11-03T14:23:47.511000+00:00
posts_count: 9
views: 17094
tags: []
---

# Using LLMs to Create Trading Signals

---

### Post #1 — **richai** | 2023-05-18 00:46 UTC

I tend to agree with Sam Altman when he was recently quoted saying [“in the next 5 years I think some of of investing vehicle is going to figure out how to use AI to get crazy outperformance”](<https://twitter.com/richardcraib/status/1656677856003629056?s=20>). I also intend to spend the next few years proving Sam right with the Numerai community.

I wanted to open up a discussion on using LLMs in finance. Practitioners and academics are writing papers about using ChatGPT to predict stocks. Unfortunately, many of these papers are low quality and produce sketchy results. Nevertheless, it’s very clear that LLMs are good at comprehension and summarization of financial information ([here’s Claude summarizing a 10-k from Netflix](<https://vimeo.com/825668090>)) and sentiment analysis on news.

Justina Lee, a journalist at Bloomberg who [recently wrote about Numerai](<https://www.bloomberg.com/news/articles/2023-02-28/tudor-jones-backed-quant-jumps-20-as-crowdsourced-bets-pay-off>), tweeted [a thread of papers which use ChatGPT in various ways for stock prediction](<https://twitter.com/justinaknope/status/1648361909018607617?s=20>). The problem with these papers is a lack of concern with implementation of the strategies (eg they ignore transaction costs or market impact costs) and the lack of rigor around whether the strategies are picking up on alpha [or simply beta and factor exposures in some form](<https://twitter.com/jonathanrlarkin/status/1656834936660172800?s=20>).

Numerai Signals solved both the problem of a signal’s implentability and alpha discernment when it launched in 2020 by developing and releasing special targets. These targets are transformed versions of the subsequent return of every stock and span a universe of ~5000 global equities. They neutralize out market risk, factor risk, country and sector risk and therefore only evaluate the true alpha contained in a signal (not unlike Barra’s residual returns). They also focus on 1m subsequent return and remove the first 2 days of returns to account for implementation difficulties executing on the signal within size within 2 days. These transformations make the signals harder to predict on in the first place but also much higher quality and more likely to generalize into the future if you can develop a predictive signal on them.

When I first announced Numerai Signals in 2020, the use our language models to create signals was not lost on me. After all the goal of Numerai is to assimilate advances in artificial intelligence faster than any other hedge fund by being the world’s open hedge fund.

“There is little doubt in Jason Rosenfeld’s mind that modern language models like OpenAI’s GPT-3 are the future”, I wrote in the [launch post for Numerai Signals](<https://medium.com/numerai/building-the-last-hedge-fund-introducing-numerai-signals-12de26dfa69c>). Jason who was formerly at the hedge fund Millennium has been a Numerai and Numerai Signals user for years. Today Jason works full-time on [Crowdcent](<https://crowdcent.com>), a startup which stakes Numerai models and uses LLMs to build signals.

I caught up with Jason to discuss the research papers I’d been reading on ChatGPT in finance, there problems and think through ways someone might build a legitimately good and impressive signal on the Numerai Signals universe using LLMs. I’ve also spoken with a company collecting and processing vast amounts of financial news data like [Nosible](<https://nosible.com>).

I wanted to share with the Numerai community how I would think about building a signal for Numerai Signals using LLMs. I think it’s valuable to share ideas so that the Numerai community can reach ‘hello world’ of a signal based on LLMs as fast as possible, and Numerai can begin to integrate more of these signals into the live trading of our hedge fund. I think the more that AI and quantitative finance secrets become public knowledge the better the world is and the stronger Numerai will be over the long term.

_Download the targets from Numerai Signals_

Go here: [Numerai](<https://signals.numer.ai/login>)  
In the left nav, click Data to download the data.  
The file to open is called historical_targets.csv. It looks like the below.

[![Screenshot 2023-05-07 at 10.01.42 AM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/5/50dc61b967bcd5798429bd43f864c85303c142b9_2_690x122.png)Screenshot 2023-05-07 at 10.01.42 AM1448×258 65.4 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/5/50dc61b967bcd5798429bd43f864c85303c142b9.png> "Screenshot 2023-05-07 at 10.01.42 AM")

The challenge on Numerai Signals is to create your own features and train a model to predict the target. The target highlighted in green is the one I would use for this: “target_20d_factor_neutral”.

_Data_

If anyone knows where one can get a free or cheap financial news or headlines dataset, tell us in the comments! Getting this type of data can be hard, ensuring that the data is point in time is hard, determining which article corresponds to which stock ticker is hard. Nevertheless, there may be easy ways to get started for example by just focussing on large US stocks where news data is very easy to find online.

The expensive but seemingly high quality data I’ve seen is at Reuters or Bloomberg but these are at inaccessible prices.

_Embeddings as features_

You can use language models to turn text into a numerical feature vector which has good properties. It might be sensible to turn all news headlines which were published before the “friday_date” column, obtain the embeddings (with OpenAI, BERT, etc) of each headline to generate 100-500 features for each stock which we can use to predict the target.

The embedding turns text into numerical features. With the features we can set up a regression problem would look like:  
headline_embedding_value_1, headline_embedding_value_2, … , **target_20d_factor_neutral**

We could then model this with a simple LightGBM model. Because the stock market is hard, if we can get just 0.01 correlation with this model’s predictions to the target variable in out of sample predictions, this will be good. 0.015 would be excellent.

It could be a good idea to simply take the most recent news article headline from the last 30 days and leave all the features blank if there was no news in the past 30 days. For example, TSLA will have news almost every day so we can just use the headline closest to (but before) the friday_date which is probably the day before. For a smaller stock without much news, we might have to take news from 10 days ago.

I think it’s good to focus on headlines because if you have a full-text article the embedding can get weird and headlines are good compressions of the content anyways.

_Prompt answers as features_

Rather than use the abstract embedding of features of in the news headline you can prompt the model directly to give a response about it and even ground it through the prompt. For example, in one of the researchers papers above the prompt they used was:

_Forget all your previous instructions. Pretend you are a financial expert. You are a financial expert with stock recommendation experience. Answer “YES” if good news, “NO” if bad news, or “UNKNOWN” if uncertain in the first line. Then elaborate with one short and concise sentence on the next line. Is this headline good or bad for the stock price of company name in the next month?_  
<https://ssrn.com/abstract=4412788>

It seems very possible that prompts could be much better than embeddings to really get precisely the feature you want by directly prompting the model. Maybe it’s important to ask various creative prompts which get to different aspects of the article to create different features. For example, “is this news positive for the long term of the company and the short term?”, “does this news improve the moat or competitive edge of the company”, “even if the news seems to be positive in sentiment, is there anything in this news which suggests the company may beat earnings expectations?”

_Point in time language models?_

Language models are often trained with data up to a certain time eg 2021. This means the model might leak information from the future in the prompt. When giving news about Apple from 2014 and asking about Apple’s prospects, the model might use information it knows about Apple after 2014 in coming up with an answer and this will compromise all the results. Could a prompt that says “use strictly the information in the news article” help… maybe? Are there open source LLMs which are designed to be point in time… I don’t know.

I’m excited to see what the Numerai community can come up with in terms of finding or building a great financial news dataset, using OpenAI’s or other LLMs to create features, and building high performing orthogonal signals on Numerai Signals.

Retroactive bounties for super impressive work that gets shared on this topic! Looking forward to talking about it in the next Numerai Fireside Chat (which we’ll do [on Discord on June 8th](<https://discord.com/invite/numerai>) ).

---

### Post #2 — **murkyautomata** | 2023-05-18 05:46 UTC

![](http://forum.numer.ai/user_avatar/forum.numer.ai/richai/48/2493_2.png) richai:

> I think it’s good to focus on headlines because if you have a full-text article the embedding can get weird and headlines are good compressions of the content anyways.

Headlines sometimes intentionally leave out information (clickbait,) or inflate the the significance of events. Maybe better to have an LLM create a very short summary and encode that.

> Could a prompt that says “use strictly the information in the news article” help… maybe? Are there open source LLMs which are designed to be point in time… I don’t know.

LLMs should be well suited to anonymizing articles. I’d suggest you just have the LLM anonymize the article first in a separate run to strip away any information that could give away the specific date and company.

---

### Post #3 — **quantverse** | 2023-05-19 10:54 UTC

I think there are two possible approaches to this:

  1. There are data vendors (live Ravenpack, Brain, …) extracting and selling precisely these features. These companies dedicate to that full-time for years in large teams of PhDs, so maybe if you don’t want to reinvent the wheel, buy and test their data (we are seriously considering doing that btw).
  2. Make it yourself (get good headline datasets and use local LLMs like LLama / Vicuna to extract the sentiment). Will be a lot of fun but a lot of work (and you still need to pay for headlines data).

---

### Post #5 — **surajp** | 2023-05-28 21:46 UTC

Not sure if this is exactly what you’d like here but I was playing with QLoRA to fine-tune the models. Just sharing something I worked on this weekend.

The idea was to, instead of training a model from scratch, how about fine-tuning with LoRA on numerai data. My initial thought was to simply use ChatGPT’s web access to let it understand and then ask it my doubts. Just like stable diffusion LoRAs, why not try it for text using a local model. More specifically, letting the LLM with a broader understanding of the world, fine-tune on all the Rocketchat discussions, Numerai docs (including OHwA), Forum and then asking it to explain me TC. In short, demystifying TC from all the discussions.

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/8/8e7d98e2ad721f8bbdbbbcc325598aa5e7ad6f6a_2_517x189.png)image748×274 20.6 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/8/8e7d98e2ad721f8bbdbbbcc325598aa5e7ad6f6a.png> "image")

I downloaded all the textual data locally and tuned a model on Numerai related content. not much processing done.

With QLoRA I was able to tune the `EleutherAI/gpt-neox-20b` with the help of notebook provided. Due to limited resources for Colab Pro, I was able to train it only for 500 steps (~0.1 epoch) without much data cleaning. Maybe someone can use this notebook/model as checkpoint and train it further for multiple epochs. This is still an early notebook without proper evaluation but a proper tuning will require much more efforts and compute(which I currently lack).

  1. base model’s output  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/8/8231df94b55d48ac4529c5bdc109697fcace0dc5.png)image734×402 13.5 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/8/8231df94b55d48ac4529c5bdc109697fcace0dc5.png> "image")

  2. output after tuning, and loading the model from HF hub  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/a/a0778874509e0653bf1efd8d8509d8aeab55c311.png)image1801×241 13.5 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/a/a0778874509e0653bf1efd8d8509d8aeab55c311.png> "image")




Notebooks:

  * QLoRA training+inference notebook: [bnb-4bit-training_numerai_forum_and_rc.ipynb](<https://colab.research.google.com/drive/1MDEXXWmtIn4TJdgv8_4YnDN5BwxLAnRD?usp=sharing>)
  * Dataset collection notebook (may not work out of the box): [01_parse_discussions.ipynb](<https://colab.research.google.com/drive/1k8zd6gIDY9uofv6sj4PtuUosvEJJgjIk?usp=sharing>)
  * HF HUB LoRA: [surajp/500steps-gptneox20b-qlora-numerai](<https://huggingface.co/surajp/500steps-gptneox20b-qlora-numerai>)



Potential improvements:

  * LoRA on financial data; reduces compute requirements by a huge margin. (easy embeddings; potential alternative to BloombergGPT?)
  * Instruction-tuning
  * Use a better baseline model
  * Train for longer



I apologize for directly training on the text without permissions (just couldn’t wait). Happy to delete the model from hub and the saved training data. Please DM

edit: Thanks [@slyfox](</u/slyfox>) for the permission to keep it hosted

---

### Post #6 — **surajp** | 2023-05-28 22:49 UTC _(reply to #5)_

How about a community wide project like BigScience for training an LLM with **data curated** by users and compute provided by Numerai (or funded by CoE)?

---

### Post #7 — **quantverse** | 2023-06-02 15:05 UTC

Playing with Guanaco 65B model on my desktop. It is a nice toy ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=12)

> How would you interpret a news headline “SentinelOne slumps ~35% after downgrades at Canaccord, BTIG on outlook, macro impact”? Please classify the  
>  headline into each of these categories: earnings, analyst ratings, insider trading, revenues, dividends, credit ratings. Make a JSON where each catego  
>  ry is a key and value is the appropriate estimated sentiment (very negative, negative, neutral, positive, very positive).

This headline can be interpreted as:

  * The stock price of SentinelOne has fallen by about 35%
  * This decline was caused by analysts downgrading the company’s outlook and citing concerns about the overall market conditions affecting the business



Based on this interpretation, we can classify the headline into these categories:

  * earnings: very negative (the stock price is down)
  * analyst ratings: very negative (downgrades)
  * insider trading: neutral (no mention of insider trading in the headline)
  * revenues: unknown (not mentioned in the headline)
  * dividends: unknown (not mentioned in the headline)
  * credit ratings: unknown (not mentioned in the headline)



The JSON output would look like this:

`{"earnings": "very negative", "analyst ratings": "very negative", "insider trading": "neutral", "revenues": "unknown", "dividends": "unknown", "credit ratings": "unknown"}`

---

### Post #8 — **thinkdevdo** | 2023-06-14 03:35 UTC

Hello,

I’ve been into LLMs since the BERT/GPT-2 days for concrete tasks such as classification and transformer models for timeseries forecasting. Recently I’ve been seeing a lot of hype around raw embeddings, and really liked ideas coming out of the space around databases and search in these latent spaces with such things like Chroma. I’m from the robotics/CS/embedded system world(s) and I came to this tournament to give myself an interesting project with which to learn the internal of Deep Learning, given that my surface level knowledge of using such architectures for my projects/research wasn’t satiating my curiosity for understanding the underlying governing statistics. For some of my models I have been using financial sentiment from a few sources, alongside timeseries OHLC-V features. I thought this post would provide a good reason to look deeper into the embeddings and hopefully claim some bounty with which to stake some of my models, but as a spoiler, the results herein are not satisfying.

Over the past year+ I spent many (many) hours obtaining financial documents and turning them into sentiment scores [-1,1], and also needed to set up internal compute infrastructure to make this pleasant to work with. Over the past month I’ve re-run my now modified code to export the D-dimensional embeddings from the last layer of my sentiment classifier into a database for all of these financial documents. I know that the discussion is about using embeddings from ChatGPT, or similar, most likely from prompting about news and social discussion, but I thought it would be a worthwhile start to replace the sentiment scores from my classifier with the raw embeddings that produced them.

I did this for a few reasons (1) to see if the downstream task could make use of the extra features, (2) my LLM classifier is already set up in-house, so there’s no need to use cloud services, which I do not have subscriptions for, nor wanted to spend the time integrating, and (3) thinking deeply about how to prompt ChatGPT to honor point-in-time, given that a lot of the financial discussions may be inherit in it’s weights, with respect to the Numerai target training dates, was not worth the time.

Early on I also tried to procure some news headlines and/or content (without cost), but the best I found was from Alpaca, which only went back to about 2015, which did not align well with the Numerai targets. Of course I can always train using this modified time period, and there is already a notebook using news sentiment, but it’s never been a part of my purview.

I present three models. The first is a baseline with only OHLC-V input features, while the first sentiment model has OHLC-V features + N sentiment features. For this work I simply replaced the N sentiment features with N*D raw embeddings from the last layer of my classifier. This proved challenging for training, since it ballooned the RAM needed to hold the dataset tremendously, so much so that I needed to implement some inefficient code in order just to load the records at runtime in order to train which substantially increases the training time.

I trained 3 models to compare.

  * OHLC-V
  * OHLC-V + N Financial Sentiment
  * OHLC-V + N*D Financial Embeddings



I was really hoping to show something interesting, but currently the results are unsatisfactory, and given the time it takes to train I’m unsure if I will keep probing at it. I thought I would share the plots though. I’ve previously trained models with the hyperparameters chosen, but those models were obviously more similar to (1) and (2), the training curves and diagnostic plots are typical of what I’ve seen from these parameters. The validation curve on the embedding model looks terrible though, doing a hyperparemter search would most likely be useful, since I just reused what I used for the previous two models, but this will take time and I wanted to put this write-up out there, before it falls by the wayside, to see if this is even useful information, or aligned with what [@richai](</u/richai>) was interested in.

Small note: for comparison between these models there’s no difference between the “x Loss” and “x Absolute Loss.” When training my models, I usually use things like learning rate annealing and/or early stopping, but for this experiment I used a fixed learning rate and let it run either until the training finished, or until I stopped it manually. The diagnostics are produced from the model with lowest “Valid Loss,” as shown by the “Best Loss” plot. This would be interesting to do this with decision trees as well, but I came to this tournament to experiment with deep learning, so these are neural networks.

* * *

## 1\. OHLC-V

Parameters: 1,054,721  
Runtime: 15 minutes, 72 epochs  
Diagnostic Inference: 2 minutes

### Training

[![ohlcv](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/e/e19704e374963151851bbdae9bd1f41edeb61f9f_2_690x404.png)ohlcv1005×589 41 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/e/e19704e374963151851bbdae9bd1f41edeb61f9f.png> "ohlcv")

### Diagnostics

[![ohlcv-diag](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/2/289f046ff4fc6a5d504f40529bb7363a4e8a4d72.png)ohlcv-diag592×421 24.7 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/2/289f046ff4fc6a5d504f40529bb7363a4e8a4d72.png> "ohlcv-diag")

  


[![ohlcv-diag-cumu](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/b/bfbdc0fdebe4abbe8eeda24aceb6fa0b8d5c30e2.png)ohlcv-diag-cumu596×428 21.2 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/b/bfbdc0fdebe4abbe8eeda24aceb6fa0b8d5c30e2.png> "ohlcv-diag-cumu")

## 2\. OHLC-V + N Financial Sentiment

Parameters: 1,060,353  
Runtime: 12 minutes, 72 epochs  
Diagnostic Inference: 2 minutes

### Training

[![ohlcvn](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/c/c4357568bd9dad71d36652ad16697960b286c4ab_2_690x404.png)ohlcvn999×585 40.9 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/c/c4357568bd9dad71d36652ad16697960b286c4ab.png> "ohlcvn")

### Diagnostics

[![ohlcvn-diag](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/8/8b17555a44fa806648e8732a5514a38aac3150ee.png)ohlcvn-diag597×424 27.2 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/8/8b17555a44fa806648e8732a5514a38aac3150ee.png> "ohlcvn-diag")

  


[![ohlcvn-diag-cumu](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/9/955ab7a279c4ccdc30ffce4ce8057e9d13efd4ad.png)ohlcvn-diag-cumu594×420 21.5 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/9/955ab7a279c4ccdc30ffce4ce8057e9d13efd4ad.png> "ohlcvn-diag-cumu")

## 3\. OHLC-V + N*D Financial Embeddings

Note: I cut training on this early to try another setup, but I will re-train it for longer to see if it improves. It’s possible the optimizer has yet to hook into a good trajectory; you’ll notice the loss is much higher, almost an order of magnitude.  
Parameters: 4,987,393  
Runtime: 6+ Hours, 18 epochs  
Diagnostic Inference: 44 minutes

### Training

[![ohlcvnd](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/a/a7285f2dd7f25ea60f0868de08c5f50b7547acd7_2_690x403.png)ohlcvnd1003×586 43.6 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/a/a7285f2dd7f25ea60f0868de08c5f50b7547acd7.png> "ohlcvnd")

### Diagnostics

[![ohlcvnd-diag](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/8/8c1a53830746bc58a5f613320d970ac1ecc01b1b.png)ohlcvnd-diag592×424 27.2 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/8/8c1a53830746bc58a5f613320d970ac1ecc01b1b.png> "ohlcvnd-diag")

  


[![ohlcvnd-diag-cumu](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/1/1280b1a25a7fa88c8db4968d84ac0b2fad113bfc.png)ohlcvnd-diag-cumu596×422 21.7 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/1/1280b1a25a7fa88c8db4968d84ac0b2fad113bfc.png> "ohlcvnd-diag-cumu")

* * *

Something I usually do is train with a smaller gap between OHLC-V candles, but to reduce training time with the embedding model I used a larger time-gap, although it’s not uncommonly high or totally foreign to my previous training. I’ll probably let the embedding model run with a smaller time-gap when I have an opportunity to see if the validation plots are smoother or the diagnostics a little better, perhaps with a reduced training set to balance the time increase.

Hope this is at least useful information, it was a lot of work for what I don’t think is any substantial insight. If the longer run for (3) provides something interesting I will be sure to update the post.

TDD

---

### Post #9 — **richai** | 2023-06-26 07:29 UTC _(reply to #8)_

This looks super encouraging to me. I think the performance is good and it is especially interesting that sentiment improves Sharpe and the more recent period.

I wouldn’t expect a sentiment-based or LLM-based score based on news to do well by itself. It’s supposed to work well blended when trained with other features. I am also not surprised that the N*D embedding makes it harder to train.

If you’re open to share the historical values of your sentiment signal, Numerai could test it by training a model on all Numerai’s Sunshine features + your sentiment feature. We could share the results of that with you here including the feature importance.

---

### Post #10 — **rustydata** | 2024-11-03 14:23 UTC

Thinking about the tech earnings this past week - where trading on earnings was influenced a bit by overall market movement - this is kind of like decoding whales’ vocalizations. They can hear each other on scales much larger than what we’re used to, so creating training data to produce whaleLLM would need a fairly large amount of information about everything happening across thousands of square km of ocean. Are they talking about a fishing boat 100km to the north, or a pack of other whales 100km to the west, 200m below the surface. Using larger time windows - 3 weeks post earnings, the brownian/short time-scale movement gets smoothed out, but things like the yen carry trade, short squeezes, overbought markets, investors holding out for rate cuts, and maybe most of all, _real_ risk-neutral adjustments can give critical context about the environment. Sometimes the easiest alpha can be realized through contrarian conclusions about beta. The fed rate is like a water line, and as it drops, it reveals all the tickers with risk adjusted return that were just below the surface, so a load of companies with previously negative beta are suddenly positive relative to.  
The more I trade sell-side, the more I appreciate the complexity of being able to actually leverage predictions to realize upside at scale.
