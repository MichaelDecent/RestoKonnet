"""
This Handles all the api Restful actions for Vendors
"""
from flask import jsonify, request, make_response
from api.v1.views import app_views
from models.vendor import Vendor
from models import storage
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token
from datetime import timedelta
from api.v1.errors import error_response, bad_request, not_found
from werkzeug.security import check_password_hash


@app_views.route('/vendor_login', methods=['POST'], strict_slashes=False)
def vendor_login():
    """ This returns a token for an authenticated vendor """

    form_request = request.form

    if not form_request:
        return bad_request("Not a JSON")
    if 'email' not in form_request:
        return bad_request("Missing Email")

    if 'password' not in form_request:
        return bad_request("Missing Password")

    for vendor in storage.all(Vendor).values():
        if vendor.email == form_request['email'] and check_password_hash(vendor.password, form_request['password']):
            expires = timedelta(seconds=3600)
            access_token = create_access_token(identity=vendor.email, expires_delta=expires)
            return make_response(jsonify({'access_token': access_token, 'id': vendor.id}), 200)

    return bad_request("Invalid credentials")


@app_views.route('/vendors', methods=['GET'], strict_slashes=False)
def get_vendors():
    """This retrieves a list all vendors"""

    vendors_list = [vendor.to_dict() for vendor in storage.all(Vendor).values()]
    return jsonify(vendors_list)

    
@app_views.route('/vendors/<vendor_id>', methods=['GET'], strict_slashes=False)
def get_vendor(vendor_id):
    """This retrieves a vendor based on its id"""

    vendor = storage.get(Vendor, vendor_id)
    if not vendor:
        return not_found("vendor does not exist")
    return jsonify(vendor.to_dict())


@app_views.route('/vendors', methods=['POST'], strict_slashes=False)
def post_vendor():
    """This creates a new vendor object"""

    form_request = request.form

    if not form_request:
        return bad_request("Not form-data")
    
    required = ['name', 'address', 'email', 'password', 'phone_no']
    for val in required:
        if val not in form_request:
            return bad_request(f"Missing {val}")


    for ven in storage.all(Vendor).values():
        if form_request['email'] == ven.email:
            return bad_request("Email Already Exist")
        if form_request['password'] == ven.password:
            return bad_request("Phone Already Exist")

    vendor = Vendor(**form_request)
    vendor.save()
    return make_response(jsonify(vendor.to_dict()), 200)

@app_views.route('/vendors/<vendor_id>', methods=['PUT'], strict_slashes=False)
def put_vendor(vendor_id):
    """Updates a particular vendor's attributes"""

    vendor = storage.get(Vendor, vendor_id)
    if not vendor:
        return not_found()
    form_request = request.form
    if not form_request:
        return bad_request("Not form-data")
    ignore_list = ['id', 'updated_at', 'created_at']

    for key, value in form_request.items():
        if key not in ignore_list:
            setattr(vendor, key, value)

    storage.save()
    return make_response(jsonify(vendor.to_dict()), 201)


@app_views.route('/vendors/<vendor_id>', methods=['DELETE'], strict_slashes=False)
def delete_vendor(vendor_id):
    """Deletes a paticular vendor object """

    vendor = storage.get(Vendor, vendor_id)
    if not vendor:
        return not_found("vendor does not exist")
    
    storage.delete(vendor)
    storage.save()

    return make_response(jsonify({}), 200)
  
