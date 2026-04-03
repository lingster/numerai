---
title: "Most Common IDE's or Software"
category: Data Science
url: https://forum.numer.ai/t/most-common-ides-or-software/2455
created_at: 2021-03-19T15:19:33.260000+00:00
last_posted_at: 2021-06-14T00:47:07.346000+00:00
posts_count: 13
views: 1609
tags: []
---

# Most Common IDE's or Software

---

### Post #1 — **1lettershor** | 2021-03-19 15:19 UTC

Just wondering what is the most common software used to code with or IDE that people use to create their models. I am very familiar with R but am not sure if it is fully compatible or the best alternative. Thanks!

---

### Post #2 — **wigglemuse** | 2021-03-19 15:23 UTC

Most use Python (don’t know about favorite IDEs), R is a somewhat distant second. Personally I use R (with RStudio Server), but will get around to doing some stuff in Python one of these days…

---

### Post #3 — **1lettershor** | 2021-03-19 15:41 UTC

Is there any advantage to using Python over R?

---

### Post #4 — **wigglemuse** | 2021-03-19 15:45 UTC _(reply to #3)_

Probably yeah – more libraries, more support. Notebooks and code that people pass around and refer to is almost always python.

---

### Post #5 — **gammarat** | 2021-03-20 01:15 UTC

I’m using MatLab. It’s probably about as hip these days as my old Saturn would have been, but it works ok, has a fair number of useful tools, and good documentation.

---

### Post #6 — **minou** | 2021-03-20 14:03 UTC

Tools I’m using for ML stuff include Spyder and emacs for code editing. Python, C++, Keras and Frugally Deep for model implementations. I also get realtime data for some instruments and store that in MySQL for backtests and warming up live trading models.

---

### Post #7 — **krm** | 2021-03-20 16:23 UTC

Emacs, EIN, and some Jupyter Labs for random tests. Python for language.

Shell scripts, docker, and some elbow grease hold it all together for me.

EIN is a bit of a bitch to setup, but I’m in emacs 24/7 so it just made sense for me to set it up.

If you aren’t strong with IDEs, Jupyter Labs is more than enough. Also if you want to organize your code a bit more, try out `ipynb` which will let you import definitions from one notebook into another. Very helpful.

my basic dir structure:
    
    
    /project
      /data
        /TOURNAMENT_NAME
      /models
        /TOURNAMENT_NAME
          /ROUND
      /cache
      /predictions
        /TOURNAMENT_NAME
          /ROUND
      /notebooks
        /production
        /experiments
      start-dev-server.sh <= starts docker containers, etc.

---

### Post #8 — **halsmith99** | 2021-03-22 13:13 UTC

for python on windows…visual studio community, visual studio code or anaconda & spyder.

---

### Post #9 — **lucky_chicken** | 2021-03-31 00:15 UTC _(reply to #8)_

jupyter notebook and nbdev  
vscode

---

### Post #10 — **evanhennis** | 2021-04-15 21:57 UTC

I am using Python and a Google Colab notebook. Someone in here found an attribute tag that will double the memory you can use. It does get frustrating when trying to load a few different data sets but I got around that by converting all the columns to float16.

---

### Post #11 — **autratec** | 2021-06-13 11:30 UTC

I am using Azure ML studio. Almost like plug and play. Not coding needed. All the computing resides on Azure cloud. Regression model parameters need to be fine tuned to get better results.

---

### Post #12 — **mrquantsalot** | 2021-06-13 19:29 UTC _(reply to #10)_

I’m mapping all the floats to ints. It saves a lot of space

`mapping = {0.0 : 0, 0.25 : 1, 0.5 : 2, 0.75 : 3, 1.0 : 4}`
    
    
    `for c in feature_cols:'
    
        'df[c] = df[c].map(mapping).astype(np.uint8)`

---

### Post #13 — **autratec** | 2021-06-14 00:47 UTC _(reply to #12)_

Good suggestion. Suggest tournament provide the data in that way.
