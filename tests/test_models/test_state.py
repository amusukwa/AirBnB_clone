import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    def test_inheritance(self):
        state = State()
        """ Check if State is an instance of BaseModel"""
        self.assertIsInstance(state, BaseModel)

    def test_default_attributes(self):
        state = State()
        """Check if the default attributes are set correctly"""
        self.assertEqual(state.name, "")


if __name__ == '__main__':
    unittest.main()
