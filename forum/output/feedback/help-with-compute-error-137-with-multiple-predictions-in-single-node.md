---
title: "Help with compute (error 137 with multiple predictions in single node)"
category: Feedback
url: https://forum.numer.ai/t/help-with-compute-error-137-with-multiple-predictions-in-single-node/2929
created_at: 2021-04-18T00:03:49.273000+00:00
last_posted_at: 2021-04-18T22:10:34.120000+00:00
posts_count: 3
views: 1039
tags: []
---

# Help with compute (error 137 with multiple predictions in single node)

---

### Post #1 — **lysk** | 2021-04-18 00:03 UTC

Hello

Not sure if it’s a bug or a feature ![:wink:](http://forum.numer.ai/images/emoji/twitter/wink.png?v=9) With `numerai cli 0.3.0` I setup a node, after testing locally if the docker container was running as expected I deployed it. Here is the logic:

  * Download data, read `tournament` data
  * Load model 1 (the one with the webhook setup), predict and submit
  * Load model 2, predict and submit



I’m getting an `OOM Error 137`, somewhere between model 2 load and predict functions (not always at the same place).

What I’ve tried:

  * use 30GB of RAM for the node, didn’t help, and delete files from disk when they aren’t necessary anymore to no avail
  * running on a 30GB machine and checking RAM usage, the max usage was ~45% (during this test I didn’t call `napi.upload_predictions(...)` maybe that matters?)
  * then I realized that a kill signal could come after the model-1-with-webhook successfully upload its prediction, so I changed the order: model 2 first then model 1, same issue after model 2 successfully upload its predictions



My question is: is it possible to submit multiple predictions (for as many models) with a single node?

Otherwise the compute 0.3.0 is really cool and easy to use, thanks ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=9)

---

### Post #2 — **profricecake** | 2021-04-18 18:08 UTC

Hi [@lysk](</u/lysk>) \- I’ve been struggling with this same issue too for the last 24 hours but I may have found a solution.

When I first ran `numerai node config` and looked at the `~/.numerai/nodes.json` file it created, I saw that the CPU and RAM were not what I wanted. So I changed those lines to read:
    
    
    "cpu": 4096,
    "memory": 30720
    

I tried deploying and testing, and it crashed with:
    
    
    Task is stopping...
    Container Exit code: 137
    Reason: OutOfMemoryError: Container killed due to memory usage
    

So I looked at the actual Task definitions via the Amazon website (log in to their web console and go to Amazon → ECS → Task Definitions). There I saw that the RAM and CPU settings were still at their previous values, which were too low for me.

A little digging showed me that the `terraform.tfstate` file in my `.numerai` folder ALSO has those CPU and RAM values set. In other words, my manual change of `nodes.js` does not trigger a change throughout the whole system like I thought it might.

The way I fixed this was to run:
    
    
    numerai node config -s mem-lg
    

Which put the right values in both the `nodes.js` file and the `terraform.tfstate` files (and perhaps elsewhere too). When I did this and deployed, the task on Amazon finally had the proper CPU and RAM limits. And just ran to completion successfully.

I hope this helps!

---

### Post #3 — **lysk** | 2021-04-18 22:10 UTC _(reply to #2)_

Hello [@profricecake](</u/profricecake>)

That worked out (`numerai node config -s mem-lg`), like you I initially assumed that manually updating `nodes.json` was enough. Thanks!

~~My`Task Definitions` tab is empty (both tabs: `active` and `inactive`) even when it’s running. I’ll try to figure out how to see the task to check the resources.~~ So my `Task Definitions` tab was empty… because I wasn’t looking at the right region. Solution: from the billing dashboard → Billing details → ECS, there the region used by ECS is indicated. Now back to ECS → Task Definitions, in the top right corner there is a menu to change region.

For anyone wondering about costs, spending the weekend trying to make it work with many runs failing halfway through was about 0.12$.
