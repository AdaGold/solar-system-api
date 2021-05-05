from app import db
from app.models.video import Video
from app.models.video import Rental
import json

class Video_Controller():

    @classmethod
    def get_all(cls):
        videos = Video.query.all()
        response = []
        for video in videos:
            json = cls.video_json(video)
        return make_reponse(response, 200)

    @classmethod
    def create(cls, data):
        errors = cls.validate_data(data)
        if errors:
            return make_response(errors, 400)
        new_video = Video(name = data["name"], postal_code = data["postal_code"], phone = data["phone"], registered_at = datetime.now())
        db.session.add(new_video)
        db.session.commit()
        json = cls.video_json(new_video)
        return make_response(json, 201)


    @classmethod
    def get_one(cls, id):
        video = Video.query.get(video_id)
        if not video:
            error = {"errors":["Not Found"]}
            return make_response(error, 400)
        json = cls.video_json(video)
        return make_response(json, 200)

    @classmethod
    def edit(cls, id, data):
        video = Video.query.get(video_id)
        if not video:
            error = {"errors":["Not Found"]}
            return make_response(error, 400)
        errors = cls.validate_data(data)
        if errors:
            return make_response(errors, 400)
        video.name = data["name"]
        video.postal_code = data["postal_code"]
        video.phone = data["phone"]
        json = cls.video_json(new_video)
        return make_response(json, 200)

    @classmethod
    def delete(cls, id):
        video = Video.query.get(video_id)
        if not video:
            error = {"errors":["Not Found"]}
            return make_response(error, 400)
        db.session.delete(video)
        db.session.commit()
        result = {"details": f"Video {id} \"{video.name}\" successfully deleted"}
        return make_response(result, 200)

    # CLASS HELPER METHODS
    @classmethod
    def validate_data(cls, data):
        errors = {}
        if "title" not in data:
            errors["title"] = "can't be blank"
        if "release_date" not in data:
            errors["release_date"] = "can't be blank"
        
        #TODO: add error checking for correct formatting :-)
        if errors:
            return {"errors":errors}

    @classmethod
    def video_json(cls, video):
        json = video.to_json()
        rentals = Rental.query.filter_by(video_id = video.video_id)
        checked_out_count = len(rentals)
        total_inventory = json["inventory"]
        json.pop("inventory")
        json["total_inventory"] = total_inventory
        json["available_inventory"] = total_inventory - checked_out_count
        return json   