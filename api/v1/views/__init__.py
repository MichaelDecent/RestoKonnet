#!/usr/bin/python3
from flask import Blueprint, request
from api.v1.auth import Auth


app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")


@app_views.before_request
def before_request():
    print(request.endpoint)
    Auth.token_required(request.endpoint)

from api.v1.views.customers import *
from api.v1.views.vendors import *
from api.v1.views.restaurants import *
from api.v1.views.items import *
from api.v1.views.reviews import *
from api.v1.views.orders import *
from api.v1.views.cart_items import *
