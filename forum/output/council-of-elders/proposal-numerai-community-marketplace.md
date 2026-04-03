---
title: "[Proposal] Numerai Community Marketplace"
category: Council of Elders
url: https://forum.numer.ai/t/proposal-numerai-community-marketplace/3622
created_at: 2021-06-19T13:22:50.853000+00:00
last_posted_at: 2021-08-04T01:54:02.956000+00:00
posts_count: 39
views: 3584
tags: []
---

# [Proposal] Numerai Community Marketplace

---

### Post #1 — **restrading** | 2021-06-19 13:22 UTC

Thanks to [@arbitrage](</u/arbitrage>) for the draft feedback.  
This proposal follows the [format](<http://forum.numer.ai/t/how-to-write-a-coe-proposal/3287>) suggested by [@jrb](</u/jrb>)

Anything in the below proposal is open for discussions and changes. Thank you for the feedback in advance.

* * *

**1.Proposal**  
**Tl;dr** : I’d like to build an open-sourced prototype of a StockX-style marketplace for Numerai model predictions. A static mockup: 

[![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/1/1c846a30a072b7d30f4b8eeb48f33e66d4aba879_2_690x481.png)743×518 47.2 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/1/1c846a30a072b7d30f4b8eeb48f33e66d4aba879.png>)

**Ideation** : The idea hit me during my recent [GPU hunting craze on StockX](<https://stockx.com/nvidia-evga-geforce-rtx-3090-ftw9-ultra-gaming-24gb-gddr6x-backplate-graphics-card-24g-p5-3987-kr>). StockX is a stock-market-like online marketplace for consumer goods (sneakers, electronics, etc.) that emphasizes authenticity and price discovery. I thought its auction mechanism and item authentication mechanism can be desirable for a marketplace of Numerai predictions, too.

This project is meant to be a proof-of-concept demo showcasing an ideal user experience for both sellers and buyers of Numerai model predictions. This would lay the foundation for future contributions to make it fully production-ready. Core UX and features will be functional, but things like payments and cybersecurity won’t be the focus of this project.

**Problem statement** :  
Like many tournament participants, I want to be able to sell my predictions to friends or strangers alike to monetize my models further. There is a lack of a go-to marketplace and people are trying various ways, such as NFTs, e-commerce platforms, generic data exchanges or even offline. This is not efficient for either party. Moreover, there are some Numerai-specific needs these methods could not accommodate, such as model ownership verification, enforcement of prediction file consistency, price discovery, intellectual property protection, automated submission and fraud protection, etc.

**Solution** : A community-run marketplace that will tackle the above pain points. The platform will have the following features:

a. **Core features** :

  1. **Buy-and-sell with price discovery** : In addition to the basic buy-and-sell functionalities, there is a limit order book mechanism for price discovery of model predictions. The seller puts up predictions for sale for each model each round, and has full-control over the ask-side of the order book to determine how many files to sell at each price _[denoted as “File Mode”]._ Alternatively, the seller can control how much NMR stake can be put on each file sold by using the number of NMRs as the transaction unit instead of the number of files, _[denoted as “Stake Mode”]_.  
_[@arbitrage](</u/arbitrage>) pointed out that model predictions are not common goods like sneakers, they are unique and hence the ask side of the order book can be redundant here. This is true, each model’s sell-side of the order book can only be managed by the single seller of this model. However, in Stake Mode this can be useful. The seller can effectively perform tiered pricing of the amount of stakes allowed by managing the sell-side order book. E.g. Sell 100 NMR allowance at $50, Sell 500 NMR allowance at $100, such that the buyer would have to progressively pay more if they want to stake more._
  2. **Ownership verification** : Buyers can be assured that the files belong to the seller’s model. During seller onboarding, the seller would prove ownership of models by putting up a one-time code to their model descriptions temporarily, similar to how domain name ownership verification is done. Payouts to sellers are locked-up until at least the first live score. The live score would be compared to the seller’s own submission for consistency check.
  3. **Intellectual property protection** : For sellers concerned about buyers abusing their files, they can opt for selling in _Stake Mode_. The platform will facilitate automatic submission for the buyers such that they would not have access to the raw file yet can still stake on it.
  4. **Fraud protection** : Each seller needs to lock up a collateral amount with the platform during onboarding. And for any model sold in Stake Mode, each buyer needs to lock some collateral amount at the time of the transaction. Transaction proceeds are withheld from the seller until live scores are checked for consistency. If inconsistent, the proceeds are returned to the buyers, and the seller will lose some collateral with the platform. For Stake Mode transactions, violations from the buyer such as over-staking (if the file was sold through automated API submission) can result in loss of collateral for the buyer.



b. **Extended features** _(Good to have if I have the time)_ :

  1. Support for sale of Signals Predictions
  2. Support for sale of model file/scripts
  3. Email notifications



c. **Optional features** _(If I have the time and ability, or something for future contributors to consider)_ :

  1. NMR for payment and collateral _[I know this is essential for anything beyond demo, and will try my best to implement it]_
  2. Fraud protection enforcement using Erasure
  3. Make this a dApp



**Auxiliary notes** :

  1. I will try to keep the code modular and well-commented for ease of future contributions from others. I have some experiences with traditional websites and web apps, but have not built any dApp. Therefore I will use a traditional backend for now. The main focus of this project is showcasing the user experiences and to serve as a starting point for future contributions.
  2. I will try to maintain a good separation of front and back-end of the app to make transition to dApp easy.
  3. Dummy payment processing first, but I will try to make real NMR payments possible if I have time after completing other features. For obvious reasons I won’t use any credit card payment processing services (but if you guys want it, I can easily support Stripe).
  4. Upon delivery of the project, I will keep this hosted for up to 3 months on Google Cloud for the community to test and gather feedback.



* * *

**2.Timeline**  
If approved, the earliest date I can start is July 15. I will commit full-time for 4-6 weeks.

**3.Best case outcome**  
All features are implemented and functional in a timely manner. The platform is well-received by the community and resulted in a lot of constructive feedback. An open-source team is formed to further improve the project, making it a production-grade platform that is trusted by the community and owned by the community. More users start buying and selling predictions. NMR gets another use case that benefits NMR holders and sees more adoptions. I am rewarded with a nice amount of NMRs too. The same platform can even be used for selling other Numerai stuff such as Signals data, Signals predictions, model files and scripts.

**4\. Worst case outcome**  
I lose the ability to work on this for unforeseeable reasons and nothing gets done. I will be paid nothing. In that case, anyone in the community is welcome to take over this proposal and build it. At worst we still have this thread as an ideation for how this kind of platform should be until someone decides to build it.

**5.Success criteria**  
Success should be evaluated upon the delivery of the open-sourced code and deployment of the test platform, according to how much of the features above are implemented and are functioning properly.

**6.Funding required, if any.**  
I don’t seek to make a ton of money out of this but need enough to keep me committed to the labor and to cover any cost, to be paid only after work delivery and evaluation. CoE can apply any deduction or addition at the end based on the evaluation of work quality. Fees can be broken down by features. The community can decide the weight of each feature. I suggest the following as a starting point:

a. Core Features (Total: 69.420 NMR)

  1. Price discovery (and basic buy-sell): 30 NMR
  2. Ownership verification / seller onboarding mechanisms: 10 NMR
  3. Intellectual property protection / automated submission: 15 NMR
  4. Fraud protection: 10 NMR
  5. Hosting cost (dev + 3 months): 4.420 NMR



b. Extension Features (Total: 30 NMR)

  1. Support for sale of Signals Predictions: 15 NMR
  2. Support for sale of model file/scripts: 15 NMR
  3. Email notifications: Free



c. Optional Features (Total: 60 NMR+?)

  1. NMR for payment and collateral: 30 NMR (labor+gas)
  2. Fraud protection enforcement using Erasure: 30 (labor+gas)
  3. Make this a dApp: ?



* * *

**Additional asks** :

  1. Permission from the Numerai team to create an additional account for dev and testing
  2. One contact person from CoE for continuous feedbacks during the project



**Some key points for discussions** :

  1. Feature scope
  2. Payment and collateral rules & mechanisms
  3. Deliverables and evaluation
  4. Funding amount and structure
  5. Anything else



EDIT:  
2020-06-30 - Postponed earliest start date

---

### Post #2 — **restrading** | 2021-06-19 13:32 UTC

What is your sentiment about this proposal?

  * This sounds great!
  * Not too sure about this…
  * This is ridiculous! smh…
  * But what about …? [Please leave your comments below]



0 voters

---

### Post #3 — **hb_scout** | 2021-06-19 15:24 UTC _(reply to #2)_

I would very much like a centralized market place for selling predictions. I think that will bring in a lot more buyers than just one-off individuals trying to sell where ever they find easiest. Like the concept a lot.

One comment to start, it seems like your concept is to lock up everyone’s funds until it can be seen that the live scores match? I think there’s a lot of value in buying predictions in order to ensemble them. That’s how people buying my NFT predictions have used them in the past. So their live scores never actually match any of mine. It might just have to be “you have one week to say you didn’t get what you expected or the funds are automatically paid out” or something along those lines.

---

### Post #4 — **restrading** | 2021-06-19 15:32 UTC _(reply to #3)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/hb_scout/48/138_2.png) hb_scout:

> I think there’s a lot of value in buying predictions in order to ensemble them.

[@hb_scout](</u/hb_scout>) Thanks for the first comment! That’s a very good point. What about the following? :

  * In File Mode (which would be the way of selling for the purpose of ensembling, etc.), proceeds are delivered to seller immediately, as there is no way to verify the consistency of user’s submission anyway. Exception being if buyer opts for automated submission in which case consistency check is possible.
  * In Stake Mode, since the buyer won’t have access to the raw file anyway, keep the same lock and collateral mechanism in the original proposal.

---

### Post #5 — **wigglemuse** | 2021-06-19 16:17 UTC

Something like this think (a market) is the best way to go – I said something along these lines in previous threads on the topic. The more the buying and selling can be a free-for-all without a bunch of commitments from either party the better it will be. I agree with [@hb_scout](</u/hb_scout>) about the ensembling – if the buyer wants to verify the predictions are the same as the seller is also submitting but doesn’t want to use them in that form, they can use a secondary unstaked slot where they can be submitted unaltered and they’ll see that they match. In any case, I think the buyer should actually get the predictions so they can mix & match them as they desire rather than have somehow submitted for them to their slots (as is sometimes suggested).

---

### Post #6 — **restrading** | 2021-06-19 16:27 UTC _(reply to #5)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/wigglemuse/48/3094_2.png) wigglemuse:

> I think the buyer should actually get the predictions

[@wigglemuse](</u/wigglemuse>) Yes I like the ensembling use case too. The buyers will be able to get the predictions if the model is sold in File Mode. However, I think a seller should be able to choose to sell only in Stake Mode to allow buyers to stake without getting the actual file, if they have concerns like preventing model distillation, unauthorized resales, etc.

As for consistency check in File Mode, buyers have the freedom to submit the raw file in a separate slot, however the platform would not be able to enforce anything even in the case of inconsistency, unless such submission is done automatically by the platform. A solution could be the buyer provides a submission API key to the platform, the platform submits the untouched raw file to one of buyer’s designated slots for consistency checks.

---

### Post #7 — **wigglemuse** | 2021-06-19 17:07 UTC

Some sort of reputation system of successful sales ought to keep people honest. There really is no particular incentive to screw somebody over that I can think of. And nobody is going to buy unproven predictions without a good track record on live. If we do have bad actors trying to game the system, I don’t think they’d do that by trying to give the buyer the “wrong” predictions – what is more likely is people using up their own slots on a bunch of very different high-risk high-reward models and hope one of them rockets to the top of the leaderboard and then they can sell it for a few rounds before it tanks again. Which may or may not go badly for the person buying as it may do just fine for a while. I mean that’s actually a legit strategy if you are a gambling type. The question is will anybody buy anything that isn’t significantly staked by the owner? Part of the point of all this would be to get money flowing to people that can’t afford to stake a lot themselves, but of course a bad actor using a shotgun strategy would also stake very little and claim poverty. (I think revealing the names of all the model slots owned by sellers is probably a good idea – is that actually part of the API now?) In any case, trying to abuse such a system seems like too big a hassle for people that like to abuse such systems – there are easier marks. Spending the time to make a decent model and selling it honestly is just as easy.

---

### Post #8 — **jrai** | 2021-06-19 17:49 UTC _(reply to #7)_

I like the proposal and would think about both buying/selling predictions. The idea of a reputation system also makes the most sense to me. With a reputation system, this all can probably be built out as a centralized front-end to opensea listings with additional comments/reviews functionality and numerai specifics (showing rank, stake, history, etc.)

---

### Post #9 — **liz** | 2021-06-19 17:54 UTC

very interested in this but would only consider participating if it’s an option to protect the predictions file so buyers don’t get them straight up. I understand others prefer to give more allowance with what can be done with their predictions, just my preference.

---

### Post #10 — **restrading** | 2021-06-19 18:12 UTC

[@wigglemuse](</u/wigglemuse>) [@jrai](</u/jrai>) Reputation system is a great suggestion. Do you rather prefer reputation based on models, or customer ratings, or both? As you can see from the static mockup, the model reputation and owner’s stake are shown prominently, hopefully these help buyers to make informed decisions.

On [@wigglemuse](</u/wigglemuse>) concern on gaming the system, I think a submission consistency check may help anwser buyer’s question “how do I know what I get is what I paid for?”, even though the likelihood of sellers purposefully selling wrong predictions is low. Sellers gambling for high risk models is indeed a concern too, hopefully buyers make their decisions based on how much the owner is staking. If a seller happens to gamble for high risk model yet stakes a lot themselves, then at least they burn too when their customers burn. If they claim poverty as a reason for not staking much, I don’t currently have good solutions to this, but perhaps a reputation system may help.

[@liz](</u/liz>) Under current proposal, the seller can choose to either sell raw files (File Mode) or allowance to stake (Stake Mode, where raw files are never sent to the buyers). So for sellers with similar concern like yours you can choose to sell your models via the Stake Mode.

---

### Post #11 — **jrb** | 2021-06-20 12:01 UTC

Great proposal [@restrading](</u/restrading>)! Thanks for the time and attention you’ve invested in think about, drafting and editing it.

I have a couple of follow up questions:

  1. Could you elaborate on the technical aspects of your proposal? 
     * What tech stack?
     * Testing plan.
     * Hosting plan after the initial 3 months. Could it perhaps fund itself with a tiny platform fee?
  2. At first glance, I’m a bit concerned about the fraud protection feature. It deserves a lot of careful thought. From my understanding of what you describe, a buyer could grief the seller by submitting different (possibly better) predictions and then crying wolf.



Finally, I think payments (preferably in NMR) should be a core feature. The project wouldn’t be of much use to the community in practice, otherwise.

---

### Post #12 — **restrading** | 2021-06-20 12:24 UTC _(reply to #11)_

[@jrb](</u/jrb>) Thanks for the tech questions. These are my current thoughts:

  1. Could you elaborate on the technical aspects of your proposal?


  * What tech stack?  
React front-end, flask (centralized) back-end. I’m not trying to make this a dApp from the get-go. Arguably the front-end UX is the main focus. Test deployment will be on GCP. Have not decided on the database. I’m open to recommendations in terms of the tech stack. I’m a fast learner and like to try out new frameworks.
  * Testing plan.  
I will try to make automated unit tests for the back-end API for the key features and integration tests for key use cases. I’ll research more on the best practice. For the front-end I would manually test key use cases. I don’t have a lot of experience with formal tests, any advice regarding testing is appreciated.
  * Hosting plan after the initial 3 months. Could it perhaps fund itself with a tiny platform fee?  
If I manage to implement the payment subsystem then the hosting could be self-sustainable. However currently this is not meant to be production ready but rather a starting point.


  2. At first glance, I’m a bit concerned about the fraud protection feature. It deserves a lot of careful thought. From my understanding of what you describe, a buyer could grief the seller by submitting different (possibly better) predictions and then crying wolf.


  * Under current proposal, in situations where fraud protection applies, the platform automatically submits the file to check for consistency, not the buyers. No buyer action can cause a penalty on the seller and vice versa.

---

### Post #13 — **jrb** | 2021-06-20 13:21 UTC _(reply to #12)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/restrading/48/2928_2.png) restrading:

> Under current proposal, in situations where fraud protection applies, the platform automatically submits the file to check for consistency, not the buyers. No buyer action can cause a penalty on the seller and vice versa.

Indeed. I should’ve elaborated on the attack vector I had in mind in my earlier post. The specific scenario I had in mind was as follows:

  1. Seller offers predictions on the platform
  2. Buyer buys the predictions
  3. The platform submits the predictions on both the seller and buyer’s numerai accounts via the API.
  4. The buyer later goes on to submit different predictions (manually, or via the API).
  5. The resulting live scores are different and the seller is griefed for no fault.



The seller could also do the same, but I can’t see an incentive in the proposed scheme for the seller to exploit it.

---

### Post #14 — **restrading** | 2021-06-20 13:33 UTC _(reply to #13)_

[@jrb](</u/jrb>) Got it. Numerai’s API provides information on the val stats and datetime of submission, so it should be easy enough to check if buyer subsequently overrode the automatic submission. If overriden, no fraud protection would be in place. Did I miss anything?

---

### Post #15 — **jrb** | 2021-06-20 18:14 UTC _(reply to #14)_

Val stats can be doctored, but the timestamp of the submission should work. Although, there might be a timing attack, lurking.

---

### Post #16 — **wigglemuse** | 2021-06-20 21:54 UTC

General idea for submissions: have Numerai compute a checksum value for each submission that could be checked by anyone via API so the entire submission could be validated as same or not same as something else. (This would be useful in scenarios outside of this proposal but also for this.) Applying it to ONLY the live era might be useful also.

---

### Post #17 — **mic** | 2021-06-20 23:14 UTC

The concept of selling predictions is interesting.

What are the benefits of selling predictions? How will it affect participants that don’t sell? How will it help the metamodel?

Does it re-enable the possibility of scoreboard attacks?

I assume the scoreboard is the place prospective buyers are to look for information. Unlike in earlier iterations, currently the scoreboard is unimportant. With selling, will there be incentive to game the scoreboard in order to profit from selling predictions?

A problem is the buyer is basing their decision on past performance. The seller knows how the model works but has not the confidence to risk further staking themselves.

---

### Post #18 — **wigglemuse** | 2021-06-21 01:02 UTC _(reply to #17)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/mic/48/2949_2.png) mic:

> …but has not the confidence to risk further staking themselves.

Or maybe just not the funds. I’d stake a lot more on my models if I had a lot more to stake – I just don’t.

---

### Post #19 — **restrading** | 2021-06-21 01:26 UTC _(reply to #15)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/jrb/48/2767_2.png) jrb:

> Although, there might be a timing attack, lurking.

[@jrb](</u/jrb>) Timing attack is possible from the moment the platform starts submitting a particular file till the moment it checks for submission status, which would be less than a minute. Since it seems Numerai API also provides filename, a random string can be added to the filename by the platform. I think this would patch things up nicely?

![](http://forum.numer.ai/user_avatar/forum.numer.ai/wigglemuse/48/3094_2.png) wigglemuse:

> Numerai compute a checksum value for each submission that could be checked by anyone via API

[@wigglemuse](</u/wigglemuse>) Checksum computed by Numerai may not be sufficient to mitigate this edge case of timing attack, unless the platform itself can also produce the checksum with the same method as Numerai.

![](http://forum.numer.ai/user_avatar/forum.numer.ai/mic/48/2949_2.png) mic:

> Does it re-enable the possibility of scoreboard attacks?

[@mic](</u/mic>) I don’t think this is comparable to a leaderboard attack as there is no guarantee of payout simply due to high position on the leaderboard, nor is the payment coming from Numerai. This is a free market solution. There will be people who gamble with high risk models, but if they are not staking much themselves the buyers are going to see that. Reasonable buyers are going to take owner’s stake amount into account. If they do stake a lot themselves, then there is no issue because they are confident in their models.

---

### Post #20 — **wigglemuse** | 2021-06-21 01:40 UTC

![](http://forum.numer.ai/user_avatar/forum.numer.ai/restrading/48/2928_2.png) restrading:

> Checksum computed by Numerai may not be sufficient to mitigate this edge case of timing attack, unless the platform itself can also produce the checksum with the same method as Numerai.

Well, that would be fine. Or just have Numerai keep a history of submissions (timestamp & checksum) viewable by API so it can be seen when submissions are replaced.

---

### Post #21 — **restrading** | 2021-06-21 01:48 UTC _(reply to #20)_

[@wigglemuse](</u/wigglemuse>) Actually you are right, it’s sufficient. The platform can compare the checksum of the buyer submission to the seller submission.

---

### Post #22 — **jeremy_berros** | 2021-06-21 16:50 UTC

![](http://forum.numer.ai/user_avatar/forum.numer.ai/mic/48/2949_2.png) mic:

> Does it re-enable the possibility of scoreboard attacks?

What kind of leaderboard attacks are you specifically talking about?

---

### Post #23 — **mic** | 2021-06-25 02:04 UTC _(reply to #22)_

![](http://forum.numer.ai/user_avatar/forum.numer.ai/jeremy_berros/48/3025_2.png) jeremy_berros:

> What kind of leaderboard attacks are you specifically talking about?

The incentive would be to get a model to reach high on the leaderboard so it appears attractive to buyers and can be sold. The attack would be to create many otherwise useless models that overfit in different ways.

The “skin in the game” shifts from the creator to a buyer. The creator makes profits without taking risk. The buyer puts the skin in the game but stakes without important knowledge.

If buying/selling models became popular, then Numerai would be relying on evaluation skills of buyers, rather than the confidence of creators in their models.

---

### Post #24 — **restrading** | 2021-06-25 02:17 UTC _(reply to #23)_

Reasonable buyers would take into account owner’s stake when forming the buying decision. If the owner is well-staked then this would not be an issue. If owner of such models do not stake much, few would be willing to buy it given other options.

---

### Post #25 — **mic** | 2021-06-25 05:55 UTC

Yes, I agree that would be a good indication.

---

### Post #26 — **nrichers** | 2021-07-03 20:09 UTC

If CoE can’t fund you for any reason, you can ask for donations… Indicate an address and a progress bar and I’ll be happy to collaborate

---

### Post #27 — **aventurine** | 2021-07-10 21:31 UTC

Possibly another way to make things a bit simpler is using something like Gumroad for individual listings. This way each individual could create what they want. Then all that would really need to happen is have some sort of webpage parser to get the pricing data from each persons gumroad account and display the data on a centralized website. This could also safeguard against fraud and security concerns around APIs etc because everything would be conducted on other peoples individual listings through gumroad and the transactions would be person to person. Could also save a lot of time in the development of a site from scratch. Sort of the inspiration behind this was a twitter post by Jordi with a link to his gumroad site where he just started listing his weekly prediction files on a tiered structure on a monthly or quarterly subscription based plan. See link <https://jrdi.gumroad.com/>. Im sort of thinking things might get so complicated with how each person wants to sell(scrips/raw predictions/tiered pricing based on stake size/lockup periods/etc) that this thing will never really kick off or take a very long time for development. Just a suggestion

---

### Post #28 — **aventurine** | 2021-07-10 21:47 UTC

I am sort of envisioning a central website that will have a cool home page. Tabs could include links to leader board, rocketchat, forums, numerai docs and a tab for account creation with submission instructions. The marketplace tab could be filled with everyone’s individual gumroad listings with pricing and subscription structures. We could also use the Numerapi to get other data from accounts/models to sort of “show off” like previous payouts, reputations/ranking, 3 mo returns on models being sold, current amount staked on models, performance charts and model stake value charts etc. Gumroad upon subscribing allows the owners to send posts to the individuals/newsletters with attachments such as scrips or CSV submission files.

---

### Post #29 — **restrading** | 2021-07-11 05:46 UTC _(reply to #27)_

[@aventurine](</u/aventurine>) Great suggestions, I think Gumroad can be used for listings that do not require platform verification or automated submissions, or for people who prefer to transact in fiat. I will see if any organic integration would be possible.

---

### Post #30 — **hb_scout** | 2021-07-12 14:12 UTC

[@restrading](</u/restrading>) So we discussed this a bit on the Office Hours live last week and seemed like we have consensus to get going on this! Is 69.420 NMR the amount that would be requested upfront? Is there a smaller chunk you’d like to begin with that has a smaller scope of work and lower cost? We talked about some kind of conversion into an hourly rate, but we also want a cap and a manageable short-term scope to get started. Ideas for what piece to do first?

---

### Post #31 — **restrading** | 2021-07-12 14:16 UTC _(reply to #30)_

Hi [@hb_scout](</u/hb_scout>) I am currently drafting the updated features list, work plan as well as funding mode, please allow me 1 or 2 more hours. Thanks.

---

### Post #32 — **restrading** | 2021-07-12 16:10 UTC _(reply to #30)_

Hi [@hb_scout](</u/hb_scout>) and everyone interested in this project. Below is the updated work plan and funding request. If you have any feature request, or want to see some features prioritized over others or anything else, feel free to comment below. Thanks all!

I have already done some prelimiary work on tech stack evaluation and decided to go with FastAPI-VueJS instead of Flask-React. I will be able to commit to this project full-time from Jul 15 for at least a month.

I will keep the table up-to-date as the project goes along. Recorded hours will always be less than actual time spent as I will exclude any unproductive time spent.

Module | Feature/Task | isOpen | Est. Hrs. | Recorded Hrs. | Completion  
---|---|---|---|---|---  
Project | Tech stack evaluation | - | 2 | 2 | Y  
| Project scaffolding and local dev env setup | - | 2 | 2 | Y  
| Local rapid frontend prototyping and designs | - | 12 | 15 | Y  
Backend-Seller | Data schema, model, profile and authentication API | - | 3 | 2 |   
| **Authentication with Metamask Integration** |  | 4 | 4 | Y  
| Seller onboarding and model ownership verification API | - | **8** |  |   
| API tests | - | 2 |  |   
Frontend-Seller | User Middleware | - | **5** | 3.5 |   
| **Authentication with Metamask Integration** |  | 11 | 11 | Y  
| Seller profile UI | - | 2 | 2.5 | Y  
| Seller listing / model verification UI | - | **5** |  |   
Backend-Listing | Data schema and model | - | **4** |  |   
| Listing details and Numerai integration | - | 4 |  |   
| API tests | - | 3 |  |   
Frontend-Listing | Product Middleware | - | **6** |  |   
| Listing Catalog UI | - | 4 | 1 |   
| Listing details UI | - | **8** | 6 |   
| Listing creation UI (Gumroad off platform) | - | 5 |  |   
OffPlatform | Gumroad integration | - | 8 |  |   
Backend-Buyer | Data schema, model, profile and authentication API | - | 2 | 1 |   
| API tests | - | 2 |  |   
Frontend-Buyer | Purchase Middleware | - | 4 |  |   
| Buyer profile UI | - | 1 |  |   
| Buyer purchases UI | - | 2 |  |   
Payment-Crypto | Support for NMR payment | **[Tentative]** |  |  |   
Backend-Submission | Seller submission API | - | 3 |  |   
| Submission file storage, access control and retention policy | - | 4 |  |   
| Submission file encryption and security | [Open] |  |  |   
| Email and other forms of notications to both parties | [Open] |  |  |   
| Live score monitoring and model consistency check | - | 4 |  |   
CI/CD | Docker Compose Setup | - | 2 |  |   
| Set up GitHub CI | - | 1 | 1 | TBC  
| CD setup for GCP | - | 4 |  |   
| Cloud deployment of Minimum Viable Product | - | 2 |  |   
| Write development guide | - | 2 |  |   
| [Code handover, transfer to CoE GitHub] |  |  |  |   
| [Start Accepting GitHub Contributions from This Point On] |  |  |  |   
Backend-OnPlatform | Auction and order book API | [Tentative] | 8 |  |   
| Stripe Connect | **[Open]** |  |  |   
| Data schema and model | [Tentative] | 1 |  |   
| Transaction API | [Tentative] | 3 |  |   
| Numerai account and stake monitoring | [Tentative] | 2 |  |   
| API tests | [Tentative] | 5 |  |   
Frontend-OnPlatform | Auction UI | [Tentative] | 4 |  |   
| Purchase UI with dummy payment processing | [Tentative] |  |  |   
| Automated job queue for submissions and delivery | [Tentative] | 8 |  |   
Payment-Crypto | NMR collateral for buyers and sellers for stake-mode sales | [Open] |  |  |   
| Erasure support for buyer stake enforcement | [Open] |  |  |   
| Erasure support for seller model verification enforcement | [Open] |  |  |   
Other | Support sales for Signals data | [Open] |  |  |   
| Support sales for Signals files | [Open] |  |  |   
| Support sales for model files / scripts / notebooks | [Open] |  |  |   
| Reputation system | [Open] |  |  |   
| Subscription Sales | [Open] |  |  |   
| UI Enhancements (Search, filter, etc.) | [Open] |  |  |   
| **Voting App with Account Requirements** | **[Open]** |  |  |   
  
**Total Estimated Hours: 162**  
**Recorded Hours Balance: 29 [For CoE: Recorded hours balance: 29 (1015 USD ~= 30 NMR at the time of writing) + 202.69 USD for domain name ~=6 NMR == > 36 NMR in total]**  
**Cumulative Recorded Hours: 51**

Funding Rate: $35 / hr (approx. market rate for junior dev)

Funding Mode: No upfront payment needed, funding to be paid at the end of the project / weekly based on recorded hours in NMR using point-in-time NMR/USD conversion rate. For fairness the CoE can apply discretion at the end to make adjustments to the funding based on assessment of work quality.

Dev Cost: I will bear any infrastructure cost during dev and the initial 3 months of deployment. Going further I might fund the hosting through community donation, small platform fee (after crypto payment is implemented) or via separate proposals for hosting cost.

**UPDATES:**

* * *

**2021-07-15 — 2021-07-17:**  
Sneak Peek:  


[![Marketplace 20210717](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/c/cacf49accf7db86fa063cf35798b1fe0cd560aba_2_690x359.png)Marketplace 202107172552×1330 234 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/c/cacf49accf7db86fa063cf35798b1fe0cd560aba.png> "Marketplace 20210717")

  * Completed framework setup and base e-commerce frontend boilerplating.
  * Updated workplans, prioritized off-platform (Gumroad) integration and CI/CD, which would allow earlier release of code, more collaborations and earlier deployment of minimum viable product.
  * Revised some estimated hours based on recent work. Changes/additions to the workplans are in bold.



**2021-07-18 — 2021-07-25:**  
Sneak Peek:  


[![NumerBay 20210725 web3](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/b/b2645a2ff942a271681fd73cd05dcffee45d7549_2_690x473.png)NumerBay 20210725 web31882×1292 175 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/b/b2645a2ff942a271681fd73cd05dcffee45d7549.png> "NumerBay 20210725 web3")

  


[![NumerBay 20210725 product details](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/2/2320ee097f8cda4ddf8be7f5aaaa4433a53cb7c2_2_690x462.png)NumerBay 20210725 product details2366×1586 209 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/2/2320ee097f8cda4ddf8be7f5aaaa4433a53cb7c2.png> "NumerBay 20210725 product details")

  * User will be able to login through Metamask (and potentially other providers) by signing a backend generated nonce, paving the way for crypto payment functionality
  * Completed generic user module (both frontend and backend), product listing UI is in-progress
  * Updated workplans and time estimates. Changes are in bold. Deprioritized buyer specific stuff as they are not yet necessary for 3rd party platform listings.
  * Next week to focus on seller onboarding and product related UI, middleware and backend.

---

### Post #33 — **jackerparker** | 2021-07-15 08:08 UTC

An important question which seems to be missing in the marketplace development is Terms of use for products. Is there any plans about it? May be we can create this document together and place it under open-source license somewhere. Otherwise, every seller have to spend some time and money on developing of this document, because it is illegal to use someone elses Terms of use with no permission. I have some draft developed by me which I can share, but I’m not a lawyer and have no experience in that kind of things. May be it would be better if CoE will sponsor professional lawyer for developing of that doc.

---

### Post #34 — **restrading** | 2021-07-15 08:43 UTC _(reply to #33)_

Right now I’m focusing on building something that works first. The early product will host 3rd party listings such as Gumroad. We can figure out the legal terms along the way as the product matures. I’m open to suggestions.

---

### Post #35 — **objectscience** | 2021-07-16 15:18 UTC

I’m late to the party but wanted to chime it. I love this idea. I may have missed it, but I didn’t see anything that addressed long-term support and maintenance. Would it make sense once the product is funded and built out to shift financial upkeep off of the COE and push it towards a self-sustaining usage fee? If I were selling models on the marketplace, I’d have zero reservation about losing a few percentage points of the purchase price, back to the marketplace. Put differently, I have no issue with [@restrading](</u/restrading>) making money off of this. A lot of money if it works well.

I’d also like to see the purchase price tied back to the seller’s skin in the game on a model via some multiplier cap: i.e. you can’t sell a model for 100 NMR if you only had 1 NMR staked on it for 20 weeks. If you had 25 NMR staked on it for six months and want to sell it for 100, maybe… If that makes sense. I think SITG is still important here.

Great idea, looking forward to seeing it mature.

---

### Post #36 — **restrading** | 2021-07-16 15:34 UTC _(reply to #35)_

Thanks for the support. Yes as said above I can think of 3 ways going forward, with the small platform fee being the most self-sustaining method. Such fees can be used to cover hosting costs as well as to fund future devs so as to reduce financial burdens on the CoE.

I like the idea of stake-tied-pricing limits, and will explore how it would make sense. ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=9)

---

### Post #37 — **jrai** | 2021-07-19 15:53 UTC _(reply to #36)_

First 26 NMR funding tranche sent from CoE multisig  
<https://etherscan.io/tx/0xcbe1402e10779a90a4461643764e5112a95a0f2db16b1c597ccd01d0bf968976>

---

### Post #38 — **restrading** | 2021-07-19 15:54 UTC _(reply to #37)_

Thanks [@jrai](</u/jrai>) and CoE for the fast turnaround and support, NMRs received! I will make the next update in a week.

---

### Post #41 — **restrading** | 2021-08-04 01:54 UTC _(reply to #40)_

This thread was archived, for new updates please see: [[Updates] NumerBay - The Community Marketplace](<http://forum.numer.ai/t/updates-numerbay-the-community-marketplace/3844>)
