import unittest
import os
import json
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        # Create an instance of FileStorage and store it as a class attribute
        self.file_storage = FileStorage()
        self.test_file_path = 'test_file.json'

    def tearDown(self):
        # Remove the test file created during the test
        if os.path.exists(self.test_file_path):
            os.remove(self.test_file_path)
    def test_save_and_reload(self):
        # Create some test data
        user = User()
        user.email = 'test@example.com'
        user.password = 'password123'

        # Add the test data to the FileStorage instance
        self.file_storage.new(user)

        # Set the test file path
        self.file_storage._FileStorage__file_path = self.test_file_path

        # Save the data to the test file
        self.file_storage.save()

        # Reload the data from the test file
        self.file_storage.reload()

        # Get all the reloaded objects
        reloaded_objects = self.file_storage.all()

        


if __name__ == '__main__':
    unittest.main()
