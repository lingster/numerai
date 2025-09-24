# Discord: Signals Channel 


### Summary of the Discussion

The chat covers a wide range of topics pertinent to the Numerai Signals tournament, which is a "bring your own data" competition. A central theme is the nature of the **target variable**. Participants discuss how the target is calculated, its relationship to raw returns, and how it's neutralized against various factors. There's a clear understanding that the target represents the *rank* of a stock's 20-day return relative to the entire universe of ~5000 stocks, not its absolute return.

Another major topic is **strategy**, specifically regarding what to train models on. Users debate the merits of training on Numerai's provided targets versus creating and training on their own custom targets. This reflects the core challenge of Signals: finding unique data and modeling approaches that are not already captured by the main tournament's meta-model.

The community also heavily discusses the use of **Large Language Models (LLMs)** for generating trading signals from news and social media sentiment. This is an active area of experimentation, with users sharing resources, code notebooks, and even launching their own news APIs.

Finally, there are numerous technical discussions about the `numerapi`, data fetching, submission automation, and the frequent updates to the scoring metrics, which have transitioned from CORR-based to FNCv4 and are moving towards an MMC-like system.

### Highlights for the Numerai Data Science Challenge

Here are some key takeaways and tips from the chat that could be useful for the Numerai Signals tournament:

#### Data and Targets

* **Understanding the Target:** The Signals target is not the raw return of a stock. It is the **rank of the 20-day return** among the entire ~5000 stock universe. This means even a stock with a negative return can have a target of 1 if all other stocks had even more negative returns. There are also several versions of the target, including raw and neutralized versions.
* **Custom Targets:** Many successful participants train on their own custom targets rather than the ones provided by Numerai. One user, for instance, trains on the relative return over the period, calculated as `(t20 - t2) / t2`.
* **Data Quality is Key:** Richard Craib, Numerai's founder, emphasizes that the biggest issue in Signals is participants relying on low-quality data. He warns that if your signal has an FNC above 0.01, you should be cautious as it's very difficult to achieve and may indicate a data quality problem.
* **Data Sources:**
    * **Free:** Yahoo Finance is a common starting point, but be aware of potential data quality issues.
    * **Paid/Community:** Services like `eodhd.com`, `QuantConnect`, and community-driven projects like `Nosible` are mentioned as potential sources for higher-quality data.

#### Modeling and Strategy

* **Feature Engineering:**
    * For beginners, techniques like **BorutaShap** and **Mean Decrease Impurity** are suggested for feature selection.
    * Advanced participants are exploring the use of **LLMs (like GPT-4)** and libraries like **LangChain** to extract sentiment from news articles and social media (e.g., Reddit's r/wallstreetbets) to create unique signals.
* **Neutralization:** The provided targets are heavily neutralized. If you are creating your own signals, you should be mindful of their correlation to known risk factors like market cap. Richard Craib warns against signals that are highly correlated with raw price or market cap.
* **Daily Submissions:** The tournament has moved to a daily submission cadence. Your automation pipeline should be able to handle this, fetching the latest data and submitting predictions for each round.
* **Minimum Tickers:** You must submit predictions for a minimum of 100 stocks. For any missing tickers, Numerai will fill in a neutral value of 0.5 *after* your submitted signals have been ranked.

#### Programming and Tools

* **`numerapi` for Signals:**
    * The `numerapi` library is essential for automating submissions and interacting with the API.
    * When using the API for Signals, you often need to specify the tournament ID (e.g., `tournament=11`).
    * You can use the `raw_query` function with GraphQL to access more advanced data and metrics not available through the standard functions. For example, a user shared a GraphQL query to fetch detailed performance metrics like FNCv4 and RIC.
* **Automation:**
    * Many users automate their daily submissions using cloud services like **AWS (ECS, Fargate)**, **Google Cloud**, or even by running scheduled scripts on a home server.
    * Tools like `numerai-cli` can help set up this cloud infrastructure.
* **Community Resources:** The chat is filled with links to valuable resources, including:
    * **Kaggle Notebooks:** For getting started with Signals, sentiment analysis, and more.
    * **Forum Posts:** Deep dives into topics like decoding the signals target.
    * **Third-party Tools:** Libraries like `OpenFIGI` and community-built tools like `signalslite` can help with ticker mapping and feature engineering.


### Summary of Resources Mentioned 
Here is a table of the resources shared in the "signals" chat, including the URL and a short description:

| Resource | Description |
|---|---|
| [https://github.com/numerai/numerai-cli](https://github.com/numerai/numerai-cli) | The official command-line interface (CLI) for Numerai, used to deploy and manage compute infrastructure for your models. |
| [https://www.kaggle.com/code/yamqwe/crypto-extension-for-numerai-signals-w-lgbm](https://www.google.com/search?q=https://www.kaggle.com/code/yamqwe/crypto-extension-for-numerai-signals-w-lgbm) | A Kaggle notebook demonstrating how to create a crypto-based signal for the Numerai Signals tournament using LightGBM. |
| [https://forum.numer.ai/t/decoding-the-signals-target/6810](https://www.google.com/search?q=https://forum.numer.ai/t/decoding-the-signals-target/6810) | A Numerai forum post that provides a deep dive into understanding the Signals target variable. |
| [https://colab.research.google.com/drive/1ItqLmzZ8B1SaJcdMW9fHPkWiCdYQ7aiA?usp=sharing](https://www.google.com/search?q=https://colab.research.google.com/drive/1ItqLmzZ8B1SaJcdMW9fHPkWiCdYQ7aiA%3Fusp%3Dsharing) | A Google Colab notebook shared by a user to illustrate a point about the scoring mechanics of the Signals tournament. |
| `OpenFIGI` | A library for mapping different ticker formats (e.g., Bloomberg tickers to FIGI). This is useful for standardizing your data. |
| `signalslite` | A community-created tool or library for working with Numerai Signals. |
| `eodhd.com` | A financial data provider that can be used as a source for building signals. |
| `QuantConnect` | A platform for algorithmic trading that can also be used as a data source. |
| `Nosible` | A news API service created by a community member, designed for generating signals from news sentiment. |
| Book: "Advances in Financial Machine Learning" by Marcos Lopez de Prado | A book recommended for its insights into applying machine learning to finance, particularly relevant for feature engineering and selection. |


