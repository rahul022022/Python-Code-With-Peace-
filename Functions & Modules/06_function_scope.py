def sum(a,b):
    # a and b are local variable
    c = a+b
    z = 1 # it creates a local variable called z which is destroyed after function is returns 
    return c

def greet():
    z = 32 # local variable
    print("hello")
z = 8 # z is global variable
print(z)
print(sum(4, 6))
print(z)
