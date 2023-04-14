from flask import Flask
import random

app = Flask(__name__)

print(random.__name__)
print(__name__)


def make_bold(base_func):
    def wrapper():
        new_str = '<b>'
        new_str += base_func()
        new_str += '</b>'
        return new_str
    return wrapper


def make_italic(base_func):
    def wrapper():
        new_str = '<em>'
        new_str += base_func()
        new_str += '</em>'
        return new_str
    return wrapper


def make_underline(base_func):
    def wrapper():
        new_str = '<u>'
        new_str += base_func()
        new_str += '</u>'
        return new_str
    return wrapper

@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello World!</h1>' \
        '<p>This is a paragraph</p>' \
        '<img src="https://media.giphy.com/media/102mqDgAb4Kfug/giphy.gif">'


@app.route('/bye')
@make_bold
@make_underline
@make_italic
def bye():
    return 'Bye'

@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f'Hello {name}, you are {number} years old!'

if __name__ == "__main__":
    app.run(debug=True)