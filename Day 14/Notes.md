Inheritance in Python:
Inheritance allows one class to inherit properties and methods from another class.
It promotes:
Code reuse
Cleaner structure
Real-world modeling
Basic Concept:
Parent Class → Base class
Child Class → Derived class
Example:
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print("Vehicle started")


class Car(Vehicle):   
    def display(self):
        print("Brand:", self.brand)


car1 = Car("Toyota")
car1.start()
car1.display()


Output:

Vehicle started
Brand: Toyota

Using super()

If child class has its own constructor:

class Vehicle:
    def __init__(self, brand):
        self.brand = brand


class Car(Vehicle):
    def __init__(self, brand, price):
        super().__init__(brand)   
        self.price = price

    def display(self):
        print("Brand:", self.brand)
        print("Price:", self.price)


car1 = Car("Toyota", 1500000)
car1.display()


