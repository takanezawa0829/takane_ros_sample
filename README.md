# takane_ros_sample
## パッケージを使うための準備
### 1. 依存関係をインストールする。
    ```
    cd ~/catkin_ws/src/takane_ros_sample
    rosdep install -iry --from-paths .
    ```

### 2. pythonコマンドでpython3.8を実行できるようにする。
    ```
    <!-- python3のversionとパスを確認する。 -->
    ll $(which python3)*

    <!-- pythonコマンドで実行できるように登録する。（パスとversionは一致させる） -->
    update-alternatives --install /usr/bin/python python /usr/bin/python3.8 1

    <!-- pythonコマンドで利用したいversionを選択する。 -->
    update-alternatives --config python 
    ```

## 開発環境
* Ubuntu20.04LTS Desktop
* ROS Noetic