def turn_right():
    turn_left()
    turn_left()
    turn_left() 
    
def move_up():
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    move()
def move_down():
    while front_is_clear():
        move()
    turn_left()
def clear():
    if not front_is_clear():
        turn_left()
        move()
        
while not at_goal():
    if not front_is_clear():
        turn_left()
        clear()
        move_up()
        move_down()
    else:
        move()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
