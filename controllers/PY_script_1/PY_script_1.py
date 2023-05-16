# Import the necessary Webots libraries
from controller import Robot, Motor, TouchSensor

# Create an instance of the Robot class
robot = Robot()

# Get handles to the robot's motors and touch sensors
fl_motor = robot.getDevice("wheel3")
fr_motor = robot.getDevice("wheel4")
rl_motor = robot.getDevice("wheel1")
rr_motor = robot.getDevice("wheel2")

ds_left = robot.getDevice("touch sensor 1")
ds_right = robot.getDevice("touch sensor 2")
ds_left.enable(64)
ds_right.enable(64)

# Set the velocity of the motors
fl_motor.setPosition(float('inf'))
fr_motor.setPosition(float('inf'))
rr_motor.setPosition(float('inf'))
rl_motor.setPosition(float('inf'))

# Set initial velocity
velocity = 1.0

# Loop over the simulation time steps
while robot.step(64) != -1:
    print("Left touch sensor value:", ds_left.getValue())
    print("Right touch sensor value:", ds_right.getValue())
    # Check if either touch sensor has been triggered
    if ds_left.getValue() > 0 or ds_right.getValue() > 0:
        # If either touch sensor is triggered, stop the robot and turn it around
        fl_motor.setVelocity(-velocity)
        fr_motor.setVelocity(-velocity)
        rl_motor.setVelocity(-velocity)
        rr_motor.setVelocity(-velocity)
        robot.step(1000)  # wait for the robot to stop moving
        fl_motor.setVelocity(-velocity*2)
        fr_motor.setVelocity(velocity/2)
        rl_motor.setVelocity(-velocity*2)
        rr_motor.setVelocity(velocity/2)
        robot.step(1000)  # wait for the robot to turn around
    else:
        # Otherwise, move the robot forward
        fl_motor.setVelocity(velocity)
        fr_motor.setVelocity(velocity)
        rl_motor.setVelocity(velocity)
        rr_motor.setVelocity(velocity)

    # Check if the robot is too close to an obstacle based on touch sensors
    # Here we assume that a touch sensor is triggered when its value is 1 (meaning contact with an obstacle)
    if ds_left.getValue() > 0 and ds_right.getValue() > 0:
        # If both touch sensors are triggered (i.e., the robot has collided with an obstacle),
        # stop the robot and turn it around
        fl_motor.setVelocity(-velocity)
        fr_motor.setVelocity(-velocity)
        rl_motor.setVelocity(-velocity)
        rr_motor.setVelocity(-velocity)
        robot.step(1000)  # wait for the robot to stop moving
        fl_motor.setVelocity(-velocity)
        fr_motor.setVelocity(velocity)
        rl_motor.setVelocity(-velocity)
        rr_motor.setVelocity(velocity)
        robot.step(1000)  # wait for the robot to turn around
    elif ds_left.getValue() > 0:
        # If only the left touch sensor is triggered, turn right to avoid the obstacle
        fl_motor.setVelocity(velocity)
        fr_motor.setVelocity(-velocity)
        rl_motor.setVelocity(velocity)
        rr_motor.setVelocity(-velocity)
        robot.step(1000)  # wait for the robot to turn
    elif ds_right.getValue() > 0:
        # If only the right touch sensor is triggered, turn left to avoid the obstacle
        fl_motor.setVelocity(-velocity)
        fr_motor.setVelocity(velocity)
        rl_motor.setVelocity(-velocity)
        rr_motor.setVelocity(velocity)
        robot.step(1000)  # wait for the robot to turn
