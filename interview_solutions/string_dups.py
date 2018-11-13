#!/usr/bin/python3

def main():
    yourString = "apple"

    sortedString = ''.join(sorted(yourString))
    i = 0
    for i in range(0, len(sortedString) - 1):
        if sortedString[i] == sortedString[i +1]:
            print(sortedString[i] + sortedString[i +1] + " True")
            i += 1
        else:
            print(sortedString[i] + sortedString[i +1] + " False")
            i += 1


if __name__ == "__main__":
    main()
