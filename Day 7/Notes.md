Lists in python:
A list is a collection of multiple items stored in a single variable. Lists are ordered, changeable, and allow duplicate values.
Syntax:
list_name=[item1,item2,item3]
*index starts from 0
*append()-add item
*remove()-delete item
*len()-counting items

Accessing elements:
numbers=[10,20,30}
print(number[0])
print(number[1])
o/p:
10
20
Adding elements:
numbers=[10,20]
numbers.append(30)
print(numbers)
o/p:
[10,20,30]
Removing elements:
numbers=[10,20,30]
numbers.remove(20)
print(numbers)
o/p:
[10,20]
Length of list:
numbers=[1,2,3,4]
print(len(numbers))
o/p:
4
Loop through list:
numbers=[1,2,3,4]
for num in numbers:
  print(num)
o/p:
1
2
3
