import json
import jwt
from SETTINGS import APP_SECRET
from flask import Flask, request, jsonify
from middleware import verify_user
from custom_exceptions import UserNotFound, UserNotAuthenticated, NoDataProvided, UserAlreadyRegistered
from auth_controller import sign_out, sign_in, sign_up
from integer_controller import get_current_integer, get_incremented_integer, set_integer_value

app = Flask(__name__)
app.config["DEBUG"] = True


# middleware to inspect the request for API-KEY verification before it reaches the routes
@app.before_request
def verify_identity():
    try:
        verify_user(request)
    except UserNotAuthenticated:
        return jsonify({"success": False, "message": "User Not Authenticated"}), 401


@app.route('/sign_up', methods=["POST"])
def signup():
    try:
        if not request.data:
            raise NoDataProvided

        api_key = sign_up(json.loads(request.data))
        return jsonify({"api_key": api_key}), 200
    except UserAlreadyRegistered:
        return jsonify({"success": False, "message": "User Already Registered"}), 501


@app.route('/login', methods=["POST"])
def login():
    try:
        if not request.data:
            raise NoDataProvided

        data = json.loads(request.data)
        api_key = sign_in(data)
        return jsonify({"api_key": api_key}), 200
    except UserNotFound:
        return jsonify({"success": False, "message": "Email or password is wrong"}), 401


@app.route('/sign_out', methods=["GET"])
def signout():
    sign_out()
    return jsonify({"success": True}), 200


@app.route('/next', methods=["GET"])
def increment():
    next_integer = get_incremented_integer()
    return jsonify({"next_integer": next_integer}), 200


@app.route('/current', methods=["GET", "PUT"])
def current():
    if request.method == 'PUT':
        if not request.data:
            raise NoDataProvided
        set_integer_value(json.loads(request.data))
        return jsonify({"success": True}), 200
    else:
        integer = get_current_integer()
        return jsonify({"integer": integer}), 200


@app.errorhandler(404)
def not_found(message):
    return jsonify({"success": False, "message": str(message)}), 404


@app.errorhandler(NoDataProvided)
def not_found(message):
    return jsonify({"success": False, "message": "Please provide the data"}), 501


@app.errorhandler(Exception)
def not_found(message):
    return jsonify({"success": False, "message": str(message)}), 501


# runs on localhost on port 5000
app.run()
