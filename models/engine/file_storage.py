#!/usr/bin/python3

"""
    module to implement the file storage engine for the hbnb console
"""

import json
from os import path


class FileStorage:
    """
        serializes object instances to JSON and deserializes JSON files
        to object instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        key = type(obj).__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, "w") as file:
            file.write(json.dumps(new_dict))

    def reload(self):
        """
            Deserializes the JSON file to __objects
            Only if the JSON file (__file_path) exists; otherwise, do nothing.
            If the file doesn’t exist, no exception should be raised.
        """
        file_name = FileStorage.__file_path
        if path.exists(file_name):
            with open(file_name, "r") as file:
                from models.base_model import BaseModel
                from models.user import User
                from models.state import State
                from models.city import City
                from models.amenity import Amenity
                from models.place import Place
                from models.review import Review
                objs = json.loads(file.read())
                for key, value in objs.items():
                    cls = value["__class__"]
                    obj = eval(cls + "(**value)")
                    FileStorage.__objects[key] = obj
