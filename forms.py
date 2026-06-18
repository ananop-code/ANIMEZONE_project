from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, IntegerField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, equal_to, length
from flask_wtf.file import FileField


class RegisterForm(FlaskForm):
    username = StringField("Enter Username", validators=[DataRequired()])
    password = PasswordField("Enter Password", validators=[DataRequired(), length(min=6, max=24)])
    confirm_password = PasswordField("Confirm Password",
                                     validators=[DataRequired(), equal_to("password", message="not same")])
    register = SubmitField("Register")


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    login = SubmitField("Log In")


class AnimeForm(FlaskForm):
    image = FileField("Upload anime poster")
    title = StringField("Enter Anime Title", validators=[DataRequired()])
    release_year = IntegerField("Enter Anime Release Year", validators=[DataRequired()])

    description_en = TextAreaField("Description (English)", validators=[DataRequired()])
    description_ka = TextAreaField("აღწერა (ქართულად)", validators=[DataRequired()])
    description_ja = TextAreaField("説明 (日本語)", validators=[DataRequired()])

    submit = SubmitField("Save Anime")