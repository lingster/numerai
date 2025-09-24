# Discord: crypto channel


### Summary of the Discussion

The chat kicks off with excitement about the new crypto tournament. Participants quickly dive into the technical details, pointing out a discrepancy in the documentation regarding the submission file format (.parquet vs. .csv). This is promptly clarified by a Numerai team member, who confirms that **both formats are supported**.

A significant portion of the conversation is dedicated to **data acquisition**. Since the crypto tournament is a "bring your own data" competition, users share and inquire about various data sources, including free APIs like Binance and Twelve Data, as well as paid services. There's also a discussion about using community-provided datasets, such as one being developed by YIEDL.

Strategy is another hot topic. Participants brainstorm ideas for features, considering the unique challenges of the crypto market, such as its high volatility and the long one-month prediction horizon. Some suggest using trends and correlations between different crypto categories (e.g., memecoins, DeFi), while others focus on technical indicators like momentum and RSI.

The `numerapi` library is a key tool for many participants, and there are several technical discussions about how to use it for the new crypto tournament, including code snippets for submitting predictions.

### Highlights for the Numerai Data Science Challenge

Here are some key takeaways and tips from the chat that could be useful for the Numerai Crypto tournament:

#### Data and Submissions

  * **Submission Format:** You can submit your predictions in either **.csv or .parquet** format.
  * **Data Sources:**
      * **Free:** Binance API, Twelve Data (free tier available), Yahoo Finance, and CCXT library are mentioned as potential sources for OHLCV data.
      * **Community-Driven:** Keep an eye out for community-provided datasets like the one from YIEDL, which may offer pre-processed features.
  * **Data Issues:** Be aware of potential data quality issues, such as gaps in historical data and inconsistencies in the universe of available tokens.

#### Modeling and Strategy

  * **Feature Engineering:**
      * **Momentum and RSI:** The example model, which performs well, reportedly uses momentum and RSI features.
      * **Correlations:** Consider using correlations between different cryptocurrencies or crypto categories as features.
      * **Meme Factor:** The chat humorously suggests that predicting memes is key to predicting the crypto market, highlighting the importance of sentiment and trend analysis.
  * **Target:** The target is based on **ranked raw returns**, not neutralized returns, over a 30-day period.
  * **Meta Model:** The meta model is currently a **naive-weighted average** of all staked models (\>= 1 NMR) to prevent distortion from large stakeholders.
  * **MMC (Meta-Model Contribution):** There's a debate about whether MMC is a suitable metric for a new tournament with few stakes. Some argue that it disincentivizes participation and should be removed until the tournament matures.

#### Programming and Tools

  * **`numerapi` for Crypto Submissions:**
      * To submit to the crypto tournament, you need to specify `tournament=12`.
      * A user-provided Python snippet shows how to create a custom `NumeraiCyptoAPI` class to simplify submissions until `numerapi` is officially updated:
        ```python
        class NumeraiCyptoAPI(numerapi.NumerAPI):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.tournament_id = 12

            def upload_predictions(self, file_path, model_id, df=None):
                return super().upload_predictions(file_path=file_path, tournament=self.tournament_id, model_id=model_id, df=df)
        numerapi.CryptoAPI = NumeraiCyptoAPI
        ```
  * **Automation:** Numerai now officially supports automation for crypto submissions, likely through webhooks and the `numerai-cli`.
  * **Community Scripts:** Users have shared helpful scripts, such as a Colab notebook for analyzing intra-round daily scores.

This chat log provides a valuable snapshot of the early days of the Numerai Crypto tournament, offering a wealth of practical tips and strategic insights for anyone looking to participate.


### Summary of resources from crypto chat
Of course. Here is a table of the resources shared in the "crypto" chat, including the URL and a short description:

| Resource | Description |
|---|---|
| [https://github.com/numerai/numerai-cli](https://github.com/numerai/numerai-cli) | The official command-line interface (CLI) for Numerai, used to deploy and manage compute infrastructure for your models. |
| [https://github.com/numerai/numerapi](https://www.google.com/search?q=https://github.com/numerai/numerapi) | The official Python client for the Numerai API. It is used to interact with the tournament, submit predictions, and manage stakes. |
| [https://colab.research.google.com/drive/1dI-MA\_oe5ETOFj\_4s4c-oM\_m\_g2dsoO3\#scrollTo=z-mYj2geXn4V](https://www.google.com/search?q=https://colab.research.google.com/drive/1dI-MA_oe5ETOFj_4s4c-oM_m_g2dsoO3%23scrollTo%3Dz-mYj2geXn4V) | A Google Colab notebook for analyzing intra-round daily scores for the crypto tournament. |
| `Binance API` | A popular API for accessing cryptocurrency market data. |
| `Twelve Data` | A financial data provider that offers a free tier for accessing market data. |
| `Yahoo Finance` | A widely used source for historical and real-time financial data. |
| `CCXT` | A Python library that provides a unified interface for interacting with various cryptocurrency exchanges. |
| `YIEDL` | A community-driven project to create and share datasets for the Numerai tournament. |

