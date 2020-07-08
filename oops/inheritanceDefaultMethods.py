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
        return '{} {}'.format(self.fname, self.lname)

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
        Changing raiseAmount value for Developers and not Employee
    """
    raiseAmount = 1.20

    def __init__(self, fname, lname, pay, programmingLanguage):
        """
        [super method]
            We want to introduce programming language for the developers, we dont want the same for Employees
        """
        super().__init__(fname, lname, pay)
        self.programmingLanguage = programmingLanguage


class Manager(Employee):
    def __init__(self, fname, lname, pay, employees=None):
        """
        [super method]
            We want to introduce programming language for the developers, we dont want the same for Employees
        """
        super().__init__(fname, lname, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def addEmployees(self, emps):
        if emps not in self.employees:
            self.employees.append(emps)

    def removeEmployees(self, emps):
        if emps in self.employees:
            self.employees.remove(emps)

    def printEmployees(self):
        for emps in self.employees:
            print('Employee -> ', emps.fullName())


# Creating instances
emp1 = Employee('Debadatta', 'Bhattacharjee', 5000)
emp2 = Employee('Deboneil', 'Bhattacharjee', 2000)
# Developer Class instances
dev1 = Developer('Rock', 'Bhattacharjee', 5000, 'Python')
dev2 = Developer('Max', 'Bhattacharjee', 2000, 'Javascript')
# Manager Class Instances
mgr1 = Manager('Abhijit', 'Chanda', 5500000, [emp1])
mgr1.addEmployees(dev2)
mgr2 = Manager('Rahul', 'Jotder', 6500000, [emp2])
mgr2.addEmployees(dev1)

"""[isInstance]
    isInstance tells us if an object is an instance of the Class
"""

print('\nCheck Instance')

print(isinstance(mgr1, Employee))
print(isinstance(mgr1, Developer))
print(isinstance(mgr1, Manager))

print('\nCheck Subclass')

print(issubclass(Developer, Employee))
print(issubclass(Employee, Developer))
print(issubclass(Manager, Employee))
