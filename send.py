#!/usr/bin/env python

import datetime
import cgi
import cgitb; cgitb.enable()  # for troubleshooting

url="https://core.rock7.com/rockblock/MT"

form = cgi.FieldStorage()
message = form.getvalue("message")

# Put in config.py
imei = ""
username = ""
password = ""

# convert message to hex-encoded data

# call remote url

# log message, time & status in msgs.d

# OK,12345678 <-- messageid
# FAILED,errorcode#,Textual description of failure
# Error Code # / Textual description
# 10 Invalid login credentials
# 11 No RockBLOCK with this IMEI found on your account
# 12 RockBLOCK has no line rental
# 13 Your account has insufficient credit
# 14 Could not decode hex data
# 15 Data too long
# 16 No data
# 99 System error
