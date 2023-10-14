import unittest
from models.city import City


class TestCity(unittest.TestCase):
    def test_city_attributes(self):
        # Create a City instance
        city = City()

        # Check if the default attributes are as expected
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")
    
    def test_city_str_representation(self):
        # Create a City instance and set attributes
        city = City()
        city.state_id = "12345"
        city.name = "New York"
        
        # Check the string representation
        expected_str = "[City] ({}) {}".format(city.id, city.__dict__)
        self.assertEqual(str(city), expected_str)


if __name__ == '__main__':
    unittest.main()

