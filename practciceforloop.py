##print numbers between 1 to 10
for i in range (1,11):
    print(i)

#print even numbers between 1 to 50
for i in range(2,51,2):
    print(i)

#print even numbers between 1 to 50
#for i in range(1,51):
 #   if 

#sum of first 10 natural numbers:
total = 0
for i in range (1,11):
    total += i
print("Sum =", total)


#odd numbers between 1 to 20

i = 1
while i<=20:
    if i %2!= 0:
        print(i,end=" ")
    i +=1 

#square
for i in range(1,6):
    print(f"{i}^2= {i**2}")


#table of 7.
n= 7
for i in range(1,11):
    print(f"{n}*{i}={n*i}")


num = int(input("Enter a number:"))
fact = 1

for i in range(1, num + 1):
    fact *= i

print("factorial= ", fact)


num = int(input("enter a number: "))
count = 0
while num > 0:
    num //= 10
    count +=1

print("number of digits", count)


for i in range(10,0,-1):
    print(i, end=" ")


#sum of all even numbers
total = 0
for i in range(2,101,2):
    total += i
print("sum=", total)


#fibonnacci series
n =int(input("enter number of terms: "))
a, b= 0,1
print("Fibonacci Series: ")
for i in range(n):
    print(a, end=" ")
    a,b =b, a+b 


#reverse a number using while loop
num=int(input("Enter a number: "))
rev = 0
while num> 0:
    digit =num % 10
    rev =rev * 10 + digit
    num //=10

print("Reversed number: ",rev)




#check if a number is palindrome
num= int(input("Enter a number: "))
temp = num 
rev = 0

while num > 0:
    rev = rev * 10 + num * 10
    num //= 10

if temp == rev:
    print("palindrome number")
else:
    print("not a palindrome")



##prime numbers:
print("prime numbers between 1 to 100")
for num in range (2,101):
    for i in range(2,num):
        if num %i ==0:
            break
        else:
         print(num,end=" ")

        
num=int(input("Enter a number:"))
product = 1
for digit in str(num):
    product *= int(digit)
print("product of digits: ", product)


for i in range(1,6):
    print("*" * i)


total = 0
while True:
    num = int(input("enter a number(0 to stop): "))
    if num == 0:
        break
    total += num
print("total sum:", total)



for i in range(1,6):
    for j in range(1, i+1):
        print(j, end=" ")
    print()


while True:
    print("\n Menu:")
    print("1.Add")
    print("2.Substract")
    print("3.Multiply")
    print("4.Exit")

    choice = int(input("enter ypur choice:"))

    if choice ==4:
        print("exiting program")

        break
    elif choice not in (1,2,3):
             print("invalide choice.try again.")
        
             continue

    a = int(input("enter first number: "))
    b = int(input("enter second number: "))

    if choice ==1:
        print("result:", a + b)
    elif choice ==2:
        print("result:", a - b)
    elif choice ==3:
        print("result: ", a * b )
    



