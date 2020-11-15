# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(n: int):
    temp=n
    rev=0
    while(n>0):
        dig = n % 10
        rev = rev * 10 + dig
        n = n // 10
    return temp == rev


def solution():
    # set maximum number
    min_number = 99
    max_number = 999
    # collect palidromes
    palindromes = list()
    # iterate over 3-digit numbers in decrescent order
    for n in range(max_number, min_number, -1):
        for m in range(n, min_number, -1):
            p = n * m
            # we safely assume the largest palindrome is a product at least above 1M. This let us break the inner loop if we reach a low product
            if p < 100000:
                break
            if is_palindrome(p):
                palindromes.append(p)
                break
    return max(palindromes)
