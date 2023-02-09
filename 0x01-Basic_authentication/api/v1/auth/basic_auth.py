#!/usr/bin/env python3
""" This module contains basic auth"""

from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ This class provides basic authentication"""
    def extract_base64_authorization_header(
          self, authorization_header: str) -> str:
        """ This function returns the authorization
        header in Base64
        """
        if authorization_header is None or type(authorization_header) != str:
            return None
        if authorization_header.startswith('Basic '):
            return None
        return authorization_header.split('Basic ')[1]
