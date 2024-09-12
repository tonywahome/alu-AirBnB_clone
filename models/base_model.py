#!usr/bin/python3
""" 
Define 'BaseModel' Class 
"""

import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
"""
class BaseModel
"""
    def __init__(self, *args, **kwargs): """initialize new basemodel instance arguments
    *args
    **kwargs"""

        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) !=0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__[k] = v
            else:
                models.storage.new(self)
    def save(self):
                self.updated_at = datetime.today()
                models.storage.save()
    
    def to_dict(self):
"""Return dictionary representation of model instance"""
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.class__.__name__
        return rdict

    def __str__(self):
        """return string representation of the model instance"""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)

