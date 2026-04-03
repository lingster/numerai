---
title: "Is TC slowing down your research and experimentation?"
category: Data Science
url: https://forum.numer.ai/t/is-tc-slowing-down-your-research-and-experimentation/5619
created_at: 2022-08-01T14:11:16.202000+00:00
last_posted_at: 2022-12-02T14:45:48.522000+00:00
posts_count: 22
views: 1949
tags: []
---

# Is TC slowing down your research and experimentation?

---

### Post #1 — **taori** | 2022-08-01 14:11 UTC

I have just realized that since the introduction of TC my desire to experiment and try new things out is slowing down.

I have still many ideas, e.g. training on multiple targets, but knowing that I cannot compute TC for my models makes me carefully ponder every new development because I cannot access its quality (being good on corr it’s not enough for me anymore). When I want to evaluate a new model I need to create a tournament test entry and wait few months before being able to get a sense of the TC performance. Not only that is boring and slow, it is also wrong to access the TC on few recent entries only.

In the long run, I believe numerai will move away from corr and will focus only on a metric that make sense for their portfolio. That metric could be TC or something else, but they need to allow users to evaluate that metric during the R&D phase. They are probably already thinking at a solution, otherwise the research of new ideas will be negatively impacted.

Why am I writing this? Just for fun and because I am curious to hear what other users think.

---

### Post #2 — **wigglemuse** | 2022-08-01 14:18 UTC

It is not slowing me down from burning holes in my cpus running new things all the time as usual, but it is slowing me down from actually staking on them yeah.

---

### Post #3 — **restrading** | 2022-08-01 14:34 UTC _(reply to #2)_

It slows me down because it takes 2wks to see the first live TC and much longer needed to tell confidence, due to the lack of TC for late subs and lack of diagnostic tools.

I’ve mentioned in RocketChat: the only ones who can research methodically for TC (with good confidence) are the ones who already have models with good TC because they have long history of backfill TCs and just need to improve on those models. For the majority who are not so lucky including myself, it’s pretty much a shot in the dark and there’s no way to tell if a new model is good on TC until it has a (very) long history. So I only stake 0.5-1xTC on very few new models without much confidence.

---

### Post #4 — **shatteredx** | 2022-08-01 16:00 UTC

TC has actually spurred me to try many more crazy experiments. I was only using 1 model slot before TC, now I am at 34.

Instead of grinding huge ensembles trying to get more bits of CORR, I’m now rapidly rolling out the most diverse set of models that I can think of in the hopes of getting slices of the TC pie. It’s like panning for gold I suppose.

But yeah, I definitely agree with you that chasing recent TC performance is a big problem.

---

### Post #5 — **qeintelligence** | 2022-08-01 20:04 UTC _(reply to #4)_

its basically like finding needles in a haystack, but before with corr you could use a metal detector (metrics for validation) to find them more quickly. Basically either we need that metal detector again or we need to increase the number of needles, so give us more slots pls ;~)

---

### Post #6 — **autratec** | 2022-08-02 02:42 UTC

No slow down. Just ignore and don’t stake on it.

---

### Post #7 — **sneaky** | 2022-08-02 07:23 UTC

100 %, I am at least trying to optimize the metrics that are suppose to be correlated with good TC, but  
it is only getting worse. My best model at TC is the stupidest one that is trained on 1/5 of the training dataset.

---

### Post #8 — **eleven_sigma** | 2022-08-02 16:23 UTC _(reply to #7)_

Totally agree. After TC I have a lot of ideas parked. If I haven’t any way to check myself if a model is better or no I have no incentive to research.

---

### Post #10 — **sunkay** | 2022-08-05 02:21 UTC

In my opinion, TC has some problems that is need to change, so I don’t want to study it at the moment too.

---

### Post #11 — **yxbot** | 2022-08-05 15:12 UTC

I second [@qeintelligence](</u/qeintelligence>) , it is more the running out of model slots that is slowing me down - ideally, I want to have at least 500 slots - and probably run 5-10 variant on each base model that I can come up with ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=12)

---

### Post #12 — **svendaj** | 2022-11-26 13:20 UTC _(reply to #4)_

Your position on [leaderboard](<https://numer.ai/shatteredx>) shows that you are doing it right!

So is your [signature model](<https://numer.ai/shatteredx>) ansambl or best single idea?

---

### Post #13 — **kayeffnumeraitor** | 2022-11-26 14:14 UTC _(reply to #12)_

Bought predictions from numerbay, the original model is [this one](<https://numer.ai/paul_the_0ct0pus>)

---

### Post #14 — **jxtrbtk** | 2022-11-27 10:13 UTC

I have a model with just random predictions that I use as a kind of base line. And it keeps gaining points on the TC rank, achieving now rank 239, better than any of my other models. You can check it [there](<https://numer.ai/jxtr_i_03>) and even buy it [there](<https://numerbay.ai/product/numerai-predictions/jxtr_i_03>).  
Thus I’m not totally confortable either with this TC stuff !  
For sure my research have changed of direction, from big ensembles to more experimental unique models. And it’s true it’s not easy to find a compass to follow.  
But isn’t Numerai “the hardest data science competition in the world” ?

---

### Post #15 — **wigglemuse** | 2022-11-27 18:01 UTC _(reply to #14)_

It’s tough, it’s true! But…please don’t sell random predictions. We don’t have to share secrets if we’ve got any (which we probably don’t because TC is the way it is). But let’s not exploit each other and take money for nonsense, even nonsense that does randomly well at times.

---

### Post #16 — **nyuton** | 2022-11-28 08:18 UTC _(reply to #15)_

A random model might have some merits!  
Check it out! Corr and FNC are ~0. TC is stricktly positive and it’s beyond statistical significance.

The random noise can improve the metamodel, when the “trained” models do poorly. Which they often do.

---

### Post #17 — **kayeffnumeraitor** | 2022-11-28 09:36 UTC _(reply to #16)_

Yes I think the reason for that is the systematic error all models inhibit when they train on the limited data we have. If you upload random noise, you are guaranteed to be decoupled from the systematic error from the training data. However, you are then also decoupled from being correlated to the signal, especially in times when all other models are performing well.

While not TC but CORR20, you can see an example here from the models page overview from all of my models. For some reason the daily round 360 has an awful start where all models are tanking significantly in corr, but my `numpy.random.rand()` predictions are obviously unfazed by that (light blue curve at the top of round 360)  


[![grafik](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/4/44065dff829610ae40782c08ab72742a517581ca.png)grafik355×288 39.3 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/4/44065dff829610ae40782c08ab72742a517581ca.png> "grafik")

---

### Post #18 — **nyuton** | 2022-11-28 10:11 UTC _(reply to #17)_

Do you dare to stake on it?

---

### Post #19 — **murkyautomata** | 2022-11-28 10:22 UTC _(reply to #16)_

Remember that inverting predictions results in the exact opposite tc. Random predictions could have just as easily been the opposite random predictions.

---

### Post #20 — **eleven_sigma** | 2022-11-30 19:40 UTC _(reply to #19)_

Inverting predictions results in opposite correlation but both can have positive TC in case most of models performs badly.

---

### Post #21 — **kayeffnumeraitor** | 2022-11-30 22:14 UTC _(reply to #20)_

I haven’t done the experiment myself, but flipping predictions should result in the same tc with opposite sign, just as [@murkyautomata](</u/murkyautomata>) said, independent of others. I guess if others are really bad the random prediction should get a value close to zero, i.e. 0.01, so flipping it would result in -0.01, which is then almost as good and still better than -0.30 tc

---

### Post #22 — **gammarat** | 2022-12-02 02:56 UTC

In response to the OP’s question (_Is TC slowing down your research and experimentation?_), I would have to say no. It just changed the direction a bit. Well, more than a bit ![:laughing:](https://emoji.discourse-cdn.com/twitter/laughing.png?v=13) Plus I (finally) had to learn enough Python to do the dailies and interface it to MatLab, my usual programming tool. BTW, thanks to the Numerai team (_see below_) for actually making that easy!!! Works like a charm, and it only took a couple of days once I set out to do it.

I find it a really interesting project, and I don’t think it’s one Numerai can really provide training targets for But I do think that individuals can research it themselves in relation to their own analysis techniques.

I think an “trick” is to do what one can to move as far away from linear solutions techniques in general when developing a model to solve for _corr_. Just as an example, here’s a plot of my results comparing the _corrWMetaModel_ variable with TC:

[![MMcorrXtc](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/4/46d35ecbc8edfc137cd2ba44fbb1320fddeef93d_2_690x361.jpeg)MMcorrXtc884×463 56.4 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/4/46d35ecbc8edfc137cd2ba44fbb1320fddeef93d.jpeg> "MMcorrXtc")

The models from 255 to around 285 were quite linear, around then I started introducing Gaussian Mixture approaches, and then from 312 on a series of different GMs based on variations of genetic algorithms. From the second plot, these different techniques certainly affect the variance in the TC; the next step is to look for consistency.

ETA: with reference to whom to thank for the Python tools, I think that my thanks actually should go to [@uuazed](</u/uuazed>) and other contributors for making the package and doing the upkeep.

---

### Post #23 — **profricecake** | 2022-12-02 14:45 UTC _(reply to #14)_

Please sell your random predictions and I hope you make money off of them! If Numerai claims your predictions are valuable in the TC sense then you’ve discovered some alpha for the metamodel. Or you’ve discovered an issue with TC. Either way, good on you.

Whether we like it or not, the game now is to maximize TC. And since we don’t have a reliable metric to train for that incorporates the impact of the optimizer, Numerai is inviting a lot of dart-throwing. Thanks for sharing your edge case study.
