ch = input("Enter a single alphabet:").lower()
if ch in('a', 'e', 'i', 'o', 'u'):
    print("Vowel")
elif ch.isalpha():
    print("consonant")
else:
    print("not an alphabet")


num = float(input("enter number: "))

if num %5 == 0 and num %11 ==0 :
    print("number is divisible by 5 and 11.")
else:
    print("not divisible.")