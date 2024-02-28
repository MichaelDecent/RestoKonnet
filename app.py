#!/usr/bin/python3
from os import getenv
from models import storage
from flask import Flask, jsonify
from api.v1.views import app_views
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_swagger_ui import get_swaggerui_blueprint


app = Flask(__name__)

app.register_blueprint(app_views)
cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
app.config["JWT_SECRET_KEY"] = getenv("JWT_SECRET_KEY", "you-cant-see-me")
jwt = JWTManager(app)

SWAGGER_URL = "/api/v1/swagger"
API_URL = "http://petstore.swagger.io/v2/swagger.json"

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={"app_name": "RestoKonnect API"},
)
app.register_blueprint(swaggerui_blueprint)


@app.route("/", methods=["GET"], strict_slashes=False)
def home():
    """home route"""
    return jsonify({"Home": "Welcome to RestoKonnect API"})


@app.teardown_appcontext
def close_db(error):
    """Close Storage"""
    storage.close()


if __name__ == ("__main__"):
    app.run(host="0.0.0.0", port=5000, threaded=True)
