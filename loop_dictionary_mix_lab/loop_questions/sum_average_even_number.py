number = int(input("Enter number: "))

total = 0
count = 0

print("Even numbers:", end=" ")

for n in range(1, number+1):
    if n % 2 == 0:
        print(n, end=" ")
        total = total + n
        count = count + 1
average = total/count
print()
print("Sum: ", total)
print("Average: ", average)         