class Employee:
    def __init__(self,first,last,pay):
        self.first= first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('Corey','shafer',50000)
emp_2 = Employee('Test','User',60000)

print(emp_2.fullname())










# emp_1.first = 'Corey'
# emp_1.last = 'Schafer'
# emp_1.email = 'corey.shafer@comp.com'
