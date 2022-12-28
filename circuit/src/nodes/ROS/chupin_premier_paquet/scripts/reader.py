#!/usr/bin/env python
import rospy
from std_msgs.msg import String
def  callback(msg):
    print(msg.data)
rospy.init_node('my_noeud_subscriber')
rospy.Subscriber("topic1",String,callback,queue_size =10)
    
rospy.spin()
