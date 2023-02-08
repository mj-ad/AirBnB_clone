#!/usr/bin/python3
""" class BaseModel """
import uuid
from datetime import datetime


class BaseModel:
    """ defines all common attributes/methods for other classes """
    now = datetime.now()
    
    def save(self):
        self.updated_at = self.now

    def __str__(self):
        self.id = str(uuid.uuid4())
        self.created_at = self.now
        return('[{}] ({}) {}'.format(self.__class__.__name__, self.id, self.__dict__))

    def to_dict(self):
        key = self.__dict__.copy()
        key['created_at'] = self.now.strftime("%Y-%m-%dT%H:%M:%S.%f")
        key['updated_at'] = self.now.strftime("%Y-%m-%dT%H:%M:%S.%f")
        key['__class__'] = self.__class__.__name__
        return key

    def __str__(self):
        self.id = str(uuid.uuid4())
        self.created_at = self.now
        return('[{}] ({}) {}'.format(self.__class__.__name__, self.id, self.__dict__))
