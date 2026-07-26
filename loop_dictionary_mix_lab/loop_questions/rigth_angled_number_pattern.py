row_number = int(input("Enter the number of row: "))
counter = 0
for i in range(1,row_number+1):
    for j in range(1, i+1):
        counter+=1
        print(j, end = " ")
    print()
print()

print(f"For {row_number} row, the total is: ", end = " ")

for i in range(1, row_number+1):
    if i == row_number:
        print(i, end=" = ")
    else:
        print(i, end=" + ")
print(counter)





    

