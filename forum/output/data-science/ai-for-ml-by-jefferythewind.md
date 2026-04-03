---
title: "AI for ML by jefferythewind"
category: Data Science
url: https://forum.numer.ai/t/ai-for-ml-by-jefferythewind/8245
created_at: 2026-02-14T21:04:04.130000+00:00
last_posted_at: 2026-02-14T21:04:04.204000+00:00
posts_count: 1
views: 251
tags: []
---

# AI for ML by jefferythewind

---

### Post #1 — **unsentient** | 2026-02-14 21:04 UTC

_Based on a presentation given at th_ e January 2026 _Numerai Symposium by_ [@jefferythewind](</u/jefferythewind>) _Restated and posted with permission._

## The Problem: Convergence in Quantitative Finance

If you are a data scientist or a participant in a tournament like Numerai, you face a common problem: convergence. If everyone uses the same open-source libraries, the same GitHub repositories, and the same standard models (like XGBoost), everyone’s predictions eventually look the same.

To win, you need to be unique. You need to find signal where others aren’t looking. But how do you automate “being unique”?

The solution isn’t just asking ChatGPT to write code—it’s building a system where a local Large Language Model (LLM) learns, through trial and error, to write machine learning pipelines that actually perform better on financial data. This is the concept of **AI for ML** : using Reinforcement Learning (RL) to train an LLM to become a better data scientist.

## Why Reinforcement Learning?

Most fine-tuning of LLMs is done via **Supervised Learning**. You feed the model a dataset of inputs (x) and outputs (y) and tell it to minimize the loss. While effective for general instruction following, this method is too rigid for discovery; it simply teaches the model to mimic existing high-quality code.

**Reinforcement Learning (RL)** offers a different paradigm. In RL, an agent interacts with an environment, takes actions, and receives a reward. It learns through exploration.

  * **Supervised Learning:** “Here is the correct code. Memorize it.”

  * **Reinforcement Learning:** “Try writing some code. If it makes money, do that more. If it crashes, do that less.”




This approach allows the model to explore the “action space” of potential Python code to find novel architectures or feature engineering methods that a human might not explicitly teach it.

## The RL Loop: Traditional vs. LLM

In traditional RL (like training an AI to play Super Mario or land a Lunar Lander), the action space is tiny—typically discrete movements like “thrust up” or “move left.”

In **LLM RL** , the paradigm shifts significantly:

**Agent**

  * Trad RL: ML Model / FFNN
  * LLM RL: The LLM itself (Policy pi)



**State (** S_t**)**

  * Trad RL: Game pixels, sensor readings
  * LLM RL: the context prompt (which can be engineered)



**Action (** a_t**)**

  * Trad RL: Small, discrete (e.g., L/R/Up)
  * LLM RL: Huge (Any text or code)



**Reward (** r_t**)**

  * Trad RL: Score, distance, survival time
  * LLM RL: Code compilation & Financial Metrics (Sharpe)



## The Architecture: Building the Environment

The hardest part of applying RL to coding is defining the environment. You can’t just let an LLM hallucinate code into the void; the code has to execute successfully to be evaluated.

To solve this, I utilized the **Model Context Protocol (MCP)** to create a server that acts as the environment. This creates a structured pipeline where the LLM interacts with specific tools.

### The Pipeline Structure

The LLM is given a strict workflow. It cannot change the raw data, but it is given “override” permissions for specific creative steps:

  1. **Load Data:** (Locked)

  2. **Create Target:** (Optional Override) – The LLM can design its own target variable.

  3. **Create Features:** (**Override Allowed**) – The LLM can write Python code to engineer new features.

  4. **Define Model:** (**Override Allowed**) – The LLM can define the architecture (e.g., a specific neural network or decision tree).

  5. **Define Cross-Validation:** (Optional Override)

  6. **Run Optimization & Metrics:** (Locked) – We must evaluate every model on the same playing field.




The LLM generates code, the MCP server executes it, and the results are fed back into the loop.

## Implementation Details

You do not need a massive cluster to do this. This Proof of Concept (PoC) was built using consumer-grade hardware and efficient fine-tuning techniques.

  * **Model:** Mistral-7B-Instruct

  * **Hardware:** Single NVIDIA RTX 3090 (24GB VRAM)

  * **Technique:** **QLoRA** (Quantized Low-Rank Adaptation)




By using QLoRA, we can load the model in 4-bit quantization and only train a small subset of parameters (adapters), making the process feasible on a single GPU.

### The Training Loop (PPO)

We use **Proximal Policy Optimization (PPO)** , the same algorithm OpenAI used for RLHF (Reinforcement Learning from Human Feedback). The loop functions as follows:

  1. **Rollout:** The model generates a batch of ML code (episodes).

  2. **Evaluation:** The code runs. We calculate the reward.

  3. **Update:** We run a PPO training step to update the model weights, encouraging the behaviors that led to high rewards.

  4. **Repeat.**




## The Reward Function

How do we tell the AI it did a good job? The reward function is a composite metric:

Reward = (0.3 *Compile Score) + (0.7 *Performance Score) 

  * **Compile Score:** A binary filter. If the code crashes or fails to run, it gets a -1. If it runs successfully, it gets a 0. This forces the model to learn valid Python syntax.

  * **Performance Score:** If the code runs, we look at financial metrics like the **Sharpe Ratio** or Total Return.




The model is essentially being told: _“First, write valid code. Second, write code that maximizes Sharpe.”_

## Results: Does it Work?

Over a test run of 40 cycles (episodes), the results showed a clear trend.

  1. **Rising Sharpe:** The “Best Sharpe” metric consistently trended upward. The model was not just memorizing syntax; it was finding model configurations that performed better on the validation set.

  2. **Compile Success:** The model averaged a **60% compile success rate**. While it still produced broken code frequently, the RL process allowed it to filter out the noise and learn from the successes.




## Conclusion

This experiment demonstrates that we can treat the LLM as a policy network in an RL context. By wrapping an LLM in an execution environment (MCP) and rewarding it for financial performance, we move beyond simple code completion.

We are no longer just asking AI to write code; we are asking it to _evolve_ strategies. For quantitative finance, where uniqueness is the only way to generate alpha, this approach opens a new frontier: automated, idiosyncratic model discovery.
