from flask import request, jsonify, Blueprint

api = Blueprint('api', __name__, url_prefix='/api/v1')

@api.route("/", methods=['GET'])
def root():
    """
    Root entrypoint
    :return: str
    """
    num = 123

    numfloat = float(num)
    return jsonify({'result': numfloat}), 200
