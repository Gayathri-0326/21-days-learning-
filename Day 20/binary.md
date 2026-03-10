Binary Search:
Binary search works only on sorted lists.
It divides the list into halves.
Program:
numbers = [10, 20, 30, 40, 50]
key = int(input("Enter number to search: "))
low = 0
high = len(numbers) - 1
while low <= high:
    mid = (low + high) // 2
    if numbers[mid] == key:
        print("Element found at index", mid)
        break
    elif numbers[mid] < key:
        low = mid + 1
    else:
        high = mid - 1
else:
    print("Element not found")

Output:
Enter number to search: 40
Element found at index 3

Time Complexity:
O(log n)
