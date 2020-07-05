"""
    Class variables are those variables which are shared among all the instances of a class
    Instance variables can be unique for each instance(eg: name, email, pay)
"""


class Employee:
    # Class variables
    raiseAmount = 1.04
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


# Creating instances
emp1 = Employee('Debadatta', 'Bhattacharjee', 5000)
emp2 = Employee('Deboneil', 'Bhattacharjee', 2000)

print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)

# Access Class Variables
print(emp1.raiseAmount)
print(emp2.raiseAmount)
print(Employee.raiseAmount)

"""
    We can access Class Variables from Class or instance of the class.
    Behind the scenes:
    When we try to access a class variable from an instance, it first checks if the INSTANCE CONTAINS THE ATTRIBUTE, if not
    IT WILL CHECK THE CLASS OR THE CLASS IT INHERITS FROM.

    So here when we try to access raiseamount, the instance of the class(emp1,emp2) does not contain this attribute but 
    the class(Employee) contains the attribute. Lets check it.
"""
print(emp1.__dict__)
print(emp2.__dict__)
print(Employee.__dict__)


"""
    [Changing the raiseamount value]
"""
# Changing the class variable for all instances
Employee.raiseAmount = 1.05
print(Employee.raiseAmount)
print(emp1.raiseAmount)
print(emp2.raiseAmount)

# Changing using Instance(emp1/emp2)
emp1.raiseAmount = 1.10
print(Employee.raiseAmount)
print(emp1.raiseAmount)
print(emp2.raiseAmount)

# Checking emp1 dict
print(emp1.__dict__)
"""
        We see that emp1 has raiseamount within its namespace
    """
