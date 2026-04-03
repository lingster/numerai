---
title: "Training the example data doesn't work"
category: Tournament
url: https://forum.numer.ai/t/training-the-example-data-doesnt-work/2402
created_at: 2021-03-16T18:18:10.598000+00:00
last_posted_at: 2021-04-01T07:01:23.834000+00:00
posts_count: 4
views: 929
tags: []
---

# Training the example data doesn't work

---

### Post #1 — **trouver** | 2021-03-16 18:18 UTC

Hello everybody,

I’m new to this community. My problem is that : I downloaded the example package and i tried to run it.  
But on Spyder i have constantly an error saying : “kernel restarting” when loading the data.

Trying in it on an other pc i have with 32Go of RAM, the data load, but the script silently stop as soon as the training begin (when model.fit is called). No exception, no error, nothing. Any idea of what is happening ? is it a resources limitation ?

I tried reducing the hyperparameters of xgb as suggested in the script, uncommeted the provided code to reduce the size of the data, but it still doesn’ t work at all.

---

### Post #2 — **orbitalteapot** | 2021-03-16 20:37 UTC

Could be. Try running Task Manager on the side (or equivalent for your system) to see if memory is the issue.

Not sure about how Spyder manages memory allocation but for Jupyter you can tune it in the configuration file. I think default is 0.5GB.

---

### Post #3 — **greenprophet** | 2021-03-16 20:53 UTC

I think the example runs pretty fast with defaults and 32 gb should be plenty. I run out of memory a lot when doing to many things. You should be able to monitor it running out depending on your OS. Seems it would only a be memory issue.

Have you verified that xgb works. Like can you run a simple random xgb sample online.

---

### Post #4 — **trouver** | 2021-04-01 07:01 UTC _(reply to #3)_

Hi,

I was indeed xgb. I updated the package and now it run like a charm ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=9)
