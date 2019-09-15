class Person:
  def __init__(self, fname, lname):
    self.fname = fname
    self.lname = lname

  def printname(self):
    print(self.fname, self.lname)

class Student(Person):
  def __init__(self, fname, lname, year):
    Person.__init__(self, fname, lname)
    self.graduationyear = year
  def bliain(self):
      print("Fuair sé céim sa bhliain : ", self.graduationyear)

x = Student("Mike", "Olsen", 1919)
print("Ainm: " + x.fname)
print("Sloinneadh: " + x.lname)
x.bliain()
