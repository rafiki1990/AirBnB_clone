#!/usr/bin/python3
import uuid
from datetime import datetime
import models


class BaseModel:
    """The BaseModel class serves as a base class
    for objects with common attributes and methods.
"""
    def __init__(self, *args, **kwargs):
        """Initialize BaseModel instance"""
    # Check if Kwargs is not empty
        if kwargs != []:
            for key, val in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        # Convert created_at and updated_at in datetime object.
                        value = datetime.strptime(val, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, val)

            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            if 'created_at' not in kwargs:
                self.created_at = datetime.now()
            if 'updated_at' not in kwargs:
                self.updated_at = datetime.now()
            # IF kwargs is empty, it is a new instance
            else:
                self.id = str(uuid.uuid4())
                self.created_at = datetime.now()
                self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Return the string format of the BaseModel object"""
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """update the updated_at attribute with the current date and time"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Convert the BaseModel object's attributes
        to a dictionary for serialization.

        Returns:
        dict: A dictionary containing the object's attributes.
        """
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        # Convert created_at and updated_at to ISO 8601 format
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()

        return new_dict
