from advent import Password

def main():
    counter = 0
    for x in range(256310, 732736 + 1):
        if Password(x).valid:
            counter += 1
    print(counter)

if __name__== "__main__":
    main()
