#!/usr/bin/python3
"""
    It will start a Flask web application.
    8. List of states
"""

from flask import Flask, render_template
from models import *
from models import storage
import models

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """It displays a HTML page with the states listed in alphabetical order"""
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


@app.route('/cities_by_states', strict_slashes=False)
def route_city():
    """It displays a HTML page states with the cities listed"""
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    city = sorted(list(storage.all("cities").values()), key=lambda x: x.name)
    return render_template('8-cities_by_states.html', states=states, city=city)


@app.teardown_appcontext
def teardown_db(exception):
    """It closes the storage on teardown"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5001')
