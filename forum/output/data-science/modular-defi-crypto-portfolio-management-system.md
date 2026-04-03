---
title: "Modular Defi Crypto Portfolio Management System"
category: Data Science
url: https://forum.numer.ai/t/modular-defi-crypto-portfolio-management-system/7887
created_at: 2024-12-17T15:34:59.619000+00:00
last_posted_at: 2024-12-18T22:23:57.190000+00:00
posts_count: 3
views: 1440
tags: []
---

# Modular Defi Crypto Portfolio Management System

---

### Post #1 — **jefferythewind** | 2024-12-17 15:34 UTC

OK Party People, here it is. An open source, modular system design, to implement decentralized portfolios based on the Numerai crypto meta model, but the generic oracles could really be based on anything.

For all the most up-to-date code and examples, check out the github project: [GitHub - jefferythewind/defi_crypto_pm: Open Source Project for Defi Crypto Portfolio Management](<https://github.com/jefferythewind/defi_crypto_pm>)

[There is also a decent PDF document that explains main concepts and also has example code here.](<https://github.com/jefferythewind/defi_crypto_pm/blob/main/Defi_Crypto_Portofolio_System_v1.pdf>)

This has been a pet project for just a short time, and I realized there is nothing really holding us back at the moment from having completely decentralized portfolios running right on our own laptop. Idealism is working, at the moment. I’ve designed a simple and modular concept that makes the problem as simple as it needs to be. 2.

**Oracles**

The first concept is the oracle. This an object that always knows the optimal portfolio. Of course, in practice, this is up to the person implementing the code, what portfolios are returned from the oracle. The the first example, i’ve implemented a very simple version of the **TB N** portfolio. This portfolio simply returns an equally weighted portfolio with N long and N short positions, based on the largest and smallest ranks given by Numerai’s meta model.

I’ve made the oracle receive a _tradable universe_ argument, which should come from the DEX. The oracle here returns the best portfolio given the intersection of the tradable universe and Numerai’s meta model.

[**We see here that we only require two methods from the oracle**](<https://github.com/jefferythewind/defi_crypto_pm/blob/main/oracle_interfaces.py>):

  1. Fetch Portfolio Weights
  2. Validate Weights



**DEX Interfaces**

Once we know an optimal portfolio, all we need is to set our exposure to match this portfolio in the real market. Our interface with the DEX should be this simple.

[We see here that we only require two methods from the DEX interface](<https://github.com/jefferythewind/defi_crypto_pm/blob/main/dex_interfaces.py>)

  1. Get Universe
  2. Set Portfolio Weights



**Portfolio Manager**

With the generic Oracle and DEX interfaces, a portfolio manager can do its job in straight-forward manner. It will get the portfolio weights from the oracle, given the tradable universe of the dex. It will then check the weights, and assuming they are good, it will send the weights to the DEX interface for setting. The portfolio manager only needs to implement the `manage_portfolio` method.
    
    
    # Portfolio Manager
    class PortfolioManager:
        def __init__(self, oracle: OracleInterface, dex: DEXInterface):
            """Initialize the Portfolio Manager with an Oracle implementation."""
            self.oracle = oracle
            self.dex = dex
    
        def manage_portfolio(self, timestamp = datetime.now(timezone.utc) ):
            """Fetch weights from the Oracle and print them."""
            print(f"[PortfolioManager] Requesting portfolio weights for {timestamp}.")
            tradable_universe = dex.get_universe()
            # tradable_universe = ['BTC','ETH','AAVE','LDO','SUI','WLD','GOAT','EIGEN','AVAX','ENS']
            weights = self.oracle.fetch_portfolio_weights(
                timestamp,
                tradable_universe
            )
    
            if not self.oracle.validate_weights(weights):
                raise ValueError("Invalid portfolio weights received from Oracle.")
    
            print(f"[PortfolioManager] Portfolio weights: {weights}")
    
            dex.set_portfolio_weights( weights )
    

[![Modular Design Schematic](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/f/f2bf03ccab9f743af8ee8a85e78a140092c5cdad_2_690x348.png)Modular Design Schematic1220×616 66.2 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/f/f2bf03ccab9f743af8ee8a85e78a140092c5cdad.png> "Modular Design Schematic")

Given this generic design, making anything happen in the markets requires overriding the generic methods for concrete cases. [I’ve done this in the example notebook.](<https://github.com/jefferythewind/defi_crypto_pm/blob/main/Example%20Code.ipynb>)

**Some Takeaways**

You’ll see in the code that most of the work so far has been implementing the DEX interface with HyperLiquid. It certainly is one of the three main parts here. However the process is straight-forward. As long as you implement the desire methods with the same inputs and outputs, you can make a DEX interface to any DEX.

I learned that Coinbase and Dydx technology for the perpetual futures markets is restricted and not available for people living in North America. Hyperliquid worked for me from my location. (This is not an endorsement of the exchange, I really don’t know much about it yet. And every geographic location has its own laws and restrictions, so please find out based on your situation.) So far, it seems like a quality project. More amazingly is that all you have to do is connect a local wallet, like meta mask or even coinbase wallet, to the hyperliquid exchange. You have to make sure it is funded on the Arbitrum network with USDC and some ETH for gas. And for **test net** , which is what I am currently using for this testing, you can get free mock USDC from their faucet. The whole thing is a cool process, and reminds me the utility that actually exists here in the crypto space. It seems to me that Hyperliquid is trying to make it as easy as it needs to be to get access to their perpetual futures market. The api works well. Hopefully my code will work for you out-of-the-box.

**Next Steps**

Hopefully before long I will make available a simple backtester which should integrate into the framework. The oracles receive a timestamp argument. The idea is that if we supply a historical timestamp, the orcale can give portfolios for those historical days as well. I think in the current version it will do that. Historical data should be available directly from the DEX but also I will check the coverage in yahoo data.

**Disclaimer**

I’m working on this project as a concept to try to encourage the community to realize that it seems all the tools are at our fingertips already to trade the AI-generated meta model from Numerai. Be careful with your money and your wallet credentials! The code I’ve posted is clearly explained, use it at your own risk!

---

### Post #2 — **jefferythewind** | 2024-12-18 21:24 UTC

So I’ve updated the repository with a backtesting framework. Currently this backtester is basically running from [Hyper Liquid’s historical data](<https://hyperliquid.gitbook.io/hyperliquid-docs/historical-data>).

[Github Repo](<https://github.com/jefferythewind/defi_crypto_pm/tree/main>)

[Back Tester](<https://github.com/jefferythewind/defi_crypto_pm/blob/main/Back%20Tester.ipynb>)

It works by

  1. first assuming we will trade the same time every day, which now is right before 11 PM UTC.
  2. Using the same oracle that is used in live trading, the same function to draw the oracle portfolio for each day.
  3. Executes the portfolio against the available historical data from the Hyper Liquid DEX historical data database.
  4. Daily rebalancing and stat collection.



**Trun off FAST MODE the first time through, it needs to slowly grab the data from Hyper Liquid’s S3 buckets and save it locally, but after one time through the data (overnight), you can turn on fast mode and complete and backtest in just 1 minute or so.**

I refined a bit the TB N function, since just getting the current best portfolio from the current meta model each day is not ideal. Instead I’ve adapted the function to get the top and bottom scored assets of a trailing window of time. [I’ve implementing this function in the oracle file.](<https://github.com/jefferythewind/defi_crypto_pm/blob/main/oracle_interfaces.py>)

What I found is that since June 1, the Hyper Liquid universe has about 130 - 150 tickers, with more more recently. After overlapping with the meta model tickers, **we are only left with current 105 tradable assets.**

**Here are some stats from the backtest with gets the top and bottom 3 assets from this group, over the past 30 days of time.**  


[![Screenshot 2024-12-18 at 4.16.33 PM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/0/09bae125d6134cacedb228f7c763260e34edfb73_2_461x375.jpeg)Screenshot 2024-12-18 at 4.16.33 PM1230×1000 66.6 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/0/09bae125d6134cacedb228f7c763260e34edfb73.jpeg> "Screenshot 2024-12-18 at 4.16.33 PM")

And I started risk modeling, by using the `meta_model` column itself as a risk column (after subtracting 0.5 to center it). This gives us an idea of the net “alpha” we have in our somewhat naive portfolio.

[![Screenshot 2024-12-18 at 4.18.33 PM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/5/5a87768b4aea676700e4e5c215059d88020d5994_2_450x375.jpeg)Screenshot 2024-12-18 at 4.18.33 PM1222×1016 81.5 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/5/5a87768b4aea676700e4e5c215059d88020d5994.jpeg> "Screenshot 2024-12-18 at 4.18.33 PM")

Finally, the only real risk control we have is that we are dollar neutral, which is also checked via the ipython notebook.

[![Screenshot 2024-12-18 at 4.19.47 PM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/8/8806c5e4475abe1db4fdf2e7b93f7880de5e2e55_2_464x375.jpeg)Screenshot 2024-12-18 at 4.19.47 PM1252×1010 107 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/8/8806c5e4475abe1db4fdf2e7b93f7880de5e2e55.jpeg> "Screenshot 2024-12-18 at 4.19.47 PM")

With this new insight I’ve been able to implement the portoflio in testnet.

[![Screenshot 2024-12-18 at 4.24.24 PM](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/e/e595ed660da4ea8dac25769f11f238e4bcd52094_2_690x243.jpeg)Screenshot 2024-12-18 at 4.24.24 PM1920×678 112 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/e/e595ed660da4ea8dac25769f11f238e4bcd52094.jpeg> "Screenshot 2024-12-18 at 4.24.24 PM")

The crypto space remains an innovative place. I think soon enough I will run my own vault on Hyper Liquid, making investing in the Numerai Crypto MM even easier!

---

### Post #3 — **joakim** | 2024-12-18 22:23 UTC

Someone please give this guy a bounty!
