import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    def test_default_attributes(self):
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_name_assignment(self):
        amenity = Amenity()
        amenity.name = "Pool"
        self.assertEqual(amenity.name, "Pool")
    
    def test_str_representation(self):
        amenity = Amenity()
        amenity.name = "Gym"
        expected_str = "[Amenity] ({}) {}".format(amenity.id, amenity.__dict__)
        self.assertEqual(str(amenity), expected_str)
        
    def test_to_dict_method(self):
        amenity = Amenity()
        amenity.name = "Sauna"
        obj_dict = amenity.to_dict()
        self.assertEqual(obj_dict["name"], "Sauna")
        self.assertEqual(obj_dict["__class__"], "Amenity")


if __name__ == '__main__':
                                                                                                                                                            unittest.main()

