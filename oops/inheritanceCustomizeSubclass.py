"""
    Customizing Subclass using Inheritance
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
    """
        Changing raiseAmount value for Developers
    """
    raiseAmount = 1.20

    def __init__(self, fname, lname, pay, programmingLanguage):
        """
        [super method]
            We want to introduce programming language for the developers, we dont want the same for Employees
        """
        super().__init__(fname, lname, pay)
        self.programmingLanguage = programmingLanguage


# Creating instances
emp1 = Employee('Debadatta', 'Bhattacharjee', 5000)
emp2 = Employee('Deboneil', 'Bhattacharjee', 2000)
# Developer Class instances
dev1 = Developer('Rock', 'Bhattacharjee', 5000, 'Python')
dev2 = Developer('Max', 'Bhattacharjee', 2000, 'Javascript')

"""
    We can see that the developer instance took the new value of raiseAmount
"""
print('Dev 2')
print(dev2.pay)
dev2.apply_raise()
print(dev2.pay)
print('\nEmp 2')
print(emp2.pay)
emp2.apply_raise()
print(emp2.pay)


# Overwritten __init__() method which we need to see.
print('\n')
print('Overwritten __init__() method')
print(dev1.email)
print(dev1.programmingLanguage)
