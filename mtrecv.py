#!/usr/bin/env python

##################################################################################################
## mtrecv.py
##
## Receive message via RockBLOCK over serial
##################################################################################################

import sys
import os
from rbControl import RockBlockControl

if __name__ == '__main__':
    if len(sys.argv) == 1:
        # TODO: configurable serial device
        RockBlockControl("/dev/ttyUSB0").mt_recv()
    else:
        print "usage: %s" % os.path.basename(sys.argv[0])
        exit(1)
