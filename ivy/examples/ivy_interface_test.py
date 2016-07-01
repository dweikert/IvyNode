#!/usr/bin/env python

import time
from thread import start_new_thread
from Ivy_Calibration_Node import *
from ivy.std_api import *

IvyInitStart()


#dostuff
IvySendCalib(5,58,0.5)
time.sleep(2)
#domorestuff
IvySendCalib(5,59,0.7)
time.sleep(2)
IvySendCalib(5,60,0.9)
IvyStop()
