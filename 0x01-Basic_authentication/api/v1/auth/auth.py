#!/usr/bin/env python3
""" This module contains auth functions
"""
from flask import request
from typing import List, Pattern, TypeVar


class Auth:
    """ This class provides authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Highlight the given path"""
        if path is None or excluded_paths is None:
            return True
        elif path in excluded_paths or path + '/' in excluded_paths:
            return False
        for e_path in excluded_paths:
            if e_path.endswith('*'):
                if path.startswith(i[:1]):
                    return False
        else:
            return True

    def authorization_header(self, request=None) -> str:
        """ This function takes the header) """
        if request is not None:
            return request.headers.get('Authorization', None)
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ This function takes the current user """
        None
