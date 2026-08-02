# (a) Create dictionaries
stock = {"pen": 25, "notebook": 12, "marker": 8}
delivery = {"notebook": 10, "marker": 5, "eraser": 20}

# (b) Update stock
for product in delivery:
    if product in stock:
        stock[product] += delivery[product]
    else:
        stock[product] = delivery[product]

# (c) Display updated stock
print("Updated stock:")
for product in sorted(stock):
    print(product, ":", stock[product])

# (d) Calculate total items
total = 0
for qty in stock.values():
    total += qty

print("\nTotal items in stock:", total)