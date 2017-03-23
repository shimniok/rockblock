#!/usr/bin/env python

import cgi
import cgitb; cgitb.enable()  # for troubleshooting
import json
import csv

result = [];

# TODO: revise to use logfile and extended format

with open('./status.d', 'rb') as f:
  entries = list(csv.reader(f))
  for e in entries:
    result.insert(0, {
      'time': e[0],
      'lat': e[1],
      'lng': e[2],
      'speed': e[3],
      'course': e[4],
      'msg': e[5]
    })
  
print "Content-type: application/json"
print
print json.dumps(result, sort_keys=True, indent=4)
