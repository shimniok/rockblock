#!/usr/bin/env python

import datetime
import cgi
import cgitb; cgitb.enable()  # for troubleshooting

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
    text = data.decode('hex')
    # TODO: parse out telemetry parameters & message (if any)

# Write to log
with open('rock.log', 'a') as mylog:
    mylog.write('%s,%s,%s,%s,%s,%s,%s,%s\n' %
        (datetime.datetime.now(), momsn, imei, transmit_time, iridium_latitude, iridium_longitude, iridium_cep, text ))

# Determine what to do with it

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
