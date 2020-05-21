import jwt
from flask import g
from SETTINGS import APP_SECRET
from custom_exceptions import UserNotFound, UserAlreadyRegistered
from database import user_integer_map


def generate_token(email):
    return jwt.encode({'email': email}, APP_SECRET, algorithm='HS256')


def sign_up(data):
    email = data.get("email")
    if email in user_integer_map:
        raise UserAlreadyRegistered

    password = data.get("password")
    api_key = generate_token(email)
    user_integer_map[email] = {
        "email": email,
        "integer_value": 0,
        "API_KEY": api_key,
        "password": password
    }

    return api_key


def sign_in(data):
    email = data.get("email")
    password = data.get("password")
    if email not in user_integer_map or user_integer_map[email]["password"] != password:
        raise UserNotFound

    api_key = generate_token(email)
    user_integer_map[email]["API_KEY"] = api_key

    return api_key


def sign_out():
    user_integer_map[g.email]["API_KEY"] = None
