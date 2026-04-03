---
title: "Synthetic data generation using GANs"
category: Data Science
url: https://forum.numer.ai/t/synthetic-data-generation-using-gans/4040
created_at: 2021-09-05T22:57:20.276000+00:00
last_posted_at: 2021-09-06T21:59:28.444000+00:00
posts_count: 9
views: 2484
tags: []
---

# Synthetic data generation using GANs

---

### Post #1 — **rtachinardi** | 2021-09-05 22:57 UTC

On traditional quant projects, synthetic data generation to support backtesting is becoming a common practice, there is a good summary of it in the appendix A of “Machine Learning for Asset Managers”, by Marcos Lopez de Prado.

We can use various different methods to generate synthetic data, one of the most promising ones is GANs (Generative Adversarial Networks).

I have searched for discussions on the forum about this topic but couldn’t find any, so I’m posting this to bring it up. What do you think? Could it be useful in numerai?

---

### Post #2 — **yxbot** | 2021-09-06 11:44 UTC

here is a repo that provides some good sources for using GAN to generate synthetic data:

[github.com](<https://github.com/BorealisAI/private-data-generation>)

![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/5/551768bf9634bc5587abe78acc4924c5a05051ef_2_690x344.png)

### [GitHub - BorealisAI/private-data-generation: A toolbox for differentially private data...](<https://github.com/BorealisAI/private-data-generation>)

A toolbox for differentially private data generation

Haven’t tried this out though, I nearly used the Pate-Gan model in one of my work projects previously, but in the end didn’t bother.

---

### Post #3 — **rtachinardi** | 2021-09-06 14:49 UTC _(reply to #2)_

Thank you for the tip, I will check it out.

Instead of using GANs are you using any other techniques to generate synthetic data? Or would you say these are not needed in the tournament?

---

### Post #4 — **yxbot** | 2021-09-06 14:52 UTC _(reply to #3)_

no, I haven’t tried such approach so far. and probably won’t be doing it due to the fact that they are releasing a larger dataset soon. Also, I have been pretty happy with my models so far ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=9)

I would wait till the new dataset arrivate anyway, because there will be additional validation data to play with

---

### Post #5 — **jacob_stahl** | 2021-09-06 21:04 UTC

I’m curious about how effective this would be. Is there a sanity test you can use on the synthetic samples to verify that they reflect patterns in the dataset? You can’t eyeball them like image GANs.

---

### Post #6 — **rtachinardi** | 2021-09-06 21:20 UTC _(reply to #4)_

Oh, I didn’t know that. Do you have any links to posts about this new dataset?

---

### Post #7 — **rtachinardi** | 2021-09-06 21:29 UTC _(reply to #5)_

Yes, there is, but they’re fairly more complex than for other types of non-time series data (like images).

Here’s an example:

[ ![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/d/db24ac727e9fb8c41ace9d2cd7f609073e44eccf.jpeg) ](<https://www.youtube.com/watch?v=ROLugVqjf00&t=95s>)

And you can find the source code here:

[github.com](<https://github.com/CasperHogenboom/WGAN_financial_time-series>)

![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/0/0f4e67c7fb9ef610d0fa1c69b02760755c49d93d_2_690x344.png)

### [GitHub - CasperHogenboom/WGAN_financial_time-series: Thesis project done on Generation Financial...](<https://github.com/CasperHogenboom/WGAN_financial_time-series>)

Thesis project done on Generation Financial Time-Series with GANs. The project was a collaboration between Wholesale Banking Advanced Analytics team with ING and University Maastricht.

Marcos Lopez de Prado books (“Advances in Financial Machine Learning” and “Machine Learning for Asset Managers”) also have discussions about this problem, but unfortunately they aren’t available online for free, so I can’t link them.

---

### Post #8 — **yxbot** | 2021-09-06 21:44 UTC _(reply to #6)_

there have been plenty of chatters on rocket chat, the released date is supposed to be 8th Sep, so in 2 days time. They also say there will be a post in the forum.

Have a look at this [link](<https://community.numer.ai/channel/general?msg=zyoqnve9ZLxc6rm4g>)  
and this [tweet](<https://twitter.com/richardcraib/status/1430237139472719873>)

---

### Post #9 — **rtachinardi** | 2021-09-06 21:59 UTC _(reply to #8)_

Thank you very much, I will take a look!
