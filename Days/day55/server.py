from flask import Flask
from random import randint

MAX = 15
TARGET = randint(1, 15)

app = Flask(__name__)


@app.route('/')
def home():
    return '<h1>Guess a number between 1 and 15 (inclusive)</h1><br><img src="https://media.giphy.com/media/xUn3CftPBajoflzROU/giphy.gif">'


@app.route('/<int:guess>')
def evaluate(guess):
    global TARGET
    if guess == TARGET:
        return '<b><h1 style="color: green">You guessed the right number!</h1></b><br><img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'
    elif guess < TARGET:
        return '<b><h1 style="color: red">Your guess is too low. Try again!</h1></b><br><img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    else:
        return '<b><h1 style="color: purple">Your guess is too high. Try again!</h1></b><br><img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'


print(__name__)
if __name__ == '__main__':
    app.run(debug=True)
