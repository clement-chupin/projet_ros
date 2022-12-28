#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Joy

def  callback(msg):
    print(msg.axes[0])
    print(msg.axes[1])
rospy.init_node('joy_node_listenner')
rospy.Subscriber("joy",Joy,callback,queue_size =10)
    
rospy.spin()
