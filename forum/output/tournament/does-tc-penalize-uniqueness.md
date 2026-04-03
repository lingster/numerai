---
title: "Does TC penalize uniqueness?"
category: Tournament
url: https://forum.numer.ai/t/does-tc-penalize-uniqueness/5575
created_at: 2022-07-18T08:16:52.263000+00:00
last_posted_at: 2022-07-20T08:39:07.195000+00:00
posts_count: 10
views: 936
tags: []
---

# Does TC penalize uniqueness?

---

### Post #1 — **sneaky** | 2022-07-18 08:16 UTC

Hi,  
I had this thought experiment about the TC metric. How is it possible to have every other metric over 79 percentile and still have TC bellow 2 percentile? Could it be that TC penalizes uniqueness? I would like to discuss whether my thought process is correct. I think that a metric like TC is needed; however, I don’t think that penalizing uniqueness is good.

_Disclaimer: I don’t know if I understand correctly how TC works._

##### Real world example: Round 323 | model: MINMAX2 | jul 16
    
    
    metric      | CORR   |  MMC   |  FNC   | FNCV3  |   TC
    val         | 0.0241 | 0.0135 | 0.0257 | 0.0146 | -0.07594 
    percentile  | 84.8   | 86.7   | 92.3   | 79.9   |  1.8 
    

### Does TC penalize uniqueness?

#### Setup

Let’s have:

Y = [ 1 , 2, 3, 4, 5, 6, 7, 8, 9, 10] ← Ground truth rank  
A = [**10** , **9** , 3, 4, 5, 6, 7, 8, **1** , **2** ] ← Average model rank  
U = [ 1 , **9** , **8** , 4, 5, 6, 7, **3** , **2** , 10] ← Unique model rank

U has way better correlation and prediction than A:  
spearman(A,Y) =~ **-0.56**  
spearman(U,Y) =~ **0.1**

#### Metamodels

_Now if I understand it correctly, TC is just a gradient between the metamodel and the metamodel without the measured model._  
So, let’s assume metamodels Mu and M, where M is Mu without U:

M = [35. 31.5 10.5 14. 17.5 21. 24.5 28. 3.5 7. ] = 3.5 * A  
Mu = [36. 40.5 18.5 18. 22.5 27. 31.5 31. 5.5 17. ] = 3.5 * A + U

Mr = [10, 9, 3, 4, 5, 6, 7, 8, 1, 2] ← M rank (Average model rank without change)  
Mur=[ **9** ,**10** , **4** , **3** , 5, 6, **8** , **7** , 1, 2] ← Mu rank

sMr = spearman(Mr,Y) =~ **-0.56**  
sMru = spearman(Mur,Y) =~ **-0.57**

**gradient = sMru - sMr = -0.012 =? TC**

#### Conclusion

_Adding U rank to M makes the metamodel M worse. Why? Because U had enough strength to flip**4** and **3** , **8 and 7** , which makes the ranking worse, and swapping **10** and **9** is not enough. Could this situation happen with the real TC?_

---

### Post #2 — **sunkay** | 2022-07-18 13:58 UTC

I also wonder how could this happen.

But I think you should use prediction value(between 0 and 1) instead of rank when calculating correlation and stake weighted meta model.

---

### Post #3 — **sunkay** | 2022-07-18 14:03 UTC

And I wonder, is it possible that increasing the stake a bit makes the meta model worse, but increasing the stake a lot make the meta model better?

---

### Post #4 — **restrading** | 2022-07-18 14:13 UTC

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/s/4bbf92/48.png) sneaky:

> Now if I understand it correctly, TC is just a gradient between the metamodel and the metamodel without the measured model.

Not quite, in my understanding TC is the gradient of portfolio return post-optimization wrt. the model’s stake.

The implication is that the extreme predictions after their optimization is going to affect the TC the most even though you could do well on CORR with non-extreme predictions.

---

### Post #5 — **sneaky** | 2022-07-18 20:57 UTC _(reply to #4)_

What do you mean by extreme predictions?

---

### Post #6 — **jrai** | 2022-07-19 00:36 UTC _(reply to #5)_

CORR, MMC, FNC and FNCv3 scores are measured in “correlation space,” whereas TC is measured in “return space.” Correlation space has a well defined, tight distribution. Return space has fat tails.

A good example is ranking GME at the bottom of your list during its short squeeze. In correlation space, your scores won’t be heavily impacted by having ranked GME at the bottom of your list if it goes up 100%, but in return space your score will be severely impacted by it.

---

### Post #7 — **restrading** | 2022-07-19 01:41 UTC _(reply to #5)_

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/s/4bbf92/48.png) sneaky:

> What do you mean by extreme predictions?

You might do well on stocks that ends up 0.25-0.75 before portfolio optimization, but not so well on stocks that ends up on the top/bottom percentiles post portfolio optimization.

---

### Post #8 — **sneaky** | 2022-07-19 06:27 UTC _(reply to #6)_

But my example still holds right? I just have to apply “random” weights as profits to the ranked items as profit/loss, and if flipping 10 and 9 is lesser profit than flipping the other two pairs combined, then I get penalize for better prediction as well, or am I missing something?

---

### Post #9 — **dzheng1887** | 2022-07-19 18:47 UTC _(reply to #6)_

This sounds like you are making a distinction between ranked correlations and return correlations. This is actually something we can simulate on our end, like what kind of scenarios would bring about high CORR/MMC and low TC.

I doubt is can be due to one stock out of thousands though. Maybe a group of stocks if you happen to be unlucky (or lucky). I think it is more likely that the model is keying in on places where the hedge fund cannot use it due to their risk mitigation/operating procedures like they mention in their reason for the introduction to TC. I think this argument, though, is more the difference in CORR vs TC volatility.

It could also be, the model is keying in on areas where the gradient is more or less flat as there is already good coverage on these stocks from other models. So you still have good CORR as every model will find it, but average TC. However, the example above is negative TC.

---

### Post #10 — **autratec** | 2022-07-20 08:39 UTC

one observation. if i add feature filtering step in the model, say reduce the feature from 310 to 120 based on their importance, the TC will be more unstable: ±0.1, comparing with full feature model: ±0.01.
