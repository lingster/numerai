---
title: "Automating R submissions?"
category: Data Science
url: https://forum.numer.ai/t/automating-r-submissions/934
created_at: 2020-09-11T01:15:39.049000+00:00
last_posted_at: 2020-09-15T17:39:19.366000+00:00
posts_count: 6
views: 1092
tags: []
---

# Automating R submissions?

---

### Post #1 — **liz** | 2020-09-11 01:15 UTC

Has anyone that uses R for submissions outlined or written about their setup? I’m an R specialist and prefer working in R rather than Python. Also, if there are any other R nerds out there, ![:wave:](http://forum.numer.ai/images/emoji/twitter/wave.png?v=9)

---

### Post #2 — **ssh** | 2020-09-11 09:29 UTC

I fall into the category of R nerds. I use mostly R/Rstudio + Rnumerai library. My approach is a set of “croned” R scripts that in a few steps generate predictions: these basic steps: get data, make some extra features & auxiliary targets (with neutralization), estimate a set of models (with main and auxiliary targets), combine models with different optimization metrics in mind (like Sharpe, Sortino, etc.) and submit predictions.

---

### Post #3 — **liz** | 2020-09-11 16:09 UTC _(reply to #2)_

awesome! what does “croned” mean in this case?

edit : “scheduled under cron” would make sense now that i think of it

---

### Post #4 — **ssh** | 2020-09-11 16:15 UTC _(reply to #3)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/liz/48/1103_2.png) liz:

> croned

task that is running the script on schedule:  
in my win10 case it’s some *.bat file that contain only a few strings
    
    
    @echo on
    "c:\Program Files\R\R-3.6.1\bin\R.exe" CMD BATCH d:\2020\numerai2020\R\run.start.A.ssh.v04.r

---

### Post #5 — **kreator** | 2020-09-15 05:59 UTC _(reply to #3)_

You could also look into the compute service provided by numerai. Using a python package it sets up an AWS service that runs a docker image (costs can be as low as 1 USD per month depending on the set-up and runtime - mine is 2 USD). In the image you can use R code. I have used this set-up for a year now. It works very well. For submitting you can use the Rnumerai package. If you need more info then I come back in the next couple of days and edit this post with more details.

---

### Post #6 — **liz** | 2020-09-15 17:39 UTC _(reply to #5)_

thanks! I should be able to figure it out, though feel free if you want to!
