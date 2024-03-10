#!/usr/bin/python3
import uuid
from datetime import datetime


class BaseModel():
    """
    BaseModel class for all models
    """
    def __init__(self, *args, **kwargs):
            """
            constructor or new instance made
            """
            if kwargs:
                if '__class__' in kwargs:
                    del kwargs['__class__']
                for key, value in kwargs.items():
                    if key == 'created_at' or key == 'updated_at':
                        setattr(self, key, datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                    else:
                        setattr(self, key, value)
            else:
                self.id = str(uuid.uuid4())
                self.created_at = datetime.utcnow()
                self.updated_at = datetime.utcnow()

    def save(self):
        """
        save the model
        """
        self.updated_at = datetime.utcnow()
        self.updated_at = self.updated_at

    def to_dict(self):
        """
        convert the model to a dictionary
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        #obj_dict['id'] = str(self.id)
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

    def __str__(self):
        """
        string representation of the model
        """
        class_name = self.__class__.__name__
        return "({}) ({})".format(class_name, self.id, self.__dict__)
