from flask import Flask
import random

app = Flask(__name__)

print(random.__name__)
print(__name__)

@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello World!</h1>' \
        '<p>This is a paragraph</p>' \
        '<img src="https://media.giphy.com/media/102mqDgAb4Kfug/giphy.gif">'

@app.route('/bye')
def bye():
    return 'Bye'

@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f'Hello {name}, you are {number} years old!'

if __name__ == "__main__":
    app.run(debug=True)