# https://projecteuler.net/problem=3
# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

x = 600851475143
prime_factors = []

def isPrime(n):
    print("Considering if %s is prime" % n)
    if n <= 1 or n % 1 > 0 or n % 2 == 0 or n % 3:
        return False
    for i in range(2, n//2):
        if n % i == 0:
            return False
    return True

for i in range(2, x):
    if (x % i) == 0 and isPrime(i):
        prime_factors.append(i)
        print(i)

print(prime_factors)