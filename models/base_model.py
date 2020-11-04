#!/usr/bin/python3
"""BaseModel Module"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """ class basemodel """

    def __init__(self, *args, **kwargs):
        """constructor method"""

        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ string method """

        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def save(self):
        """ update time method """

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ add new items to the dict method """

        new_dict = dict(self.__dict__)
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
