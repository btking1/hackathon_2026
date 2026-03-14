import unittest
from utils import validate_city, format_temperature


class TestUtils(unittest.TestCase):
    def test_validate_city_valid(self):
        self.assertTrue(validate_city("New York"))
    
    def test_validate_city_empty(self):
        self.assertFalse(validate_city(""))
    
    def test_validate_city_numbers(self):
        self.assertFalse(validate_city("City123"))
    
    def test_format_temperature(self):
        self.assertEqual(format_temperature(72.456), "72.5°F")
