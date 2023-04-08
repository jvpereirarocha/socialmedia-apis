from flask import Flask, Blueprint
from app.rest.instagram import instagram as api_instagram


api_v1 = Blueprint("api_v1", __name__, url_prefix="/api/v1")


def create_app(environment: str = "production"):
    app = Flask(__name__)
    app.config.from_object(f'app.configs.environments.{environment}.Config')
    api_v1.register_blueprint(api_instagram)
    app.register_blueprint(api_v1)

    return app