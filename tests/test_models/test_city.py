#!/usr/bin/python3
from models.city import City
import unittest


class TestCity(unittest.TestCase):
    def test_instance_creation(self):
        """Test if an instance of City is created successfully"""
        city = City()
        self.assertIsInstance(city, City)

    def test_attributes(self):
        """Test if City has the expected attributes"""
        city = City()
        self.assertTrue(hasattr(city, 'state_id'))
        self.assertTrue(hasattr(city, 'name'))

    def test_default_values(self):
        """Test if the attributes have default values"""
        city = City()
        self.assertEqual(city.state_id, '')
        self.assertEqual(city.name, '')

if __name__ == "__main__":
    unittest.main()
