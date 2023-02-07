#!/usr/bin/env python3
""" This module contains auth functions
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """ This class provides authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Highlight the given path"""
        return False

    def authorization_header(self, request=None) -> str:
        """ This function takes the header) """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ This function takes the current user """
        return None
