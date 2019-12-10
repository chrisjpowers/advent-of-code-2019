from advent import Intcode


def main():
    memory = codes()
    for noun in range(99):
        for verb in range(99):
            ic = Intcode(memory)\
                .replace(1, noun)\
                .replace(2, verb)\
                .compute()
            total = ic.memory[0]
            if total == 19690720:
                print(100 * noun + verb)
                return
            elif total > 19690720:
                break

def codes():
    with open("scripts/star_03_data.txt") as f:
        contents = f.read()
        return [int(c) for c in contents.split(',')]


if __name__== "__main__":
    main()

