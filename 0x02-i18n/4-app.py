#!/usr/bin/env python3
"""
    Basic flask setup using babel, defines class Config
"""
from flask import Flask, render_template, request
from flask_babel import Babel, _


class Config:
    """ class Configuration for babel """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


""" configure app """
app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)


@babel.localeselector
def get_locale() -> str:
    """
    get the best matched language for the locale
    Returns:
        str: language short form
    """
    lang = request.args.get('locale')

    if lang in app.config["LANGUAGES"]:
        return lang
    return "en"


@app.route('/')
def index() -> str:
    """
    The index/home page
    Returns:
        str: renders the template for display
    """
    return render_template('./3-index.html')


if __name__ == "__main__":
    app.run()
