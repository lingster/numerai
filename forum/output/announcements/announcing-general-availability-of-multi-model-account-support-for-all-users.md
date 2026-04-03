---
title: "Announcing general availability of multi-model account support for all users"
category: Announcements
url: https://forum.numer.ai/t/announcing-general-availability-of-multi-model-account-support-for-all-users/399
created_at: 2020-05-14T18:40:19.359000+00:00
last_posted_at: 2020-05-14T18:40:19.605000+00:00
posts_count: 1
views: 3601
tags: []
---

# Announcing general availability of multi-model account support for all users

---

### Post #1 — **pschork** | 2020-05-14 18:40 UTC

Numerai is pleased to announce the general availability of multi-model account support for all users.

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/fa6b343a6b44e9d833ace33d7ce112d21b1ba9d8_2_690x414.png)image2142×1288 270 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/fa6b343a6b44e9d833ace33d7ce112d21b1ba9d8.png> "image")

  
With this release, users can quickly add (or absorb) up to 10 models to a primary account and easily manage submissions and stakes on a consolidated models management page

Multi-model account support does have some important implications that users need to understand before enabling - especially for compute/API users - so it is disabled by default. To enable it, visit the the new [Models](<https://numer.ai/models>) management page and click the Enable-Multi-Model-Support button.

[![Screen Shot 2020-05-14 at 11.02.13 AM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/cb4c9d165d736d900d28de0eb036a6a1427c1214_2_440x374.png)Screen Shot 2020-05-14 at 11.02.13 AM2034×1732 344 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/cb4c9d165d736d900d28de0eb036a6a1427c1214.png> "Screen Shot 2020-05-14 at 11.02.13 AM")

If you are a compute/API users ensure you have the latest releases and have updated your code to pass model_ids which can be found on the [Models](<https://numer.ai/models>) management page.

  * [NumerAPI >= 2.2.4](<https://github.com/uuazed/numerapi/releases/tag/2.2.4>)
  * [Numerox >= 4.1.6](<https://github.com/numerai/numerox/releases/tag/v4.1.6>)
  * [Numerai-cli > 0.1.22](<https://github.com/numerai/numerai-cli/releases/tag/v0.1.22>)
  * [Rnumerai >= 2.1.1](<https://github.com/Omni-Analytics-Group/Rnumerai>)



Numerai compute users should also be sure to checkout a new [python3-multimodel](<https://git.io/JfBvu>) example.

If you have any questions, feedback or need support, jump in the #multi-model-support room on Rocketchat.

Finally, a shoutout and special thanks to all of our beta testers for providing great feedback and bug reports during testing phase.![:vulcan_salute:](https://emoji.discourse-cdn.com/twitter/vulcan_salute.png?v=13)
