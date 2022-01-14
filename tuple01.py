#fn = input("your file: ")
#fh = open(fn)

fh = open("mbox-short.txt")

r=dict()


for line in fh:
    line = line.rstrip()
    word = line.split()
    if len(word) <3  or word[0]!="From":
        continue

    address = word[1]

    r[address] =r.get(address,0) + 1

#create a list of tuple and sort the list
#t = sorted([(v,k) for k,v in dict.items()])
lst = list()
for address,key in r.items():
    lst.append((key,address))

lst.sort(reverse=True)

for key,address in lst[0:1] :
    print(address,key)
