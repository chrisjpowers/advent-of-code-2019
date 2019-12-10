from advent import Intcode


def main():
    comp = Intcode(codes())\
        .replace(1, 12)\
        .replace(2, 2)\
        .compute()
    print(comp.codes[0])


def codes():
    with open("scripts/star_03_data.txt") as f:
        contents = f.read()
        return [int(c) for c in contents.split(',')]


if __name__== "__main__":
    main()

