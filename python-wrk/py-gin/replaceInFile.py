import re, time, os
file_in = "note.txt"
count = 1
with open(file_in, "r") as fin:
    for line in fin:
            print(str(count)+ ':' + line.replace('dog', 'banana man'))
            time.sleep(2)
            count+=1

time.sleep(15)
os.system('clear')
