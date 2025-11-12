s = "hello world" # Strings are immutable

# name[0] = "R" # You cannot do this

a = len(s)
print(a)
print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.title())



print("*******")



text = "\n Hello World "
print('Orignal String:- ',text)
print(text.strip()) # This will remove spaces and provide clean string
print(text.lstrip()) # This will only remove spaces of left side of a string
print(text.rstrip()) # This will only remove spaces of Right side of a string



print("****************")



text_1 = "Python is fun and fun and fun"
print(text_1.find("is")) # Output: 7 Index of list of first occurence
print(text_1.replace("fun", "awesome"))


print("*************")

text_2 = "Appeles, bananas, pinepples"

print(text_2.split(","))
print(",".join(['Appeles', ' bananas', ' pinepples']))



print("************")


text_3 = "python123"

print(text_3.isalpha()) #output: False
print(text_3.isdigit()) #output: False
print(text_3.isalnum()) #output: True
print(text_3.isspace()) #output: False