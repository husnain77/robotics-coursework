"""obstacle_avoidance controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot

# create the Robot instance.
robot = Robot()

# get the time step of the current world.

#Global Variables
TIMESTEP = 32
MAX_SPEED = 6.28

def run_robot(robot):

    # You should insert a getDevice-like function in order to get the
    # instance of a device of the robot. Something like:
    #  motor = robot.getDevice('motorname')
    #  ds = robot.getDevice('dsname')
    #  ds.enable(timestep)
    left_motor=robot.getDevice('left wheel motor')
    right_motor=robot.getDevice('right wheel motor')
    
    left_motor.setPosition(float('inf'))  #setting position to infinity we are indicating we will use velocity
    right_motor.setPosition(float('inf'))
    
    left_motor.setVelocity(0.0)
    right_motor.setVelocity(0.0)
    
    # Main loop:
    # - perform simulation steps until Webots is stopping the controller
    while robot.step(TIMESTEP) != -1:
        # Read the sensors:
        # Enter here functions to read sensor data, like:
        #  val = ds.getValue()
    
        # Process sensor data here.
    
        # Enter here functions to send actuator commands, like:
        #  motor.setPosition(10.0)
        left_motor.setVelocity(MAX_SPEED)
        right_motor.setVelocity(MAX_SPEED    )

# Enter here exit cleanup code.

#Main robot function
if __name__ == "__main__":
    #create the robot instance
    my_robot=Robot()
    run_robot(my_robot)
    
     
     