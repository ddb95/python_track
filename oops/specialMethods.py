
"""[Dunder Methods (__init__) are special methods]

    Dunder means double underscore
    like dunder init => __init__


    1. __repr__
    Unabmbiguous representation of the object, for developers, used in loggin/debugging

    2. __str__
    Readable representation of the object, for end users


    **IMPT**
    When we print the employee object, it will print the template of __str__ first and if not avaiable it will print the __repr__ template


    We can also print them indivisually
"""


class Employee:
    raiseAmount = 1.04

    def __init__(self, fname, lname, pay):
        self.firstName = fname
        self.lastName = lname
        self.pay = pay
        self.email = fname + '.' + lname + '@gmail.com'

    def apply_raise(self):
        self.pay = int(self.pay * self.raiseAmount)

    def fullName(self):
        return '{} {}'.format(self.firstName, self.lastName)

    def __repr__(self):
        return "Employee('{}' '{}' '{}')".format(self.firstName, self.lastName, self.pay)

    def __str__(self):
        return "Employee('{}' '{}' '{}' '{}')".format(self.firstName, self.lastName, self.pay, self.email)


emp1 = Employee('Debadatta', 'Bhattacharjee', 1000)
# Before __repr__ and __str__ methods
# <__main__.Employee object at 0x7f11745134f0>
print(emp1)
