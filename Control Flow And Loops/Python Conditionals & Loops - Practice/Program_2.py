# 2. Create a program that checks if a person is eligible to vote (age >= 18).

name = input("Enter Your Name:- ")
age_vote_check = int(input("Enter Your Age:- "))

if age_vote_check>=18:
    print(f" hey {name} based on your age {age_vote_check} Your are eligible for vote ")

else:
    print(f" hey {name} based on your age {age_vote_check} Your are not eligible for vote ")
