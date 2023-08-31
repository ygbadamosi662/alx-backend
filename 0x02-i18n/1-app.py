#!/usr/bin/env python3
"""
    Basic flask setup using babel, defines class Config
"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """ class Configuration for babel """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/')
def index():
    """
    The index/home page
    Returns:
        str: renders the template for display
    """
    return render_template('./1-index.html')


if __name__ == "__main__":
    app.run()
