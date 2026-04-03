---
title: "[Newbie Question!] Error When Running Example Notebook to Load Data"
category: Data Science
url: https://forum.numer.ai/t/newbie-question-error-when-running-example-notebook-to-load-data/4675
created_at: 2021-12-24T07:17:01.324000+00:00
last_posted_at: 2021-12-25T02:56:08.294000+00:00
posts_count: 3
views: 1292
tags: []
---

# [Newbie Question!] Error When Running Example Notebook to Load Data

---

### Post #1 — **odeforodds** | 2021-12-24 07:17 UTC

Hi guys, this is my first time trying to get involved in the numerai tournament.

I have tried and downloaded the example script from the numerai main website.

I was able to download the dataset which is as big as 1 Gigabytes but failed to load it into dataframe.

## I installed the required libraries and ran the code below:

napi = NumerAPI()  
current_round = napi.get_current_round(tournament=8) # tournament 8 is the primary Numerai Tournament

# read in all of the new datas

# tournament data and example predictions change every week so we specify the round in their names

# training and validation data only change periodically, so no need to download them over again every single week

napi.download_dataset(“numerai_training_data.parquet”, “numerai_training_data.parquet”)

## df = pd.read_parquet(‘numerai_training_data.parquet’)  
df.head()

and get the error below:  
2021-12-24 07:06:39,275 INFO numerapi.utils: target file already exists  
2021-12-24 07:06:39,289 ERROR numerapi.utils: deleting file and restarting  
numerai_training_data.parquet: 1.01GB [00:32, 30.9MB/s]

OSError Traceback (most recent call last)  
in ()  
7 # training and validation data only change periodically, so no need to download them over again every single week  
8 napi.download_dataset(“numerai_training_data.parquet”, “numerai_training_data.parquet”)  
\----> 9 df = pd.read_parquet(‘numerai_training_data.parquet’)  
10 df.head()

7 frames  
/usr/local/lib/python3.7/dist-packages/pyarrow/error.pxi in pyarrow.lib.check_status()

## OSError: Corrupt snappy compressed data.

This was executed in google colab (I am using M1 Mac) after I ran pip install on all the requirements (there was some version conflicts highlights but I doubt this is the reason).

Sorry for the long question but would anybody be able to guide me on this?

I really wanted to get started into this journey.

Thank you so much!

*** Edit Note ***  
This is resolved by ignoring all the version stated in requirements.txt and just install all of them as latest version.

---

### Post #2 — **mic** | 2021-12-24 18:59 UTC

Why do you think the version conflicts are unrelated?

I remember hearing about some having problems with an error message about a corrupt parquet file a few weeks ago. I don’t know but maybe related?

You could also try asking on the support channel in chat

![](https://community.numer.ai/channel/support/assets/favicon_16.png) [community.numer.ai](<https://community.numer.ai/channel/support>) ![](https://community.numer.ai/channel/support/assets/favicon_512.png)

### [Numerai Community](<https://community.numer.ai/channel/support>)

---

### Post #3 — **odeforodds** | 2021-12-25 02:56 UTC _(reply to #2)_

Hi Mic,

Thank you for pointing me to the support channel. I will update the thread here if the solution is found.

_**Edit**_

This is finally resolved after I install all packages to their latest version. Big thanks to shatteredx for the advice!
