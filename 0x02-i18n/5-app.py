#!/usr/bin/env python3
"""
This script sets up a basic Flask app with Babel for localization.
It also mocks a user login system using a 'login_as' URL parameter.
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, _

# Mock user database
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

# Set up the Flask app
app = Flask(__name__)


# Config class to set up the app configuration
class Config:
    """
    Configuration class for the Flask app. Defines supported languages and
    default locale/timezone.
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# Apply the config to the Flask app
app.config.from_object(Config)

# Instantiate the Babel object
babel = Babel(app)


@app.before_request
def before_request():
    """
    This function is executed before handling every request. It checks if the
    'login_as' parameter is present in the request. If so, it fetches the user
    corresponding to the ID in the 'login_as' parameter and sets the user as a
    global variable on flask.g.
    """
    user_id = request.args.get('login_as')
    if user_id:
        user = get_user(user_id)
        g.user = user


def get_user(user_id):
    """
    This function returns the user dictionary corresponding to the given
    user ID. If the user ID is not found, it returns None.

    Args:
        user_id (str): The ID of the user to retrieve.

    Returns:
        dict or None: The user dictionary or None if not found.
    """
    return users.get(int(user_id))


@app.route('/', strict_slashes=False)
def index():
    """
    Renders the index page. Displays a welcome message if
    the user is logged in.
    """
    return render_template('5-index.html')


@babel.localeselector
def get_locale():
    """
    Selects the locale based on the 'locale' URL parameter or Accept-Language
    header.
    """
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    """
    Run the app, which listens on all IP addresses (0.0.0.0) and port 5000,
    with debugging enabled.
    """
    app.run(host='0.0.0.0', port=5000, debug=True)
