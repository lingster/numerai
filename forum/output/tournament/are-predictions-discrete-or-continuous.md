---
title: "Are predictions discrete or continuous?"
category: Tournament
url: https://forum.numer.ai/t/are-predictions-discrete-or-continuous/1157
created_at: 2020-11-06T17:52:54.618000+00:00
last_posted_at: 2021-05-22T05:56:28.695000+00:00
posts_count: 20
views: 4047
tags: []
---

# Are predictions discrete or continuous?

---

### Post #1 — **daot** | 2020-11-06 17:52 UTC

Hello,

Noob here. Inspecting the file `example_predictions_target_kazutsugi.csv`, I see a column with decimal numbers. For example:

n0003aa52cab36c2 | 0.48416  
---|---  
n000920ed083903f | 0.47641  
n0038e640522c4a6 | 0.53401  
  
However the training and validation data has discrete values for the target, i.e. target_value ⊂ {0,0.25,0.5, 0.75, 1}. Also, the number of rows is very different: Whereas there are only about 5000 **data_type** =“live” rows in the tournament_data, there are about 1.6 million lines in the example.

Clearly I am confused about the meaning of either the target or the `example_predictions_target`. Could somebody clarify what the format of the predictions should be?

---

### Post #2 — **wigglemuse** | 2020-11-06 18:22 UTC

The example predictions file you are looking at is a valid submission file. You could upload it right now and it would be accepted. So that’s what it is supposed to be like – it includes ALL of the rows in the “tournament” data file (i.e. submit predictions for that entire file.) But the only new data each week is the “live” data, so if your model doesn’t change from week to week you can work out your system so you don’t need to predict the entire thing every time. Just depends how fast your model runs and the resources it needs if you need to fuss about that. (Last week’s live data is added to the end of the tournament file each week as a new test era.)

As far as your predictions, they should be in the range of 0-1 just like in the example file. But yes, the training data only uses 5 discrete values/buckets for the targets. Nevertheless, your predictions should be real valued and ideally not contain any ties (they will be broken by row order, i.e. essentially randomly).

Oh, and in about a week we are getting new validation eras and moving to a target with a different distribution (but still only has discrete training values) so what I’ve just said about the file being relatively stable won’t be true on the round that starts Nov 14. On that round, you’ll see some test eras disappear and some new validation eras be added. Keep on eye on this forum and the rocketchat for the latest changes.

---

### Post #3 — **daot** | 2020-11-06 18:42 UTC _(reply to #2)_

Thank you for the detailed reply [@wigglemuse](</u/wigglemuse>). So just to clarify, what is the intuitive meaning of each target value? What would the following row mean

> **n0003aa52cab36c2** 0.48416

with respect to 0, 0.25, 0.5, 0.75, 1?

> your predictions should […] not contain any **ties**

What are ties? or what would be an example of a prediction containing ties?

---

### Post #4 — **wigglemuse** | 2020-11-06 19:08 UTC _(reply to #3)_

You are scored on ranking correlation PER ERA. Each era has about 5000 rows. When I say you should not have ties I mean for that 5000 row era you should have 5000 different values, not 1000 0.0s, and 1000 .0.25, etc – each of your predictions should be unique. (So to answer your original question predictions are continuous and not discrete even though the training targets are discrete.) And again, you are scored on rank so the values don’t really have intuitive meanings, only the order of them. If there were only 5 rows in the era, then 0.1, 0.2, 0.3, 0.4, 0.5 would get the exact same score as 0.6, 0.62, 0.8, 0.85, 0.99 because they are in the same ranking order (and with no ties).

---

### Post #5 — **daot** | 2020-11-09 20:26 UTC

I’m afraid it’s still unclear to me where the advantage of unique (or strictly ordered) predictions lies. Perhaps I don’t quite understand what we are trying to predict.

To try to flesh out my question, assuming the `numerai_score` is indeed calculated as:
    
    
    rank_pred = y_pred.groupby(eras).apply(lambda x: x.rank(pct=True, method="first"))
    numpy.corrcoef(y_true, rank_pred)[0,1]
    

We are trying to find the pearson product-moment correlation coefficients between the target and our prediction. To look at a concrete example. In the numerai example data, 400 rows of target in the first era look like this:  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/10724d6e74f584cda8c55d9851802028b95e3348_2_690x181.png)image1153×303 131 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/10724d6e74f584cda8c55d9851802028b95e3348.png> "image")

  
and the prediction of a linear regression looks like this:  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/01dead88c1d9fabad1c4cd50d0aa6a30bbca8cf0_2_517x135.png)image1159×303 77.9 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/01dead88c1d9fabad1c4cd50d0aa6a30bbca8cf0.png> "image")

  
which after ranking becomes:  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/aac120e8ad53a290fe21787d1d8c5a242e15440e_2_690x181.png)image1153×303 123 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/aac120e8ad53a290fe21787d1d8c5a242e15440e.png> "image")

  
We then calculate the correlation.

Why wouldn’t a perfect discrete prediction that matches exactly the target work best? Let’s take a toy example where my model is _god-like_ and predicts the output perfectly:
    
    
    t = numpy.array([0,0.25,0.5,0.25,0.25,0.75,1]) # target
    pre = numpy.array([0,0.25,0.5,0.25,0.25,0.75,1]) # prediction
    

If I rank and calculate correlations with:
    
    
    pre_rank = pandas.DataFrame(pre).apply(lambda x: x.rank(pct=True, method="first"))
    numpy.corrcoef(t, pre_rank.T)[0,1]
    

I get a `numerai_score` of 0.95:  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/0b690cdac665af5b78ae234119959747056d3f6b.png)image372×248 12.4 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/0b690cdac665af5b78ae234119959747056d3f6b.png> "image")

If I instead construct a prediction which is directionally correct (goes up and down when the target does), but has repeated values (**has ties**) I still get the same score:  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/5d9716449aac38fb783bf7eb322b6bc6db52f84f.png)image372×248 11.9 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/5d9716449aac38fb783bf7eb322b6bc6db52f84f.png> "image")

If I remove the ties in the prediction, nothing changes in the score. For example, using
    
    
    pre = numpy.array([0,0.2, 0.4, 0.3, 0.35, 0.6, 0.8])
    

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/d6ab9759f81e1106e33a9dcfdd8fa8f228980374.png)image372×248 11.9 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/d6ab9759f81e1106e33a9dcfdd8fa8f228980374.png> "image")

Equally, introducing errors in the 3 cases above (perfect prediction, monotonically correct prediction with ties, monotonically correct prediction without ties) seems to give equal scores.

With that little exploration, I’m back to my original question: Why can’t the submission look like the target, … in other words, a column with just the 5 possible values between 0 and 1? It seems the `numerai_score` in the documentation would allow it.

I would appreciate any insights you may have to help me what I am missing. Thank you.

---

### Post #6 — **wigglemuse** | 2020-11-09 21:20 UTC

I’m not making any theoretical statements about where advantage may be, or if they are using the “correct” scoring model. I’m telling you how the scores are generated. They break the ties in your predictions (that’s what the “first” does in the line of code there you posted – it breaks the ties by row order). But they don’t break the ties in the targets – they are left just as they are with only 5 discrete values. And then they do pearson correlation of those two vectors to get your correlation score. So you _CAN_ have only 5 discrete values in your predictions if you want, it just isn’t smart because the ties in your predictions will be broken essentially randomly (by row order, but row order has no meaning in this data).

So if your predictions are {.25,.25,.25,.5,.5,.5,.75,.75,.75} then they are converted to {1,2,3,4,5,6,7,8,9} for scoring (i.e. no ties). So now the .25 in the 3rd position is considered to be after the .25 in the 1st position just because that’s the order of the rows. But any decent model will be able to make much finer and better distinctions between rows, so submitting predictions like {.3, .2, .25, .46,.52,.51, .68, .81,. 74} is much better because now you’ve controlled the ranks they are going to end up with {3,1,2,4,6,5,7,9,8} instead of leaving it up to chance which can lead to wildly different scores just depending on the row order (if you have a large number of ties – a few ties isn’t so bad). [In your example I think you broke the ties but not in such a way that the order changed.] And the row order is fixed, you can’t submit rows in a different order. So let your model be the best that it can be under this system without a random component to your score and don’t have ties in your predictions…

---

### Post #7 — **daot** | 2020-11-10 01:39 UTC

Thank you [@wigglemuse](</u/wigglemuse>), that was a clear explanation which helped me understand what you meant.

I tried to test the idea with twice your series. But:  
`{.3, .2, .25, .46,.52,.51, .68, .81,. 74,.3, .2, .25, .46,.52,.51, .68, .81,. 74} -> ranked as: {0.278 , 0.056 , 0.167 , 0.389 , 0.611 , 0.5 , 0.722 , 0.944 , 0.833 , 0.333 , 0.111 , 0.222 , 0.444 , 0.667 , 0.556 , 0.778 , 1.0 , 0.889 , }`

gives the same score as:  
`{.25,.25,.25,.5,.5,.5,.75,.75,.75,.25,.25,.25,.5,.5,.5,.75,.75,.75} -> ranked as {0.056 , 0.111 , 0.167 , 0.389 , 0.444 , 0.5 , 0.722 , 0.778 , 0.833 , 0.222 , 0.278 , 0.333 , 0.556 , 0.611 , 0.667 , 0.889 , 0.944 , 1.0}`

Graphically, it would be the difference between:  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/d52248f8bdef9d3bf517736f61aa017a5ea72ff7.png)image376×248 12.9 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/d52248f8bdef9d3bf517736f61aa017a5ea72ff7.png> "image")

and 

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/0f6524f7b44ff98b99934aed00dc218579aef9a0.png)image376×248 15.7 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/0f6524f7b44ff98b99934aed00dc218579aef9a0.png> "image")

But perhaps the differences will show with a larger dataset? or when prediction and target are much less correlated? I will explore further and post here if I gain any further insights.

---

### Post #8 — **wigglemuse** | 2020-11-14 17:18 UTC _(reply to #7)_

Yes, with tiny samples there are lots of ways to get the same correlation score. In the real tournament the typical era has around 5000 rows and you are lucky to get 5% positive correlation.

---

### Post #9 — **factorsparsity** | 2021-02-28 21:04 UTC

Hi, I’ve just started the passage through the learning curve and while I was reading this very interesting thread I was wondering… Do you have any further insights?  
One thing is not yet clear to me: So, according to what you are saying and what I read in the documentation, the predictions are ranked (pct, first) and then correlated with the ranked target. It therefore makes a difference whether the predictions are discrete (0,0.25,0.5,0.75,1) or continuous. But do we know if the target is discrete or continuous at this point?

---

### Post #10 — **wigglemuse** | 2021-02-28 22:13 UTC

The targets you are scored against are just the same as they are in the training data. And they are not ranked – they are left just as they are.

p = your predictions  
t = targets

So, to score:  
p = rank(p,ties.method=“first”)  
score = cor(p,t)

That’s it.

So this is why I say you shouldn’t have (many) ties in your predictions – they are just going to get broken automatically and randomly (in the sense that row order has no predictive value), so you might as well break them yourself intelligently. And if you submitted ONLY 5 discrete values, your score would be have a huge random component – if you don’t believe me just try some examples yourself ranking with “first”, “last”, and “random” and see how some of the scores are hugely different just because of the different tie-breaking.

---

### Post #11 — **profricecake** | 2021-05-18 03:09 UTC

Hi all. Thought experiment for you. What do you think the spearman correlation should be between the target column and itself?

Come on, this is easy. They’re two identical columns, right? No-brainer. The answer should be 1.0.

Sadly, that’s not what you get if you pass in two copies of the target column to this ubiquitous scoring method from `example_model.py`:
    
    
    # Submissions are scored by spearman correlation
    def correlation(predictions, targets):
        ranked_preds = predictions.rank(pct=True, method="first")
        return np.corrcoef(ranked_preds, targets)[0, 1]
    

You don’t get 1.0. You get 0.91.
    
    
    correlation( valid_df[ "target"], valid_df[ "target"])
    > 0.9099594540994242
    

It happens because however the target values are ranked, it’s not by any built-in method that comes with pandas. Every time I rank a series using `pandas.Series.rank()` and then rank it again with identical settings, I get a perfect match. In other words, once a series has been ranked by pandas, re-ranking it with the same settings leaves it unchanged.

Not so for the target values. Re-ranking those values gives a different series no matter what method I choose from `pandas.Series.rank()`.

I get the expected result when I don’t re-rank:
    
    
    np.corrcoef( valid_df["target"], valid_df["target"])[ 0, 1]
    > 1.0
    

In conclusion, whatever ranking method Numerai uses on the target values does not seem to be an option in `pandas.Series.rank()`. And I find that a little frustrating, because it means that passing two identical columns to the Numerai-provided `correlation()` function does not return 1.0.

prc

---

### Post #12 — **wigglemuse** | 2021-05-18 03:18 UTC

That is correct. The targets are not ranked (i.e. ties are never broken), and the theoretical maximum score we can achieve is in fact 0.91 (not that you’ll ever get close).

---

### Post #13 — **profricecake** | 2021-05-18 17:08 UTC _(reply to #12)_

Ranked sequences can have ties, there’s nothing strange or illegal about that. Indeed, there are many options in `pandas.Series.rank()` for how to manage (and preserve) ties in rank. So having ties in a series doesn’t mean that it isn’t ranked.

But who am I, right? I’ll let [@jrb](</u/jrb>) chime in:

![](http://forum.numer.ai/user_avatar/forum.numer.ai/jrb/48/2767_2.png)[A more clear understanding of the Ranked Correlation](<http://forum.numer.ai/t/a-more-clear-understanding-of-the-ranked-correlation/1387/2>)

> The targets are already ranked, all you need to do is rank your predictions and then compute Pearson’s correlation coefficient between your ranked predictions and the targets.

Are the targets ranked or not? We have two more senior folks here in disagreement ([@wigglemuse](</u/wigglemuse>) [@jrb](</u/jrb>)). Maybe you two can work it out publicly so the rest of us can benefit from the debate?

I’m sticking with the idea that they are ranked, using a method of handling ties similar - but not quite the same - as the pandas “dense” method. If I’m right, I’d like to see the true ranking code shared. Because it seems strange to me to compute the Spearman between sequences that were ranked using different techniques for resolving ties.

I did discover that if I compute the Spearman between the targets and the targets re-ranked using panda’s “dense” method, I do finally get a correlation coefficient of 1.0, which is nice. Even though the resulting re-ranked sequence doesn’t match the original sequence.
    
    
    def correlation(predictions, targets):
        ranked_preds = predictions.rank(pct=True, method="dense")
        return np.corrcoef(ranked_preds, targets)[0, 1]
    
    correlation( valid_df[ "target"], valid_df[ "target"])
    > 0.99999999999
    

I’m sure someone will object to this change of ranking methods, even though it feels right to have the targets be 100% correlated with themselves.

---

### Post #14 — **wigglemuse** | 2021-05-18 17:25 UTC

I mean nothing further is done to the targets for scoring – they are just left as-is. They are already 5 discrete equally-spaced values, so yes they are “ranked” in that way. Whereas the predictions the ties are broken (by “first” method). And then pearson corr is done on those two vectors, just as jrb said above and I’ve said a gazillion times. (True spearman correlation is actually never used in scoring, despite being referred to very often.) This has been discussed a million times around here, and the actual scoring code is posted. (And why are you always trying to tell me I’m wrong when I give you simple known facts about the tournament? I don’t make things up.)

You can even see in this thread [New Target Nomi Release](<http://forum.numer.ai/t/new-target-nomi-release/959>) that I pointed out the 0.91 thing when we switched from the old target (where the max score was 0.98).

---

### Post #15 — **profricecake** | 2021-05-19 02:53 UTC _(reply to #14)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/wigglemuse/48/3094_2.png) wigglemuse:

> You can even see in this thread [New Target Nomi Release ](<http://forum.numer.ai/t/new-target-nomi-release/959>) that I pointed out the 0.91 thing when we switched from the old target (where the max score was 0.98).

The 0.91 thing seems to bother us both, but for different reasons.

You wrote with concern about its impact on payouts compared to the previous system. I’m bothered by the unintuitive nature of the fact that you don’t get 1.0 if you score the targets against themselves using the `correlation()` function in the example code.

The purist in me believes that two identical series should have a corr of 1.0 if we’re going to call it a corr. This could be done by either changing how the targets are ranked to the `method="first"` approach used in the example `correlation()` function, or changing the example `correlation()` function to use the same ranking system that is used on the targets now. The latter probably makes more sense, because everyone already trains on the 0, 0.25, 0.5, 0.75, and 1.0 targets. But making a fundamental change in the scoring measure like this could have tourney implications that are too big to grapple with. I wouldn’t know. Still, I wanted to throw a vote to clean this oddity up so that we have sane correlation numbers in the future.

And now for something completely different…

![](http://forum.numer.ai/user_avatar/forum.numer.ai/wigglemuse/48/3094_2.png) wigglemuse:

> And why are you always trying to tell me I’m wrong when I give you simple known facts about the tournament? I don’t make things up.

[@wigglemuse](</u/wigglemuse>) You have styled yourself as something of an educator here. I chalk this up to your love for the tourney, your interest in helping people out, and your vast knowledge of all things Numerai.

But when you write something like:

![](http://forum.numer.ai/user_avatar/forum.numer.ai/wigglemuse/48/3094_2.png) wigglemuse:

> The targets are not ranked

… that flies in the face of what other well-informed senior posters have written and also common sense, I will call you out for it. I do this because I want to know the real answers, and also because these are permanent records (more permanent than RocketChat at least) that will either help future tourney participants or confuse them further.

If in one post you say they aren’t ranked, and in the next you write:

![](http://forum.numer.ai/user_avatar/forum.numer.ai/wigglemuse/48/3094_2.png) wigglemuse:

> yes they are “ranked”

… you muddy the signal with noise. (Editor’s note: the targets are actually ranked, not “ranked.”)

For the record: I’m someone who takes what you write seriously because I’m seeking information and you’re offering it. I’m paying attention. I appreciate it when you illuminate something that I’ve been struggling to understand. That’s happened multiple times around here already, most recently regarding stake reduction. But I’m not going to smile and nod if you say stuff that doesn’t sit right or that demands further explication.

If you want people to believe what you say without question then you’ve chosen the wrong role for yourself. Educators should expect students to poke holes in their claims and demand more evidence. Real learning requires interrogation, not blind acceptance. So instead of taking it personally, I encourage you to see it as a compliment that I am taking what you say you seriously.

---

### Post #16 — **wigglemuse** | 2021-05-19 03:32 UTC

…and if you want people to engage with your questions at all, you shouldn’t act like a tool and make insinuating insults instead of just normal back-and-forth clarifying questions.

---

### Post #17 — **jrb** | 2021-05-20 11:47 UTC _(reply to #12)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/wigglemuse/48/3094_2.png) wigglemuse:

> The targets are not ranked (i.e. ties are never broken)

Apples and Oranges. What does ranking have to do with tie breaking? They’re not the same thing. Someone from the team could correct me if I’m wrong, but AFAIK the targets are discretized ranks. And they’re discretized to prevent us from overfitting on the targets.

---

### Post #18 — **mindyoself** | 2021-05-20 12:13 UTC

As a newby check out Arbitrages videos if you haven’t already.

---

### Post #19 — **wigglemuse** | 2021-05-20 13:50 UTC _(reply to #17)_

I’m talking about the scoring code – the targets do not go through a “ranking process” like the predictions at score time in the code. That’s all. The targets are already ranked when given to us – they are left alone after that. And that confuses people because the predictions aren’t and the ranking process the predictions go through is _different_ than the one that may or may not have been previously applied to the targets, and that’s where the ties come in – the predictions end up having no ties, but the targets keep theirs. So when we just say something is “ranked” it is unclear because we’ve got two different ways of doing that: one with ties, one without; one explicitly in code shown to us, one unseen (done beforehand) on raw data That’s pretty much the sole point I’ve ever made about this ranking stuff, although I’ve made it a lot of times because it gets brought up a lot. It is a super simple point, and there isn’t an ounce of opinion in it. Just a super simple technical point – predictions ranked with ties removed, targets left alone and ties remain. The end.

---

### Post #20 — **profricecake** | 2021-05-22 05:56 UTC _(reply to #16)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/wigglemuse/48/3094_2.png) wigglemuse:

> you shouldn’t act like a tool and make insinuating insults

Wow! You insult me in the same breath that you encourage me not to make insults.

Of course, I can’t find examples in my posts where I’ve actually insulted you, but hey, I get it. It sucks when someone points out that you’ve written something inaccurate, or hypocritical, or confusing. But it’s not _actually_ an insult. Like, I’m not trashing your character, I’m just interrogating what you’ve written. I could certainly insult you–I could call you a “tool” for example–but I’d have to be willing to violate the [Forum Guidelines](<http://forum.numer.ai/guidelines>) and I’m not.
