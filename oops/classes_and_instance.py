class Employee:
    """
        Class Name: Employee
        attributes: name, email, lname, pay
    """
    pass


# Instantiate a Class
emp1 = Employee()
emp2 = Employee()
# print(emp1)
# print(emp2)

# Manually Instantiate attributes
"""
    Manually Instantiate the attributes without mentioning in the class.
    Not a good workflow
    There's too much code to work around and inefficient to maintain
    So we need to create in classes
"""
emp1.name = 'Debadatta'
emp1.lname = 'Bhattacharjee'
emp1.email = 'Bhattacharjee@gmail.com'
emp1.pay = 10000
# Second emp
emp2.name = 'Debaneil'
emp2.lname = 'Bhatt'
emp2.email = 'neilacharjee@gmail.com'
emp2.pay = 10050
print(emp1.pay)
print(emp2.name)
