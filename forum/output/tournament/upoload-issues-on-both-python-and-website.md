---
title: "Upoload issues on both python and website"
category: Tournament
url: https://forum.numer.ai/t/upoload-issues-on-both-python-and-website/2680
created_at: 2021-04-04T13:09:45.950000+00:00
last_posted_at: 2021-04-07T00:05:38.861000+00:00
posts_count: 6
views: 942
tags: []
---

# Upoload issues on both python and website

---

### Post #1 — **sarang** | 2021-04-04 13:09 UTC

Facing issues when trying to upload the predictions file.  
If i use the python , I am getting error “OverflowError: string longer than 2147483647 bytes”  
and if i directly to upload it is giving endpoint timeout error.

Can somebody help.

---

### Post #2 — **asteeber** | 2021-04-05 14:16 UTC

How is your predictions file formatted? Does it match the example predictions CSV?

---

### Post #3 — **minou** | 2021-04-05 16:49 UTC

Two things worth checking.

  1. File size. Is your predictions file in excess of 2GB? As a guide, my prediction files have 1687617 lines for round 258 and with ~16 dp precision and are around 60MB.

  2. What is your line break sequence? I’d normally use \n but use \r\n as I think that’s what the example file had. If manually writing the lines, mistakes such as accidentally escaping the `\`, using `/` instead or having no newline sequence at all would break import. If you’re on a Unix environment or have cygwin installed on Windows, you could do an `od -c` of the file to easily check.

---

### Post #4 — **sarang** | 2021-04-06 19:04 UTC _(reply to #3)_

I am using the correct break sequence but my file is coming to 2.3 GB .  
Am i doing something wrong at a very basic level ??

---

### Post #5 — **minou** | 2021-04-06 21:12 UTC _(reply to #4)_

The minimum submission would be a row with an id and a prediction corresponding to each id on rows marked as live in the tournaments file. There are 5431 rows for era 258. You can also include predictions for other rows, and these get scored and used to give model diagnostics. The start of a predictions might look like:
    
    
    id,prediction
    n0003aa52cab36c2,0.4365650630948831
    n000920ed083903f,0.38158981674726994
    n0038e640522c4a6,0.588572273950082
    

Check how the file is being created. It could even be that the file is being written to continuously and it only stopped when it reached a file size limit and your script bailed out.

---

### Post #6 — **sarang** | 2021-04-07 00:05 UTC _(reply to #5)_

Thank you for taking the time out to explain .There was a issue with my understanding and logic on file generation .It is now corrected
