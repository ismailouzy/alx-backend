#!/usr/bin/env python3
"""
basic flask app
"""

from flask import Flask, render_template


class Config:
    """config"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False

babel = Babel(app)


@app.route('/')
def index():
    """ render a html template"""
    return render_template("0-index.html",)


if __name__ == "__main__":
    app.run(debug=True)
