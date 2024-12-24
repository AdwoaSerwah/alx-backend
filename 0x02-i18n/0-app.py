#!/usr/bin/env python3
"""
This script sets up a basic Flask app with a single route.
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """
    Render the index page with 'Welcome to ALX' title and
    'Hello world' header.
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    # Make the app accessible on all network interfaces, and
    # allow access with or without a trailing slash
    app.run(host='0.0.0.0', port=5000, debug=True)
