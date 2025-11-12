##if else--
##example 1st:
age = int(input("Enter your age: "))
if age >= 18:
    print("you can vote.")
elif age > 0:
    print("you are too young to vote.")
else:
    print("invalid age")



num = float(input("Enter Number:"))
if num > 0:
    print("given number is positive number.")
elif num < 0:
    print("given number is negative number.")
else:
    print("given number is zero.")


a =float(input("Enter 1st number: "))
b =float(input("enter 2nd number: "))
c =float(input("enter 3rd number: "))
if a >=b and a>=c :
   print("largest number is: ",a)
elif b>=a and b>=c :
    print("largest number is: ",b)
else:
    print("largest number is: ",c)



marks =int(input("Enter marks: "))
if marks >=90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >=60:
    grade = "C"
elif marks >= 40:
    grade= "D"
else: 
    grade="F"

print("your grade is: ",grade)


year = int(input("enter a year: "))
if (year % 400 ==0 ) or (year % 4== 0 and year % 100 != 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")



##calculator
print("Select Operation: ")
print("1.Addition")
print("2.Substraction")
print("3.Multiplication")
print("4.Division")

choice = input("Enter choice (1/2/3/4): ")

num1  =float(input("Enter first number: "))
num2  =float(input("Enter second number:"))

if choice == '1':
    print("Result:", num1 + num2)
elif choice == '2':
    print("Result:", num1 - num2)
elif choice == '3':
    print("result:", num1 * num2)
elif choice == '4':
    if num2 != 0:
        print("result:", num1/num2)
    else:
        print("division by zero not allowed.")
else:
    print("invalid choice")


##odd and even
num = int(input("Enter Number: "))

if(num %2 ==0 and num >0 ):
    print("even number: ")
elif(num %2!= 0):
    print("odd number")
else:
    print("given number is zero.")



num = int(input("Enter Number: "))

if num %2 == 0 :
    print("even number: ")
else:
    print("odd number")



