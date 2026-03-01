class Car:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def display(self):
        print("Brand:", self.brand)
        print("Price:", self.price)
car1 = Car("Toyota", 1500000)
car1.display()
print("------")
car2 = Car("Hyundai", 1000000)
car2.display()
