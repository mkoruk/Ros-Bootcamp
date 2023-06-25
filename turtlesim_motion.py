#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
pi=3.14

def move():
        
    rospy.init_node('turtlesim_motion', anonymous=True)
    pub=rospy.Publisher("/turtle1/cmd_vel",Twist,queue_size=10)
    vel_obj=Twist()

    rospy.loginfo("Enter speed:")
    linear_x=int(input())
    rospy.loginfo("Enter yaw angle:")
    angle=int(input())
    angle_in_radian=(pi*angle)/180
    forward=str(input("Forward (f) or backward(b)?"))
    try:
        if forward=='f':
            vel_obj.linear.x=abs(linear_x)
        if forward=='b':
            vel_obj.linear.x=-abs(linear_x)
    except ValueError:
        print("Invalid input!")

    vel_obj.linear.y=0
    vel_obj.linear.z=0
    vel_obj.angular.x=0
    vel_obj.angular.y=0
    vel_obj.angular.z=angle_in_radian
    pub.publish(vel_obj)

if __name__ == '__main__':
    try:
        while not rospy.is_shutdown():
            move()
    except rospy.ROSInterruptException:
        pass