number = int(input("Enter an integer greater than 1: "))
for i in range (2, number):
    if number%i==0:
        print(f"{number} is not prime, Its first divisor is {i}")
        break
    
else: print(f"{number} is a prime")