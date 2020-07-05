"""
    When should you not use a self?
    Lets check how many employees do I have?
"""


class Employee:
    # Class variables
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

    # Method to print full Name
    def fullName(self):
        return '{} {}'.format(emp1.fname, emp1.lname)

    # Raise
    def apply_raise(self):
        """
            We need to access class variables using Class or an instance of the class
            So raiseAmount is not a correct syntax
        """
        # self.pay = int(self.pay * raiseAmount)
        self.pay = int(self.pay * self.raiseAmount)


# Check total employees before initialising
print(Employee.numberOFEmployees)

# Creating instances
emp1 = Employee('Debadatta', 'Bhattacharjee', 5000)
emp2 = Employee('Deboneil', 'Bhattacharjee', 2000)

# Check total employees
print(Employee.numberOFEmployees)
