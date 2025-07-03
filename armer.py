import rclpy
from rclpy.node import Node
from std_srvs.srv import SetBool
# from rcl_interfaces.srv import GetParameters

class Armer(Node): 
    
    def __init__(self):
        ''' 
        Initializes node, names it armer, creates a client that can request from the arming service.
        '''
        super().__init__("armer")
        self.cli = self.create_client(SetBool, 'arming') # creates client for the arming sevice of type SetBool
        self.get_logger().info("arming client created")
        self.req = SetBool.Request()

        self.send_request(True) # sends request for robot to be armed


    def send_request(self, bool):
        '''
        takes true if the robot should be armed and false if it should be disarmed
        '''
        self.req.data = bool # sets message value to the given boolean

        self.future = self.cli.call_async(self.req)
        rclpy.spin_until_future_complete(self, self.future)
        self.get_logger().info("request sent")


    

def main(args=None):

    rclpy.init(args=args)

    node = Armer() # creates node with service client

    try:
        rclpy.spin(node)

    except KeyboardInterrupt:
        print("\nKeyboardInterrupt received, shutting down...")
    finally:

        node.send_request(False) # disarms the robot before killing the node
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()

if __name__ == "__main__":
    main()
