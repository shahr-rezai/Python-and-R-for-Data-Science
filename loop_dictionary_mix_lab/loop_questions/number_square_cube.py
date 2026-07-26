number = int(input("Enter n: "))
print("Number\tSquare\tCube")
for number in range(1, number+1):
    square = number ** 2
    cube = number ** 3
    print(f"{number}\t{square}\t{cube}")


