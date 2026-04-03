---
title: "Some Simple Tournament Questions"
category: Tournament
url: https://forum.numer.ai/t/some-simple-tournament-questions/2301
created_at: 2021-03-11T21:25:29.569000+00:00
last_posted_at: 2021-03-16T19:34:19.989000+00:00
posts_count: 13
views: 2017
tags: []
---

# Some Simple Tournament Questions

---

### Post #1 — **gammarat** | 2021-03-11 21:25 UTC

I’m newish to this, and I would just like to make sure I’m doing it right.

On the data:  
There’s training, validation, test, and live data types. The test data and the live data do not have valid target values. What is the test data for? Just to make sure my programs run?

On the tournament, if I am not staking my prediction, can I submit a prediction on the current live data after the the cutoff day, just to see how it runs over the remainder of the cycle?

If it makes any difference, I am running my programs at home from downloaded data, and not on the services that most seem to be using.

TIA;  
Chris

Ps. Pointers to appropriate FAQs would be fine.

---

### Post #2 — **wigglemuse** | 2021-03-11 22:38 UTC

Gonna take these questions in reverse order.

It doesn’t matter how you compute or how you submit (automated, api, direct upload). You are delivering a prediction file to Numerai one way or another, doesn’t matter how.

Even though there are 4 overlapping “open” rounds at any given time, only the most recent is eligible for submissions. So new data comes out each Saturday for a new round. For that submission to “count” – be stake eligible and to count towards your “rep” score, predictions must be submitted for that round before the Monday morning deadline. However, if you miss that deadline, you can still submit for that round up until the next round data comes out but it will be “late” (so you can submit monday through early saturday morning). But you can’t submit two weeks into a round for that round.

Important but confusing note: although you can overwrite your submission with a new upload during the submission window, the “before the deadline” and “after the deadline” windows are a bit different. If you submit something before the deadline (meaning on the weekend when the data comes out) so that it is an “on time” submission, you can’t replace that after monday morning (because it “counts”). However, if you wait until that deadline has passed so your submission is “late”, then you can replace it as many times as you want before the next round starts – some people do this just to see the diagnostics when they upload. So “late” submissions are possibly actually more useful for newbies if you think you want to replace your model while you are tinkering. You can replace an “on time” submission though while you are still in the “on time” window.

What is the test data for? Numerai internal backtesting and validation of your model. They need predictions for which they have the targets but you don’t (so you can’t overfit to it, it is clean).

---

### Post #3 — **datacryptoanalytics** | 2021-03-12 00:55 UTC _(reply to #2)_

Great [@wigglemuse](</u/wigglemuse>), very enlightening!

I had doubts about sending the predictions before and ended up adapting ways to analyze the predictions through Colab with help from the community here.

I am changing some things and soon I will make the link available in case anyone is interested.

---

### Post #4 — **gammarat** | 2021-03-12 04:12 UTC _(reply to #2)_

Thanks, [@wigglemuse](</u/wigglemuse>). I think my biggest problem is that I spent most of my career in very rigorously documented environment, so this is a bit of a change. I guess this old dog is going to learn some new tricks ![:dog:](http://forum.numer.ai/images/emoji/twitter/dog.png?v=12)

Re. this bit:

![](http://forum.numer.ai/user_avatar/forum.numer.ai/wigglemuse/48/3094_2.png) wigglemuse:

> What is the test data for? Numerai internal backtesting and validation of your model. They need predictions for which they have the targets but you don’t (so you can’t overfit to it, it is clean).

So I need to submit results to the tournament for the test data as well as the live data? I’m cool with that.

---

### Post #5 — **themicon** | 2021-03-12 08:49 UTC _(reply to #4)_

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/forum.numer.ai/gammarat/48/3281_2.png) gammarat:

> So I need to submit results to the tournament for the test data as well as the live data? I’m cool with that.

You need to submit predictions for everything in the “tournament” file, this includes test, validation and live.

---

### Post #6 — **gammarat** | 2021-03-12 15:39 UTC _(reply to #5)_

Thank you [@themicon](</u/themicon>), that cleared up a whole lot of other questions.

---

### Post #7 — **backe** | 2021-03-14 11:48 UTC

[@wigglemuse](</u/wigglemuse>) [@themicon](</u/themicon>)

Hi, I have two questions related to this topic:

  1. When I make a submission, is model diagnostic feedback calculated on validation or test data_type (or maybe both)?

  2. There was a talk in [Validation 2 Announcement](<http://forum.numer.ai/t/validation-2-announcement/166>) about validation1 and validation2 subsets. My question is are they 121-132 and 197-212 era clusters in the validation set?




Thanks.

---

### Post #8 — **wigglemuse** | 2021-03-14 16:32 UTC

Validation only, yes. So you could even compute all those yourself because you have the targets.

And yes, all the validation eras are included in the diagnostics.

---

### Post #9 — **gammarat** | 2021-03-16 14:57 UTC

Another simple question…  
Are the predictions for the Validation era Ids that are included in the _example_predictions.csv_ file samples of the measured values corresponding to those Ids, or the output of Numerai’s prediction model?

---

### Post #10 — **wigglemuse** | 2021-03-16 16:13 UTC

I don’t understand the first option, but the answer is the second option – it is just the model’s output for the whole tournament file including validation eras. (i.e. just like it would be if it were your model – except they truncate the decimal places which you shouldn’t do)

---

### Post #11 — **gammarat** | 2021-03-16 19:01 UTC _(reply to #10)_

I just got curious about what mapping Numerai uses to convert whatever actual measured values they have into the target values included in the _training_ and _tournament_ sets. I suspect that they take whatever the measured values are, they pass it through a normalization filter that translates the data into a distribution, such as a normal distribution, and then output that result fitted between 0 and 1. For example

I got curious because if you take the example predictions file, all of the results fall within [0.4217, 0.5652]. range. Which means, of course, if they simply use rounding to get bins like [0,0.25,0.5,0.75,1.0], all their results would fall into one bin (around 0.5).

FWIW, here’s a copy of the top of the _example_predictions.csv_ file:

> id,prediction  
>  n0003aa52cab36c2,0.48919  
>  n000920ed083903f,0.49109  
>  n0038e640522c4a6,0.53275  
>  n004ac94a87dc54b,0.50717  
>  …

and here’s what a histogram of the whole file looks like:  


[![estimates](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/728ca61aab931bfb81620973f69fb0c281e4021c.jpeg)estimates560×420 13.4 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/728ca61aab931bfb81620973f69fb0c281e4021c.jpeg> "estimates")

Now in my own predictions, I’m using a mixed regression/classification approach; below is a typical histogram of results based on the tournament data. (I’m taking that approach because it’s worked well for me in the past, it’s usually good at picking up outliers. OTOH it’s sort of a _this dog is resistant to learning new tricks_ issue as well ![:slightly_smiling_face:](https://emoji.discourse-cdn.com/twitter/slightly_smiling_face.png?v=13) )  
:  


[![Trial001](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/2f0fd983fcda6e6e8519069475014ec267a4648b.jpeg)Trial001560×420 10.6 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/2f0fd983fcda6e6e8519069475014ec267a4648b.jpeg> "Trial001")

This one has an output range of [0.0278 ,0.9731], and obviously it looks somewhat more skewed and significantly more leptokurtic than the Numerai predictions (just eyeballing here, I haven’t calculated the numbers yet).

The reason I’m interested is that, as I go along, it might be worthwhile to determine a separate mapping from my training outputs to the training targets. Sort of a final stage calibration, so to speak.

Sorry if I go on too much.

---

### Post #12 — **wigglemuse** | 2021-03-16 19:06 UTC

Just remember you are scored on rank, so only the ordering of your predictions matters to how you score, not what the raw values are or the shape of their distribution.

---

### Post #13 — **gammarat** | 2021-03-16 19:34 UTC _(reply to #12)_

Thanks for the reminder, [@wigglemuse](</u/wigglemuse>). But right now I’m just more interested in understanding the problem than in the actual scoring.
