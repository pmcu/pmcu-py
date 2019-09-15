import re

str = "The rain in Spain"
str2 ="""
Tá an cat ar an tábla agus
is tábla an deas a bhfuil an cat
ina shuí ar mar is tábla buí an
tábla sin.
"""
#x = re.search("ai", str)
#print(x) #this will print an object
x = re.findall("tábla", str2)
print(x)
