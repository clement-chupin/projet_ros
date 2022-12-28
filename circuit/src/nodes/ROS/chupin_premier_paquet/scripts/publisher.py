#!/usr/bin/env python
import rospy
from std_msgs.msg import String
rospy.init_node('mon_premier_publisher')
pub = rospy.Publisher('topic1',String,queue_size=10) 
rate = rospy.Rate(10)
while not rospy.is_shutdown():
    msg = String()
    msg.data = "hello world "
    pub.publish(msg)
    rate.sleep()
