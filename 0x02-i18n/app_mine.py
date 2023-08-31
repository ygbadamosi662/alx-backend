#!/usr/bin/env python3
"""
    Basic flask setup using babel, defines class Config
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, _
from typing import Optional, Dict, Any
import pytz
from pytz import timezone, exceptions
from datetime import datetime as dt
import locale

app = Flask(__name__)
babel = Babel()


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


def get_locale() -> str:
    """
    get the best matched language for the user
    Returns:
        str: language short form
    """
    try:
        lang_url: Optional[str] = request.args.get('locale')
        if lang_url and (lang_url in app.config["LANGUAGES"]):
            return lang_url

        lang_user: Optional[Dict[str, Any]] = get_user()
        if lang_user:
            if lang_user.get("locale") in app.config["LANGUAGES"]:
                return lang_user["locale"]

        lang_req = request.headers.get('Accept-Language')
        if lang_req:
            langs = [lang.strip() for lang in lang_req.split(',')]
            for lang in langs:
                if lang in app.config["LANGUAGES"]:
                    return lang

    except Exception:
        return "en"

    return 'en'


def get_timezone() -> str:
    """
    get the timezone for the user
    Returns:
        str: the timezone
    """
    try:
        zone_url: Optional[str] = request.args.get('timezone')
        if zone_url and timezone(zone_url):
            return zone_url

        zone_user: Optional[Dict[str, Any]] = get_user()
        if zone_user and timezone(zone_user['timezone']):
            return zone_user['timezone']

    except exceptions.UnknownTimeZoneError:
        return "UTC"

    return "UTC"


def get_user() -> Optional[Dict[str, Any]]:
    """
        get the user data from the storagedict
    Returns:
        Optional[Dict[str, Any]]: the value of the user from the srorage.
    """
    try:
        login: Optional[str] = request.args.get('login_as')
        if login:
            return users.get(int(login))

    except Exception:
        return None

    return None


@app.before_request
def before_request():
    """ assign the user data to the global variable """
    g.user = get_user()

    fmt = "%b %d, %Y, %I:%M:%S %p"
    time_now = pytz.utc.localize(dt.utcnow())
    time = time_now.astimezone(timezone(get_timezone()))
    locale.setlocale(locale.LC_TIME, (get_locale(), 'UTF-8'))
    time_format = "%b %d, %Y %I:%M:%S %p"                  
    g.time = time.strftime(time_format)


app.config.from_object(Config)
babel.init_app(app, locale_selector=get_locale, timezone_selector=get_timezone)


@app.route('/')
def index() -> str:
    """
    The index/home page
    Returns:
        str: renders the template for display
    """
    return render_template('./index.html', user=g.user, ctime=g.time)


if __name__ == "__main__":
    app.run()
