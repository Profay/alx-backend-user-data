#!/usr/bin/env python3
""" This module contains basic auth"""

from api.v1.auth.auth import Auth
import base64
from typing import TypeVar


class BasicAuth(Auth):
    """ This class provides basic authentication"""
    def extract_base64_authorization_header(
          self, authorization_header: str) -> str:
        """ This function returns the authorization
        header in Base64
        """
        if authorization_header is None or type(authorization_header) != str:
            return None
        elif not authorization_header.startswith('Basic '):
            return None
        return authorization_header.split('Basic ')[1]

    def decode_base64_authorization_header(
          self, base64_authorization_header: str) -> str:
        """ This function returns the decoded value of a
        Base64 string base64_authorization_header: """
        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) != str:
            return None

        try:
            return base64.b64decode(base64_authorization_header).\
                          decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
         self, decoded_base64_authorization_header: str) -> (str, str):
        """ This function return user email and password"""
        if decoded_base64_authorization_header is None:
            return (None, None)
        elif type(decoded_base64_authorization_header) != str:
            return (None, None)
        elif ':' not in decoded_base64_authorization_header:
            return (None, None)
        return (
                decoded_base64_authorization_header.split(':')[0],
                decoded_base64_authorization_header.split(':')[1])

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """ return User instance based on their email and password
        """
        if user_email is None or type(user_email) != str:
            return None
        if user_pwd is None or type(user_pwd) != str:
            return None

        try:
            users = User.search({'email': user_email})
            for user in users:
                if user.is_valid_password(user_pwd):
                    return user
        except Exception:
            return None
