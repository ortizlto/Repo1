Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> print("Hola Gitters")
Hola Gitters
>>> bash
... 
... python3 << 'EOF'
... def sieve_of_eratosthenes(limit):
...     """Generate all prime numbers up to limit using the Sieve of Eratosthenes"""
...     if limit < 2:
...         return []
...     
...     # Create a boolean array and mark all as prime initially
...     is_prime = [True] * (limit + 1)
...     is_prime[0] = is_prime[1] = False
...     
...     # Mark multiples of each prime as not prime
...     for i in range(2, int(limit**0.5) + 1):
...         if is_prime[i]:
...             for j in range(i*i, limit + 1, i):
...                 is_prime[j] = False
...     
...     # Collect all numbers marked as prime
...     primes = [num for num in range(2, limit + 1) if is_prime[num]]
...     return primes
... 
... # Generate primes from 1 to 1000
... primes = sieve_of_eratosthenes(1000)
... 
... print(f"Prime numbers from 1 to 1000:\n")
... print(f"Total count: {len(primes)}\n")
... 
... # Print them in rows of 10 for readability
... for i in range(0, len(primes), 10):
...     print(" ".join(f"{p:4d}" for p in primes[i:i+10]))
