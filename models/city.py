#!/usr/bin/python3

""" module containing the City class """

from models.base_model import BaseModel


class City(BaseModel):
    """ class that acts as a blueprint for a City instance """
    state_id = ""
    name = ""
