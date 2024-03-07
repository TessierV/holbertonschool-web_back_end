#!/usr/bin/env python3
""" Basic Flask app with user login emulation """
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

def get_user(user_id):
    """ Get user information based on user ID """
    return users.get(user_id)

@app.before_request
def before_request():
    """ Function to be executed before all other functions """
    user_id = int(request.args.get('login_as', 0))
    g.user = get_user(user_id)

@babel.localeselector
def get_locale():
    """ Locale selector """
    if g.user:
        return g.user['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index():
    """ Display welcome message based on login status """
    if g.user:
        return render_template('5-index.html', username=g.user['name'])
    else:
        return render_template('5-index.html', username=None)

if __name__ == "__main__":
    app.run(debug=True)
