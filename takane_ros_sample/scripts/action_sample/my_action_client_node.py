#! /usr/bin/env python3
# coding: UTF-8
import actionlib
import rospy
from takane_ros_sample.msg import *


# フィードバック受信時に呼ばれる
def on_feedback(feedback):
    # ログ出力
    rospy.loginfo("Feedback : " + str(feedback.rate))


# メイン
def main():
    # ノードの初期化
    rospy.init_node("my_client_node")

    # アクションクライアントの生成
    client = actionlib.SimpleActionClient("my_action", MyActionAction)

    # サーバー接続まで待機
    client.wait_for_server()

    # メッセージの生成
    goal = MyActionGoal()
    goal.a = 1
    goal.b = 2

    # リクエストの送信
    client.send_goal(goal, feedback_cb=on_feedback)

    # レスポンス受信まで待機
    client.wait_for_result()

    # レスポンスの受信
    result = client.get_result()
    rospy.loginfo("Result : " + str(result.sum))

    # ノード終了まで待機
    rospy.spin()


if __name__ == "__main__":
    main()
