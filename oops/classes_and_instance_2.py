class Employee:
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


# Creating instances
emp1 = Employee('Debadatta', 'Bhattacharjee', 5000)
emp2 = Employee('Deboneil', 'Bhattacharjee', 2000)

# Print Email
print(emp1.email)

# Print full name
# print('{} {}'.format(emp1.fname, emp1.lname))
"""
    Code Resuability
"""
print(emp1.fullName())
# Another way
print(Employee.fullName(emp1))
