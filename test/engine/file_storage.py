#!/usr/bin/python3
"""
file storage module
"""

from base_model import BaseModel
import json
import os


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects.update({f"{obj.__class__.__name__}.{obj.id}": obj})
    
    def save(self):
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()
            json.dump(new_dict, open(self.__file_path, "w"))

    def reload(self):
        if os.path.exists(self.__file_path):
            new_data = json.load(open(self.__file_path, "r"))
            for key, value in new_data.items():
                FileStorage.__objects[key] = eval(value['__class__'])(**value)
