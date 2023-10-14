import unittest
from models.base_model import BaseModel
from models.place import Place

class TestPlace(unittest.TestCase):
    def test_inheritance(self):
        place = Place()
         # Check if Place is an instance of BaseModel
        self.assertIsInstance(place, BaseModel)

    def test_default_attributes(self):
        place = Place()
        #Check if the default attributes are set correctly
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

if __name__ == '__main__':
    unittest.main()
