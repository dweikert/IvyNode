#!/usr/bin/env python

import time
from thread import start_new_thread
from IvyCalibrationNode import *
from std_api import *

x=Ivy_Calibration_Node()
x.IvyInitStart()

#dostuff
x.IvySendCalib(5,58,0.5)
time.sleep(1)
#domorestuff
x.IvySendCalib(5,59,0.7)
time.sleep(1)
x.IvySendCalib(5,60,0.9)
x.IvyGetPos()
x.IvyInitStop()
