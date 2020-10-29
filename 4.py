palindromes = []

def isPalindromic(n):
    if str(n) == str(n)[::-1]:
        return True
    else:
        return False

for x in range(999, 1, -1):
    for y in range(999, 1, -1):
        product = x * y
        if isPalindromic(product):
            palindromes.append(product)

largest_palindrome = max(palindromes)
print(largest_palindrome)