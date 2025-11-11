# Write a program that takes a number from the user and prints “Even” if it is even, otherwise “Odd”.

number = int(input("Enter a Number:- "))

if number%2==0:
    print(f"This {number} Is a Even Number")
else:
    print(f"This {number} Is a Odd Number")