import datetime


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

    @classmethod
    def createNewEmployee(cls, emp):
        fname, lname, pay = emp.split('-')
        return cls(fname, lname, pay)

    @staticmethod
    def checkWorkDay(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

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

# Employee details as strings
empDet1 = 'Reenakshi-Bhatt-7000'
emp3 = Employee.createNewEmployee(empDet1)

print(emp3.email)
print(emp3.pay)

myDate = datetime.date(2016, 7, 10)
# Calling Static Methods
print(Employee.checkWorkDay(myDate))
