---
title: "[RFC] NumerBay Future Features Brainstorming"
category: Council of Elders
url: https://forum.numer.ai/t/rfc-numerbay-future-features-brainstorming/4198
created_at: 2021-09-25T12:03:22.110000+00:00
last_posted_at: 2021-10-25T12:57:11.733000+00:00
posts_count: 13
views: 893
tags: []
---

# [RFC] NumerBay Future Features Brainstorming

---

### Post #1 — **restrading** | 2021-09-25 12:03 UTC

It’s been an exciting week for NumerBay with its second milestone release for on-platform sales. I think this is a good time to gather community feedbacks for future features.

The following features are already planned for the coming releases. Please comment here to add other features that you would like to see. If there is enough feedback, a vote will be organized for new features.

Already planned features:

  1. ~~[Next milestone] Stake Mode (NumerBay directly submits for buyers with/without distributing raw files, and optionally may also allow sellers to set stake limits for the buyers)~~
  2. Prepaid subscription sales (E.g. pay once, download products for the next 4 weeks, etc.)
  3. Seller/product reviews by buyers & buyer reputation



Currently unplanned features:

  1. Multi-tiered pricing / Auction pricing
  2. Other payment options
  3. Mobile optimization / mobile app
  4. NumerBay Apps section to host community built products such as dashboards, etc.
  5. More buyer management for sellers, sales analytics, etc.
  6. Favorites / wishlists



Thank you for the support as always.

---

### Post #2 — **objectscience** | 2021-09-25 16:09 UTC

I’m behind the curve here a little, just getting my Numerbay account setup etc. I should have everything setup this week at some point and will officially open for business next Sat (with no expectation of selling anything for many weeks ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=9) ). Having said that, when I do start selling, I’d like to see a portion of those sales (1 to 2%?) roll back as a platform fee. It’s easy enough to make a donation to the cause, but I think a standard fee makes easier to write off for tax purposes. Never too early to think about survival after the CoE relationship ends.

On a different note, I’d also like to see a sub forum here where sellers can discuss their products a little. Add a little hype and clarity etc.

---

### Post #3 — **restrading** | 2021-09-25 16:24 UTC _(reply to #2)_

[@objectscience](</u/objectscience>) Appreciate your thoughts. Sustainability of the platform is going to be a discussion point in future after most of dev is completed. However, platform fees may have the following disadvantages in my opinion:

  1. It makes the platform less economically appealing compared to 3rd party platforms. This will especially be the case once Numerai moves on to BYOW and txns will no longer be gas-free.

  2. There is almost certainly going to be tax consequences for NumerBay and me as an entity if any money flows towards the platform as txn fees (and even regulatory problems as a crypto payment processor), instead of just being a fancy Craigslist.

  3. Technical implementation and potentially more gas cost




I’m sure there are other solutions for sustainability.

---

### Post #4 — **restrading** | 2021-10-14 00:27 UTC

Bump for more community inputs

---

### Post #5 — **nick_richers** | 2021-10-16 03:14 UTC

If there is a `technical` and `legal` way to determine the price and the payment at the round closing, we can setup performance triggers.

Eg.  
3M subscription: regular price 1nmr/round  
But if the model reaches +50% 3M returns the price is 1.2nmr/round

The payment occurs at the end of the subscription. Dunno if it is possible technically and legally

---

### Post #6 — **restrading** | 2021-10-16 03:17 UTC _(reply to #5)_

Prepaid subscription would be possible. As for pricing, it is left to the seller to decide. There will be possibly multi-tier pricing based on stake amount. As for relating pricing to performance, I am not sure of the legal side, but the seller certainly has the liberty to adjust manually.

---

### Post #7 — **nick_richers** | 2021-10-19 04:48 UTC _(reply to #6)_

more two tips here

1- I have to choose between `file` or `stake only`. Not sure from buyer side if they can choose both when I’m in `file` mode… but I don’t mind if they wanna stake only. It is useful if the buyer got a monthly subscription

2- A pack of models. model1 & model2, by 1.5NMR rather than 1NMR each.

---

### Post #8 — **restrading** | 2021-10-19 05:00 UTC _(reply to #7)_

1. In file mode, buyer can optionally designate a slot to submit to

  2. More flexible pricing is the next feature to work on. However, bundled sales is not yet planned, probably after subscription pricing.

---

### Post #9 — **nick_richers** | 2021-10-20 07:32 UTC

round summary with all trackable stakes at round closing could incentivize the buyer side…

---

### Post #10 — **restrading** | 2021-10-20 07:47 UTC _(reply to #9)_

Yes this information can be useful. Are you referring to tournament-wide summary or product-wise stake summary?

---

### Post #11 — **nick_richers** | 2021-10-20 10:16 UTC _(reply to #10)_

I guess you can track all stake only purchases… and if you consider each purchase/stake as independent model same way numerai does with your models, you can calculate “numerbay wallet” returns and show the summary on home page

---

### Post #12 — **restrading** | 2021-10-20 10:29 UTC _(reply to #11)_

Very interesting, thanks for the suggestions.

---

### Post #13 — **suud** | 2021-10-25 12:57 UTC

Scoreboard-like view for Numerai and Signals listings.

A table structure would make it easier to compare listings. Current filter and sorting is already awesome, though! So not a high priority thing.
