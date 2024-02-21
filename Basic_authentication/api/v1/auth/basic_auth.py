#!/usr/bin/env python3
""" Basic Authentication
"""
from api.v1.auth.auth import Auth


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
