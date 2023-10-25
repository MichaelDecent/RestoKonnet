#!/usr/bin/python3
"""
This Handles all the api Restful actions for Restaurants
"""
from flask import jsonify, request, make_response
from api.v1.views import app_views
from models import storage
from models.vendor import Vendor
from models.restaurant import Restaurant
from api.v1.errors import error_response, bad_request, not_found


@app_views.route('/restaurants', methods['GET'], strict_slashes=False)
def get_restaurants():
    """This retrieves a list all restaurants"""

    restaurants_list = [rest.to_dict() for rest in storage.all(Restaurant).values()]
    return jsonify(restaurants_list)

@app_views.route('/restaurants/<restaurant_id>', methods=['GET'], strict_slashes=False)
def get_restaurant(restaurant_id):
    """This retrieves a restaurant based on its id"""

    restaurant = storage.get(Restaurant, restaurant_id)
    if not restaurant:
        return not_found("restaurant does not exist")
    return jsonify(restaurant.to_dict())

@app_views.route('/vendors/<vendor_id>/restaurants', methods=['POST'], strict_slashes=False)
def post_restaurant(vendor_id):
    """ This creates a new restaurant object """

    vendor = storage.get(Vendor, vendor_id)
    if not vendor:
        return not_found("vendor does not exist")
    
    if vendor.restaurants is not None:
        return error_response("Vendor Already created Restaurant")

    json_request = request.get_json()
    if not json_request:
        bad_request("Not a JSON")

    required = ['name', 'address']
    for val in required:
        if val not in json_request:
            return bad_request(f"Missing {val}")

    for rest in storage.all(Restaurant).values():
        if json_request['name'] == rest.name:
            bad_request("Name Already Exist")
    
    restaurant = Restaurant(**json_request)
    restaurant.save()

    return make_response(jsonify(restaurant.to_dict()), 201)

@app_views.route('/restaurants/<restaurant_id>', methods=['PUT'], strict_slashes=False)
def put_restaurant(restaurant_id):
    """Updates a particular restaurant's attributes"""

    restaurant = storage.get(Restaurant, restaurant_id)
        if not restaurant:
            return not_found("restaurant does not exist")

    json_request = request.get_json()
    if not json_request:
        return bad_request("Not JSON")
    ignore_list = ['id', 'updated_at', 'created_at']

    for key, value in json_request.items():
        if key not in ignore_list:
            setattr(restaurant, key, value)

    storage.save()
    return make_response(jsonify(restaurant.to_dict()), 201)


@app_views.route('/restaurants/<restaurant_id>', methods=['DELETE'], strict_slashes=False)
def delete_restaurant(restaurant_id):
    """Deletes a paticular restaurant object """

     restaurant = storage.get(Restaurant, restaurant_id)
        if not restaurant:
            return not_found()
    
    storage.delete(restaurant)
    storage.save()

    return make_response(jsonify({}), 200)
