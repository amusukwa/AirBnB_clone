import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    def test_inheritance(self):
        review = Review()
        # Check if Review is an instance of BaseModel
        self.assertIsInstance(review, BaseModel)

    def test_attributes(self):
        review = Review()
        # Check if the default attributes are set correctly
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")


if __name__ == '__main__':
    unittest.main()
