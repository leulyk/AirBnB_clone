#!/usr/bin/env python3

"""
    module containing the BaseModel class for the HBnB console
"""

import json
import uuid
from datetime import datetime
from dateutil import parser


class BaseModel:
    """
        base class that defines common attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """ constructor of the BaseModel class """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ['created_at', 'updated_at']:
                        new_value = parser.parse(value)
                    else:
                        new_value = value
                    setattr(self, key, new_value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """ string representation of the BaseModel class """
        return "[{}] ({}) {}".format(type(self).__name__, self.id,
                                     self.__dict__)

    def save(self):
        """
            updates the public instance attribute updated_at
            with current time
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ dictionary representation of a BaseModel object """
        self.__dict__['__class__'] = type(self).__name__
        self.__dict__['created_at'] = self.__dict__['created_at'].isoformat()
        self.__dict__['updated_at'] = self.__dict__['updated_at'].isoformat()
        return self.__dict__
