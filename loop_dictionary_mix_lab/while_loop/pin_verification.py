# (a) Store correct PIN
correct_pin = "2468"
attempts = 3

# (b) Verify PIN
while attempts > 0:
    pin = input("Enter PIN: ")

    if pin == correct_pin:
        print("Access granted")
        break

    attempts -= 1
    if attempts > 0:
        print("Incorrect PIN. Attempts remaining:", attempts)
    else:
        print("Account locked")