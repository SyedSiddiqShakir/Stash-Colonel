#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class MyNode(Node):
    
    def __init__(self):
        super().__init__("first_node")
        self.get_logger().info("Hello from German-ROS2")



def main(args=None):
    #initializing code
    rclpy.init(args=args)

    #create a node
    node = MyNode()

    #loops the node (keeps the node alive), but needs an argument for spin
    rclpy.spin(node)
    
    
    #closing code
    rclpy.shutdown()








if __name__ == '__main__':
    main()