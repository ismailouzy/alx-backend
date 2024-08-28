#!/usr/bin/env python3
"""
basic flask app
"""

from typing import Dict, Union
from flask import Flask, render_template
from flask import request, g
from flask_babel import Babel, _


class Config:
    """config"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False

babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(id) -> Union[Dict[str, Union[str, None]], None]:
    """
    Validates the users credentials
    """
    return users.get(int(id), 0)


@app.before_request
def before_request():
    """
    Adds a valid user
    """
    setattr(g, 'user', get_user(request.args.get('login_as', 0)))


@babel.localeselector
def get_locale() -> str:
    """
    Get locale from request
    """
    options = [
        request.args.get('locale', '').strip(),
        g.user.get('locale', None) if g.user else None,
        request.accept_languages.best_match(app.config['LANGUAGES']),
        Config.BABEL_DEFAULT_LOCALE
    ]
    for locale in options:
        if locale and locale in Config.LANGUAGES:
            return locale


@app.route('/')
def index() -> str:
    """ render a html template"""
    return render_template("5-index.html")


if __name__ == "__main__":
    app.run(debug=True)
