---
title: "Development Environments - RapidsAI, cuML, Docker"
category: Data Science
url: https://forum.numer.ai/t/development-environments-rapidsai-cuml-docker/2307
created_at: 2021-03-12T01:38:00.368000+00:00
last_posted_at: 2021-03-12T01:38:00.484000+00:00
posts_count: 1
views: 1372
tags: []
---

# Development Environments - RapidsAI, cuML, Docker

---

### Post #1 — **krm** | 2021-03-12 01:38 UTC

I’ve been asked a few times in RocketChat to go over how to leverage RapidsAI and Docker for both local or Compute development.

The best place to start is with Docker.  
From Docker themselves:

> Docker takes away repetitive, mundane configuration tasks and is used throughout the development lifecycle for fast, easy and portable application development - desktop and cloud. Docker’s comprehensive end to end platform includes UIs, CLIs, APIs and security that are engineered to work together across the entire application delivery lifecycle.

What is RapidsAI?

![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/1X/056e7f169c39a0c3d1709eac8947fdc9c7336abf.png) [RAPIDS | GPU Accelerated Data Science](<https://rapids.ai/>)

### [RAPIDS | GPU Accelerated Data Science](<https://rapids.ai/>)

Open source GPU accelerated data science libraries

The tl;dr is that RapidsAI is a pre-built set of GPU ready docker containers and libraries (including everyone’s favorite XGBoost).  
You can run the Rapids environment locally via conda as well, but when in rome…

What cool stuff do I get?  
There are a bunch of cool GPU accelerated packages that come ready to rip, the one that first got me interested was [Welcome to cuML’s documentation! — cuml 25.02.00 documentation](<https://docs.rapids.ai/api/cuml/stable/>)  
cuML is insanely fast for most of the big computation that I’ve come across.  
It does take some casting between numpy, pandas, cudf, and cupy but we are using Python, so casting is part of life right?  
<https://docs.rapids.ai/overview/latest.pdf>  
This is a really good overview of all the GPU accelerated features that cuML opens up.  
Something else that is super snazzy is the pre-configured Dask Scheduler, even for my single GPU setup I can run a lot of stuff in parallel.

So what if I want to try it out and feel the speed for myself?  
Read below:

Pre-Reqs:

  * Linux
  * NVidia GPU



First install Docker

![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/6/6cb676b81038818ae990f74639ec6704a3531b4e.png) [Docker Documentation – 12 Nov 24](<https://docs.docker.com/engine/install/> "03:37PM - 12 November 2024")

![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/2X/1/12f289aea2774af1106f968d7dac2e3a6b6aa611_2_690x362.webp)

### [Install](<https://docs.docker.com/engine/install/>)

Learn how to choose the best method for you to install Docker Engine. This client-server application is available on Linux, Mac, Windows, and as a static binary.

Then install the NVidia GPU CUDA Drivers

![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/f/fbd43c92cdb0edf8fafab6335a92b1f9d26ead9a.png) [docs.nvidia.com](<https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html>)

### [1\. Introduction — Installation Guide for Linux 12.8 documentation](<https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html>)

The installation instructions for the CUDA Toolkit on Linux.

go through:

  * Pre-Installation
  * Package Manager Installation
  * Driver Installation



Next download and run the basic RapidsAI Docker Container

[RAPIDS Docs](<https://docs.rapids.ai/install/>)

![](https://canada1.discourse-cdn.com/flex009/uploads/numerai/optimized/1X/3748e19c37cb9f611dfd8e3d3f20180daaee0259_2_690x345.png)

### [Installation Guide - RAPIDS Docs](<https://docs.rapids.ai/install/>)

Guide to installing RAPIDS
    
    
    docker pull rapidsai/rapidsai:0.18-cuda11.0-runtime-ubuntu20.04-py3.8
    docker run --gpus all --rm -it -p 8888:8888 -p 8787:8787 -p 8786:8786 \
        rapidsai/rapidsai:0.18-cuda11.0-runtime-ubuntu20.04-py3.8
    

  * make sure to select the right CUDA version, OS version
  * I use python 3.8 here for the walrus operator `:=` ![:slight_smile:](https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=13)



Once the container boots, it will display a URL to open for the Jupyter labs instance

If you like the environment and want to make it a bit more reusable, here are a few steps to consider:

  1. Make a shell script that runs the docker command
  2. Get rid of the `--rm`
  3. Add some volumes for your personal files/notebooks
  4. Persist the Jupyter settings
  5. More?



This is an older example of my start-rapids.sh script which shows off a bunch of the optional flags:  
#!/bin/sh
    
    
    sudo docker run \
      --gpus all \
      -it \
      -p 8888:8888 \
      -p 8787:8787 \
      -p 8786:8786 \
      -e EXTRA_APT_PACKAGES="build-essential" \
      -e EXTRA_PIP_PACKAGES="numerapi numpy" \
      -e EXTRA_CONDA_PACKAGES="joblib scikit-learn torch" \
      -v $(pwd):/rapids/workspace \
      rapidsai/rapidsai:cuda11.0-runtime-ubuntu20.04-py3.8
    

Happy to talk more about local / cloud development environments with people. I’ve been working with AWS for many years professionally, and love helping myself/others optimize their workflows through tooling ![:slight_smile:](https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=13)
