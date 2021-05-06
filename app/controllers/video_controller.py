from app import db
from app.models.video import Video
from app.models.rental import Rental
from app.models.customer import Customer
import json
from flask import make_response, jsonify


class Video_Controller():

    @classmethod
    def get_all(cls):
        videos = Video.query.all()
        response = []
        for video in videos:
            json = cls.video_json(video)
            response.append(json)
        return make_response(jsonify(response), 200)

    @classmethod
    def create(cls, data):
        errors = cls.validate_data(data)
        if errors:
            return make_response(errors, 400)
        new_video = Video(title = data["title"], release_date = data["release_date"], inventory = data["total_inventory"])
        db.session.add(new_video)
        db.session.commit()
        json = cls.video_json(new_video)
        return make_response(json, 201)


    @classmethod
    def get_one(cls, video_id):
        video = Video.query.get(video_id)
        if not video:
            error = {"errors":["Not Found"]}
            return make_response(error, 400)
        json = cls.video_json(video)
        return make_response(json, 200)

    @classmethod
    def edit(cls, video_id, data):
        video = Video.query.get(video_id)
        if not video:
            error = {"errors":["Not Found"]}
            return make_response(error, 400)
        errors = cls.validate_data(data)
        if errors:
            return make_response(errors, 400)
        video.title = data["title"]
        video.release_date = data["release_date"]
        video.inventory = data["total_inventory"]
        db.session.commit()
        json = cls.video_json(video)
        return make_response(json, 200)

    @classmethod
    def delete(cls, video_id):
        video = Video.query.get(video_id)
        if not video:
            error = {"errors":["Not Found"]}
            return make_response(error, 400)
        db.session.delete(video)
        db.session.commit()
        result = {"details": f"Video {video_id} \"{video.title}\" successfully deleted"}
        return make_response(result, 200)

    @classmethod
    def list_rental_customers(cls, video_id):
        db_results = db.session.query(Video, Rental, Customer)\
            .join(Rental, Rental.video_id==Video.video_id)\
            .join(Customer, Rental.customer_id==Customer.customer_id)\
            .filter(Video.video_id == video_id).all()
        result = []
        for element in db_results:
            customer = element[2]
            rental = element[1]
            #print(element[2])
            json = customer.to_json()
            #json.pop("inventory")
            json["due_date"] = rental.due_date
            result.append(json)

        return make_response(jsonify(result), 200)

    # CLASS HELPER METHODS
    @classmethod
    def validate_data(cls, data):
        errors = {}
        if "title" not in data:
            errors["title"] = "can't be blank"
        if "release_date" not in data:
            errors["release_date"] = "can't be blank"
        if "total_inventory" not in data:
            errors["total_inventory"] = "can't be blank"
        
        #TODO: add error checking for correct formatting :-)
        if errors:
            return {"errors":errors}

    @classmethod
    def video_json(cls, video):
        json = video.to_json()
        rentals = Rental.query.filter_by(video_id = video.video_id).count()
        checked_out_count = rentals
        total_inventory = json["inventory"]
        json.pop("inventory")
        json["total_inventory"] = total_inventory
        json["available_inventory"] = total_inventory - checked_out_count
        return json   