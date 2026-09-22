def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False

    return True

n = int(input("Enter any number: "))

if is_prime(n):
    print("The number is prime")
else: 
    print("The number is not prime")