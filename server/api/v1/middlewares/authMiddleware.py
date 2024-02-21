import os
import jwt

from flask import request, abort, g


class AuthMiddleware:

    @staticmethod
    def is_valid_token(token):
        from ..app import app
        secret = app.config.get('SECRET_KEY')
        try:
            return jwt.decode(token, secret, algorithms=["HS256"])
        except Exception as e:
            print(str(e))

    def authenticate(self):
        auth_token = request.headers.get('Authorization')

        if not auth_token:
            abort(401)
        decoded = self.is_valid_token(auth_token.split(' ')[1])
        if not decoded:
            abort(401)
        g.user = decoded


def require_authentication(func):
    def wrapper(*args, **kwargs):
        AuthMiddleware().authenticate()
        return func(*args, **kwargs)

    return wrapper
