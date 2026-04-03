---
title: "Building XGBoost from source on Windows 10 with GPU support"
category: Data Science
url: https://forum.numer.ai/t/building-xgboost-from-source-on-windows-10-with-gpu-support/333
created_at: 2020-05-05T15:24:59.754000+00:00
last_posted_at: 2020-08-07T16:02:44.493000+00:00
posts_count: 7
views: 3602
tags: []
---

# Building XGBoost from source on Windows 10 with GPU support

---

### Post #1 — **arbitrage** | 2020-05-05 15:24 UTC

You bought/built a new PC and due to your work or personal preference, you use Windows 10. Congratulations on your new purchase! Also, I’m very sorry for all the trouble. Hopefully, this write-up will help you get your machine set up for XGBoost with CUDA.

First thing you should do is download and install Visual Studio Community 2019 and add the C++ build tools

Install Anaconda with Python 3.7

Next, install Mingw64, but create a new folder to install such as C:\mingw and then change the PATH to reflect this

Install CMAKE and allow CMAKE to set PATH

Install CUDA and make sure CUDA recognizes the VS2019 installation

Follow NVIDIA’s instructions to run the sample programs. Doing so will ensure that your PC recognizes CUDA, the GPU, and that CUDA is working correctly. Any errors during this phase must be fixed prior to trying to build XGBoost with GPU support from source.

Install Git for Windows

Open your Git command prompt and:

git clone --recursive <https://github.com/dmlc/xgboost>

git submodule init

git submodule update

cd xgboost

mkdir build

cd build

cmake … --G"Visual Studio 16 2019" -DUSE_CUDA=ON

cmake --build . --config Release

python package install

If you have everything installed correctly and the PATH variables are correct then you will successfully build from source, XGBoost will be installed, and you’ll be heating up your room in no time!

---

### Post #2 — **joakim** | 2020-05-05 23:32 UTC

Thanks [@arbitrage](</u/arbitrage>)! FWIW I’ve upgraded my system now to Pop!OS/Ubuntu 20.04 LTS and everything appears to be working fine so far, including XGBoost. I’m still on v0.90 though with CUDA support, and I don’t dare upgrading it just yet. I mostly just use XGBoost with the example model as my baseline.

---

### Post #3 — **lazerfazer** | 2020-05-11 13:02 UTC

I’ve been using Windows 10, Python 3.6, XGBoost, and CUDA without any problems. Does this give any advantage over the pre-built package?

---

### Post #4 — **arbitrage** | 2020-05-11 13:52 UTC _(reply to #3)_

if you are having no problems then you should leave everything alone. Keep calm and carry on ![:slight_smile:](https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=13)

---

### Post #5 — **lazerfazer** | 2020-05-11 14:01 UTC _(reply to #4)_

Were you having specific issues around CUDA and XGBoost on Windows 10? Having built a good few packages myself previously, back when CUDA on Windows 10 wasn’t as widely supported, I’m just trying to understand why you’d go through the pain of building it yourself

---

### Post #6 — **arbitrage** | 2020-05-11 14:05 UTC _(reply to #5)_

Vanity. Plain and simple ![:slight_smile:](https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=13) I built a new computer and wanted GPU support on XGBoost. I built from source on 3 other PC’s 2 years ago but lost my notes on the process. Not much has changed but I figured I’d write up the process for others should they choose to suffer along with me.

---

### Post #8 — **surajp** | 2020-08-07 16:02 UTC _(reply to #6)_

!git clone --recursive https://github.com/Microsoft/LightGBM
    %cd /content/LightGBM
    !mkdir build
    !cmake -DUSE_GPU=1
    !make -j$(nproc)
    !sudo apt-get -y install python-pip
    !sudo -H pip install setuptools pandas numpy scipy scikit-learn -U
    %cd /content/LightGBM/python-package
    !sudo python setup.py install --precompile
    

This is what I use on colab
