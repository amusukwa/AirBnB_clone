#!/usr/bin/python3
import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    __file_path = "file.json"
    __objects = {}
    CLASS_MAPPING = {'BaseModel': BaseModel, 'User': User}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        serialized_objects = {}
        for key, value in self.__objects.items():
            serialized_objects[key] = value.to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(serialized_objects, file)

    def classes(self):
        """Retuens a dict of valid classes plus their references"""
        from models.base_model import BaseModel
        from models.user import User
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.state import State

        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "Amenity": Amenity,
                   "City": City,
                   "Place": Place,
                   "State": State}
        return classes

    def reload(self):
        """Deserializes the JSON file to __objects (if it exists)."""
        try:
            with open(self.__file_path, "r") as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    cls = self.CLASS_MAPPING.get(class_name)
                    if cls:
                        obj = cls(**value)
                        self.__objects[key] = obj
        except FileNotFoundError:
            pass

    def attributes(self):
        """Returns valid atteibutes for each class name"""
        attributes = {
                "BaseModel": {
                    "id": str,
                    "created_at": datetime.datetime,
                    "updated_at": datetime.datetime
                },

                "User": {
                    "email": str,
                    "password": str,
                    "first_name": str,
                    "last_name": str
                },

                "Place": {
                    "city_id": str,
                    "user_id": str,
                    "name": str,
                    "description": str,
                    "number_rooms": int,
                    "number_bathrooms": int,
                    "max_guest": int,
                    "price_by_night": int,
                    "latitude": float,
                    "longitude": float,
                    "amenity_ids": list
                },

                "State": {
                    "name": str
                },

                "City": {
                    "state_id": str,
                    "name": str
                },

                "Amenity": {
                    "name": str
                },

                "Review": {
                    "place_id": str,
                    "user_id": str,
                    "text": str
                }
        }
        return attributes
