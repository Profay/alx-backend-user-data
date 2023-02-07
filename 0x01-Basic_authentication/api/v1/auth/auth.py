#!/usr/bin/env python3
""" This module contains auth functions
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """ This class provides authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Highlight the given path"""
        if path is None or excluded_paths is None:
            return True
        elif path in excluded_paths or path + '/' in excluded_paths:
            return False
        else:
            return True

    def authorization_header(self, request=None) -> str:
        """ This function takes the header) """
        if request is not None:
            return request.headers.get('Authorozation', None)
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ This function takes the current user """
        return None
