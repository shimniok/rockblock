# RockBlock Tracking System

A RockBlock web service to receive messages, a javascript / Google Maps
tracking and messaging interface, and a mobile client.

Written in Python for Linux (including Raspberry Pi), tested on Linux
Mint 17.3

## Cloning
You'll need to run the following commands to populate the pyRockBlock
submodule:

```
git submodule init
git submodule update
```

## Message Format
The data portion of the RockBlock message is csv formatted:
lat,lon,speed,course,text

where:
 * lat, lon: are in decimal format, fixed to 6 decimal digits, no '.'
 * speed, course: integers,
 * text: arbitrary string

## Installation

 * Install the files in a subdirectory accessible to your web server
 * config.py references the data file location (e.g., data/status.d).
 * Create the data file (and directory if necessary), make it writeable
by the httpd user (typically www-data)
 * Obtain a Google Maps API key
 * Edit the map.html and put your key after *key=* and before *&callback*
removing any key that may be there

## Background

MO = Mobile Originated
MT = Mobile Terminated

Messages sent TO the RockBlock from home base are MT messages. Messages
send from the RockBlock to home base are MO messages.

## Files

* base/		       -- Base station app and api
* base/data/           -- data files (status and messages)
*   messages.d	       -- message database
*   status.d           -- telemetry database
*   images/	       -- base app image files
*   config.py          -- configuration for base api/app
*   config.py.template -- configuration template (copy to config.py, edit)
*   map.css            -- Style sheet for Map/Txt web page
*   index.html         -- Map/Txt web page
*   map.js             -- Implements tracking and messaging
*   messages.py        -- REST web service that lists recent messages
*   receive.py         -- Implements GCI web service called by Rock's servers
*   status.py          -- REST web service to return current status
* mobile_client.py     -- Mobile-side: client app for sending position and text chat
* mosend.py            -- Mobile-side: Send message to home via RockBlock over serial
* mtrecv.py*           -- Mobile-side: Receive message from home via RockBlock over serial
* mtstub.py*           -- Mobile-side: Emulates rockblock api for testing without burning credits
* rockBlock.py	       -- Mobile-side: Library for communicating with RockBLOCK
* rbControl.py*        -- Mobile-side: Library for sending/receiving, uses rockBlock.py
* send.py*             -- Mobile-side: Sends message by calling Rock API
