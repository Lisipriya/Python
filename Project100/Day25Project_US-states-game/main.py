from turtle import Turtle, Screen
import pandas

view = Screen()
view.title("State Game")
image = "blank_states_img.gif"
view.addshape(image)
img = Turtle()
img.shape(image)


def move_state():
    for state_value in fifty_states:
        if state_value == guess_state:
            guessed_states.append(guess_state)
            state_data = data[data.state == guess_state]
            turtle = Turtle()
            turtle.penup()
            turtle.hideturtle()
            turtle.setposition(int(state_data.x), int(state_data.y))
            turtle.write(guess_state)
            return True



# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
data = pandas.read_csv("50_states.csv")
fifty_states = data["state"]
length = len(fifty_states)
score = 0
guessed_states = []
non_guessed_states = []
while range(length):

    guess_state = view.textinput(title=f"States correct: {len(guessed_states)}/50", prompt="What's the another state").title()
    if move_state():
        score += 1
    if guess_state == "Exit":
        for state in fifty_states:
            if state not in guessed_states:
                non_guessed_states.append(state)
        # print(len(non_guessed_states), non_guessed_states)
        learn = pandas.DataFrame(non_guessed_states)
        learn.to_csv("learn_states.csv")
        break

