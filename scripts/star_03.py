from advent import Intcode


def main():
    ic = Intcode(codes())
    ic.replace(1, 12)
    ic.replace(2, 2)
    comp = ic.compute()
    print(comp.codes[0])


def codes():
    with open("scripts/star_03_data.txt") as f:
        contents = f.read()
        return [int(c) for c in contents.split(',')]


if __name__== "__main__":
    main()

