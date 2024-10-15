from flask import jsonify

def register_error_handlers(app):
    @app.errorhandler(404)
    def not_found_error(error):
        return jsonify({"error": "Not Found"}), 404
