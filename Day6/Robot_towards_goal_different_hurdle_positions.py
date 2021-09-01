def turn_right():
    turn_left()
    turn_left()
    turn_left()  

def run_path():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
while not at_goal():
    if not front_is_clear():      
        run_path()
    else:
        move()
    
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
