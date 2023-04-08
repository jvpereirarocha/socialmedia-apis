import json
from flask import jsonify, Blueprint
from instagram.entrypoint.requester import InstagramRequestAPI
from instagram.entrypoint.serializers import InstagramSerializer


instagram = Blueprint("api", __name__, url_prefix="/instagram")


@instagram.route("/get_user_id/<username>", methods=["GET"])
def get_user_id_by_instagram_user_name(username: str) -> dict:
    custom_api = InstagramRequestAPI(endpoint=f"get_user_id", query_params={"username": username})
    response = custom_api.get()
    serializer = InstagramSerializer(data=json.loads(response.text))
    data = serializer.serialized_data()
    return jsonify(data), 200


@instagram.route("/get_user_information/<user_id>", methods=["GET"])
def get_user_detailed_informations_by_user_id(user_id: str) -> dict:
    custom_api = InstagramRequestAPI(endpoint=f"email_and_details", query_params={"userid": user_id})
    get_infos = custom_api.get()
    response = get_infos.text
    return jsonify(response), 200