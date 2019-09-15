import re, os

#Split the string at every white-space character:
file2 = "setUnique.txt"
file = "note.txt"
with open(file, "r") as f:
    for line in f:
        for word in line.split():
            print(word)
            
