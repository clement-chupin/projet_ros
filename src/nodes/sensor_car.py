#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import LaserScan,Range
from geometry_msgs.msg import Twist

class Controlleur:
    def callback_front(self,data):
        self.range_front = data.range
    def callback_right(self,data):
        self.range_right = data.range
    def callback_left(self,data):
        self.range_left = data.range

    
    def move_test(self):
        # Create a publisher which can "talk" to Turtlesim and tell it to move
        pub = rospy.Publisher(str('/robot_'+str(self.robot_index)+'/cmd_vel'), Twist, queue_size=1)

        move_cmd = Twist()
        rate = rospy.Rate(1)

        while True:
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

            rate.sleep()


    def __init__(self):
        self.range_front =0
        self.range_right =0
        self.range_left =0
        
        

        rospy.init_node("control_the_bot", anonymous=True)

        self.node_name = rospy.get_name()

        self.robot_index = rospy.get_param(self.node_name+"/robot_index")


        rospy.Subscriber('/sensor_'+str(self.robot_index)+'/front_ir_front', Range, self.callback_front)
        rospy.Subscriber('/sensor_'+str(self.robot_index)+'/left_ir_front', Range, self.callback_left)
        rospy.Subscriber('/sensor_'+str(self.robot_index)+'/right_ir_front', Range, self.callback_right)
        self.move_test()
        rospy.spin()


contro = Controlleur()
