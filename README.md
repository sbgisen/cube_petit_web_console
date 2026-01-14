# cube_petit_web_console

Cube petit 用の Webコンソール（Webアプリケーション） です。<br/>
ROS 2（Jazzy）環境で起動し、ブラウザからロボットの状態確認・操作を行うことを目的としています。

Cube petit Web Console (Web application).<br/>
It runs in a ROS 2 (Jazzy) environment and is intended to allow users to monitor and control the robot from a web browser.

- OS: Ubuntu 24.04
- ROS: ROS 2 Jazzy
- Frontend: Vite + React + TypeScript
- Package manager: yarn

Repository：
- cube_petit_ros： https://github.com/sbgisen/cube_petit_ros

## Requirements

- Ubuntu 24.04
- ROS 2 Jazzy
- nodejs / npm
- yarn


## Install dependencies

```bash
sudo apt update
sudo apt install -y nodejs npm
sudo npm install -g yarn
```

## Build (ROS workspace)
```bash
cd ~/ros/src
git clone https://github.com/sbgisen/cube_petit_web_console.git

cd ~/ros
rosdep install --from-paths src -iry
colcon build --symlink-install
source ~/ros/install/setup.bash
```

## Run
1. Launch `rosbridge_server`
    ```bash
    ros2 launch cube_petit_web_console web_app.launch.py
    ```
2. Launch Web application
    ```bash
    cd ~/ros/src/cube_petit_web_console/web_app
    yarn dev
    ```

## Access (Chrome)
- http://localhost:5173

    ※Viteのデフォルトは 5173 です。<br/>
    もし別ポートで起動している場合は、ターミナルの表示を優先してください。<br/>
    The default port for Vite is 5173.<br/>
    If the app is running on a different port, please follow the URL shown in the terminal output.

## How to use App

