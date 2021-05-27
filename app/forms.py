from app import models
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, SelectField, SubmitField, BooleanField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired

class SearchIDForm(FlaskForm):
    sub_id = StringField('Document ID')
    name = StringField('Name')
    submit = SubmitField('Submit')

class AddSubscriptionForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    sub_id = StringField('Document ID', validators=[DataRequired()])
    email_id = StringField('Discord ID', validators=[DataRequired()])
    submit = SubmitField('Submit')

class RenewSubscriptionForm(FlaskForm):
    active_status = BooleanField('Active Status')
    submit = SubmitField('Submit')

class ResetAllSubscriptionsForm(FlaskForm):
    reset = StringField('Please type "Reset" into this box to reset all subscriptions.')
    submit = SubmitField('Submit')


class DeleteSubscriptionForm(FlaskForm):
    delete = StringField('Please type "Delete" into this box to delete the subscription.')
    submit = SubmitField('Submit')

class DeleteAllForm(FlaskForm):
    delete = StringField('Please type the password into this box to delete all data.')
    submit = SubmitField('Submit')