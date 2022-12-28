#!/usr/bin/env python
import rospy

from sensor_msgs.msg import Range
from geometry_msgs.msg import Twist

rospy.init_node('control_robot')
rate = rospy.Rate(10)
pub = rospy.Publisher('/cmd_vel', Twist,queue_size=10)



capF = 0
capLF = 0
capLB = 0
capRF = 0
capRB = 0
seuilSonar = 0.2


def sendMove(x_,z_):
    twist = Twist()
    twist.linear.x = x_
    twist.angular.z = z_
    pub.publish(twist)
    rate.sleep()
def makeDesision():
    if capF > seuilSonar:
        sendMove(1,0)
    else:
        sendMove(0,1)

def  callback(msg):
    global direction
    #print(msg)
    sonar = 0
    if msg.header.frame_id == "SonarFront_frame":
        capF = 0.9*capF + msg.range
    if msg.header.frame_id == "SonarLeftFront_frame":
        capLF = 0.9*capLF + msg.range
    if msg.header.frame_id == "SonarRightFront_frame":
        capRF= 0.9*capRF + msg.range
    if msg.header.frame_id == "SonarLeftBack_frame":
        capLB = 0.9*capLB + msg.range
    if msg.header.frame_id == "SonarRightBack_frame":
        capRB = 0.9*capRB + msg.range

           
    # twist = Twist()
    # twist.linear.x = 0
    # twist.angular.z = 0
    
    
    
    # if sonar ==1:
    #     if msg.range > 0.3:
    #         print("up")
    #         twist.linear.x = 1
    #     else:
    #         print("evitement")
    #         if(direction==1):
    #             print("evitement dir 1")
    #             twist.angular.z = 1 #droite
    #         else:
    #             print("evitement dir 2")
    #             twist.angular.z = -1
            
    # if sonar ==2 and msg.range > 0.5:
    #     print("sonar 2 dir 1")
    #     direction = 1

    # if sonar ==3 and msg.range > 0.5:
    #     direction = 2
    #     print("sonar 3 dir 2")
        
    # pub.publish(twist)
    # rate.sleep()


rospy.Subscriber("/mobile_robot/sonar_front",Range,callback,queue_size =10)

rospy.Subscriber("/mobile_robot/sonar_left_front",Range,callback,queue_size =10)
rospy.Subscriber("/mobile_robot/sonar_right_front",Range,callback,queue_size =10)

rospy.Subscriber("/mobile_robot/sonar_left_back",Range,callback,queue_size =10)
rospy.Subscriber("/mobile_robot/sonar_right_back",Range,callback,queue_size =10)

rospy.spin()


