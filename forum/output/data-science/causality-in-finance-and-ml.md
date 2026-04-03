---
title: "Causality in Finance and ML"
category: Data Science
url: https://forum.numer.ai/t/causality-in-finance-and-ml/6049
created_at: 2023-01-18T21:21:38.657000+00:00
last_posted_at: 2023-01-23T01:05:31.106000+00:00
posts_count: 5
views: 2542
tags: []
---

# Causality in Finance and ML

---

### Post #1 — **jefferythewind** | 2023-01-18 21:21 UTC

There’s a great new article by Marcos López de Prado, Causal Factor Investing:  
[Can Factor Investing Become Scientific](<https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4205613>)? de Prado is a well-known author in subjects spanning investment finance and machine learning. In this recent paper he lays bare a fundamental shortcoming of popular factor investing literature: the lack of causal claims.

The first part of the text is concerned with discussing the basics of discerning **causality** from **association**. We understand association as an observed correlation between two variables X and Y. When two variables are associated, observing the value of one conveys information about the value of the other, ie. P[Y=y|X=x] != P[Y=y], or equivalently, P[X=x|Y=y] != P[X=x]. However this association doesn’t tell us anything about whether X causes Y or Y causes X. Causality is concerned with identifying the data-generating process, which describes the reason for a particular result. More than conditional probabilities, we want to know whether X causes Y or Y causes X. Usually an experiment with an intervention is required to discern this relationship. Relationships are usually represented as a directed acyclic graph, which is paramount to this field of study.

[![Screen Shot 2023-01-18 at 3.46.13 PM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/b/b423dac332fdba79c74c66789444acdc2953f696_2_690x171.png)Screen Shot 2023-01-18 at 3.46.13 PM2236×556 68.6 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/b/b423dac332fdba79c74c66789444acdc2953f696.png> "Screen Shot 2023-01-18 at 3.46.13 PM")

The rest of the text delves deeper into basic science in a clear way, describing how causal relationships are usually discovered by scientists. It goes on to describe some basic flaws in traditional econometric literature. There is a great section describing the various types of spurious factors that can be discovered with poor or incomplete experimental design. To me, a powerful, simple concept was that linear regression models imply a causal relationship. There are a couple software packages mentioned in the paper which aim to create causal graphs based only on observational data (PC algorithm and FCI algorithm).

A lot of ideas fit into general machine learning literature and indeed [a burgeoning field of study is concerned with integrating causality into ML](<https://arxiv.org/pdf/2206.15475.pdf>). While causality still is pretty new to me, the concepts appear to make a lot of sense for financial data science. Causal models are interpretable by explicitly explaining the data-generation process with a graph, and this is supposed to address issues with out-of-sample generalization. Another benefit is that a causal model is always potentially falsifiable by experiment, which is another hallmark of sound scientific theory.

I am really interested to see what the community thinks about this topic and how it applies to our data science project.

Can we endeavor to make directed acyclic graphs of our models?  
Do we think it would actually help? Why?  
Has anyone tried causality with ML or finance and has it helped?

For further reading check out the links above and

  * Riccardo Rebonato - _Coherent Stress Testing: A Bayesian Approach to the Analysis of Financial Stress_

  * Riccardo Rebonato and Alexandre Denev - _Portfolio Management under Stress: A Bayesian-Net Approach to Coherent Asset Allocation_

  * De Prado - _Machine Learning for Asset Managers_

---

### Post #2 — **dzheng1887** | 2023-01-19 01:34 UTC

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/forum.numer.ai/jefferythewind/48/3270_2.png) jefferythewind:

> to make directed acyclic graphs of our models?  
>  Do we think it would actually help? Why?  
>  Has anyone tried causality

This is an interesting post. Thank you for sharing. However, for the sake of prediction, I believe association may be enough. You would only be interested in casual impacts if, like you mentioned, you are mainly concerned of the effect on Y if some actor made some change to X. For example, the Federal Reserve would be interested in what happens to CPI and GDP for each unit increase in the Fed Funds rate. In the Rebonato links, he seems concerned about portfolio returns (Y) to some macroeconomic shock (X). A simpler framework to think through may be something found here: [Monetary Policy Surprises, Credit Costs, and Economic Activity - American Economic Association](<https://www.aeaweb.org/articles?id=10.1257/mac.20130329>)

A second point is that even if you are able to model most dynamics using a directed acyclic graph, the main issue is usually a lack of data for confounding variables Z. In that, for example, it would be onerous to collect data on Z or the nature of Z is too subjective (although relevant) to be quantifiable.

Ideally, if you would like to build a causal model for whatever reason, you would need what is considerd “exogenous variation” in your X variables. The paradigm linear example would be an instrumental variable approach. You can also think of random sampling for an A/B test as an instrumental variable that 100% correlates with treatment. However, I have never tested this, but I believe once you identified the exogenous variation, you can just treat it like any other variation that you use in your models.

That is at least how I understand it. Please let me hear your thoughts if different. Thanks.

---

### Post #3 — **jefferythewind** | 2023-01-19 20:40 UTC _(reply to #2)_

That’s some great insight. Yes I agree it seems a lot of the difficulty in finance and ML with applying these causal models is that we just have our data sets which are somewhat “flat”. In the context of supervised ML, we have our input data and our target variables. The targets are in the future and input comes from the past, so we aren’t worried that the direction of the causal graph goes backward in time. Instead we should be worried that we are predicting based on an association that turns out to be spurious, ie. we observe the association in the past training data but this association no-longer exists in the future. I am interested in understanding whether there are tools in the causal toolbox to help us identify these potentially dangerous associations. Perhaps there are confounders present in the input data itself? This is in the spirit of improving the generalization ability of our models in a scientific way.

Indeed the idea of identifying macroeconomic confounders is very interesting as well, and maybe even more promising than what I described above. Now that we have weekly data updates, it seems feasible that we could connect some outside data, like macro data, along the same time axis as our tournament data. This may provide us with some variables with exogenous variation.

---

### Post #4 — **mundan** | 2023-01-20 19:02 UTC

Here are my two cents

My limited understanding of causal inference is that you need second level information to get second level conclusions. See [On Pearl’s Hierarchy and  
the Foundations of Causal  
Inference]

In other words, you need causality priors, and unless you break the anonymity of the features and build a proper model of all the stocks (specifying which variables don’t affect others) that’s something you don’t have.

The problem in numerai is supervised learning and a lot of effort goes on making it tabular ml. I don’t see how to build causality into it, but I’m open to be mistaken

---

### Post #5 — **liz** | 2023-01-23 01:05 UTC _(reply to #4)_

for anyone interested, here’s a link to [The Foundations of Causal Inference](<https://ftp.cs.ucla.edu/pub/stat_ser/r355-reprint.pdf>).
