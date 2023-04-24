#!/usr/bin/env python3
# coding: UTF-8
import rospy


# メイン
def main():
    # ノードの初期化
    rospy.init_node("my_parameter_node")

    # パラメータの値の指定
    if not rospy.has_param("~my_parameter"):
        rospy.set_param("~my_parameter", 0)

    # 1秒毎にパラメータ出力
    r = rospy.Rate(1)  # 1Hz
    while not rospy.is_shutdown():
        # パラメータの値の取得
        value = rospy.get_param("~my_parameter", 0)

        # ログ出力
        rospy.loginfo("my_parameter : " + str(value))

        # スリープ
        r.sleep()

    # ノード終了まで待機
    rospy.spin()


if __name__ == "__main__":
    main()
