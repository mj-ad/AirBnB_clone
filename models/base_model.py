#!/usr/bin/python3
""" class BaseModel """
import models
import uuid
from datetime import datetime


class BaseModel:
    """ defines all common attributes/methods for other classes """
    now = datetime.now()

    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key != '__class__':
                    self.__dict__[key] = value
                if key == 'updated_at':
                    self.__dict__[key] = datetime.now()
                if key == 'created_at':
                    self.__dict__[key] = datetime.today()
        else:
            models.storage.new(self)

    def save(self):
        """ updates the public instance
        attribute updated_at with the current datetime """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ returns a dictionary containing
        all keys/values of __dict__ of the instance """
        key = self.__dict__.copy()
        key['created_at'] = self.created_at.isoformat()
        key['updated_at'] = self.updated_at.isoformat()
        key['__class__'] = self.__class__.__name__
        return key

    def __str__(self):
        """ should print: [<class name>] (<self.id>) <self.__dict__> """
        self.id = str(uuid.uuid4())
        name = self.__class__.__name__
        return '[{}] ({}) {}'.format(name, self.id, self.__dict__)
