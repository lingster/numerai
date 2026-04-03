---
title: "Fine-Tuning LLMs with RL for ML Code Generation: Post-Mortem"
category: Data Science
url: https://forum.numer.ai/t/fine-tuning-llms-with-rl-for-ml-code-generation-post-mortem/8235
created_at: 2026-01-29T04:44:39.292000+00:00
last_posted_at: 2026-01-29T04:44:39.345000+00:00
posts_count: 1
views: 193
tags: []
---

# Fine-Tuning LLMs with RL for ML Code Generation: Post-Mortem

---

### Post #1 — **jefferythewind** | 2026-01-29 04:44 UTC

Following up from my talk at the Numerai Symposium today - thanks to everyone who attended and especially those who asked great questions afterward. The feedback inspired me to dig into what the LLM was actually writing and make some adjustments.

## **Quick Recap**

I built a system that uses reinforcement learning to teach Mistral-7B to write ML code for crypto trading. The model generates Python code, the code runs against real data, and the Sharpe ratio becomes the reward signal for PPO updates.

After running overnight (775 experiments, 48 PPO cycles), I got curious about what code the model was actually producing.

## **What I Found**

Someone asked: “What models is it trying?”

So I checked:

Model Type | Usage  
---|---  
LightGBM | 96%  
XGBoost | 0%  
Neural Nets | 0%  
Everything else | 0%  
  
**It used LightGBM 96% of the time and never tried anything else.**

Same story with features - 99.9% of experiments used the template features, only 1 out of 775 attempted custom feature engineering.

## **The Problem: My Prompt**

Re-reading my prompt, I realized I’d been too specific. I included a complete working example using LightGBM:

“model_config”: “import lightgbm as lgb…”

The model learned to copy and modify this example rather than explore alternatives. Classic exploitation over exploration.

## **The Fix**

New prompt - just the rules, no examples:

AVAILABLE PACKAGES:

numpy, pandas, scikit-learn, scipy, statsmodels, lightgbm, xgboost, torch

Model must have .fit() and .predict_proba() methods.

Be creative. Try different models, features, parameters.

Now PyTorch is available, meaning the model could try neural networks. XGBoost, random forests, SVMs - all fair game. Let’s see what it discovers on its own.

## **Why 43% Failed to Compile**

Error Type | % | Cause  
---|---|---  
KeyError | 34% | Tried accessing DataFrame columns that don’t exist  
Syntax Error | 12% | Malformed Python code  
TypeError | 12% | Wrong argument types  
JSON Parse | 9% | LLM output wasn’t valid JSON  
  
The biggest issue - **KeyError** \- happened because the prompt didn’t specify what columns were available in the data. The model would try things like full_data_base[‘target_data’] when that column doesn’t exist.

Fixed in the new prompt by explicitly listing available columns**

## **Run 2 Started**

Reset the model weights back to base Mistral and cleared the replay buffer. The new run is live with the open-ended prompt.

This is the flexibility that RL provides - same training loop, different prompt, potentially very different outcomes. Will report back with what the model tries when given freedom to explore.
