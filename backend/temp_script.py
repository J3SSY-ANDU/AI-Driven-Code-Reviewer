def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)  # Missing base case check for negative numbers

def print_numbers(limit):
    for i in range(limit):
        print(i)  # Inefficient loop, no way to stop early

print(factorial(-5))  # This will cause infinite recursion
print_numbers(10)
