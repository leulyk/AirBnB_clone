#!usr/bin/python3

""" module to define a user """

from models.base_model import BaseModel


class User(BaseModel):
    """ class that is a blueprint for a User instance """
    first_name = ""
    last_name = ""
    email = ""
    password = ""
