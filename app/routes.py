import json
from flask import request, jsonify, Blueprint, Response, make_response
from datetime import datetime
import requests
from app.controllers.customer_controller import Customer_Controller

# Index Route
index_bp = Blueprint("index_bp", __name__, url_prefix = "/")
@index_bp.route("", methods=["GET"])
def index():
    return make_response({"name":"Video Store API", "message":"Everything you need to run your retro video store."})


# Customer CRUD Routes
customer_bp = Blueprint("customer_bp", __name__, url_prefix="/customers")
@customer_bp.route("", methods=["POST", "GET"])
def customers():
    if request.method == "POST":
        return Customer_Controller.create(request.get_json())
    elif request.method == "GET":
        return Customer_Controller.get_all()

@customer_bp.route("<customer_id>", methods=["PUT", "DELETE", "GET"])
def single_customer():
    if request.method == "PUT":
        return Customer_Controller.edit(customer_id, request.get_json())
    elif request.method == "DELETE":
        return Customer_Controller.delete(customer_id)
    elif request.method == "GET":
        return Customer_Controller.get_one(customer_id)


# Video CRUD Routes
video_bp = Blueprint("video_bp", __name__, url_prefix="/Videos")
@video_bp.route("", methods=["POST", "GET"])
def videos():
    if request.method == "POST":
        return Video_Controller.create(request.get_json())
    elif request.method == "GET":
        return Video_Controller.get_all()
    else:
        #add error checking
        pass

@Video_bp.route("<video_id>", methods=["PUT", "DELETE", "GET"])
def single_video():
    if request.method == "PUT":
        return Video_Controller.edit(video_id, request.get_json())
    elif request.method == "DELETE":
        return Video_Controller.delete(video_id)
    elif request.method == "GET":
        return Video_Controller.get_one(video_id)
    else:
        #add error checking
        pass


#Rental Custom Routes
rental_bp = Blueprint("rental_bp", __name__, url_prefix="/rentals")
@rental_bp.route("check-out", methods=["POST"])
def check_out():
    if request.method == "POST":
        return Rental_Controller.check_out(request.get_json())
    else:
        #add error checking
        pass

@rental_bp.route("check-in", methods=["POST"])
def check_in():
    if request.method == "POST":
        return Rental_Controller.check_in(request.get_json())
    else:
        #add error checking
        pass
    

