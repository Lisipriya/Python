from flask import Flask
app = Flask(__name__)
print(__name__)

def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper

def make_underline(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper


def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper


@app.route('/')
@make_bold
@make_underline
@make_emphasis
def hello_world():
    return 'Hello, World!'

@app.route("/username/<name>")
def greeting(name):
    return f'<h1 style="text-align: center">Hello {name}</h1><p>How is the Weather today</p><img ' \
           f'src"https://media.giphy.com/media/QFSD9tGuryBHy/giphy-downsized-large.gif" > '

@app.route("/username/<username>/<int:age>")
def greet(username, age):
    return f"Hello {username}, I am {age} old"


if __name__ == "__main__":
    app.run(debug=True)