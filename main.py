import random

with open('words.txt') as w:
    l=[]
    lr=[]
# make a list of all words in words.txt
    for i in w:
        l.append(i)

# convert list to string and ignore the newline(\n) and again append in a list
for i in l:
    s=str(i)
    lr.append(s.rstrip('\n'))

# ignore the last empty ' ' in the list
print(lr[0:-1])

r=random.choice(lr)
listofrandom=[]
for i in r:
    listofrandom.append(i)




