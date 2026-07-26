number = int(input("Enter a nonnegataive integer: "))
factorial = 1;
if number == 0:
    print('0! = 1')
for n in range(1, number+1):
    factorial = factorial * n
    if n == number:
        print(n, end=" ")
    else:
        print(n, end=" * ")
print("=", end=" ")
print(factorial)
    

    
