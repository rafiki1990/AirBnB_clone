import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    def test_instance_creation(self):
        # Test creating a new instance of BaseModel
        obj = BaseModel()
        self.assertIsInstance(obj, BaseModel)

    def test_attributes_existence(self):
        # Test if essential attributes exist in a new instance
        obj = BaseModel()
        self.assertTrue(hasattr(obj, 'id'))
        self.assertTrue(hasattr(obj, 'created_at'))
        self.assertTrue(hasattr(obj, 'updated_at'))

    def test_id_generation(self):
        # Test if a new ID is generated when creating a new instance
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertNotEqual(obj1.id, obj2.id)

    def test_datetime_format(self):
        # Test if 'created_at' and 'updated_at' are datetime objects
        obj = BaseModel()
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test_str_representation(self):
        # Test the string representation of the object
        obj = BaseModel()
        expected_str = f"[BaseModel] ({obj.id}) {obj.__dict__}"
        self.assertEqual(str(obj), expected_str)

    def test_save_method(self):
        # Test if 'save' method updates the 'updated_at' attribute
        obj = BaseModel()
        original_updated_at = obj.updated_at
        obj.save()
        self.assertNotEqual(original_updated_at, obj.updated_at)

    def test_to_dict_method(self):
        # Test the 'to_dict' method for correct dictionary format
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertTrue('id' in obj_dict)
        self.assertTrue('created_at' in obj_dict)
        self.assertTrue('updated_at' in obj_dict)
        self.assertTrue('__class__' in obj_dict)

if __name__ == '__main__':
    unittest.main()
