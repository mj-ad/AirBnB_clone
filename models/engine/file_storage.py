#!/usr/bin/python33
""" class FileStorage """
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """ serializes instances to a JSON file and deserializes JSON file to instances """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        clname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(clname, obj.id)] = obj

    def save(self):
        obd = FileStorage.__objects
        objd = {obj: obd[obj].to_dict() for obj in obd.keys()}
        with open('file.json', 'w') as f:
            json.dump(objd, f)

    def reload(self):
        try:
            with open(FileStorage.__file_path) as f:
                objd = json.load(f)
                for obj in objd.values():
                    clname = obj['__class__']
                    del obj['__class__']
                    self.new(eval(clname)(**obj))
        except FileNotFoundError:
            return
