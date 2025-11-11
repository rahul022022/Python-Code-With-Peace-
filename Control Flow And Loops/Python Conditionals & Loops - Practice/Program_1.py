# 1. Write a program that asks the user for a number and prints whether it is positive, negative, or zero.


number = int(input("Enter a Number:- "))
print(number)

if number>0:
    print(f"This {number} Number is positive ")

elif number<0:
    print(f"This {number} Number is negative ")
else:
    print(f"This {number} Number is zero ")