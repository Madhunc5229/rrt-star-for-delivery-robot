#!/usr/bin/env python3
import actionlib
import rospy
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal, MoveBaseFeedback, MoveBaseResult

def moveBaseNav(goal_point):


    rospy.init_node('send_client_goal')

    client = actionlib.SimpleActionClient('/move_base', MoveBaseAction)
    rospy.loginfo("Waiting for move base server")
    client.wait_for_server()

    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = 'map' 
    goal.target_pose.pose.position.x = (goal_point[0]/30)-10
    goal.target_pose.pose.position.y = (goal_point[1]/30)-1
    # goal.target_pose.pose.orientation.z = 0.0
    goal.target_pose.pose.orientation.w = 0.5

    client.send_goal(goal)
    rospy.loginfo("goal sent")
    client.wait_for_result()
    
# print(client.wait_for_result())


# goal.target_pose.header.frame_id = 'map' 
# goal.target_pose.pose.position.x = new value
# goal.target_pose.pose.position.y = new value
# goal.target_pose.pose.orientation.z = new value
# goal.target_pose.pose.orientation.w = new value

# client.send_goal(goal)
# client.wait_for_result()
