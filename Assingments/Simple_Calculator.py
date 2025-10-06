

x = float(input("number 1\n> "))
y = float(input("number 2\n> "))


def add(x,y):
    print(x + y)

def subtract(x,y):
    print(x-y)

def multiply(x,y):
    print(x*y)

def divide(x,y):
    print(x / y)

def exponent(x,y):
    print(x**y)

def modulus(x,y):
    print(x%y)

def floor(x,y):
    print(x//y)

choice = input("Please select an operation: add, subtract, multiply, divide, exponent, modulus, floor.\n> ")
if choice == "add":
    add(x, y)
if choice == "subtract":
    subtract(x,y)
if choice == "multiply":
    multiply(x,y)
if choice == "divide":
    divide(x,y)
if choice == "exponent":
    exponent(x,y)
if choice == "modulus":
    modulus(x,y)
if choice == "floor":
    floor(x,y)


