---
title: "Numerapi command line interface with new data format"
category: Tournament
url: https://forum.numer.ai/t/numerapi-command-line-interface-with-new-data-format/4200
created_at: 2021-09-25T20:28:18.497000+00:00
last_posted_at: 2022-06-30T20:43:28.518000+00:00
posts_count: 10
views: 1398
tags: []
---

# Numerapi command line interface with new data format

---

### Post #1 — **factorsparsity** | 2021-09-25 20:28 UTC

Hi - I’m using uuazed’s numerapi command line interface to download the Numerai data (scripted). I cannot really find the right option to change to the new data format. In fact, ideally I’d like to download only the tournament parquet file (as the other files don’t change that often). Can somebody help me out here?

---

### Post #2 — **profricecake** | 2021-09-26 00:17 UTC

napi = numerapi.NumerAPI()
    napi.download_dataset( "numerai_tournament_data.parquet")
    

This is what works for me!

---

### Post #3 — **uuazed** | 2021-09-28 09:26 UTC _(reply to #2)_

Indeed, the cli interface doesn’t work with the new data yet. I’ve ticketed it and will take a look soonish. Of course, PRs are welcome ![:wink:](https://emoji.discourse-cdn.com/twitter/wink.png?v=13)

[github.com/uuazed/numerapi](<https://github.com/uuazed/numerapi/issues/63>)

####  [allow downloading the new dataset via the cli interface](<https://github.com/uuazed/numerapi/issues/63>)

opened 09:25AM - 28 Sep 21 UTC

closed 06:33AM - 07 Oct 21 UTC

[ ![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/f/f024be723c90ef83a7a6692854be20cf16868a81.png) uuazed ](<https://github.com/uuazed>)

---

### Post #4 — **factorsparsity** | 2021-10-11 19:48 UTC

Nice. Does uploading work with both old and new datasets?

(Small comment BTW: the warning says “use download_dataset_old” but should say “use download-dataset-old” (for command line users))

---

### Post #5 — **uuazed** | 2021-10-14 07:04 UTC _(reply to #4)_

Thanks for pointing out the type, I fixed that. Uploading now also works for both datasets when using the command line interface. You need to add `--new-data` flag

---

### Post #6 — **factorsparsity** | 2022-06-26 15:22 UTC

Hi - Is it planned to implement the cli interface for the v4 data also?

---

### Post #7 — **uuazed** | 2022-06-28 12:26 UTC _(reply to #6)_

Have you tried? Anything not working?

---

### Post #8 — **factorsparsity** | 2022-06-28 18:41 UTC

Yes.

numerapi download-dataset --filename numerai_tournament_data.parquet

works, but

numerapi download-dataset --filename “v3/numerai_tournament_data.parquet”  
numerapi download-dataset --filename “v4/live.parquet”  
numerapi download-dataset --filename live.parquet

do not (with or without quotes). Also, I wouldn’t know which switch to use for submitting, as “–new_data” obviously assumes version v3, not v4. I haven’t tried that yet though.

---

### Post #9 — **uuazed** | 2022-06-30 06:59 UTC _(reply to #8)_

I double checked and made some tweaks to numerapi. Both, downloading and uploading, should now work via the cli.

  * re downloading: Check that the filename is valid by calling `numerapi --list-datasets`. If the filename contains a directory, like `v3`, it tries downloading to a directory as well. The latest numerapi version will ensure directories exist. The other workaround is to specify the `dest_path` explicitely` or to create the directory manually.
  * re uploading: that `--new_data` flag is no longer needed and uploading works the same across all data versions. In fact, the live ‘ids’ are the same for v2, v3 and v4.

---

### Post #10 — **factorsparsity** | 2022-06-30 20:43 UTC _(reply to #9)_

Thanks. Creating the directory beforehand did the trick. I also hadn’t upgraded to the latest version (which then, as you say, doesn’t need the directory anymore). Shame on me. Will try the submission on Saturday.
