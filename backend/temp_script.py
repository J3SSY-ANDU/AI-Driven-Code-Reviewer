import os

def greet(name):
    print("Hello " + name) # Missing proper string formatting

def add_numbers(a, b):
    return a + b  # No type hints

def divide(a, b):
    if b == 0:
        print("Error: Cannot divide by zero")  # Should raise an exception
        return None
    return a / b

class Sample:
    def __init__(self, value):
        self.value = value # Missing type hint

    def get_value(self):
        return self.value

print(greet("Alice"))
print(add_numbers(5, 3))
print(divide(10, 0))
