from launch import LaunchDescription
from launch_ros.actions import Node

import os
import xacro
from ament_index_python.packages import get_package_share_directory

pkg_share = get_package_share_directory('four_dof_arm')

xacro_file = os.path.join(
    pkg_share,
    'urdf',
    'four_dof_arm.xacro'
)

urdf_file = os.path.join(
    pkg_share,
    'urdf',
    'four_dof_arm.urdf'
)

robot_description = xacro.process_file(xacro_file).toxml()

rviz_config = os.path.join(
    pkg_share,
    'rviz',
    'four_dof_arm.rviz'
)

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{
                'robot_description': robot_description
            }]
        ),

        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            arguments=[urdf_file]
        ),

        Node(
            package='rviz2',
            executable='rviz2',
            arguments=['-d', rviz_config]
        )
    ])