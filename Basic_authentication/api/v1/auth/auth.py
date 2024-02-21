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

        path_slash_tolerant = path.endswith('/') and path[:-1]

        return path_slash_tolerant not in excluded_paths

    def authorization_header(self, request=None) -> str:
        """ authorization header """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Method to get the current user """
        return None
