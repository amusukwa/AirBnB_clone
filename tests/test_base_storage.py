import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class MockStorage:
    def __init__(self):
        self.saved_objects = []

    def save(self, obj):
        self.saved_objects.append(obj)


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.mock_storage = MockStorage()
        # Replace the real storage with the mock
        BaseModel._BaseModel__storage = self.mock_storage

    def tearDown(self):
        # Restore the original storage to avoid affecting other tests
        BaseModel._BaseModel__storage = FileStorage()


if __name__ == '__main__':
    unittest.main()
