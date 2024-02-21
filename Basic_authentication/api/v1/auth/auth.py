#!/usr/bin/env python3
""" Auth
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """ Auth class to manage API authentication """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ authentication is required """
        if path is None or excluded_paths is None or not excluded_paths:
            return True

        if path[-1] != '/':
            path += '/'
        if excluded_paths[-1] != '/':
            excluded_paths += '/'
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """ authorization header """
        if request is None:
            return None

        return request.headers.get("Authorization", None)

    def current_user(self, request=None) -> TypeVar('User'):
        """ Method to get the current user """
        return None
