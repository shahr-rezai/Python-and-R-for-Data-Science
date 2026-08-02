# (a) Create dictionaries
prices = {"rice": 75.0, "oil": 185.0, "milk": 95.0, "eggs": 12.0}
quantities = {"rice": 20, "oil": 10, "milk": 15, "eggs": 60}

# (b) Calculate stock values
total = 0
highest_product = ""
highest_value = 0

print("Product-wise stock values:")
for product in prices:
    value = prices[product] * quantities[product]
    print(product, ":", value)
    total += value
    if value > highest_value:
        highest_value = value
        highest_product = product

# (c) Display total and highest value product
print("\nTotal inventory value:", total)
print("Highest stock value product:", highest_product)