

from flask import Flask
from app.routers import api_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(api_bp)

    app.config['JSON_SORT_KEYS'] = False

    return app

