# https://projecteuler.net/problem=1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

num = 0
limit = 1000
total = 0

while num < limit:
    print(num)
    if num % 3 == 0 or num % 5 == 0:
        total += num
    num += 1

print(total)