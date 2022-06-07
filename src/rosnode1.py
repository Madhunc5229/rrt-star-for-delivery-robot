#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
import time
import math
import numpy as np


def send_vel(path, radius, w_dist, step):

    rospy.init_node('robot_talker', anonymous=True)
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    msg = Twist()
    dir = [1, 0]

    for i in range(1, len(path)):
        new_dir = [path[i][0] - path[i-1][0], path[i][1] - path[i-1][1]]
        th = math.atan2(((new_dir[0] * dir[1]) - (new_dir[1] * dir[0]))
                       , (new_dir[0]*dir[0]) + (new_dir[1]*dir[1]))

        th = -round(th * 180/3.14)
        dist = round(np.linalg.norm(np.array(path[i])- np.array(path[i-1])))/3
        # dist = round(math.dist(path[i], path[i-1]))
        print('goint to point: ', path[i])
        cnt = 0
        while cnt < abs(th*1.9):
            cnt += 1
            if th < 0:
                ang_v = -0.105
            else:
                ang_v = 0.105
            publishMsg(msg, 0, ang_v, pub)
        cnt = 0
        while cnt < dist*10:
            cnt += 1
            lin_v = 0.1
            publishMsg(msg, lin_v, 0, pub)
        publishMsg(msg, 0, 0, pub)
        dir = new_dir
    return True


def publishMsg(msg, lin_v, ang_v, pub):

    msg.angular.z = ang_v
    msg.angular.x = 0
    msg.angular.y = 0
    msg.linear.x = lin_v
    msg.linear.y = 0
    msg.linear.z = 0
    pub.publish(msg)
    time.sleep(0.1)