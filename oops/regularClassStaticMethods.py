"""
    [Regular Methods vs Class Methods vs Static Methods]

"""
"""
    Regular Methods in a Class automatically takes instance as the first argument and by Convention we call it 'self'
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

    def apply_raise(self):
        """
            We need to access class variables using Class or an instance of the class
            So raiseAmount is not a correct syntax
        """
        # self.pay = int(self.pay * raiseAmount)
        self.pay = int(self.pay * self.raiseAmount)


# Creating instances
emp1 = Employee('Debadatta', 'Bhattacharjee', 5000)
emp2 = Employee('Deboneil', 'Bhattacharjee', 2000)

# Check raise amount value
print('\nClass Variable Value')
print(Employee.raiseAmount)
print(emp1.raiseAmount)
print(emp2.raiseAmount)


# Calling the Class method
Employee.raise_amount(1.40)

# Check raise amount value
print('\nBy Class')
print(Employee.raiseAmount)
print(emp1.raiseAmount)
print(emp2.raiseAmount)


# Using instance to change the values of Class Variables
emp1.raise_amount(1.9)
# Check raise amount value
print('\nBy Instance')
print(Employee.raiseAmount)
print(emp1.raiseAmount)
print(emp2.raiseAmount)
