---
title: "Full signals pipeline"
category: Signals
url: https://forum.numer.ai/t/full-signals-pipeline/5632
created_at: 2022-08-08T15:56:19.178000+00:00
last_posted_at: 2022-10-18T17:25:44.642000+00:00
posts_count: 7
views: 2247
tags: []
---

# Full signals pipeline

---

### Post #1 — **olivepossum** | 2022-08-08 15:56 UTC

Hi,

I’ve recently been working on a Signals Pipeline. No secret sauce. As most of the ideas or even the code I used are from previous forum posts or messages from Rocketchat, I’ve [open sourced it](<https://github.com/sturlese/numerai_signals_pipeline>).

Used to work on a low memory machine so there is a lot of parquet column read/write to disk (that’s not the case anymore and might also be noticed on most recent parts of the code).

Hope someone finds it useful.  
Any feedback is more than welcome!

The current validation metrics look like this:

[![validation_metrics](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/1/167c1d9666cb40751291bf572d2834110cfc891b_2_690x418.png)validation_metrics1486×902 71.1 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/1/167c1d9666cb40751291bf572d2834110cfc891b.png> "validation_metrics")

[![validation_tb200_metrics](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/2/2cd318a9b02ab450d2dc7e33e827d630b097febb_2_690x417.png)validation_tb200_metrics1486×900 74.7 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/2/2cd318a9b02ab450d2dc7e33e827d630b097febb.png> "validation_tb200_metrics")

Thanks to the whole community, especially to [@jrdi](</u/jrdi>) [@habakan](</u/habakan>) [@joakim_arvidsson](</u/joakim_arvidsson>) [@kunigaku](</u/kunigaku>) [@ageonsen](</u/ageonsen>) [@katsu1110](</u/katsu1110>)

Thanks!

---

### Post #2 — **liz** | 2022-10-07 16:08 UTC

Thanks [@olivepossum](</u/olivepossum>) ! I’m jumping back into Signals now and using this pipeline as my home base. I’m used to programming in R so I’m still getting my bearings with Python, my apologies for this surely noob-ish question. I did a private clone of the repo, specified my properties JSON file, and ran it, with a big block of errors I am unsure if I am reading correctly. I won’t have time to run the downloading again until next week, but wanted to see if my guesses are anywhere near correct. [Googling about the errors](<https://stackoverflow.com/questions/38661464/filenotfounderror-winerror-3>) that came up, I think I may want to use a prepended ‘r’ instead of ‘f’ in folders.py (see line 30 folders.py for example).

The downloader appears to be working as intended but did not succeed in writing the data files.

[Here’s a pastebin of my console output.](<https://pastebin.com/E5YWwjTg>)

Also I’d be glad to contribute to the project after I get my bearings if I come up with anything useful!

Thanks.

---

### Post #3 — **olivepossum** | 2022-10-07 18:54 UTC _(reply to #2)_

Hi [@liz](</u/liz>) good to have you back!

The output looks strange. Haven’t seen it before.  
Did you run several executions at the same time? You shouldn’t for it to work.  
It might also be related to OS and/or path issues. I’m running the code on a Linux box Ubuntu 20.04.4 LTS

---

### Post #4 — **liz** | 2022-10-08 20:35 UTC _(reply to #3)_

Thanks! Yeah I think I ran it once only, but gonna try again. I’m using PowerShell on Windows 10 Pro.

---

### Post #5 — **liz** | 2022-10-09 15:01 UTC

ran again and this time there are 25 parquet files in the raw downloaded folder. looking at the console output it definitely tried to download again a number of times and had other weird errors. I think I’ll probably run this in a linux environment in the near future to avoid having to figure out Windows/PowerShell specific hang-ups.

---

### Post #6 — **wigglemuse** | 2022-10-09 15:37 UTC _(reply to #5)_

Linux box (or virtualbox w/ linux) gotta be better than powershell, right?

---

### Post #7 — **jrai** | 2022-10-18 17:25 UTC _(reply to #5)_

This looks like it’s definitely a Windows issue. I’d strongly recommend setting up WSL on your machine [WSL | Ubuntu](<https://ubuntu.com/wsl>) and I also use Windows Terminal to manage the multiple command line interfaces.

(also welcome back!)
