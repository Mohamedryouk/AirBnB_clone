#!/usr/bin/python3
from models.base_model import BaseModel
import os
import json

class FileStorage():
    """
    FileStorage class provides storage for files and data to be stored in a database.
    """
    __file_path = "file.json"
    __objects = {}

    def new(self, obj):
        """
        create a new object and save class name and content in the obj variable.
        """
        class_name_obj = obj.__class__.__name__
        key = "{} {}".format(class_name_obj, obj.id)
        FileStorage.__objects[key] = obj

    def all(self):
        """
        return FileStorage.__objects.
        """
        return FileStorage.__objects

    def save(self):
        """
        save the file to the database as a JSON string.
        """
        allObjects = FileStorage.__objects
        Obj_dict = {}
        for obj in allObjects.keys():
            Obj_dict[obj] = allObjects[obj].to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(Obj_dict, file)

def reload(self):
    """Reload data from file and update objects dictionary."""
    try:
        with open(FileStorage.__file_path, "r") as f:
            loaded_data = json.load(f)
        for key, val in loaded_data.items():
            if key in self.all():
                self.all()[key].update(val)
            else:
                self.all()[key] = BaseModel(**val)
    except FileNotFoundError:
        pass
