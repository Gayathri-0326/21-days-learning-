class Animal:
    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def sound(self):   # Overriding
        print("Dog barks: Woof Woof")


d1 = Dog()
d1.sound()
