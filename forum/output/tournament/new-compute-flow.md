---
title: "New compute flow"
category: Tournament
url: https://forum.numer.ai/t/new-compute-flow/949
created_at: 2020-09-15T19:14:23.230000+00:00
last_posted_at: 2020-09-15T19:14:23.328000+00:00
posts_count: 1
views: 976
tags: []
---

# New compute flow

---

### Post #1 — **slyfox** | 2020-09-15 19:14 UTC

Dear Computers ![:nerd_face:](https://emoji.discourse-cdn.com/twitter/nerd_face.png?v=13)

Some upcoming changes to the compute flow which will be live starting round 230 (Sep 19 2020).

  * New compute triggered / error emails - once your compute node has been triggered, we will send you either a “triggered” email if your webhook was triggered successfully (2XX http status code) or a “error” email if it did not (all other http status codes, including request timeouts)  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/09fba5f8e76d86bfd41a45b86dc9fd6b014bb198.png)image647×491 32.3 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/09fba5f8e76d86bfd41a45b86dc9fd6b014bb198.png> "image")

  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/2c0dda42e905637eb26d7ba248456d709b25fa8b_2_355x375.png)image642×677 43.7 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/2c0dda42e905637eb26d7ba248456d709b25fa8b.png> "image")

  * New success/timeout emails - once we receive all of your submissions, you will receive this a “success” confirmation. If in 24 hours we have not received all your submissions, you will instead get a “timeout” email.  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/8306ca6013c41f5ea360a286f77746141b9b2aaf_2_297x374.png)image639×805 42.8 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/8306ca6013c41f5ea360a286f77746141b9b2aaf.png> "image")

  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/4536b818099886b71432a62516e8f204e19e522d_2_360x500.png)image637×883 55.1 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/4536b818099886b71432a62516e8f204e19e522d.png> "image")

  * NO MORE RETRIES - in the past, we would try to trigger your compute node again Sunday afternoon if we have not received your submissions. We are no longer going to do this. Instead, if there are any problems with your node (webhook trigger failed, node crashed, or just taking too long to run), you will need to FIX IT MANUALLY by re-triggering your node or uploading via the website.

  * Unsubscribe - tired of compute emails? you can now unsubscribe from them. Just click the unsubscribe link at the bottom of the email. or go to numer.ai/accounts and manage your email preferences.  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/04f23764f5a572c72dbaba480aa46c981670358a.png)image479×354 9.18 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/04f23764f5a572c72dbaba480aa46c981670358a.png> "image")

  * Small bug fix - don’t trigger webhooks or send compute emails to absorbed accounts

  * Did you know you can “test” your compute webhook in the website now? Clicking this button tells our API to hit your webhook. This should help you debug any configuration issues.  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/bd7908ef4b788571c9374727f309581387a5aa0a.png)image478×293 13.3 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/bd7908ef4b788571c9374727f309581387a5aa0a.png> "image")




That’s it for now! Hope you enjoy these changes. [@arbitrage](</u/arbitrage>) now you can have your weekends back for golf ![:smiling_face_with_halo:](https://emoji.discourse-cdn.com/twitter/smiling_face_with_halo.png?v=13)  
**

[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/a952bfec0eed81344b016d2032cf04dc4dd28d3d_2_690x455.jpeg)1253×825 193 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/a952bfec0eed81344b016d2032cf04dc4dd28d3d.jpeg>)

**
