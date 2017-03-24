#!/usr/bin/env python

## receive.py
##
## Expects post or get with parameters:
##
## imei : string
## momsn : string
## transmit_time : string
## iridium_latitude : string
## iridium_longitude : string
## iridium_cep : string
## data : hex-encoded string, format:
##      lat: string as [-]NNNNNNN (not padded; 5 decimal digits only, no '.')
##      lon: string as [-]NNNNNNNN (not padded; 5 decimal digits only, no '.')
##      speed: string as integer, not padded
##      course: string as integer, not padded

import datetime
import cgi
import cgitb; cgitb.enable()  # for troubleshooting

########################################################################
# parseGeo: adds decimal to unpadded 5 decimal digit number string
#
def parseGeo(g):
    r = list(g)
    r.reverse()
    r.insert(5, '.')
    r.reverse()
    s = ''.join(r)
    return s

########################################################################
# Main code

form = cgi.FieldStorage()

imei = form.getvalue("imei")
momsn = form.getvalue("momsn")
transmit_time= form.getvalue("transmit_time")
iridium_latitude= form.getvalue("iridium_latitude")
iridium_longitude= form.getvalue("iridium_longitude")
iridium_cep= form.getvalue("iridium_cep")
data = form.getvalue("data")
text = ''

# Decode the data
if (data != None):
    d = data.decode('hex').split(',')
    lat = parseGeo(d[0])
    lon = parseGeo(d[1])
    speed = d[2]
    course = d[3]

# Write status data
#with open('rock.log', 'a') as mylog:
#    mylog.write('%s,%s,%s,%s,%s,%s,%s,%s\n' %
#        (datetime.datetime.now(), momsn, imei, transmit_time, iridium_latitude, iridium_longitude, iridium_cep, text ))

print "Content-type: text/html"
print
print """
<html>
<head><title>RockBlock web service</title></head>
<body>
<p>Message submitted.</p>
</body>
</html>
"""

