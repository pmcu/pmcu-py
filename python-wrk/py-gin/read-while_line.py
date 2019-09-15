import datetime
# Open the file with read only permit
f = open('lines.txt')

print("----------")
# print(f.readline())
head = [next(f) for x in range(2)]
# print(head)
for x in head:
    print(x)
x= datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))
print(x.strftime("%B"))
print(x.strftime("%d"))
f.close()
