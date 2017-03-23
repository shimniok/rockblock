#!/usr/bin/env python

import cgi
#import cgitb; cgitb.enable()  # for troubleshooting
import json
import csv

result = [];

form = cgi.FieldStorage()
history = form.getvalue("history")

# TODO: revise to use logfile and extended format

with open('./status.d', 'rb') as f:
  entries = list(csv.reader(f))
  
  if history == None:
    # current entry only
    e = entries[len(entries)-1];
    result.append({
      'time': e[0],
      'lat': e[1],
      'lng': e[2],
      'speed': e[3],
      'course': e[4],
      'msg': e[5]
    })
  elif history > 0:
    # print number of entries specified by history param
    maximum = int(history)
    i = 0
    for e in reversed(entries):
      result.append({
        'time': e[0],
        'lat': e[1],
        'lng': e[2],
        'speed': e[3],
        'course': e[4],
        'msg': e[5]
      })
      i += 1
      if i >= maximum:
        break
    # insert actual number of entries
    result.insert(0, i)
  
print "Content-type: application/json"
print
print json.dumps(result, sort_keys=True, indent=4)
