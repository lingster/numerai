---
title: "How can we overcome Key Errors with Numerox"
category: Data Science
url: https://forum.numer.ai/t/how-can-we-overcome-key-errors-with-numerox/2792
created_at: 2021-04-10T16:05:02.521000+00:00
last_posted_at: 2021-05-07T18:39:02.165000+00:00
posts_count: 4
views: 785
tags: []
---

# How can we overcome Key Errors with Numerox

---

### Post #1 — **mindyoself** | 2021-04-10 16:05 UTC

Hello,

I was trying to run one of arbitrages notebooks to try out numerox as I am not used to it. I noticed you ([@arbitrage](</u/arbitrage>) ) were splitting eras which I wanted to experiment with. Still very new to this as you can tell but getting the hang of it.

So at this point in the code

y_train = data[‘era1’:‘era30’].df[‘target’].values

it outputs a KeyError: ‘target’

Did you encounter this problem with numerox as well or is it just me, likely it is me.

Thank you for all the newby teaching. You’ve been awesome.

JD

---

### Post #2 — **ml_is_lyf** | 2021-04-10 16:22 UTC

If I remember rightly, numerox was mentioned on one of the office hours. It was written by a user who stopped participating, so it’s no longer maintained, so it’s not recommended to use it anymore. So it’s probably not you, it’s probably just its broken ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=9)

Look at how the example scripts on numer.ai/submit loads the data, and try and replace it with that approach instead.

Some quick code to get you started, this should do the same thing as the example code you gave:
    
    
    training_data = pd.read_csv("https://numerai-public-datasets.s3-us-west-2.amazonaws.com/latest_numerai_training_data.csv.xz")
    first_30_training_eras = set(training_data.era.unique()[:30])
    training_data_first_30_eras = training_data.loc[[era in first_30_training_eras for era in training_data.era]]
    y_train = training_data_first_30_eras.target
    

And yes arbitrage is definitely the MVP ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=9)

---

### Post #3 — **mindyoself** | 2021-04-10 16:30 UTC _(reply to #2)_

Hello [@ml_is_lyf](</u/ml_is_lyf>)

Thank you so much for the quick response on this.

He is indeed. Petition to make him Professor Arbitrage (Minister of Education) if he isn’t already.

But that said, yes I have been using training_data = pd.read_csv excetra… so I am familiar with that. I wanted to broaden my horizons a little bit more and try other frameworks within the ecosystem. But I will definitely try what you have suggested. I didn’t know that numerox was no longer being maintained. Wish we could help cos it offers another dimension to data manipulation.

Thank you so much for your incredible insights. Awesome stuff. Good luck on your journey also.

Best Regards,  
JD

---

### Post #4 — **elimark1** | 2021-05-07 18:39 UTC

The API responds with 4xx HTTP status codes on a regular basis, since we require some authentication and sometimes users do not have it. However, these 4xx responses are causing “Error rate > 5.0%” events to be triggered on one of our key transactions.

How can I tell the key transaction that it’s okay to have a 4xx on this endpoint?

For the New Relic team, here is an example of an event I want to ignore. This “event” is being caused due to perfectly legitimate 4xx status code responses from our API, rather than any real problem.

* * *

[The brooks brothers trailers](<https://www.brooksbrotherstrailers.com/>)
