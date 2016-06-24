#!/usr/bin/env python

import time
from thread import start_new_thread
from Ivy_Calibration_Node import *
from ivy.std_api import *

IvyInitStart()
IvyTest()
pose = IvyGetPos()
#dostuff
IvySendParams(pose.x,pose.y,pose.theta,0)
time.sleep(2)
#domorestuff
pose = IvyGetPos()
IvySendParams(pose.x,pose.y,pose.theta,0)
IvyStop()
