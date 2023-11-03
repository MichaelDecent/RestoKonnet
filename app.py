#!/usr/bin/python3
from os import getenv
from models import storage
from flask import Flask, make_response, jsonify
from api.v1.views import app_views
from flask_cors import CORS
from flask_jwt_extended import JWTManager


app = Flask(__name__)

app.register_blueprint(app_views)
cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
app.config['JWT_SECRET_KEY'] = getenv('JWT_SECRET_KEY', 'you-cant-see-me')
jwt = JWTManager(app)

@app.teardown_appcontext
def close_db(error):
    """ Close Storage """
    storage.close()

host = getenv('RESTOKONNECT_API_HOST', '0.0.0.0')
port = getenv('RESTOKONNECT_API_PORT', '5000')

app.run(host=host, port=port, threaded=True)
