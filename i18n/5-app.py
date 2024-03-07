#!/usr/bin/env python3
""" Basic Flask app """

from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext

app = Flask(__name__)
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

class Config:
    """ Config """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """ Locale selector """
    if request.args.get('locale') in app.config['LANGUAGES']:
        return request.args.get('locale')
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    """ returns a user """
    try:
        userId = request.args.get('login_as')
        return users[int(userId)]
    except Exception:
        return None

@app.before_request
def before_request():
    """ before  """
    g.user = get_user()


@app.route('/')
def root():
    """ Basic Flask app """
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run()
