#!/usr/bin/python3
"""
This is a module that handles creation of forms using Python's WTF library
and Bootstrap
""" 
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    """Class to create User Registration form"""
    firstname = StringField('First Name',
                                  validators=[DataRequired(),
                                              Length(min=3, max=32)],
                                  id='firstname', name='firstname')
    lastname = StringField('Last Name',
                                  validators=[DataRequired(),
                                              Length(min=3, max=32)],
                                  id='lastname', name='lastname')
    email = StringField('Email ID', validators=[DataRequired(),
                                                      Email()],
                        id='email', name='email')
    password = PasswordField('Password', validators=[DataRequired()],
                             id='password', name='password')
    password_confirm = PasswordField('Confirm Password',
                                     validators=[DataRequired(),
                                                 EqualTo('password')],
                                     id='password_confirm',
                                     name='password_confirm')
    submit = SubmitField('Register')
    
    
class UserLoginForm(FlaskForm):
    """Class to create Login form"""
    email = StringField('Email ID', validators=[DataRequired(),
                                                      Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
    
  