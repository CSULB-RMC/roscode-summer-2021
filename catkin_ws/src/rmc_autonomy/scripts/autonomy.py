#!/usr/bin/env python

import rospy
from std_msgs.msg import Empty
from std_msgs.msg import Byte

dt_left_pub = rospy.Publisher('dt_left', Byte, queue_size=1)
dt_right_pub = rospy.Publisher('dt_right', Byte, queue_size=1)

dumper_up_pub = rospy.Publisher('dumper_up', Empty, queue_size=10)
dumper_down_pub = rospy.Publisher('dumper_down', Empty, queue_size=10)
stop_all_pub = rospy.Publisher('stop_all_arduino', Empty, queue_size=10)

test_led_pub = rospy.Publisher('test_led', Empty, queue_size=10)

auger_up_pub = rospy.Publisher('auger_up', Empty, queue_size=10)
auger_down_pub = rospy.Publisher('auger_down', Empty, queue_size=10)

auger_dig_pub = rospy.Publisher('auger_dig', Empty, queue_size=10)
auger_dig_rev_pub = rospy.Publisher('auger_dig_reverse', Empty, queue_size=10)

telescope_forward_pub = rospy.Publisher('telescope_forward', Empty, queue_size=10)
telescope_backward_pub = rospy.Publisher('telescope_backward', Empty, queue_size=10)

def stopMoving(event):
    stop_all_pub.publish()

def moveForward(event):
    dt_left_pub.publish(Byte(127))
    dt_right_pub.publish(Byte(127))
    rospy.Timer(rospy.Duration(10), stopMoving, oneshot=True)
    

if __name__=="__main__":
    rospy.init_node("rmc_autonomy")
    rospy.Timer(rospy.Duration(5), moveForward, oneshot=True)
    rospy.spin()