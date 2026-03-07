Factorial Using Recursion:

def factorial(n):
    if n == 1:         
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter number: "))
print("Factorial:", factorial(num))

Output:

Enter number: 5
Factorial: 120

Sum of Numbers:

def sum_numbers(n):
    if n == 1:
        return 1
    else:
        return n + sum_numbers(n-1)

print(sum_numbers(5))

Output:

15

Fibonacci Series:

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))

Output:

8




