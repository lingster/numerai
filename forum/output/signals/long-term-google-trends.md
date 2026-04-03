---
title: "Long-term google trends"
category: Signals
url: https://forum.numer.ai/t/long-term-google-trends/5293
created_at: 2022-04-20T20:45:20.785000+00:00
last_posted_at: 2022-06-30T20:44:04.088000+00:00
posts_count: 6
views: 1741
tags: []
---

# Long-term google trends

---

### Post #1 — **quantized** | 2022-04-20 20:45 UTC

I took part in Signals for a while, and in the process, designed a system for downloading long-term google trends, by pulling overlapping trend periods and rescaling i+1th to the ith.

I’ve turned it into a python package available for general use: [Github](<https://github.com/mikedbjones/longtrends>) / [PyPI](<https://pypi.org/project/longtrends/>).
    
    
    pip install longtrends
    
    from longtrends import LongTrend
    from datetime import datetime
    
    keyword = 'suncream'
    
    # Create LongTrend object
    longtrend = LongTrend(
                          keyword=keyword,
                          start_date=datetime(2018, 1, 1),
                          end_date=datetime(2022, 3, 31))        # use verbose=True for print output
    # Build long-term trends
    lt_built = longtrend.build()
    
    # Plot (matplotlib required)
    lt_built.plot(title=f"Google Trends: {longtrend.keyword}", figsize=(15, 3))
    

More info and images illustrating how the rescaling works [here](<https://github.com/mikedbjones/longtrends>).

---

### Post #2 — **wigglemuse** | 2022-04-20 21:50 UTC

It has been a while, but a number of years ago I was doing some stuff with google trends and found that it was really hard to stitch together different time periods or to compare two trends from different queries because the scale from each query was totally arbitrary (was just scaled according to the results gotten, I think). Also seemed to be a fair amount of randomness, i.e. the sampling wasn’t consistent even when doing the same query over again (on the past) – I’d get (at least somewhat) different results. It was good for comparing two or more trends in a relative way (or the relative ups & downs of a single trend) in the same query, but very challenging to track results over time, and no way to pin anything down to an absolute objective level.

---

### Post #3 — **quantized** | 2022-04-21 05:00 UTC _(reply to #2)_

[@wigglemuse](</u/wigglemuse>) , you’re right that the scale is different for each period; the top result is always 100 and the bottom result can be as low as 0. You’re also right that overlapping periods aren’t 100% consistent, because Google looks at a sample of searches for each request (it doesn’t look at every single search for obvious reasons). This means there is some variation.

However, usually, the shapes of each period are similar, which allows them to be rescaled, keeping most of the ‘signal’ intact. This is what my longtrends package does under the hood:

Non scaled:  


[![olympics_overlapping](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/4/46bdfd58c964e5de830619426026e404fbd9adf0_2_690x184.png)olympics_overlapping1500×400 69.7 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/4/46bdfd58c964e5de830619426026e404fbd9adf0.png> "olympics_overlapping")

Scaled to each other:  


[![olympics_rescaled](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/2/26af10d97d7e724966b8df500fa14886b2e28da9_2_690x184.png)olympics_rescaled1500×400 46.8 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/2/26af10d97d7e724966b8df500fa14886b2e28da9.png> "olympics_rescaled")

You can see the shape of the overall trend is quite consistent, even in this example where there was a big spike in interest for the search term.

---

### Post #4 — **quantized** | 2022-04-30 19:24 UTC _(reply to #3)_

I’ve written a more in-depth article about how it works here:

![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/8/8988adbdc6573e068049c6752be8f352b3cb6716.png) [Medium – 16 Nov 22](<https://medium.datadriveninvestor.com/long-term-google-trends-in-python-with-longtrends-e478bb3d54f5?gi=e21254a944dd> "05:48AM - 16 November 2022")

![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/e/ea40a8ac41da9598df8ac74ca1bdf587ceeef05c_2_690x365.png)

### [Long-term Google Trends in Python with Longtrends](<https://medium.datadriveninvestor.com/long-term-google-trends-in-python-with-longtrends-e478bb3d54f5?gi=e21254a944dd>)

The Longtrends package allows downloads of reliable, daily, long-term Google Trend data.

Reading time: 5 min read

---

### Post #5 — **arbitrage** | 2022-05-02 15:13 UTC

I have a published paper that uses google search trends as a proxy for retail investor demand:

<https://www.emerald.com/insight/content/doi/10.1108/IJMF-10-2021-0542/full/html>

---

### Post #6 — **ricklamers** | 2022-06-30 20:44 UTC

Just came here to say thank you for an awesome package! ![:pray:](http://forum.numer.ai/images/emoji/twitter/pray.png?v=10)
