#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

rospy.init_node('mon_premier_publisher')
rate = rospy.Rate(10)
pub = rospy.Publisher('/cmd_vel', Twist,queue_size=10)

while not rospy.is_shutdown():
    twist = Twist()
    twist.linear.x =1
    pub.publish(twist)
    rate.sleep()


