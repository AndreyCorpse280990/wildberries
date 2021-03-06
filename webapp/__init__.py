from flask import Flask, render_template
from webapp.saving_to_database import db
from webapp.forms import LoginForm


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    #
    # @app.route('/login')
    # def login():
    #     title = 'Авторизация'
    #     login_form = LoginForm()
    #     return render_template('login.html', page_title=title, form=login_form)
    return app


if __name__ == "__main__":
    create_app().run(debug=True)