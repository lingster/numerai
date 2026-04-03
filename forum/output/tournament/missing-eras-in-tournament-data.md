---
title: "Missing eras in tournament data"
category: Tournament
url: https://forum.numer.ai/t/missing-eras-in-tournament-data/483
created_at: 2020-05-29T12:09:07.237000+00:00
last_posted_at: 2020-11-16T00:34:18.711000+00:00
posts_count: 6
views: 1705
tags: []
---

# Missing eras in tournament data

---

### Post #1 — **correlator** | 2020-05-29 12:09 UTC

With the announcement of Validation data - 2 it was mentioned that test eras 854-899 were being replaced by val eras 197-206. However in the downloaded tournament data file test eras 853 and 900 are not present. Am I missing something here?  
[@master_key](</u/master_key>)

---

### Post #2 — **master_key** | 2020-05-29 18:03 UTC

This is just a difference between the time it was announced vs the implementation by the time I finished testing and launched, you’re not missing anything

---

### Post #3 — **ladylikelaces** | 2020-11-15 23:25 UTC _(reply to #2)_

AttributeError Traceback (most recent call last)  
in ()  
1 # create a model and fit the training data (~30 sec to run)  
2 model = sklearn.linear_model.LinearRegression()  
\----> 3 model.fit(training_features, training_data.target_kazutsugi)

/usr/local/lib/python3.6/dist-packages/pandas/core/generic.py in **getattr**(self, name)  
5137 if self._info_axis._can_hold_identifiers_and_holds_name(name):  
5138 return self[name]  
-> 5139 return object.**getattribute**(self, name)  
5140  
5141 def **setattr**(self, name: str, value) -> None:

AttributeError: ‘DataFrame’ object has no attribute ‘target_kazutsugi’

---

### Post #4 — **wigglemuse** | 2020-11-15 23:43 UTC _(reply to #3)_

I think you’re behind on your announcements. The dataset this week has lost some test eras and added some validation eras. And we are using the new nomi target for scoring as of this round.

---

### Post #5 — **ladylikelaces** | 2020-11-15 23:48 UTC _(reply to #4)_

need more detail, please  
i’m used <https://colab.research.google.com/github/numerai/example-scripts/blob/master/making-your-first-submission-on-numerai.ipynb#scrollTo=WeAIJHaoW3VU>

---

### Post #6 — **wigglemuse** | 2020-11-16 00:34 UTC _(reply to #5)_

There is a new target:

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/forum.numer.ai/mdo/48/3398_2.png)

[New Target Nomi Release](<http://forum.numer.ai/t/new-target-nomi-release/959>) [Tournament](</c/tournament/7>)

> We are releasing today a new target, target_nomi, that you can optionally use to train your models. You should still submit predictions in the same exact way as before but just using the outputs of the newly trained model. Fundamentally, this target represents the same thing as target_kazutsugi, but just a bit more faithfully. Consequently, it is compatible with target_kazutsugi and we will continue scoring using target_kazutsugi for the time being. We will give plenty of warning before we event… 

So no more kazutsgui.

6 new validation eras have been added this week. At the same time, test eras 901-926 have been removed (they cover the same period).

Are you on rocketchat? See:  
<https://community.numer.ai/channel/announcements>

If you are just finding out about this now, I’m not sure what has to be adjusted in your pipeline, etc, but there are changes!
