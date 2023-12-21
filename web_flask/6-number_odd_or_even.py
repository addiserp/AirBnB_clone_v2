#!/usr/bin/env bash
# a script that starts a Flask web application:
# retun HTML tag is n is integer.
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    """
    will return H1 tag: “Number: n is even|odd” inside the tag BODY
    """
    if (n % 2 == 0):
        nvalue = "{} is even".format(n)
    else:
        nvalue = "{} is odd".format(n)

    return render_template('6-number_odd_or_even.html', n=nvalue)


@app.route('/number_template/<int:n>', strict_slashes=False)
def isinteger_template(n):
    """
        this will display display a HTML page only if
        n is an integer:
    """
    return render_template('5-number.html', n=n)


@app.route('/number/<int:n>', strict_slashes=False)
def isinteger(n):
    """this will display “n is a number ” only if n is an integer"""
    return "{} is a number".format(n)


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
