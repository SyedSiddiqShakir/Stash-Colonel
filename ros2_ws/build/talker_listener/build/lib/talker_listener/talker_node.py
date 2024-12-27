import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class TalkerNode(Node):
    def __init__(self):
        super().__init__('talker_node')
        self.publisher_ = self.create_publisher(String, 'topic', 10)
        time_period = 0.5
        self.timer = self.create_timer(time_period, self.timer_callback)
        self.count = 0
    def timer_callback(self):
        msg = String()
        msg.data = f"Hello all {self.count}"
        self.publisher_.publish(msg)
        self.count += 1
        self.get_logger().info(f"Publishing {msg.data}")

def main(args=None):
    rclpy.init(args=args)

    #create node
    talkernode = TalkerNode()

    #use node
    rclpy.spin(talkernode)

    #destroy node
    talkernode.destroy_node()
    rclpy.shutdown()



if __name__ == "__main__":
    main()
