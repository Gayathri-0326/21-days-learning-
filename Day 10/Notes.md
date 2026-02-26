Sets in Python:
A set is a collection of unique elements.
Sets are unordered and do not allow duplicate values.
Syntax:
set_name = {value1, value2, value3}
Example:
numbers = {1, 2, 3, 4}
print(numbers)
Output:
{1, 2, 3, 4}
Duplicate values are removed:
numbers = {1, 2, 2, 3, 4, 4}
print(numbers)
Output:
{1, 2, 3, 4}
Add element:
numbers.add(5)
Remove element:
numbers.remove(3)
Set Operations:
A = {1, 2, 3}
B = {3, 4, 5}
Union: A | B
Intersection: A & B
Difference: A - B

