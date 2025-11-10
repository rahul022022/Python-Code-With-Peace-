# Write a Python program to find the largest of two numbers using conditional statements.

num1 = int(input("Enter Number 1:- "))
num2 = int(input("Enter Number 2:- "))

if num1>num2:
    print("Number 1 is larger then Number 2")
elif num1<num2:
    print("Number 2 is larger then Number 1")
else:
    print("Both Numbers are equal")