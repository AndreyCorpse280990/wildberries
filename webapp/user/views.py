from flask_login import login_user, logout_user, current_user
from flask import Blueprint, render_template, flash, redirect, url_for, request

from webapp.db import db
from webapp.user.forms import LoginForm, RegistrationForm, SearchForm
from webapp.user.models import User
from webapp.parsing.models import ItemPrice, Item

blueprint = Blueprint('user', __name__, url_prefix='/user')


@blueprint.route("/login")
def login():
    if current_user.is_authenticated:
        return redirect(url_for('parsing.index'))
    title = "Авторизация"
    login_form = LoginForm()
    return render_template('user/login.html', page_title=title, form=login_form)


@blueprint.route("/process-login", methods=['POST'])
def process_login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter(User.username == form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash('Вы вошли на сайт')
            return redirect(url_for('parsing.index'))
        flash('Неправильное имя пользователя или пароль')
        return redirect(url_for('user.login'))


@blueprint.route('/logout')
def logout():
    logout_user()
    flash('Вы успешно разлогинились')
    return redirect(url_for('parsing.index'))


@blueprint.route('/register')
def register():
    if current_user.is_authenticated:
        return redirect(url_for('parsing.index'))
    title = "Регистрация"
    form = RegistrationForm()
    return render_template('user/registration.html', page_title=title, form=form)


@blueprint.route('/process_reg', methods=['POST'])
def process_reg():
    form = RegistrationForm()
    if form.validate_on_submit():
        news_user = User(username=form.username.data, email=form.email.data,
                         role='user')
        news_user.set_password(form.password.data)
        db.session.add(news_user)
        db.session.commit()
        flash('Вы успешно зарегистрировались!')
        return redirect(url_for('user.login'))
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash(f'Ошибка в поле "{getattr(form, field).label.text}":'
                      f' - {error}')
    flash('Пожалуйста, исправьте ошибки в форме')
    return redirect(url_for('user.register'))


@blueprint.route('/user_account', methods=['POST', 'GET'])
def user_account():
    form = SearchForm()
    title = 'Личный кабинет'
    if form.validate_on_submit():

        #entered_data = request.form['entered_data']
        #article = User(enter_data=form.entered_data.data)
        article = form.entered_data.data
        return article
        # try:
        #     db.session.add(article)
        #     db.session.commit()
        #     return article
        #     #return redirect(url_for('/result_search'))
        # except:
        #     #return article
        #     return "Данный товар недоступен для парсинга"
    else:
        return render_template('user/user_account.html', page_title=title,
                               form=form)
    # if search_form.validate_on_submit():
    #     entered_data = User.query.filter(User.enter_data == search_form.entered_data.data)
    #     db.session.add(entered_data)
    #     db.session.commit()
    #     flash('Подождите')
    #     redirect(url_for('user.result_search'))



@blueprint.route('/result_search')
def result_search():
    title = 'Результаты поиска'
    search_form = SearchForm()
    item = Item.query.all()
    price = ItemPrice.query.all()
    return render_template('user/result_search.html', form=search_form,
                           page_title=title, item=item, price=price)





