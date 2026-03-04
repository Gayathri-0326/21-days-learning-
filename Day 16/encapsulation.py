class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary   # private variable

    def show_salary(self):
        print("Salary:", self.__salary)

    def update_salary(self, new_salary):
        self.__salary = new_salary
        print("Salary updated successfully")



emp1 = Employee("Gayathri", 30000)

emp1.show_salary()

emp1.update_salary(40000)

emp1.show_salary()
