#for every outer loop there is inner loop.
for i in range(1,4):
    for j in range(1,4):
        print(i,j)


#loop with else
for i in range(3):
    print(i)
else:
    print("Loop Completed")


#loop with enumerate()
names = ["Amit", "Neha", "Raj"]
for index, name in enumerate(names):
   print(index ,name)


   