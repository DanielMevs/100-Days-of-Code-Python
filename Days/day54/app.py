from flask import Flask
import random

app = Flask(__name__)

print(random.__name__)
print(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/bye')
def bye():
    return 'Bye'

if __name__ == "__main__":
    app.run()