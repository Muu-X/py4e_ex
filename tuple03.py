fn = input("enter you file:")
try:
    fh = open(fn)
except:
    print("not found")
    quit()

import string
lowercaseletter = list(string.ascii_lowercase)

letterdict = dict()
for line in fh:
    line = line.lower().rstrip()
    for letter in line:
        if letter not in lowercaseletter:
            continue
        letterdict[letter] = letterdict.get(letter,0) + 1
#从小到大
t = sorted([(v,k) for k,v in letterdict.items()])
for v,k in t:
    print(k,v)
