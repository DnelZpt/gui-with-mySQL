"""
This file contains the form for the client.

Daniel Zapata - 2024
"""

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired


class ClientForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    membership = IntegerField('Membership', validators=[DataRequired()])
    save = SubmitField('Save')
