#print 1 to 5
i = 1
while i <= 5:
    print(i)
    i +=1

##decrementing loop
count = 5
while count > 0:
    print(count)
    count -= 1


##using break and continue
i=0
while i < 10:
    i += 1
    if i==5:
        continue
    print(i)


#infinte loop
while True:
    print("Running")
    break