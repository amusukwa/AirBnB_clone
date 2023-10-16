import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.base_instance = BaseModel()

    def test_id_creation(self):
        self.assertTrue(hasattr(self.base_instance, 'id'))
        self.assertIsInstance(self.base_instance.id, str)

    def test_created_at_type(self):
        self.assertIsInstance(self.base_instance.created_at, datetime)

    def test_updated_at_type(self):
        self.assertIsInstance(self.base_instance.updated_at, datetime)

    def test_save_method(self):
        model = BaseModel()
        original_updated_at = model.updated_at
        model.save()
        newly_updated_at = model.updated_at
        self.assertNotEqual(newly_updated_at, original_updated_at)

    def test_to_dict_method(self):
        obj_dict = self.base_instance.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertTrue('id' in obj_dict)
        self.assertTrue('__class__' in obj_dict)
        self.assertTrue('created_at' in obj_dict)
        self.assertTrue('updated_at' in obj_dict)

    def test_str_representation(self):
        model = BaseModel()
        expected_str = f"[{model.__class__.__name__}] ({model.id}) {model.__dict__}"
        self.assertEqual(str(model), expected_str)


if __name__ == '__main__':
    unittest.main()
