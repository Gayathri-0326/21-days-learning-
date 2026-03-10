Linear Search:
Linear search checks each element one by one.

Program:

numbers = [10, 20, 30, 40, 50]

key = int(input("Enter number to search: "))

for i in range(len(numbers)):
    if numbers[i] == key:
        print("Element found at position", i)
        break
else:
    print("Element not found")

Output:

Enter number to search: 30
Element found at position 2

Time Complexity

O(n)




If you want, I can also give the last two topics (Day 20 and Day 21) so your challenge ends with a mini project, which looks very good on GitHub.
