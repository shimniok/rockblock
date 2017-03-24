#!/usr/bin/env python

print "Content-type: application/json"
print

import math
import cgi
#import cgitb; cgitb.enable()  # for troubleshooting
import json
import csv

result = [];

form = cgi.FieldStorage()
history = form.getvalue("history")
if history == None:
  maximum = 1
else:
  maximum = int(history)

# TODO: revise to use logfile and extended format

with open('./status.d', 'rb') as f:
  entries = list(csv.reader(f))
  # if specified history is > length of records, use length
  maximum = min(maximum, len(entries))
  # calculate how many entries to skip
  skip = len(entries) - maximum
  # print number of entries specified by history param
  for e in entries:
    if skip:
      skip -= 1
      continue
    result.append({
      'time': e[0],
      'emei': e[1],
      'id': e[2],
      'lat': e[3],
      'lng': e[4],
      'speed': e[5],
      'course': e[6],
      'msg': e[7]
    })
  
print json.dumps(result, sort_keys=True, indent=4)
    
