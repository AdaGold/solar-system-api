from app import db
from app.models.customer import Customer
from app.models.rental import Rental
from app.models.video import Video
import json
from flask import make_response, jsonify
from datetime import datetime

class Customer_Controller():

    @classmethod
    def get_all(cls):
        customers = Customer.query.all()
        response = []
        for customer in customers:
            json = cls.customer_json(customer)
            response.append(json)
        return make_response(jsonify(response), 200)

    @classmethod
    def create(cls, data):
        errors = cls.validate_data(data)
        if errors:
            return make_response(errors, 400)
        new_customer = Customer(name = data["name"], postal_code = data["postal_code"], phone = data["phone"], registered_at = datetime.now())
        db.session.add(new_customer)
        db.session.commit()
        json = cls.customer_json(new_customer)
        return make_response(json, 200)


    @classmethod
    def get_one(cls, customer_id):
        customer = Customer.query.get(customer_id)
        if not customer:
            error = {"errors":["Not Found"]}
            return make_response(error, 400)
        json = cls.customer_json(customer)
        return make_response(json, 200)

    @classmethod
    def edit(cls, customer_id, data):
        customer = Customer.query.get(customer_id)
        if not customer:
            error = {"errors":["Not Found"]}
            return make_response(error, 400)
        errors = cls.validate_data(data)
        if errors:
            return make_response(errors, 400)
        customer.name = data["name"]
        customer.postal_code = data["postal_code"]
        customer.phone = data["phone"]
        db.session.commit()
        json = cls.customer_json(customer)
        return make_response(json, 200)

    @classmethod
    def delete(cls, customer_id):
        customer = Customer.query.get(customer_id)
        if not customer:
            error = {"errors":["Not Found"]}
            return make_response(error, 400)
        db.session.delete(customer)
        db.session.commit()
        result = {"details": f"Customer {customer_id} \"{customer.name}\" successfully deleted"}
        return make_response(result, 200)

    # CLASS HELPER METHODS
    @classmethod
    def validate_data(cls, data):
        print(data)
        errors = {}
        if "name" not in data:
            errors["name"] = "can't be blank"
        if "postal_code" not in data:
            errors["postal_code"] = "can't be blank"
        if "phone" not in data:
            errors["phone"] = "can't be blank"
        
        #TODO: add error checking for correct formatting :-)
        if errors:
            return {"errors":errors}

    @classmethod
    def customer_json(cls, customer):
        json = customer.to_json()
        rentals = Rental.query.filter_by(customer_id = customer.customer_id).count()
        print(rentals)
        json["videos_checked_out_count"] = rentals
        return json   
    
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