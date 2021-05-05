from flask import current_app
from app import db


class Customer(db.Model):
    customer_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    registered_at = db.Column(db.DateTime)
    postal_code = db.Column(db.String)
    phone = db.Column(db.String)

    def to_json(self):
        json = {}
        json["id"] = self.customer_id
        json["name"] = self.name
        json["registered_at"] = self.registered_at
        json["postal_code"] = self.postal_code
        json["phone"] = self.phone

        return json
