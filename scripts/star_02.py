from advent import Ship, ShipModule


def star_02():
    s = Ship()
    [s.add_module(ShipModule(mass=m)) for m in masses()]
    print(s.compound_fuel_for_launch())


def masses():
    with open("star_01_data.txt") as f:
        contents = f.read()
        return [int(line) for line in contents.split("\n")]


if __name__== "__main__":
    star_02()

