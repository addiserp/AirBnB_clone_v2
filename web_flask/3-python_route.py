#!/usr/bin/env bash
# a script that starts a Flask web application:

from flask import Flask

app = Flask(__name__)


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythoniscool(text="is cool"):
    """
        this will display “Python ” and followed by the value of input variable
    """
    return 'Python ' + text.replace('_', ' ')


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """this will display “C ” and followed by the value of input variable"""
    return 'C ' + text.replace('_', ' ')


@app.route("/hbnb", strict_slashes=False)
def hello_world():
    """this will return HBNB!"""
    return "HBNB!"


@app.route("/", strict_slashes=False)
def hello():
    """this will return Hello HBNB!"""
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
