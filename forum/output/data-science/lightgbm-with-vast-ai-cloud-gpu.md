---
title: "LightGBM with vast.ai cloud GPU"
category: Data Science
url: https://forum.numer.ai/t/lightgbm-with-vast-ai-cloud-gpu/4478
created_at: 2021-11-09T18:47:22.255000+00:00
last_posted_at: 2021-11-11T06:40:20.525000+00:00
posts_count: 2
views: 1386
tags: []
---

# LightGBM with vast.ai cloud GPU

---

### Post #1 — **gbrecht** | 2021-11-09 18:47 UTC

Some time ago @yifanxie mentioned vast.ai in rocket chat as a cheap cloud GPU option.  
I liked the instances (you can plugin in any image on docker hub and they give you a running tmux session) and prices so I played around with them. This is not meant as advertising.

With the release of the new dataset it became clear that CPU training is no longer an option. But the packages you get off pip or conda for lightgbm do not have GPU support. The compile instructions for GPU support are pretty straightforward, but I never got it to run. There was always some error or another. I found a gpu docker file on the lightgbm github and found a working setup. I talked about it in rocketchat and said I would do a forum post if there was interest in it. I got a :shufflepartyparrot: from [@surajp](</u/surajp>), so here we go.

The docker image used on the lightgbm github is `nvidia/cuda:8.0-cudnn5-devel` which is ancient, I currently use `nvidia/cuda:11.2.0-cudnn8-devel-ubuntu20.04` which works fine. It is important to have a devel and cudnn version.

These are the commands I run when the instance is up
    
    
    apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    bzip2 \
    ca-certificates \
    libglib2.0-0 \
    libxext6 \
    libsm6 \
    libxrender1 \
    git \
    vim \
    mercurial \
    subversion \
    cmake \
    libboost-dev \
    libboost-system-dev \
    libboost-filesystem-dev \
    gcc \
    g++ \
    nano htop wget
    
    # Add OpenCL ICD files for LightGBM
    mkdir -p /etc/OpenCL/vendors && echo "libnvidia-opencl.so.1" > /etc/OpenCL/vendors/nvidia.icd
    
    #################################################################################################################
    #           CONDA
    #################################################################################################################
    
    # Install miniconda
    echo "export PATH=/opt/conda/bin:"'$PATH' > /etc/profile.d/conda.sh && \
    curl -sL https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -o ~/miniconda.sh && \
    chmod +x ./miniconda.sh && \
    /bin/bash ~/miniconda.sh -b -p /opt/conda && \
    rm ~/miniconda.sh
    
    conda config --set always_yes yes --set changeps1 no && \
    conda create -y -q -n py3 python=3.8 mkl numpy scipy scikit-learn pandas matplotlib tqdm fastparquet && \
    pip install numerapi xgboost gpustat treelite_runtime treelite halo loguru pyarrow optuna
    
    #################################################################################################################
    #           LightGBM
    #################################################################################################################
    
    cd /usr/local/src && mkdir lightgbm && cd lightgbm && \
    git clone --recursive --branch stable --depth 1 https://github.com/microsoft/LightGBM && \
    cd LightGBM && mkdir build && cd build && \
    cmake -DUSE_GPU=1 -DOpenCL_LIBRARY=/usr/local/cuda/lib64/libOpenCL.so -DOpenCL_INCLUDE_DIR=/usr/local/cuda/include/ .. && \
    make OPENCL_HEADERS=/usr/local/cuda-8.0/targets/x86_64-linux/include LIBOPENCL=/usr/local/cuda-8.0/targets/x86_64-linux/lib
    /bin/bash -c "source activate py3 && cd /usr/local/src/lightgbm/LightGBM/python-package && python setup.py install --precompile"
    

Afterwards you have a conda environment named py3 with everything setup and ready to go. What I do then additionally is to github my code and dropbox some custom data and away we go.

Let me know if this works for you!

---

### Post #2 — **yxbot** | 2021-11-11 06:40 UTC

Nice setup!

additionally, I think now [paperspace’s](<https://www.paperspace.com/pricing>) solution is also getting more cost efficient for those of us relying more on GPU powers for model training ![:slight_smile:](//forum.numer.ai/images/emoji/twitter/slight_smile.png?v=9)
