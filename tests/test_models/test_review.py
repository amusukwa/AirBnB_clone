import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    def setUp(self):
        self.review = Review()
        self.file_path = "models/review.py"

    def test_attributes(self):
        # Check if the default attributes are set correctly
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")


if __name__ == '__main__':
    unittest.main()
