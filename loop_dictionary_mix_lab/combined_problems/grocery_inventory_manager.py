# (a) Create inventory
inventory = {
    "rice": {"price": 75.0, "quantity": 20},
    "milk": {"price": 95.0, "quantity": 15}
}

# (b) Menu-driven inventory manager
while True:
    print("\n1. Add product")
    print("2. Restock product")
    print("3. Sell product")
    print("4. Display inventory")
    print("5. Total inventory value")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter product name: ")
        price = float(input("Enter price: "))
        qty = int(input("Enter quantity: "))
        if price >= 0 and qty >= 0:
            inventory[name] = {"price": price, "quantity": qty}
            print("Product added.")
        else:
            print("Price and quantity must be non-negative.")

    elif choice == "2":
        name = input("Enter product name: ")
        if name in inventory:
            qty = int(input("Enter quantity to add: "))
            if qty >= 0:
                inventory[name]["quantity"] += qty
                print("Stock updated.")
            else:
                print("Quantity must be non-negative.")
        else:
            print("Product not found.")

    elif choice == "3":
        name = input("Enter product name: ")
        if name in inventory:
            qty = int(input("Enter quantity to sell: "))
            if qty <= inventory[name]["quantity"]:
                inventory[name]["quantity"] -= qty
                print("Sale completed.")
            else:
                print("Insufficient stock.")
        else:
            print("Product not found.")

    elif choice == "4":
        print("\nInventory:")
        for name in sorted(inventory):
            value = inventory[name]["price"] * inventory[name]["quantity"]
            print(name, "- Price:", inventory[name]["price"],
                  "Quantity:", inventory[name]["quantity"],
                  "Stock Value:", value)

    elif choice == "5":
        total = 0
        for item in inventory.values():
            total += item["price"] * item["quantity"]
        print("Total inventory value:", total)

    elif choice == "6":
        print("Exiting...")
        break

    else:
        print("Invalid choice.")