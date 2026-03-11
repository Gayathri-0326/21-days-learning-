Sorting Algorithms in Python:
Sorting means arranging elements in ascending or descending order.

Using Built-in Sort:
numbers = [5, 2, 8, 1, 9]
numbers.sort()
print(numbers)
Output:
[1, 2, 5, 8, 9]

Bubble Sort:
Bubble sort repeatedly swaps adjacent elements if they are in the wrong order.
Example:
numbers = [5, 2, 8, 1, 9]
n = len(numbers)
for i in range(n):
    for j in range(0, n-i-1):
        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
print("Sorted list:", numbers)

Output:
Sorted list: [1, 2, 5, 8, 9]




---

After this, the final topic for Day 21 can be a small Python mini-project (which looks great on GitHub).
