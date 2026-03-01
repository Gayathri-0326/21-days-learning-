Object-oriented Programming(OOP) is a programming approach that organizes code using classes and objects.
Ex:
Class - Student
Object- Gayathri(one student)

Class:
A class is a blueprint for creating objects.

Object:
An object is an instance of a class.

Constructor(__init__)
A constructor runs automatically when object is created.
Ex:
class Student:
    def__init__(self,name,age):
      self.name=name
      self.age=age
    def display(self):
      print("Name:",self.name)
      print("Age:",self.age)
s1=Student("Gayu",20)
s1.display()

Output:
Name: Gayu
Age: 20
