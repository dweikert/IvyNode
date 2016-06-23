#!/usr/bin/python2
import rospy
from ivy.std_api import *
from std_msgs.msg import String
from geometry_msgs.msg import Pose2D
import time

Class Ivy_Calibration_Node:
    """Implements and Ivy Node for communication between ROS, the calibration
    Software and the ground network.

    """
    def IvyInitStart():
        """ Initializes the Ivy Server and ROS Subscriber

        Should only be called once per session.
        """
        IvyInit('Calibration Node', '', 0)
        IvyStart()
        initRosSub()
        time.sleep(1)
        print('Ivy Calibration Node ready!')

    def IvyGetPos():
        """Simply returns the position grabbed via ROS to the caller

        """
        return copterPos

    def IvySendParams(AC_ID, x, y, z):
        """Sends the given parameters via Ivy

        """
        #TODO implement correct messsage format
        IvySendMsg('%d DL %d %d %d' %
                    (AC_ID,
                    x,
                    y,
                    z))

    def IvyInitStop():
        """Stops the Ivy Server.

        """
        time.sleep(5)
        IvyStop()

    def handlePos(data):
        """ Callback for the ROS subscriber.


        """
        global copterPos
        copterPos=data


    def initRosSub():
        """ Initializes the ROS subscriber.

        Is automatically called during the Ivy initialization process
        in IvyInitStart().
        """
        rospy.init_node('poseListener', anonymous=False)
        rospy.Subscriber("pose", Pose2D, handlePos)
