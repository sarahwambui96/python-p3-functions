#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")
    pass

def greet(name):
    print(f"Hello, {name}!")
    pass
greet("Sarah")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")
    pass
greet_with_default()
greet_with_default("Sarah")

def add(num1, num2):
    return num1 + num2
    pass
add(10, 15)

def halve(number):
    return number / 2
    pass
halve(30)