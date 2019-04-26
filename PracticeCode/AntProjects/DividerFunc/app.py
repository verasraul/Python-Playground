__author__ = 'verasraul'
'''
Flask API for divider/addtion functions.

This will allow the functions to run on the browser.
'''

# import flask moudle to create REST api.
from flask import Flask

# import divider and addition function from modules.
import dividerFunction1
import additionFunction1



app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome Home"

@app.route("/divider")
def divider():
    return str((dividerFunction1.divider(10,2)))

@app.route("/addition")
def addition():
    return str((additionFunction1.addition(5,5)))


if __name__ == '__main__':
    app.run()