#!/usr/bin/python3
from models.base_model import BaseModel
import os
import json
import logging

logger = logging.getLogger('FileStorage')
logger.setLevel(logging.DEBUG)

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
        """ reload the database from the database and deserialize it into an object."""
        """logger.debug('Objects before reload: %s', len(self.__objects))"""
        if os.path.isfile(self.__file_path):
            try:
                with open(self.__file_path, "r") as file:
                    loaded_data = json.load(file)
                for obj_dict in loaded_data.values():
                    class_name = obj_dict["__class__"]
                    del obj_dict["__class__"]
                    obj = eval(class_name)(**obj_dict)
                    self.__objects[obj.id] = obj
            except Exception as e:
                pass
        """logger.debug('Objects after reload: %s', len(self.__objects))"""
