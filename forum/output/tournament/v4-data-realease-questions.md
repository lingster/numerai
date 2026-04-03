---
title: "V4 data realease - questions"
category: Tournament
url: https://forum.numer.ai/t/v4-data-realease-questions/5227
created_at: 2022-04-07T22:47:42.255000+00:00
last_posted_at: 2022-07-04T22:29:54.157000+00:00
posts_count: 15
views: 2172
tags: []
---

# V4 data realease - questions

---

### Post #1 — **sneaky** | 2022-04-07 22:47 UTC

Hi,

  * I downloaded the new v4 data and the last era (era 1004) has target filled with NaNs.  
Does the era 1004 correspond to the round 310? Respectively, is the era 1004 the current era?

  * Also, are there any missing weeks? Is it always true that era(X) and era(X+1) corresponds to consecutive weeks?

  * Another thing that I found is that compared to V3 some eras have different amount of instances. Is that OK? (I checked only validation data.)



    
    
    era  V3   V4
    0871 4910 4911
    0872 4918 4919
    0873 4932 4933
    0875 5051 5052
    0902 4997 5002
    0912 5174 5182
    0913 5001 5009
    0914 5203 5212
    0915 5185 5193
    0916 5183 5191
    0936 5192 5191
    

  * How does the mapping of features in features.json work? I wanted to harvest my previous research on features so I wouldn’t have to start over again; however, I found only an array of features inside the json file.: `json.load('features.json')['feature_sets']['v3_equivalent_features']`, so I thought it should match the ordering of features from the V3 dataset, but when I run correlation test on each pair it is not exact match.


    
    
    0.9930286498066472
    0.9973728390894694
    0.9618079870303051
    0.9936341791676602
    0.9831262504964846
    0.9934326084172069
    0.9990904802940008
    0.9916135182068833
    1.0
    1.0
    1.0
    0.9996968267646669
    0.998989490641361
    0.9987875113360812
    0.9989895927800676
    0.9989895927800676
    1.0
    0.9937375180105527
    0.9704001245800853
    0.9956573427977774
    0.9165522644319917
    1.0
    1.0
    1.0
    1.0
    1.0
    1.0
    1.0
    1.0
    1.0
    1.0
    1.0
    1.0
    

Thank you!

Sneaky

---

### Post #3 — **kgareth** | 2022-04-16 02:27 UTC

Another question: Will there be int8 versions for V4?

---

### Post #4 — **shatteredx** | 2022-04-16 03:58 UTC

[@sneaky](</u/sneaky>) [GitHub - miciasto/numerai](<https://github.com/miciasto/numerai>)

---

### Post #5 — **sneaky** | 2022-04-16 18:30 UTC _(reply to #3)_

It is there, I managed to download it via api. I am afk, but I think you just need to add sufix _int8.

---

### Post #6 — **mundan** | 2022-04-16 22:20 UTC

how can you specify in the api to download from v4 instead of v3?

---

### Post #7 — **eleele** | 2022-04-16 23:17 UTC _(reply to #6)_

[@mundan](</u/mundan>) see <https://numer.ai/data/v4>

---

### Post #8 — **orbitalteapot** | 2022-04-17 08:37 UTC _(reply to #7)_

This link should definitely be added to [Numerai Tournament Overview - Numerai Tournament](<https://docs.numer.ai/tournament/learn#data>) .

---

### Post #9 — **mundan** | 2022-04-17 09:37 UTC _(reply to #7)_

thanks! I ended up there

---

### Post #10 — **mundan** | 2022-04-17 10:59 UTC

Find here the shapes of the v3 data and v4 datav3/train v3/val v3/tour v4/train and v4/val respectively
    
    
     (2412105, 1073)  # v3/train
      (539658, 1073)  # v3/val
     (1412927, 1073)  # v3/tour
     (2420521, 1214)  # v4/train
     (2203644, 1214)  # v4/val
    

v4/val has some test entries, but most of them are validation entries (2176973 of them have targets)

No more unlabeled data then!

---

### Post #11 — **slowmoe** | 2022-05-04 09:05 UTC _(reply to #10)_

so just to settle this question, because I was wondering the same:

>   * I downloaded the new v4 data and the last era (era 1004) has target filled with NaNs.  
>  Does the era 1004 correspond to the round 310? Respectively, is the era 1004 the current era?
> 


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/a/a3a666edec14dd8203eacd94b8b302b35efc7149.png)image943×184 9.49 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/a/a3a666edec14dd8203eacd94b8b302b35efc7149.png> "image")

which means:

  * the last era that is shipped in validation data corresponds to what was shipped as live data the week before
  * in other words: `era = round + 695`

---

### Post #12 — **halvar** | 2022-05-08 18:48 UTC

Is it possible that the json file “v4/features.json” contains invalid json?

I am downloading the file via NumerAPI  
`napi.download_dataset("v4/features.json", "features.json")`

When trying to parse the file using:
    
    
    with open(".../<path to feature file>/v4/features.json", "r") as f:
        feature_metadata = json.load(f)
    features = feature_metadata["feature_sets"]["v3_equivalent_features"]
    

I get the following error:
    
    
    JSONDecodeError("Extra data", s, end)
    JSONDecodeError: Extra data
    

Also the Chrome extension “{JSON} Editor” tells me that the json is invalid.

Am I missing something here?

---

### Post #13 — **jnolan9** | 2022-07-01 14:54 UTC

All, I am just starting to work with the V4 data. I have a question, in one of the older example scripts I have, the data is sampled at every 4th era to prevent “overlap,” but looking at example scripts now, that bit of code is removed. Is it still required to get an un-duplicated set of data to sample every 4th era?

thanks

Mike

---

### Post #14 — **wigglemuse** | 2022-07-01 15:25 UTC _(reply to #13)_

Yes. That doesn’t mean you can’t train on adjacent eras, but you shouldn’t train on era X and then test/validate on era X+1 (or X+2 or X+3) because they overlap in the 20 day (4 week) targets. If you use the 60 day (12 week) targets, then your gap should be 12 eras to cover that. So it’s all about avoiding “false validation” which may or may not come into your training/validation setup. For instance, I just train on all 574 training eras (at least – with v4 even more is available) and only use the later eras validation/testing. Training on every 4th era is obviously a lot quicker and less resource-intensive too since it is only 25% of the data. You are not losing as much as it sounds like this way because the overlapped eras do tend to be very similar.

---

### Post #15 — **jnolan9** | 2022-07-04 22:22 UTC _(reply to #14)_

Is this also the case with the validation data?

---

### Post #16 — **wigglemuse** | 2022-07-04 22:29 UTC _(reply to #15)_

There is no difference between the train and validation data other than those labels. train+val as a block is simply consecutive eras (weeks) 1-1000something (whatever it is up to now).
