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

# Set retreat distance and turn duration
retreat_distance = 0.5
turn_duration = 1.0

# Variables to store previous sensor values
previous_left_value = 0
previous_right_value = 0

# Loop over the simulation time steps
while robot.step(64) != -1:
    # Read the current sensor values
    left_value = ds_left.getValue()
    right_value = ds_right.getValue()
    # Print the current sensor values
    print("Left sensor value:", left_value)
    print("Right sensor value:", right_value)
    # Check if either touch sensor has been triggered
    if left_value > 0 or right_value > 0:
        # If either touch sensor is triggered, stop the robot and turn it around
        fl_motor.setVelocity(-velocity)
        fr_motor.setVelocity(-velocity)
        rl_motor.setVelocity(-velocity)
        rr_motor.setVelocity(-velocity)
        robot.step(1000)  # wait for the robot to stop moving
        
        # Retreat a specific distance
        fl_motor.setVelocity(-velocity)
        fr_motor.setVelocity(-velocity)
        rl_motor.setVelocity(-velocity)
        rr_motor.setVelocity(-velocity)
        robot.step(int(retreat_distance * 1000))  # retreat for a specific distance
        
        # Execute a turn in an alternate direction
        fl_motor.setVelocity(-velocity)
        fr_motor.setVelocity(velocity)
        rl_motor.setVelocity(-velocity)
        rr_motor.setVelocity(velocity)
        robot.step(int(turn_duration * 1000))  # wait for the robot to turn around
        
    else:
        # Otherwise, move the robot forward
        fl_motor.setVelocity(velocity)
        fr_motor.setVelocity(velocity)
        rl_motor.setVelocity(velocity)
        rr_motor.setVelocity(velocity)

    # Check if the robot has collided with an obstacle
    if (previous_left_value > 0 and left_value > 0) or (previous_right_value > 0 and right_value > 0):
        # If both touch sensors were triggered in the previous step and are still triggered,
        # stop the robot and turn it around
        fl_motor.setVelocity(-velocity)
        fr_motor.setVelocity(-velocity)
        rl_motor.setVelocity(-velocity)
        rr_motor.setVelocity(-velocity)
        robot.step(1000)  # wait for the robot to stop moving
        
        # Execute a turn in an alternate direction
        fl_motor.setVelocity(-velocity)
        fr_motor.setVelocity(velocity)
        rl_motor.setVelocity(-velocity)
        rr_motor.setVelocity(velocity)
        robot.step(int(turn_duration * 1000))  # wait for the robot to turn around
        
    elif previous_left_value > 0 and left_value > 0:
        # If only the left touch sensor was triggered in the previous step and is still triggered,
        # turn right to avoid the obstacle
        fl_motor.setVelocity(velocity)
        fr_motor.setVelocity(-velocity)
        rl_motor.setVelocity(velocity)
        rr_motor.setVelocity(-velocity)
        robot.step(int(turn_duration * 1000))  # wait for the robot to turn
        
    elif previous_right_value > 0 and right_value > 0:
        # If only the right touch sensor was triggered in the previous step and is still triggered,
        # turn left to avoid the obstacle
        fl_motor.setVelocity(-velocity)
        fr_motor.setVelocity(velocity)
        rl_motor.setVelocity(-velocity)
        rr_motor.setVelocity(velocity)
        robot.step(int(turn_duration * 1000))  # wait for the robot to turn
        
    # Update the previous sensor values
    previous_left_value = left_value
    previous_right_value = right_value
