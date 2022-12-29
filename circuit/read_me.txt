pour lancer :

roslaunch circuit launch_circuit_full_auto.launch

rappel procédure de un peu tout :


dans le src de ton espace ros :

git clone git@github.com:clement-chupin/projet_ros.git
pour récuperer le boulot


git add .
git commit -m ""
git push origin master
pour envoyer le boulot



je te joint également mon bash_history pour que tu puisse voire toutes les commandes que j'ai fait














le tree du bordel :


projet_ros
── install
── build
── devel
└── src
    ├── circuit
    │   ├── CMakeLists.txt
    │   ├── package.xml
    │   ├── projet_car_install.sh
    │   ├── src
    │   │   ├── blend
    │   │   │   ├── car_blender.blend
    │   │   │   ├── car_blender.blend1
    │   │   │   ├── circuit.blend
    │   │   │   └── circuit.blend1
    │   │   ├── config
    │   │   │   └── mobile_robot
    │   │   │       ├── back_wheel.yaml
    │   │   │       ├── base.yaml
    │   │   │       └── front_wheel.yaml
    │   │   ├── launch
    │   │   │   ├── launch_circuit_full_auto.launch
    │   │   │   ├── launch_circuit_with_joy.launch
    │   │   │   └── launch_circuit_withoot_cars.launch
    │   │   ├── nodes
    │   │   │   ├── circuit_manager.py
    │   │   │   ├── control_by_joy.py
    │   │   │   ├── control_by_sensor.py
    │   │   │   ├── images
    │   │   │   │   ├── .....
    │   │   │   └── ROS
    │   │   │       ├── chupin_joystick
    │   │   │       │   ├── CMakeLists.txt
    │   │   │       │   ├── package.xml
    │   │   │       │   └── scripts
    │   │   │       │       ├── main_joystick.py
    │   │   │       │       ├── publisher_test_joystick.py
    │   │   │       │       └── reader_joystick.py
    │   │   │       ├── chupin_premier_paquet
    │   │   │       │   ├── CMakeLists.txt
    │   │   │       │   ├── package.xml
    │   │   │       │   └── scripts
    │   │   │       │       ├── publisher.py
    │   │   │       │       └── reader.py
    │   │   │       ├── COMMANDES UTILES.txt
    │   │   │       └── main_control_sonar.py
    │   │   ├── urdf
    │   │   │   ├── include
    │   │   │   │   └── common_macros.urdf.xacro
    │   │   │   ├── meshes
    │   │   │   │   ├── car_blender.dae
    │   │   │   │   ├── circuit_visual.dae
    │   │   │   │   ├── texture_car.png
    │   │   │   │   └── track_map.stl
    │   │   │   ├── mobile_robot.urdf.xacro
    │   │   │   └── race_track.urdf.xacro
    │   │   └── worlds
    │   │       └── world.world
    │   └── srv
    │       └── StartRace.srv
    └── CMakeLists.txt -> /opt/ros/noetic/share/catkin/cmake/toplevel.cmake
