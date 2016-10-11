from flask_wtf import FlaskForm
from wtforms import TextField,IntegerField,TextAreaField,SubmitField,RadioField,SelectField
from wtforms import validators,ValidationError
import requests
class ContactForm(FlaskForm):
    name=TextField("Name of Fucker",[validators.Required("Enter your name fucker")])
    Address=TextAreaField("Address")
    email=TextField("Email",[validators.Required("Enter your email"),validators.Email("Please enter valid email")])
    Age=IntegerField("age")
    language=SelectField("Language",choices=[('cpp','c++'),('py','python')])
    submit=SubmitField("Send")
