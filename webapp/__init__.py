from flask import Flask, render_template
from flask_login import LoginManager, login_required, current_user

from webapp.selenium_similar import get_html
from webapp.User.models import db, User
from webapp.User.views import blueprint as user_blueprint


from webapp.config import *

"""через if __name__ могу запустить сервер, через create_app сервер не 
запускается, функция create_app нужна в файле create_db для создания БД"""

# app = Flask(__name__)
# app.config.from_pyfile('config.py')
# db.init_app(app)
#
# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = 'login'
#
#
# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(user_id)
#
#
# @app.route("/")
# def index():
#     title = 'Wildberries parser'
#     return render_template('index.html', page_title=title)
#
#
# @app.route("/login")
# def login():
#     if current_user.is_authenticated:
#         return redirect(url_for('index'))
#     title = "Авторизация"
#     login_form = LoginForm()
#     return render_template('login.html', page_title=title, form=login_form)
#
#
# @app.route("/process-login", methods=['POST'])
# def process_login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         user = User.query.filter(User.username == form.username.data).first()
#         if user and user.check_password(form.password.data):
#             login_user(user)
#             flash('Вы вошли на сайт')
#             return redirect(url_for('index'))
#
#         flash('Неправильное имя пользователя или пароль')
#         return redirect(url_for('login'))
#
#     @app.route('/logout')
#     def logout():
#         logout_user()
#         flash('Вы успешно разлогинились')
#         return redirect(url_for('index'))
#
#     @app.route('/admin')
#     @login_required
#     def admin_index():
#         if current_user.is_admin():
#             return 'Привет, admin'
#         else:
#             return 'Ты не admin'
#
#
# if __name__ == "__main__":
#     app.run(debug=True)



def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'
    app.register_blueprint(user_blueprint)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    @app.route("/")
    def index():
        title = 'Wildberries parser'
        return render_template('index.html', page_title=title)


    @app.route('/admin')
    @login_required
    def admin_index():
        if current_user.is_admin():
            return 'Привет, admin'
        else:
            return 'Ты не admin'

    return app
