"""
    Inheritance allows you to access attributes and methods from parent class
    We can create subclasses, overwrite a new functionality
"""


class Employee:
    # Class variable
    raiseAmount = 1.04
    numberOFEmployees = 0

    # Contructor
    def __init__(self, fname, lname, pay):
        # It can be as well like
        # self.firstName = fname
        # but a good practice to keep it same
        self.fname = fname
        self.lname = lname
        self.pay = pay
        # Custom attribute
        self.email = fname + '.' + lname + '@gmail.com'

        # Increasing the number of employees
        Employee.numberOFEmployees += 1

    # Regular Method
    def fullName(self):
        return '{} {}'.format(emp1.fname, emp1.lname)

    # Class method: takes Class as the first argument
    # cls is the common convention for class like 'self' for regular methods inside class
    @classmethod
    def raise_amount(cls, amount):
        cls.raiseAmount = amount

    # Regular Method
    def apply_raise(self):
        """
            We need to access class variables using Class or an instance of the class
            So raiseAmount is not a correct syntax
        """
        # self.pay = int(self.pay * raiseAmount)
        self.pay = int(self.pay * self.raiseAmount)


# Create a sub class developer
class Developer(Employee):
    pass


# Creating instances
emp1 = Employee('Debadatta', 'Bhattacharjee', 5000)
emp2 = Employee('Deboneil', 'Bhattacharjee', 2000)
# Developer Class instances
dev1 = Developer('Rock', 'Bhattacharjee', 15000)
dev2 = Developer('Max', 'Bhattacharjee', 20000)

# print(dev1.email)
# print(dev2.pay)


# Finding the Definition and inheritance
# print(help(Developer))
# print(help(Employee))
