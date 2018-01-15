#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

rospy.init_node('robot_cleaner')

pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
rate = rospy.Rate(2)
count = Twist()

count.linear.x = 0.5
count.linear.y = 0
count.linear.z = 0
count.angular.x = 0
count.angular.y = 0
count.angular.z = 0

def callback(msg): 
   
  print msg.ranges[180]
  
  if(msg.ranges[180] < 1):
      count.linear.x = 0
      vel_pub(count)

def vel_pub(msg):
    pub.publish(msg)
 

while not rospy.is_shutdown(): 
  pub.publish(count)
 
  sub = rospy.Subscriber('/kobuki/laser/scan', LaserScan, callback)
  
  
  rate.sleep()
 




