# open a new file to write
outF = open("myOutfile.txt", "w")

textList =["One","Two","Three","Four","Five"]

for line in textList:
    #write line to output myOutfile
    outF.write(line)
    outF.write("\n")

outF.close()
