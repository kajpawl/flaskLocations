from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class SignupForm(Form):
    first_name = StringField('First name', validators=[DataRequired("Please enter your first name.")])
    last_name = StringField('Last name', validators=[DataRequired("Please enter your last name.")])
    email = StringField('Email', validators=[DataRequired("Please enter your email address."),
                                             Email("Please make sure that email format is correct.")])
    password = PasswordField('Password', validators=[DataRequired("Please enter your password."),
                                                     Length(min=6, max=54,
                                                            message="Password must have 6 to 54 characters.")])
    submit = SubmitField('Sign up')


class LoginForm(Form):
    email = StringField('Email', validators=[DataRequired("Please enter your email address."),
                                             Email("Please make sure that email format is correct.")])
    password = PasswordField('Password', validators=[DataRequired("Please enter your password.")])
    submit = SubmitField('Sign in')
