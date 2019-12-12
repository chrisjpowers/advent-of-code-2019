from advent import Password2

def main():
    counter = 0
    for x in range(256310, 732736 + 1):
        if Password2(x).valid:
            counter += 1
    print(counter)

if __name__== "__main__":
    main()
