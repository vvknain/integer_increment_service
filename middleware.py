import jwt
from flask import g
from SETTINGS import APP_SECRET
from custom_exceptions import UserNotAuthenticated
from integer_controller import user_integer_map


# methods for user authentication and registration
def verify_user(request):
    rule = str(request.url_rule)
    if "login" in rule or "sign_up" in rule:
        pass
    else:
        api_key = request.headers.get("Authorization").split()[1]
        email = jwt.decode(api_key, APP_SECRET, algorithms=['HS256']).get("email")
        if email not in user_integer_map or user_integer_map[email]["API_KEY"] != api_key or not api_key:
            raise UserNotAuthenticated

        g.email = email
