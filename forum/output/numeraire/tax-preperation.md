---
title: "Tax Preperation"
category: Numeraire
url: https://forum.numer.ai/t/tax-preperation/4954
created_at: 2022-02-15T05:21:20.572000+00:00
last_posted_at: 2023-03-13T04:49:51.746000+00:00
posts_count: 27
views: 2547
tags: []
---

# Tax Preperation

---

### Post #1 — **ihab** | 2022-02-15 05:21 UTC

Hello Numerai and fellow Data Scientists,

First, I am not sure what category this should be under. I hope I picked the correct one.

Now to the point of this topic…

When I decided to participate in this tournament in the early 2021, there was a tax article here on numer.ai that clearly defined taxable events and Numerai were issuing 1099 to tournament participants. Now that article was taken down and there is no 1099 for 2021. So how are we now supposed to figure this out on our own?

Frankly, I am really disappointed by this as I do not know how I am going to figure it out on my own.

I signed up with Cointracker but it does not correctly register stake decreases and increases. I am exploring other crypto tax preparation tools and willing to pay for more than one to compare the results and make sure that NMR transaction are correctly categorized.

I am asking for help from the Numerai people and fellow Data Scientists here on this forum. I need some recommendations for the best Crypto tax tools out there that correctly recognize NMR staking on models and/or how to correctly categorize these transaction on a tool like cointracker (or other tools).

Any help from anyone here will be greatly appreciated and it might help others as well. Thank you.

Respectfully,

---

### Post #2 — **mic** | 2022-02-15 06:12 UTC

[@pschork](</u/pschork>) and the team have generated tax reports and put them in the account. Maybe it has the information you are looking for.

Login and go to Account > Settings and there is a Tax Reports section with downloads.

---

### Post #3 — **wigglemuse** | 2022-02-15 18:02 UTC

Yes, the reports are still available, you just don’t get a 1099 (and so also aren’t reporting anything to the government). That’s an improvement! (The value that would be on a 1099 is something you can calculate yourself anyway.) So there is no less information this year than last, but I guess it is actually your first year and it is confusing no doubt. Numerai isn’t going to help you and will just say consult your tax professional – the reasons should be obvious.

There are a number of services that will help generate tax reports for crypto, but I don’t think any of them will do your NMR stuff automatically ( they will do other popular crypto exchanges, etc) but they all have a method to import transactions manually. I think I used koinly last year and it was quite straightforward and actually way easier than I thought it was going to be. (I was also worried the 1099 would create a double-reporting situation but it turned out that was fine too. But now that’s even one less thing to bother with.) How complicated it will be depends how much other crypto stuff you were buying and selling in 2021 – if you weren’t doing anything but Numerai (with only a transaction or two somewhere else to acquire or sell NMR) then it shouldn’t be that tough.

---

### Post #4 — **ihab** | 2022-02-15 20:34 UTC _(reply to #2)_

Thank you for your reply [@mic](</u/mic>)

---

### Post #5 — **ihab** | 2022-02-15 20:47 UTC _(reply to #3)_

Thank you for your reply [@wigglemuse](</u/wigglemuse>)

Correct. It is my first year. And you’re right the information is there and I downloaded them but I don’t know what to do with them because it is the first time for me.

I came across Koinly yesterday as I was searching for a tool that understands staking on Numerai Models but I was not sure if I should use it. But since you said you used it last year and it worked for you, I will give it a try.

So Koinly understands NMR transactions on a Numerai wallet? did you need to edit anything?

I need some general guidance as to how to deal with earns and burns in two cases:  
a. when payouts are not transferred back to the wallet (i.e., earns are kept with the model).  
b. when burns occur and stake is reduced to 0 and NMRs are returned back to the wallet (i.e., stake minus burns are transferred back to the wallet).

Which is a taxable event and which is not? Are payouts considered rewards (income) at the time they occur whether or not they are transferred back to the wallet or kept with the model? etc.

Are all the above understood by Koinly?

I am sure I am not alone. There must be a number of data scientists here who are having the same/similar questions and we appreciate every help we can get from Numeral, You, or anyone on this.

Thank you.

---

### Post #6 — **wigglemuse** | 2022-02-15 21:03 UTC _(reply to #5)_

It doesn’t necessarily automatically undertstand like it does some of the exchanges, but it can be made to understand (possibly with editing of the categories) to get the inputs and outputs to be registered correctly. I’m being vague because I don’t remember exactly and I haven’t yet done it for this year. (Other services should be able to do this just as well, but some are more annoying than others or just cost too much for my piddly needs.) I just remember it being easier than I thought it would be (and last year I didn’t have much crypto stuff going on besides Numerai so that made it easy also). It should be able to get the USD equivalent prices at transfer times, etc which is the important thing for declaring income in USD (and since there will be no 1099 this year, the number you come up with doesn’t have to exactly match that). That’s assuming you even made any withdrawals to wallet. Basically I was only concerned with crypto I bought on the market or other external transactions (USD → ETH → NMR, etc), with new stakes at Numerai, and Numerai withdrawals back to wallet. Anything that occurs while my NMR is staked was not considered at all (i.e. weekly payouts and burns that just roll-over to the next round) – only actual new stakes added from wallet, or NMR going back to wallet. This year should be very easy for me because I only had a handful of transactions all year and mainly just kept my NMR in the tournament and didn’t add any new NMR.

---

### Post #7 — **ihab** | 2022-02-15 21:14 UTC _(reply to #6)_

Thank you [@wigglemuse](</u/wigglemuse>)

I will give it a try.

I did not sell any NMRs.

But I reduced my stake to 0 on my signal models (i.e, I transferred from the signal model back into the wallet less than what I originally staked which was stake minus burns). So how those are treated?

---

### Post #8 — **wigglemuse** | 2022-02-15 22:33 UTC

Hey, I’m not giving tax advice either, but if you reduced your stake to 0 and you had less NMR than you put in, then the difference would be a loss, eh? (And something like koinly will keep track of that for you once you import the transactions.)

---

### Post #9 — **ihab** | 2022-02-16 02:26 UTC _(reply to #8)_

Understood [@wigglemuse](</u/wigglemuse>)

Once again, thank you.

---

### Post #10 — **ihab** | 2022-02-16 03:05 UTC

Another clarifying question anybody, please.

If I use any of the crypto tax prep tools (e.g., Cointracker, TaxBit, Koinly, etc.), which one of the three download files that Numerai provide I am supposed to use and upload?

Thank you all and apology for the many questions.

---

### Post #11 — **ihab** | 2022-02-18 02:58 UTC

Anyone please?

I need to know how to add my NMR wallet to a crypto tracking tool. Do I add it as an ETH wallet? Thank you. I have no idea and any help will be greatly appreciated.

---

### Post #12 — **wigglemuse** | 2022-02-18 03:22 UTC

Probably not as an ETH wallet because it isn’t an ETH wallet. They will have some sort of miscellaneous upload csv format. You may have to reformat it to how they like. Just have to look at their docs. All of this is less complicated than participating in Numerai – I’m sure you can figure it out.

---

### Post #13 — **ihab** | 2022-02-18 03:28 UTC _(reply to #12)_

Hi [@wigglemuse](</u/wigglemuse>)  
True. It might not be complex, nonetheless confusing. Believe me, I am confused about it.  
So If I upload a csv, which one? since Numeral provides 3 different files!  
Thank you as always ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=10)

---

### Post #14 — **wigglemuse** | 2022-02-18 03:35 UTC _(reply to #13)_

Beats me, can’t remember. When I look at them for this year, I’ll figure it out. You’re not married to anything you do with those places – play around with it, see what it seems to want and want you have in those reports. (Use the free versions.) If you screw it up, erase it and start over. No risk. Basically you are just keeping track of stuff going in and stuff going out. It might only be 2 transactions for the whole year. If your activity was minimal you may not need any service at all, you just need to look up what the NMR price was on certain days or something.

---

### Post #15 — **ihab** | 2022-02-18 04:09 UTC _(reply to #14)_

Thank you [@wigglemuse](</u/wigglemuse>)

---

### Post #16 — **themicon** | 2022-02-18 06:17 UTC _(reply to #15)_

You should be able to add your NMR wallet address to any crypto tracking tool as an ETH wallet. I’ve been able to do that on most platforms; Koinly, Coinpanda, Zenledger, etc. all support that feature, BUT they all import incorrectly and the reason is highlighted here: [Etherscan is broken - #2 by pschork](<http://forum.numer.ai/t/etherscan-is-broken/4870/2>)

You best option would be to use the CSV files provided by Numerai, or manually correct the entries imported by the crypto tracking tools.

---

### Post #17 — **ihab** | 2022-02-18 14:37 UTC _(reply to #16)_

Thank you [@themicon](</u/themicon>)

My wallet was created about a year ago (March or April of 2021). Is it one of those newer wallets?

I prefer to add my NMR wallet if I only have to do little to no corrections. But I am not exactly even sure how to correct transactions ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=10)

So if I end up having to import from a csv file, which file of the 3 I need to use? Once again, thank you.

---

### Post #18 — **ihab** | 2022-02-24 06:16 UTC _(reply to #17)_

Any hope that someone from the Numer.ai team to answer my simple question, please: “which file of the 3 I need to use with any crypto tax tool?” I also emailed support and no answer for more than a week.  
Thank you.

---

### Post #19 — **davebaty** | 2022-06-05 15:51 UTC

Hi [@ihab](</u/ihab>) did you manage to find out which of the 3 files are needed for tax reporting?

I am having the exact same issue as you had

Thank you!

---

### Post #20 — **ihab** | 2022-06-05 18:46 UTC _(reply to #19)_

Hi [@davebaty](</u/davebaty>)

I used [taxbit.com](<http://taxbit.com>) and subscribed to one of their higher level paid plans. I think I paid $175/year for this subscription. I gave them all the three files and they prepared the form for me.

Hope that helps. Good luck.

---

### Post #21 — **davebaty** | 2022-06-05 19:10 UTC _(reply to #20)_

Thanks, I appreciate taking the time to respond!

---

### Post #22 — **ihab** | 2023-03-03 23:28 UTC _(reply to #3)_

Hi [@wigglemuse](</u/wigglemuse>)  
I am using Koinly this year but not quite sure exactly how. Would you kindly share an example of how you use them? I would really appreciate it. Thank you.

---

### Post #23 — **wigglemuse** | 2023-03-03 23:31 UTC _(reply to #22)_

I can never remember, and I figure it out anew each time. I haven’t gotten into it yet for this year.

---

### Post #24 — **rdugh** | 2023-03-04 14:36 UTC

I believe if you kept NMR in the staking wallet for compounding, you are invested, there is no sale of NMR to get cash. This should not cause taxes. But I am not an expert in this. Consult a tax professional.

---

### Post #25 — **anthill** | 2023-03-10 20:08 UTC _(reply to #24)_

My understanding is that if you are staked and receive any Numeraire payouts that counts as taxable income, even if you never sold any of the Numeraire. As an analogy, if you work at Google, Google will give you stock as part of your compensation and you have to pay income taxes on that stock, even if you never sell the stock.

---

### Post #26 — **themicon** | 2023-03-11 08:48 UTC _(reply to #25)_

That depends on your country though and their tax systems. One size does not fit all in tax cases. Get a tax consultant to help you and maybe even more than one. I’ve had conflicting reports from various tax people in my country.

---

### Post #27 — **anthill** | 2023-03-13 04:49 UTC _(reply to #26)_

Very true, my statement was for the US. I can’t speak to how it might work in other countries.
