#!/usr/bin/env python3

def happy_new_year():
    i=10
    while i > 0:
        print(f"{i}")
        i-=1
    print("Happy New Year!")

def square_integers(int_list):
    new_list = list()
    for i in int_list:
        new_value = i ** 2
        new_list.append(new_value)
    return new_list

def fizzbuzz():
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)
