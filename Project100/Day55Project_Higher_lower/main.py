import random
from flask import Flask

random_num = random.randint(0, 10)
print(random_num)
app = Flask(__name__)


@app.route('/')
def guess_the_number():
    return "<h1>Guess the number between 0 to 9</h1><img " \
           "src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'> "




@app.route("/<int:number>")
def check_number(number):
    if number == random_num:
        return "<h1 style='color:green'>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"

    elif number > random_num:
        return "<h1 style='color:red'>Too High! Try again</h1>" \
               "<img src = 'https://media.giphy.com/media/UIpzEC5QTvuOQ/giphy.gif'>"

    else:
        return "<h1 style='color:blue'>Too Low! Try again</h1>" \
               "<img src = 'https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"


if __name__ == "__main__":
    # Run the app in debug mode to auto-reload

    app.run(debug=True)

