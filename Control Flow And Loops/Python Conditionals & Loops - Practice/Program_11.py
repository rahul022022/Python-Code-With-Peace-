# 2. Write a program that keeps asking the user to enter a password until they enter the correct one.

fix_password = "admin@123"
Entered_password = input("Enter a password:- ")

while Entered_password != fix_password:
    Entered_password = input("Wrong Password Try again and enter Password:- ")
    
print("Success! You are logged in")