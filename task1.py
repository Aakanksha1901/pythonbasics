#take 2 numbers from the user and print their sum, difference and product.

a = 10
b = 4

print(a+b)
print(a-b)
print(a*b)


num1 = float(input("Enter first Number: "))
num2 = float(input("Enter Second Number: "))

sum_result= num1 + num2
difference= num1 - num2
product = num1 * num2

print("sum:", sum_result)
print("difference::", difference)
print("product:", product)


#ask user for name , age and city and display formatted message.
name = input("Enter your name: ")
age  =int(input("Enter your age: "))
city = input("enter where are you from: ")

print(f"hello {name}, you are {age}years old and you are from {city}.")

#convert a float value into integer and string and display all three.

a = 5.6
print(a)
print(int(a))
print(str(a))

float_value = float(input("enter float value:"))
int_value = int(float_value)
str_value =str(float_value)

print("float value:", float_value)
print("int value:", int_value)
print("string value: ", str_value)

#Ask the user for their name and print a welcome message.
name =input("Enter your name: ")

print(f"Hello {name} ,welcome to python")

#Personal Details input: name, age, and city.
name = input("enter your name: ")
age  =int(input("Enter your age: "))
city =input("Enter your city name: ")
print(f"hiii {name},you are {age} years old and live in {city}")

#Sum of Two Numbers Take two integers as input and display their sum.
a =int(input("Enter first number: "))
b =int(input("Enter second number: "))           

sum = a + b

print("Sum: ",sum)

#Area of a Circle
#Input: radius
#Output: area = π × r²
#(Use 3.14159 for π)

radius = int(input("Enter Radius: "))

area = 3.14159 * radius * radius

print("area of circle:" ,area)

#Temperature Converter
#Convert Celsius → Fahrenheit
#Formula: F = (C × 9/5) + 32

Celsius = int(input("Enter Temperature: "))
Fahrenheit = (Celsius* 9/5) + 32

print("Temperature in Fahrenheit: ", Fahrenheit)

#Take any input and print its data type using type().
a =input("Enter data: ")
b =float(input("enter values: "))

print(type(a))
print(type(b))


#Simple Interest Calculator Input: P, R, T → Output: SI = (P × R × T) / 100

P =int(input ("Enter P: "))
R =float(input("Enter R: "))
T =int(input("Enter T: "))

SI = (P * R *T )/100

print("Simple Interest: ", SI)

#String to Integer Input: a string like "50" → Convert it to integer and add 10.
a = input("enter number: ")

print(type(a))

a=int(a)
print(a)

b = a +10

print(b)


#Average of 3 Numbers Input three floats → find and display average (with 2 decimal places).
num1 =float(input("Enter first number: "))
num2 =float(input("Enter second number: "))
num3 =float(input("Enter third number: "))

average = (num1 + num2 +num3)/3

print("Average: ", average)

# Boolean Conversion Input any number → print True if non-zero, False if zero.
a = int(input("enter number: "))

print(bool(a))
