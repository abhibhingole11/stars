

n = int(input("Enter a number: "))
if n<=1:
    print("It is not a prime number")
else:
    is_prime = True
    for i in range(2,n):
        if n%i==0:
            is_prime = False
            break
    if is_prime == True:
        print('it is prime number')
    else:
        print('it is not prime number')
            

