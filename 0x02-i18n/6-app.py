#!/usr/bin/env python3
"""
This script sets up a basic Flask app with Babel for localization.
It supports setting the locale based on the URL parameters or user settings.
It uses a mock user database and the user's locale preference is used
if available.
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


# Create the Flask app
app = Flask(__name__)


# Config class to set up the app configuration
class Config:
    """
    Configuration class for Flask app.
    Defines available languages and default locale/timezone.
    """

    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# Apply the config to the Flask app
app.config.from_object(Config)


# Instantiate the Babel object
babel = Babel(app)


# Function to get the user from the URL parameter
def get_user():
    """
    Returns a user dictionary based on the 'login_as' parameter in the URL.
    If no valid user is found, returns None.
    """
    user_id = request.args.get('login_as')
    if user_id:
        return users.get(int(user_id))
    return None


# Before request function to set the user globally
@app.before_request
def before_request():
    """
    Set the user globally for all routes before the request is processed.
    """
    user = get_user()
    g.user = user


# Function to determine the best match locale
@babel.localeselector
def get_locale():
    """
    Determine the best match with the client's preferred language based on:
    1. Locale from URL parameter
    2. Locale from user settings
    3. Locale from request header
    4. Default locale
    """
    # Locale from URL parameter
    locale = request.args.get('locale')

    if locale and locale in app.config['LANGUAGES']:
        return locale

    # Locale from user settings
    if g.get('user') and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']

    # Locale from request header
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index():
    """
    Renders the index page with user information if logged in.
    Displays a welcome message or a default message.
    """
    return render_template('6-index.html')


if __name__ == '__main__':
    """
    Run the app. Starts a development server that listens on all IP addresses
    (0.0.0.0) and port 5000 with debugging enabled.
    """
    app.run(host='0.0.0.0', port=5000, debug=True)
