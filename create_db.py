from webapp import db, create_app

app = create_app()
db.init_app(app)
db.create_all(app=app)