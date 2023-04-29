# AprilTagを使いたいとき
1. ~/catkin_ws/srcにapriltag_rosをクローンする。
```
git clone --recursive git@github.com:AprilRobotics/apriltag_ros.git
```
2. catkin_makeでビルドする。
```
catkin_make
```
3. 実行する。
```
source catkin_ws/devel/setup.bash
roslaunch takane_ros_sample apriltag.launch
```