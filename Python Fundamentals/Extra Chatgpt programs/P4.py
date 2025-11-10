# 4.Write a program that takes name and age, and prints whether the user is eligible to vote (age ≥ 18).

name = input("Enter Name: - ")
age = int(input("Enter Age:- "))


print()
print("Analyzing If Eligible For Vote")
print("Name :-", name)
print("Age:- ", age)
if age>=18:
    print(f"{name} You Are eligible to vote") 

else:
    print(f"{name} You Are Not eligible to vote")
