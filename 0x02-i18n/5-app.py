#!/usr/bin/env python3
"""
    Basic flask setup using babel, defines class Config
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, _
from typing import Optional, Dict, Any


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """ class Configuration for babel """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


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
    lang: Optional[str] = request.args.get('locale')

    if lang in app.config["LANGUAGES"]:
        return lang
    return "en"


def get_user() -> Optional[Dict[str, Any]]:
    try:
        login: Optional[str] = request.args.get('login_as')
        if login:
            return users.get(int(login))
    except Exception:
        return None


@app.before_request
def before_request():
    """ assign the user data to the global variable"""
    g.user = get_user()


@app.route('/')
def index() -> str:
    """
    The index/home page
    Returns:
        str: renders the template for display
    """
    return render_template('./5-index.html', user=g.user)


if __name__ == "__main__":
    app.run()
