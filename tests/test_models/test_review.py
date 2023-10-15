#!/usr/bin/python3
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    def test_instance_creation(self):
        """Test if an instance of Review is created successfully"""
        review = Review()
        self.assertIsInstance(review, Review)

    def test_attributes(self):
        """Test if Review has the expected attributes"""
        review = Review()
        self.assertTrue(hasattr(review, 'place_id'))
        self.assertTrue(hasattr(review, 'user_id'))
        self.assertTrue(hasattr(review, 'text'))

    def test_default_values(self):
        """Test if the attributes have default values"""
        review = Review()
        self.assertEqual(review.place_id, '')
        self.assertEqual(review.user_id, '')
        self.assertEqual(review.text, '')

if __name__ == "__main__":
    unittest.main()
