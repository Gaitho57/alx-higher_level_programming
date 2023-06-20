#!/usr/bin/python3

def fizzbuzz():
    # Print numbers from 1 to 100 with variations
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz ", end="")
        elif num % 5 == 0:
            print("Buzz ", end="")
        elif num % 3 == 0:
            print("Fizz ", end="")
        else:
            print(f"{num} ", end="")

# Calls the fizzbuzz function towork
fizzbuzz()

