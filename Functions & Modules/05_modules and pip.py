# Two Type of modules in python 
# - built in modules
# - external modules
# List of all the built in modules https://docs.python.org/3/py-modindex.html
import math
import os
import mymodule
import requests

print(math.sqrt(16))
mymodule.hello()
r = requests.get("https://www.youtube.com")
print(r.text)