mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))

for x in mytuple:
    print("RUD \n :- " + x  + "\n --------\n")
