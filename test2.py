#!/usr/bin/env python

import requests
import time
url = 'http://nogales/rock/receive.py'

points = [ 
	{ 'lon': "-104.932838", 'lat': "39.597550", 'speed': 5, 'course': 12 },
	{ 'lon': "-104.932823", 'lat': "39.598514", 'speed': 5, 'course': 2 },
  { 'lon': "-104.932373", 'lat': "39.599715", 'speed': 5, 'course': 2 },
  { 'lon': "-104.932359", 'lat': "39.601095", 'speed': 5, 'course': 46 },
  { 'lon': "-104.930727", 'lat': "39.600900", 'speed': 5, 'course': 73 }
]

momsn = 0

for p in points:
	time.sleep(3)
	# split into integer/fractional parts
	lat = p['lat'].split('.')
	lon = p['lon'].split('.')
	# N decimal digits
	lat[1] = lat[1][:5]
	lon[1] = lon[1][:5]
	# put data back together, don't include '.' for lat/lon
	mydata = '%s%s,%s%s,%s,%s' % (lat[0], lat[1], lon[0], lon[1], p['speed'], p['course'])
	print mydata
	message = {
		'imei': '300234010753370',
		'momsn': '12345',
		'transmit_time': '12-10-10 10:41:50',
		'iridium_latitude': '%s.%s'%(lat[0], lat[1][:4]),
		'iridium_longitude': '%s.%s'%(lon[0], lon[1][:4]),
		'iridium_cep': '8',
		'data': mydata.encode('hex')
	}
	print message
	# POST with form-encoded data
	r = requests.post(url, data=message)
	# Response, status etc
	print r.text, r.status_code