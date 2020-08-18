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
    # Some dunder methods
    # Representation of an object: (displaying objects)
    def __repr__(self): # used in debugging, logging
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

    def __str__(self): # used as a display to users (more priority)
        return '{} - {}'.format(self.fullname(), self.email)

    # Customized __add__ function
    def __add__(self, other):
        # return self.pay + other.pay
        return self.fullname() + '-' + other.fullname()

    # Customized __len__ function to count the length of employee's fullname
    def __len__(self):
        return len(self.fullname())

    # Other dunder methods
    print(int.__add__(1, 2)) # == print(1+2) (built-in function)
    print(str.__add__('a', 'b')) # == print('a' + 'b') (built-in function)

    print('test'.__len__()) # == print(len('test'))


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

print(emp_1)
# access an object (instance) representation specifically
# print(repr(emp_1))
# print(str(emp_1))
print(emp_1.__repr__())
print(emp_1.__str__())
print(emp_1.__add__(emp_2))# == print(emp_1 + emp_2)
print(emp_1.__len__()) # == print(len(emp_1))
