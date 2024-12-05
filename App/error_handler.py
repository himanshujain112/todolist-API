from flask import jsonify

def handle_404_error(e):
    return jsonify({
        "error" : "Resource not found",
        "message" : str(e)
    }), 404

def handle_400_error(e):
    return jsonify({
        "error" : "Bad request",
        "message" : str(e)
    }), 400

def handle_generic_error(e):
    return jsonify({
        "error": "Internal server error",
        "message" : "Something went wrong. Please try again later!"
    }), 500