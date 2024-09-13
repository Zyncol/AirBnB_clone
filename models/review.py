#!/usr/bin/python3
""" Review module"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ Reviewing the details """
    place_id = ""
    user_id = ""
    text = ""
