import string
from functools import wraps
from flask_smorest import abort
from flask_jwt_extended import verify_jwt_in_request, get_jwt


def admin_only(allowed_role: string):
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            if claims["role"] == allowed_role:
                abort(401, message="Only admins can access this functionality")
            else:
                return func(*args, **kwargs)

        return inner

    return wrapper
