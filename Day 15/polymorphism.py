Polymorphism in Python
Polymorphism means:
Same method name, different behavior.
“Poly” → many
“Morphism” → forms
So one function behaves differently depending on object.


Polymorphism with Method Overriding



class Animal:
    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def sound(self):
        print("Dog barks")


class Cat(Animal):
    def sound(self):
        print("Cat meows")


a = Animal()
d = Dog()
c = Cat()

a.sound()
d.sound()
c.sound()


Output

Animal makes a sound
Dog barks
Cat meows







