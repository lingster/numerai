---
title: "Payouts as USD (Unofficial improvement implemented)"
category: Feedback
url: https://forum.numer.ai/t/payouts-as-usd-unofficial-improvement-implemented/5074
created_at: 2022-03-13T22:02:02.621000+00:00
last_posted_at: 2023-03-29T20:21:21.341000+00:00
posts_count: 7
views: 1749
tags: []
---

# Payouts as USD (Unofficial improvement implemented)

---

### Post #1 — **wigglemuse** | 2022-03-13 22:02 UTC

Hello,

I’m posting this in “Feedback” even though it really isn’t – there is (shockingly) no “general” category on this forum. This is an unofficial response to feedback I’ve heard though.

Do you want those mouseover tooltips on the website to show the USD equivalent of your payouts again instead of NMR with a million digits? Of course you do, but discreetly, privately, unofficially! (Numerai can no longer have this as part of the actual website for regulatory reasons, apparently.)

Well, install the Violentmonkey or Tampermonkey extension for your browser (I prefer the former as it is open-source and doesn’t do any funny business but either will work the same) and then pop this script in there:
    
    
    // ==UserScript==
    // @name					numerai_sitetweak
    // @namespace			wigglemuse.numerai
    // @description		tweaks the numerai website (currently only changes those NMR payout mouseover tooltips to USD)
    // @match				  https://numer.ai/*
    // @match				  https://signals.numer.ai/*
    // @noframes
    // @author        wigglemuse
    // @version				1.0
    // ==/UserScript==
    
    
    
    
    var nmrusd = 0;
      
    var appdiv = document.querySelector("#app");
    
    var mutationObserver = new MutationObserver(function(mutations) {
    
      if(!nmrusd) {
        nmrusd = document.querySelector("a[href*='coinmarketcap.com']");
        if(!nmrusd) { 
          return; 
        }
        nmrusd = nmrusd.textContent.match(/1 NMR ≈ \$([0-9\.]+)/)[1];
        console.log("NMR/USD: " + nmrusd);
      }
    
    
      let tooltips = document.querySelectorAll("#app > div.v-tooltip__content span");
      for (let i=0;i<tooltips.length;i++) {
        let tt = tooltips[i].textContent.match(/^(-?[0-9\.]+|null)\s+NMR$/);
        if(tt) {
          tt = tt[1];
          if(tt == "null" || tt == "0") {
            tt = "$0";
          } else {
            tt = Math.sign(tt)<0?"($" + (Math.abs(tt) * nmrusd).toFixed(2) + ")":"$" + (tt * nmrusd).toFixed(2);      
          }
          tooltips[i].textContent = tt;
        }
      }    
    
    });
    
    mutationObserver.observe(appdiv, {
      childList: true,
      subtree: true  
    });
    
    

So you just hit the New Script (+) button (plain “New” on the menu in Violentmonkey), it will bring up a template for a script in the editor – erase what’s there and replace it with the above code. Save, and make sure both the script and the extension are enabled (each can be turned off/on) and there you go.

---

### Post #2 — **aventurine** | 2022-03-13 23:18 UTC

Amazing! Works perfect. Thanks for this. How much time did this take you to research and put together?

---

### Post #3 — **wigglemuse** | 2022-03-13 23:23 UTC

Oh, an hour or so. There’s other tweaks I can add, but I know people wanted that one so there’s a start. It could probably do other currencies but with USD all the information is part of the page already so that was easy. (Anything else would need to call some API, etc etc)

---

### Post #4 — **aventurine** | 2022-03-18 01:46 UTC _(reply to #3)_

Hey we want to send you 1.81 NMR as a retroactive bounty for this. If you DM me a wallet I can initiate the multisig transaction

---

### Post #5 — **ssh** | 2022-04-01 15:28 UTC

[@wigglemuse](</u/wigglemuse>) thx for usefull tweak!  
hope you don’t mind a few minor updates:

  * spaces within big numeric values (thousands and hopefully millions for some future NMR whales)
  * changed to “-” sign instead of round brackets for negative values


    
    
    // ==UserScript==
    // @name					numerai_sitetweak
    // @namespace			wigglemuse.numerai
    // @description		tweaks the numerai website (currently only changes those NMR payout mouseover tooltips to USD)
    // @match				  https://numer.ai/*
    // @match				  https://signals.numer.ai/*
    // @noframes
    // @author        wigglemuse
    // @version				1.1
    // ==/UserScript==
    
    
    function numberWithSpaces(x) {
        var parts = x.toString().split(".");
        parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, " ");
        return parts.join(".");
    }
    
    var nmrusd = 0;
      
    var appdiv = document.querySelector("#app");
    
    var mutationObserver = new MutationObserver(function(mutations) {
    
      if(!nmrusd) {
        nmrusd = document.querySelector("a[href*='coinmarketcap.com']");
        if(!nmrusd) { 
          return; 
        }
        nmrusd = nmrusd.textContent.match(/1 NMR ≈ \$([0-9\.]+)/)[1];
        console.log("NMR/USD: " + nmrusd);
      }
    
    
      let tooltips = document.querySelectorAll("#app > div.v-tooltip__content span");
      for (let i=0;i<tooltips.length;i++) {
        let tt = tooltips[i].textContent.match(/^(-?[0-9\.]+|null)\s+NMR$/);
        if(tt) {
          tt = tt[1];
          if(tt == "null" || tt == "0") {
            tt = "$0";
          } else {
            tt = Math.sign(tt)<0?"-$" + numberWithSpaces((Math.abs(tt) * nmrusd).toFixed(2)) :"$" + numberWithSpaces((tt * nmrusd).toFixed(2));      
          }
          tooltips[i].textContent = tt;
        }
      }    
    
    });
    
    mutationObserver.observe(appdiv, {
      childList: true,
      subtree: true  
    });

---

### Post #6 — **wigglemuse** | 2022-04-04 16:14 UTC _(reply to #5)_

Cool. I didn’t bother with much formatting because it was just a pop-up (and I have plans for other tweaks and just wanted to get this out there first). I did code it with the negative sign at first, and I just didn’t like the way it looked. I think it needs to be red maybe – I thought the parentheses as used in accounting was a more prominent visual signal.

---

### Post #7 — **wigglemuse** | 2023-03-29 20:21 UTC

Needs a tiny fix for recent site changes:

change “span” to “div” in the line:
    
    
      let tooltips = document.querySelectorAll("#app > div.v-tooltip__content span");
    

should now be:
    
    
      let tooltips = document.querySelectorAll("#app > div.v-tooltip__content div");
