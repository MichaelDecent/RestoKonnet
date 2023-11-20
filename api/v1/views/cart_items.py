#!/usr/bin/python3
"""
This Handles all the api Restful actions for Reviews
"""
from flask import jsonify, request, make_response
from api.v1.views import app_views
from models import storage
from models.customer import Customer
from models.restaurant import Restaurant
from models.cart_item import CartItem
from models.vendor import Vendor
from api.v1.errors import error_response, bad_request, not_found

@app_views.route('/cart_items', methods=['GET'], strict_slashes=False)
def get_cart_item():
    """This retrieves a list all items in the cart of a particular customer"""
    form_request = request.form
    if not form_request:
        bad_request("Not a form-data")

    if 'customer_id' in form_request:
        customer = storage.get(Customer, form_request['customer_id'])
        if customer:
            carts_items = [cart.to_dict() for cart in customer.cart_items]
        else:
            return not_found("customer does not exist")

    elif 'vendor_id' in form_request:
        vendor = storage.get(Vendor, form_request['vendor_id'])
        if vendor:
            carts_items = [cart.to_dict() for cart in vendor.cart_items]
        else:
            return not_found("vendor does not exist")
    else:
        return not_found("Missing customer_id or vendor_id does not exist")
    return (carts_items)


@app_views.route('/cart_items', methods=['POST'], strict_slashes=False)
def post_cart_item():
    """ This creates a new cart_item order """
    
    form_request = request.form
    if not form_request:
        bad_request("Not a form-data")

    required = ['item_name', 'item_price']
    for val in required:
        if val not in form_request:
            return bad_request(f"Missing {val}")
    
    if 'customer_id' in form_request:
        print("customer")
        customer = storage.get(Customer, form_request['customer_id'])
        print("customer")
        if customer:
            cart_item = CartItem(**form_request)
            cart_item.save()
        else:
            return not_found("customer does not exist")

    elif 'vendor_id' in form_request:
        print("vendor")
        vendor = storage.get(Vendor, form_request['vendor_id'])
        print("vendor")
        if vendor:
            cart_item = CartItem(**form_request)
            cart_item.save()
        else:
            return not_found("vendor does not exist")
    else:
        return not_found("Missing customer_id or vendor_id does not exist")

    return make_response(jsonify(cart_item.to_dict()), 201)


@app_views.route('/cart_items/<cart_item_id>', methods=['PUT'], strict_slashes=False)
def put_cart_item(cart_item_id):
    """Updates a particular customer cart_item attributes"""

    cart_item = storage.get(CartItem, cart_item_id)
    if not cart_item:
        return not_found("cart_item does not exist")

    form_request = request.form
    if not form_request:
        return bad_request("Not form-data")
    ignore_list = ['id', 'updated_at', 'created_at']

    for key, value in form_request.items():
        if key not in ignore_list:
            setattr(order, key, value)

    storage.save()
    return make_response(jsonify(cart_item.to_dict()), 201)


@app_views.route('/cart_items/<cart_item_id>', methods=['DELETE'], strict_slashes=False)
def delete_cart_item(cart_item_id):
    """Deletes a paticular cart_item object """

    cart_item = storage.get(CartItem, cart_item_id)
    if not cart_item:
        return not_found("cart_item does not exist")
    
    storage.delete(cart_item)
    storage.save()

    return make_response(jsonify({}), 200)
