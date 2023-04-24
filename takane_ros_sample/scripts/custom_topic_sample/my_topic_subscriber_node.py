#!/usr/bin/env python3
# coding: UTF-8
import rospy
from takane_ros_sample.msg import MyMessage


# サブスクライブ受信時に呼ばれる
def on_subscribe(msg):
    # ログ出力
    rospy.loginfo("Subscribe : " + str(msg.x) + ", " + str(msg.y))


# メイン
def main():
    # ノードの生成
    rospy.init_node("my_subscriber_node")

    # サブスクライバーの生成
    rospy.Subscriber("my_custom_topic", MyMessage, on_subscribe)

    # ノード終了まで待機
    rospy.spin()


if __name__ == "__main__":
    main()
