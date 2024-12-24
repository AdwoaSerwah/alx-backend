#!/usr/bin/env python3
"""
Module to create a Flask application with internationalization support.

This module sets up a Flask application that uses Flask-Babel for translation.
It defines a route for the home page and configures the locale selector.
"""


from flask import Flask, render_template, request
from flask_babel import Babel, gettext


app = Flask(__name__)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    Select the locale based on the user's accept header.

    :return: The best matching locale from the user's accept header.
    """
    return request.accept_languages.best_match(['en', 'fr'])


@app.route('/')
def index():
    """
    Route for the home page.

    :return: The rendered template for the home page.
    """
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(debug=True)
