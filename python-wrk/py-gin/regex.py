import re
txt ="The rain in Spain"
x = re.search("^dog", txt)
if (x):
    print("Aye, he's there")
else:
    print("not at all")
