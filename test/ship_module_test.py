import unittest
from advent import ShipModule


class TestStringMethods(unittest.TestCase):
    def test_it_works(self):
        self.assertTrue(ShipModule)

    # For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2
    def test_fuel(self):
        sm = ShipModule(mass=12)
        self.assertEqual(sm.fuel_for_launch(), 2)

    # The fuel required by a module of mass 100756 and its fuel is:
    # 33583 + 11192 + 3728 + 1240 + 411 + 135 + 43 + 12 + 2 = 50346.
    def test_compound_fuel_for_launch(self):
        sm = ShipModule(mass=1969)
        self.assertEqual(sm.compound_fuel_for_launch(), 966)

        sm = ShipModule(mass=100756)
        self.assertEqual(sm.compound_fuel_for_launch(), 50346)


