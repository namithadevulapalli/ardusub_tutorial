import rclpy
from rclpy.node import Node
from mavros_msgs.msg import ManualControl

class MotorControl(Node):
    def __init__(self):
        super().__init__("motor_control_node")

        self.pub = self.create_publisher(
            ManualControl,
            "manual_control",
            10
        )

        self.get_logger().info("initialized publisher")
        self.publish_command()

    def publish_command(self):
        self.get_logger().info("entered publishing method")
        msg = ManualControl()

        msg.x = 100.0
        msg.y = 100.0
        
        self.pub.publish(msg)
        self.get_logger().info("published command")

def main(args=None):
    rclpy.init(args=args)
    node = MotorControl()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt received, shutting down...")
    finally:
        # Cleanup
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == '__main__':
    main()