---
title: "Automated submissions from bash shell script"
category: Tournament
url: https://forum.numer.ai/t/automated-submissions-from-bash-shell-script/5806
created_at: 2022-10-29T15:30:04.453000+00:00
last_posted_at: 2023-09-02T07:28:06.349000+00:00
posts_count: 6
views: 3065
tags: []
---

# Automated submissions from bash shell script

---

### Post #1 — **liborty** | 2022-10-29 15:30 UTC

Here is a bash script I have written which automates submissions to daily tournaments from home machines, without using `Compute` or web hooks or any other complications. If you want to learn to write similar scripts yourself, you may like to buy my e-book [Bash for Fun](<https://leanpub.com/bashforfun>)

Edit:

  1. Now an updated version that executes Tuesdays till Saturdays inclusive (can be changed).

  2. Simplified version that uses `sleep` instead of rewriting crontab.




It is assumed that your script does all else that is necessary: that is check for new validations and live data, download them when necessary, do the processing and send the predictions to the server.
    
    
    #!/bin/bash
    # Sets up cron checks for new numerai rounds TUE-FRI, from 13:01 UTC.
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
    while [ "$NAPI check-new-round --hours 1" != '1' ]; do 
        printf "$0: `date -u`: tournament has not yet started\n" 
        sleep "$MINS"m #sleep till tournament opens
    done
    # new tournament has started within the last hour, so download, predict, upload 
    printf "$0: `date -u`: new tournament has started!\n" 
    printf "$0: running $PD/$PREDICT\n" 
    $PD/$PREDICT >> $PD/$LOG 
    printf "$0: All done for today!\n" 
    exit 0

---

### Post #3 — **liborty** | 2023-01-27 13:19 UTC _(reply to #2)_

I have now also multithreaded my Rust back end and it runs like the wind

---

### Post #4 — **bridgeface** | 2023-02-07 16:21 UTC

Thank you for posting this. Trying to get this to work. I have a few questions.

PREDICT=numbatch # bash script in this directory that does all the dowloading, processing and uploading

**Is this my own .py script (model)?** Should I have a standalone python or can i reference utils?

NAPI=/home/l/.local/bin/numerapi # absolute path/name of fully installed numerapi CLI (python) script

**Is this the python package or my own .py script?**

Thank you sir.

---

### Post #6 — **bridgeface** | 2023-02-08 16:35 UTC _(reply to #5)_

Thank you very much. Fingers crossed. It appears to be properly set up.  


[![image](https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/c/c1113448127bddd515eee18a34bd2cdb345120db.png)image928×319 11.3 KB](<https://canada1.discourse-cdn.com/flex009/uploads/numerai/original/2X/c/c1113448127bddd515eee18a34bd2cdb345120db.png> "image")

---

### Post #7 — **liborty** | 2023-02-09 07:05 UTC

You are welcome. It works well for me.  
The problem I have are the unpredictable times of the tournament start.  
I could leave cron running and it would do it at the right time but  
it is around midnight here and I want to switch my big computer off and go to bed.  
If it at least was at the originally promised 13:00 UTC, it would not be so bad.

---

### Post #10 — **liborty** | 2023-09-02 07:28 UTC _(reply to #8)_

It has been a while, so here is my latest version with some improvements:
    
    
    #!/bin/bash
    # Sets up crontab that checks for and runs numerai tournaments. 
    # Local timezones are automatically taken care of.
    # `./cronrun d` sets up crontab for daily runs (Tue-Fri, 13:00 UTC).
    # `./cronrun w` sets up crontab for weekly runs (Saturdays, 18:00 UTC).
    # `./cronrun b` sets up crontab entries for both daily and weekly runs.
    # Can also be activated immediately manually, with `./cronrun daily` or 
    # `./cronrun weekly`, when crontab was not previously set up.
    # After the activation, will be waking up at the specified MINS intervals,
    # checking for new tournament and then running the processing script.
    # Tue-Fri runs script named `daily`,
    # on Saturdays runs script named `weekly`. 
    # Both `daily` and `weekly` scripts must be present in the same directory.
    # Activate only once, verify with `crontab -l`, cancel with `crontab -r`.
    # Your computer and internet connection must be on at the local target time.
    
    ########### Change these values to suit (no spaces around =) ##############
    FIRSTDAY=Tue
    LASTDAY=Fri
    HRS=13 # hours in UTC activations for daily tournament runs
    MINS=5 # initial delay and subsequent sleep intervals
    # absolute path/name of fully installed numerapi CLI (python) script
    NAPI=/home/l/.local/bin/numerapi 
    LOG=cronlog # main log file
    ERRLOG=errlog # logfile for numerapi errors
    
    ############ No need to change anything below here #########################
    SCRIPT=`realpath $0`
    PD=$(dirname $SCRIPT) # absolute path directory to this SCRIPT 
    [ "$1" == 'w' ] && let HRS=HRS+5 # weekend tournaments start 5 hours later
    LMINS=`date -d "$HRS:$MINS UTC" +%M`
    LHRS=`date -d "$HRS:$MINS UTC" +%H`
    LFDAY=`date -d "$HRS:$MINS next $FIRSTDAY UTC" +%w`
    LLDAY=`date -d "$HRS:$MINS next $LASTDAY UTC" +%w`
    SAT=`date -d "$HRS:$MINS next Sat UTC" +%w`
    
    # Manual invocation with `d` argument sets up crontab for daily runs (Tue-Fri).
    [ "$1" == 'd' ] && {
        printf "$LMINS $LHRS * * $LFDAY-$LLDAY $SCRIPT daily\n" | crontab - && { 
            printf "$0: `date` crontab set up:\n`crontab -l`\n" | tee -a $PD/$LOG
            exit 0
        } || {
            printf "$0: `date` crontab daily initiation failed!\n" | tee -a $PD/$LOG
            exit 2
        }
    }
    # Manual invocation with `w` argument sets up crontab for weekly runs (Saturdays).
    [ "$1" == 'w' ] && {
        printf "$LMINS $LHRS * * $SAT $SCRIPT weekly\n" | crontab - && { 
            printf "$0: `date` crontab set up:\n`crontab -l`\n" | tee -a $PD/$LOG
            exit 0
        } || {
            printf "$0: `date` crontab weekly initiation failed!\n" | tee -a $PD/$LOG
            exit 2
        }
    }
    # Manual invocation with `b` argument sets up crontab
    # entries for both daily and weekly runs.
    [ "$1" == 'b' ] && {
        DAILY="$LMINS $LHRS * * $LFDAY-$LLDAY $SCRIPT daily\n"
        let HRS=HRS+5
        LMINS=`date -d "$HRS:$MINS UTC" +%M`
        LHRS=`date -d "$HRS:$MINS UTC" +%H`
        SAT=`date -d "$HRS:$MINS next Sat UTC" +%w`
        printf "$DAILY$LMINS $LHRS * * $SAT $SCRIPT weekly\n" | crontab - && { 
            printf "$0: `date` crontab set up:\n`crontab -l`\n" | tee -a $PD/$LOG
            exit 0
        } || {
            printf "$0: `date` crontab initiations failed!\n" | tee -a $PD/$LOG
            exit 2
        }
    }
    # Arguments `daily` or `weekly` are used by automatic cron activations
    [ "$1" == 'daily' ] || [ "$1" == 'weekly' ] || {
        printf "$0: `date` crontab argument $1 not recognised!\n" | tee -a $PD/$LOG
        exit 2
    }
    [ -f "$PD/$1" ] || {
        printf "$0: `date` crontab: script $PD/$1 not found!\n" | tee -a $PD/$LOG
        exit 2
    }
    while :; do
        NRES=`$NAPI check-new-round` 2>$PD/$ERRLOG
        # numerapi status is valid and the new tournament has started
        [ $? ] && [  "$NRES" == '1' ] && { 
            printf "$0: `date -u`: new tournament has started!\n" | tee -a $PD/$LOG
            printf "$0: running $PD/$1\n" | tee -a $PD/$LOG
            $PD/$1 | tee -a $PD/$LOG  # download, predict, upload 
            printf "$0: All done for today!\n" | tee -a $PD/$LOG
            exit 0
        }
        printf "$0: `date -u`: tournament has not yet started, sleeping for $MINS minutes\n" | tee -a $PD/$LOG
        sleep "$MINS"m  
    done
