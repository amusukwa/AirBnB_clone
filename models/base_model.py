#!/usr/bin/pythion3
"""
The BaseModel module
This class will be the "base" of all other classes in this project
"""


import uuid
from datetime import datetime


class BaseModel():
    """This class represents the BaseModel"""

    def __init__(self, *args, **kwargs):
        """Initialized instance attributes

        Args:
            - *args: List of arguments
            - **kwargs: dictionary of key/values arguments
        """
        from models import storage
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ('created_at', 'updated_at'):
                        setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        Returns a string representation of the Base Model
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        updates public instance  updated_at with  current datetime
        """
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        returns all dictionary keys/values of __dict__
        """
        class_name = self.__class__.__name__
        return {
            "__class__": self.__class__.__name__,
            "id": self.id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
