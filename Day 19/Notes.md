Time Complexity (Big-O Basics):
Time complexity measures how the running time of a program increases as the input size increases.
It helps us know whether an algorithm is efficient or slow.
O(1) – Constant Time:
The program takes the same time no matter how big the input is.
Example:
num = int(input("Enter number: "))
print(num * 2)
Even if the input size grows, the time is constant.
O(n) – Linear Time:
Time increases linearly with input size.
Example:
numbers = [1,2,3,4,5]
for num in numbers:
    print(num)
If list size increases -loop runs more times.
O(n²) – Quadratic Time:
Usually happens with nested loops.
Example:
numbers = [1,2,3]
for i in numbers:
    for j in numbers:
        print(i, j)


