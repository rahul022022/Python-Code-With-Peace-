'''
1. Using format() , create a sentence:
"My name is John and I am 25 years old."
by passing "John" and 25 as variables.

'''

sentence = "my name is {} and i am {} year old."

name1 = 'john'
age = 25

print(sentence.format(name1, age))


# Now Do the same using f-strings.

print(f"my name is {name1} and i am {age} year old.")