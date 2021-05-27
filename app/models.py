from app import db
from datetime import datetime

class Subscription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sub_id = db.Column(db.String(12), unique=True, nullable=False)
    name = db.Column(db.String(128), nullable=False)
    email_id = db.Column(db.String(128))
    active_status = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return '{}'.format(self.name)

class SubChange(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time_of_change = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    sub_id = db.Column(db.Integer, db.ForeignKey('subscription.id'))
    prev_name = db.Column(db.String(128), nullable=False)
    new_name = db.Column(db.String(128), nullable=False)
    prev_status = db.Column(db.Boolean, nullable=False)
    new_status = db.Column(db.Boolean, nullable=False)
    prev_sub_id = db.Column(db.String(12), nullable=False)
    new_sub_id = db.Column(db.String(12), nullable=False)
    prev_email_id = db.Column(db.String(128))
    new_email_id = db.Column(db.String(128))