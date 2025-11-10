# 7. Write a Python program that prints whether a number is positive, negative, or zero.

number = int(input("Enter a number:- "))

if number>0:
    print(f"This {number} Number is Positive")
elif number<0:
    print(f"This {number} Number is Negitive")
else:
    print(f"This {number} Number is Zero")