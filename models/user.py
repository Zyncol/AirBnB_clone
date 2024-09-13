#!/usr/bin/python3
"""
A class user
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    methods definintion
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
