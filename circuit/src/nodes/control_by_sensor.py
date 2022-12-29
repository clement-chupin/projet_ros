#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import LaserScan,Range
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Image


from circuit.srv import StartRaceResponse,StartRace
import numpy as np
class Controlleur:
    def callback_front(self,data):
        self.range_front = data.range
    def callback_right(self,data):
        self.range_right = data.range
    def callback_left(self,data):
        self.range_left = data.range


    def call_service(self,):

        savoir_si_la_course_commence = rospy.ServiceProxy("/circuit/start_the_race",StartRace)
        resp = savoir_si_la_course_commence()


        self.start = resp.result
 

    def move_test(self):
        # Create a publisher which can "talk" to Turtlesim and tell it to move
        pub = rospy.Publisher(str('/robot_'+str(self.robot_index)+'/cmd_vel'), Twist, queue_size=1)

        move_cmd = Twist()
        rate = rospy.Rate(1)

        while True:
            print(self.start)
            if self.start:
                move_cmd.angular.z = 0
                move_cmd.linear.x = 0
                if self.range_right > self.range_left and self.range_right-self.range_left > 0.3:
                    move_cmd.angular.z = 0.8
                if self.range_left > self.range_right and self.range_left-self.range_right > 0.3:
                    move_cmd.angular.z = -0.8
                if self.range_front > 0.5:
                    move_cmd.linear.x = 0.4


                print("sensor :")
                print(self.range_right,self.range_left)
                print("move :")

                print(move_cmd.linear.x,move_cmd.angular.z)
                
                pub.publish(move_cmd)
            self.call_service()
            rate.sleep()


    def __init__(self):
        self.range_front =0
        self.range_right =0
        self.range_left =0
        self.start = True
        

        rospy.init_node("control_by_sensor", anonymous=True)

        self.node_name = rospy.get_name()

        self.robot_index = rospy.get_param(self.node_name+"/robot_index")
  
        rospy.Subscriber('/robot_'+str(self.robot_index)+'/sensor_front_ir', Range, self.callback_front)
        rospy.Subscriber('/robot_'+str(self.robot_index)+'/sensor_left_ir', Range, self.callback_left)
        rospy.Subscriber('/robot_'+str(self.robot_index)+'/sensor_right_ir', Range, self.callback_right)
        # rospy.Subscriber("/camera/rgb/image_raw", Image, image_callback)


        self.move_test()
        
        rospy.spin()


contro = Controlleur()




#<!---->""