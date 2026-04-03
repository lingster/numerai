---
title: "Automated submission with google cloud"
category: Tournament
url: https://forum.numer.ai/t/automated-submission-with-google-cloud/3888
created_at: 2021-08-01T19:52:59.125000+00:00
last_posted_at: 2021-08-19T13:06:46.418000+00:00
posts_count: 2
views: 2119
tags: []
---

# Automated submission with google cloud

---

### Post #1 — **bor1** | 2021-08-01 19:52 UTC

For those of you who aren’t comfortable following the compute example for aws (I have no idea what I am doing for half the steps), and are happy with something simpler - google cloud made it easier recently to have your virtual machine (VM) spin up on a weekly schedule.

I will explain how in the steps below.

**Step 1. Adding the metadata to the VM config that starts your program**

This program should fetch the numer.ai data, run the predictions, and submit those predictions to numer.ai in any way of your making, and shuts down the VM afterwards.

To add the metadata **click on the name of your VM** , and **click edit**  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/d/dd3ae823d195d0d2c65852e585be3b496bf0d854.png)image434×142 25.3 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/d/dd3ae823d195d0d2c65852e585be3b496bf0d854.png> "image")

  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/8/8185eaeb743ab6f8a6aca7349e1a7ea848a4e5f5.png)image434×112 14.1 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/8/8185eaeb743ab6f8a6aca7349e1a7ea848a4e5f5.png> "image")

Scroll down and **add a metadata entry called “startup-script”** , and **add your own variant of the startup script** you see in the image.  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/3/3c604d238dd42d8272d0eca589e14f97b3ae3f25.png)image623×448 54.7 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/3/3c604d238dd42d8272d0eca589e14f97b3ae3f25.png> "image")

The script I have added there is as follows

> #! /bin/bash  
>  cd /home/username  
>  runuser -l username -c ‘./compute.linux’  
>  sudo poweroff

What it does is go to your user directory --do remember to change _username_ with your actual google cloud username!–, and run your program.

As the startup-script is run by the root user, the first it has to do is switch to the username home directory and invoke your program from there. In this example, the program is a script called compute.linux, and for good practices, we don’t run the program as root but as a user.

Remember that the program is responsible for everything numer.ai related - fetch the data, generate the predictions, and submit the results.

After the program has run its course, the startup-script invokes a “sudo poweroff” to shut down the instance. Note that if the program hangs for some reason, your instance is not shut down!

**Step 2. Schedule your VM to start once a week.**

Not so long ago, google added an instance scheduler to their compute engine, and it is now trivial to set a weekly schedule for your VM, so that you can submit your predictions every week while on holiday ![:smiley:](https://emoji.discourse-cdn.com/twitter/smiley.png?v=13). First **click on instance schedule** , and then **click on create schedule**.  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/5/50b8c4066a68bddd69aa4df4e7c6893b6943a1f4.png)image623×204 43.5 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/5/50b8c4066a68bddd69aa4df4e7c6893b6943a1f4.png> "image")

  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/c/cf0e069b502bc862fcc54b4a5a9cf37d4b95297a.png)image623×252 32.7 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/c/cf0e069b502bc862fcc54b4a5a9cf37d4b95297a.png> "image")

You see that I already have a named schedule there, but I will go through the process of making another one here.

When you click create schedule, you get the following tab.  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/0/099c90efa74cb850621061382597c9a3630650be.png)image623×379 30.9 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/0/099c90efa74cb850621061382597c9a3630650be.png> "image")

What is important for you is to select the same region as your VM is from, and then select a start time/time zone, an initial date from whence forwards the schedule becomes active, the frequency, and when you pick weekly, also the day of the week that your VM is started.

I picked a starting hour that is a few hours later than when the new data typically becomes available. If numer.ai is a bit late in uploading their new weekly dataset, my program isn’t caught trying to predict and submit last week’s predictions again!

**Step 3. Give your schedule permission to start a VM**

Now you have to make a small detour to <https://console.cloud.google.com/iam-admin/iam>, which is where you can give your schedule permission to start your VM.

Your first action is to click the little box marked in red below, and that will make your compute engine service agent show up. Edit its permissions by clicking the pencil to the right, and add the role of Compute Instance Admin (v1) to the service agent account.

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/c/c271fd477cd72b28447dbe2346deb3ca51d38b2e.png)image624×218 30.6 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/c/c271fd477cd72b28447dbe2346deb3ca51d38b2e.png> "image")

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/7/7b837ad0c83eb7dbeab40b70370e2d346c3d575b.png)image624×205 34.4 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/7/7b837ad0c83eb7dbeab40b70370e2d346c3d575b.png> "image")

Well done. Just one more step!

**Step 4. Back to the VM page, and attach the schedule to your VM**

Now, go back to your VM instances page on google cloud, and in the instance schedule tab, **click on the weekly schedule that you created**.  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/1/13b0a72d1e263a3a2e87f62e8fe9eac3e1e8a14f.png)image624×168 27.6 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/1/13b0a72d1e263a3a2e87f62e8fe9eac3e1e8a14f.png> "image")

Now you can add your VM instance to your schedule without errors on permissions.

[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/3/3238106d2f7639fb057d4cba01d51ff15c278e16.png)image624×278 31.2 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/3/3238106d2f7639fb057d4cba01d51ff15c278e16.png> "image")

And congratulations! You are set! You have got something similar to numer.ai’s AWS compute working, but on google’s cloud - which seems better tailored to people that think of the cloud as ssh’ing into a linux box and running a program, rather than fancy stateless functions and docker images ![:stuck_out_tongue_winking_eye:](https://emoji.discourse-cdn.com/twitter/stuck_out_tongue_winking_eye.png?v=13) .

---

### Post #2 — **kenfus** | 2021-08-19 13:06 UTC

Works great, thx! I did try numerai compute but I always got an OOM-Error, even after increasing it to 30 GB. Locally, it only uses around 18 GB of Ram (as proven scientifically with Task Manager) but it still crashes with numerai CLI. However, I also need the 64 GB Ram Box on GCP.

Here is a little script I use to set up the boxes. In the future I might do it with Docker, but here is the script and adapt it as you need:
    
    
    #!/bin/sh
    cd
    sudo apt update
    sudo apt-get install wget -y 
    sudo apt install python3 python3-dev python3-venv -y 
    wget https://bootstrap.pypa.io/get-pip.py
    sudo python3 get-pip.py
    sudo apt-get install p7zip-full -y
    7z x kenfus_2_submission.zip
    pip install pip --upgrade
    pip install -r requirements.txt
    pip install wandb
    python3 -m wandb login <API KEY>
    

Also, this creates a log in the root folder saving all output (google the syntax a little, you’ll find a stackoverflow post with a good description).
    
    
    #!/bin/sh
    exec 3>&1 4>&2
    trap 'exec 2>&4 1>&3' 0 1 2 3
    exec 1>"$(date +"%Y_%m_%d_%I_%M_%p").log" 2>&1
    echo "Starting run at" $(date -u)
