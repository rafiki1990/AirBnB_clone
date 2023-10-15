#!/usr/bin/python3

import uuid
from datetime import datetime
import models


class BaseModel:
    """
The BaseModel class serves as a base class for
objects with common attributes and methods.

Attributes:
    - id (str): A unique identifier for the object.
    - created_at (datetime): A datetime r
        epresenting the object's creation time.
    - updated_at (datetime): A datetime
        representing the object's last update time.

Methods:
    - __init__(self, *args, **kwargs):
        Initializes a BaseModel instance, either from
        provided keyword arguments or as a new instance.

    - __str__(self):
        Returns a string representation of the object.

    - save(self):
        Updates the `updated_at` attribute to the current date and time.

    - to_dict(self):
        Converts the object's attributes to a dictionary
        suitable for serialization.
"""


def __init__(self, *args, **kwargs):
    """
    Initialize a BaseModel instance.

    Args:
        *args: Variable-length argument list (not used).
        **kwargs (dict): Keyword arguments to initialize attributes.

    Notes:
        - If `kwargs` is provided, it initializes
            the object from the given data.
        - If `kwargs` is empty, it creates a new instance
            with unique identifiers and timestamps.
    """
    # Check if kwargs is not empty
    if kwargs:
        for key, val in kwargs.items():
            if key != '__class__':
                if key in ['created_at', 'updated_at']:
                    # Convrt created_at and updated_at to datetime objects
                    value = datetime.strptime(val, '%Y-%m-%dT%H:%M:%S.%f')
                setattr(self, key, value)

        if 'id' not in kwargs:
            self.id = str(uuid.uuid4())
        if 'created_at' not in kwargs:
            self.created_at = datetime.now()
        if 'updated_at' not in kwargs:
            self.updated_at = datetime.now()
        else:  # If kwargs is empty, it is a new instance
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        models.storage.new(self)


def __str__(self):
    """
    Return a string representation of the BaseModel object.

    Returns:
        str: A string in the format "[ClassName] (id) {attributes}".
    """
    return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"


def save(self):
    """
    Update the `updated_at` attribute to the current date and time.
    """
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
