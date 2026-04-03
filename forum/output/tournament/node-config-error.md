---
title: "Node Config Error"
category: Tournament
url: https://forum.numer.ai/t/node-config-error/6613
created_at: 2023-08-11T21:23:19.578000+00:00
last_posted_at: 2023-08-13T20:05:24.938000+00:00
posts_count: 2
views: 449
tags: []
---

# Node Config Error

---

### Post #1 — **rdugh** | 2023-08-11 21:23 UTC

I am trying to config a new node using numerai cli.

The (sample) code I am running goes like this:  
C:\Models\model_a> numerai node config -s mem-lg -p C:\Models\model_a

The error (in red font) that I am getting is as follows :  
No tournament 8 model with name “model_a” found in list of models:  
{  
Here is a list of my models with format mode_name: mode_id  
}  
(use the “-s” flag for signals model)  
I can’t deploy any new model. Running “numerai doctor” shows me no errors, everything is set up correctly.

Thanks

---

### Post #2 — **ark** | 2023-08-13 20:05 UTC

Hey [@rdugh](</u/rdugh>),

Sorry about the confusion here. There are actually 2 -s flags that can be used in different parts of the command, the -s flag you’re using is actually for the size of the node, you’ll need to add a -s before “config” like so:
    
    
    numerai node -s config -s mem-lg -p [path/to/code]
    

Also, apologies for the delay in my response, if you would like faster support I’d recommend heading over to our discord.

Hope this helps,  
Noah
