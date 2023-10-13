import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBase(unittest.TestCase):

    def setUp(self):
        # Create an instance of the Base class
        self.base_instance = BaseModel()

    def test_id_creation(self):
        # Check if the id attribute is created and is a string
        self.assertTrue(hasattr(self.base_instance, 'id'))
        self.assertIsInstance(self.base_instance.id, str)

    def test_created_at_type(self):
        # Check if created_at is a datetime object
        self.assertIsInstance(self.base_instance.created_at, datetime)

    def test_updated_at_type(self):
        # Check if updated_at is a datetime object
        self.assertIsInstance(self.base_instance.updated_at, datetime)

    def test_save_method(self):
        # Check if the save method updates the updated_at attribute
        original_updated_at = self.base_instance.updated_at
        self.base_instance.save()
        self.assertNotEqual(original_updated_at, self.base_instance.updated_at)

    def test_to_dict_method(self):
        # Check if the to_dict method returns a dictionary with expected keys
        obj_dict = self.base_instance.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertTrue('id' in obj_dict)
        self.assertTrue('__class__' in obj_dict)
        self.assertTrue('created_at' in obj_dict)
        self.assertTrue('updated_at' in obj_dict)


if __name__ == '__main__':
    unittest.main()
