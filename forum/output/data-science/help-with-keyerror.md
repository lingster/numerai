---
title: "Help with KeyError"
category: Data Science
url: https://forum.numer.ai/t/help-with-keyerror/5268
created_at: 2022-04-15T13:49:10.399000+00:00
last_posted_at: 2022-04-15T23:42:41.811000+00:00
posts_count: 2
views: 726
tags: []
---

# Help with KeyError

---

### Post #1 — **supernoesis** | 2022-04-15 13:49 UTC

Hi,

I’ve been away from the tournament for a few years now, trying to get back into it. I tried out the example_model_advanced.py and with downsample_cross_val=1 I get preds_model_target_neutral_riskiest_50 KeyError. Any suggestions? I also see mentions of example_model_advanced_32gb.py on this forum but can’t find it anywhere. Do you know where I can find it?

TIA.

---

### Post #2 — **zubinator** | 2022-04-15 23:42 UTC

[github.com](<https://github.com/numerai/example-scripts>)

![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/b/b792e70d9bc3849e3555852013db6d395365028f_2_690x344.png)

### [GitHub - numerai/example-scripts: A collection of scripts and notebooks to help you...](<https://github.com/numerai/example-scripts>)

A collection of scripts and notebooks to help you get started quickly.

not sure if this is what you were looking for  
Also maybe try downsample= 2? I’m not an expert on this stuff but perhaps downsample 1 is too little data?  
Good luck
