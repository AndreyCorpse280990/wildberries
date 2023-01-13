from flask import Flask, render_template

from webapp.saving_to_database import db, app


@app.route("/")
def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    return app
