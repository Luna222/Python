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

#sub-class, inheriting from Employee
class Developer(Employee):
    raise_amount = 1.10 #increase 10%

    def __init__(self, first, last, pay, pro_lang):
        super().__init__(first, last, pay)
        self.pro_lang = pro_lang

class Manager(Employee):
    #emplyees here is a list of employee objects(instances)
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees =  employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
        else:
            raise Exception("This employee doesn't exist !")

    def print_emps(self):
        for emp in self.employees:
            print(emp.fullname(), end = '-->') #emp is an employee object passing to

print(Employee.num_of_emps)

dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Test', 'User', 60000, 'Java')
dev_3 = Developer('Test1', 'User1', 60000, 'Php')

print(dev_1.__dict__)
print('Dev 1 - pay: {}'.format(dev_1.pay))
dev_1.apply_raise()
print('Dev 1 - After pay raising: {}'.format(dev_1.pay))
print(dev_1.pro_lang)

mgr_1 = Manager('Dimashi', 'Kudaibergenov', 33000, [dev_1])
print('Manager 1 - original: {}'.format(mgr_1.__dict__))
print('Employee list original:')
mgr_1.print_emps()
mgr_1.add_emp(dev_2)
print('\nEmployee list after adding:')
mgr_1.print_emps()
mgr_1.remove_emp(dev_1)
print('\n(Updated) Employee list:')
mgr_1.print_emps()
mgr_1.remove_emp(dev_1)

# print(help(Developer)) #get the info of the sub-class
# 2 built-in functions
print('\n')
print(isinstance(dev_1, Employee))
print(isinstance(dev_1, Manager))
print(issubclass(Manager, Employee))
print(issubclass(Manager, Developer))
