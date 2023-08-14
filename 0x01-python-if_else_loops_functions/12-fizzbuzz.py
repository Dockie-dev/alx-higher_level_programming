#!/usr/bin/python3
# Author - Dorcas John Ndukwe
"""Print the numbers from 1 to 100 separated by a space.
  For multiples of Three, print Fizz instead of the number
  For multiples of Five, print Buzz instead of the number.
  For multiples of Three and five, print FizzBuzz instead of the number.
  """


def fizzbuzz():
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz ", end="")
        elif number % 3 == 0:
            print("Fizz ", end="")
        elif number % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(number), end="")
