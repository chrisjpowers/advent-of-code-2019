import unittest
from unittest.mock import Mock
from advent import Ship


class TestShip(unittest.TestCase):
    def test_fuel_for_launch_without_modules(self):
        ship = Ship()
        self.assertEqual(ship.fuel_for_launch(), 0)

    def test_fuel_for_launch(self):
        ship = Ship()
        sm1 = Mock()
        sm1.fuel_for_launch.return_value = 1
        sm2 = Mock()
        sm2.fuel_for_launch.return_value = 2
        ship.add_module(sm1)
        ship.add_module(sm2)
        self.assertEqual(ship.fuel_for_launch(), 3)

    def test_compound_fuel_for_launch(self):
        ship = Ship()
        sm1 = Mock()
        sm1.compound_fuel_for_launch.return_value = 1
        sm2 = Mock()
        sm2.compound_fuel_for_launch.return_value = 2
        ship.add_module(sm1)
        ship.add_module(sm2)
        self.assertEqual(ship.compound_fuel_for_launch(), 3)
