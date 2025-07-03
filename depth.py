#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import FluidPressure as Pressure
from mavros_msgs.msg import Altitude, OverrideRCIn


class DepthNode(Node):
    
    def __init__(self):
        super().__init__("depth_node")
        self.get_logger().info("starting initializer")

        # self._step_counter = 0

        self.pressure_sub = self.create_subscription(
            Pressure, 
            "pressure", 
            self.pressure_callback,
            10
        )
        self.pressure_sub
        self.get_logger().info("starting pressure subscriber")

        # self.depth_pub = self.create_publisher(
        #     OverrideRCIn, 
        #    "bluerov2/override_rc", 
        #    10
        # )

        # self.pub_timer = self.create_timer(
        #    1.0, self.depth_callback
        # )

        # self.get_logger().info("starting depth publisher")

        # self.loop = self.create_timer(1.0, self._loop)

    def pressure_callback(self, msg):
        self.get_logger().info("pressure called back")
        pressure = msg.fluid_pressure
        self.depth = (pressure - 99479) * 0.0001019
        self.get_logger().info(f"current depth: {self.depth} meters")

    def depth_callback(self):
        # msg = Altitude()
        # msg.relative = self.depth
        # self.publish(msg)
        self.get_logger().info("depth message sent")

def main(args=None):
    rclpy.init(args=args)
    node = DepthNode()

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