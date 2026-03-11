print("Sort a list of numbers entered by the user")
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
numbers.sort()
print("Sorted list:", numbers)

print("Find the second largest number in a list")
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
numbers.sort()
print("Second largest number:", numbers[-2])

