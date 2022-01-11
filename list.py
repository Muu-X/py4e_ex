fn = input("Enter file: ")
fh = open(fn)

u_w = list()
for line in fh:
    line = line.rstrip()
    word = line.split()

    for i in word:
        if i not in u_w:
            u_w.append(i)

u_w.sort()
print(u_w)
