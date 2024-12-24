#!/usr/bin/env python3
"""
This script sets up a basic Flask app with Babel for localization.
It supports forcing a locale by passing the locale parameter in the URL
(e.g., locale=fr or locale=en).
"""

from flask import Flask, render_template, request
from flask_babel import Babel, _


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


@app.route('/', strict_slashes=False)
def index():
    """
    Renders the index page with the translated title and header.
    """
    return render_template('4-index.html')


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


# Context processor to pass get_locale to Jinja2 templates
@app.context_processor
def inject_locale():
    """
    Injects the get_locale function into the Jinja2 template context so that
    it can be used in templates.
    """
    return {'get_locale': get_locale}


if __name__ == '__main__':
    """
    Run the app, which listens on all IP addresses (0.0.0.0) and port 5000,
    with debugging enabled.
    """
    app.run(host='0.0.0.0', port=5000, debug=True)
