import unittest
from unittest.mock import Mock
from advent import Ship


class TestStringMethods(unittest.TestCase):
    def test_fuel_for_launch_without_modules(self):
        ship = Ship()
        self.assertEqual(ship.fuel_for_launch(), 0)

    def test_fuel_for_launch(self):
        ship = Ship()
        ship.add_module(Mock(fuel_for_launch=2))
        ship.add_module(Mock(fuel_for_launch=3))
        ship.add_module(Mock(fuel_for_launch=4))
        self.assertEqual(ship.fuel_for_launch(), 9)
