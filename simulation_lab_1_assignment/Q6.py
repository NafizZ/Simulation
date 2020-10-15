def isPrime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for x in range(2,n):
            if n % x == 0:
                return False
        return True


x = int(input("input a number: "))
if isPrime(x):
    print(" prime")
else:
    print(" not prime")
