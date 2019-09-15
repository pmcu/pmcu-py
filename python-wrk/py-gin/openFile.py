import re, os, time
f = open("note.txt", "r")

count = 1
word = input("What word ? ")
time.sleep(2)
for line in f:
    if word in line:
         print(str(count) + ': ' + line)
         count+=1



time.sleep(7)
os.system('clear')
# print(line)
