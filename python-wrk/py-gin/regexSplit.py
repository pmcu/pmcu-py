import re

#split the string at the first white-space
#character

str ="The rain in Spain"
x = re.split("\s", str)
print(x)
for y in x:
    print(y)
