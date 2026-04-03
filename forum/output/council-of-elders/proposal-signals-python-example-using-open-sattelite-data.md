---
title: "Proposal: Signals Python Example Using Open Sattelite Data"
category: Council of Elders
url: https://forum.numer.ai/t/proposal-signals-python-example-using-open-sattelite-data/3288
created_at: 2021-05-13T17:50:18.690000+00:00
last_posted_at: 2021-09-08T18:41:01.196000+00:00
posts_count: 13
views: 1431
tags: []
---

# Proposal: Signals Python Example Using Open Sattelite Data

---

### Post #1 — **bensch** | 2021-05-13 17:50 UTC

I have been experimenting with using various types of daily/weekly [open satellite data from NASA](<https://ladsweb.modaps.eosdis.nasa.gov/missions-and-measurements/products/MYD06_L2/>) for signals and maybe it would make a good example? I would need my [models](<https://signals.numer.ai/bensch_c>) to see more live performance before I would share this, just getting my idea out there for comment. Maybe this could be a good example notebook to show how creative one could possibly get in their search for data.

The notebook/article would cover:

  * getting the signals universe
  * mapping tickers to street addresses and sectors using yahoo finance (rain/temperature data might only apply to agriculture tickers etc)
  * finding applicable coordinates to the satellite data format (HDF usually) by using a geocoding API(with local caching to keep request volume as low as possible) or other and some simple coordinate transforms
  * requesting and reading the data from NASA with an API key using an HDF python library and an http library
  * possible sampling, models, and filters (what land area do you sample 1km^2, 3km^2…,differentiation, rolling averages, linear modeling, maybe more complex ML models)
  * automating everything just mentioned to run weekly and submit (featuring new data frame submissions with NumerAPI ![:wink:](http://forum.numer.ai/images/emoji/twitter/wink.png?v=9))
  * possibly getting validation data for the signal if download times allow (for now I have no validation data, it takes quite a while to do 5000 ticker signals for one week)



My goal would be to produce heavily commented code since there would be 3-4 APIs/modules used besides pandas and have an accompanying medium or forum post for deeper explanation. Any feedback (including telling me this just isn’t a good idea) is appreciated.

---

### Post #2 — **liz** | 2021-05-13 18:02 UTC

love this proposal, +1

---

### Post #3 — **bensch** | 2021-05-13 19:10 UTC

Adding stuff from this post <http://forum.numer.ai/t/how-to-write-a-coe-proposal/3287> to flesh this out as much as I can.  
Timeline:  
I finish my finals today and the semester this friday, I could begin work on this on ~May 16. I estimate I could get it done in two weeks to a month since I already have the code and understanding, I just need to clean it up (alot LOL), streamline the different scripts I use, write comments and the article, and get some rounds submitted

Success:  
The clearest long term success evaluation of this project would probably be something like seeing a spike of example model submissions on main tournament in the percentile graph, or having successful signals users open up about using this type of data as inspired by my example. Inspiring people to build even better models and find better data that is the main goal. Discussion/reference about this example on rocket chat or the forums would also indicate that this example was helping the community and new users learn about signals, specifically creativity of sourcing data and dealing with ugly or uncommon APIs to get that data.

Worst case:  
Satellite data publicly available has no corr(3 rounds in this seems to be untrue, but things could easily change), the specifics of this tutorial become useless but readers still learn about API’s in python and chaining them together to get a signal, creativity, and how cool signals can be(auditing companies with an eye in the sky). The tutorial will also give the reader so basic understanding of modeling of series and application of filters and models. I am not worried too much about the readability or quality of explanation since I have done and enjoyed a bit of technical writing and will be seeking community feedback throughout the process which should help to spot any failure in my explanations.

Best case:  
Corr is good and users look for other similar data or are inspired to try hard/weird/uncommon data sources that often have the least exploited market information, users stake on models inspired by this or directly copied and the meta model gets better for signals. Readers of the article and code are more prepared to deal with API’s, data series, and signals more generally since article is well written and gives users basic tools not just NASA sattelite specific skills.

Funding:  
Some parts of this process take a while to run given the speed of yfinance and other API requests(hours), I will try to fix this but If I cannot maybe sub 1 NMR could be useful for me to rent a server for a long time and automate the retreival of addresses or geocodings of tickers each week for signals users to download via a link(A csv of tickers, addresses, and common coordinates)

This would also take significant time to write, though im not sure if the CoE is interested in compensating for time spent on proposals. If they are maybe a reward for keeping things up to date over a longer period and answer questions, not just after the first release? Tentatively 1-2 NMR might be fair if the example stays up to date, relevant, and starts useful discussions on RC or the forums?

---

### Post #4 — **bensch** | 2021-05-13 20:19 UTC

<https://ladsweb.modaps.eosdis.nasa.gov/> is a good overview of what data NASA has along with the pages for each mission on that page, I am not sure If I want to make my model’s specific data type the focus of the example since I am concerned about losing mmc, but there are multiple promising data like temperature, cloud cover, cloud physical state, visible light, or moisture that with some domain specific massaging/partitioning could be promising (for example dont use moisture data to give a signal for a tech stock like apple, and average over X days since most crops are planted in harvested in 2X days) . Also I have realized to make getting validation possible would just require a data source for historical company location/address so if anyone has one to recommend that is free that would be great.

---

### Post #5 — **nyuton** | 2021-05-14 11:54 UTC _(reply to #3)_

Why don’t you just do it for yourself and stake it?  
If it works, you get a lot more then just 1-2 NMR.  
It it doesn’t work, then it’s useless anyway…

---

### Post #6 — **bensch** | 2021-05-14 14:49 UTC _(reply to #5)_

Yeah I probably didn’t make it clear enough that I’m just getting the idea down since my model has only three rounds, and the time horizon needs to change, more like a few months until I could be confident in my model to stake a significant amount of my own NMR and share the code framework.

---

### Post #7 — **mic** | 2021-05-14 23:18 UTC

I think you have lots of good ideas here, but can’t see why it needs funding.

Perhaps example scripts should be super simple, use freely available data and not be intended to produce high performance.

---

### Post #8 — **bensch** | 2021-05-14 23:34 UTC _(reply to #7)_

yeah it is probably too complex for an example, probably better off as just a forum post, and you’re right most likely nothing needs to be bought or rented for this.

---

### Post #9 — **liz** | 2021-05-15 01:08 UTC

I’d love it if the CoE funded you to post an example script utilizing open satellite data, would be so much easier to adapt my own satellite ideas from, and I imagine many others would love this as a jumping-off point.

---

### Post #10 — **bensch** | 2021-05-15 01:36 UTC _(reply to #9)_

yeah ill post it for sure within the next month or two (here are some links if you dont want to wait to start on your own ideas, address to coordinates:[Overview | Geocoding API | Google Developers](<https://developers.google.com/maps/documentation/geocoding/overview>), ticker to address: [All you need to know about yfinance : Yahoo! Finance Library | by Abhijith Chandradas | Nerd For Tech | Medium](<https://medium.com/nerd-for-tech/all-you-need-to-know-about-yfinance-yahoo-finance-library-fa4c6e48f08e>), reading h5 files from NASA: [HDF5 for Python — h5py 3.2.1 documentation](<https://docs.h5py.org/en/stable/>) , each NASA h5 file source should also have a good pdf with it on how that specific data is to be interpreted and the technical spec on the measurements)but they are right any funding if any this needs is so small gas fees will be half of it and the time taken to vote on it would be too much

---

### Post #11 — **aventurine** | 2021-08-05 23:43 UTC _(reply to #10)_

Any updates from CoE or [@bensch](</u/bensch>) on this? Is this a still open proposal?

---

### Post #12 — **uuazed** | 2021-09-08 18:18 UTC _(reply to #11)_

I believe this is too complex and special for a example script. If it works, it could make a good forum post or medium article. And obviously, if it works the author should submit the predictions and stake some NMR on it. Sounds like that was also the tenor from the community

[@bensch](</u/bensch>) Any success using the satellite data?

---

### Post #13 — **steaktest** | 2021-09-08 18:41 UTC _(reply to #12)_

Sorry for going MIA here(This is bensch, just on a separate account since this PC only has this test account saved), my linear model based off of ~km^2 light intensity data I was using and company HQ locations did not have any correlation. For now I am too busy to add anything more to this or try new models and data but I did link most of the docs I used. My code isn’t really worth sharing given how messy it is.
