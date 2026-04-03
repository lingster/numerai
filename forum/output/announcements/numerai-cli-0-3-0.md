---
title: "Numerai CLI 0.3.0"
category: Announcements
url: https://forum.numer.ai/t/numerai-cli-0-3-0/2627
created_at: 2021-04-01T15:11:01.347000+00:00
last_posted_at: 2021-04-01T15:11:01.469000+00:00
posts_count: 1
views: 2004
tags: []
---

# Numerai CLI 0.3.0

---

### Post #1 — **ark** | 2021-04-01 15:11 UTC

Attention Data Scientists! We are announcing an important new update to the Numerai CLI that introduces the idea of Prediction Nodes, the new generic building block for your models. Prediction Nodes are agnostic to cloud providers, tournaments, data sources, and languages. This update allows you to configure your current model as a Prediction Node that runs on any one of the supported cloud providers. It also gives us a software architecture to add more [**cloud providers supported by terraform**](<https://registry.terraform.io/browse/providers>), improve commands and UX, and streamline setup.

If you haven’t seen already, the 0.2 versions of the tool added scripts and documentation making setup easier than ever! If you haven’t set up Numerai Compute yet, start submitting reliably and automatically today by visiting the [**numerai-cli repository**](<https://github.com/numerai/numerai-cli>) and following the setup steps. If you already have Numerai Compute setup, simply run these commands to get the latest version and update your .numerai configuration files:

  * pip install --upgrade numerai-cli
  * numerai upgrade



If you’re currently running multiple models on your compute node, you can begin separating these into Prediction Nodes using Dockerfiles in separate directories. For more information please [**review the Prediction Node wiki page**](<https://github.com/numerai/numerai-cli/wiki/Prediction-Nodes>). Any questions and feedback can be directed to the [**Compute Channel**](<https://community.numer.ai/channel/compute>).

Here’s the full Changelog:

  * restructure package code and improve nomenclature
  * new commands structure: 
    * numerai upgrade handles upgrading to 0.3.0 from previous versions of CLI
    * numerai setup only records+tests API keys and initializes configuration
    * numerai node [create | deploy | test | destroy] for configuring and managing Prediction Nodes
    * numerai doctor for checking env setup script, package version, and API keys
    * numerai copy-example copies numerai example code to your computer
    * numerai list-constants list all constants and defaults the CLI uses including Prediction Node size options
  * restructure configuration storage: 
    * move keyfile from $HOME/.numera to .numerai/.keys
    * split keyfile API keys into separate provider sections (allow multiple providers)
    * add logic to move/restructure old keyfile to new keyfile
    * move docker_repo/webhook output to .numerai/nodes.json
    * move entire .numerai/ config folder to $HOME/.numerai/
  * Restructure Terraform: 
    * restructure terraform into more navigable file structure
    * add terraform nodes.json file input so it can read config directly
    * modularize aws resources to make room for future cloud providers
    * cloud provider modules take input for per-node configurations
    * reformat terraform outputs to compute per-node outputs
  * update webhook lambda code to handle new Trigger ID, which will help pinpoint issues in the pipeline
  * misc: remove unnecessary .gitignore entries
  * lots of bug fixes



If you want to read more about why this update matters and the vision of Numerai Compute, [**check out our Medium Post**](<https://medium.com/numerai/building-the-numerai-network-af733c29d56f>). Automate your submissions today so you don’t miss another round ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=9)
