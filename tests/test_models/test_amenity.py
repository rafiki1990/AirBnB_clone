import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    def test_instance_creation(self):
        """Test if an instance of Amenity is created successfully"""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)

    def test_name_attribute(self):
        """Test if Amenity has a 'name' attribute"""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, 'name'))

    def test_name_default_value(self):
        """Test if the 'name' attribute has a default empty string value"""
        amenity = Amenity()
        self.assertEqual(amenity.name, '')

if __name__ == "__main__":
    unittest.main()
