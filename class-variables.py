class Employee:

    #class variable
    num_of_emps = 0
    raise_amount = 1.04
    #constructor
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        #accessing class variable through the class
        # self.pay = int(self.pay * Employee.raise_amount)

        # accessing class variable through an instance of the class
        self.pay = int(self.pay * self.raise_amount)

print(Employee.num_of_emps)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

print(Employee.num_of_emps)

#assign the raise amount for emp_1 manually
emp_1.raise_amount = 1.05
print(emp_1.__dict__)
# print(emp_2.__dict__)

emp_1.apply_raise()
print(emp_1.pay)
print(emp_1.__dict__)
