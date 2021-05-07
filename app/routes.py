import json
from flask import request, jsonify, Blueprint, Response, make_response
from datetime import datetime
import requests
from app.controllers.customer_controller import Customer_Controller
from app.controllers.video_controller import Video_Controller
from app.controllers.rental_controller import Rental_Controller
from app.api_description import api_description


# Index Route
index_bp = Blueprint("index_bp", __name__, url_prefix = "/")
@index_bp.route("", methods=["GET"])
def index():
    return make_response({"name":"Video Store API", "message":"Everything you need to run your retro video store.", "API Description":api_description}, 200)


# Customer CRUD Routes
customer_bp = Blueprint("customer_bp", __name__, url_prefix="/customers")
@customer_bp.route("", methods=["POST", "GET"])
def customers():
    if request.method == "POST":
        return Customer_Controller.create(request.get_json())
    elif request.method == "GET":
        return Customer_Controller.get_all()

@customer_bp.route("<customer_id>", methods=["PUT", "DELETE", "GET"])
def single_customer(customer_id):
    if request.method == "PUT":
        return Customer_Controller.edit(customer_id, request.get_json())
    elif request.method == "DELETE":
        return Customer_Controller.delete(customer_id)
    elif request.method == "GET":
        return Customer_Controller.get_one(customer_id)

@customer_bp.route("<customer_id>/rentals", methods=["GET"])
def list_rentals(customer_id):
    return Customer_Controller.list_rentals(customer_id)

# Video CRUD Routes
video_bp = Blueprint("video_bp", __name__, url_prefix="/videos")
@video_bp.route("", methods=["POST", "GET"])
def videos():
    if request.method == "POST":
        return Video_Controller.create(request.get_json())
    elif request.method == "GET":
        return Video_Controller.get_all()

@video_bp.route("<video_id>", methods=["PUT", "DELETE", "GET"])
def single_video(video_id):
    if request.method == "PUT":
        return Video_Controller.edit(video_id, request.get_json())
    elif request.method == "DELETE":
        return Video_Controller.delete(video_id)
    elif request.method == "GET":
        return Video_Controller.get_one(video_id)

@video_bp.route("<video_id>/rentals", methods=["GET"])
def list_rental_customers(video_id):
    return Video_Controller.list_rental_customers(video_id)


#Rental Custom Routes
rental_bp = Blueprint("rental_bp", __name__, url_prefix="/rentals")
@rental_bp.route("check-out", methods=["POST"])
def check_out():
    return Rental_Controller.check_out(request.get_json())

@rental_bp.route("check-in", methods=["POST"])
def check_in():
    return Rental_Controller.check_in(request.get_json())
    

