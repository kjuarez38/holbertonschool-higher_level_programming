#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):

        if i % 3 != 0 and i % 5 != 0:
            print("{:d}".format(i), end="")
        elif i % 3 == 0:
            print("Fizz", end="")
        elif i % 5 == 0:
            print("Buzz", end="")
        if i != 100:
            print("{} ".format(i), end="")
