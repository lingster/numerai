---
title: "NumerBay API Question"
category: Tournament
url: https://forum.numer.ai/t/numerbay-api-question/5490
created_at: 2022-06-12T05:12:54.312000+00:00
last_posted_at: 2022-06-12T10:24:01.290000+00:00
posts_count: 4
views: 583
tags: []
---

# NumerBay API Question

---

### Post #1 — **dzheng1887** | 2022-06-12 05:12 UTC

Hey, I decided to list my models for sale on NumerBay. Would anyone know if there is an API for me to automatically upload these prediction files like I do for the tournament? Thanks.

<https://numerbay.ai/product/numerai-predictions/dz_model1>

---

### Post #2 — **restrading** | 2022-06-12 05:20 UTC

NumerBay dev here, there’s a Python client for it: [numerbay · PyPI](<https://pypi.org/project/numerbay/>)

Docs for using it for automation: [Automate Submissions (seller) | NumerBay](<https://docs.numerbay.ai/docs/tutorial-extras/api-automation>)

Please note that buyer-side file encryption is used by default, and for encrypted listings upload is only possible when you have active sale orders. For details: [FAQ | NumerBay](<https://docs.numerbay.ai/docs/faq#im-getting-upload-cancelled-no-active-order-to-upload-for>)

Feel free to post in [#numerbay](<https://rocketchat.numer.ai/channel/numerbay>) in case of any question ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=10)

---

### Post #3 — **qeintelligence** | 2022-06-12 10:00 UTC _(reply to #2)_

Was there any test-api available ? to test the upload functionality

---

### Post #4 — **restrading** | 2022-06-12 10:24 UTC _(reply to #3)_

There isn’t a test server right now. If there’s enough demand for it I can make one.
