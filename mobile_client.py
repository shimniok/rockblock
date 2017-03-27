#!/usr/bin/env python

from gps3 import gps3
gps_socket = gps3.GPSDSocket()
ds = gps3.DataStream()
gps_socket.connect()
gps_socket.watch()
for new_data in gps_socket:
    if new_data:
        ds.unpack(new_data)
        print('Alt = ', ds.TPV['alt'])
        print('Lat = ', ds.TPV['lat'])
        print('Lon = ', ds.TPV['lon'])
        print('Speed = ', ds.TPV['speed'])
        print('Course = ', ds.TPV['track'])
        
