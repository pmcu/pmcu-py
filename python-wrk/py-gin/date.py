import datetime
x = datetime.datetime.now()
print('Scéal an Dáta')
print("-----------\n")
print(x.year)
print(x.strftime("%A"))
print(x.strftime("%B"))

print(x.strftime("%d"))
print(x.strftime("%H"))
print(x.strftime("%M"))
print("-----------\n")
print(x)
