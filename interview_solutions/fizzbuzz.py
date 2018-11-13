#!/usr/bin/python3

def main():
    for i in range(100):
        if i % 3 == 0 and i % 5 == 0:
            print(str(i) + " fizzbuzz")
        elif i % 3 == 0:
            print(str(i) + " fizz")
        elif i % 5 == 0:
            print(str(i) + " buzz")
        else:
            print(str(i) + " zap")


if __name__ == "__main__":
    main()
