---
title: "Etherscan is broken"
category: Numeraire
url: https://forum.numer.ai/t/etherscan-is-broken/4870
created_at: 2022-01-29T22:57:27.491000+00:00
last_posted_at: 2022-02-19T03:32:36.316000+00:00
posts_count: 7
views: 1354
tags: []
---

# Etherscan is broken

---

### Post #1 — **ganon** | 2022-01-29 22:57 UTC

Please excuse my click bait title, but I am trying to calculate some stuff and it seems to me our friends at Etherscan may have forgotten basic math.

Now, more specifically, I have collected all NMR transactions on the blockchain so that I could gain historical perspective, as well as some other information. Part of my information compilation extravaganza is the current NMR balance of all NMR addresses that have ever been used. However, when I was reviewing the data, I noticed some… inconsistencies. See [here](<https://etherscan.io/token/0x1776e1f26f98b1a5df9cd347953a26dd3cb46671?a=0x0000000000000000000000000000000000000075>) as an example of where, I postulate, the reported balance on Etherscan is wrong (I intentionally chose a simple example so it would be obvious there was an error.)

Clicking on that link will reveal there are three transactions in this example, each adding to the address 0x0000000000000000000000000000000000000075. Now, you’ll have to forgive me, I did not get a PhD in math so I’m only guessing when I say that 0.1907843 + 0.1 + 0.1 is 0.3907843 and NOT 0.2907843 as Etherscan as suggested. My question, dear subjects of Numerai-dom, is how is this is possible? What am I missing? Do I have a smooth brain (just be honest, I can take it)?

If that example is not enough for you, I have found some more addresses with the same problem. View them at your own leisure (formatted as address - expected NMR balance, Etherscan NMR balance, # of transactions for that address. Sorry I didn’t know how to make a table.)

0x00000000000000000000000000000000000000e0 - Expected: 36.38124031668799, Got: 1.3212403166879967, Txns: 130  
0x00000000000000000000000000000000000000ed - Expected: 76.50000000097874, Got: 9.78750619e-10, Txns: 71  
0x00000000000000000000000000000000000000f1 - Expected: 62.180422213195186, Got: 54.28042221319519, Txns: 68  
0x0000000000000000000000000000000000000104 - Expected: 4.271598, Got: 0.771598, Txns: 46  
0x0000000000000000000000000000000000000075 - Expected: 0.3907843, Got: 0.2907843, Txns: 3  
0x00000000000000000000000000000000000001ed - Expected: 200.89549419276224, Got: 62.145494192762236, Txns: 102  
0x00000000000000000000000000000000000001f2 - Expected: 85.00000463431584, Got: 70.00000463431584, Txns: 73  
0x000000000000000000000000000000000000012d - Expected: 5.10580006, Got: 4.10580006, Txns: 5  
0x0000000000000000000000000000000000000165 - Expected: 909.0, Got: 0.0, Txns: 188  
0x000000000000000000000000000000000000016e - Expected: 174.605367394, Got: 144.605367394, Txns: 65  
0x00000000000000000000000000000000000000ca - Expected: 46.7228288379, Got: 1.002828837900002, Txns: 58  
0x00000000000000000000000000000000000002e7 - Expected: 6.301325870395709, Got: 0.15132587039570825, Txns: 58  
0x00000000000000000000000000000000000003e2 - Expected: 79.5037006452, Got: 39.9036006452, Txns: 59  
0x0000000000000000000000000000000000000388 - Expected: 234.440219, Got: 223.440219, Txns: 4  
0x0000000000000000000000000000000000000216 - Expected: 30.123519, Got: 21.123519, Txns: 36  
0x000000000000000000000000000000000000025d - Expected: 3919.59301808111, Got: 1589.5930180811101, Txns: 500  
0x000000000000000000000000000000000000041e - Expected: 25.265008347896284, Got: 0.7650083478962841, Txns: 155  
0x000000000000000000000000000000000000053d - Expected: 633.0458263664165, Got: 541.6958263664164, Txns: 192  
0x00000000000000000000000000000000000004e1 - Expected: 0.2, Got: 0.0, Txns: 33  
0x00000000000000000000000000000000000005f8 - Expected: 24.52773842, Got: 23.52773842, Txns: 15  
0x0000000000000000000000000000000000000500 - Expected: 69.57459223047664, Got: 33.83459223047664, Txns: 28  
0x000000000000000000000000000000000000050e - Expected: 474.83288188684077, Got: 470.73288188684074, Txns: 194  
0x0000000000000000000000000000000000000753 - Expected: 137.19890813701824, Got: 125.19890813701824, Txns: 17  
0x0000000000000000000000000000000000000775 - Expected: 36.467264133361894, Got: 18.467264133361898, Txns: 343  
0x00000000000000000000000000000000000007dd - Expected: 1.700000396702247, Got: 3.96702246989e-07, Txns: 28  
0x00000000000000000000000000000000000007e0 - Expected: 43821.7578598, Got: 0.0078598, Txns: 7  
0x00000000000000000000000000000000000007f9 - Expected: 190.313913683, Got: 144.313913683, Txns: 39  
0x0000000000000000000000000000000000000680 - Expected: 27.0063820987, Got: 8.0063820987, Txns: 87  
0x0000000000000000000000000000000000000684 - Expected: 15.223406760918003, Got: 14.223406760918003, Txns: 21  
0x000000000000000000000000000000000000069f - Expected: 191.41168841581856, Got: 24.411688415818563, Txns: 264  
0x00000000000000000000000000000000000006de - Expected: 0.8006064323186601, Got: 0.000606432318660085, Txns: 106  
0x00000000000000000000000000000000000007a5 - Expected: 6.104016, Got: 0.004016, Txns: 38  
0x00000000000000000000000000000000000006bf - Expected: 435.87877188462124, Got: 31.298771884621257, Txns: 14  
0x00000000000000000000000000000000000006e9 - Expected: 8.8, Got: 5e-18, Txns: 103  
0x00000000000000000000000000000000000007a6 - Expected: 22.00078267538513, Got: 0.000782675385128397, Txns: 12  
0x00000000000000000000000000000000000007a7 - Expected: 30.173739876594674, Got: 26.173739876594674, Txns: 26  
0x0000000000000000000000000000000000000727 - Expected: 54.550333441428805, Got: 5.550333441428806, Txns: 34  
0x0000000000000000000000000000000000000730 - Expected: 34.82, Got: 0.0, Txns: 42  
0x0000000000000000000000000000000000000739 - Expected: 15.643820089283285, Got: 3.0438200892832836, Txns: 60  
0x000000000000000000000000000000000000094b - Expected: 55.00090964, Got: 0.00090964, Txns: 44  
0x000000000000000000000000000000000000094e - Expected: 740.0, Got: 300.0, Txns: 348  
0x0000000000000000000000000000000000000953 - Expected: 1.810000096702247, Got: 9.6702246989e-08, Txns: 26  
0x000000000000000000000000000000000000096d - Expected: 70.45518377923113, Got: 44.45518377923114, Txns: 191  
0x0000000000000000000000000000000000000898 - Expected: 163.993845, Got: 0.003845, Txns: 18  
0x000000000000000000000000000000000000089f - Expected: 8.3789589132, Got: 0.17895891320000007, Txns: 17  
0x000000000000000000000000000000000000082b - Expected: 792.3659006224101, Got: 99.41090062241008, Txns: 197  
0x000000000000000000000000000000000000097d - Expected: 200.40004774996302, Got: 4.7749963030532e-05, Txns: 324  
0x0000000000000000000000000000000000000861 - Expected: 47.60057891768566, Got: 0.000578917685657223, Txns: 27  
0x000000000000000000000000000000000000087f - Expected: 17.128526, Got: 0.128526, Txns: 4  
0x0000000000000000000000000000000000000888 - Expected: 6.9, Got: 0.0, Txns: 124  
0x00000000000000000000000000000000000008b2 - Expected: 16.931967145723032, Got: 0.4319671457230333, Txns: 8  
0x00000000000000000000000000000000000008ba - Expected: 88.90352431019711, Got: 0.6035243101971138, Txns: 315  
0x00000000000000000000000000000000000008d4 - Expected: 24.0999371, Got: 13.0999371, Txns: 42  
0x0000000000000000000000000000000000000904 - Expected: 602.846495111256, Got: 602.346495111256, Txns: 21  
0x0000000000000000000000000000000000000a70 - Expected: 303.21334682136126, Got: 300.21334682136126, Txns: 6  
0x0000000000000000000000000000000000000a96 - Expected: 312.06782959494444, Got: 0.507829594944469, Txns: 85  
0x0000000000000000000000000000000000000c28 - Expected: 113.08078960152078, Got: 65.08078960152078, Txns: 28  
0x0000000000000000000000000000000000000b1a - Expected: 1143.1339642702235, Got: 1139.3339642702233, Txns: 77  
0x0000000000000000000000000000000000000bcd - Expected: 5.27434923, Got: 0.27434923, Txns: 8  
0x0000000000000000000000000000000000000bf1 - Expected: 148.9127349549427, Got: 0.11273495494268887, Txns: 122  
0x0000000000000000000000000000000000000c0c - Expected: 75.36431932055318, Got: 73.36431932055318, Txns: 28  
0x0000000000000000000000000000000000000d3b - Expected: 0.45117976, Got: 0.35117976, Txns: 3  
0x0000000000000000000000000000000000000d55 - Expected: 0.4, Got: 0.0, Txns: 41  
0x0000000000000000000000000000000000000d93 - Expected: 584.169448957308, Got: 0.06944895730799734, Txns: 383  
0x0000000000000000000000000000000000000dda - Expected: 832.2648097959479, Got: 831.064809795948, Txns: 39  
0x0000000000000000000000000000000000000dde - Expected: 259.1000000008799, Got: 8.79902688e-10, Txns: 313  
0x0000000000000000000000000000000000000e17 - Expected: 818.0, Got: 800.0, Txns: 6  
0x0000000000000000000000000000000000000e26 - Expected: 19.5, Got: 0.0, Txns: 15  
0x0000000000000000000000000000000000000e3f - Expected: 263.0003364042072, Got: 0.000336404207207894, Txns: 25  
0x0000000000000000000000000000000000000e40 - Expected: 164.52052945627412, Got: 122.42052945627411, Txns: 88  
0x0000000000000000000000000000000000000ded - Expected: 3.51889036333089, Got: 0.018890363330889944, Txns: 7  
0x0000000000000000000000000000000000000ccb - Expected: 805.3, Got: 0.0, Txns: 335  
0x0000000000000000000000000000000000000df1 - Expected: 2.4, Got: 0.0, Txns: 46  
0x0000000000000000000000000000000000000cfb - Expected: 1.6646553, Got: 0.8646553, Txns: 5  
0x0000000000000000000000000000000000000cfe - Expected: 97.6291719105031, Got: 0.029171910503108113, Txns: 134

---

### Post #2 — **pschork** | 2022-01-30 22:24 UTC

You’re right. Etherscan is _not_ the source of truth of all chain transactions, the Ethereum blockchain is.

The wallet balance displayed on Etherscan _is_ correct because Etherscan is simply querying the NMR contract `balanceOf` for the specified wallet. This number is coming from the source of truth - the blockchain.  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/4/4ce8241fdc5301ce7a3e3b4704620dc3cc776ba7_2_690x71.png)image1768×184 19.2 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/4/4ce8241fdc5301ce7a3e3b4704620dc3cc776ba7.png> "image")

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/b/b416053b51ae83f735013ef37efa4c223519b1dd_2_675x500.png)image916×678 34.4 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/b/b416053b51ae83f735013ef37efa4c223519b1dd.png> "image")

The ERC-20 transactions tab on Etherscan, however, is _not_ querying the blockchain. Those transactions are a kind of materialized view that Etherscan constructs based on their own ingestion pipeline that processes all transactions since epoch. You can’t ask Infura or Geth for all transactions for a given wallet - you need to construct this yourself by processing all transactions ever made starting from epoch.

The reason why there is a discrepancy between ERC-20 tab transactions and the wallet balance is because the early versions of the NMR contract were not ERC-20 compliant and did not emit ERC-20 transfer events. Because of this, these early NMR transfers are interpreted as ETH transactions, or not at all.

Early version of the NMR contract can be found at [0xc75498c67386eba37af1e35d54744d15064ef70f](<https://etherscan.io/address/0xc75498c67386eba37af1e35d54744d15064ef70f>)

If you click on that contract you will see that it lists NMR transfers under the Transactions tab, not the ERC-20 tab. Early version of this contract used the `numeraiTransfer` function, as opposed to `transfer`, and did not properly emit token transfer events. There were probably other issues that were fixed along the way that I am not familiar with, but suffice to say that these were early days on Ethereum and standards were still in flux.

Lastly, the balance discrepancy you’ve identified only impacts old wallets that interacted with the early contracts. Newer wallets that have only interacted with the latest NMR contract do not have this issue.

Moral of the story, Etherscan is great and super convenient, but is not the source of truth. The blockchain is.

---

### Post #3 — **ihab** | 2022-02-18 15:19 UTC _(reply to #2)_

Hi [@pschork](</u/pschork>)

I used the balance of (which as you said, it supposed to query the blockchain) and found a big discrepancy.

My Numerai wallet has only 16.84 NMR, however my the balanceOf on etherscan shows 29.88 nmr. What you think the source of this discrepancy? Thank you.

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/c/c7b5b1d5720b2ca41561990b8c2c2cec6e11c974.png)image546×292 15.1 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/c/c7b5b1d5720b2ca41561990b8c2c2cec6e11c974.png> "image")

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/c/c303e958c3b64a41c9c750113a1c0e73b16619a9.png)image421×234 3.4 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/c/c303e958c3b64a41c9c750113a1c0e73b16619a9.png> "image")

---

### Post #4 — **ganon** | 2022-02-18 15:49 UTC

Hi [@ihab](</u/ihab>),

I think I might be able to shed some light on this. The available balance on your NMR wallet shows how much NMR is instantly available to you, not necessarily how much NMR you have. For instance, if you deposit 50 NMR into your wallet, then stake 50 NMR, your available balance will be 0 NMR, not 50 (since it is staked, it is not considered “available”.)

I will also note that, as I understand it, Numerai, to save ETH on gas, does not push transactions onto the chain as they happen. Rather, they only post transactions when they need to (so they can aggregate them.) Your Etherscan balance should reflect all the NMR you have deposited and withdrawn to the address, not necessarily the amount of NMR you have in your Numerai wallet, since it is sometimes off-chain.

---

### Post #5 — **ihab** | 2022-02-19 00:04 UTC _(reply to #4)_

Hi [@ganon](</u/ganon>)

Thank you for your reply.

But I barely have any activities for a few months, so how could the blockchain balancOf be way off from my Numerai wallet.

This is very concerning and I believe some one from Numerai needs to look into this, please. I would really appreciate that.

---

### Post #6 — **wigglemuse** | 2022-02-19 00:20 UTC

[@ihab](</u/ihab>) But do you still have anything staked in the tournament(s) or did you pull everything out? BTW, my wallet is basically empty (which is correct), but shows 60-something NMR on etherscan. But I also have hundreds of NMR currently staked which has been building up over time. How much is your wallet supposed to have according to your own staking and withdrawals? 16.84 probably, right? Or are you saying that’s wrong and you are missing something?

---

### Post #7 — **ihab** | 2022-02-19 03:32 UTC _(reply to #6)_

Hi [@wigglemuse](</u/wigglemuse>)

Yes I do have staked models in the tournament but I also have a small balance in my Numerai wallet.

My Numerai wallet currently shows that I have 16 NMR which I believe is correct.

However, my etherscan balanceOf query shows that I have 29 NMR which is not matching my actual Numerai wallet balance.

If the balanceOf queries the blockchain as per [@pschork](</u/pschork>) and therefore it supposed to be the most accurate, then there must be an error somewhere. Any idea what that could be? I have no clue and I need help, please.

I hope this is something the Numerai people could help me with.

Once again, thank you.
