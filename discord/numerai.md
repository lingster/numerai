# Discord: Numerai Channel

This document is a chat log from the Numerai Discord server, where data scientists discuss the Numerai tournament. The conversation covers a range of topics including scoring metrics, modeling strategies, and technical tips.

### Summary of the Discussion

The main focus of the chat is on **True Contribution (TC)**, a key performance metric in the tournament. Participants debate its **zero-sum nature**, with some providing evidence against it while others discuss the underlying mathematical proofs. There is a clear demand for a more transparent and official formula for TC.

The conversation also explores the relationship between TC, **Correlation (CORR)**, and the newer **Meta-Model Contribution (MMC)** metric, especially in light of the updated payout formula that heavily weights MMC. Participants share their modeling strategies, with a recurring theme of creating **unique and orthogonal models** to improve their scores.

Technical discussions include issues with the dataset, such as anomalies in certain "eras" (time periods), and tips on using the `numerapi` library for automating submissions. The community appears to be a valuable resource for both new and experienced participants, with users frequently sharing links to forum posts, code, and other helpful resources.

### Highlights for the Numerai Data Science Challenge

Here are some key takeaways and tips from the chat that could be useful for the Numerai tournament:

#### Scoring and Payouts

* **Understand the Metrics:** Familiarize yourself with the different scoring metrics:
    * **CORR (Correlation):** A direct measure of your model's predictive performance.
    * **TC (True Contribution):** A measure of your model's unique contribution to the meta-model.
    * **MMC (Meta-Model Contribution):** The successor to TC, which is now a major component of the payout formula.
* **New Payout Formula:** Starting in 2024, the payout formula is heavily weighted towards MMC: `payout = stake * clip(payout_factor * (corr * 0.5 + mmc * 2), -0.05, 0.05)`. This means that having a high MMC is crucial for profitability.

#### Modeling and Strategy

* **Build Unique Models:** To achieve a high TC and MMC, it's not enough to have a high correlation. Your model needs to be **unique and orthogonal** to the existing models in the tournament.
* **Tree-Based Models:** The chat suggests that **tree-based models** (like LightGBM and XGBoost) have consistently performed well.
* **Neural Networks:** While less common, some participants are experimenting with **neural networks**. These can be more complex to train but could potentially lead to unique models.
* **Feature Neutralization:** This is a technique mentioned in the chat that can help to control risk and improve model stability. You can find resources and examples on the Numerai forum.
* **Don't Overfit to Validation Data:** Be cautious about training on the validation set, as this will make the diagnostics on the website meaningless for evaluating your model's true performance on unseen datGa.

#### Data and Features

* **Weekly Data Updates:** The validation dataset is updated weekly. Make sure your pipeline accounts for these updates to keep your models current.
* **Exploratory Data Analysis (EDA):** It's important to analyze the data for any anomalies. For example, the chat mentions that some features in a specific era were found to be constant values.
* **Feature Metadata:** While there isn't an official script for generating feature metadata, the community consensus is that the statistics are likely calculated using only the "train" portion of the dataset.

#### Programming and Tools

* **numerapi:** Use the `numerapi` Python library to automate your submissions and interact with the Numerai platform.
* **Community Resources:** The Numerai Discord and forum are invaluable resources. You can find help, share ideas, and discover useful tools and code shared by other participants.
* **Cloud Computing:** Services like Google Colab can be a good option for training models if you don't have a powerful local machine.
* **Python Environment:** For model uploads, Numerai supports Python versions 3.9 and 3.10. Ensure your environment is compatible.

### Summary of resources mentioned in numerai chat
Of course. Here is a table of the resources shared in the "numerai" chat, including the URL and a short description:

| Resource | Description |
|---|---|
| [https://www.youtube.com/watch?v=dh-0-V\_1sgc](https://www.google.com/search?q=https://www.youtube.com/watch%3Fv%3Ddh-0-V_1sgc) | A YouTube video of a talk by Richard Craib (Numerai's founder) from 2016. |
| [https://github.com/numerai/numerai-cli](https://github.com/numerai/numerai-cli) | The official command-line interface (CLI) for Numerai, used to deploy and manage compute infrastructure for your models. |
| [https://docs.numer.ai/numerai-tournament/payouts](https://www.google.com/search?q=https://docs.numer.ai/numerai-tournament/payouts) | The official Numerai documentation explaining the payout system. |
| [https://forum.numer.ai/t/true-contribution-release-and-tc-adjusted-staking-threshold/6588/1](https://www.google.com/search?q=https://forum.numer.ai/t/true-contribution-release-and-tc-adjusted-staking-threshold/6588/1) | A Numerai forum post announcing the release of True Contribution (TC) and the TC-adjusted staking threshold. |
| `numerapi` | The official Python client for the Numerai API. It is used to interact with the tournament, submit predictions, and manage stakes. |

