# open a new file to write
file = "myOutfile.txt"
outF = open(file, "w")

text = """
==================
An asal agus
an banana man
was up the street
and it was cat.
==================
"""

outF.writelines(text)
outF.close()
outF = open(file, "r")

print(outF.read())
