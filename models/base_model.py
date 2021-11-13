#!/usr/bin/env python3

"""
    module containing the BaseModel class for the HBnB console
"""

import uuid
from datetime import datetime
from dateutil import parser
from models import storage


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
        if 'id' not in kwargs.keys():
            self.id = str(uuid.uuid4())
        if 'created_at' not in kwargs.keys():
            self.created_at = datetime.now()
        if 'updated_at' not in kwargs.keys():
            self.updated_at = self.created_at
        if not kwargs or len(kwargs) == 0:
            storage.new(self)

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
        storage.save()

    def to_dict(self):
        """ dictionary representation of a BaseModel object """
        dict_copy = self.__dict__.copy()
        dict_copy['__class__'] = type(self).__name__
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.updated_at.isoformat()
        return dict_copy
