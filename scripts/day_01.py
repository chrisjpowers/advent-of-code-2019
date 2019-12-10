from advent import Ship, ShipModule

def day_01():
    s = Ship()
    [s.add_module(ShipModule(mass=m)) for m in masses()]
    print(s.fuel_for_launch())

def masses():
    with open("day_01_data.txt") as f:
        contents = f.read()
        return [int(line) for line in contents.split("\n")]

if __name__== "__main__":
    day_01()
