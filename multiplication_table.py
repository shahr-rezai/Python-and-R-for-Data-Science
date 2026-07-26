number = int(input("Enter an integer: "))
print("Number\t\tMultiplier\tProduct")
for n in range (1, 13):
    print(f"{number}\t*\t{n}\t =\t {number * n}")