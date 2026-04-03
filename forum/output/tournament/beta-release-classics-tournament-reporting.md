---
title: "[Beta Release] : Classics tournament reporting"
category: Tournament
url: https://forum.numer.ai/t/beta-release-classics-tournament-reporting/4008
created_at: 2021-08-29T15:26:47.348000+00:00
last_posted_at: 2021-10-16T18:54:58.118000+00:00
posts_count: 5
views: 1164
tags: []
---

# [Beta Release] : Classics tournament reporting

---

### Post #1 — **qeintelligence** | 2021-08-29 15:26 UTC

Hi all,

As part of learning new tools / technologies and also to gain more insight into the classic tournament I have recently been busy with setting up a reporting solution.

There is of course already the numerai website which contains great information for your models and also the leaderboard for example and is basically the default to go to for live insights (next to the other dashboards mentioned on the site). In addition of course the excellent app from [@ceunen](</u/ceunen>) for live payouts.

I was still missing other information though which is more useful for long-term analysis and could not find a complete report out on the web. Also I was anxious to learn more about certain tools like Power BI and decided that it was time create a new report with all the information that is available on <https://api-tournament.numer.ai/>. Also I learned a lot from the community, twitch, forum, rocket chat and decided it was time to give something back to the community ![:slight_smile:](https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=13)

Today the beta version (0.2.0) is released of the Numerai statistics report and can be found over here:

[Numerai Statistics Retrieval and Report](<https://github.com/jos1977/numerai_statistics>)

Like I said its still beta and 80% finished I guess but someone ([@arbitrage](</u/arbitrage>)) told me I should release it soon and get some feedback from the community. I hope you will check it out and do please tell me what you think!

The report is based on PowerBI Desktop which is a free to use tool that can be installed by everyone with a Windows / Mac. All the instructions can be find on the repo readme on how to install and start using the report.

Alternatively you can also get just the pdf exports which are also on the repo, but then you will miss a lot of functionality that its in the report!. The report has the following:

  * General dashboard with quick round status: stakes, payouts, correlation
  * Top 10 page: medals scores, most earned
  * Leaderboard statistics
  * Option to select your models for detailed analysis
  * Option to use slicers on many pages for: dates, rounds, models, stakes
  * Rankings of your models
  * Round performances
  * Payouts for your models and for the whole tournament
  * Price data extraction from Coinbase



The data that is used in the reports are parquet files which are updated on a weekly basis (sunday) and can be used for refreshing the report. The parquet files are also in the repo. In the following weeks I will also put the C# project in the repo which is responsible for retrieving the statistics, but this needs to be a little bit cleaned up first ![:slight_smile:](https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=13)

Over here are some quick screenshots, please do use the tool and give me feedback.

[![pbi_general](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/c/c09c4b843193f8c0b3af2d61048abcca6ae45024_2_690x337.png)pbi_general1092×534 162 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/c/c09c4b843193f8c0b3af2d61048abcca6ae45024.png> "pbi_general")

  


[![pbi_roundstatus](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/b/beacf59e97e05fb39efbf9caa621a23e18df8e16_2_628x500.png)pbi_roundstatus1080×859 131 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/b/beacf59e97e05fb39efbf9caa621a23e18df8e16.png> "pbi_roundstatus")

  


[![pbi_roundperformance](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/e/eec249b695d2d9ed84990147f39989f75e3006b3_2_613x500.jpeg)pbi_roundperformance1063×867 195 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/e/eec249b695d2d9ed84990147f39989f75e3006b3.jpeg> "pbi_roundperformance")

  


[![pbi_ranking](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/5/53c79410b494d8458aaa6362e9647e66746f2c0e_2_601x499.png)pbi_ranking1041×866 172 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/5/53c79410b494d8458aaa6362e9647e66746f2c0e.png> "pbi_ranking")

  


[![pbi_payoutperformance](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/b/b274992fffac26061113eef25a86e09f9857664c_2_624x499.png)pbi_payoutperformance1081×866 175 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/b/b274992fffac26061113eef25a86e09f9857664c.png> "pbi_payoutperformance")

---

### Post #2 — **qeintelligence** | 2021-08-31 20:34 UTC

I also put the reporting dashboard on PowerBI Service, today hone5com made it part of the Numerbay website! ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=9) thanks! <https://numerbay.ai/>

---

### Post #3 — **restrading** | 2021-09-01 01:14 UTC

Amazing work! Sorry I jumped the gun on publishing it. Glad you liked it.

---

### Post #4 — **qeintelligence** | 2021-09-06 20:46 UTC

Hi All, a quick update from me on the tournament reporting/dashboard. I now also added the visual studio solution and Python support files to the git repository. These are examples on how to retrieve the statistics from the graphql endpoint of numerai (and convert to parquet, push to git).

I didn’t do any update on the dashboard itself at the moment, but will start working on that again. I noticed that currently on Numerbay default page 3 is shown of the dashboard upon opening the website, which should actually default to page 1 (easy fix). In addition I will have a look at the following:

  * Add dates to visuals where roundnumber is used on X-axis
  * Visual to compare selected/all models against example_model (corr/mmc/fnc diff, performance diff)
  * Visual with ‘custom metamodels’ performance: metamodel existing of top users (e.g. top 100 users, most staked users, etc…)
  * Option to filter ranking increase statistics based on 20 rounds submissions
  * Visual cleanup of PowerBI report, simplify pages
  * Investigate option cloud-based instance (daily retrieval)



![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=9) This is going to take some time ofcourse, since its a personal project at the moment and I also want to spend (lots of) time on the upcoming data release!

---

### Post #6 — **qeintelligence** | 2021-10-16 18:54 UTC

Hi all, another quick update on the (classic) tournament reporting/dashboard. I didn’t do much lately, and was more occupied with work/study and ofcourse the new dataset. A minor beta release has been put online and is already available and part of the Numerbay website ![:smiley:](https://emoji.discourse-cdn.com/twitter/smiley.png?v=13)

Besides minor fixes/improvements here and there, there is also a new page available: ‘Performance Scenarios’. The purpose of this page is quite easy, it gives you insights in your models performances when chosing for correlation only or with the various mmc multipliers. Ofcourse when TC is going to be introduced I will have to update this one again, but we will have to wait on that one.

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/3/3de55f6d2c5ad0d8adf2b499f1bd801091fc83ef_2_690x377.png)image1523×834 109 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/3/3de55f6d2c5ad0d8adf2b499f1bd801091fc83ef.png> "image")

Have fun!
