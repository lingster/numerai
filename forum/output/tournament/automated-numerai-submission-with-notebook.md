---
title: "Automated numerai submission with Notebook"
category: Tournament
url: https://forum.numer.ai/t/automated-numerai-submission-with-notebook/5716
created_at: 2022-09-25T22:19:00.014000+00:00
last_posted_at: 2023-03-25T19:33:16.081000+00:00
posts_count: 18
views: 2313
tags: []
---

# Automated numerai submission with Notebook

---

### Post #1 — **zwk** | 2022-09-25 22:19 UTC

hello all, I’d like to share a new discovered platform [https://deepnote.com](<https://deepnote>) for those who are using jupyter notebook for weekly submission.  
The biggest advantage is that one can migrate easily the notebook to the cloud, together with all neccessary model files, scripts, environment variables, etc. All config takes about <5 min.  
Once setup, one can schedual the notebook execution with the schedualer.  
In terms of pricing, under basic hardware environment (2.5G ram/5G space), it’s all free (it’s adequate for my prediction process). Of course, one can choose to upgrade to performing environment for demanded calculation (like model training) with full transparent hourly fees.  
Hopefully this can help people to alleviate the submission with physical machine.

---

### Post #2 — **autratec** | 2022-10-22 23:55 UTC

Thanks for sharing. How is your experience after using it for a while ?

---

### Post #3 — **zwk** | 2022-10-23 19:23 UTC _(reply to #2)_

It works smoothly since day one. It’s simple and easy to configurate if you are working with notebook.  
Once the job is scheduled, the life cannot be easier.

---

### Post #4 — **autratec** | 2022-10-27 07:41 UTC _(reply to #3)_

[@zwk](</u/zwk>) hi, your post coming at right timing. i start to use deepnote to submit my prediction daily for both main and signal. thanks

---

### Post #5 — **zwk** | 2022-10-27 13:55 UTC _(reply to #4)_

Indeed! Glad it works well for you! The only missing point for schedular is to have webhook trigger, for which I have submitted a request to their Dev, hopefully can have it soon!

---

### Post #6 — **sunkay** | 2022-10-30 13:28 UTC

Thanks for sharing. It’s very easy to set up deepnote

---

### Post #7 — **mattiasl** | 2022-11-14 09:41 UTC

I’m using google colab pro+ which also has a scheduler. It works very well. The only downside is that you need to download all the data and re-train the model every time (you can’t save/download a pickled model, and you need to redownload universe and targets from Numerai server every time you run it).

Files can be downloaded from and saved to your google drive but unfortunately google doesn’t allow you to do that without authenticating and giving permission in person when you start the notebook. Therefore the google drive seems to be inaccessible while using the scheduler.

Also, the google scheduler is limited to 13 days ahead (which is good enough for my purposes).

---

### Post #8 — **shatteredx** | 2022-11-14 14:39 UTC _(reply to #7)_

You may actually be able to auto-mount google drive per Colab notebook. It seems to work for me.

First, you need to create a blank notebook first (don’t copy or save as) that isn’t shared.

Then, mount Google drive using the file browser. After that, it should auto-mount. Not sure how reliable this method is but it seems to work right now.

[stackoverflow.com](<https://stackoverflow.com/questions/52808143/colab-automatic-authentication-of-connection-to-google-drive-persistent-per-n>) [ ![Marius Brataas](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/2/2f571b8a3f779f6328ded47cbc9d8108b93bb41a.jpeg) ](<https://stackoverflow.com/users/7025394/marius-brataas>)

####  [Colab - automatic authentication of connection to google drive, persistent per-notebook](<https://stackoverflow.com/questions/52808143/colab-automatic-authentication-of-connection-to-google-drive-persistent-per-n>)

**python, authentication, google-colaboratory**

asked by [ Marius Brataas ](<https://stackoverflow.com/users/7025394/marius-brataas>) on [12:01AM - 15 Oct 18 UTC](<https://stackoverflow.com/questions/52808143/colab-automatic-authentication-of-connection-to-google-drive-persistent-per-n>)

Not sure if this works with the scheduler though.

---

### Post #9 — **mattiasl** | 2022-11-15 02:29 UTC _(reply to #8)_

Thank you so much! I’ve just given it a try and it works

I’ve been mounting programmatically in the start of my programs which necessitated an online approval:

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/3/3c0755ac599cc8c89e4ab0d95da199c00fc3565b.png)image818×126 5.27 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/3/3c0755ac599cc8c89e4ab0d95da199c00fc3565b.png> "image")

---

### Post #10 — **autratec** | 2022-12-04 03:49 UTC

Daily submission need to upgrade to event driven, rather than schedule. Any new cloud notebook support that new demand?

---

### Post #11 — **zwk** | 2022-12-04 17:44 UTC _(reply to #10)_

Indeed, we’ll need to hire an intern to click the button ![:smile:](http://forum.numer.ai/images/emoji/twitter/smile.png?v=12)

---

### Post #12 — **autratec** | 2022-12-06 03:18 UTC _(reply to #11)_

actually, the intern is myself. i start checking my email regularly and click the button if i saw the message ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=12)

---

### Post #13 — **autratec** | 2022-12-08 02:13 UTC

For those who like to use telegram to get a notification from Numerai, pls feel free to join following telegram group.

---

### Post #14 — **autratec** | 2022-12-08 04:58 UTC _(reply to #13)_

hi. i just close my telegram group and change to channel. please use the following linkage:

![](https://telegram.org/img/website_icon.svg?4) [Telegram](<https://t.me/numeraidaily>) ![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/f/f1be713231a12acdfae4d71909ac80c166f67896.jpeg)

### [Numerai Daily](<https://t.me/numeraidaily>)

Provide open notification of NUMERAI daily prediction submission window.

---

### Post #15 — **svendaj** | 2022-12-08 16:21 UTC

I am using Kaggle both for learning and submissions and because they now provide for free notebooks with 4 CPU cores and 30GB RAM and I am lazy person to go elsewhere, [I have created workaround using Oracle Cloud compute node (always free! ![:wink:](http://forum.numer.ai/images/emoji/twitter/wink.png?v=12)), installed Kaggle public API, running `cron` triggering execution of Kaggle notebooks](<https://www.kaggle.com/discussions/product-feedback/371090>) at expected round openning. Inside of the [notebooks I wait for openning of given round](<http://forum.numer.ai/t/server-errors-on-friday/5883/5>).

---

### Post #20 — **lcrmorin** | 2023-03-23 12:53 UTC _(reply to #15)_

At this point why not use the kaggle scheduler ?

---

### Post #21 — **svendaj** | 2023-03-24 00:35 UTC _(reply to #20)_

Kaggle scheduler is very rudimentary and allows only daily, weekly or monthly frequency without possibility to set time for execution. So for numerai purposes useless.

---

### Post #22 — **svendaj** | 2023-03-25 19:33 UTC _(reply to #10)_

I have just finished [python Flask server processing numerai compute webhook and launching Kaggle notebooks.](<https://www.kaggle.com/discussions/questions-and-answers/397468>) Server runs in Oracle Cloud (always free ![:wink:](http://forum.numer.ai/images/emoji/twitter/wink.png?v=12) and up and running 24x7), but it can be built even locally and ngrok would provide you with public entrypoint.
