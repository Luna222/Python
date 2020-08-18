import time as _time
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

    #regular class method
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        #accessing class variable through the class
        # self.pay = int(self.pay * Employee.raise_amount)

        # accessing class variable through an instance of the class
        self.pay = int(self.pay * self.raise_amount)

    @classmethod #decorator
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    #class method can be used as an alternative constructor
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay) #return new employee object

    @classmethod
    def fromtimestamp(cls, t):
        y, m, d, hh, mm, ss, weejday, jday, dst = _time.localtime(t)
        return cls(y, m, d) #return a new date/time object

    @classmethod
    def today(cls):
        t = _time.time()
        return cls.fromtimestamp(t)

    @staticmethod # take no instance, no class variable
    # By convention: Moday - 0; Sunday - 6
    def is_workday(day): # day - datetime type
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

print(Employee.num_of_emps)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

print(Employee.num_of_emps)

#check class method
emp_str_1 = 'Taki-Nguyen-50000'
# first, last, pay = emp_str_1.split('-')
# new_emp_1 = Employee(first, last, pay)
new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.__dict__)

#check static method
import datetime
my_date = datetime.date(2020, 8, 17)
print(Employee.is_workday(my_date))

print(emp_1.__dict__)
# print(emp_2.__dict__)

print('Em 1 - pay: {}'.format(emp_1.pay))
# call classmethod
Employee.set_raise_amt(1.05)
emp_1.apply_raise()
print('Emp 1 - After pay raising: {}'.format(emp_1.pay))
