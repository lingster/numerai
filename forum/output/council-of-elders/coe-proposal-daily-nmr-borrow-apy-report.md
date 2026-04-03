---
title: "COE Proposal: Daily NMR Borrow APY Report"
category: Council of Elders
url: https://forum.numer.ai/t/coe-proposal-daily-nmr-borrow-apy-report/5409
created_at: 2022-05-17T15:10:31.685000+00:00
last_posted_at: 2022-06-06T05:07:15.559000+00:00
posts_count: 16
views: 1117
tags: []
---

# COE Proposal: Daily NMR Borrow APY Report

---

### Post #1 — **dev0n** | 2022-05-17 15:10 UTC

Proposal Summary: Create a bot that regularly reports on the NMR/USDC borrow rate to the [#numeraire](</c/numeraire/9>) channel, so that community participants can decide when the borrow rate is higher than their expected return for directly staking and adjust their allocation accordingly.

Background: I think a more stable borrow rate on the NMR/USDC pair would encourage larger inflows of staking (and therefore NMR demand) because the risk-adjusted returns would be higher using borrowed NMR (because currency price risk is removed). I posted a [related proposal encouraging COE to try to make the borrow APY more stable](<http://forum.numer.ai/t/coe-proposal-coe-monetary-policy/5405>). This proposal is a complementary mechanism where the community can have more visibility the borrow APY to help decide between lending and staking their NMR.

V1 Proposal detail:

  * Build a bot that scrapes the Sushi graph: <https://thegraph.com/hosted-service/subgraph/sushiswap/bentobox?query=Example%20query>
  * Have a daily message sent to the [#numeraire](</c/numeraire/9>) Rocket chat channel reporting on key stats, including percent borrowed and borrow and supply APY



V2 ideas:

  * Find other places to surface this report
  * Create alerts for large swings in any key metric



(Note this is a proposal of requirements, I’m not proposing that I would build this. So it’s also a bit of an RFP for interested developers as well - assuming COE would be interested in funding the development of this.)

---

### Post #2 — **uuazed** | 2022-05-17 15:23 UTC

1. I’d hope there is some API or at least some existing crawler. A quick searched revealed this one: [GitHub - keyko-io/defi-crawler-py: Python library helping to fetch DeFi protocols data](<https://github.com/keyko-io/defi-crawler-py>)
  2. could be a twitter bot



Overall I like the idea. Should be straight-forward to build.

---

### Post #3 — **dev0n** | 2022-05-17 16:50 UTC _(reply to #2)_

1. Nice find!
  2. Agree Twitter is another good channel for this report/alert

---

### Post #4 — **dev0n** | 2022-05-21 20:44 UTC

I did some poking at that library, unfortunately I didn’t see a way to get borrowAPR.

I don’t have much GraphQL experience but I was able to get this query working:
    
    
    {
      kashiPair(id: "0x7bee2161afa1aee4466e77bed826a41d5a28db46") {
      id, exchangeRate, totalAssetBase, totalBorrowBase, totalAssetElastic, totalBorrowElastic, totalCollateralShare supplyAPR, borrowAPR, utilization, type, symbol, asset {
        id, name, symbol
      }, collateral {
        id, name, symbol
      },
    	}
    }
    
    

Which returns
    
    
    {
      "data": {
        "kashiPair": {
          "id": "0x7bee2161afa1aee4466e77bed826a41d5a28db46",
          "exchangeRate": "13263458",
          "totalAssetBase": "6002943442680362042872",
          "totalBorrowBase": "958375394457672395803",
          "totalAssetElastic": "5370781687642382921729",
          "totalBorrowElastic": "1136475446802526877451",
          "totalCollateralShare": "64711938848",
          "supplyAPR": "1241007948896566",
          "borrowAPR": "7879828695436800",
          "utilization": "174990824584131262",
          "type": "medium",
          "symbol": "kmUSDC/NMR-LINK",
          "asset": {
            "id": "0x1776e1f26f98b1a5df9cd347953a26dd3cb46671",
            "name": "Numeraire",
            "symbol": "NMR"
          },
          "collateral": {
            "id": "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
            "name": "USD Coin",
            "symbol": "USDC"
          }
        }
      }
    }
    

(Note it returns APYs bigints that need to be divided by 1000000000000000…I think)

---

### Post #5 — **dev0n** | 2022-05-21 21:10 UTC

OK using this [tutorial](<https://cryptomarketpool.com/use-the-graph-to-query-ethereum-data-in-python/>) I’ve got a simple python script going:
    
    
    import requests
    from pprint import pprint
    
    def run_query(q):
        request = requests.post('https://api.thegraph.com/subgraphs/name/sushiswap/bentobox'
                                '',
                                json={'query': query})
        if request.status_code == 200:
            return request.json()
        else:
            raise Exception('Query failed. return code is {}.      {}'.format(request.status_code, query))
    
    
    query = """
    {
      kashiPair(id: "0x7bee2161afa1aee4466e77bed826a41d5a28db46") {
      id, exchangeRate, totalAssetBase, totalBorrowBase, totalAssetElastic, totalBorrowElastic, totalCollateralShare supplyAPR, borrowAPR, utilization, type, symbol, asset {
        id, name, symbol
      }, collateral {
        id, name, symbol
      },
    	}
    }
    """
    result = run_query(query)["data"]["kashiPair"]
    pprint(result)
    borrowAPR = float(result["borrowAPR"]) / 1000000000000000
    supplyAPR = float(result["supplyAPR"]) / 1000000000000000
    print(f"borrowAPR: {borrowAPR}%")
    print(f"supplyAPR: {supplyAPR}%")
    

Returns
    
    
    {'asset': {'id': '0x1776e1f26f98b1a5df9cd347953a26dd3cb46671',
               'name': 'Numeraire',
               'symbol': 'NMR'},
     'borrowAPR': '7879828695436800',
     'collateral': {'id': '0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48',
                    'name': 'USD Coin',
                    'symbol': 'USDC'},
     'exchangeRate': '13263458',
     'id': '0x7bee2161afa1aee4466e77bed826a41d5a28db46',
     'supplyAPR': '1241007948896566',
     'symbol': 'kmUSDC/NMR-LINK',
     'totalAssetBase': '6002943442680362042872',
     'totalAssetElastic': '5370781687642382921729',
     'totalBorrowBase': '958375394457672395803',
     'totalBorrowElastic': '1136475446802526877451',
     'totalCollateralShare': '64711938848',
     'type': 'medium',
     'utilization': '174990824584131262'}
    borrowAPR: 7.8798286954368%
    supplyAPR: 1.241007948896566%

---

### Post #6 — **dev0n** | 2022-06-01 04:01 UTC

I tried [dune.com](<http://dune.com>) for the first time and made this dashboard - would appreciate some peer review: [Dune](<https://dune.com/dev0n/nmr>)

I can’t get the rates to match what I see on [sushi.com](<http://sushi.com>), but the utilization and rate drop after the recent May 17 NMR deposit from CoE seems to line up…

---

### Post #7 — **jorijnsmit** | 2022-06-03 12:47 UTC _(reply to #6)_

i believe you still have to convert the logged `rate` from seconds to apr. see line 936 here: [DethCode](<https://etherscan.deth.net/address/0x7bee2161afa1aee4466e77bed826a41d5a28db46#code>)

latest `rate` logged by nmr/weth is `79274480`, which matches with `MINIMUM_INTEREST_PER_SECOND` (line 849). then `79274480/365/24/60/60~=2.5` (apr in bps, which roughly matches what ui is showing atm).

not sure if tracking these events is the way to go though, since they are only emitted on certain interactions with the contract (`removeCollateral`, `addAsset`, `removeAsset`, `borrow`, `repay`, `liquidate` and `withdrawFees`). at no point is interest accrued ‘automatically’, meaning the last log might be quite old and deviating from the current situation.

ideally you would want to call `accrue` yourself offchain at regular intervals, and save that data.

here is a start, a script that just prints the current state to stdout: [GitHub - gosuto-ai/numerai-kashi-logger](<https://github.com/gosuto-ai/numerai-kashi-logger>)

---

### Post #8 — **dev0n** | 2022-06-03 23:09 UTC

Very helpful [@jorijnsmit](</u/jorijnsmit>) \- thank you for this. Lots to learn about reading data from smart contracts. I’ve updated the dashboard, but as you say, without polling it will become out of date. I will look into this more, but one quick question:

> you would want to call `accrue` yourself offchain at regular intervals

So this is a call that costs nothing but as a result does not update the data in the blockchain? If so I’m trying to wrap my head around what the call is actually doing / what is doing the computation… is the `brownie` package simulating what the EVM would do? And the [sushi.com](<http://sushi.com>) front end must be doing something similar to get psuedo-live data even when transactions are not happening?

---

### Post #9 — **dev0n** | 2022-06-03 23:53 UTC

Following up, I tried to run your script but it looks like there is some setup required (potentially adding eth account details and maybe even paying gas each time to check the new rate?)

Any pointers on how to get that set up would be appreciated. Thanks again

---

### Post #10 — **jorijnsmit** | 2022-06-04 06:17 UTC _(reply to #8)_

![](https://yyz1.discourse-cdn.com/flex009/user_avatar/forum.numer.ai/dev0n/48/3389_2.png) dev0n:

> So this is a call that costs nothing but as a result does not update the data in the blockchain? If so I’m trying to wrap my head around what the call is actually doing / what is doing the computation… is the `brownie` package simulating what the EVM would do? And the [sushi.com](<http://sushi.com>) front end must be doing something similar to get psuedo-live data even when transactions are not happening?

correct; brownie uses [ganache](<https://trufflesuite.com/ganache/>) to fork the blockchain at its current block. all new transactions are simulated (computated) locally, looking backwards on previous live blocks for storage if needed.

at no point do you actually write to the live blockchain; no keys or gas needed.

im not sure what setup you are talking about. maybe register with infura for a key to paste into `.env`?

---

### Post #11 — **dev0n** | 2022-06-04 17:55 UTC _(reply to #10)_

Thanks - OK I finally hacked it together and got it to run. For anyone else interested (and for my future self):

  1. Get an Infura Project ID and set it as an env var
  2. Install Node
  3. Install Ganache
  4. Install Eth-brownie
  5. Run `brownie run call_accrue`

---

### Post #12 — **aventurine** | 2022-06-05 23:09 UTC _(reply to #11)_

This will be available to see updated on Numerbay [@restrading](</u/restrading>) soon ? [@dev0n](</u/dev0n>)

---

### Post #13 — **dev0n** | 2022-06-06 00:14 UTC _(reply to #12)_

If we want to just start with a dashboard we could put yours up - but we should put a caveat that it often has old data… if we want to do it with the way [@jorijnsmit](</u/jorijnsmit>) showed with live that will be a lot more work I think (will require building a database and running a server to pull and store the data)

I suggest just the dashboard for V1, then for V2, someone building a simple bot that posts daily stats to a rocketchat channel and/or a twitter account

---

### Post #14 — **aventurine** | 2022-06-06 00:48 UTC _(reply to #13)_

Ok sounds good we can wait to see what [@restrading](</u/restrading>) wants to do

---

### Post #15 — **restrading** | 2022-06-06 02:25 UTC _(reply to #14)_

[@aventurine](</u/aventurine>) [@dev0n](</u/dev0n>) In terms of dashboard, the one from [@aventurine](</u/aventurine>) has already been added to the home page. Live feed is possible, if the CoE find it worth the effort I’d be happy to add it to the home page as another section.

---

### Post #16 — **aventurine** | 2022-06-06 05:07 UTC _(reply to #15)_

Oh nice sounds good. I think that should be good enough for now unless we get more of an outpouring of demand for the defi stats to be more in the open. [@dev0n](</u/dev0n>) let me know about how many hours you worked on writing this little dune script that I added to my dashboard and if you would like a bounty. You can DM address on rocketchat but place your hours worked publicly here ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=10)
