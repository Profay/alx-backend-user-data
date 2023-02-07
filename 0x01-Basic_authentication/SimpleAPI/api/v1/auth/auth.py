#!/usr/bin/env python3
""" This module contains auth functions"""


from flask import requests


class Auth:
    """ This class provides authentication"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Highlight the given path"""
        return path in excluded_paths
    

    def authorization_header(self, request=None) -> str:
        
