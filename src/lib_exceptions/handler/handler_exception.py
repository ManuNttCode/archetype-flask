from flask import current_app as app, jsonify

def register_errorhandlers(app):
    @app.errorhandler(Exception)
    def handle_exception(error):
        response = jsonify({'error': str(error)})
        response.status_code = 400
        return response