from app import db
from app.models.video import Video
from app.models.customer import Customer
from app.models.rental import Rental
import json
from flask import make_response, jsonify
from datetime import datetime, timedelta


class Rental_Controller():

    @classmethod
    def check_out(cls, data):
        errors = cls.validate_data(data)
        if errors:
           return(make_response(errors, 400))
        rental = Rental.query.get((data["customer_id"], data["video_id"]))
        if rental:
            return(make_response({"errors":"Video is already checked out to Customer"}, 400))
        
        video = Video.query.get(data["video_id"])
        rentals = Rental.query.filter_by(video_id = video.video_id).count()
        if rentals + 1 > video.inventory:
            return(make_response({"errors":"Insufficient inventory available"}, 400))
        due_date = datetime.now() + timedelta(days=7)
        new_rental = Rental(customer_id = data["customer_id"], video_id = data["video_id"], due_date = due_date)
        db.session.add(new_rental)
        db.session.commit()

        json = cls.rental_json(new_rental)
        return make_response(json, 200)

        

    @classmethod
    def check_in(cls, data):
        errors = cls.validate_data(data)
        if errors:
           return(make_response(errors, 400))
        rental = Rental.query.get((data["customer_id"], data["video_id"]))
        if not rental:
            return(make_response({"errors":"No such rental"}))
        db.session.delete(rental)
        db.session.commit()
        json = cls.rental_json(rental)
        json.pop("due_date")
        return make_response(json, 200)
        
    @classmethod
    def list_rentals(cls, customer_id):
        db_results = db.session.query(Video, Rental, Customer)\
            .join(Rental, Rental.video_id==Video.video_id)\
            .join(Customer, Rental.customer_id==Customer.customer_id)\
            .filter(Customer.customer_id == customer_id).all()
        result = []
        for element in db_results:
            video = element[0]
            rental = element[1]
            #print(element[2])
            json = video.to_json()
            json.pop("inventory")
            json["due_date"] = rental.due_date
            result.append(json)

        return make_response(jsonify(result), 200)

    @classmethod
    def rental_json(cls, rental):
        json = rental.to_json()
        customer_rentals = Rental.query.filter_by(customer_id = rental.customer_id).count()
        videos_rented = Rental.query.filter_by(video_id = rental.video_id).count()
        video = Video.query.get(rental.video_id)
        json["videos_checked_out_count"] = customer_rentals
        json["available_inventory"] = video.inventory - videos_rented
        return json
        
    @classmethod
    def validate_data(cls, data):
        errors = {}
        if "customer_id" not in data:
            errors["customer_id"] = "required"
        if "video_id" not in data:
            errors["video_id"] = "required"

        if "customer_id" in data:
            customer = Customer.query.get(data["customer_id"])
            if not customer:
                id = data["customer_id"]
                errors["customer_id"] = f"Customer {id} does not exist"
        if "video_id" in data:
            video = Video.query.get(data["video_id"])
            if not video:
                id = data["video_id"]
                errors["video_id"] = f"Video {id} does not exist"
        
        #TODO: add error checking for correct formatting :-)
        if errors:
            return {"errors":errors}