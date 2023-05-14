from flask import request, jsonify

def register_routes(app):
  @app.route("/", methods=['GET'])
  def root():
    """
    Root entrypoint
    :return: str
    """
    return jsonify({'result': 'Todo funcionando mi animalito de dios'}), 200