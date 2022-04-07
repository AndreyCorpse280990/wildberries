from flask import Flask, render_template
from webapp.selenium_similar import get_html
from webapp.saving_to_database import db, app
from webapp.forms import LoginForm

from webapp.config import *


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @app.route("/")
    def index():
        title = 'Wildberries parser'
        return render_template('index.html', page_title=title)

    @app.route("/login")
    def login():
        title = "Авторизация"
        login_form = LoginForm()
        return render_template('login.html', page_title=title, form=login_form)

    #return app


# if __name__ == "__main__":
#     app.run(debug=True)
