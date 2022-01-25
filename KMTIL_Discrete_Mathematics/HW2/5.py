"""
Returns the list of all the prime numbers that are less than 
or equal to n using the sieve of Eratosthenes algorithm
"""

def sieve(n):
    prime = [num for num in range(n) if num > 1]
    prime = [num for num in prime if num == 2 or num % 2 == 1]
    prime = [enum[1] for enum in enumerate(prime) if ((enum[0] - 2) % 3 != 0) or (enum[0] > 4 and enum[0] % 3 != 0) or enum[1] == 5]
    prime = [num for num in prime if num == 5 or num % 5 != 0]
    return prime

print(sieve(30))