import logging

from flask import make_response, g, abort, request
from flask_restful import Resource, wraps

from app.common.error_handling import AuthError
from app.modules.models import User

def get_token_auth_header():
    """Obtains the Access Token from the Authorization Header
    """
    auth = request.headers.get("Authorization", None)
    if not auth:
        raise AuthError({"code": "authorization_header_missing",
                        "description":
                            "Authorization header is expected"}, 401)

    parts = auth.split()

    if parts[0].lower() != "bearer":
        raise AuthError({"code": "invalid_header",
                        "description":
                            "Authorization header must start with"
                            " Bearer"}, 401)
    elif len(parts) == 1:
        raise AuthError({"code": "invalid_header",
                        "description": "Token not found"}, 401)
    elif len(parts) > 2:
        raise AuthError({"code": "invalid_header",
                        "description":
                            "Authorization header must be"
                            " Bearer token"}, 401)

    token = parts[1]
    return token

def require_login(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if "id" not in g.cookie:
            logging.warning("No authorization provided!")
            abort(401)

        g.user = User.query.get(g.cookie["id"])

        if not g.user:
            response = make_response("", 401)
            response.set_cookie("user", "")
            return response

        return func(*args, **kwargs)

    return wrapper


class AuthenticatedView(Resource):
    method_decorators = [require_login]