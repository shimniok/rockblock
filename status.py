#!/usr/bin/env python

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
  # print number of entries specified by history param
  i = 0
  for e in entries:
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
    i += 1
    if i >= maximum:
      break
  
print "Content-type: application/json"
print
print json.dumps(result, sort_keys=True, indent=4)
