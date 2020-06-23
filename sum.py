def add(x, y):
    return x + y

print(add(3, 6))

def isPrime(n):
    for i in range(2, n-1):
        if n % i == 0:
            return False
    return True

print(isPrime(15))