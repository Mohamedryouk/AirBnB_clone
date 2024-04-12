#!/usr/bin/python3
import uuid
from datetime import datetime
import models


class BaseModel():
    """
    Initialize BaseModel class.
    Arguments:
    *args:
        *args (any) : unused argument.
        **kwargs (dict) : unused keyword arguments.
    """
    def __init__(self, *args, **kwargs):
        """
        initialize the model
        """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value, time_format))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
        models.storage.new(self)
    def save(self):
        """
        save the model
        """
        self.updated_at = datetime.utcnow()
        models.storage.save()
    def to_dict(self):
        """
        convert the model to a dictionary
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

    def __str__(self):
        """
        string representation of the model
        """
        className = self.__class__.__name__
        return "[{}] ({}) {}".format(className, self.id, self.__dict__)
