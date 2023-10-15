#!usr/bin/python3
import json
from models.base_model import BaseModel


class FileStorage:
    __file_path = "file.json"
    __objects = {}
    ModelStruct = {
        "BaseModel": BaseModel
    }
    def all(self):
        return self.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        data = {} # This line initializes an empty dictionary called data. 
        # This dictionary will be used to store the data that you want to save to the JSON file
        for key, obj in self.__objects.items(): #Iterate through key-value pairs of the dictionary
            data[key] = obj.to_dict() # Creating a dictionary with object data (as per instructions)
        
        with open(self.__file_path ,'w') as file:
            json.dump(data, file)
        

    def reload(self):
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
    
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    cls = self.ModelStruct[class_name]
                    self.__objects[key] = cls(**value)
        except FileNotFoundError:
            pass

