# Day6 of 100DaysOfPython
# function to turn the robot right
def turn_right():
    turn_left()
    turn_left()
    turn_left()
# while to check if the front is clear
while front_is_clear():
    # move the robot
    move()
# turn the robot left
turn_left()
# while to check if the robot is not at the goal
while not at_goal():
    # if the right is clear
    if right_is_clear():
        # turn the robot right
        turn_right()
        # move the robot
        move()
    # if the front is clear
    elif front_is_clear():
        # move the robot
        move()
    # if the left is clear
    else:
        # turn the robot left
        turn_left()
  
        