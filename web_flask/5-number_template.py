#!/usr/bin/python3
"""
    a script that starts a Flask web application:
    retun HTML tag is n is integer.
"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/number/<int:n>', strict_slashes=False)
def isinteger(n):
    """this will display “n is a number ” only if n is an integer"""
    return '{} is a number'.format(n)


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythoniscool(text='is cool'):
    """
        this will display “Python ” and followed by the value of input variable
    """
    return 'Python ' + text.replace('_', ' ')


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """this will display “C ” and followed by the value of input variable"""
    return 'C ' + text.replace('_', ' ')


@app.route('/hbnb', strict_slashes=False)
def hello_world():
    """this will return HBNB!"""
    return 'HBNB!'


@app.route('/', strict_slashes=False)
def hello():
    """this will return Hello HBNB!"""
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
