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

