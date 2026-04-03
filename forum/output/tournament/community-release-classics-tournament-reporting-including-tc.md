---
title: "[Community Release] : Classics tournament reporting including TC"
category: Tournament
url: https://forum.numer.ai/t/community-release-classics-tournament-reporting-including-tc/5270
created_at: 2022-04-15T19:39:22.687000+00:00
last_posted_at: 2022-06-22T21:24:19.371000+00:00
posts_count: 5
views: 1095
tags: []
---

# [Community Release] : Classics tournament reporting including TC

---

### Post #1 — **qeintelligence** | 2022-04-15 19:39 UTC

Hi guys, as you may remember about 6 months ago I was working on a classics tournament dashboard, details about that one you can find back in the famous [@arbitrage](</u/arbitrage>) Office Hours ![:slight_smile:](https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=13) [https://www.youtube.com/watch?v=rwudtxQiAFU&t=451s](<https://www.youtube.com/watch?v=rwudtxQiAFU&t=451s>)

And also in the original forum post over here:

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/numerai.discourse.group/qeintelligence/48/2531_2.png) [[Beta Release] : Classics tournament reporting](<http://forum.numer.ai/t/beta-release-classics-tournament-reporting/4008>) [Tournament](</c/tournament/7>)

> Hi all, As part of learning new tools / technologies and also to gain more insight into the classic tournament I have recently been busy with setting up a reporting solution. There is of course already the numerai website which contains great information for your models and also the leaderboard for example and is basically the default to go to for live insights (next to the other dashboards mentioned on the site). In addition of course the excellent app from [@ceunen](</u/ceunen>) for live payouts. I was st… 

Since that time not many changes were done on the dashboard (partly due to me and a superbusy social/work life lol). I did notice no TC ranking history is available yet at the numerai site or on other dashboards afaik and I did have some hours left. I updated the dashboard, page(s) ‘Ranking’ ,‘Round Performance’ and ‘Payout’ are probably the most interesting ones when related to the new TC/FncV3 stuff.

For basic instructions check out the youtube video, the link to the powerbi dashboard is:

![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/7/70c8161e39f4f6e9b385241d1b8f40484a9ee9fe.png) [app.powerbi.com](<https://app.powerbi.com/view?r=eyJrIjoiNTA4N2RlNjYtZTI5YS00ZmUxLTk0NWItMWM1MzgxNmZkZGRiIiwidCI6Ijg3ZDc2ZDQ2LWYxZmYtNDkzMi05MGNiLTUyNzY3Yzg2OTk2ZiIsImMiOjl9>) ![](https://app.powerbi.com/https://content.powerapps.com/resource/powerbiwfe/images/PowerBI125x125.6906aa6687c696ce3dcb.png)

### [Power BI Report](<https://app.powerbi.com/view?r=eyJrIjoiNTA4N2RlNjYtZTI5YS00ZmUxLTk0NWItMWM1MzgxNmZkZGRiIiwidCI6Ijg3ZDc2ZDQ2LWYxZmYtNDkzMi05MGNiLTUyNzY3Yzg2OTk2ZiIsImMiOjl9>)

Report powered by Power BI

I will see if I can host the report from a proper https link, but for that I need to setup some hardware stuff first.

The github repo containing the pbi report and source code is still the same:

[github.com](<https://github.com/jos1977/numerai_statistics>)

![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/e/e53525a2973edb8a1f9b4245c17ac01e4f35045d_2_690x344.png)

### [GitHub - jos1977/numerai_statistics: Numerai Statistics (Retrieval and Power BI)](<https://github.com/jos1977/numerai_statistics>)

Numerai Statistics (Retrieval and Power BI)

Its not perfect yet, and also I will see if I can fix the minor issues left in the report and also include more interesting stuff, but its a start ![:smiley:](https://emoji.discourse-cdn.com/twitter/smiley.png?v=13)

---

### Post #2 — **aventurine** | 2022-04-15 22:59 UTC

Nice work! How many hours did you work on this dashboard total you think including the recent updates? Let us know if you want a retro bounty. I dont know if we ever asked the first time or if you had said no. I dont see chatter from the first post. Maybe this was done right before we started doing the bounty thing

---

### Post #3 — **qeintelligence** | 2022-04-17 18:45 UTC

I think maybe in total including the api-code (C#) and powerbi reporting I spend a total of 4 days I guess (including the several hours from the latest change). Don’t worry about the retro bounty though, this one I still do for free (and for fun and educational purposes). Actually we did have the same conversation I remember (at that time the retro bounty stuff was still being setup), ![:wink:](http://forum.numer.ai/images/emoji/twitter/wink.png?v=10) still don’t want to get paid for this community stuff though, especially since it sort of gives me the idea that from now on I need to deliver high-quality stuff and on time, lol for now I will do it on a best-effort basis. But thank you for the offer ofcourse!

---

### Post #4 — **qeintelligence** | 2022-05-28 19:15 UTC

Hi all, yesterday and today I did a little update together with [@restrading](</u/restrading>) on the classic tournament reporting tool, it now contains a new page with the NumerBay Sales statistics for classic tournament! Basically, this page is meant for anyone who wants to buy predictions or models for the classic tournament and wants to have an overview of the current available models and the relevant statistics (like tc ranking, 3-months return, etc).

You can find the new report if you go to the [NumerBay website](<https://numerbay.ai/>) and select Community Apps->Power BI Numerai Dashboard. Next go to the page ‘Numerbay’ to find the stats.

If there are any stats that you think could be relevant and is not there yet let me know and we will see if it is possible to add them in the future. Have fun and see you in London!

[![numerbay](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/1/12b3068733a6cf98ba49142a83008665960b4e91_2_690x308.png)numerbay1858×832 134 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/1/12b3068733a6cf98ba49142a83008665960b4e91.png> "numerbay")

---

### Post #5 — **qeintelligence** | 2022-06-22 21:24 UTC

Hi all, I noticed several people talking in the chat about stability of the models, mean average, std. Also I remembered the performance scenarios in the reporting tool was still based on corr and mmc. There is a new report out since today, v1.2.0. In this version you have the following (new) pages:

  * Performance scenarios: in this page you can check what you performance would have been based on the 8 different corr/tc combinations currently possible. Just select a model and compare, I am noticing at the moment I should do 3xtc+1xcorr for most of my new models lol
  * Model stability: on this page you can see std and (mean) average of your selected model for the time windows of 10 rounds or 20 rounds. I think shorter would be not meaningfull and for a longer period of time you could check on the numerai site anyway for mean average.



The link to the new report is over here:

[Numerai Classics report](<https://app.powerbi.com/view?r=eyJrIjoiYTI4N2FkY2YtYTliYy00ZjQ5LWE2NjMtMTBjOTkwYTg2NDE2IiwidCI6Ijg3ZDc2ZDQ2LWYxZmYtNDkzMi05MGNiLTUyNzY3Yzg2OTk2ZiIsImMiOjl9>)

You can also find it through the numerbay website, I think the new report link will be also updated there soon. Have fun and hope the updates are useful!
