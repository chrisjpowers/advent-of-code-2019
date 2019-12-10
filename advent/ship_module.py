import math


class ShipModule:
    def __init__(self, mass=0):
        self.mass = mass

    def fuel_for_launch(self):
        return math.floor(self.mass / 3) - 2

