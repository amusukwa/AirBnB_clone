import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    def test_amenity_attributes(self):
        """ Create an Amenity instance"""
        amenity = Amenity()

        """ Check if the default attributes are as expected"""
        self.assertEqual(amenity.name, "")
    
    def test_amenity_str_representation(self):
        """ Create an Amenity instance and set attributes"""
        amenity = Amenity()
        amenity.name = "Swimming Pool"
        
        """ Check the string representation"""
        self.assertEqual(str(amenity), "[Amenity] ({}) {}".format(amenity.id, amenity.__dict__))

if __name__ == '__main__':
    unittest.main()

