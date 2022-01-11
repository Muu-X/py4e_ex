fh = open("mbox-short.txt")

count = 0
for line in fh:
    line = line.rstrip()
    word = line.split()
    if len(word) >= 2 and line.startswith("From"):
        print(word[1])
        count = count+1

print("there were",count, "lines in the file with From as the first word")
