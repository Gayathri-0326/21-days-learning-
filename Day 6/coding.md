1.ADD TWO NUMBERS:
def add(a, b):
    return a + b

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = add(num1, num2)
print("Sum =", result)
2.FIND SQUARE OF A NUMBER:
def square(num):
    return num * num

result = square(4)
print("Square =", result)
3.CHECK EVEN OR ODD:
def check_even_odd(num):
    if num % 2 == 0:
        print("Even number")
    else:
        print("Odd number")

check_even_odd(8)
4.FUNCTION TO GREET USER:
def greet(name):
    print("Hello", name)

greet("Gayathri")
