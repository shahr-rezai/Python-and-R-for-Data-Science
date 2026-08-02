# (a) Input validation
n = int(input("Enter a positive integer: "))

while n <= 0:
    print("Invalid input. Try again.")
    n = int(input("Enter a positive integer: "))

# (b) Countdown
while n > 0:
    print(n)
    n -= 1

print("Launch!")