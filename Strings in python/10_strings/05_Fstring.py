# String Formating

templates = "Dear {}, You are awsome. Take this {}$ bag"

name_1 = "John"
amount_1 = 10000
name_2 = "maira"
amount_2 = 2000
name_3 = "alex"
amount_3 = 22000

print(templates.format(name_1, amount_1))

# Now this Is a new way to use variable inside a string

print(f"Hey {name_3} You Are awsome. Take This {amount_3}$ bag")