from flask import Flask
app = Flask(__name__)
print(__name__)
@app.route('/')
def hello_world():
    return 'Hello, World!'
# 1st method to run
# set FLASK_APP=hello.py
# $env:FLASK_APP = "hello.py"
# python - m flask run

# 2nd method to run
if __name__ == "__main__":
    app.run()