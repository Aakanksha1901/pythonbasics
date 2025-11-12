#print numbers 1 to 5
for i in range(1, 6):
    print(i)


#loop over a list.
fruits =[ "apple", "banana", "mango"]
for item in fruits:
    print("I like", item)


#loop over a string

for ch in "PYTHON":
    print(ch)


#range() variations
for i in range(2, 11, 2):
##start=2,stop=11,step=2
    print(i)


for i in range(1, 10):
    if i ==5:
        break
    print(i)


for i in range(1, 10):
    if i== 5:
        continue
    print(i)


