# 2. Write a program using match case that simulates a simple calculator.
# Ask the user for two numbers and an operation (+, -, *, /).
# Perform the operation using match case .


num1 = int(input("Enter a Number1:- "))
num2 = int(input("Enter a Number2:- "))

choice = input("Enter a choice ' +, -, /, * ':- ")

match choice:
    case "+":
        print("Addition:- ", num1+num2) 
    case "-":
        print("Subtraction:- ", num1-num2) 
    case "/":
        print("Divition:- ", num1/num2) 
    case "*":
        print("Multiplication:- ", num1*num2) 
    case _:
        print("Invalid Choice")