---
title: "Server Errors on Friday"
category: Tournament
url: https://forum.numer.ai/t/server-errors-on-friday/5883
created_at: 2022-11-25T13:34:11.973000+00:00
last_posted_at: 2022-11-28T02:03:56.192000+00:00
posts_count: 6
views: 995
tags: []
---

# Server Errors on Friday

---

### Post #1 — **liborty** | 2022-11-25 13:34 UTC

I am getting nothing but server errors today (Friday), when trying to download data with ‘numerapi’.

---

### Post #2 — **gammarat** | 2022-11-26 01:31 UTC

The competitions opened about half an hour late. That happens once in a while. If that was your problem, just put a loop in your script to check if the round is open, if not, wait 5 or 10 minutes and try again.

---

### Post #3 — **liborty** | 2022-11-26 09:41 UTC _(reply to #2)_

I have that already but after half an hour of failed attempts I thought the problem was perhaps in my script, so I turned the check off. My fault, I guess.

---

### Post #4 — **gammarat** | 2022-11-26 10:51 UTC _(reply to #3)_

Other things to check when there’s a problem like this:

  * The Tournament or Signals web page. If there’s no submission panel showing, then it usually means there’s a problem on the Numerai end.
  * The [support channel on the Chat](<https://rocketchat.numer.ai/channel/support>). Numerai generally puts up notices there about what’s wrong and how long before it’ll be working again pretty quickly after a failure. See @pshork’s comment there at 13:08 UTC.



On the bright side, they do say the round will always be open for a full hour, regardless of when it starts.

---

### Post #5 — **svendaj** | 2022-11-26 12:12 UTC _(reply to #2)_

Piece of code I have added to my script on Friday (while waiting for round openning):
    
    
    from numerapi import NumerAPI
    from time import sleep
    from datetime import datetime
    
    napi = NumerAPI(public_id="your_public_id", secret_key="your_secret_key")
    
    # wait until current round is open and get current_round number
    current_round = 0
    while current_round == 0:
        print("Waiting for openning of current round at", datetime.now())
        try:
            if napi.check_round_open():
                current_round = napi.get_current_round() 
            else:
                sleep(60)
            
        except:
            sleep(60)

---

### Post #6 — **liborty** | 2022-11-28 02:03 UTC

As I do not use Python, I have a Bash script:
    
    
    #!/bin/bash
    # Sets up cron checks for new numerai rounds TUE-FRI, from 13:05 UTC.
    # Local timezone is taken care of, as long as it is not sub-hourly.
    # Activate only once, verify with crontab -l, deactivate with crontab -r
    # Make sure that your computer and internet connection are on at the target time
    
    # days of the week to be checking for new tournaments - no spaces!
    FIRSTDAY=Tue
    LASTDAY=Sat
    # hours in UTC to be checking from
    HRS=13
    # at MINS minutes intervals after the initial attempt at $HRS:01
    MINS=5
    # name of bash script here that downloads live data, generates predictions and uploads them
    PREDICT=numbatch
    # full path/name of fully installed numerapi CLI (python) script
    NAPI=/home/l/.local/bin/numerapi
    # name of log file here 
    LOG=cronlog
    
    ############ no need to change anything below ###################
    
    # physical path/name of this script
    SCRIPT=$(realpath $0)
    # PREDICT script must be in the same directory as this script: $PD
    PD=$(dirname $SCRIPT)
    # crontab expects by default local time, so convert from UTC
    LHRS=`date -d "$HRS UTC" +%H`
    DAYS=`date -d "$HRS next $FIRSTDAY UTC" +%w`-`date -d "$HRS next $LASTDAY UTC" +%w`
    
    # no argument given means first time manual startup to initiate crontab
    # thereafter this script is invoked by cron with dummy argument 'r' to do actual processing
    [ $1 ] || {
        printf "1 $LHRS * * $DAYS $SCRIPT r >> $PD/$LOG\n" | crontab - && { 
            printf "$0: `date` crontab initiated:\n`crontab -l`\n" | tee -a $PD/$LOG
            exit 0
        } || {
            printf "$0: `date` crontab initiation failed!\n" | tee -a $PD/$LOG
            exit 2
        }
    }
    
    # Invoked by cron at the specified time 13:01 UTC
    while [ `"$NAPI" check-new-round --hours 1` != '1' ]; do 
        printf "$0: `date -u`: tournament has not yet started\n" 
        sleep "$MINS"m #sleep till tournament opens
    done
    # new tournament has started within the last hour, so download, predict, upload 
    printf "$0: `date -u`: new tournament has started!\n" 
    printf "$0: running $PD/$PREDICT\n" 
    $PD/$PREDICT >> $PD/$LOG 
    printf "$0: All done for today!\n" 
    exit 0
