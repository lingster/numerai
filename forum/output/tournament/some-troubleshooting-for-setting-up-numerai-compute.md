---
title: "Some troubleshooting for setting up Numerai Compute"
category: Tournament
url: https://forum.numer.ai/t/some-troubleshooting-for-setting-up-numerai-compute/3623
created_at: 2021-06-19T19:04:14.619000+00:00
last_posted_at: 2022-04-23T09:58:53.787000+00:00
posts_count: 15
views: 2478
tags: []
---

# Some troubleshooting for setting up Numerai Compute

---

### Post #1 — **ml_is_lyf** | 2021-06-19 19:04 UTC

## EDIT: I had quite a few problems setting up Numerai compute, I’ve described my solutions in this post, hopefully, it’ll help other users migrating to Numerai compute in the future.

### TLDR

  1. “Cannot read property ‘taskArn’ of undefined” error occurs as there is no error handling in the export.js code for Lambda. It assumes that the ECS will successfully start. If it fails to start, and there are no tasks, then you get the error above.
  2. It seems if you have a new AWS account you can only use the “gen-md” node type. If you try to use a larger spec then you’ll encounter the taskArn error above as the task will never start.
  3. gen-md seems specs seem sufficient for a prediction script (for reference I’m using TensorFlow), but you’ll need to make sure your loading the dataset into a memory in a sensible way (cast to float16 during loading rather than after), otherwise you’ll get OOM errors.
  4. You may also get the taskArn error if you try to run more than 2 models on compute. To get around this I requested a quota increase from AWS. They only bumped my quota a little (to 150 on-demand instances from the 100 they originally gave me), much less than I thought I needed, but the next week compute was successful for all 15 of my models. Maybe they increased a hidden quota in the backend? Or maybe it was because my account paid its first bill, so maybe that unlocks some hidden quota in the backend?



## Original post

I tested my model build locally using:
    
    
    node test -l -v
    

And my submission is successful. But when the webhook is tested it gets an internal server error:
    
    
    Checking if Numerai can Trigger your model...
    2021-06-19 19:49:18,185 ERROR numerapi.base_api: Error received from your webhook server: {"message":"Internal Server Error"}
    

With the following error:
    
    
    [2021/06/19/[$LATEST]43d836c017944196929c1420f3ff3d04] 2021-06-19 19:49:18.453000: 2021-06-19T18:49:18.453Z     8ec1176d-68a8-4026-a2e5-e356fa95aec3    ERROR   Invoke Error    {"errorType":"TypeError","errorMessage":"Cannot read property 'taskArn' of undefined","stack":["TypeError: Cannot read property 'taskArn' of undefined","    at Runtime.exports.handler (/var/task/exports.js:46:34)","    at process._tickCallback (internal/process/next_tick.js:68:7)"]}

---

### Post #2 — **ml_is_lyf** | 2021-06-20 10:35 UTC

In case it was a system configuration issue, I tried uninstalling Docker for Windows, and instead installing Ubuntu 20 via WSL2. I got docker installed on it and numerai-cli. Built the node again, redeployed, tested, and encountered exactly the same error

---

### Post #3 — **ml_is_lyf** | 2021-06-20 11:34 UTC

After some further digging in the AWS console using the logs, it seems to be coming from this code in Lambda (“export.js”):
    
    
    const AWS = require('aws-sdk');
    const util = require('util');
    
    
    exports.handler = async (event) => {
        const body = JSON.parse(event.body)
        console.log(body)
        const task_name = process.env.ecs_task_arn.split('/')[1].split(':')[0]
        
        const ecs = new AWS.ECS();
    
        let messages = []
        
        // run an ECS Fargate task
        const params = {
            cluster: `${process.env.ecs_cluster}`,
            launchType: 'FARGATE',
            taskDefinition: `${process.env.ecs_task_arn}`,
            networkConfiguration: {
                awsvpcConfiguration: {
                    subnets: [
                        `${process.env.subnet}`,
                    ],
                    assignPublicIp: "ENABLED",
                    securityGroups: [
                        `${process.env.security_group}`,
                    ],
                },
            },
            overrides: { 
                containerOverrides: [{
                    name: task_name,
                    environment: [{ 
                        name: "TRIGGER_ID",
                        value: body.triggerId
                   }]
                }]
            }
        };
        console.log("running task with taskDefinition:", params.taskDefinition);
        const taskStart = await ecs.runTask(params).promise();
    
        console.log("started :", );
    
        const message = {
            task: taskStart.tasks[0].taskArn,
            status: "pending"
        };
        messages.push(message)
    
        return {
            statusCode: 200,
            body: JSON.stringify(messages)
        };
    };
    

The logs say its happening on line 46 which is this:
    
    
            task: taskStart.tasks[0].taskArn,
    

My knowledge of JavaScript is pretty basic, but I am guessing whats happening is the `taskStart.tasks[0]` is undefined.

---

### Post #4 — **ml_is_lyf** | 2021-06-20 12:46 UTC _(reply to #3)_

I tried changed line 45 onwards to the following:
    
    
        const message = {
            task: taskStart.failures[0],
            status: "pending"
        };
        messages.push(message)
        
        console.log(message)
    
        return {
            statusCode: 200,
            body: JSON.stringify(messages)
        };
    

The reasoning was if you look at the documentation of the return value of ecs.runTask, it returns a JSON with an error parameter which the javascript code is ignoring [run-task — AWS CLI 1.19.97 Command Reference](<https://docs.aws.amazon.com/cli/latest/reference/ecs/run-task.html#output>)

I’m now seeing in the logs:
    
    
    INFO { task: { reason: 'The requested MEMORY configuration is above your limit' }, status: 'pending' }
    

So it seems like starting the ECS is failing as I’m requesting more memory than I’m allowed.

---

### Post #5 — **ml_is_lyf** | 2021-06-20 13:36 UTC

Seems like this is a common problem, my AWS account was dormant for many years so this is probably the issue:

<https://forums.aws.amazon.com/thread.jspa?threadID=335825>

---

### Post #6 — **ml_is_lyf** | 2021-06-20 18:35 UTC

I tried creating a new AWS account, and ran into the issue again. So I guess there must be new restrictions on the amount of compute new users can access.

I did manage to get the node to run by reducing down to the gen-md preset, which has 2 CPUs and 8GB of RAM. Any more CPUs and I got ‘The requested CPU configuration is above your limit’, and more memory and I got ‘The requested MEMORY configuration is above your limit’. But unfortunately this is far few resources to run my prediction script, with the node running out of memory shortly after downloading the dataset for this week:
    
    
    [ecs/numerai-ml_is_lyf/a5374f8f09f04513bda918d15bbb6def] 2021-06-20 19:25:47.709000: Downloading data from https://numerai-public-datasets.s3-us-west-2.amazonaws.com/latest_numerai_tournament_data.csv.xz
    167870464/167863420 [==============================] - 8s 0us/step0 19:25:55.768000:
    
    Task is stopping...
    Container Exit code: 137
    Reason: OutOfMemoryError: Container killed due to memory usage
    checking for submission...
    Your node did not submit the Trigger ID assigned during this test, please ensure your node uses numerapi >= 0.2.4 (ignore if using rlang)

---

### Post #7 — **ml_is_lyf** | 2021-06-20 20:43 UTC

I managed to get it working, looks like I just needed to be a bit smarter on how to load the dataset using pandas. Previously I was casting to np.float16 AFTER loading in the dataset. But I saw JRB’s post where he sets it to np.float16 during reading via the dtype arg:

![](http://forum.numer.ai/user_avatar/forum.numer.ai/jrb/48/2767_2.png) [Saving memory with uint8 features](<http://forum.numer.ai/t/saving-memory-with-uint8-features/254>) [Data Science](</c/data-science/5>)

> I’ve noticed that there have been quite a few complaints in the chat rooms about memory usage on compute since the test set got bigger. I’d originally contributed the float16 patch to example_model.py to help alleviate this, a couple of months ago. I just realized that there’s a simple way improve on this and to nearly halve the memory usage in your inference pipeline if you’re using a tree based classifier (Xgboost, Catboost, Lightgbm, etc). We just need to rescale the features and cast them t… 

So I changed my code to set the dtype as np.float16 for the feature column and target like so:
    
    
    tournament_data = pd.read_csv(tournament_data_file_path, dtype={COLUMN_NAME: np.float16 for COLUMN_NAME in FEATURE_COLUMNS+["target"]})
    

And now my prediction script runs successfully on the gen-md node.

---

### Post #8 — **ml_is_lyf** | 2021-06-22 08:26 UTC

For anyone who needs a higher spec machine. It turns out you need to request a quota increase for Fargate on AWS to use machines with larger than 8GB of RAM and 2 vCPUs. At the time of writing, there is no option for an increase in vCPU/RAM, but if you request a quota increase for something under Fargate, and explain the issue your encountering, the support team seems aware of the issue and are able to help you resolve it.

---

### Post #9 — **aventurine** | 2021-06-23 23:22 UTC

![](http://forum.numer.ai/letter_avatar_proxy/v4/letter/m/e56c9b/48.png) ml_is_lyf:

> ` task: taskStart.failures[0],`

I think you might have just saved my life!!! I just randomly stated having issues with compute a couple weeks back with the taskArn/Internal Server Error. Just made the change to all my Lamda files in AWS and ran local test and it looks like it will work. I am also getting success testing the node web addresses in the models tab! Thank you!

---

### Post #10 — **ml_is_lyf** | 2021-06-25 16:30 UTC _(reply to #9)_

Great to hear, glad it helped ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=9)

---

### Post #11 — **ml_is_lyf** | 2021-06-27 10:25 UTC

I’ve encountered a new issue now. Looks like by default AWS only allows you to run 2 Fargate instances concurrently. I haven’t managed to capture the full error message associated with the limit, as again when this error is given the number of tasks is 0, so the taskArn problem occurs again. I managed to get a snippet of it though, which says “the limit on the number of tasks you can run concurrently”. Currently my quota is limited to 100 on-demand Fargate instances. So I’m assuming 750 is needed to run 15 models in parallel. I’ll make a request for this and update when I hear back.

---

### Post #12 — **ml_is_lyf** | 2021-07-01 18:12 UTC _(reply to #11)_

AWS got back to me. They said they can only bump me up to 150 for now as my account is new. They gave these tips on how to be accepted for higher usage limits:

>   * Use your services about 90% of usage in that way we can request a limit increase.
>   * You can use a Free Tier for a month, in order to increase the activity in your account and the Service Team can analysis your request.
>   * You can wait for the next billing cycle then we can request again the limit increase.
>   * Take advantage of free tier resources in other regions and later on attempt to use a different area.
> 


So it sounds like if you want to use compute for lots of models you need to grind AWS.

---

### Post #13 — **ml_is_lyf** | 2021-07-03 19:32 UTC _(reply to #12)_

Surprisingly this week all my models ran successfully without the concurrency issue. I’m guessing maybe the Fargate team reduced some hidden limit in the backend when I asked for a usage increase? Or maybe the instances quota doesn’t scale linearly? Or it might have been because last week I paid my first bill, so maybe that unlocked a hidden limit? Either way, I am now able to run 15 models on compute ![:slight_smile:](http://forum.numer.ai/images/emoji/twitter/slight_smile.png?v=9)

---

### Post #14 — **ml_is_lyf** | 2021-08-15 09:45 UTC _(reply to #4)_

Ark just mentioned on RocketChat you can change line 43 (currently ` console.log("started :", );` ) to the following:
    
    
        console.log("task response:");
        console.log(util.inspect(taskStart))
        
        if (!taskStart.tasks || !taskStart.tasks.length) {
            return {
                statusCode: 500,
                body: JSON.stringify(taskStart)
            }
        }
    

This is way nicer than changing line 45 onwards like I did, as it means your webhook responds with the error if there is one, so it’s easier to see the problem.

---

### Post #15 — **ml_is_lyf** | 2022-04-23 09:58 UTC

I just upgraded to the new compute and it turns out symlinks are no longer supported for model paths when configuring your node. If you configure the path to your model using a symlink, when you try to deploy it you’ll see a runtime error like:
    
    
    RuntimeError: Current directory invalid, you must run this command either from "C:/my_symlink/my_model" or a parent directory of that path.
    

I’ve reported this issue in RocketChat so hopefully it’ll be fixed in a future release.
