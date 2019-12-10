import unittest
from advent import ShipModule


class TestStringMethods(unittest.TestCase):
    def test_it_works(self):
        self.assertTrue(ShipModule)

    # For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2
    def test_fuel(self):
        sm = ShipModule(mass=12)
        self.assertEqual(sm.fuel_for_launch(), 2)
