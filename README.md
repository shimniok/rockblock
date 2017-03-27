# RockBlock Tracking System

A RockBlock web service to receive messages, a javascript / Google Maps
tracking and messaging interface, and a mobile client.

Written in Python for Linux (including Raspberry Pi), tested on Linux
Mint 17.3

## Message Format
The data portion of the RockBlock message is csv formatted:
lat,lon,speed,course,text

where:
 * lat, lon: are in decimal format, fixed to 6 decimal digits, no '.'
 * speed, course: integers,
 * text: arbitrary string

## Installation
 
 * config.py references the data file location (e.g., data/status.d). 
 * Create the data file (and directory if necessary), make it writeable
by the httpd user (typically www-data)
 * Obtain a Google Maps API key
 * Edit the map.html and put your key after *key=* and before *&callback*
removing any key that may be there
