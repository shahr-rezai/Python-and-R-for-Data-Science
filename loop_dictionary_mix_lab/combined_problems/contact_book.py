# (a) Create contact book
contacts = {}

# (b) Menu-driven contact book
while True:
    print("\n1. Add or update a contact")
    print("2. Search for a contact")
    print("3. Delete a contact")
    print("4. Display all contacts")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        contacts[name] = phone
        print("Contact saved.")

    elif choice == "2":
        name = input("Enter name: ")
        if name in contacts:
            print(name, ":", contacts[name])
        else:
            print("Contact not found.")

    elif choice == "3":
        name = input("Enter name: ")
        if name in contacts:
            del contacts[name]
            print("Contact deleted.")
        else:
            print("Contact not found.")

    elif choice == "4":
        print("\nContacts:")
        for name in sorted(contacts):
            print(name, ":", contacts[name])

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice.")