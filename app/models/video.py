from flask import current_app
from app import db


class Video(db.Model):
    video_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    release_date = db.Column(db.DateTime)
    inventory = db.Column(db.Integer)

    def to_json(self):
        json = {}
        json["id"] = self.video_id
        json["title"] = self.title
        json["release_date"] = self.release_date
        json["inventory"] = self.inventory

        return json
