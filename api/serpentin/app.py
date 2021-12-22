from flask import Flask
from flask_cors import CORS
from serpentin.api import register_api
from serpentin.core.database import connect_to_database


def create_app():
    app = Flask("serpentin")
    app.config["ENV"] = "development"

    # CORS
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}}) # fix cors issue on Firefox
    # API
    register_api(app)

    # Database
    connect_to_database()

    return app
