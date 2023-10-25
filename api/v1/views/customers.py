#!/usr/bin/python3
"""
This Handles all the api Restful actions for Customers
"""
from flask import jsonify, request, make_response
from api.v1.views import app_views
from models.customer import Customer
from models import storage
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token
from datetime import timedelta
from api.v1.errors import error_response, bad_request, not_found


@app_views.route('/customer_login', methods=['POST'], strict_slashes=False)
def customer_login():
    """ This returns a token for an authenticated customer """

    json_request = request.get_json()

    if not json_request:
        return bad_request("Not a JSON")
    if 'phone_no' not in json_request:
        return bad_request("Missing Phone Number")
    
    for customer in storage.all(Customer).values():
        if customer.phone_no == json_request['phone_no']:
            expires = timedelta(seconds=3600)
            access_token = create_access_token(identity=customer.phone_no, expires_delta=expires)
            return make_response(jsonify({'access_token': access_token}), 200)

    return bad_request("Invalid credentials")


@app_views.route('/customers', methods=['GET'], strict_slashes=False)
@jwt_required()
def get_customers():

    """This retrieves a list all customers"""
    customers_list = [cust.to_dict() for cust in storage.all(Customer).values()]
    return jsonify(customers_list)

    
@app_views.route('/customers/<customer_id>', methods=['GET'], strict_slashes=False)
def get_customer(customer_id):
    """This retrieves a customer based on its id"""

    customer = storage.get(Customer, customer_id)
    if not customer:
        return not_found("customer not found")
    return jsonify(customer.to_dict())


@app_views.route('/customers', methods=['POST'], strict_slashes=False)
def post_customer():
    """This creates a new customer object"""

    json_request = request.get_json()

    if not json_request:
        return bad_request("Not JSON")

    required = ['name', 'phone_no', 'address', 'email']
    for val in required:
        if val not in json_request:
            return bad_request(f"Missing {val}")

    for cust in storage.all(Customer).values():
        if json_request['email'] == cust.email:
            return bad_request("Email Already Exist")
        if json_request['phone_no'] == cust.phone_no:
            return bad_request("Phone Already Exist")

    customer = Customer(**json_request)
    customer.save()
    return make_response(jsonify(customer.to_dict()), 201)
    


@app_views.route('/customers/<customer_id>', methods=['PUT'], strict_slashes=False)
def put_customer(customer_id):
    """Updates a particular customer's attributes"""

    customer = storage.get(Customer, customer_id)
    if not customer:
        return not_found()
    json_request = request.get_json()
    if not json_request:
        return bad_request("Not JSON")
    ignore_list = ['id', 'updated_at', 'created_at']

    for key, value in json_request.items():
        if key not in ignore_list:
            setattr(customer, key, value)

    storage.save()
    return make_response(jsonify(customer.to_dict()), 200)


@app_views.route('/customers/<customer_id>', methods=['DELETE'], strict_slashes=False)
def delete_customer(customer_id):
    """Deletes a paticular customer object """

    customer = storage.get(Customer, customer_id)
    if not customer:
        return not_found()
    
    storage.delete(customer)
    storage.save()

    return make_response(jsonify({}), 200)
  