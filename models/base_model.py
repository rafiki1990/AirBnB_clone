#!/usr/bin/python3
import uuid
from datetime import datetime
import models

class BaseModel:
    def __init__(self, *args, **kwargs):
    # Check if Kwargs is not empty
     if kwargs != []:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        #Convert created_at and updated_at in datetime object.
                        value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, value)
                    
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            if 'created_at' not in kwargs:
                self.created_at = datetime.now()
            if 'updated_at' not in kwargs:
                self.updated_at = datetime.now()
            else: # IF kwargs is empty, it is a new instance
                self.id = str(uuid.uuid4())
                self.created_at = datetime.now()
                self.updated_at = datetime.now()
            models.storage.new(self)
                
    def __str__(self):
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")
    
    def save(self):
        self.updated_at = datetime.now()
        
    
    def to_dict(self):
        
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        # Convert created_At and upated_at
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()

        return new_dict

