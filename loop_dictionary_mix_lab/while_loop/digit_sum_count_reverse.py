# (a) Input number
n = int(input("Enter a positive integer: "))

# (b) Calculate digits, sum, and reverse
temp = n
digits = 0
digit_sum = 0
reverse = 0

while temp > 0:
    digit = temp % 10
    digits += 1
    digit_sum += digit
    reverse = reverse * 10 + digit
    temp //= 10

# (c) Display results
print("Number of digits:", digits)
print("Sum of digits:", digit_sum)
print("Reversed number:", reverse)