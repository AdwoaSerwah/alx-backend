#!/usr/bin/env python3
"""
This script sets up a basic Flask app with Babel for localization.
It also supports
forcing a locale by passing the locale parameter in the
URL (e.g., locale=fr or locale=en).

The app selects the locale from the request based on:
1. The locale parameter in the URL (e.g., ?locale=fr).
2. The client's preferred language from the Accept-Language header,
if the locale parameter is not provided.
3. A default locale (English in this case) if no other locale is determined.

By using this setup, the app can display content in different languages based
on the user's preference.

Flask-Babel is used for the translation and locale management.
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

    Attributes:
        LANGUAGES (list): List of supported languages (English and French).
        BABEL_DEFAULT_LOCALE (str): Default locale set to 'en' (English).
        BABEL_DEFAULT_TIMEZONE (str): Default timezone set to 'UTC'.
    """
    LANGUAGES = ['en', 'fr']  # Supported languages
    BABEL_DEFAULT_LOCALE = 'en'  # Default locale is English
    BABEL_DEFAULT_TIMEZONE = 'UTC'  # Default timezone is UTC


# Apply the config to the Flask app
app.config.from_object(Config)

# Instantiate the Babel object, which handles locale selection and translations
babel = Babel(app)


@app.route('/', strict_slashes=False)
def index():
    """
    Renders the index page. The title and header of the page will be translated
    based on the selected locale. The appropriate translation will be displayed
    based on the URL parameter or the Accept-Language header.

    Returns:
        render_template: The rendered HTML template for the index page.
    """
    return render_template('4-index.html')


@babel.localeselector
def get_locale():
    """
    Determines the best match with the client's preferred language based on
    the following priorities:
    1. If the 'locale' parameter is provided in the URL and it's a supported
    language (either 'en' or 'fr'), use that locale.
    2. If the 'locale' parameter is not present or invalid, fallback to the
    Accept-Language header of the request.
    3. If neither is found, fallback to the default locale (English).

    This function ensures that the app will display the correct translations
    based on the user's preferred language.

    Returns:
        str: The selected locale (either 'en' or 'fr').
    """
    # Check if 'locale' parameter is present in the URL
    locale = request.args.get('locale')

    # If 'locale' is valid and supported, return it
    if locale and locale in app.config['LANGUAGES']:
        return locale

    # Otherwise, fallback to the Accept-Language header
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    """
    Run the app. When executed, the app will start a development server that
    listens on all IP addresses
    (0.0.0.0) and port 5000, with debugging enabled for easier troubleshooting.
    """
    app.run(host='0.0.0.0', port=5000, debug=True)
