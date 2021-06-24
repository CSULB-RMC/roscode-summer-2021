#!/usr/bin/env python

import rospy
from std_msgs.msg import Empty
from std_msgs.msg import Byte

from sensor_msgs.msg import Joy

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

def joyCallback(data):
	#rospy.loginfo(rospy.loginfo(rospy.get_caller_id() + "JOY CALLBACK! %s", data))

	# Y/A button 
	if data.buttons[2] == 1: #Y - dumper up
		dumper_up_pub.publish()
	if data.buttons[0] == 1: #A - dumper down
		dumper_down_pub.publish()

	if data.buttons[8] == 1: #back button is emergency stop everything
		stop_all_pub.publish()

	if data.buttons[9] == 1: #start button - toggle led
		test_led_pub.publish()


	rospy.loginfo(rospy.loginfo(rospy.get_caller_id() + " CALLING DT " + str(data.axes[1]*64) + "\n"))

	curbed = int(64+(data.axes[1]*64))
	if curbed > 127:
		curbed = 127

	dt_left_pub.publish(Byte(curbed))


	curbed = int(64+(data.axes[3]*64))
	if curbed > 127:
		curbed = 127

	dt_right_pub.publish(Byte(curbed))

	if data.buttons[1] == 1:
		rospy.loginfo(rospy.loginfo("OOOO TESTING\n"))
		auger_up_pub.publish()

	if data.buttons[3] == 1:
		auger_down_pub.publish()

	if data.buttons[4] == 1:
		telescope_forward_pub.publish()

	if data.buttons[5] == 1:
		telescope_backward_pub.publish()

	if data.buttons[6] == 1:
		auger_dig_pub.publish()

	if data.buttons[7] == 1:
		auger_dig_rev_pub.publish()

if __name__=="__main__":
	rospy.init_node("rmc_teleop")
	rospy.Subscriber("joy". Joy, joyCallback)