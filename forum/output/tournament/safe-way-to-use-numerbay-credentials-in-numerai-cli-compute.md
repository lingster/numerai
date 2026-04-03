---
title: "Safe way to use numerbay credentials in numerai-cli compute"
category: Tournament
url: https://forum.numer.ai/t/safe-way-to-use-numerbay-credentials-in-numerai-cli-compute/6282
created_at: 2023-04-08T11:25:02.776000+00:00
last_posted_at: 2023-04-08T15:31:19.039000+00:00
posts_count: 2
views: 543
tags: []
---

# Safe way to use numerbay credentials in numerai-cli compute

---

### Post #1 — **quantized** | 2023-04-08 11:25 UTC

I’m using numerai-cli compute for my daily submissions. Not being very experienced with Docker, can someone advise how I can safely use my numerbay credentials in my scripts? I can hard-code into my Dockerfile like this but it’s not great:
    
    
    ARG NUMERBAY_USERNAME
    ENV NUMERBAY_USERNAME="user"
    
    ARG NUMERBAY_PASSWORD
    ENV NUMERBAY_PASSWORD="pass"
    

I know the numerai and AWS keys are stored in .numerai/.keys. Is there a ‘safe’ way to pass other environment variables during `numerai setup`, or another way? Thanks.

---

### Post #2 — **restrading** | 2023-04-08 15:31 UTC

I don’t use numerai-cli compute specifically and am a Google customer, but these docs might be relevant:

  * [Passing environment variables to a container - Amazon Elastic Container Service](<https://docs.aws.amazon.com/AmazonECS/latest/developerguide/taskdef-envfiles.html>)
  * [Using AWS Lambda environment variables - AWS Lambda](<https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars.html>)
