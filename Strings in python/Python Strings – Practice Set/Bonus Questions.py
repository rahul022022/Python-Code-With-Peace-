# 1. Write a program that counts how many vowels are in a given string.
sentence = "Coding in Python is Fun"
vowels = ['a','e','i','o','u']
sum = 0

for char in sentence.lower():
    if char in vowels:
        sum += 1

print(f"There are {sum} vowels in this sentence")


# now user will add sentence

user = input("Enter Sentence:- ")
vowels = ['a','e','i','o','u']
sum = 0

for char in user.lower():
    if char in user:
        sum += 1

print(f"There are {sum} vowels in this sentence")




# 2.Take a user input string and check if it is a palindrome (same forwards and backwards).

name = input("Enter a sentence:- ")

if name == name[::-1]:
    print(f"This {name} sentecne is palindrome")
else:
    print(f"This {name} sentecne is not palindrome")