#!/usr/bin/env python3
from api.v1.auth.auth import Auth
from base64 import b64decode
from flask import request

class BasicAuth(Auth):
    """ Basic authentication class """

    def authorization_header(self, request=None) -> str:
        """ Parse Authorization header for basic authentication """
        if request is None or 'Authorization' not in request.headers:
            return None

        auth_header = request.headers.get('Authorization')
        if not auth_header.startswith('Basic '):
            return None

        encoded_credentials = auth_header.split(' ')[1]
        decoded_credentials = b64decode(encoded_credentials).decode('utf-8')
        return decoded_credentials

    def current_user(self, request=None) -> TypeVar('User'):
        """ Extract user information from basic authentication """
        credentials = self.authorization_header(request)
        if credentials is None:
            return None

        return user
