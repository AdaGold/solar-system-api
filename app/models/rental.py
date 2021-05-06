from flask import current_app
from app import db


class Rental(db.Model):
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.customer_id'), primary_key=True)
    video_id = db.Column(db.Integer, db.ForeignKey('video.video_id'), primary_key=True)
    due_date = db.Column(db.DateTime)

    def to_json(self):
        json = {}
        json["customer_id"] = self.customer_id
        json["video_id"] = self.video_id
        json["due_date"] = self.due_date

        return json
