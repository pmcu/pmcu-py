import os
import datetime
f = open("demofile2.txt", "a")
print("Write something: ")
content = input()
f.write(content + "\n")

x = datetime.datetime.now()

f.write(str(x) + "\n")
f.write("====================\n")
f.write("Ábhar Úr")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())



#open and read the file after the appending:
