# YOLOv3-tinyを使いたいとき
1. ~/catkin_ws/srcにdarknet_rosをクローンする。  
```
git clone --recursive https://github.com/leggedrobotics/darknet_ros.git
```
2. catkin_makeでビルドする。
```
catkin_make
```
3. 実行する。
```
source catkin_ws/devel/setup.bash
roslaunch takane_ros_sample yolov3-tiny.launch
```