#!/usr/bin/python3
""" City Module """
from models.base_model import BaseModel


class City(BaseModel):
    """city class has state ID and name """
    state_id = ""
    name = ""
