#!/usr/bin/python3

from model.base_model import BaseModel

class User(BaseModel):
    
    email = ''
    password = ''
    first_name = ''
    last_name = ''
