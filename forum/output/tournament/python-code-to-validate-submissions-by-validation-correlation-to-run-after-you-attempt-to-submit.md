---
title: "Python code to validate submissions by validation correlation to run after you attempt to submit"
category: Tournament
url: https://forum.numer.ai/t/python-code-to-validate-submissions-by-validation-correlation-to-run-after-you-attempt-to-submit/3062
created_at: 2021-04-25T15:34:01.881000+00:00
last_posted_at: 2021-04-25T15:34:01.974000+00:00
posts_count: 1
views: 669
tags: []
---

# Python code to validate submissions by validation correlation to run after you attempt to submit

---

### Post #1 — **bensch** | 2021-04-25 15:34 UTC

[github.com](<https://github.com/benschreyer/NumeraiScripts/blob/main/verify_by_val_corr.py>)

#### [benschreyer/NumeraiScripts/blob/main/verify_by_val_corr.py](<https://github.com/benschreyer/NumeraiScripts/blob/main/verify_by_val_corr.py>)
    
    
    #Bensch 4/20/21
    #Script to check validation correlation of a list of Numer.ai models and print whether or not they changed from the previous round to the current
    import requests
    
    
    
    def getAccountValidations(name):
        req = requests.get("https://api-tournament.numer.ai/?query={userActivities(username:\""+name+"\",tournament:8){submission {validationCorrelation } } } ").json()
        return (req["data"]["userActivities"][1]["submission"]["validationCorrelation"],req["data"]["userActivities"][0]["submission"]["validationCorrelation"])
    
    accounts = ["bensch","bensch_a"]
    
    for account in accounts:
        get = getAccountValidations(account)
        #print(get)
        prev = get[0]
        curr = get[1]
        if(curr == prev):
            print(account+ " UNCHANGED " + str(prev))
        else:
    

This file has been truncated. [show original](<https://github.com/benschreyer/NumeraiScripts/blob/main/verify_by_val_corr.py>)

This could be useful to anyone that wants to check their underlying model didn’t change week to week for some unexpected reason by getting the validation correlations of the model for the two latest rounds and checking if they match. Note this has the blocking line input() at the end since I run it after all my other scripts when I do submissions locally.
