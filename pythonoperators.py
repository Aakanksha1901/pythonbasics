a ,b = 10, 5
x, y = True, False
lst = [1, 2, 3, 4]

print("====Arithmetic Operators====")
print("Addition: ", a + b)
print("Substraction: ",a - b)
print("Multiplication: ", a * b)
print("Division: ", a / b)
print("floor division:", a//b )
print("Modulus: ", a % b)
print("Exponentiation: ", a ** b)


print("\n===Relational Operators===")
print("a > b:", a > b)
print("a < b:", a  < b)
print("a==b :", a==b)
print("a !=b :", a!=b)
print("a>= b:", a>=b)
print("a ,=b: ", a <= b)

print("\n=====Logical Operators====")
print("x and y:", x and y)
print("x or y: ", x or y)
print("not x:", not x)

print("\n==== Assignment Operators ====")
c = 10
c += 5
print("After += :", c)

c -= 3
print("After -= :", c)

c *= 2
print("After *= :", c)

c /= 4
print("After /= :", c)

print("\n===== Bitwise Operators====")
print("a & b:", a & b)
print("a | b:", a | b)
print("a ^ b:", a ^ b)
print("~a :", ~a)
print("a << 1 :", a << 1)
print("a >> 1 :", a >> 1)


print("\n====Membership Operators====")
print("3 in lst: ", 3 in lst)
print("10 not in lst: ", 10 not in lst)


print("\n ==== identity operators==")
p =[1,2,3]
q =p
r =[1,2,3]

print("p is q:",p is q)
print("p is r:", p is r)
print("p is not r", p is not r)