#!/usr/bin/python3
"""
a class FileStorage that serializes instances to a JSON file
and deserializes JSON file to instance
"""

import os
import json
from models.base_model import BaseModel


class FileStorage:
    """
    for serialisation  to JSON file
    and deserialisation to instance
    """
    __file_path = "file.json"
    __objects = {}

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        obj_cl_nm = obj.__class__.__name__
        key = "{}.{}".format(obj_cl_nm, obj.id)
        FileStorage.__objects[key] = obj

    def all(self):
        """
        returns the dictionary __objects
        """
        return FileStorage.__objects

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        ons_objcts = FileStorage.__objects
        obj_pre = {}
        for obj in ons_objcts.keys():
            obj_pre[obj] = ons_objcts[obj].to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(obj_pre, file)

    def reload(self):
        """
        deserializes the JSON file to __object
        """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                try:
                    obj_pre = json.load(file)
                    for key, value in obj_pre.items():
                        class_name, obj_id = key.split('.')
                        kls = eval(class_name)
                        instance = kls(**value)
                        FileStorage.__objects[key] = instance
                except Exception:
                        pass
