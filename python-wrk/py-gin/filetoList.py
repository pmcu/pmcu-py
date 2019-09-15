with open('outfile.txt') as f:
    lines = f.read().split()

myset = set(lines)
for x in myset:
    print(x)
