from app import models
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, SelectField, SubmitField, BooleanField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired

class SearchIDForm(FlaskForm):
    sub_id = StringField('Subscription ID')
    name = StringField('Name')
    submit = SubmitField('Submit')

class AddSubscriptionForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    sub_id = StringField('Subscription ID', validators=[DataRequired()])
    submit = SubmitField('Submit')

class RenewSubscriptionForm(FlaskForm):
    active_status = BooleanField('Active Status')
    submit = SubmitField('Submit')

class ResetAllSubscriptionsForm(FlaskForm):
    reset = StringField('Please type "Reset" into this box to reset all subscriptions.')
    submit = SubmitField('Submit')