---
title: "US Taxes from the Numerai (corporate) side... and the trickle down"
category: Numeraire
url: https://forum.numer.ai/t/us-taxes-from-the-numerai-corporate-side-and-the-trickle-down/7562
created_at: 2024-07-10T19:15:58.913000+00:00
last_posted_at: 2024-07-11T18:57:29.279000+00:00
posts_count: 6
views: 582
tags: []
---

# US Taxes from the Numerai (corporate) side... and the trickle down

---

### Post #1 — **pumplerod** | 2024-07-10 19:15 UTC

While I struggle, like many in the US on how to accurately report earnings vs cap gains relating to Numerai, I’m wondering what it looks like from the Company’s side of things.

For example, if they generated 11MM NMR out of thin air, and it initially began selling for $40/NMR, even though much was held in reserve, does that effectively mean that Numerai the company was required to file an income gain of $440MM with the IRS in that year?

And if receiving NMR based on our performance is considered “income” for us, does that mean that the company needs to report the distribution as a cost of doing business, for each day, at the going rate for NMR on that day?

And now that the earn/burn is all effectively happening “off-chain” until we actually pull the NMR out of their system, is the IRS only concerned with what goes into the Numerai system vs what comes out? It seems to me that whether you track every daily earn/burn, along with it’s value for that day and then re-adjust for the value at the time you pull NMR out, Or just keep track of the overall in/out of what ultimately gets turned into cash, it basically should end up roughly the same. And tracking every tick of each daily earn/burn along with the fluctuation of stake and final conversion is definitely a full time job.

I’m testing out <https://coinstats.app> to see how well that might be able to resolve the headache, but since daily earn/burn now happen off-chain, those events no longer show up.

If there is an accepted formula for this it certainly seems like there could be a published spreadsheet which can pull in the historical transactions and make sense of it all without each person needing to wrestle with their own personal solution.

I realize the Numerai team cannot provide tax advice for legal reasons. But if anyone has a spreadsheet they could publish or even suggest some other crypto tracking SAS platform it would really be helpful.

---

### Post #2 — **anthill** | 2024-07-10 21:03 UTC

The mechanisms that Numerai is using are novel enough that I don’t think that anyone yet knows what the “correct” tax implications are. I assume that they are, like the rest of us, making their best guess (though I assume they have spent more on tax attorneys than we have).

I don’t think that generating the NMR token de novo is a taxable event. The token is not stock and doesn’t come with any corresponding ownership rights or legal claims the way that stock does. It’s not obvious that it should have any intrinsic value. If I recall correctly the first trades of NMR came several days after the token was created and were at very low volumes. So I don’t think it would make sense to claim that the creation of the NMR token resulted in $440MM in income. (Just my opinion — an aggressive IRS agent could disagree!)

As to payouts it probably depends on the way they are doing accounting and the fine text of the terms of service. But I would speculate that the proper way of doing this would be to list NMR that they hold on behalf of user’s is booked as a liability whereas NMR that they hold in their treasury is an asset. Then anytime they make a payout they would record an expense even if nothing has changed on chain. (Similarly a bank would record an interest payment to you as an expense even though all they have done is update their internal ledgers.) So they would have a daily expense based on the cash value of the total NMR paid out that day. On the other side of the ldeger I believe that they would have to book as income the capital gains that they have seen on the NMR. So if NMR is at $10 and they pay out 100 NMR, they would have an expense of $1000 but also an income of $1000 because the cost basis of the NMR is $0. So on net they would have no income or loss.

Once they have made the payout, it’s not really “their” NMR anymore, even though they are holding it in custody for you. So for accounting purposes they probably don’t care what you do with it after that, whether you leave it in the system or pull it out.

---

### Post #3 — **pumplerod** | 2024-07-10 22:48 UTC _(reply to #2)_

Interesting take, thank you. It’s all super confusing for me, and each time I speak with a CPA they seem to be kind of taking a guess, which always seems to involve the most work possible on my end.

---

### Post #4 — **anthill** | 2024-07-10 23:12 UTC _(reply to #3)_

FYI, for our own individual taxes, Numerai does provide a CSV file that contains a record of all payouts, burns, and the price of NMR at the time of these events, so you don’t independently need to collect NMR prices yourself.

---

### Post #5 — **pumplerod** | 2024-07-11 18:42 UTC _(reply to #4)_

Yes, I do utilize that. However fully connecting those earnings and losses in combination with any buys and sells, managing cost basis, etc into a final number is a rather herculean effort.

---

### Post #6 — **anthill** | 2024-07-11 18:57 UTC _(reply to #5)_

It’s worthwhile to write a Python script (or whatever your favorite language is) to merge the Numerai CSV and the exchange CSV and track the cost basis. Takes a bit of upfront work, but once it’s done it’s pretty straightforward to calculate your taxes going forward.
