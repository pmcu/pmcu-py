import os
import datetime
note ='/home/padraig/note/note.txt'
f = open(note, "a")
print("Write something: ")
content = input()
f.write(content + "\n")

x = datetime.datetime.now()

f.write(str(x) + "\n")
f.write("====================\n")
f.write("Seo rud úr ar fad\n")
f.close()

#open and read the file after the appending:
f = open(note, "r")
print(f.read())



#open and read the file after the appending:
