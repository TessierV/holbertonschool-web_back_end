#!/usr/bin/env python3
""" Basic Authentication
"""
import base64
import binascii
from typing import TypeVar
from api.v1.auth.auth import Auth
from models.user import User


class BasicAuth(Auth):
    """ Basic Authentication Class """

    def extract_base64_authorization_header(
        self, authorization_header: str
    ) -> str:
        """ Extract Base64 """
        if (
            authorization_header is None
            or not isinstance(authorization_header, str)
        ):
            return None

        if not authorization_header.startswith("Basic "):
            return None

        base64_part = authorization_header.split(" ")[1]
        return base64_part

    def decode_base64_authorization_header(
        self, base64_authorization_header: str
    ) -> str:
        """ Decode Base64 """
        if (
            base64_authorization_header is None
            or not isinstance(base64_authorization_header, str)
        ):
            return None

        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            decoded_str = decoded_bytes.decode('utf-8')
            return decoded_str
        except binascii.Error:
            return None

    def extract_user_credentials(
        self, decoded_base64_authorization_header: str
    ) -> (str, str):
        """ Extract User Credentials """
        if (
            decoded_base64_authorization_header is None
            or not isinstance(decoded_base64_authorization_header, str)
            or ':' not in decoded_base64_authorization_header
        ):
            return None, None

        email, password = decoded_base64_authorization_header.split(':', 1)
        return email, password

    def user_object_from_credentials(
        self, user_email: str, user_pwd: str
    ) -> TypeVar('User'):
        """ Get User Object """
        if (
            user_email is None
            or not isinstance(user_email, str)
            or user_pwd is None
            or not isinstance(user_pwd, str)
        ):
            return None

        try:
            found_users = User.search({'email': user_email})
        except Exception:
            return None

        if not found_users or not found_users[0].is_valid_password(user_pwd):
            return None

        return found_users[0]

    def current_user(self, request=None) -> TypeVar('User'):
        """ overloads """
        if request is None:
            return None

        auth_header = request.headers.get('Authorization')
        if not auth_header or not auth_header.startswith('Basic '):
            return None

        decoded_credentials = self.decode_base64_authorization_header(
            auth_header.split(" ")[1])
        if not decoded_credentials or ':' not in decoded_credentials:
            return None

        user_email, user_pwd = decoded_credentials.split(':', 1)
        if not user_email or not user_pwd:
            return None

        return self.user_object_from_credentials(user_email, user_pwd)
