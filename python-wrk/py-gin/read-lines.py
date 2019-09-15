
f = open("lines.txt", "r")
f2 = open("doggy.txt", "a")

f2.write("<p>\n")
for x in f:
  print(x)
  f2.write(x)

f2.write("</p>\n")

f.close()
f2.close()
print("Bye Byes, you boy you!")
