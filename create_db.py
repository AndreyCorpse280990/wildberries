from webapp import db, create_app
from flask import send_from_directory

app = create_app()
db.init_app(app)
db.create_all(app=app)
