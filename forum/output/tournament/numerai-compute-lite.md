---
title: "Numerai Compute Lite"
category: Tournament
url: https://forum.numer.ai/t/numerai-compute-lite/6204
created_at: 2023-03-05T16:20:20.349000+00:00
last_posted_at: 2023-03-05T21:49:00.442000+00:00
posts_count: 2
views: 630
tags: []
---

# Numerai Compute Lite

---

### Post #1 — **bridgeface** | 2023-03-05 16:20 UTC

Anybody have this issue with compute lite?  
**ValueError: Insufficient permission for read_user_info**

looks like a file permission issue, but I don’t know which file??

* * *

starting docker build  
…  
Build complete, status = SUCCEEDED  
Logs at <https://console.aws.amazon.com/cloudwatch/home?region=us-west-2#logEvent:group=/aws/codebuild/build-numerai-compute-lambda-image;stream=d3e52309-2ce1-4551-b36b-4801a832fd87>

2023-03-05 10:14:12,158 ERROR numerapi.base_api: Insufficient permission for read_user_info

* * *

ValueError Traceback (most recent call last)  
/tmp/ipykernel_115729/3635924747.py in   
6 os.environ[‘AWS_SECRET_ACCESS_KEY’] = ‘ieQ1kb3yNuN4W5ItoRhJ3d3/j/vYWDm4s6L9tM1+’  
7 model_id = model  
\----> 8 napi.deploy(model_id, model, napi.feature_sets(‘small’), ‘requirements.txt’, data_version=‘v2’)

~/anaconda3/lib/python3.10/site-packages/numerapi/numerapi.py in deploy(self, model_id, model, features, requirements_path, data_version, model_pipeline, custom_pipeline_path)  
1170 }}  
1171 ‘’’  
→ 1172 resp = self.raw_query(query, authorization=True)  
1173 model_name = resp[‘data’][‘model’][‘name’]  
1174 lambda_role_arn, lambda_function_name = compute_utils.maybe_create_lambda_function(model_name, ecr, bucket_name, aws_account_id, model_id, external_id)

~/anaconda3/lib/python3.10/site-packages/numerapi/base_api.py in raw_query(self, query, variables, authorization, retries, delay, backoff)  
128 err = self._handle_call_error(result[‘errors’])  
129 # fail!  
→ 130 raise ValueError(err)  
131 return result  
132

**ValueError: Insufficient permission for read_user_info**

---

### Post #2 — **bridgeface** | 2023-03-05 21:49 UTC

Nevermind. Found the fix on the chat.
