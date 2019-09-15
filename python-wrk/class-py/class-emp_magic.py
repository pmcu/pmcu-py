class Employee:
    def __init__(self,first,last,pay):
        self.first= first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

emp_1 = Employee('John','Smith',50000)

emp_1.fullname = 'Corey Schafer'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)
# print(emp_1)











# emp_1.first = 'Corey'
# emp_1.last = 'Schafer'
# emp_1.email = 'corey.shafer@comp.com'
