"""[Property Decorators]
Returns:
    Allows our class attribute getter setter and deleter functionality

    Property decorator allows us to define a method but we can access it like an attribute
"""


class Employee:
    raiseAmount = 1.04

    def __init__(self, fname, lname, pay):
        self.firstName = fname
        self.lastName = lname
        self.pay = pay
        # self.email = fname + '.' + lname + '@gmail.com'

    def apply_raise(self):
        self.pay = int(self.pay * self.raiseAmount)

    def fullName(self):
        return '{} {}'.format(self.firstName, self.lastName)

    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.firstName, self.lastName)

    def __repr__(self):
        return "Employee('{}' '{}' '{}')".format(self.firstName, self.lastName, self.pay)

    def __str__(self):
        return "Employee('{}' '{}' '{}' '{}')".format(self.firstName, self.lastName, self.pay, self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullName())


emp1 = Employee('Debadatta', 'Bhattacharjee', 1000)
emp2 = Employee('Deboneil', 'Bhattacharjee', 10000)


# Problem without getter and setter
# Changing name to "Mohar"

emp1.firstName = 'Mohar'
# Employee('Mohar' 'Bhattacharjee' '1000' 'Debadatta.Bhattacharjee@gmail.com')
# Thus we see that first name changes but the email doesnt reflect the same
print(emp1)
print(emp1.fullName())
# print(emp1.email())

# Adding property decorator
print(emp1.email)
