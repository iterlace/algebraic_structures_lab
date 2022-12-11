def phi(n: int) -> int:
    """Euler's Totient Function"""

    phi = int(n > 1 and n)
    for p in range(2, int(n**0.5) + 1):
        if not n % p:
            phi -= phi // p
            while not n % p:
                n //= p

    # if n is > 1 it means it is prime
    if n > 1:
        phi -= phi // n
    return phi


def mu(n: int):
    """Mobius Function"""
    if n == 1:
        return 1

    # For a prime factor i check if i^2 is also a factor.
    p = 0
    for i in range(1, n + 1):
        if n % i == 0 and __is_prime(i):
            # Check if n is divisible by i^2
            if n % (i**2) == 0:
                return 0
            else:
                p = p + 1

    # All prime factors are contained only once. Return 1 if p is even else -1
    if p % 2 != 0:
        return -1
    return 1


def __is_prime(n):
    if n < 2:
        return False
    for i in range(2, n + 1):
        if i * i <= n and n % i == 0:
            return False
    return True
