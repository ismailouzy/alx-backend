#!/usr/bin/env python3
"""
basic flask app
"""

from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """config"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False

babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """
    Get locale from request
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """ render a html template"""
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run(debug=True)
