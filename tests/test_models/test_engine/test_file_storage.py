import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os
import json


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()
        self.base_instance = BaseModel()
        self.storage.new(self.base_instance)

    def tearDown(self):
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_all_method(self):
        objects = self.storage.all()
        self.assertIsInstance(objects, dict)
        self.assertTrue(len(objects) > 0)

    def test_new_method(self):
        new_obj = BaseModel()
        self.storage.new(new_obj)
        key = "{}.{}".format(new_obj.__class__.__name__, new_obj.id)
        self.assertTrue(key in self.storage.all())

    def test_save_method(self):
        self.base_instance.save()
        with open(FileStorage._FileStorage__file_path, "r") as file:
            data = json.load(file)
            key = "{}.{}".format(
                    self.base_instance.__class__.__name__,
                    self.base_instance.id
                )
            self.assertTrue(key in data)

        def test_reload_method(self):
            self.base_instance.save()
            new_storage = FileStorage()
            new_storage.reload()
            objects = new_storage.all()
            key = "{}.{}".format(
                    self.base_instance.__class__.__name__,
                    self.base_instance.id
                )
            self.assertTrue(key in objects)


if __name__ == '__main__':
    unittest.main()
