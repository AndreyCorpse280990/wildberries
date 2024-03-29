from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, \
    Length

from webapp.user.models import User


class LoginForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()],
                           render_kw={"class": "form-control"})
    password = PasswordField('Пароль', validators=[DataRequired()],
                             render_kw={"class": "form-control"})
    remember_me = BooleanField("Запомнить меня", default=True,
                               render_kw={"class": "form-check-input"})
    submit = SubmitField('Отправить', render_kw={"class": "btn btn-primary"})


class RegistrationForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()],
                           render_kw={"class": "form-control"})
    email = StringField('Электронная почта', validators=[DataRequired(),
                                                         Email()],
                        render_kw={"class": "form-control"})
    password = PasswordField('Пароль',
                             validators=[DataRequired(),
                                         Length(min=4, max=16)],
                             render_kw={"class": "form-control"})
    password2 = PasswordField('Повторите пароль',
                              validators=[DataRequired(),
                                          Length(min=4, max=16),
                                          EqualTo('password',
                                                  message='Пароли не совпадают')],
                              render_kw={"class": "form-control"})
    submit = SubmitField('Отправить', render_kw={"class": "btn btn-primary"})


    def validate_username(self, username):
        user_count = User.query.filter_by(username=username.data).count()
        if user_count > 0:
            raise ValidationError(
                'Пользователь с такими именем уже зарегистрирован')

    def validate_email(self, email):
        user_count = User.query.filter_by(email=email.data).count()
        if user_count > 0:
            raise ValidationError(
                'Пользователь с таким email уже зарегистрирован')


class SearchForm(FlaskForm):
    entered_data = StringField('Название товара', validators=[DataRequired()],
                               render_kw={"class": "form-control"})
    submit = SubmitField('Отправить', render_kw={"class": "btn btn-primary"})
