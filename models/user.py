#!/usr/bin/python3

from models.base_model import BaseModel


class User(BaseModel):
    """
    User class for storing information about users.
    """
    email = ''
    password = ''
    first_name = ''
    last_name = ''
