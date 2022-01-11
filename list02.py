# fn = input("Enter a file name:") fh = open(fn)

fh = open("mbox-short.txt")
count = 0
for line in fh:
    line = line.rstrip()
    if line.startswith("From"):
        word = line.split()
        print(word[1])
        count = count+1
print("so far so good")
print("there were",count, "lines in the file with From")
