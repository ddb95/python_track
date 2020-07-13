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

    """
    Setting up a setter
    1. Add @property in the method(fullname())
    2. Add another decorator @method.setter (@fullname.setter)
    3. Another method with same method name(def fullname(self, name))
    """

    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.firstName, self.lastName)

    @property
    def fullName(self):
        print('getter method called')
        return '{} {}'.format(self.firstName, self.lastName)

    @fullName.setter
    def fullName(self, name):
        print('setter method called')
        self.firstName, self.lastName = name.split(' ')

    @fullName.deleter
    def fullName(self):
        print('deleter method called')
        self.firstName = None
        self.lastName = None

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

# trying to set a full name and coversely change the first name and last name
emp1.fullName = "Neil Padra"
print(emp1.firstName)
print(emp1.lastName)
print(emp1.fullName)
# Doesnt work

# Deleting the fname and lname
del emp1.fullName
print(emp1)
