from app import db
from datetime import datetime

class Subscription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sub_id = db.Column(db.String(12), unique=True, nullable=False)
    name = db.Column(db.String(128), nullable=False)
    active_status = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return '{}'.format(self.name)