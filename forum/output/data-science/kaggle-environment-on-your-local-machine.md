---
title: "Kaggle environment on your local machine"
category: Data Science
url: https://forum.numer.ai/t/kaggle-environment-on-your-local-machine/226
created_at: 2020-04-22T07:34:41.940000+00:00
last_posted_at: 2021-03-29T18:40:12.677000+00:00
posts_count: 3
views: 5539
tags: []
---

# Kaggle environment on your local machine

---

### Post #1 — **kainsama** | 2020-04-22 07:34 UTC

On rocket chat, I have seen people talk about how they have been struggling to get models like XGBoost running on GPU so I decided to share with you instructions on how to set up Kaggle’s environment for Python on your own computer (cloud or local instances). It comes with almost all the libraries you need for data science tasks (for example in this image you have access to XGBoost and CatBoost on both GPU and CPU by default) and it is maintained regularly.

Requirements:

  * I’m assuming that your using Ubuntu as your OS, not Windows or something else with an Nvidia GPU card (but of course it would be nice if someone shares a tutorial for Windows). You have
  * Docker is installed on your computer



Running the container:

  1. clone (or download) `https://github.com/Kaggle/docker-python`
  2. change directory to the folder `docker-python`
  3. build a docker image with the latest updates `./build --gpu`  
**note** : this step would take a while to finish and you need to have space for docker to download like 50GB+ of images
  4. run the image using the following script:  
`docker run -d --name=kagglecontainer --restart=always -v $(pwd):/home/ml/Kain --env LD_LIBRARY_PATH=/usr/local/cuda/lib64 --runtime=nvidia -p 9999:8888 -it kaggle/python-gpu-build jupyter notebook --no-browser --ip="0.0.0.0" --NotebookApp.token='' --NotebookApp.password='' --allow-root`  
**note** : here you can replace `9999` with the port you want to use, replace `/home/ml/Kain` with your own working directory for data science tasks
  5. go to localhost:9999 (or whatever port to you replaced 9999 with) in your browser to have access to the environment



Atter this, the only thing we need to do is build a docker image from time to time and run it as a container. With this docker container, we can have the same functionalities avaiable in Kaggle environments on our local machines (without run time or hard disk restrictions).

---

### Post #2 — **surajp** | 2020-05-05 05:08 UTC

Colab works well for me

---

### Post #4 — **sirmobius** | 2021-03-29 18:40 UTC

Thanks, this is great.

I would be very interested if anyone could share how to do this on a windows 10 machine - without using WSL2.
