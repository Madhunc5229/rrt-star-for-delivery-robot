# rrt-star-for-delivery-robot

In this project, RRT* star algorithm has been implemeted for path planning for a mobile delivery robot to deliver to multiple locations in a efficient way.

## Dependencies
-   Python
-   Gazebo
-   ROS
-   Opencv 4.1.0
-   Numpy

## Steps to run the package
1.Navigate to the source folder of your catkin workspace and clone the package
  
    cd catkin_ws/src
    git clone https://github.com/Madhunc5229/rrt-star-for-delivery-robot
2.Build the package and source it

    cd ..
    cd catkin build
    source ~/catkin_ws/devel/setup.bash 

3.Launch the algorithm:
    
    roslaunch rrt rrt_start.launch

4.For OpenCV simulation only run:
  
    rosrun rrt rrt_star_algorithm
    
5.For OpenCV & Turtlebot simulation run:
  
    rosrun rrt rrt_star_algorithm_turtlebot
