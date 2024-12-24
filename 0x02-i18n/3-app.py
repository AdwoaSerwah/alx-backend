#!/usr/bin/env python3
"""
This script sets up a basic Flask app with Babel for localization and selects the locale from the request.
"""
from flask import Flask, render_template, request
from flask_babel import Babel, _

# Set up the Flask app
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

@app.route('/', strict_slashes=False)
def index():
    """
    Render the index page with a title and header based on translations.
    """
    return render_template('3-index.html')

@babel.localeselector
def get_locale():
    """
    Determine the best match with the client's preferred language
    based on the request's Accept-Language header.
    """
    return request.args.get('locale', request.accept_languages.best_match(app.config['LANGUAGES']))

if __name__ == '__main__':
    # Run the app
    app.run(host='0.0.0.0', port=5000, debug=True)
