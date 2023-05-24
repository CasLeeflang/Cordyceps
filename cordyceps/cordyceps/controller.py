import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Pose
import numpy as np
import time

from cordyceps_interfaces.action import Controller

class ControllerActionServer(Node):
    def __init__(self):
        super().__init__('cordyceps_controller')
        self.action_server = ActionServer(self, Controller, 'controller', self.execute_callback)
        
        # Outputs: cmd_vel for each robot
        self.cmd_vel_publisher = [
            self.create_publisher(Twist, 'r1/cmd_vel', 10),
            self.create_publisher(Twist, 'r2/cmd_vel', 10),
            self.create_publisher(Twist, 'r3/cmd_vel', 10),
            self.create_publisher(Twist, 'r4/cmd_vel', 10),
        ]  

    def execute_callback(self, goal_handle):
        self.get_logger().info('Executing goal...')
        goal_handle.succeed()
        result = Controller.Result()
        return result

def main(args=None):
    rclpy.init(args=args)
    controller_action_server = ControllerActionServer()
    rclpy.spin(controller_action_server)
    controller_action_server.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()