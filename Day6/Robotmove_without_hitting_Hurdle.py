def turn_right():
    turn_left()
    turn_left()
    turn_left()  

def run_path():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
for movement in range(0, 6):
    run_path()

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
