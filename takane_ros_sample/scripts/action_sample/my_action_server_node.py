#! /usr/bin/env python3
# coding: UTF-8
import actionlib
import rospy
from takane_ros_sample.msg import *


# メイン
def main():
    # ノードの生成
    rospy.init_node("my_server_node")

    # リクエスト受信時に呼ばれる
    def on_request(goal):
        r = rospy.Rate(2)  # 2Hz
        for i in range(10):
            # フィードバックの返信
            feedback = MyActionFeedback(i * 10)
            server.publish_feedback(feedback)

            # スリープ
            r.sleep()

        # レスポンスの返信
        result = MyActionResult(goal.a + goal.b)
        server.set_succeeded(result)

    # アクションサーバーの生成
    server = actionlib.SimpleActionServer("my_action", MyActionAction, on_request, False)

    # アクションサーバーを開始
    server.start()

    # ノード終了まで待機
    rospy.spin()


if __name__ == "__main__":
    main()
