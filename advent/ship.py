class Ship:
    def __init__(self):
        self.ship_modules = []

    def fuel_for_launch(self):
        return sum([x.fuel_for_launch() for x in self.ship_modules])

    def add_module(self, ship_module):
        self.ship_modules.append(ship_module)

    def compound_fuel_for_launch(self):
        return sum([x.compound_fuel_for_launch() for x in self.ship_modules])
