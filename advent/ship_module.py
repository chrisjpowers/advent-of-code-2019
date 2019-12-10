import math


class ShipModule:
    def __init__(self, mass=0):
        self.mass = mass

    def fuel_for_launch(self):
        return self._calculate_fuel_mass(self.mass)

    def compound_fuel_for_launch(self):
        total_mass = 0
        next_mass = self.fuel_for_launch()
        while next_mass > 0:
            total_mass += next_mass
            next_mass = self._calculate_fuel_mass(next_mass)
        return total_mass

    @staticmethod
    def _calculate_fuel_mass(mass):
        return math.floor(mass / 3) - 2
