#!/usr/bin/python3
def fizzbuzz():
    for number in range (1, 101):
        if number == 3 and number == number * 3:
            print(Fizz, end="")
        elif number == 5 and number == number * 5:
            print(Buzz, end="")
        elif number == number * 3 and number == number * 5:
            print(FizzBuzz, end="")
