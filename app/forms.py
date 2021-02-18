from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(message='please enter a valid email')])
    subject = StringField('Subject' )
    message = TextAreaField('Message' )
    submit = SubmitField('Send Message')