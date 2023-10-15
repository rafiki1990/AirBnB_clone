#!/usr/bin/python3
"""Module for storing instances in a dictionary and handling file storage."""
import json
from models.base_model import BaseModel


class FileStorage:
    """A class to manage storage of instances in a dictionary and file storage."""
    
    __file_path = "file.json"
    __objects = {}
    ModelStruct = {
        "BaseModel": BaseModel
    }
    
    def all(self):
        """
        Return the dictionary of all instances.

        Returns:
            dict: A dictionary containing all instances.
        """
        return self.__objects

    def new(self, obj):
        """
        Add a new instance to the storage dictionary.

        Args:
            obj: An instance to be added to the storage dictionary.
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        Save the current state of instances to a JSON file.
        """
        data = {}  # Initialize an empty dictionary to store data.
        for key, obj in self.__objects.items():
            data[key] = obj.to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(data, file)

    def reload(self):
        """
        Load previously saved instances from a JSON file.
        """
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)

                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    cls = self.ModelStruct[class_name]
                    self.__objects[key] = cls(**value)
        except FileNotFoundError:
            pass
