a=int(input("Enter a number: "))
b=int(input("Enter another number: "))

def add_number(a, b):
    return a + b

def subtract_number(a, b):
    return a - b


def multiply_number(a, b):
    return a * b

def multiply_number(a, b):
    return a * b

def division_number(a, b):
    if b == 0:
        return "Cannot divide by zero"
    else:
        return a / b


print(add_number(a, b))
print(subtract_number(a, b))
print(multiply_number(a, b))
print(division_number(a, b))