# ROS 2 4-DOF Industrial Robotic Arm

A 4-DOF industrial robotic arm modeled using ROS 2 URDF/Xacro.
My first ros2 project!!!

## Features

- 4 revolute joints
- Visual and collision geometry
- Joint limits and axes
- Xacro-based robot description
- RViz2 visualization
- TF tree verification
- Launch file for complete visualization

## Structure

- `urdf/` — URDF and Xacro files
- `launch/` — ROS 2 launch file
- `rviz/` — RViz configuration
- `report/` — Project report
- `screenshots/` — Demonstration screenshots

## Run

```bash
colcon build
source install/setup.bash
ros2 launch four_dof_arm display.launch.py
```
