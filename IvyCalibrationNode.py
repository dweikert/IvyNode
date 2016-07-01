#!/usr/bin/python2
import rospy
from std_api import *
from std_msgs.msg import String
from geometry_msgs.msg import Pose2D
import time

class Ivy_Calibration_Node:
    def IvyInitStart(self):
        """ Initializes the Ivy Server and ROS Subscriber

        Should only be called once per session.
        """


        try:
            IvyInit('Calibration Node', '', 0)
        except AssertionError:
            print('Assertion Error in IvyInit(!= none), is there a server already running? Exiting')
            IvyStop()
            raise SystemExit()

        print('asd')
        IvyStart()
        try:
            self.initRosSub()
        except rospy.exceptions.ROSInitException as e:
            print('\nInitialization failed due to ROS error, exiting...')
            self.IvyInitStop()

        time.sleep(1)
        print('Ivy Calibration Node ready!')



    def IvyInitStop(self):
        """Stops the Ivy Server.

        """
        time.sleep(1)
        IvyStop()

    def handlePos(data):
        """ Callback for the ROS subscriber.


        """
        global copterPos
        copterPos=data


    def initRosSub(self):
        """ Initializes the ROS subscriber.

        Is automatically called during the Ivy initialization process
        in IvyInitStart().
        """
        try:
            rospy.init_node('poseListener', anonymous=False)
        except KeyboardInterrupt:
            print('\nROS initialization canceled by user')
        except rospy.exceptions.ROSInitException as e:
            print('\nError Initializing ROS:')
            print(str(e))
            raise

        rospy.Subscriber("copters/0/pose", Pose2D, self.handlePos)




    def IvyGetPos(self):
        """Simply returns the position grabbed via ROS to the caller

        """
        try:
            return copterPos
        except NameError as e:
            print("CopterPos not yed defined! (No data from ROS?):")
            print(str(e))


    def IvySendCalib(self,AC_ID, param_ID, value):
        """Sends the given parameter via Ivy

        param_IDs:  phi   = 58
                    theta = 59
                    psi   = 60
        """

        IvySendMsg('dl DL_SETTING %d %d %f' %
                    (AC_ID,
                    param_ID,
                    value
                    ))
