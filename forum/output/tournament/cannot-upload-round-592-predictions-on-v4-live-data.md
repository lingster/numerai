---
title: "Cannot upload round 592 predictions on v4 live data"
category: Tournament
url: https://forum.numer.ai/t/cannot-upload-round-592-predictions-on-v4-live-data/6722
created_at: 2023-10-12T14:26:41.534000+00:00
last_posted_at: 2023-10-13T19:27:33.809000+00:00
posts_count: 6
views: 504
tags: []
---

# Cannot upload round 592 predictions on v4 live data

---

### Post #1 — **jaca_ml** | 2023-10-12 14:26 UTC

ValueError: FileNotFoundError numerai-datasets-us-west-2/20231011/v3/numerai_live_ids_data.parquet

I got this error while trying to upload predicitons for round 592, with v4 live data. Any ideas why? It seems it is trying to acces v3 data although the live data is v4

---

### Post #2 — **waitingkuo** | 2023-10-12 14:35 UTC

i got the same issue, any one uploaded predictions successfully?

---

### Post #3 — **waitingkuo** | 2023-10-12 14:49 UTC _(reply to #2)_

it works for me now, and the upload is still on time

---

### Post #4 — **jaca_ml** | 2023-10-12 14:55 UTC _(reply to #3)_

yes, it worked for me too

---

### Post #5 — **gammarat** | 2023-10-13 02:20 UTC

I realize this is to late to help you now, but when there’s problems like this, check [Numerai Discord chat](<https://discord.gg/numerai>). Particularly the General channel, and the Support channel. Here’s the thread from this morning’s brouhaha:

![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/7/7c08661fbf4f824bf9d645ee8d76bc2b70764389.png) [Discord](<https://discord.com/channels/894652647515226152/1162017788462899271>)

![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/b/b82c5ac4e6a196fc7b1a105ce808e34ab8d22aaf_2_690x362.png)

### [Discord - Group Chat That’s All Fun & Games](<https://discord.com/channels/894652647515226152/1162017788462899271>)

Discord is great for playing games and chilling with friends, or even building a worldwide community. Customize your own space to talk, play, and hang out.

Numerai is actually pretty quick about getting these things fixed and letting us know what’s going on. Plus it’s nice to know you aren’t alone. ![:partying_face:](https://emoji.discourse-cdn.com/twitter/partying_face.png?v=13)

---

### Post #6 — **bjdottcom** | 2023-10-13 19:27 UTC

It might have been coincidence (time vs. update), but I updated my numerapi package yesterday evening and it worked.
